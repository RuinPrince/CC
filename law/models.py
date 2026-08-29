from django.db import models

class Bns(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    subchapter = models.IntegerField()
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Bns'

class ChildMarriage(models.Model):
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
        db_table = 'ChildMarriage'

class ChildProtection(models.Model):
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
        db_table = 'ChildProtection'

class Electricity(models.Model):
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
        db_table = 'Electricity'

class IT(models.Model):
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
        db_table = 'IT'

class JuvenileJustice(models.Model):
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
        db_table = 'JuvenileJustice'

class Lawtablelist(models.Model):
    tname = models.TextField(primary_key=True)
    category = models.TextField()
    description = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'LawTableList'


class MoneyLaundering(models.Model):
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
        db_table = 'MoneyLaundering'

class MotorVehicles(models.Model):
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
        db_table = 'MotorVehicles'

class NationalHighways(models.Model):
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
        db_table = 'NationalHighways'

class PetroleumAndNaturalGas(models.Model):
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
        db_table = 'PetroleumAndNaturalGas'

class WomenProtection(models.Model):
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
        db_table = 'WomenProtection'

class Wildlife(models.Model):
    section = models.TextField(primary_key=True)
    chapter = models.TextField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Wildlife'

class Realestate(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.TextField()
    name = models.TextField()
    name_ta = models.TextField(blank=True, null=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'RealEstate'

class Water(models.Model):
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
        db_table = 'Water'

class Muslimmarriage(models.Model):
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
        db_table = 'MuslimMarriage'

class Forest(models.Model):
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
        db_table = 'Forest'

class Evs(models.Model):
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
        db_table = 'Environment'

class Air(models.Model):
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
        db_table = 'Air'

class Companies(models.Model):
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
        db_table = 'Companies'

class Hindumarriage(models.Model):
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
        db_table = 'hindumarriage'

class Specialmarriage(models.Model):
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
        db_table = 'specialmarriage'


class ConsumerProtection(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True)

    class Meta:
        managed = True
        db_table = 'ConsumerProtection'    

class Divorce(models.Model):
    section = models.AutoField(primary_key=True)
    chapter = models.IntegerField()
    name = models.TextField()
    name_ta = models.TextField(blank=True)
    title = models.TextField()
    title_ta = models.TextField(blank=True)
    description = models.TextField()
    summary = models.TextField()
    summary_ta = models.TextField(blank=True)

    class Meta:
        managed = True
        db_table = 'divorce'