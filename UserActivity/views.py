from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from UserActivity.models import UsersActivity, UserProfile

def try_or(fn, default, *args, **kwargs):
    """
    Usage: try_or(lambda: request_user.email, None, *args, **kwargs)
    """
    try:
        return fn(*args, **kwargs)
    except Exception:
        return default


class UserActivityViewset(viewsets.ViewSet):
    """
    (GET) Api for all User Activities.
    """
    permission_classes = (AllowAny, )

    def list(self, request):
        response = dict()
        user_dict = dict()
        all_users = UserProfile.objects.all()
        response["ok"] = True
        response["members"] = list()
        for every in all_users:
            same_user = UserProfile.objects.filter(id=every.id)
            if same_user:
                user_dict = {
                        "id": same_user[0].id,
                        "real_name": same_user[0].full_name,
                        "tz": same_user[0].time_zone,
                    }
                user_dict['activity_periods'] = list()
                for user in same_user:
                    user_activity = {
                        "start_time": user.start_time,
                        "end_time": user.end_time
                    }
                user_dict['activity_periods'].append(user_activity)
            response['members'].append(user_dict)
        return Response(response)