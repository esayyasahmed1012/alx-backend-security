from django.core.management.base import BaseCommand, CommandError
from django.core.validators import validate_ipv46_address
from django.core.exceptions import ValidationError
from ip_tracking.models import BlockedIP

class Command(BaseCommand):
    help = 'Add an IP address to the BlockedIP blacklist'

    def add_arguments(self, parser):
        parser.add_argument('ip_address', type=str, help='The IP address to block')

    def handle(self, *args, **options):
        ip_address = options['ip_address']

        # Validate IP address
        try:
            validate_ipv46_address(ip_address)
        except ValidationError:
            raise CommandError(f"Invalid IP address: {ip_address}")

        # Check if IP is already blocked
        if BlockedIP.objects.filter(ip_address=ip_address).exists():
            self.stdout.write(self.style.WARNING(f"IP address {ip_address} is already blocked."))
            return

        # Add IP to BlockedIP
        BlockedIP.objects.create(ip_address=ip_address)
        self.stdout.write(self.style.SUCCESS(f"Successfully blocked IP address: {ip_address}"))