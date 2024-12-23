# Generated by Django 5.1.2 on 2024-10-27 18:07

import base.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_image', models.TextField()),
                ('course_description', models.TextField()),
                ('course_category', models.TextField(blank=True, null=True)),
                ('time_to_complete', models.CharField(max_length=100)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg', upload_to='profile_pics')),
                ('subject', models.CharField(max_length=100)),
                ('verified', models.BooleanField(default=False)),
                ('rating', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('likes', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('time_to_complete', models.IntegerField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='base.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_tutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='base.tutor'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', base.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='tutor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.user'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='profile_pics/Default_pfp.svg', upload_to='profile_pics')),
                ('profile_views', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)])),
                ('bio', models.TextField(blank=True, null=True)),
                ('preferred_name', models.CharField(blank=True, max_length=20, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('enrolled_courses', models.ManyToManyField(related_name='enrolled_students', to='base.course')),
                ('saved_courses', models.ManyToManyField(related_name='saved_students', to='base.course')),
                ('socials', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.socials')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.user')),
            ],
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('course_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.coursematerial')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='base.student')),
            ],
        ),
    ]
