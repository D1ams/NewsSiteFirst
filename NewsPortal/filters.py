from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Post, Category


class NewsFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=True
    )

    class Meta:
        model = Post
        fields = {
            'name': ['icontains'],
            'date': ['time']
        }


