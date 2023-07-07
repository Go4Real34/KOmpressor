import subprocess
import re
import time
import os


def handle_first_run(which_handling):
    if which_handling == 'console':
        if not os.path.exists("ProjectFiles/TestIO/"):
            os.mkdir("ProjectFiles/TestIO/")
            os.mkdir("ProjectFiles/TestIO/Inputs")
            os.mkdir("ProjectFiles/TestIO/Outputs")
        else:
            if not os.path.exists("ProjectFiles/TestIO/Inputs/"):
                os.mkdir("ProjectFiles/TestIO/Inputs")

            if not os.path.exists("ProjectFiles/TestIO/Outputs/"):
                os.mkdir("ProjectFiles/TestIO/Outputs")

    elif which_handling == 'web':
        if not os.path.exists("ProjectFiles/static/"):
            os.mkdir("ProjectFiles/static/")
            os.mkdir("ProjectFiles/static/inputs")
            os.mkdir("ProjectFiles/static/outputs")
        else:
            if not os.path.exists("ProjectFiles/static/inputs/"):
                os.mkdir("ProjectFiles/static/inputs")
            else:
                for file in os.listdir('ProjectFiles/static/inputs'):
                    os.remove(os.path.join('ProjectFiles/static/inputs', file))

            if not os.path.exists("ProjectFiles/static/outputs/"):
                os.mkdir("ProjectFiles/static/outputs")
            else:
                for file in os.listdir('ProjectFiles/static/outputs'):
                    os.remove(os.path.join('ProjectFiles/static/outputs', file))

    elif which_handling == 'KOmpressor':
        handle_first_run('console')
        handle_first_run('web')

    if os.path.exists('ProjectFiles/current_video.txt'):
        os.remove('ProjectFiles/current_video.txt')


def get_video_length_in_seconds(video_path):
    return float(
        subprocess.check_output(
            [
                'ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of',
                'default=noprint_wrappers=1:nokey=1', video_path
            ]
        )
    )


def update_progress(process, speed, duration, process_start_time, running_on_flask, socketio_reference, stage, stages):
    is_it_updated = False

    progress_duration = (duration * 100) / float(speed)
    seconds = int((progress_duration // 100) % 60)
    minutes = int((progress_duration // (100 * 60)) % 60)
    hours = int((progress_duration // (100 * 60 * 60)) % 24)
    ms = int(progress_duration % 100)
    duration_text = f"{str(hours) if hours >= 10 else '0' + str(hours)}:" \
                    f"{str(minutes) if minutes >= 10 else '0' + str(minutes)}:" \
                    f"{str(seconds) if seconds >= 10 else '0' + str(seconds)}:" \
                    f"{str(ms) if ms >= 10 else '0' + str(ms)}"

    try:
        for line in process.stdout:
            if "frame=" in line:
                match = re.search(r'time=(\d{2}:\d{2}:\d{2}\.\d{2})', line)
                if not is_it_updated:
                    if match is not None:
                        current_time = match.group(1).replace('.', ':')
                        stamp = [int(time_stamp) for time_stamp in current_time.split(':')]
                        time_in_ms = stamp[0] * 60 * 60 * 100 + stamp[1] * 60 * 100 + stamp[2] * 100 + stamp[3]
                        progress = round((time_in_ms / progress_duration) * 100, 2)
                    else:
                        current_time = "00:00:00:00"
                        progress = 0.00

                    print(f"\r\t\t{line.rstrip()}, " +
                          f"Processing: {current_time}/{duration_text} " +
                          "({:.2f}%), ".format(progress) +
                          "Time Elapsed: " + "{:.2f}s".format(round(time.perf_counter() - process_start_time, 2)) + ".",
                          end="", flush=True)
                    if running_on_flask:
                        dict_to_emit = {
                            'current': current_time,
                            'end': duration_text,
                            'progress': progress,
                            'stage': stage,
                            'total': stages,
                            'complete': False
                        }
                        socketio_reference.emit('update progress', dict_to_emit)

                is_it_updated = not is_it_updated

        if running_on_flask:
            dict_to_emit = {
                'current': duration_text,
                'end': duration_text,
                'progress': 100.00,
                'stage': stage,
                'total': stages,
                'complete': True
            }
            socketio_reference.emit('update progress', dict_to_emit)
        return duration_text

    except KeyboardInterrupt:
        process.terminate()
        print("Process cancelled. Killing the process.")
        exit(1)

    except Exception as e:
        process.terminate()
        print(f"Critical exception occured: {e}. Killing the process.")
        exit(1)


def print_usage():
    print('If you dont want to use a certain compression method, just enter 0 for that value.')
    print("\nUSAGE (enter the command in single line):\n\n"
          "COMPRESS 'input_video_path', 'output_video_name',\n"
          "'resolution (default 1920x1080)', 'bitrate_in_kbps' (default 8192),\n"
          "'output_codec' [possible options: H264, H265, VP9, AV1] (default H264)\n"
          "'format' (default .mp4) [possible options:\n"
          "\t\tH264: '.mp4', '.mov', '.avi', '.flv', '.mkv'\n"
          "\t\tH265: '.mp4'1, '.mkv'\n"
          "\t\tVP9: '.webm', '.mkv'\n"
          "\t\tAV1: '.mp4', '.webm'],\n"
          "'fps' (default 30),\n"
          "'max_enabled', 'maximum_size_in_MB' (default 50)\n"
          "'will_be_crf', 'value_if_crf' (default 23)\n"
          "'will_be_percentage', 'value_if_percentage' (default 100)\n"
          "'will_change_speed', 'speed_if_speed' (default 1.0)\n"
          "'will_change_volume', 'volume_if_change' (default 1.0)\n"
          "'will_be_cut', 'start_of_cut', 'end_of_cut'\n"
          "'horizontal_flip_enabled', 'vertical_flip_enabled'\n"
          "'will_rotate', 'side_of_rotate' (default CW), 'rotation_angle' (default 0).")


def main():
    return 0


if __name__ == "__main__":
    main()
