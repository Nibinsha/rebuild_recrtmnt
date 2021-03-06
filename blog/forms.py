from django import forms
from django.forms import modelformset_factory
from .models import UserProfile, ClientMaster, Candidate
from django.forms import formset_factory
from django.contrib.admin.widgets import AdminDateWidget


class userprofileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Password'})
        }


# CandicateModelFormset = modelformset_factory(
#     Book,
#     fields = '__all__'
#     extra=1,
# widgets={'name': forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Enter Book Name here'
#     })
# }
# )


class ClientMasterForm(forms.ModelForm):
    class Meta:
        model = ClientMaster
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'industry_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CandidateForm(forms.ModelForm):

    # intervew_company = forms.ChoiceField(required=False, choices=company_list)
    intervew_company = forms.ModelChoiceField(queryset=ClientMaster.objects.all(),required=False)
    # scheduled_on = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    # duration_in_min = forms.IntegerField(required=False)
    # licence_id = forms.CharField(max_length=25, required=False)
    # country = forms.CharField(max_length=50, required=False)
    # valid_up_to = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    # dob = forms.DateField(required=False, input_formats='%d/%m/%Y')
    # forms.fields['interview'].widget = forms.HiddenInput()

    # def __init__(self, *args, **kwargs):
    #     super(CandidateForm, self).__init__(*args, **kwargs)
    #     self.base_fields['dob'].widgets = forms.HiddenInput()
    #     # self.base_fields['driving_license'].widgets = forms.HiddenInput()
    #     import pdb; pdb.set_trace()

    class Meta:
        model = Candidate
        fields = '__all__'
        # exclude = ['driving_license', 'interview']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'primary_mob_no': forms.TextInput(attrs={'class': 'form-control'}),
            'secondary_mob_no': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            # 'dob': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'passport_no': forms.TextInput(attrs={'class': 'form-control'}),
            'salary_details': forms.TextInput(attrs={'class': 'form-control'}),
            'total_experence': forms.TextInput(attrs={'class': 'form-control'}),
            # 'document_files': forms.FileInput(attrs={'class': 'form-control'}),
            # 'passport_expery_date': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_expery_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'interview_status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'passport_status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'abroad_experence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'job_category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'visa_approval_status': forms.CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            # 'departure_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'departure_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Enter the username'}),

            # 'intervew_company': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            # 'scheduled_on': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            # 'scheduled_on': forms.DateInput(
            #     attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Enter the username'}),
            'added_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'interview': forms.HiddenInput(),
            'driving_license': forms.HiddenInput(),
            'id': forms.HiddenInput(),

            'licence_id' : forms.TextInput(attrs={'class': 'form-control'}),
            'country' : forms.TextInput(attrs={'class': 'form-control'}),
            'valid_up_to' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

            'scheduled_on' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'duration_in_min' : forms.TextInput(attrs={'class': 'form-control'}),

        }

    def save(self, commit=True):
        cd = self.cleaned_data

        # try:
        candidate_id = self.initial.get('id')

        # if not cd.get('interview'):
        #     inter = Interview.objects.create()
        # else:
        #     inter = Interview.objects.get(id=cd.get('interview'))

        # inter.company_id = cd.get('intervew_company')
        # inter.scheduled_on = cd.get('scheduled_on')
        # inter.duration_in_min = cd.get('duration_in_min')
        # inter.save()
        # licence_id = cd.get('licence_id')
        # try:
        #     dr_licence = DrvingLicence.objects.get(licence_id=licence_id)
        #     if cd.get('country') == dr_licence.country:
        #         dr_licence.valid_up_to = cd.get('valid_up_to')
        #
        # except DrvingLicence.DoesNotExist:
        #     # dr_licence = DrvingLicence.objects.create()
        #     dr_licence = DrvingLicence()
        #     dr_licence.country = cd.get('country')
        #     dr_licence.valid_up_to = cd.get('valid_up_to') if cd.get('valid_up_to') else None
        #     dr_licence.licence_id = cd.get('licence_id')
        #     dr_licence.save()

        # dr_licence.save()

        # can = Candidate.objects.get_or_create(id = candidate_id)
        if candidate_id:
            can = Candidate.objects.get(id=candidate_id)
        else:
            can = Candidate()
        can.first_name = cd.get('first_name')
        can.last_name = cd.get('last_name')
        can.primary_mob_no = cd.get('primary_mob_no')
        can.secondary_mob_no = cd.get('secondary_mob_no')
        can.age = cd.get('age')
        can.dob = cd.get('dob')
        can.passport_no = cd.get('passport_no')
        can.passport_expery_date = cd.get('passport_expery_date')
        can.job_category = cd.get('job_category')
        can.total_experence = cd.get('total_experence')
        can.abroad_experence = cd.get('abroad_experence')
        can.document_files = cd.get('document_files')
        # can.interview = inter
        can.scheduled_on = cd.get('scheduled_on')
        can.duration_in_min = cd.get('duration_in_min')
        can.intervew_company = cd.get('intervew_company')

        can.interview_status = cd.get('interview_status')
        can.visa_approval_status = cd.get('visa_approval_status')
        can.salary_details = cd.get('salary_details')
        can.passport_status = cd.get('passport_status')
        can.departure_date = cd.get('departure_date')

        can.licence_id = cd.get('licence_id')
        can.country = cd.get('country')
        can.valid_up_to = cd.get('valid_up_to')
        # can.driving_license.add(dr_licence)
        can.save()

        # except  Exception as e:
        #     print('error', e)
        #     import pdb; pdb.set_trace()

        # instance = super(SelectCourseYear, self).save(commit=False)
        # instance.course = self.course
        # instance.user = self.user
        # if commit:
        #     instance.save()


extra_num = Candidate.objects.count() + 1
CandidateFormset = formset_factory(CandidateForm, extra=extra_num)


# nibinsha
class SubuserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'email', 'phone')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
