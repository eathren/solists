# Generated by Django 3.1.2 on 2020-11-11 22:28

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0023_auto_20201107_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Agile', 'Agile'), ('AWS', 'AWS'), ('AngularJS', 'AngularJS'), ('Ansible', 'Ansible'), ('AI', 'AI'), ('Apache', 'Apache'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Backbone.js', 'Backbone.js'), ('Backend', 'Backend'), ('Big Data', 'Big Data'), ('Blockchain', 'Blockchain'), ('Objective-C', 'Objective-C'), ('C#', 'C#'), ('C++', 'C++'), ('Celery', 'Celery'), ('CouchDB', 'CouchDB'), ('CSS3', 'CSS3'), ('Cryptocurrency', 'Cryptocurrency'), ('DevOps', 'DevOps'), ('Django', 'Django'), ('Django Rest Framework', 'Django Rest Framework'), ('Docker', 'Docker'), ('Elasticsearch', 'Elasticsearch'), ('Ember.js', 'Ember.js'), ('Express', 'Express'), ('Fabric', 'Fabric'), ('Flask', 'Flask'), ('Frontend', 'Frontend'), ('Fullstack', 'Fullstack'), ('Gatsby.js', 'Gatsby.js'), ('Git', 'Git'), ('Golang', 'Golang'), ('Google Cloud Platform', 'Google Cloud Platform'), ('GraphQL', 'GraphQL'), ('Gunicorn', 'Gunicorn'), ('Hadoop', 'Hadoop'), ('Heroku', 'Heroku'), ('Hugo', 'Hugo'), ('Java', 'Java'), ('JavaScript', 'JavaScript'), ('Jenkins', 'Jenkins'), ('jQuery', 'jQuery'), ('Kafka', 'Kafka'), ('Kotlin', 'Kotlin'), ('Kubernetes', 'Kubernetes'), ('Linux', 'Linux'), ('Machine Learning', 'Machine Learning'), ('Matplotlib', 'Matplotlib'), ('Memcached', 'Memcached'), ('Mercurial', 'Mercurial'), ('Microsoft Azure', 'Microsoft Azure'), ('MongoDB', 'MongoDB'), ('MySQL', 'MySQL'), ('Natural Language Processing', 'Natural Language Processing'), ('.NET', '.NET'), ('Nginx', 'Nginx'), ('Node', 'Node'), ('NumPy', 'NumPy'), ('Pandas', 'Pandas'), ('PostegreSQL', 'PostegreSQL'), ('PyQt', 'PyQt'), ('Pyramid', 'Pyramid'), ('PySide', 'PySide'), ('Python', 'Python'), ('PyTorch', 'PyTorch'), ('RabbitMQ', 'RabbitMQ'), ('Redis', 'Redis'), ('React.js', 'React.js'), ('React Native', 'React Native'), ('REST', 'REST'), ('Rust', 'Rust'), ('SaltStack', 'SaltStack'), ('Saas', 'Saas'), ('Sass', 'Sass'), ('Scala', 'Scala'), ('SciPy', 'SciPy'), ('Scrapy', 'Scrapy'), ('Scrum', 'Scrum'), ('Security', 'Security'), ('Selenium', 'Selenium'), ('Solr', 'Solr'), ('Spark', 'Spark'), ('SQL', 'SQL'), ('SQLAlchemy', 'SQLAlchemy'), ('Swift', 'Swift'), ('TensorFlow', 'TensorFlow'), ('Terraform', 'Terraform'), ('Test-Driven Development', 'Test-Driven Development'), ('Tornado', 'Tornado'), ('TypeScript', 'TypeScript'), ('UI', 'UI'), ('uWSGI', 'uWSGI'), ('UX', 'UX'), ('Vagrant', 'Vagrant'), ('Virtualenv', 'Virtualenv'), ('VR', 'VR'), ('Visualization', 'Visualization'), ('Vue.js', 'Vue.js'), ('Web Development', 'Web Development'), ('Web Scraping', 'Web Scraping')], help_text='Select up to six', max_length=1000, verbose_name='Skills (select up to 6)'),
        ),
    ]