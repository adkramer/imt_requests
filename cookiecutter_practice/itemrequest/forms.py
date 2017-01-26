from django import forms
from django.forms.models import inlineformset_factory

from braces.forms import UserKwargModelFormMixin

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import ItemRequest, Manufacturer

class ItemRequestForm(UserKwargModelFormMixin, forms.ModelForm):
    class Meta:
        model = ItemRequest
        exclude = ['created_by', 'state']
        initial_fields = ['requester',]

    def __init__(self, *args, **kwargs):
        super(ItemRequestForm, self).__init__(*args, **kwargs)
        
        # self.fields['requested_by'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.helper = FormHelper()
        self.helper.form_id = 'id-requestForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('save', 'Save'))
        self.fields['unit'].initial = 1
        self.fields['requester'].initial = self.user.name
    
    def clean_weblink(self): # not working
        data = self.cleaned_data['weblink']
        return data

    def alert(self):
        pass

class ItemRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = ItemRequest
        exclude = ['created_by']

    def __init__(self, *args, **kwargs):
        super(ItemRequestUpdateForm, self).__init__(*args, **kwargs)
        
        # self.fields['requested_by'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.helper = FormHelper()
        self.helper.form_id = 'id-requestForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('save', 'Save'))