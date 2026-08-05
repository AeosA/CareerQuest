from django.shortcuts import render, redirect
from .models import UserSkill, Skill, UserCareerGoals, Jobs, JobSkills
from .forms import SkillsForm, ChooseCareerForm
# Create your views here.
def setupAccount(request):
    return render(request, 'careerquest_accountsetup.html')

def addskill(request):
    if request.method == "POST":
        skillform = SkillsForm(request.POST)
        if skillform.is_valid():
            # Get the selected Skill objects after Django validates the submitted skillsform.
            selected_skills = skillform.cleaned_data['skill_options']
            UserSkill.objects.filter(user=request.user).delete() #when you turn in the form to choose skills, delete previous submission to prevent duplicates and promote editting

            for skills in selected_skills:
                print(f"Creating objects within the database {skills} within the databse")
                UserSkill.objects.create(
                    user = request.user,
                    skill = skills
                )

            return redirect("cq_setupaccount:addskill")
    
    else:
        skillform = SkillsForm()
    
    return render(request, 'careerquest_accountsetup.html', {"skillform": skillform})

def choosecareer(request):
    if request.method == "POST":
        careerform = ChooseCareerForm(request.POST)
        if careerform.is_valid():
            # Get the selected Roles objects after Django validates the submitted choosecareerform.
            selected_career = careerform.cleaned_data['role_options']
            UserCareerGoals.objects.filter(user=request.user).delete()

            UserCareerGoals.objects.create(
                user = request.user,
                role = selected_career,
                # We dont need to include 'goal_id' since its a primary key and 'created_at' since its automatically filled
            )
    else:
        careerform = ChooseCareerForm()

    return render(request, 'careerquest_accountsetup.html', )


def ProfileSetup(request):
    if request.method == "POST":
        if "addskill" in request.POST:
            skillform = SkillsForm(request.POST)
            if skillform.is_valid():
                # Get the selected Skill objects after Django validates the submitted skillsform.
                selected_skills = skillform.cleaned_data['skill_options']
                UserSkill.objects.filter(user=request.user).delete() #when you turn in the form to choose skills, delete previous submission to prevent duplicates and promote editting

                for skills in selected_skills:
                    print(f"Creating objects within the database {skills} within the databse")
                    UserSkill.objects.create(
                        user = request.user,
                        skill = skills
                    )

                return redirect("cq_setupaccount:addskill")

        elif "choosecareer" in request.POST:
            careerform = ChooseCareerForm(request.POST)
            if careerform.is_valid():
                # Get the selected Roles objects after Django validates the submitted choosecareerform.
                selected_career = careerform.cleaned_data['role_options']
                UserCareerGoals.objects.filter(user=request.user).delete()

                UserCareerGoals.objects.create(
                    user = request.user,
                    role = selected_career,
                    # We dont need to include 'goal_id' since its a primary key and 'created_at' since its automatically filled
                )

                selected_jobs = Jobs.objects.filter(role=selected_career) #filters Jobs' by role_id: gets jobs w/ job_id
                required_skills = JobSkills.objects.filter(job__in = selected_jobs)#filters JobSkills' by job_id: gets jobskills w/ job_id

                #We need the skill_id from all the required skills
                required_skills_id = required_skills.values_list("skill_id", flat=True) #we are using flat = true b/c we only need the single "skill_id" field

                #Creates the SkillsForm with the corresponding skills that come alone with the role users want
                skillform = SkillsForm(skillID=required_skills_id)


                return render(request, 'careerquest_accountsetup.html', {"skillform": skillform, "careerform": careerform})
    else:
        skillform = SkillsForm()
        careerform = ChooseCareerForm()

    return render(request, 'careerquest_accountsetup.html', {"skillform": skillform, "careerform": careerform})

