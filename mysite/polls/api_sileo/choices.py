from sileo.sileo.resource import Resource
from sileo.sileo.fields import ResourceTypeConvert, ResourceModelManager, ResourceMethodField
from polls.models import Question, Choice
from polls.forms import ChoiceForm
from sileo.sileo.registration import register


class ChoiceResource(Resource):
    query_set = Choice.objects.all()
    fields = [
        'pk', 'choice_text', 'votes'
    ]
    allowed_methods = [
        'get_pk', 'filter', 'create', 'update', 'delete', 'form_dict'
    ]
    update_filter_fields = ['pk']
    delete_filter_fields = ['pk']
    filter_fields = ['pk']
    form_class = ChoiceForm

register('polls', 'choices', ChoiceResource, version='v1')