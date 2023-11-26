from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User , Review
class UserCreationFormByMe(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'phone_num',

        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'title',
            'body',
            'rating'
        ]

    title = forms.CharField(label='Заголовок', max_length=255)
    body = forms.CharField(label='Текст отзыва', widget=forms.Textarea)
    rating = forms.ChoiceField(label='Рейтинг', choices=Review.RATING_CHOICES)

    