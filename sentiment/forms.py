from django.forms import ModelForm, EmailField, CharField, Textarea

from .models import Review


class ReviewForm(ModelForm):
   author_email = EmailField(max_length=80, help_text='Required', required=True, label="Email")
   author = CharField(max_length=150, label='Your name')
   review_title = CharField(max_length=300, label='Title', required=True)
   review_body = CharField(widget=Textarea({}), label='Feedback', required=True)

   class Meta:
       model = Review
       fields = ['author', 'author_email', 'review_title', 'review_body', 'sentiment_score']