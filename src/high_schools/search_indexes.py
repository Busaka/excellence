import datetime
from haystack import indexes
from high_schools.models import HighSchool


class HighSchoolIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='high_school_name')
    published = indexes.DateTimeField(model_attr='published')

    def get_model(self):
        return HighSchool

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(published__lte=datetime.datetime.now())
