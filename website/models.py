from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from website.utils.blogs import get_reading_time



class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContactUsQuery(TimeStampModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    message = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(TimeStampModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])



class ThumbnailMixin(TimeStampModel):
    thumbnail = models.ImageField(
        upload_to='thumbnails/',
        blank=True,
        null=True
    )
    name = models.CharField(blank=True, null=True)

    class Meta:
        abstract = True

class Author(TimeStampModel):
    full_name = models.CharField(unique=True, max_length=255)
    designation = models.CharField(max_length=255, blank=True, null=True)
    

class Blog(ThumbnailMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        Category,
        related_name='blogs',
        on_delete=models.CASCADE
    )
    short_decription = models.CharField(max_length=512, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='all_blogs')
    content = RichTextUploadingField()
    tags = TaggableManager(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])
    

    @property
    def reading_time(self):
        return get_reading_time(self.content)

