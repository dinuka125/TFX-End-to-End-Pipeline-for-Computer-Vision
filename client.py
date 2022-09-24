import requests
import json
import cv2



def _prediction(data):
    headers = {"content-type": "application/json"}
    payload = {"instances":[{"raw_image":data.tolist()}]}
    json_response = requests.post(url='http://localhost:8502/v1/models/fashion_model:predict',json=payload ,headers=headers)
    json_result = json.loads(json_response.text)["predictions"]
    return json_result



img1 = cv2.imread("image_path.jpg")
img = cv2.resize(img1,(100,100))
img_pred = _prediction(img)
if img_pred[0][0]  == 0.0:
    print("Prediction output is : dog")
else:
    print("Prediction output is : cat")