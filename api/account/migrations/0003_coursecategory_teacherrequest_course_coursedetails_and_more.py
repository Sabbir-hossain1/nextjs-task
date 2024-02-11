# Generated by Django 5.0.1 on 2024-02-08 11:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_category', models.CharField(choices=[('SSC_Academic_Course', 'SSC Academic Course'), ('HSC_Academic_Course', 'HSC Academic Course'), ('Diploma_Academic_Course', 'Diploma Academic Course'), ('University_Academic_Course', 'University Academic Course'), ('DUET_Admission_Course', 'DUET Admission Course'), ('Skill_Based_Development_Course', 'Skill Based Development Course')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number: ')),
                ('current_location', models.TextField(choices=[('in_dhaka', 'Inside Dhaka'), ('in_gazipur', 'Inside Gazipur'), ('others', 'Others')], verbose_name='Current Location')),
                ('current_address', models.TextField()),
                ('university_name', models.CharField(max_length=100, verbose_name='University')),
                ('department', models.CharField(max_length=50, verbose_name='Department')),
                ('current_education_year', models.CharField(choices=[('1st_year', '1st Year'), ('2nd_year', '2nd Year'), ('3rd_year', '3rd Year'), ('4th_year', '4th Year'), ('graduated', 'Graduated'), ('post_graduation_running', 'Enrolled In Postgraduation studies')], max_length=50, verbose_name='Current Education Year:')),
                ('fb_link', models.CharField(max_length=300, verbose_name='Facebook Link')),
                ('interested_teaching_area', models.CharField(choices=[('polytechnic', 'Polytechnic'), ('class_6_to_12', 'Class 6-12'), ('duet_admission', 'DUET Admission')], max_length=50, verbose_name='Interested Teaching Segments')),
                ('interested_subjects', models.CharField(choices=[('non_department', 'Non Department'), ('department', 'Department')], max_length=50, verbose_name='Interested Subjects')),
                ('link_previous_class', models.CharField(max_length=200, verbose_name='Previous Class Link Live or Recorded')),
                ('experience', models.IntegerField()),
                ('describe_your_experience', models.TextField()),
                ('cv', models.FileField(max_length=150, upload_to='teacher_cv')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.coursecategory')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_student', models.IntegerField()),
                ('duration', models.DurationField()),
                ('videos', models.IntegerField()),
                ('quiz', models.IntegerField()),
                ('classes', models.IntegerField()),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('short_message', models.TextField()),
                ('course', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.course')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='EnrollmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('completed', 'COMPLETED'), ('running', 'RUNNING')], max_length=150)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.studentmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(to='account.teachermodel'),
        ),
    ]
