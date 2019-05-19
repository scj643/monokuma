from django.db import models

MONTH_CHOICES = (
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December')
)


class Character(models.Model):
    GENDERS = (('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown'), ('?', '?'))
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDERS, blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Height in centimeters")
    birth_month = models.PositiveSmallIntegerField(blank=True, null=True, choices=MONTH_CHOICES)
    birth_day = models.PositiveSmallIntegerField(blank=True, null=True)
    chest = models.PositiveSmallIntegerField(help_text='Chest Size in centimeters', blank=True, null=True)
    weight = models.PositiveSmallIntegerField(help_text='Weight in kilograms', blank=True, null=True)
    kanji = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_character'),
            models.CheckConstraint(check=models.Q(birth_day__gte=1) & models.Q(birth_day__lte=31),
                                   name='birth_day_limit')
        ]

    def __str__(self):
        return f'Character: {self.first_name} {self.last_name}'


class Media(models.Model):
    english_name = models.CharField(max_length=255, null=True)
    jp_name = models.CharField(max_length=255, null=True)
    us_release_date = models.DateField(null=True, blank=True)
    jp_release_date = models.DateField(null=True, blank=True)
    media_type = models.CharField(max_length=255, null=True, default='game')

    class Meta:
        constraints = [
            # Limit entries so that only one media entry for each game
            models.UniqueConstraint(fields=['english_name', 'media_type'], name='unique_media')
        ]

    def __str__(self):
        return f'Media: {self.english_name}'


class Appearance(models.Model):
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    spoiler = models.BooleanField(default=False)
    primary_media = models.BooleanField(default=True)

    class Meta:
        constraints = [
            # Limit appearances to one per character+media combo
            models.UniqueConstraint(fields=['character', 'media'], name='unique_appearance')
        ]

    def __str__(self):
        return f'Appearance: {self.character} in {self.media}'


class Talent(models.Model):
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    spoiler = models.BooleanField(default=False)
    talent = models.CharField(max_length=80)

    class Meta:
        constraints = [
            # Limit to 1 character to media to talent pairing.
            models.UniqueConstraint(fields=['character', 'media', 'talent'], name='unique_talent')
        ]

    def __str__(self):
        return f'Talent: {self.character.first_name} {self.character.last_name} - {self.talent}'


class Chapter(models.Model):
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True)
    number = models.SmallIntegerField(help_text="The number of the chapter in the game.\n"
                                                "Starts at 0 for the Prologue")

    class Meta:
        constraints = [
            # limit to one media to number pairing
            models.UniqueConstraint(fields=['media', 'number'], name='unique_chapter')
        ]

    def __str__(self):
        return f'Chapter: {self.number} - {self.name}'


class Murder(models.Model):
    murderer = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, related_name='murderer')
    murdered = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, related_name='murdered')
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            # limit to one muderer - murdered - chapter relation since two of the same murders can't happen.
            models.UniqueConstraint(fields=['murderer', 'murdered', 'chapter'], name='unique_murder')
        ]

    def __str__(self):
        return f'Murder: {self.murderer} killed {self.murdered} in {self.chapter}'


class Quote(models.Model):
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    quote = models.CharField(max_length=4096, null=True)
    spoiler = models.BooleanField(default=False)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            # Avoid duplicate quotes
            models.UniqueConstraint(fields=['character', 'quote', 'media'], name='unique_quote')
        ]

    def __str__(self):
        return f'Quote "{self.quote}" by {self.character}'
