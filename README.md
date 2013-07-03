DjangoBase
==========

The easiest way to start a Django web project.

## Instructions:

1. Run python setup.py project_name install_directory
2. After installation is complete, go to the install_directory
3. Run source venv/bin/activate
4. Run python manage.py runserver
5. Enjoy!

## Features:

* Simple and intuitive project folder layout
* Proper Django custom user model setup
* AJAX view endpoint decorator
* Environment-sensitive settings files
* LESS setup for modular front-end design
* Pylint and PEP8 code quality check
* Production settings template with Boto, Amazon S3, and Django-Compressor

### Heroku Production Setup:

1. Run heroku config:add PROJECT_NAME_ENV=PROD --app app_name
2. Add AWS information in "config/settings_prod.py"
3. Create an Amazon S3 bucket called "project_name"
4. Run heroku config:add S3_BUCKET_NAME=project_name --app app_name
5. Run heroku config:add AWS_ACCESS_KEY_ID=your_access_key_id
6. Run heroku config:add AWS_SECRET_ACCESS_KEY=your_secret_access_key
