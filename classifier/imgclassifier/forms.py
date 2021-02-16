from django import forms
from .models import ImgClassifier
from keras.preprocessing import model_from_json
import numpy as np

class ImgClassifierForm(forms.modelForm):
    class Meta:
        model = ImgClassifier
        fields = ('image', 'prediction')

        def create(self, validated_data):
            classification_obj = ImgClassifier.objects.create(**validated_data)

            model_json_path  = '../model/model_architecture.json'
            model_weigth_path = '../model/model_weights.h5'

            # convert image to array
            img = image.load_img(classification_obj.image.file.filename, target_size=(150,150))
            img_array = image.image_to_array(img)
            img_array.shape = (1, 150, 150, 3)

            self.update_state(state='load_model', meta={'progess': 25})

            # load model
            with open(model_json_path, 'r') as f:
                model = model_from_json(f.read())

            model.load_weigths(model_weight_path)

            # predict
            prediction = model.predict(img_array, verbose=1)
            if prediction == 0:
                result = 'clase 1'
            elif prediction == 1:
                result = 'clase 2'
            elif prediction == 1:
                result = 'clase 2'
            elif prediction == 1:
                result = 'clase 2'
            elif prediction == 1:
                result = 'clase 2'

            classification_obj.prediction = result
            return classificatoin_obj