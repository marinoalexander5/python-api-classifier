from django.shortcuts import render

from .serializers import ImageSerializers

import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np

class ImagesView(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializers

@api_view(['POST'])
def predict(request)
    try:
        input_feature1 = request.data.get('input_feature1', None)
        # lo mismo para todas las input features. ej:
            # age = request.data.get('age',None)
            # bs_fast = request.data.get('bs_fast',None)
        fields = [input_feature1, age, etc]
        if not None in fields:
            #convert data from string a formato deseado 
            model_path = '/model/model.pkl' # o h5
            classifier = pickle.load(open(model_path, 'rb'))
            prediction = classifier.predict([fields])[0]
            conf_score = np.max(classifier.predict_proba([result])
            predictions = {
                'error': '0',
                'message': 'Successfull',
                'prediction': prediction,
                'confidence_score': conf_score
            }

            else:
                predictions = {
                    'error' : '1',
                    'message': 'Invalid Parameters'                
                }

        except Exception as e:
            predictions = {
                'error' : '2',
                "message": str(e)
            }
    
        return Response(predictions)