from django.db import models

# Create your models here.
class Experience(models.Model):
    years = 0
    pass

class Projects(models.Model):
    project1 = "website project"
    project2 = "data visualization using streamlit"
    project3 = "data analysis and visualization using pandas and seaborn"
    project4 = "website project 2"
    project5 = "website project 3"
    pass

class Education(models.Model):
    pass

class Skills(models.Model):
    skill1 = "python"
    skill2 = "django"
    skill3 = "flask"
    skill4 = "mysql or nosql or some other database"
    skill5 = "pandas"
    skill6 = "matplotlib, seaborn"
    skill7 = "machineLearning"
    pass

class Certificates(models.Model):

    pass


class BasicData(models.Model):
    name = ""
    address = ""
    contact = ""
    email = ""
    description = ""
    pass