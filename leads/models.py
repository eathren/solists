import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
# from . import services


from multiselectfield import MultiSelectField
# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Lead(models.Model):
    ordering = ['-created_at']
    user_author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="author",
    )
    salary_range = models.CharField(
        max_length=100, blank=True, help_text="Ex: $70,000 - $80,000", verbose_name="Annual Salary")
    developer = models.BooleanField(default=False)
    designer = models.BooleanField(default=False)
    description = RichTextField()
    how_to_apply= RichTextField(verbose_name="How To Apply?", blank=True)
    country = CountryField(
        blank_label='(Select Country)', blank=True, help_text="If the job is constrained to one country, please select it" )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.CharField(max_length=100, blank=True, default='')
    logo = models.ImageField(upload_to='logos/', blank=True)
    author = models.CharField(max_length=200, blank=True)
    contact_info = models.CharField(max_length=100, blank=True, help_text="This email is public. The apply button defaults to it if you do not supply an Apply Url")
    application_link = models.CharField(max_length=100, blank=True, verbose_name="Application URL", help_text="Ex: https://www.yoursite.com/apply")
    status = models.IntegerField(choices=STATUS, default=1)

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
        choices=EXPERIENCE_LEVEL, max_choices=4, max_length=200, blank=True, help_text="You can select more than one")

    ROLE_TYPE = (
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('DevOps', 'DevOps'),

    )
    role = MultiSelectField(
        choices=ROLE_TYPE, max_choices=2, max_length=200, blank=True, verbose_name="Role Type", help_text="This will dictate who gets shown what posts, as well as in searches")

    REMOTE_TYPE = (
        ('Remote', 'Remote'),
        ('Part-Remote', 'Part-Remote'),
        ('Non-Remote', 'Non-Remote'),

    )
    remote = MultiSelectField(
        choices=REMOTE_TYPE, max_choices=3, max_length=200, blank=True, default='Remote')

    LEAD_SKILLS = (
        ('AGILE', 'Agile'),
        ('AWS', 'AWS'),
        ('ANGULAR', 'AngularJS'),
        ('ANGULARJS', 'AngularJS'),
        ('ANGULAR.JS', 'AngularJS'),
        ('ANSIBLE', 'Ansible'),
        ('AI', 'AI'),
        ('APACHE', 'Apache'),
        ('ARTIFICIAL INTELLIGENCE', 'Artificial Intelligence'),
        ('BACKBONE.JS', 'Backbone.js'),
        ('BACKEND', 'Backend'),
        ('BIG DATA', 'Big Data'),
        ('BLOCKCHAIN', 'Blockchain'),
        ('OBJECTIVE-C', 'Objective-C'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('CELERY', 'Celery'),
        ('COUCHDB', 'CouchDB'),
        ('CSS', 'CSS'),        
        ('CSS3', 'CSS3'),
        ('CRYPTOCURRENCY', 'Cryptocurrency'),
        ('DEVOPS', 'DevOps'),
        ('DJANGO', 'Django'),
        ('DJANGO REST FRAMEWORK', 'Django Rest Framework'),
        ('DOCKER', 'Docker'),
        ('ELASTICSEARCH', 'Elasticsearch'),
        ('EMBER.JS', 'Ember.js'),
        ('EXPRESS', 'Express'),
        ('FABRIC', 'Fabric'),
        ('FLASK', 'Flask'),
        ('FRONTEND', 'Frontend'),
        ('FULLSTACK', 'Fullstack'),
        ('GATSBY.JS', 'Gatsby.js'),
        ('GIT', 'Git'),
        ('GO', 'Go'),
        ('GOLANG', 'Go'),
        ('GOOGLE CLOUD PLATFORM', 'Google Cloud Platform'),
        ('GRAPHQL', 'GraphQL'),
        ('GUNICORN', 'Gunicorn'),
        ('HADOOP', 'Hadoop'),
        ('HEROKU', 'Heroku'),
        ('HTML','HTML'),
        ('HTML5', 'HTML5'),
        ('HUGO', 'Hugo'),
        ('JAVA', 'Java'),
        ('JAVASCRIPT', 'JavaScript'),
        ('JENKINS', 'Jenkins'),
        ('JQUERY', 'jQuery'),
        ('KAFKA', 'Kafka'),
        ('KOTLIN', 'Kotlin'),
        ('KUBERNETES', 'Kubernetes'),
        ('LINUX', 'Linux'),
        ('MACHINE LEARNING', 'Machine Learning'),
        ('MATPLOTLIB', 'Matplotlib'),
        ('MEMCACHED', 'Memcached'),
        ('MERCURIAL', 'Mercurial'),
        ('MICROSOFT AZURE', 'Microsoft Azure'),
        ('MONGODB', 'MongoDB'),
        ('MYSQL', 'MySQL'),
        ('NATURAL LANGUAGE PROCESSING', 'Natural Language Processing'),
        ('.NET', '.NET'),
        ('NGINX', 'Nginx'),
        ('NODE', 'Node'),
        ('NODEJS', 'Node'),
        ('NODE.JS', 'Node'),
        ('NUMPY', 'NumPy'),
        ('PANDAS', 'Pandas'),
        ('POSTEGRESQL', 'PostegreSQL'),
        ('PYQT', 'PyQt'),
        ('PYRAMID', 'Pyramid'),
        ('PYSIDE', 'PySide'),
        ('PYTHON', 'Python'),
        ('PYTORCH', 'PyTorch'),
        ('RABBITMQ', 'RabbitMQ'),
        ('REDIS', 'Redis'),
        ('REACT', 'React.js'),
        ('REACTJS', 'React.js'),
        ('REACT.JS', 'React.js'),
        ('REACT NATIVE', 'React Native'),
        ('REST', 'REST'),
        ('RUST', 'Rust'),
        ('SALTSTACK', 'SaltStack'),
        ('SAAS', 'Saas'),
        ('SASS', 'Sass'),
        ('SCALA', 'Scala'),
        ('SCIPY', 'SciPy'),
        ('SCRAPY', 'Scrapy'),
        ('SCRUM', 'Scrum'),
        ('SECURITY', 'Security'),
        ('SELENIUM', 'Selenium'),
        ('SOLR', 'Solr'),
        ('SPARK', 'Spark'),
        ('SQL', 'SQL'),
        ('SQLALCHEMY', 'SQLAlchemy'),
        ('SWIFT', 'Swift'),
        ('SVELTE', 'Svelte'),
        ('TENSORFLOW', 'TensorFlow'),
        ('TERRAFORM', 'Terraform'),
        ('TEST-DRIVEN DEVELOPMENT', 'Test-Driven Development'),
        ('TORNADO', 'Tornado'),
        ('TYPESCRIPT.JS', 'TypeScript'),
        ('TYPESCRIPTJS', 'TypeScript'),
        ('TYPESCRIPT', 'TypeScript'),
        ('UI', 'UI'),
        ('UWSGI', 'uWSGI'),
        ('UX', 'UX'),
        ('VAGRANT', 'Vagrant'),
        ('VIRTUALENV', 'Virtualenv'),
        ('VR', 'VR'),
        ('VISUALIZATION', 'Visualization'),
        ('VUE', 'Vue.js'),
        ('VUEJS', 'Vue.js'),
        ('VUE.JS', 'Vue.js'),
        ('WEB DEVELOPMENT', 'Web Development'),
        ('WEB SCRAPING', 'Web Scraping')
    )

    skills = MultiSelectField(
        choices=LEAD_SKILLS, max_choices=6, max_length=1000, blank=True, verbose_name="Skills (select up to 6)", help_text="Select up to six")

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index')
        ]

    def get_absolute_url(self):
        return "/leads/{}".format(self.id)
        #  return reverse('leads', args=[str(self.id)])

    def __str__(self):
        return self.title
    
