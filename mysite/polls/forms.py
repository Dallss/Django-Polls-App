from django import forms
from polls.models import *
from dataclasses import fields
from sileo.sileo.forms import ModelForm

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = [
            'question_text',
            'pub_date'
        ]

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = [
            'choice_text',
            'votes',
            'question'
        ]
