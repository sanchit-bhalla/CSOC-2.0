from django import forms

class OtpForm(forms.Form):
    Phone_number=forms.CharField()

    def clean(self):
        all_clean_data = super().clean()
        Phone_number = all_clean_data['Phone_number']


class ConfirmOtpForm(forms.Form):
    Confirm_OTP = forms.CharField()

    def clean(self):
        all_clean_data = super().clean()
        Confirm_OTP = all_clean_data['Confirm_OTP']
