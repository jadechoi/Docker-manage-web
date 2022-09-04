from django import forms

class CreateForm(forms.Form):
    stack_name = forms.CharField(max_length=15)
    create_yml = forms.CharField(widget=forms.Textarea)

class CreateNetworkForm(forms.Form):
    network_name = forms.CharField(max_length=15)
    CHOICES=[('overlay','overlay'),('bridge','bridge')]
    driver = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    attachable = forms.BooleanField(required=False)

class CreateVolumeForm(forms.Form):
    volume_name = forms.CharField(max_length=15)
