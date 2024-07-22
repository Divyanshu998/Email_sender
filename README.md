# Email_sender
#using Django framework
#expalnation of the code:-
#from setting import student: Imports the student module or variable from a local setting module. This line seems to be incorrect as it should likely be settings instead of setting.
#import time: Imports the time module, which provides various time-related functions.
#from django.core.mail import send_mail: Imports the send_mail function from Django's email module.
#from django.conf import settings: Imports the settings object from Django's configuration, which contains various settings for the Django project.
#run_this_function(): A simple function that prints messages to the console and pauses for 2 seconds.
#print("function started"): Prints a message indicating the function has started.
#print("function started..."): Prints another message indicating the function is still running.
#time.sleep(2): Pauses the execution for 2 seconds.
#print("function executed"): Prints a message indicating the function has finished executing.
#send_mail_to_client(): A function to send an email using Django's email system.
#subject: The subject of the email.
#message: The body of the email.
#from_email: The sender's email address, retrieved from Django settings (settings.EMAIL_HOST_USER).
#recipient_list: A list containing the recipient's email address.
#send_mail(subject, message, from_email, recipient_list): Sends the email with the specified subject, message, sender, and recipient.
