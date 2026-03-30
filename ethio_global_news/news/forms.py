from django import forms
from .models import News, Category

class NewsForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",  # Placeholder
        required=True  # Force selection
    )

    class Meta:
        model = News
        fields = ['title', 'category', 'content', 'image']