from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

#from joblib import load
#model = load('./savedModels/model.joblib')

import tensorflow as tf
from keras.models import load_model

# Load the trained model
model = load_model('./savedModels/model.h5')

'''

#from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
model = tf.keras.models.load_model('./savedModels/model.h5')


@csrf_exempt 
def mainpage(request):
    if request.method == 'POST': 
        class_names = ['Mild_Demented', 'Very_Mild_Demented', 'Non_Demented', 'Moderate_Demented']
        img_size = (128, 128)

        
        Pyramidal = request.POST['Pyramidal']
        Cerebellar = request.POST['Cerebellar']
        Brainstem = request.POST['Brainstem']
        Sensory = request.POST['Sensory']
        Bowel = request.POST['Bowel']
        Visual = request.POST['Visual']
        Mental = request.POST['Mental']
        walk = request.POST['walk']
        Y_pred = model.predict([[Pr, Brainstem, Sensory, Bowel, Visual, Mental, walk]])
        if Y_pred[0] == 0:
            Suggestion = 'You are not suffering from MS. It is suggested that visit a neurologist for further examination.'  
            return render(request, 'page2.html', {'Suggestion' : Suggestion})
        else:
            Suggestion = 'You need to take an MRI image at a medical center and then press the button below to continue the process'
            return render(request, 'page2.html', {'Suggestion' : Suggestion})
    return render(request, 'index.html')
'''
from django.shortcuts import render
import numpy as np
from PIL import Image

def index(request):
    if request.method == 'POST':
        class_names = ['Mild_Demented', 'Very_Mild_Demented', 'Non_Demented', 'Moderate_Demented']
        img_size = (128, 128)
        if 'image' in request.FILES:
            uploaded_file = request.FILES.get('image')
            image = Image.open(uploaded_file)
              
            # Convert the image to a numpy array
            img_array = np.array(image)
            
            # Add a batch dimension to the array to match the model's input shape
            img_array = np.expand_dims(img_array, axis=0)
            
            # Make a prediction using the model
            #prediction = model.predict(img_array)
            Suggestion = 'djff'
            return render(request, 'index.html', {'Suggestion' : Suggestion})
    
    return render(request, 'index.html')
'''

def index(request):
    if request.method == 'POST':
        # Get the uploaded file from the request
        uploaded_file = request.FILES.get['image']

        # Do something with the uploaded file (e.g. process it in Python)
        # ...

        # Return a response to the client
        Suggestion = 'ggod'
        return render(request, 'index.html', {'Suggestion' : Suggestion})
    else:
        Suggestion = 'bad'
        return render(request, 'index.html', {'Suggestion' : Suggestion})

'''