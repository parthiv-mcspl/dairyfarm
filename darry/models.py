from django.db import models

class Info(models.Model):
    title = models.CharField(max_length=200)  # Field for title
    message = models.TextField()  # Field for message
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Optional image upload

    def __str__(self):
        return self.title  # String representation of the model

class Product(models.Model):
    name = models.CharField(max_length=200)  # Field for title
    detail = models.TextField()  # Field for message
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Optional image upload

    def __str__(self):
        return self.name # String representation of the model


class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    content = models.TextField()  # Book content (detailed description)
    image = models.ImageField(upload_to='book_images/')  # Optional: Cover or related image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.IntegerField(default=3)  # Ensure this field exists
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name