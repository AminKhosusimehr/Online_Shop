import os
from celery import Celery


# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ShopProject.settings')

app = Celery('ShopProject')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=False)
def debug_task(self):
    print(f'Request: {self.request!r}')