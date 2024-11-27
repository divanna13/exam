DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=[('completed', 'Выполнено'), ('in_progress', 'В процессе')])
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


python manage.py makemigrations tasks
python manage.py migrate









