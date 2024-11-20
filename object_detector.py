import numpy as np
import tensorflow as tf
from preprocess import preprocess_image
from utils import load_labels

class ObjectDetector:
    def __init__(self, model_path, labels_path):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        self.labels = load_labels(labels_path)

    def detect(self, image):
        input_shape = self.input_details[0]['shape']
        
        preprocessed_image = preprocess_image(image, input_shape[1], input_shape[2])
        
        self.interpreter.set_tensor(self.input_details[0]['index'], preprocessed_image)
        self.interpreter.invoke()

        boxes = self.interpreter.get_tensor(self.output_details[0]['index'])[0] 
        class_ids = self.interpreter.get_tensor(self.output_details[1]['index'])[0] 
        scores = self.interpreter.get_tensor(self.output_details[2]['index'])[0] 

        detections = []
        for i in range(len(scores)):
            if scores[i] > 0.5:  
                box = boxes[i]
                class_id = int(class_ids[i])
                detections.append({
                    'label': self.labels[class_id],
                    'confidence': scores[i],
                    'box': [int(box[1] * image.shape[1]), int(box[0] * image.shape[0]),
                            int(box[3] * image.shape[1]), int(box[2] * image.shape[0])]
                })
        
        return detections