import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from werkzeug.utils import secure_filename

from Functions.web_handling import web_input_to_command_converter
from Functions.render_handling import create_commands, run_renders
from Functions.extra_functions import handle_first_run


UPLOAD_FOLDER = 'ProjectFiles\\static\\inputs'
ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi', 'flv', 'mkv', 'webm'}

app = Flask(__name__)
socketIO = SocketIO(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

video_out = ''


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_page():
    return render_template('upload_page.html')


@app.route('/rendering', methods=['POST'])
def rendering():
    global video_out
    command, splitted, settings = web_input_to_command_converter(request.form.to_dict())
    command1, command2 = create_commands(settings, f"temp.{splitted[6]}")
    run_renders(command1, command2, settings, command, splitted, f"temp.{splitted[6]}", 0, 1, True, socketIO)
    video_in = settings['input_video_path'].split('\\')[-1]
    video_out = settings['output_video_path'].split('\\')[-1]
    return render_template('video_settings.html', input_video_path=video_in)


@app.route('/video_settings', methods=['POST'])
def video_settings():
    if 'video_file' not in request.files:
        return render_template('upload_page.html', error='No video file provided.')

    video_file = request.files['video_file']

    if video_file.filename == '':
        return render_template('upload_page.html', error='No video file selected.')

    if not allowed_file(video_file.filename):
        return render_template('upload_page.html', error='Invalid video file format.')

    filename = secure_filename(video_file.filename)
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open('ProjectFiles/current_video.txt', 'w') as f:
        f.write(os.path.abspath(video_path))
    video_file.save(video_path)

    return render_template('video_settings.html', input_video_path=filename)


def main():
    file_path = os.path.abspath(__file__)
    project_files_folder = file_path.rstrip("web_compressor.py").rstrip("\\")
    kompressor_folder_path = project_files_folder.rstrip("ProjectFiles").rstrip("\\")
    os.chdir(kompressor_folder_path)

    handle_first_run('web')

    socketIO.run(app=app, debug=False, allow_unsafe_werkzeug=True)

    return 0


if __name__ == '__main__':
    main()
