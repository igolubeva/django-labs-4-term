from celery import shared_task
from orders.utils import send_report


@shared_task
def send_email_report():
    send_report()
