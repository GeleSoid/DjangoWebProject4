from tabnanny import verbose
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

class Blog(models.Model):

    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Author")

    title = models.CharField(max_length = 100, unique_for_date= "posted", verbose_name= "Title")

    description = models.TextField(verbose_name = "Summary")

    content = models.TextField(verbose_name = "Full content")

    posted = models.DateTimeField(default = datetime.now(), db_index= True, verbose_name = "To publish")

    image = models.FileField(default='teep.jpg', verbose_name= "The path to the picture")

    def get_absolute_url(self):
        return reverse("blogpost", args = [str(self.id)])

    def __str__(self):
        return self.title

    class Meta:

        db_table = "Posts"

        ordering = ["-posted"]

        verbose_name = "blog article"

        verbose_name_plural = "blog article"

admin.site.register(Blog)

class Comment(models.Model):

    text = models.TextField(verbose_name= "Comment text")

    date = models.DateTimeField(default= datetime.now(), db_index= True, verbose_name= "Date of the comment")

    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name= "The author of the comment")

    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name= "Comment Article")

    def __str__(self):
        return 'Comments %d %s to %s' % (self.id, self.author, self.post)

    class Meta:

        db_table = "Comment"

        ordering = ["-date"]

        verbose_name = "Comments on the blog article"

        verbose_name_plural = "Comments on blog articles"

admin.site.register(Comment)

