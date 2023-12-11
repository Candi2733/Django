from django.core.mail import send_mail
from basic_features.settings import EMAIL_HOST_USER
from .models import User
import logging

logger = logging.getLogger(__name__)

def scheduled_ad():
    logger.info("cron job was called")
    try:
        users = User.objects.all()
        for user in users:
            send_mail(
                "Sign Up Successful",
                "Welcome New User, your sign up has been successfully completed.",
                EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            logger.info("cron job was called gtjk")
        return 1
    except Exception as e:
        logger.info(str(e))
        return str(e)