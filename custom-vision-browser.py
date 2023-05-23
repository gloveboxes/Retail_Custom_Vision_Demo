# image_browser.py

import glob
import PySimpleGUI as sg
import requests
import json
from PIL import Image, ImageTk
import io

CUSTOM_VISION_ENDPOINT = "http://dgnuc:80/image"

TRESHOLD = 0.8


def parse_folder(path):
    images = glob.glob(f'{path}/*.jpg') + glob.glob(f'{path}/*.png')
    return images


def load_image(path, window):

    try:
        with open(path, 'rb') as img:
            image_raw = img.read()

        image = Image.open(io.BytesIO(image_raw))
        image.thumbnail((400, 400))
        photo_img = ImageTk.PhotoImage(image)
        window["image"].update(data=photo_img)

        r = requests.post(CUSTOM_VISION_ENDPOINT, data=image_raw, timeout=5)

        if r.status_code == 200:
            window["prediction"].update(r.text)
            prediction = json.loads(r.text)
            if prediction:

                predictions = prediction.get("predictions")
                if not predictions:
                    return
                
                predictions.sort(key=lambda x: x["probability"], reverse=True)

                window["prediction"].update(
                    "Prediction: " + predictions[0]["tagName"])
                probablity = predictions[0]["probability"]

                text_color = "black" if probablity > TRESHOLD else "red"

                window["confidence"].update(
                    "Confidence: " + str(predictions[0]["probability"]), text_color=text_color, background_color="white")

    except Exception as e:
        print(e)


def main():
    font = ("Arial", 20)
    elements = [
        [
            sg.Text("Image folder"),
            sg.Input(size=(50, 1), enable_events=True, key="file"),
            sg.FolderBrowse(),
        ],
        [
            sg.Button("Prev"),
            sg.Button("Next")
        ],
        [sg.Image(key="image")],
        [sg.Text(key="prediction", font=font)],
        [sg.Text(key="confidence", font=font)],
    ]

    window = sg.Window("Azure Custom Vision Image Scoring",
                       elements, size=(800, 500), icon='logo.ico')
    images = []
    location = 0

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "file":
            images = parse_folder(values["file"])
            if images:
                load_image(images[0], window)
        if event == "Next" and images:
            if location == len(images) - 1:
                location = 0
            else:
                location += 1
            load_image(images[location], window)
        if event == "Prev" and images:
            if location == 0:
                location = len(images) - 1
            else:
                location -= 1
            load_image(images[location], window)

    window.close()


if __name__ == "__main__":
    main()
