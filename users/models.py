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
    published = models.BooleanField(default=False, help_text="Your profile will only show up in the developer or designer list if this is checked.")
    developer = models.BooleanField(default=False)
    designer = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    country = CountryField(blank_label='(select country)')
    job_title = models.CharField(max_length = 200, blank=True, )
    linkedin = models.CharField(max_length = 200, blank=True, )
    github = models.CharField(max_length = 200, blank=True, )
    website = models.CharField(max_length = 200, blank=True, )
    contact_email =  models.CharField(max_length = 200, blank=True, )
    allow_contact = models.BooleanField(default=False, help_text="If this is selected, your email will be available and displayed.")
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
        ('AWS', 'AWS'),
        ('AngularJS', 'AngularJS'),
        ('Ansible', 'Ansible'),
        ('AI', 'AI'),
        ('Apache', 'Apache'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Backbone.js', 'Backbone.js'),
        ('Backend', 'Backend'),
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
        ('Django', 'Django'),
        ('Django Rest Framework', 'Django Rest Framework'),
        ('Docker', 'Docker'),
        ('Elasticsearch', 'Elasticsearch'),
        ('Ember.js', 'Ember.js'),
        ('Express', 'Express'),
        ('Fabric', 'Fabric'),
        ('Flask', 'Flask'),
        ('Frontend', 'Frontend'),
        ('Fullstack', 'Fullstack'),
        ('Gatsby.js', 'Gatsby.js'),
        ('Git', 'Git'),
        ('Golang', 'Golang'),
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
        ('MySQL', 'MySQL'),
        ('Natural Language Processing', 'Natural Language Processing'),
        ('.NET', '.NET'),
        ('Nginx', 'Nginx'),
        ('Node', 'Node'),
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
        ('Rust', 'Rust'),
        ('SaltStack', 'SaltStack'),
        ('Saas', 'Saas'),
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

    def get_absolute_url(self):
        return "/developers/{}".format(self.id)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='user_id_index')
        ] 
