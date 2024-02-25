from tabnanny import verbose
from django.db import models


# Create your models here.

class exemple(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("exemple")
        verbose_name_plural = ("exemple")
        db_table = 'exemple'



#base de donne pour les matieres:

#font
class Aa002(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Aa002")
        verbose_name_plural = ("Aa002")
        db_table = 'Aa002'


# Aluminium primaire - Lingot
class Ab001(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=80, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=130, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Ab001")
        verbose_name_plural = ("Ab001")
        db_table = 'Ab001'


#   ABS, acrylonitrile butadiène syrène - Copolymère - Granulés    
class Ac001(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=80, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Ac001")
        verbose_name_plural = ("Ac001")
        db_table = 'Ac001'


# PVC, polychlorure de vinyle - Moulé par injection 
class Ac008(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Ac008")
        verbose_name_plural = ("Ac008")
        db_table = 'Ac008'



# base de donne des procedes:

# Fraisage - Fonte
class Ba043(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Ba043")
        verbose_name_plural = ("Ba043")
        db_table = 'Ba043'

# Fraisage - Acier
class Ba044(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Ba044")
        verbose_name_plural = ("Ba044")
        db_table = 'Ba044'


# Fraisage - Aluminium
class Ba045(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Ba045")
        verbose_name_plural = ("Ba045")
        db_table = 'Ba045'


# Injection soufflage - Plastiques
class Bf004(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Bf004")
        verbose_name_plural = ("Bf004")
        db_table = 'Bf004'


# base de donne de energie:

# Electricité basse tension - France:
class Ca001(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Ca001")
        verbose_name_plural = ("Ca001")
        db_table = 'Ca001'

class Cb001(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Cb001")
        verbose_name_plural = ("Cb001")
        db_table = 'Cb001'


# base de donne du  Fin de vie:


# Scénario de fin de vie - Acier
class Ez004(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Ez004")
        verbose_name_plural = ("Ez004")
        db_table = 'Ez004'


# Scénario de fin de vie - Aluminium
class Ez005(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Ez005")
        verbose_name_plural = ("Ez005")
        db_table = 'Ez005'

# Scénario de fin de vie - Plastiques
class Ez007(models.Model):
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Ez007")
        verbose_name_plural = ("Ez007")
        db_table = 'Ez007'

    
# base de donne transport:

# Avion moyen courrier, transport:
class Da002(models.Model):
    a = models.CharField(db_column='A', max_length=200, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Da002")
        verbose_name_plural = ("Da002")
        db_table = 'Da002'

# Bateau, transport océanique de marchandises - Monde
class Db001(models.Model):
    a = models.CharField(db_column='A', max_length=200, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Db001")
        verbose_name_plural = ("Db001")
        db_table = 'Db001'

# Péniche, transport de marchandises - Europe
class Db002(models.Model):
    a = models.CharField(db_column='A', max_length=200, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Db002")
        verbose_name_plural = ("Db002")
        db_table = 'Db002'


# Camion 16 à 32t - Europe
class Dc001(models.Model):
    a = models.CharField(db_column='A', max_length=200, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Dc001")
        verbose_name_plural = ("Dc001")
        db_table = 'Dc001'


# Train, transport de marchandises - Europe
class Dd001(models.Model):
    a = models.CharField(db_column='A', max_length=200, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Dd001")
        verbose_name_plural = ("Dd001")
        db_table = 'Dd001'


# Scénario de transport aérien - Approvisionnement en France depuis la Chine
class Dz001(models.Model):
    a = models.CharField(db_column='A', max_length=200, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Dz001")
        verbose_name_plural = ("Dz001")
        db_table = 'Dz001'

# Scénario de transport maritime - Approvisionnement en France depuis la Chine
class Dz002(models.Model):
    a = models.CharField(db_column='A', max_length=200, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Dz002")
        verbose_name_plural = ("Dz002")
        db_table = 'Dz002'


# Scénario de transport aérien - Approvisionnement en France depuis l'Inde
class Dz003(models.Model):
    a = models.CharField(db_column='A', max_length=200, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Dz003")
        verbose_name_plural = ("Dz003")
        db_table = 'Dz003'


# Scénario de transport maritime - Approvisionnement en France depuis l'Inde
class Dz004(models.Model):
    a = models.CharField(db_column='A', max_length=200, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=100, blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = ("Dz004")
        verbose_name_plural = ("Dz004")
        db_table = 'Dz004'