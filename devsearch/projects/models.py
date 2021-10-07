from django.db import models
import uuid
from users.models import Profile


class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL) # ManyToOne
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    # 'Tag' because the model is created down otherwise with Tag
    tags = models.ManyToManyField('Tag', blank=True)  # ManyToMany
    vote_total = models.IntegerField(null=True, default=0, blank=True)
    vote_ratio = models.IntegerField(null=True, default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # By defalt django manage the id like integer we are going to use other kind
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote'),
    )
    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # ManyToOne
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)

    def __str__(self):
        return self.name