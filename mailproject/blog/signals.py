from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import CustomUser
from django.core.mail import send_mail



@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Site!'
        message = f'Hi {instance.username}, thank you for registering at our site.'
        from_email = 'sahanshrestha2000@gmail.com'
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list,fail_silently=False)
        print( f'Welcome email sent to {instance.username} ')


