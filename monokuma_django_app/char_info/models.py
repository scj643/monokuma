from django.db import models


class Character(models.Model):
    GENDERS = (('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown'))
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDERS, blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Height in centimeters")
    birth_month = models.PositiveSmallIntegerField(blank=True, null=True)
    birth_day = models.PositiveSmallIntegerField(blank=True, null=True)
    chest = models.PositiveSmallIntegerField(help_text='Chest Size in centimeters', blank=True, null=True)
    weight = models.PositiveSmallIntegerField(help_text='Weight in kilograms', blank=True, null=True)
    kanji = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'Character: {self.first_name} {self.last_name}'


class Media(models.Model):
    english_name = models.CharField(max_length=255, null=True)
    jp_name = models.CharField(max_length=255, null=True)
    us_release_date = models.DateField(null=True, blank=True)
    jp_release_date = models.DateField(null=True, blank=True)
    media_type = models.CharField(max_length=255, null=True, default='game')

    def __str__(self):
        return f'Media: {self.english_name}'


class Appearance(models.Model):
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    spoiler = models.BooleanField(default=False)
    primary_media = models.BooleanField(default=True)

    def __str__(self):
        return f'Appearance: {self.character} in {self.media}'


class Talent(models.Model):
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    spoiler = models.BooleanField(default=False)
    talent = models.CharField(max_length=80)


class Chapter(models.Model):
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True)
    number = models.SmallIntegerField(help_text="The number of the chapter in the game.\n"
                                                "Starts at 0 for the Prologue")


class Murder(models.Model):
    murderer = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, related_name='murderer')
    murdered = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, related_name='murdered')
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True)


class Quote(models.Model):
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    quote = models.CharField(max_length=4096, null=True)
    spoiler = models.BooleanField(default=False)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
