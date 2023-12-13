# 🏛️ Django Theatre Management System 🏛️

## Overview  

This project implements a Theatre Management System using DRF, providing models and functionalities for managing plays, performances, reservations, and tickets.

---
# Features 📜

### ✅ Managing Reservations and Tickets

- Seamlessly handle orders and tickets for a stellar user experience.

### ✅ Creating Performances

- Create performances based on theatres, plays, actors, and genres.

### ✅ Filtering for Plays and Performances

- Implement filtering that allows you to easily search for a play or performance.

### ✅ Image Uploading

- You can upload an image for your play.

### ✅ JWT Authenticated

- Feel your account is safe with JWT authentication.

### ✅ Admin Panel (/admin/)

- Access to the admin panel

### ✅ API Documentation (/api/doc/swagger/)

- Explore the API with comprehensive documentation located at http://localhost:8000/api/doc/swagger/

# Installation Guide 📜

---

### Clone repository

```
git clone https://github.com/MiskoRuslan/theatre-api
```

### Pull the interstellar project

```
docker pull ruslanmisko/theatre_api
```

### Configure Environment
Configure the .env file using .env.sample as your tutor.

```
cp .env.sample .env
```
Edit the .env file with the necessary configuration.

### Run the following docker-compose command to initiate liftoff:

```
docker-compose up --build
```
This command will build the necessary containers and launch the Theatre API.

### 🤵 Default user

### Next, you can either create a regular user by following the URL:


 http://localhost:8000/api/user/register/

In this case, you will only be able to register new reservations and tickets and will not have access to make changes or create other objects.

---

### 🫅 Superuser
Or you can create a superuser, for this after you have built the project, open a new terminal window and enter the command in it:
```
docker exec -it container_id bash
```
(for example docker exec -it 3e3c198c1 bash)

This will allow you to enter commands to interact with the built project. Next, we create a superuser using the usual method:
python manage.py createsuperuser

## Navigation 🧭

 - Access the API at http://localhost:8000/api/theatre/.

 - For authentication tokens, visit http://localhost:8000/api/user/token/.

# Documentation
### Swagger 📝
```http://localhost:8000/api/doc/swagger/```

![10.png](images%2F10.png)

---

### Redoc 📝

```http://localhost:8000/api/doc/redoc/```

![2.png](images%2F2.png)


---

# Scheme 📈

The idea is to allow visitors of the Theatre to make Reservations online and choose needed seats, without going physically to the Theatre.

![13.png](images%2F13.png)


---

# Some another screenshots of API:
![1.png](images%2F1.png)
![2.png](images%2F2.png)
![3.png](images%2F3.png)
![4.png](images%2F4.png)
![5.png](images%2F5.png)
![6.png](images%2F6.png)
![7.png](images%2F7.png)
![8.png](images%2F8.png)
![9.png](images%2F9.png)
![10.png](images%2F10.png)

# That`s all :) Thx for attention!
