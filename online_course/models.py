from django.db import models
import datetime

from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save


class OnlineCourseCategory(models.Model):
    online_course_category = models.CharField(max_length=100)

    def __str__(self):
        return self.online_course_category

class OnlineCourse(models.Model):

    class CourseLevel(models.TextChoices):
        BEGINNER = 'مبتدی'
        INTERMEDIATE = 'متوسط'
        PROFFESSIONAL = 'حرفه ای'

    class CourseStatus(models.TextChoices):
        PRE_REGISTRATION = 'پیش ثبت نام'
        RUNNING = 'در حال برگزاری'
        DONE = 'برگزار شده'

    online_course_title = models.CharField(max_length=100, default='')
    online_course_category = models.ForeignKey(OnlineCourseCategory, on_delete=models.CASCADE, default=1)
    online_course_related_category = models.ManyToManyField(OnlineCourseCategory, related_name='online_rel_cat')
    online_course_price = models.IntegerField(default=1)
    online_course_discount_percent = models.IntegerField(default=0)
    online_course_discounted_price = models.IntegerField(default=1)
    online_course_teacher = models.ForeignKey("users.User",on_delete=models.PROTECT)
    online_course_description = models.TextField(default='')
    online_course_duration = models.DurationField(default=datetime.timedelta(days=2).total_seconds())
    #online_course_date = models.DateTimeField(auto_now_add=True)
    online_course_image = models.ImageField(upload_to='images/', default='')
    number_of_videos = models.IntegerField(default=1)
    online_course_level = models.CharField(max_length=100, choices=CourseLevel.choices, default=CourseLevel.BEGINNER)
    online_course_status = models.CharField(max_length=100, choices=CourseStatus.choices,default=CourseStatus.RUNNING)
    online_course_start_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.online_course_title

@receiver(pre_save,sender=OnlineCourse)
def calculate_online_course_discounted_price(sender,**kwargs):
    online_course = kwargs['instance']
    online_course.online_course_discounted_price = float(online_course.online_course_price)-(float(online_course.online_course_price)*float(online_course.online_course_discount_percent)/100)

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
    chapter_duration = models.TimeField(default='')
    number_of_episode = models.IntegerField(default=1)
    related_to_online_course = models.ForeignKey(OnlineCourse, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.chapter_title

class Episode(models.Model):
    episode_order = models.IntegerField(default=1)
    episode_title = models.CharField(max_length=100 ,default='')
    episode_description = models.TextField(default='')
    episode_duration = models.TimeField(default='')
    related_to_chapter = models.ManyToManyField(Chapter)

    def __str__(self):
        return self.episode_title