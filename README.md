# Custom Vision Retail for Vision Impaired people

This project is a demo of how Custom Vision can be used to help vision impaired people shop for groceries. The demo uses a Custom Vision model to identify grocery items and then uses text to speech to read the item name and price to the user.

The project has been tested on the following platforms:

1. Windows 11 on Intel and ARM
2. Ubuntu 20.04 on Intel and ARM
3. MacOS Ventura on ARM

## Clone the repo

Clone this repository.

```bash
git clone https://github.com/gloveboxes/Retail_Custom_Vision_Demo.git
```

## Install Dependencies

1. Python. This project was developed using Python 3.11.3. You can download the latest version of Python from [here](https://www.python.org/downloads/). I'd expect the app to work with any version of Python 3.10 or higher.
1. Install the Python dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

2. On Windows, you may need to install the C++ Redistributable. The C++ Redistributable is required by the Pillow Python library. If the solution fails and reports `ImportError: DLL load failed while importing _imaging:` then you need to manually install the [Microsoft Visual C++ Redistributable latest supported downloads](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist)

## Custom Vision Model

The Custom Vision model can be used as a cloud service or deployed locally. To deploy the model locally, follow these instructions.

1. Install Docker on your local machine. You can download Docker from [here](https://www.docker.com/products/docker-desktop)
1. Change to the `custom_vision_docker_linux` folder, from the command line, run the following command to build the Docker image:

    ```bash
    docker build -t custom_vision_model .
    ```
2. Build the Custom Vision Docker image

    ```bash
    docker build -t custom_vision_model .
    ```
3. Run the Custom Vision Docker container using the following command:

    ```bash
    docker run -p 80:80 -d custom_vision_model
```

### Create your own Custom Vision model

You can create your own custom vision model. To do this, follow the instructions below to download and build your own custom model [here](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/get-started-build-detector)


# Usage

1. Update the `CUSTOM_VISION_ENDPOINT` variable in the `custom-vision-browser.py` file with the endpoint of your Custom Vision model. For example, if you are running the model locally using Docker, the endpoint will be `http://localhost:80/image`.
1. Run the `custom-vision-browser.py` file using the following command:

    ```bash
    python3 custom-vision-browser.py
    ```
