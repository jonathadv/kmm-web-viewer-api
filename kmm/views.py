from django.core import serializers
from django.http import HttpResponse, HttpRequest
from django.views.generic import View

from kmm.models import Kmmtransactions

class Transactions(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        data = serializers.serialize("json", Kmmtransactions.objects.all())
        return HttpResponse(data, content_type="application/json")
