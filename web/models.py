from django.db import models
from django import forms

class News(models.Model):
	title = models.CharField(max_length = 120)
	text = models.TextField()
	date = models.DateTimeField()
	img = models.ImageField(upload_to='news/', blank=True)

	@property
	def img_url(self):
		if self.img and hasattr(self.img, 'url'):
			return self.img.url

	def __str__(self):
		return str(self.id)+" | "+str(self.title)

class Message(models.Model):
	FIO = models.CharField(max_length = 60)
	phone = models.CharField(max_length = 11)
	email = models.EmailField()
	text = models.TextField()

	def __str__(self):
		return str(self.id)+" | "+str(self.FIO)

class Product(models.Model):

	CATEGORY = [
		(11, 'Судовой'),
		(12, 'Пирсовый'),
		(13, 'Съемный портальный'),
		(14, 'Балки грузовые'),
		(15, 'Грузовой специальный'),
		(16, 'Грузовой арктический'),
		(21, 'Грузовой - перем. ток | мал. ср.'),
		(22, 'Грузовой - перем. ток | бол.'),
		(23, 'Пром. Грузовой - эл. привод | мал.'),
		(24, 'Пром. Грузовой - перем. ток | бол.'),
		(25, 'Вьюшка топенантная - перем. ток'),
		(26, 'Подъемно тяговая - перем. ток'),
		(27, 'Грузовой - перем. ток'),
		(28, 'Гидрологический'),
		(29, 'Пром. Лебедка или комплекс'),
		(210, 'Буксирная автом. эл. привод'),
		(211, 'Буксирно-технологическая эл. привод'),
		(212, 'Шлюпочная - гидр. привод'),
		(217, 'Трелевочная'),
		(218, 'Люктового закрытия - перем. ток'),
		(219, 'Траповая - перем. ток'),
		(31, 'Водоструйный стационарный'),
		(32, 'Водоструйный переносной')
	]

	name = models.CharField(max_length = 120)
	category = models.PositiveSmallIntegerField( ("category"), choices=CATEGORY )
	img = models.ImageField(upload_to='product/', blank=True)
	text = models.TextField()

	@property
	def img_url(self):
		if self.img and hasattr(self.img, 'url'):
			return self.img.url

	def __str__(self):
		return str(self.name)
