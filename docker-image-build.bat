SET PATH=%PATH%;C:\Users\krish\Documents\Google-Cloud-SDK\bin
SET IMAGE_NAME=gcr.io/nu-microservices-1/pymicro-image2:%BUILD_NUMBER%
cd D:\Programming\Web Frameworks\Tornado\Microservices-1\Source
gcloud builds submit --tag %IMAGE_NAME% .
