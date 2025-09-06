from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django_ip_geolocation.decorators import with_ip_geolocation
from django.http import HttpResponseForbidden
from .models import RequestLog, BlockedIP

class IPTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Get IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip_address = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

        # Check if IP is blocked
        if BlockedIP.objects.filter(ip_address=ip_address).exists():
            return HttpResponseForbidden("Access denied: Your IP address is blocked.")

        # Get path
        path = request.path

        # Check cache for geolocation data
        cache_key = f"geolocation_{ip_address}"
        geolocation_data = cache.get(cache_key)

        if not geolocation_data:
            # Use django-ipgeolocation to fetch geolocation data
            with_ip_geolocation(request)
            location = getattr(request, 'geolocation', None)
            if location:
                geolocation_data = {
                    'country': location.get('country_name'),
                    'city': location.get('city')
                }
                # Cache for 24 hours (24 * 60 * 60 seconds)
                cache.set(cache_key, geolocation_data, timeout=24 * 60 * 60)
            else:
                geolocation_data = {'country': None, 'city': None}

        # Create log entry
        RequestLog.objects.create(
            ip_address=ip_address,
            path=path,
            country=geolocation_data['country'],
            city=geolocation_data['city']
        )

        return None