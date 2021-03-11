# Generated by Django 3.1.2 on 2021-03-11 00:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0030_auto_20210311_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AGILE', 'Agile'), ('AWS', 'AWS'), ('ANGULAR', 'AngularJS'), ('ANGULARJS', 'AngularJS'), ('ANGULAR.JS', 'AngularJS'), ('ANSIBLE', 'Ansible'), ('AI', 'AI'), ('APACHE', 'Apache'), ('ARTIFICIAL INTELLIGENCE', 'Artificial Intelligence'), ('BACKBONE.JS', 'Backbone.js'), ('BACKEND', 'Backend'), ('BIG DATA', 'Big Data'), ('BLOCKCHAIN', 'Blockchain'), ('OBJECTIVE-C', 'Objective-C'), ('C#', 'C#'), ('C++', 'C++'), ('CELERY', 'Celery'), ('COUCHDB', 'CouchDB'), ('CSS', 'CSS'), ('CSS3', 'CSS3'), ('CRYPTOCURRENCY', 'Cryptocurrency'), ('DEVOPS', 'DevOps'), ('DJANGO', 'Django'), ('DJANGO REST FRAMEWORK', 'Django Rest Framework'), ('DOCKER', 'Docker'), ('ELASTICSEARCH', 'Elasticsearch'), ('EMBER.JS', 'Ember.js'), ('EXPRESS', 'Express'), ('FABRIC', 'Fabric'), ('FLASK', 'Flask'), ('FRONTEND', 'Frontend'), ('FULLSTACK', 'Fullstack'), ('GATSBY.JS', 'Gatsby.js'), ('GIT', 'Git'), ('GO', 'Go'), ('GOLANG', 'Go'), ('GOOGLE CLOUD PLATFORM', 'Google Cloud Platform'), ('GRAPHQL', 'GraphQL'), ('GUNICORN', 'Gunicorn'), ('HADOOP', 'Hadoop'), ('HEROKU', 'Heroku'), ('HTML', 'HTML'), ('HTML5', 'HTML5'), ('HUGO', 'Hugo'), ('JAVA', 'Java'), ('JAVASCRIPT', 'JavaScript'), ('JENKINS', 'Jenkins'), ('JQUERY', 'jQuery'), ('KAFKA', 'Kafka'), ('KOTLIN', 'Kotlin'), ('KUBERNETES', 'Kubernetes'), ('LINUX', 'Linux'), ('MACHINE LEARNING', 'Machine Learning'), ('MATPLOTLIB', 'Matplotlib'), ('MEMCACHED', 'Memcached'), ('MERCURIAL', 'Mercurial'), ('MICROSOFT AZURE', 'Microsoft Azure'), ('MONGODB', 'MongoDB'), ('MYSQL', 'MySQL'), ('NATURAL LANGUAGE PROCESSING', 'Natural Language Processing'), ('.NET', '.NET'), ('NGINX', 'Nginx'), ('NODE', 'Node.js'), ('NODEJS', 'Node.js'), ('NODE.JS', 'Node.js'), ('NUMPY', 'NumPy'), ('PANDAS', 'Pandas'), ('POSTEGRESQL', 'PostegreSQL'), ('PYQT', 'PyQt'), ('PYRAMID', 'Pyramid'), ('PYSIDE', 'PySide'), ('PYTHON', 'Python'), ('PYTORCH', 'PyTorch'), ('RABBITMQ', 'RabbitMQ'), ('REDIS', 'Redis'), ('REACT', 'React.js'), ('REACTJS', 'React.js'), ('REACT.JS', 'React.js'), ('REACT NATIVE', 'React Native'), ('REST', 'REST'), ('RUST', 'Rust'), ('SALTSTACK', 'SaltStack'), ('SAAS', 'Saas'), ('SASS', 'Sass'), ('SCALA', 'Scala'), ('SCIPY', 'SciPy'), ('SCRAPY', 'Scrapy'), ('SCRUM', 'Scrum'), ('SECURITY', 'Security'), ('SELENIUM', 'Selenium'), ('SOLR', 'Solr'), ('SPARK', 'Spark'), ('SQL', 'SQL'), ('SQLALCHEMY', 'SQLAlchemy'), ('SWIFT', 'Swift'), ('SVELTE', 'Svelte'), ('TENSORFLOW', 'TensorFlow'), ('TERRAFORM', 'Terraform'), ('TEST-DRIVEN DEVELOPMENT', 'Test-Driven Development'), ('TORNADO', 'Tornado'), ('TYPESCRIPT.JS', 'TypeScript'), ('TYPESCRIPTJS', 'TypeScript'), ('TYPESCRIPT', 'TypeScript'), ('UI', 'UI'), ('UWSGI', 'uWSGI'), ('UX', 'UX'), ('VAGRANT', 'Vagrant'), ('VIRTUALENV', 'Virtualenv'), ('VR', 'VR'), ('VISUALIZATION', 'Visualization'), ('VUE', 'Vue.js'), ('VUEJS', 'Vue.js'), ('VUE.JS', 'Vue.js'), ('WEB DEVELOPMENT', 'Web Development'), ('WEB SCRAPING', 'Web Scraping')], help_text='Select up to six', max_length=1000, verbose_name='Skills (select up to 6)'),
        ),
    ]
