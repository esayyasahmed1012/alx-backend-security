# IP Tracking Django App

## Overview
The `IP Tracking` Django app provides middleware to log the IP address, timestamp, and path of every incoming HTTP request in a Django application. This app is designed for security auditing and monitoring, storing request metadata in a database for analysis.

This project resides in the `alx-backend-security` GitHub repository under the `ip_tracking` directory.

## Features
- Logs IP address, timestamp, and request path for all incoming HTTP requests.
- Stores data in a Django model (`RequestLog`) for easy querying.
- Handles IP addresses behind proxies using the `X-Forwarded-For` header.
- Seamlessly integrates with any Django project.


## Prerequisites
- Python 3.6+
- Django 3.0+
- Visual Studio Code with recommended extensions:
  - **Python** (by Microsoft): For Python language support, linting, and debugging.
  - **Django** (by Baptiste Darthenay): For Django template and syntax support.
  - **SQLite** (by alexcvzz, optional): For SQLite database inspection.
  - **GitLens** (by GitKraken): For enhanced Git integration.

### Notes
- **No Changes Needed**: The `models.py` and `middleware.py` files already include the requested geolocation enhancements and are compatible with the `BlockedIP` functionality.
- **API Key**: Ensure you have a valid API key for `django-ipgeolocation` and update `settings.py`.
- **Caching**: Use Redis or Memcached in production for better performance.
- **Privacy**: Ensure compliance with regulations (e.g., GDPR) when logging IPs and geolocation data.
- **Testing**: Simulate requests from blocked and non-blocked IPs to verify functionality.

If you need modifications (e.g., different caching duration, additional geolocation fields, or admin interface integration), please let me know!
