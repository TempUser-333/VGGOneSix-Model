from django.shortcuts import render
from rest_framework.views import APIView
import sys
from django.http import HttpResponse
from train_and_test_model import TrainAndTestVGGOneSixModel
# Create your views here.

class TrainAndTestAVGGOneSixModel(APIView):
    def post(self, request):
        l = []
        try:
            print('***********************')
            res = TrainAndTestVGGOneSixModel().test_model(request.data['image_path'])
        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
        else:
            l.append(res)
        finally:
            with open('templates/template_1.html',mode='w') as f:
                f.write('<!doctype html>\n<html>\n<body><p><font color = #FF0000>' + str(l) + 
                        '</p></body>\n</html>')
            return render(request, 'template_1.html', {})
            
        # res = TrainAndTestVGGOneSixModel().test_model(request.data['image_path'])
        # return HttpResponse(res)
 