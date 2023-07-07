import os

from .extra_functions import get_video_length_in_seconds, print_usage


def handle_command(entered):
    settings = {
        "input_video_path": "input.mp4",
        "output_video_name": "output",
        "resolution": "1920x1080",
        "bitrate": int(8192 * 1024 * 0.8),
        "output_codec": "libx264",
        "output_format": ".mp4",
        "output_video_path": "output.mp4",
        "fps": 30,

        'max_enable': 0,
        'maximum_size': 0,

        'crf_enabled': 0,
        'crf_value': 23,

        'percentage_enabled': 0,
        'percentage_value': 100,

        'speed_enabled': 0,
        'video_speed_ratio': 1.0,
        'audio_speed_ratio': 1.0,

        'volume_change_enabled': 0,
        'volume_rate': 1.0,

        'cut_enabled': 0,
        'cut_start': 0,
        'cut_end': 0,

        'horizontal_flip_enabled': 0,
        'vertical_flip_enabled': 0,

        'rotation_enabled': 0,
        'rotation_type': 'CW',
        'rotation_value': 0
    }

    try:
        if entered[0].upper() != "COMPRESS":
            print("You have not called the command itself. Killing the process.")
            exit(1)

        settings['input_video_path'] = entered[1]
        settings['output_video_name'] = entered[2]
        settings['resolution'] = entered[3].lower()

        settings['bitrate'] = int((int(entered[4]) * 1024) * 0.8)

        if entered[5].upper() in ["H264", "H265", "VP9", "AV1"]:
            if entered[5].upper() == "H264":
                settings['output_codec'] = "libx264"
            elif entered[5].upper() == "H265":
                settings['output_codec'] = "libx265"
            elif entered[5].upper() == "VP9":
                settings['output_codec'] = "libvpx-vp9"
            elif entered[5].upper() == "AV1":
                settings['output_codec'] = "libaom-av1"
        else:
            print(f"The codec you have entered ({entered[5]}) is not supported. Killing the process.")
            exit(1)

        if ((settings['output_codec'] == "libx264" and
             entered[6].lower() in [".mp4", "mp4", ".mov", "mov", ".avi", "avi", ".flv", "flv", ".mkv", "mkv"]) or
                (settings['output_codec'] == "libx265" and
                 entered[6].lower() in [".mp4", "mp4", ".mkv", "mkv"]) or
                (settings['output_codec'] == "libvpx-vp9" and
                 entered[6].lower() in [".webm", "webm", ".mkv", "mkv"]) or
                (settings['output_codec'] == "libaom-av1" and
                 entered[6].lower() in [".mp4", "mp4", ".webm", "webm"])):

            if entered[6].lower().startswith("."):
                settings['output_format'] = entered[6].lower()
            else:
                settings['output_format'] = "." + entered[6].lower()

        else:
            print(f"The output format you have entered ({entered[6]}) is not supported by {entered[5]} codec. "
                  f"Killing the process.")
            exit(1)

        if settings['output_video_name'].endswith(settings['output_format']):
            settings['output_video_path'] = settings['output_video_name']
        else:
            settings['output_video_path'] = settings['output_video_name'] + settings['output_format']

        settings['fps'] = int(entered[7])

        settings['max_enable'] = int(entered[8])
        settings['maximum_size'] = int(float(entered[9]) * 1024 * 1024 * 8)

        settings['crf_enabled'] = int(entered[10])
        settings['crf_value'] = int(entered[11])

        settings['percentage_enabled'] = int(entered[12])
        settings['percentage_value'] = int(entered[13])

        settings['speed_enabled'] = int(entered[14])
        if int(entered[14]) > 0:
            try:
                settings['video_speed_ratio'] = float(1 / float(entered[15]))
                settings['audio_speed_ratio'] = float(entered[15])
            except ZeroDivisionError:
                print("Zero division error detected. Disabling the speed settings.")
                settings['video_speed_ratio'] = 1.0
                settings['audio_speed_ratio'] = 1.0

        settings['volume_change_enabled'] = int(entered[16])
        settings['volume_rate'] = float(entered[17])

        settings['cut_enabled'] = int(entered[18])
        settings['cut_start'] = float(entered[19])
        settings['cut_end'] = float(entered[20])

        settings['horizontal_flip_enabled'] = int(entered[21])
        settings['vertical_flip_enabled'] = int(entered[22])

        settings['rotation_enabled'] = int(entered[23])
        settings['rotation_type'] = entered[24]
        if entered[24] == 'CW':
            settings['rotation_value'] = int(entered[25])
        elif entered[24] == 'CCW':
            settings['rotation_value'] = int((-1) * int(entered[25]))
        else:
            settings['rotation_value'] = 0

        duration = get_video_length_in_seconds(settings['input_video_path'])

        if settings['cut_start'] == 0 and settings['cut_end'] == 0:
            settings['cut_enabled'] = 0

        if settings['cut_enabled'] > 0:
            if settings['cut_start'] > 0 and settings['cut_end'] == 0:
                settings['cut_end'] = duration

            if settings['cut_end'] <= duration:
                duration = settings['cut_end'] - settings['cut_start']
            else:
                duration = duration - settings['cut_start']

        if settings['speed_enabled'] > 0:
            duration = duration / settings['video_speed_ratio']

        filesize = os.path.getsize(settings['input_video_path'])

        if settings['percentage_enabled'] > 0:
            limited_size = (filesize * 8) * (settings['percentage_value'] / 100)
            if settings['max_enable'] > 0:
                if settings['maximum_size'] > limited_size:
                    settings['maximum_size'] = limited_size
            else:
                settings['max_enable'] = 1
                settings['maximum_size'] = limited_size

        if settings['max_enable'] > 0:
            if settings['bitrate'] * duration > settings['maximum_size']:
                settings['bitrate'] = int(settings['maximum_size'] / duration * 0.8)

    except IndexError or ValueError:
        print("You have entered wrong type input. Killing the process.")
        exit(1)

    return settings


def handle_input(single_multiple):
    entered = input()
    if entered.lower().startswith("end"):
        if single_multiple == "single":
            print("You wanted to enter one command but you wanted to end it.")
        elif single_multiple == "multiple":
            print("Saved previous commands. Starting to execute with saved commands if exists.")

        return 'end', None, None

    if not entered.upper().startswith("COMPRESS"):
        if single_multiple == "single":
            print("You wanted to enter one command but you forgot to start with COMPRESS.")
        elif single_multiple == "multiple":
            print("You forgot to start with COMPRESS. Starting to execute with saved commands if exists.")

        return 'end', None, None

    splitted = entered.split(" ")
    if len(splitted) != 26:
        print("You have not entered than 25 values. Each settings has to have one value.")
        return 'end', None, None

    settings = handle_command(splitted)
    return entered, splitted, settings


def get_commands():
    print("Welcome to our 'Web Based Video Compressor using FFMPEG's command line version.")
    single_or_multiple = input("Will you going to render single video or multiple videos (0-1): ")
    try:
        single_or_multiple = int(single_or_multiple)
    except ValueError:
        print("You have entered invalid option. Killing the process.")
        exit(1)

    commands = []
    splitted_settings = []
    raw_commands = []

    if single_or_multiple == 0:
        print_usage()
        print("Please enter the command: ")
        command, splitted, settings = handle_input("single")
        if command != 'end':
            print("Saved command. Starting the render.")
        else:
            print("Thanks for using our compressor.")
            exit(1)

        raw_commands.append(command)
        splitted_settings.append(splitted)
        commands.append(settings)

        raw_commands.append("end")
        splitted_settings.append(None)
        commands.append(None)

    elif single_or_multiple == 1:
        print_usage()
        print("\nPlease enter the commands one by one.\n"
              "If you finish the command just press enter to enter next command to next line.\n"
              "If you provide same output name and output format with the previous commands; "
              "unless you cancel the process, the videos will be overwritten with the last ones.\n"
              "If you done entering command, enter 'end' instead of the command.")
        while True:
            command, splitted, settings = handle_input("multiple")
            raw_commands.append(command)
            splitted_settings.append(splitted)
            commands.append(settings)
            if command == 'end':
                break

    else:
        print("You have entered invalid option. Killing the process.")
        exit(1)

    return raw_commands, splitted_settings, commands


def main():
    return 0


if __name__ == "__main__":
    main()
