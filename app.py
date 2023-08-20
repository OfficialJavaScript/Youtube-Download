#Copyright 2023 Sebastian Johnstone - All Rights Reserved
#This application is for educational purposes and is not intended for Illegal uses - To download anything with this tool you must have explicit permission from the owner of the video/audio.
#By using this application you agree to my Terms and Conditions - I take no responsibility for any illegal activity resulting in downloaded files using this application.

from flask import Flask, render_template, request, redirect, jsonify
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.json['video_url']
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        video_title = yt.title
        thumbnail_url = yt.thumbnail_url

        download_folder = 'downloads/'
        os.makedirs(download_folder, exist_ok=True)
        video_stream.download(download_folder)

        response = {
            'status': 'success',
            'title': video_title,
            'thumbnail_url': thumbnail_url
        }
    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e)
        }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
