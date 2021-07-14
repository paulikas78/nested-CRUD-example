from django.db import models

class Cohort(models.Model):
    cohort_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200) # in a real example, we'd want this to be a date field
    end_date = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id}, cohort_name={self.cohort_name}, start_date={self.start_date}, end_date={self.end_date}"

class Student(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id}, first_name={self.first_name}, last_name={self.last_name}"
    

