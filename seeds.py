from cohorts_and_students.models import Cohort, Student

Cohort.objects.all().delete()
Student.objects.all().delete()

bravo = Cohort(cohort_name='Bravo', start_date='1/4/17', end_date='5/1/17')
bravo.save()

charlie = Cohort(cohort_name='Charlie', start_date='5/27/17', end_date='8/10/17')
charlie.save()

student_1 = Student(cohort=bravo, first_name='Conlin', last_name='M')
student_1.save()

student_2 = Student(cohort=bravo, first_name='Scott', last_name='P')
student_2.save()

student_3 = Student(cohort=bravo, first_name='Mike', last_name='L')
student_3.save()

student_4 = Student(cohort=bravo, first_name='Jin', last_name='C')
student_4.save()

student_5 = Student(cohort=charlie, first_name='Darnell', last_name='G')
student_5.save()

student_6 = Student(cohort=charlie, first_name='Arthur', last_name='M')
student_6.save()