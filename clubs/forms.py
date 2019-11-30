from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('club','date1','person','role2')

class ClubMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('date1','persontxt','role2')

class ClubMeetingWithDateForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('persontxt','role2')

class MeetingFormV2(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('club','date1','person','role2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['person'].queryset = Person.objects.none()


# from django import forms
from .models import Person, Club

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        # fields = ('club','name','fullname', 'is_member', 'member_since', 'note')
        
        # club is fixed, not to edit by encoder
        # NOTE based on the account login
        fields = ('name','fullname', 'is_member', 'member_since', 'note')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['city'].queryset = City.objects.none()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['city'].queryset = City.objects.none()

        # if 'country' in self.data:
        #     try:
        #         country_id = int(self.data.get('country'))
        #         self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['city'].queryset = self.instance.country.city_set.order_by('name')