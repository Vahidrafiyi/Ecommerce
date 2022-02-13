from django.db import models

class ConsultationForm(models.Model):
    CONSULTATION_TYPE = [
        ('social media', 'شبکه های اجتماعی'),
        ('content production', 'تولید محتوا'),
        ('website development and designment', 'طراحی و پیاده سازی سایت'),
    ]
    MEETING_TYPE = [
        ('in person', 'حضوری'),
        ('online', 'آنلاین')
    ]
    HOW_TO_KNOW = [
        ('search in internet', 'سرج در اینترنت'),
        ('social media', 'شبکه اجتماعی'),
        ('introduced by friends', 'معرفی دوستان')
    ]
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    consultation_type = models.CharField(choices=CONSULTATION_TYPE, max_length=100)
    description = models.TextField()
    brand_name = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    meeting_type = models.CharField(choices=MEETING_TYPE, max_length=100)
    how_to_know = models.CharField(choices=HOW_TO_KNOW,max_length=100, default=HOW_TO_KNOW[1][1])
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name + " درخواست مشاوره داده است "