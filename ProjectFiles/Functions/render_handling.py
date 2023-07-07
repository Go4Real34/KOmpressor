import os
import subprocess
import time

from .input_handling import get_commands
from .extra_functions import update_progress, get_video_length_in_seconds


def create_commands(settings, temp_location):
    c1 = f"ffmpeg -hide_banner "
    if settings['cut_enabled'] > 0:
        c1 += f"-ss {settings['cut_start']} -to {settings['cut_end']} "
    c1 += f"-i {settings['input_video_path']} "
    c1 += f"-s {settings['resolution']} "
    c1 += f"-b:v {int(settings['bitrate'])} "
    c1 += f"-c:v {settings['output_codec']} "
    c1 += f"-r {settings['fps']} "
    c1 += f"-preset medium "
    if settings['rotation_enabled'] > 0 or \
            settings['horizontal_flip_enabled'] > 0 or \
            settings['vertical_flip_enabled'] > 0:
        c1 += f"-vf \""
        if settings['horizontal_flip_enabled'] > 0:
            c1 += "hflip, "
        if settings['vertical_flip_enabled'] > 0:
            c1 += "vflip, "
        if settings['rotation_enabled'] > 0:
            c1 += f"rotate={settings['rotation_value']}*PI/180, "
        c1 = c1.rstrip(", ")
        c1 += "\" "
    if settings['volume_change_enabled'] > 0:
        c1 += f"-filter:a \"volume={settings['volume_rate']}\" "
    if settings['crf_enabled'] > 0:
        c1 += f"-crf {settings['crf_value']} "
    c1 += f"-pix_fmt yuv420p "
    c1 += f"-movflags +faststart "
    c1 += f"-y "
    c1 += f"{temp_location} "
    c1 += f"-progress pipe:1"

    if settings['speed_enabled'] > 0:
        c2 = f"ffmpeg -hide_banner "
        c2 += f"-i {temp_location} "
        c2 += f"-filter:v \"setpts={settings['video_speed_ratio']}*PTS\" "
        c2 += f"-filter:a \"atempo={settings['audio_speed_ratio']}\" "
        c2 += f"-b:v {int(settings['bitrate'])} "
        c2 += f"-c:v {settings['output_codec']} "
        c2 += f"-preset medium "
        c2 += f"-r {settings['fps']} "
        c2 += f"-pix_fmt yuv420p "
        c2 += f"-movflags +faststart "
        c2 += f"-y "
        c2 += f"{settings['output_video_path']} "
        c2 += f"-progress pipe:1"
    else:
        c2 = None

    return c1, c2


def run_renders(command1, command2, current_settings, raw_command, splitted_command, temp_location, index, total,
                running_on_flask, socketio_reference):
    print(f"\n\nExecuting command: {index + 1}/{total} -> '{raw_command}'")

    print(f"\tStep: 1/{'2' if current_settings['speed_enabled'] > 0 else '1'} "
          f"-> Video Cut - Flip - Rotation - Audio Volume - Compressions settings are being applied.")
    full_duration = get_video_length_in_seconds(current_settings['input_video_path'])
    if current_settings['cut_enabled'] > 0:
        if current_settings['cut_end'] < full_duration:
            full_duration = current_settings['cut_end'] - current_settings['cut_start']
        else:
            full_duration = full_duration - current_settings['cut_start']

    if command2 is None:
        stages = 1
    else:
        stages = 2

    process1 = subprocess.Popen(command1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    start_time1 = time.perf_counter()
    process1_timestamp = update_progress(process1, 1, full_duration, start_time1,
                                         running_on_flask, socketio_reference, 1, stages)
    end_time1 = time.perf_counter()
    print(f"\n\tStep: 1/{'2' if current_settings['speed_enabled'] > 0 else '1'} is completed. " +
          f"Processed {process1_timestamp}/{process1_timestamp} (100.00%), " +
          f"Video Length: {process1_timestamp}, " +
          "Time Elapsed: " + "{:.2f}s".format(round(end_time1 - start_time1, 2)) + ".")

    if command2 is not None:
        print("\n\tStep: 2/2 -> Video Speed - Bitrate - FPS settings are being applied.")

        process2 = subprocess.Popen(command2, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        start_time2 = time.perf_counter()
        process2_timestamp = update_progress(process2, splitted_command[15], full_duration, start_time2,
                                             running_on_flask, socketio_reference, 2, stages)
        end_time2 = time.perf_counter()
        print(f"\n\tStep: 2/2 is completed. " +
              f"Processed: {process2_timestamp}/{process2_timestamp} (100.00%), " +
              f"Video Length: {process2_timestamp}, " +
              "Time Elapsed: " + "{:.2f}s".format(round(end_time2 - start_time2, 2)) + ".")

        print(f"\n\tCommand {index + 1}/{total} is successfully completed in " +
              "{:.2f}s".format(round((end_time1 - start_time1) + (end_time2 - start_time2), 2)) + ".")

        if os.path.exists(temp_location):
            os.remove(temp_location)

    else:
        print(f"\n\tCommand {index + 1}/{total} is successfully completed in " +
              "{:.2f}s".format(round(end_time1 - start_time1, 2)) + ".")

        if os.path.exists(f"{current_settings['output_video_path']}"):
            os.remove(f"{current_settings['output_video_path']}")

        os.rename(temp_location, f"{current_settings['output_video_path']}")


def handle_render():
    raw_commands, splitted_commands, handled_commands = get_commands()

    if len(handled_commands) == 0:
        print("No commands are found to execute. Thanks for using our compressor.")
        return 0

    for index, current_settings in enumerate(handled_commands):
        if raw_commands[index] == "end":
            print("\nAll commands are executed.\nThanks for using our compressor.")
            break

        temporary_first_location = f"temp{current_settings['output_format']}"
        command1, command2 = create_commands(current_settings, temporary_first_location)
        run_renders(command1, command2, current_settings, raw_commands[index], splitted_commands[index],
                    temporary_first_location, index, len(handled_commands) - 1,
                    False, None)


def main():
    return 0


if __name__ == "__main__":
    main()
