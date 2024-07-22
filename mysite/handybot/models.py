from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=100, default="unknown project")
    project_type = models.CharField(max_length=200)
    def __str__(self):
        return self.project_name
    def is_named(self):
        return self.project_name != "unknown project"

class Tool(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tool_name = models.CharField(max_length=100, default="unknown tool")
    price = models.FloatField(default=0)
    link = models.CharField(max_length=1000)
    def __str__(self):
        return self.tool_name