# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from tagging.fields import TagField
from markdown import markdown
from django.db.models import permalink
from django.conf import settings
from django.db.models import permalink
from django.conf import settings


# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=100,  unique=False)
	slug = models.SlugField(max_length=100, unique=True)
	description = models.CharField(max_length=100)
	class Meta:
		ordering = ['title']
		verbose_name_plural = "Categories"

	def __unicode__(self):
		return "/cats/%s/" % self.title

	def get_absolute_url(self):
		return self.slug
class Entry(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = ( (LIVE_STATUS, 'Live'),(DRAFT_STATUS, 'Draft'), (HIDDEN_STATUS, 'Hidden'))
	title = models.CharField(max_length=100 , unique=False)
	excerpt = models.TextField(blank=True, help_text='main content')
	body = models.TextField(blank=False, help_text='Short body max 100 char')
	pub_date=models.DateField(default=datetime.now, blank=False)
	author = models.ForeignKey(User)
	enable_comments=models.BooleanField(default=True)
	featured= models.BooleanField(default=False)
	slug = models.SlugField(unique_for_date='pub_date',help_text="Suggested value automatically generated ➥from title.Must be unique.")
	status = models.IntegerField(choices = STATUS_CHOICES, default = LIVE_STATUS)
	category= models.ManyToManyField(Category)
	tags = TagField()
	excerpt_html = models.TextField(editable=False, blank=True)
	body_html= models.TextField(editable=False, blank=True)
	count=models.IntegerField(max_length=1000, default=0, blank=False)
	image1 = models.ImageField(upload_to='images',
                              verbose_name='Image',blank=True )
	image2 = models.ImageField(upload_to='images',
                              verbose_name='Image',blank=True )
	image3 = models.ImageField(upload_to='images',
                              verbose_name='Image',blank=True )



	def save(self, force_insert=False, force_update=False):
		self.body_html = markdown(self.body)
		if self.excerpt:
			self.excerpt_html= markdown(self.excerpt)
		super(Entry, self).save(force_insert, force_update)

	class Meta:
			ordering=["-pub_date"]
			verbose_name_plural="Entries"

	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return(self.slug)

class Trending(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = ( (LIVE_STATUS, 'Live'),(DRAFT_STATUS, 'Draft'), (HIDDEN_STATUS, 'Hidden'))
	title = models.CharField(max_length=100 , unique=False)
	excerpt = models.TextField(blank=True)
	body = models.TextField(blank=False)
	pub_date=models.DateField(default=datetime.now, blank=False)
	author = models.ForeignKey(User)
	enable_comments=models.BooleanField(default=True)
	featured= models.BooleanField(default=False)
	slug = models.SlugField(unique_for_date='pub_date',help_text="Suggested value automatically generated ➥from title.Must be unique.")
	status = models.IntegerField(choices = STATUS_CHOICES, default = LIVE_STATUS)
	category= models.ManyToManyField(Category)
	tags = TagField()
	excerpt_html = models.TextField(editable=False, blank=True)
	body_html= models.TextField(editable=False, blank=True)
	#count=models.TextField(max_length=100, default=0)
	image1 = models.ImageField(upload_to='images',
                              verbose_name='Image',blank=True )
	image2 = models.ImageField(upload_to='images',
                              verbose_name='Image',blank=True )
	image3 = models.ImageField(upload_to='images',
                              verbose_name='Image',blank=True )



	def save(self, force_insert=False, force_update=False):
		self.body_html = markdown(self.body)
		if self.excerpt:
			self.excerpt_html= markdown(self.excerpt)
		super(Entry, self).save(force_insert, force_update)

	class Meta:
			ordering=["-pub_date"]
			verbose_name_plural="Trending"

	def __unicode__(self):
		return  self.title
	def get_absolute_url(self):
		return(self.slug)

class Link(models.Model):
	title= models.CharField(max_length=100, unique=False)
	description = models.TextField(blank=True)
	description_html= models.TextField(blank=True)
	url=models.URLField(unique=True)
	posted_by= models.ForeignKey(User)
	pub_date= models.DateField(default = datetime.now, blank=False)
	slug= models.SlugField(unique_for_date = 'pub_date')
	tags = TagField()
	enable_comments= models.BooleanField(default=True)
	post_elsewhere = models.BooleanField('Post to Delicious', default=True)
	via_name= models.CharField('Via',max_length=100, help_text="the site you spotted the link" )
	via_url = models.URLField('Via URL', blank=True, help_text="Link you found the story")
	class Meta:
		ordering =['-pub_date']
	def __unicode__(self):
		return self.title
	def save(self):
		if self.description:
			self.description_html= markdown(self.description)
		if not self.id and self.post_elsewhere:
			import pydelicious
			from django.utils.encoding import smart_str
			pydelicious.add(settings.DELICIOUS_USERNAME, settings.DELICIOUS_PASSWORD,
							smart_str(self.url),smart_str(self.title), smart_str(self.tags))
		super(Link, self).save()
	@permalink
	def get_absolute_url(self):
		return('entry_detail', None, {'slug':self.slug})
class fakeusers(models.Model):
	user = models.OneToOneField(User)
	bio=models.TextField(max_length=300, blank=True)
	social_twitter=models.CharField(max_length=300)
	social_facebook=models.CharField(max_length=300)
	social_youtube=models.CharField(max_length=300)
	social_google=models.CharField(max_length=300)
	social_pintrest=models.CharField(max_length=300)
	profile_pic= models.ImageField(upload_to='images',
								  verbose_name='Image', blank=True)
	created_on = models.DateField(default=datetime.now, blank=False)


def __unicode__(self):
        return self.user.username
