from django import forms

class CubiceqForm(forms.Form):
    val1 = forms.IntegerField(label="a")
    val2 = forms.IntegerField(label="b")
    val3 = forms.IntegerField(label="c")
    val4 = forms.IntegerField(label="d")