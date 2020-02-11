from django.db import models
from django.urls import reverse
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)
    limit = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    finished_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    def finish(self):
        self.finished_at = timezone.now()
        self.save()

    def restart(self):
        self.finished_at = None
        self.save()

    def get_absolute_url(self):
        return reverse('index')

class Idea(models.Model):
    idea = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey('box.Project', on_delete=models.CASCADE, related_name='ideas')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_list', kwargs={'pk': self.project.pk})

class Conclusion(models.Model):
    conclusion = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('box.Project', on_delete=models.CASCADE, related_name='conc')
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.conclusion

    def get_absolute_url(self):
        return reverse('project_list', kwargs={'pk': self.project.pk})