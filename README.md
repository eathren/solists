## Jobboard written in Django ( And also migrating to Django from React / Django / DRF)
### 1.0 MVP is live!
[![License](https://img.shields.io/badge/License-GNU%203.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)

Post about why this project exists can be found [here](https://www.nolanbraman.com/100%20hours%20of%20django/)

---



Let's be real. Most of us hate the job hunt process (I certainly do). Some of the sites are confusing, applying is difficult, and there is a definite lack of quality control for jobs posted and their formatting. Solists is a step in the direction of fixing some of those problems.

Right now the 1.0 MVP is written in  Django and postres, having transitioned from a React + DRF codebase I previously had been working on. 

![solists screenshot](https://i.imgur.com/IUCJ74T.png )

### Features currently live:

User sign up  
User login  
User job creation  
User Customizable Profile Page
Developer pages
listing sub-pages
postgresdb
UI/UX for job-creation experience
Stripe payments & system
Job search 
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

### License:
GNU General Public License v3.0
