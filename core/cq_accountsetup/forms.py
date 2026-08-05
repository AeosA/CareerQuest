from django import forms
from .models import Skill, Roles

class SkillsForm(forms.Form):
    skill_options = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.none(),
        required = True,
        widget = forms.CheckboxSelectMultiple,
        help_text ="Select one or more for your current skills."
    )

    def __init__(self, skillID = None, *args, **kwargs): #setting up SkillsForm initial characteristics.
        super().__init__(*args, **kwargs)

        #Given skill_id arguements, get Skill objects with the skill_id  of 'skillID'
        if skillID:
            self.fields["skill_options"].queryset = Skill.objects.filter(skill_id__in = skillID)
            

class ChooseCareerForm(forms.Form):
    role_options = forms.ModelChoiceField(
        queryset=Roles.objects.all(),
        required = True,
        widget = forms.RadioSelect,
        help_text = "Select the career path you wish to take."
    )

