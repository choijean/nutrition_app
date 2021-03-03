<!-- omit in toc -->
# Nutrition Application

This is a toy application that performs a search against the Nutritionix API to display the nutritional information about a specific food.

<!-- omit in toc -->
## Table of Contents 📖

- [Features ✨](#features-)
- [Technologies ⚙️](#technologies-️)
- [Getting Started 🛠](#getting-started-)
- [Deploy 🚀](#deploy-)
  - [Development 📝](#development-)
  - [Production 🖥](#production-)
    - [Docker](#docker)
    - [Cloud Registry](#cloud-registry)
  - [Teardown](#teardown)
- [Contributing 👥](#contributing-)
- [Authors & Acknowledgements ✍](#authors--acknowledgements-)
- [License 📄](#license-)

## Features ✨

- Search a food item by name
- Display the basic nutrition information
- Dockerized application
- Run on [Google Cloud Platform](https://cloud.google.com/)

## Technologies ⚙️

- [Python3](https://www.python.org)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja2](https://palletsprojects.com/p/jinja/)
- [Docker](https://hub.docker.com/)
- [Google Cloud Run](https://cloud.google.com/run), [Google Cloud Container Registry](https://cloud.google.com/container-registry), [Google Cloud Build](https://cloud.google.com/cloud-build)

## Getting Started 🛠

Clone the repository and navigate to the project's root directory.

```shell
git clone git@github.com:choijean/nutrition_app.git
cd nutrition_app
```

Create an account at [Nutritionix API](https://developer.nutritionix.com). You will need to keep note of your **Application ID** as well as your **Application Key**

Create a [Docker](https://hub.docker.com/) account.

Visit [Google Cloud Platform Console](https://console.cloud.google.com) and login to enable GCP.

## Deploy 🚀

### Development 📝

Because the Nutritionix API requires an **Application ID** as well as an **Application Key**, we will need to store them as environment variables before running the application locally.

```shell
export NIX_APP_ID=<YOUR_NUTRITIONIX_APP_ID>
export NIX_API_KEY=<YOUR_NUTRITIONIX_APP_KEY>
```

To run the application locally, run the following code:

```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py
```

Navigate to `http://0.0.0.0:5000/` on a browser.

### Production 🖥

We will use [Google Cloud Run](https://cloud.google.com/run) to deploy our application.

Start a new project at
[Google Cloud Platform](https://console.cloud.google.com/). This [document](https://cloud.google.com/resource-manager/docs/creating-managing-projects#console) explains how to create a new project. Alternatively, you can create projects in Cloud Shell.

```shell
gcloud projects create <YOUR_APP_NAME_HERE>
gcloud config set project <YOUR_APP_NAME_HERE>
```

Activate Cloud Shell, clone the repository and navigate to the project's root directory.

```shell
git clone git@github.com:choijean/nutrition_app.git
cd nutrition_app
```

#### Docker

First we build the Docker container and tag it. We also need to login to Docker. Then, we tag the image with our Docker ID. Finally, we can push the image to Docker Hub. Run the following as separate commands.

```shell
docker build -t nutritionapp .
docker login
docker tag final <DOCKER_USERNAME>/nutritionapp
docker push <DOCKER_USERNAME>/nutritionapp
```

#### Cloud Registry

We are going to build the container using [Google Cloud Build](https://cloud.google.com/cloud-build) and then push it to [Google Cloud Container Registry](https://cloud.google.com/container-registry) instead of building and running a DockerHub image.

```shell
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/nutritionapp
gcloud run deploy nutritionapp \
--image gcr.io/${GOOGLE_CLOUD_PROJECT}/nutritionapp \
--update-env-vars NIX_APP_ID=<YOUR_NUTRITIONIX_APP_ID,NIX_API_KEY=<YOUR_NUTRITIONIX_API_KEY>
```

Finally, navigate to the provide URL to see the deployed application.

### Teardown

The easiest way to take down the application is to delete the entire GCP project.

```shell
gcloud projects delete <PROJECT_ID_OR_NUMBER>
```

## Contributing 👥

This is a toy application so I am not taking any contributions.

## Authors & Acknowledgements ✍

Written by [Jean Choi](https://www.github.com/choijean)

## License 📄

This code is licensed under [MIT](https://opensource.org/licenses/MIT).
