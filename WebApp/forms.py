from WebApp.models import BCand,GCand,Voter
from django import forms
class VForm(forms.Form):
    AdNo=forms.IntegerField()
    Dobv=forms.DateField()


class TForm(forms.Form):
    Tid=forms.CharField(max_length=15)
    Tpass=forms.CharField(max_length=20)


class Boy(forms.ModelForm):
    class Meta:
        model = BCand
        fields = [
            'Bname',
            'Bhouse',
            'Bpic',
            'Bclass',
            'Bcount'
        ]


class Girl(forms.ModelForm):
    class Meta:
        model = GCand
        fields = [
            'Gname',
            'Ghouse',
            'Gpic',
            'Gclass',
            'Gcount'
        ]


class Voters(forms.ModelForm):
    class Meta:
        model = Voter
        fields = [
            'Vname',
            'Votedone',
            'AdmisNo',
            'Vhouse',
            'Vdob',
            'Vclass',
            'GCand',
            'BCand'

        ]