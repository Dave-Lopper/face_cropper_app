# Face cropping API
Welcome to the face cropper API !  
This API will allow you to :   
- Automatically detect faces on a provided picture
- Download the biggest one

## API doc
### crop_largest_face/ endpoint (POST)    
#### Required param :
***image*** : The image to be cropped
#### Optional param :
***attachment*** : Optional, if provided and set to "true", the image will be
downloaded as a response

