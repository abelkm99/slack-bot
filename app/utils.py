from datetime import datetime, time, timedelta, date
date_format = "%Y-%m-%d %H:%M:%S"


def parse_date_time(date_string, date_format=date_format):
    if isinstance(date_string, str):
        return datetime.strptime(date_string, date_format)
    return datetime.strftime(date_string, date_format)


def get_day_range(start_date, end_date):
    """Returns the start and end datetime objects for a date range.

    Args:
        start_date (date): The start date of the range.
        end_date (date): The end date of the range.

    Returns:
        tuple: A tuple of two datetime objects representing the start and end of the day for each date.
    """

    start_of_day = datetime.combine(start_date, time.min)
    end_of_day = datetime.combine(end_date, time.max)
    return start_of_day, end_of_day


def convert_seconds(seconds):
    # Use time.gmtime() to convert seconds to a struct_time object
    t = time.gmtime(seconds)
    # Use time.strftime() to format the struct_time object as HH:MM:SS
    return time.strftime("%H:%M:%S", t)


FAKE_TASKS = ["Implement new user authentication flow",  "Optimize database queries for faster performance",  "Refactor legacy codebase to improve maintainability",  "Integrate with third-party API for geolocation data",  "Create automated testing suite for frontend code",  "Resolve issues with mobile responsiveness on product pages",  "Improve accessibility for users with disabilities",  "Implement multi-factor authentication for improved security",  "Add support for two-factor authentication in mobile app",  "Improve error handling and logging for better debugging",  "Create documentation for API endpoints and usage",  "Implement search functionality for internal knowledge base",  "Improve performance of image upload feature",  "Upgrade backend server to newer version of Node.js",  "Implement responsive design for email templates",
              "Integrate with payment gateway for online transactions",  "Create custom reporting dashboard for analytics data",  "Fix bug causing data loss in user profile updates",  "Improve onboarding process for new users",  "Implement role-based access control for admin users",  "Optimize page load times for better user experience",  "Add support for OAuth2 authentication protocol",  "Create automated deployment pipeline using CI/CD tools",  "Resolve issue causing intermittent server crashes",  "Integrate with social media platforms for sharing functionality",  "Improve caching mechanisms for faster API responses",  "Implement email notification system for user actions",  "Add support for localization and internationalization",  "Upgrade frontend framework to latest version of React",  "Improve handling of high traffic periods on website"]


def convert_time_to_string(checkIn_time):
    dt = datetime.strptime(str(checkIn_time), "%Y-%m-%d %H:%M:%S")
    formatted_dt = dt.strftime("%A, %b %d %Y, %I:%M%p")
    return formatted_dt
  # Use time.gmtime() to convert seconds to a struct_time object


FAKE_TASKS = ["Implement new user authentication flow",  "Optimize database queries for faster performance",  "Refactor legacy codebase to improve maintainability",  "Integrate with third-party API for geolocation data",  "Create automated testing suite for frontend code",  "Resolve issues with mobile responsiveness on product pages",  "Improve accessibility for users with disabilities",  "Implement multi-factor authentication for improved security",  "Add support for two-factor authentication in mobile app",  "Improve error handling and logging for better debugging",  "Create documentation for API endpoints and usage",  "Implement search functionality for internal knowledge base",  "Improve performance of image upload feature",  "Upgrade backend server to newer version of Node.js",  "Implement responsive design for email templates",
              "Integrate with payment gateway for online transactions",  "Create custom reporting dashboard for analytics data",  "Fix bug causing data loss in user profile updates",  "Improve onboarding process for new users",  "Implement role-based access control for admin users",  "Optimize page load times for better user experience",  "Add support for OAuth2 authentication protocol",  "Create automated deployment pipeline using CI/CD tools",  "Resolve issue causing intermittent server crashes",  "Integrate with social media platforms for sharing functionality",  "Improve caching mechanisms for faster API responses",  "Implement email notification system for user actions",  "Add support for localization and internationalization",  "Upgrade frontend framework to latest version of React",  "Improve handling of high traffic periods on website"]
