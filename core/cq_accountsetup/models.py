from django.db import models
from django.contrib.auth.models import User

# Used as a foreign key by model's:'UserSkill', 'JobSkills'
class Skill(models.Model):
    #By default Django creates an id as a primary key but we're using legacy databse with a different primary so we have to declare it
    skill_id = models.IntegerField(primary_key=True)
    skill_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "skills"
    
    def __str__(self):
        return self.skill_name

#Links user with the career skills they have turned in
class UserSkill(models.Model):
    #This is our introduction to foreign key...used for many-to-one relationship i.e var skill references class skill
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    pk = models.CompositePrimaryKey("user_id", "skill_id")
    class Meta:
        managed = False
        db_table = "user_skills"

# Models for careers/jobs/roles

# Used as a foreign key by model's:'Jobs', 'UserCareerGoals'
class Roles(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = "roles"

    def __str__(self):
        return self.role_name

# Used as a foreign key by model's:'JobSkills'
class Jobs(models.Model):
    job_id = models.IntegerField(primary_key=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    source = models.CharField(max_length=100)
    date_posted = models.DateField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "jobs"

#Links corresponding job with the skills required for them
class JobSkills(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


    pk = models.CompositePrimaryKey("job_id", "skill_id")

    class Meta:
        managed = False
        db_table = "job_skills"

class UserCareerGoals(models.Model):
    goal_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True) #auto_now =True sets date/time when model is updated/instantiated 

    class Meta:
        managed = False
        db_table = "user_career_goals"