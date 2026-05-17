from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


@receiver(user_logged_in, sender=User, dispatch_uid="login_success_signal")
def login_success (sender , request,user, **kwargs):
    print("Login Success--------------")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print(f"kwargs: {kwargs}")


# user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out, sender=User, dispatch_uid="logout_success_signal")
def logout_success (sender, request, user, **kwargs):
    print("Logout Success--------------")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print(f"kwargs: {kwargs}")
  

# user_logged_out.connect(logout_success,sender=User)

@receiver(user_login_failed, sender=User, dispatch_uid="login_failed_signal")
def login_failed (sender, request, credentials, **kwargs):
    print("Login Failed--------------")
    print("sender:", sender)
    print("request:", request)
    print("credentials:", credentials)
    print(f"kwargs: {kwargs}")