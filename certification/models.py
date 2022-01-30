from django.db import models
from users.models import User
from online_course.models import OnlineCourse
from course.models import Course



class Certificate(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    online_course = models.ForeignKey(OnlineCourse, on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    course_title_fani = models.CharField(max_length=50)
    code_fani = models.CharField(max_length=10,default='1234567890')
    code_academy = models.CharField(max_length=10,default='1234567890')
    certificate_image_academy = models.ImageField(upload_to='store_image/certificate_academy_image/', null=True, blank=True)
    certificate_image_fani = models.ImageField(upload_to='store_image/certificate_fani_image/', null=True, blank=True)
    fani_score = models.PositiveIntegerField(default='100')
    academy_score = models.PositiveIntegerField(default='100')


    def __str__(self):
        return self.user.first_name+' '+self.user.last_name+'   '+self.user.username
