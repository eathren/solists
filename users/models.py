from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField

# Create your models here.


class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    published = models.BooleanField(default=False)
    developer = models.BooleanField(default=False)
    designer = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    country = CountryField(blank_label='(select country)')
    job_title = models.CharField(max_length = 200, blank=True, )
    linkedin = models.CharField(max_length = 200, blank=True, )
    github = models.CharField(max_length = 200, blank=True, )
    website = models.CharField(max_length = 200, blank=True, )
    contact_email =  models.CharField(max_length = 200, blank=True, )
    allow_contact = models.BooleanField(default=False)
    stackoverflow = models.CharField(max_length = 200, blank=True, )
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
            models.Index(fields=['id'], name='user_id_index')
        ]
