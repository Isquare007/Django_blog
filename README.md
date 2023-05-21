# Blog App

## This is a Django-based blog application that provides user authentication and management, allowing users to create and manage their blog posts. The application also supports different user roles, including default users, moderator users, and superusers, with varying levels of permissions.

## Features
### User authentication and management: Users can sign up, log in, and manage their profiles.
### Blog post functionality: Users can create, edit, and delete their blog posts.
### User roles and permissions: Different user roles provide varying levels of access and permissions.
### Bootstrap 5 and Crispy Forms: The blog UI is built using Bootstrap 5 for a responsive and modern look, with forms styled using Crispy Forms.
### CSRF protection: The API endpoints are secured with CSRF protection to prevent cross-site request forgery attacks.

## Installation
```Clone the repository:
https://github.com/Isquare007/Django_blog.git
```

```Install the dependencies:
pip install -r requirements.txt
```

```Create the database:
python manage.py migrate
```

```Start the development server:
python manage.py runserver
```

## Usage

### Create a new account or log in with an existing account.
### Explore the blog posts, create new posts, edit existing posts, or delete your own posts.
### Users with moderator or superuser roles can also delete and ban other users' posts.
### Access the management dashboard at http://localhost:8000/ to view user metrics and other relevant information.
### You can also access the retool dashboard here https://isquare.retool.com/apps/3809b29c-f689-11ed-b2c6-7f5f18356d5e/Django%20Blog

# Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
