from django.db import models

# Create your models here.

class Righttablelist(models.Model):
    name = models.TextField(db_column='Name',  blank=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    tname = models.TextField(db_column='Tname', primary_key=True, blank=True, )  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'RightTableList'

class Disabilities(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Disabilities'


class Education(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Education'


class Information(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Information'


class HumanRights(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HumanRights'


class SCST(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'SCST'


class FoodSecurity(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'FoodSecurity'


class LegalServices(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'LegalServices'


class ChildLabour(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ChildLabour'


class Surrogacy(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Surrogacy'


class Welfare(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Welfare'