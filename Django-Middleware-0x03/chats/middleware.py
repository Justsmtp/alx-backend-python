# chats/middleware.py

import logging
from datetime import datetime, timedelta

from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Set up logging to write to requests.log
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(message)s'
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)

        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        # Restrict access outside 6PM (18) to 9PM (21)
        if current_hour < 18 or current_hour >= 21:
            return HttpResponseForbidden("Chat access is restricted during this time.")
        return self.get_response(request)

ip_request_log = {}

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.limit = 5  # messages allowed per window
        self.window = timedelta(minutes=1)

    def __call__(self, request):
        # Only apply to POST requests (messages)
        if request.method == "POST" and "/api/conversations/" in request.path:
            ip = self.get_client_ip(request)
            now = datetime.now()

            # Initialize log for this IP
            if ip not in ip_request_log:
                ip_request_log[ip] = []

            # Remove timestamps older than 1 minute
            ip_request_log[ip] = [
                ts for ts in ip_request_log[ip] if now - ts < self.window
            ]

            # Check if limit exceeded
            if len(ip_request_log[ip]) >= self.limit:
                return HttpResponseForbidden(
                    "Message limit exceeded. Try again after 1 minute."
                )

            # Log the new request timestamp
            ip_request_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        """Extract client IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only enforce on specific paths, e.g., admin actions
        if request.path.startswith("/api/conversations/"):  
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Authentication required.")
            
            # Example: Check user role (assuming you have a 'role' field on User)
            user_role = getattr(request.user, "role", None)
            
            # Only allow admin or moderator
            if user_role not in ["admin", "moderator"]:
                return HttpResponseForbidden("You do not have permission to perform this action.")
        
        return self.get_response(request)