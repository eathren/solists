## Jobboard written in Django ( And also migrating to Django from React / Django / DRF)

![Netlify](https://img.shields.io/netlify/a71ca40d-f524-4c22-8ea2-9d42c6fdf177) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Let's be real. Most of us hate the job hunt process (I certainly do). Some of the sites are confusing, applying is difficult, and there is a definite lack of quality control for jobs posted and their formatting. Solists is a step in the direction of fixing some of those problems.

Right now the 1.0 MVP is written in React / Django / Django Rest Framework. This repo is my work transitioning the project to 100% Django.

### Features currently live:

User sign up  
User login  
User job creation  
Job search  
Developers listing (names only on sub-pages at the moment)

### Features upcoming for 1.0 MVP release

improved developer pages  
user profile updates  
search bar  
better job-creation experience  
user and skill search for jobs

### Starting the instance

Make sure you have python3 / pip installed. You'll need it for the shell instance and to install the project.

Run <code> pipenv shell</code>
Run <code> pipenv install </code>

### Live site is available at [www.solists.com](https://www.solists.com)

### Testing

python manage.py test

To test stripe functionality, use a stripe_test key (that you create @ stripe.com), and use the cc value of 4242 4242 4242 4242,. Put any expiration date and etc numbers in afterwards.

### Notes and gotchas

Procfile has to have a capital P. Otherwise it doesn't work on heroku.
