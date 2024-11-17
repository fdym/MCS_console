from django.db import models

# Create your models here.

class Vanilla(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    Type = models.CharField(max_length=15) # Developnent status,example:release
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class Forge(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    ForgeVersion = models.CharField(max_length=20) # Forge version
    Type = models.CharField(max_length=15) # Forge developnent status,example:release
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class Fabric(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    FabricVersion = models.CharField(max_length=20) # Fabric version
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class NeoForge(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    NeoForgeVersion = models.CharField(max_length=20) # NeoForge version
    Type = models.CharField(max_length=15) # NeoForge developnent status,example:release
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class CraftBukkit(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class Spigot(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class Paper(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    BuildNumber = models.IntegerField() # Build number,example:10
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class SpongeVanilla(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    SpongeVersion = models.CharField(max_length=20) # Sponge version
    Type = models.CharField(max_length=15) # SpongeVanilla developnent status,example:release
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class SpongeForge(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    ForgeVersion = models.CharField(max_length=20) # Forge version
    SpongeVersion = models.CharField(max_length=20) # Sponge version
    Type = models.CharField(max_length=15) # SpongeForge developnent status,example:release
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class SpongeNeo(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    NeoForgeVersion = models.CharField(max_length=20) # NeoForge version
    SpongeVersion = models.CharField(max_length=20) # Sponge version
    Type = models.CharField(max_length=15) # SpongeNeo developnent status,example:release
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class Mohist(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    ForgeVersion = models.CharField(max_length=20) # Forge version
    BuildNumber = models.IntegerField() # Build number,example:10
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL

class Bedrock(models.Model):
    MCVersion = models.CharField(max_length=25,primary_key=True) # Minecraft version
    Type = models.CharField(max_length=15) # Developnent status,example:release
    URL = models.URLField(max_length=150) # URL
    ThirdPartySourceURL = models.URLField(max_length=150) # Third-party source URL
