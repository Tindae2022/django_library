from django.db import models
from django.urls import reverse
import uuid


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("author-details", args=[str(self.id)])

    def __str__(self):
        return f" {self.first_name}, {self.last_name} "


class Genre(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("genre-detail", args=[str(self.id)])


class Language(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text="Enter a brief description of the book")
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    genre = models.ManyToManyField(Genre, help_text="Select a group Genre")
    language = models.ForeignKey(Language, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On Loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book Availability",

    )

    def __str__(self):
        return f"{self.id}, {self.book.title}"

    class Meta:
        ordering = ["due_back"]
