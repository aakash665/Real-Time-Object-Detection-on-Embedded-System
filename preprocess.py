import cv2

def preprocess_image(image, target_height, target_width):
    image_resized = cv2.resize(image, (target_width, target_height))
    image_normalized = image_resized / 255.0 
    return np.expand_dims(image_normalized, axis=0).astype(np.float32) 