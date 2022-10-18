# Took linux-based base image of python with slim buster from docker hub
FROM python:3.8-slim-buster

# Copied all the dependencies in req.txt to current directory
COPY requirements.txt .

# Run installation of dependencies
RUN pip install -r requirements.txt

# Copy all the contents to our current directory
COPY . .

# The EXPOSE instruction in a Dockerfile refers to the container port. Need to give a port to docker container to
# interact with local host.
EXPOSE 5000

# To run the flask file which is an executable parameter and need to give local host port
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

# Problem encountered was the enormous size of the image, it was 2.3gb which could have created problem on deploying
# it over AWS-ECR as under free tier only 500 mb is allowed

# So in order to resize it first made a dockerignore file and in it specified the venv folder which contained all virtual
# environment libraries and operating python version which will ignore it completely and wont get included in image file.
# This brought down the size to 1.29gb

# Next tried alpine based python base image but that had lots of issues with basic libraries such as numpy and was not able
# to create image, so gone with slim-buster, it created image successfully and brought down image size further to 490mb,
# and total compressed size of the image was ~230mb which is perfectly fine to deploy over AWS.

# Could have also used multi-layer staging to compress size of image more.