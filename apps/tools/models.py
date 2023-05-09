from django.db import models

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=100)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    numeric_code = models.CharField(max_length=3, blank=True, null=True)
    iso2 = models.CharField(max_length=2, blank=True, null=True)
    phonecode = models.CharField(max_length=255, blank=True, null=True)
    capital = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    currency_name = models.CharField(max_length=255, blank=True, null=True)
    currency_symbol = models.CharField(max_length=255, blank=True, null=True)
    tld = models.CharField(max_length=255, blank=True, null=True)
    native = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    subregion = models.CharField(max_length=255, blank=True, null=True)
    timezones = models.TextField(blank=True, null=True)
    translations = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    emoji = models.CharField(max_length=191, blank=True, null=True)
    emojiu = models.CharField(db_column='emojiU', max_length=191, blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField()
    wikidataid = models.CharField(db_column='wikiDataId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        db_table = str(__package__.split('.')[1])+'_countries'
        
class States(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Countries,on_delete=models.PROTECT)
    country_code = models.CharField(max_length=2)
    fips_code = models.CharField(max_length=255, blank=True, null=True)
    iso2 = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    flag = models.IntegerField()
    wikidataid = models.CharField(db_column='wikiDataId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '%s | %s' % ( self.country.name, self.name)

    class Meta:
        db_table = str(__package__.split('.')[1])+'_states'

class Cities(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(States,on_delete=models.PROTECT)
    state_code = models.CharField(max_length=255)
    country = models.ForeignKey(Countries,on_delete=models.PROTECT)
    country_code = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    flag = models.IntegerField()
    wikidataid = models.CharField(db_column='wikiDataId', max_length=255, blank=True, null=True)  # Field name made lowercase.

    
    def __str__(self):
        return '%s | %s' % ( self.country.name, self.name)

    class Meta:
        db_table = str(__package__.split('.')[1])+'_cities'