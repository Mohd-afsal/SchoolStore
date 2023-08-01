from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    url = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class Courses(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


class Purpose(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    class Meta:
        ordering = ['name']
        verbose_name = 'purpose'
        verbose_name_plural = 'purposes'

    def __str__(self):
        return self.name


class Materials(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    class Meta:
        ordering = ['name']
        verbose_name = 'material'
        verbose_name_plural = 'materials'

    def __str__(self):
        return self.name


class Detail(models.Model):
    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    ]

    name = models.CharField(max_length=124)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128, default=None)
    phone_number = models.PositiveBigIntegerField()
    mail = models.EmailField(max_length=254,)
    address = models.TextField(max_length=250)
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, blank=True, null=True)
    materials = models.CharField(max_length=128, default=None)

    def __str__(self):
        return self.name
