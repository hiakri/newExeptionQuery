#!usr/bin/env python
# coding: utf-8


from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def __unicode__(self):
        return self.file
