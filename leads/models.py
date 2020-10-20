import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField

from multiselectfield import MultiSelectField
# Create your models here.


class Lead(models.Model):
    ordering = ['created_at']
    user_author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="author"
    )
    developer = models.BooleanField(default=False)
    designer = models.BooleanField(default=False)
    description = RichTextField()
    country = CountryField(blank_label='(select country)')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.CharField(max_length=100, blank=True, default='')
    logo = models.ImageField(upload_to='logos/', blank=True)
    author = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=100, blank=True)
    application_link = models.CharField(max_length=100, blank=True)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)

    EMPLOYMENT_TYPE = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    )
    job_type = MultiSelectField(
        choices=EMPLOYMENT_TYPE, max_choices=4, max_length=200, blank=True)

    EXPERIENCE_LEVEL = (
        ('Junior', 'Junior'),
        ('Intermediate', 'Intermediate'),
        ('Senior', 'Senior'),
        ('Intern', 'Intern'),
    )
    experience = MultiSelectField(
        choices=EXPERIENCE_LEVEL, max_choices=4, max_length=200, blank=True)

    ROLE_TYPE = (
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),

    )
    role = MultiSelectField(
        choices=ROLE_TYPE, max_choices=2, max_length=200, blank=True)

    REMOTE_TYPE = (
        ('Remote', 'Remote'),
        ('Part-Remote', 'Part-Remote'),
        ('Non-Remote', 'Non-Remote'),

    )
    remote = MultiSelectField(
        choices=REMOTE_TYPE, max_choices=3, max_length=200, blank=True)

    LEAD_SKILLS = (
        ('Agile', 'Agile'),
        ('Amazon Web Services', 'Amazon Web Services'),
        ('AngularJS', 'AngularJS'),
        ('Ansible', 'Ansible'),
        ('AI', 'AI'),
        ('Apache', 'Apache'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Backbone.js', 'Backbone.js'),
        ('Backend Development', 'Backend Development'),
        ('Big Data', 'Big Data'),
        ('Blockchain', 'Blockchain'),
        ('Objective-C', 'Objective-C'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('Celery', 'Celery'),
        ('CouchDB', 'CouchDB'),
        ('CSS3', 'CSS3'),
        ('Cryptocurrency', 'Cryptocurrency'),
        ('DevOps', 'DevOps'),
        ('Docker', 'Docker'),
        ('Django ', 'Django '),
        ('Django Rest Framework', 'Django Rest Framework'),
        ('Docker', 'Docker'),
        ('Elasticsearch', 'Elasticsearch'),
        ('Ember.js', 'Ember.js'),
        ('Fabric', 'Fabric'),
        ('Flask', 'Flask'),
        ('Frontend Development', 'Frontend Development'),
        ('Fullstack Development', 'Fullstack Development'),
        ('Gatsby.js', 'Gatsby.js'),
        ('Git', 'Git'),
        ('Google Cloud Platform', 'Google Cloud Platform'),
        ('GraphQL', 'GraphQL'),
        ('Gunicorn', 'Gunicorn'),
        ('Hadoop', 'Hadoop'),
        ('Heroku', 'Heroku'),
        ('Hugo', 'Hugo'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
        ('Jenkins', 'Jenkins'),
        ('jQuery', 'jQuery'),
        ('Kafka', 'Kafka'),
        ('Kotlin', 'Kotlin'),
        ('Kubernetes', 'Kubernetes'),
        ('Linux', 'Linux'),
        ('Machine Learning', 'Machine Learning'),
        ('Matplotlib', 'Matplotlib'),
        ('Memcached', 'Memcached'),
        ('Mercurial', 'Mercurial'),
        ('Microsoft Azure', 'Microsoft Azure'),
        ('MongoDB', 'MongoDB'),
        ('Natural Language Processing', 'Natural Language Processing'),
        ('.NET', '.NET'),
        ('Nginx', 'Nginx'),
        ('NumPy', 'NumPy'),
        ('Pandas', 'Pandas'),
        ('PostegreSQL', 'PostegreSQL'),
        ('PyQt', 'PyQt'),
        ('Pyramid', 'Pyramid'),
        ('PySide', 'PySide'),
        ('Python', 'Python'),
        ('PyTorch', 'PyTorch'),
        ('RabbitMQ', 'RabbitMQ'),
        ('Redis', 'Redis'),
        ('React.js', 'React.js'),
        ('React Native', 'React Native'),
        ('REST', 'REST'),
        ('SaltStack', 'SaltStack'),
        ('Sass', 'Sass'),
        ('Scala', 'Scala'),
        ('SciPy', 'SciPy'),
        ('Scrapy', 'Scrapy'),
        ('Scrum', 'Scrum'),
        ('Security', 'Security'),
        ('Selenium', 'Selenium'),
        ('Solr', 'Solr'),
        ('Spark', 'Spark'),
        ('SQL', 'SQL'),
        ('SQLAlchemy', 'SQLAlchemy'),
        ('Swift', 'Swift'),
        ('TensorFlow', 'TensorFlow'),
        ('Terraform', 'Terraform'),
        ('Test-Driven Development', 'Test-Driven Development'),
        ('Tornado', 'Tornado'),
        ('TypeScript', 'TypeScript'),
        ('UI', 'UI'),
        ('uWSGI', 'uWSGI'),
        ('UX', 'UX'),
        ('Vagrant', 'Vagrant'),
        ('Virtualenv', 'Virtualenv'),
        ('VR', 'VR'),
        ('Visualization', 'Visualization'),
        ('Vue.js', 'Vue.js'),
        ('Web Development', 'Web Development'),
        ('Web Scraping', 'Web Scraping'),

    )
    skills = MultiSelectField(
        choices=LEAD_SKILLS, max_choices=45, max_length=1000, blank=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index')
        ]

    def get_absolute_url(self):
        return "/leads/{}".format(self.id)
        #  return reverse('leads', args=[str(self.id)])

    def __str__(self):
        return self.title
