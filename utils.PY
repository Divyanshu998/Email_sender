from setting import student
import time
from django.core.mail import send_mail
from django.conf import settings



def run_this_function():
    print("function started")
    print("function started...")
    
    time.sleep(2)
    print("function executed")
    
    
def send_mail_to_client():
    subject = "this email if from django server"
    message = "this is a test email from django server"
    from_email = settings.EMAIL_HOST_USER 
    recipient_list = ["hurnobita3@gmail.com"]
    send_mail(subject , message , from_email , recipient_list)