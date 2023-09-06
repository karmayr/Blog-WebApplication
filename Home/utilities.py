from django.template.defaultfilters import slugify
import string,random
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def generate_string(n):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    return res

def create_slug(text):
    new_slug = slugify(text)
    from .models import Blog
    if Blog.objects.filter(slug = new_slug).first():
        return create_slug(text + generate_string(7))
    return new_slug

def send_otp(token,email):
    
    subject = "Account Verification"
    message = f'Press The Link to Verify the account http://127.0.0.1:8000/verify/{token} '
    email_from = EMAIL_HOST_USER 
    send_to = [email]

    send_mail(subject,message,email_from,send_to)
    return True