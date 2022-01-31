from django.db import models
import datetime
from django.contrib.auth.models import User

class OnlineCourse(models.Model):
    class CourseLevel(models.TextChoices):
        BEGINNER = 'مبتدی'
        INTERMEDIATE = 'متوسط'
        PROFFESSIONAL = 'حرفه ای'

    class CourseStatus(models.TextChoices):
        PRE_REGISTRATION = 'پیش ثبت نام'
        BEING_HELD = 'درحال برگزاری'
        WAS_HELD = 'برگزار شده'
    # MEDIA_CHOICES = [
    #     ('Audio', (
    #         ('vinyl', 'Vinyl'),
    #         ('cd', 'CD'),
    #     )
    #      ),
    #     ('Video', (
    #         ('vhs', 'VHS Tape'),
    #         ('dvd', 'DVD'),
    #     )
    #      ),
    #     ('unknown', 'Unknown'),
    # ]
    online_course_name = models.CharField(max_length=100, default='')
    online_course_price = models.IntegerField(default=1)
    # online_course_teacher = models.ForeignKey()
    online_course_description = models.TextField(default='')
    online_course_duration = models.DurationField(default=datetime.timedelta(days=2).total_seconds())
    online_course_date = models.DateTimeField(auto_now_add=True)
    online_course_image = models.ImageField(upload_to='images/', default='')
    number_of_videos = models.IntegerField(default=1)
    online_course_level = models.CharField(max_length=100, choices=CourseLevel.choices, default=CourseLevel.BEGINNER)
    online_course_status = models.CharField(max_length=100, choices=CourseStatus.choices, default=CourseStatus.BEING_HELD)

    def __str__(self):
        return self.online_course_name

    # def convert(self):
    #
    #     time = datetime.timedelta().total_seconds()
    #     duration = time // 3600
    #     self.online_course_duration.default = duration
    #     return self.online_course_duration





class Chapter(models.Model):
    chapter_order = models.IntegerField(default=1)
    chapter_title = models.CharField(max_length=100 ,default='')
    chapter_description = models.TextField(default='')
    chapter_duration = models.TimeField(default=0)
    number_of_episode = models.IntegerField(default=1)
    chapter_related_to = models.ForeignKey(OnlineCourse, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.chapter_title

class Episode(models.Model):
    episode_order = models.IntegerField(default=1)
    episode_title = models.CharField(max_length=100 ,default='')
    episode_description = models.TextField(default='')
    episode_duration = models.TimeField(default=0)
    episode_related_to = models.ManyToManyField(Chapter)
    episode_file = models.FileField(upload_to='files/', default='')

    def __str__(self):
        return self.episode_title

