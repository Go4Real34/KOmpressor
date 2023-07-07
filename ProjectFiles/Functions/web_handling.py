import os

from .extra_functions import get_video_length_in_seconds
from .input_handling import handle_command


def fill_missing_input(input_dict):
    try:
        with open('ProjectFiles/current_video.txt', 'r') as f:
            video = f.read()
    except FileNotFoundError:
        video = os.path.join(os.path.abspath(__file__), 'ProjectFiles\\static\\outputs\\input.mp4')

    video_file_location = video.split('\\')

    if 'input_path' not in input_dict:
        input_dict.update({'input_path': 'ProjectFiles\\static\\inputs\\' +
                                         f'{video_file_location[-1]}'})

    if 'output_path' not in input_dict:
        input_dict.update({'output_name': 'ProjectFiles\\static\\outputs\\' +
                                          f'{video_file_location[-1].split(".")[0]}'})

    if 'width' not in input_dict or 'height' not in input_dict:
        input_dict.update({'width': '1920',
                           'height': '1080'})

    if 'bitrate' not in input_dict:
        input_dict.update({'bitrate': str(int(8192 * 0.8))})

    if 'output_codec' not in input_dict:
        input_dict.update({'output_codec': 'H264'})

    if 'output_format' not in input_dict:
        input_dict.update({'output_format': 'mp4'})

    if 'fps' not in input_dict:
        input_dict.update({'fps': '30'})

    if 'max_filesize' not in input_dict:
        input_dict.update({'max_filesize': '0'})

    if 'max_enable' not in input_dict:
        input_dict.update({'max_enable': 'off',
                           'max_filesize': '0'})

    if 'crf_value' not in input_dict:
        input_dict.update({'crf_value': '23'})

    if 'crf_enable' not in input_dict:
        input_dict.update({'crf_enable': 'off',
                           'crf_value': '0'})

    if 'percentage_value' not in input_dict:
        input_dict.update({'percentage_value': '100'})

    if 'percentage_enable' not in input_dict:
        input_dict.update({'percentage_enable': 'off',
                           'percentage_value': '0'})

    if 'speed' not in input_dict:
        input_dict.update({'speed': '1.0'})

    if 'change_speed' not in input_dict:
        input_dict.update({'change_speed': 'off',
                           'speed': '0'})

    if 'volume' not in input_dict:
        input_dict.update({'volume': '1.0'})

    if 'change_volume' not in input_dict:
        input_dict.update({'change_volume': 'off',
                           'volume': '0'})

    if 'start_time' not in input_dict:
        input_dict.update({'start_time': '0'})

    if 'start_enable' not in input_dict:
        input_dict.update({'start_enable': 'off',
                           'start_time': '0'})

    if 'end_time' not in input_dict:
        input_dict.update({'end_time': str(get_video_length_in_seconds(video))})

    if 'end_enable' not in input_dict:
        input_dict.update({'end_enable': 'off',
                           'end_time': '0'})

    if 'cut' not in input_dict:
        input_dict.update({'cut': 'off',
                           'start_enable': 'off',
                           'start_time': '0',
                           'end_enable': 'off',
                           'end_time': '0'})

    if 'horizontal_flip' not in input_dict:
        input_dict.update({'horizontal_flip': 'off'})

    if 'vertical_flip' not in input_dict:
        input_dict.update({'vertical_flip': 'off'})

    if 'rotate_direction' not in input_dict:
        input_dict.update({'rotate_direction': 'clockwise'})

    if 'rotate_degree' not in input_dict:
        input_dict.update({'rotate_degree': '0'})

    if 'rotate' not in input_dict:
        input_dict.update({'rotate': 'off',
                           'rotate_direction': 'clockwise',
                           'rotate_degree': '0'})

    return input_dict


def web_input_to_command_converter(input_dict):
    input_dict = fill_missing_input(input_dict)

    input_video_path = input_dict['input_path']
    output_video_name = input_dict['output_name']
    resolution = input_dict['width'] + 'x' + input_dict['height']
    bitrate = input_dict['bitrate']
    output_codec = input_dict['output_codec']
    output_format = input_dict['output_format']
    fps = input_dict['fps']

    if input_dict['max_enable'] == 'on':
        will_be_max = '1'
        maximum_size_in_mb = input_dict['max_filesize'].replace(',', '.')
    else:
        will_be_max = '0'
        maximum_size_in_mb = '0'

    if input_dict['crf_enable'] == 'on':
        will_be_crf = '1'
        value_if_crf = input_dict['crf_value']
    else:
        will_be_crf = '0'
        value_if_crf = '0'

    if input_dict['percentage_enable'] == 'on':
        will_be_percentage = '1'
        value_if_percentage = input_dict['percentage_value']
    else:
        will_be_percentage = '0'
        value_if_percentage = '0'

    if input_dict['change_speed'] == 'on':
        will_change_speed = '1'
        speed_if_change = input_dict['speed'].replace(',', '.')
    else:
        will_change_speed = '0'
        speed_if_change = '0'

    if input_dict['change_volume'] == 'on':
        will_change_volume = '1'
        volume_if_change = input_dict['volume'].replace(',', '.')
    else:
        will_change_volume = '0'
        volume_if_change = '0'

    if input_dict['cut'] == 'on':
        will_be_cut = '1'
        if input_dict['start_enable'] == 'on':
            start_of_cut = input_dict['start_time'].replace(',', '.')
        else:
            start_of_cut = '0'

        if input_dict['end_enable'] == 'on':
            end_of_cut = input_dict['end_time'].replace(',', '.')
        else:
            end_of_cut = '0'
    else:
        will_be_cut = '0'
        start_of_cut = '0'
        end_of_cut = '0'

    if input_dict['horizontal_flip'] == 'on':
        horizontal_flip_enabled = '1'
    else:
        horizontal_flip_enabled = '0'

    if input_dict['vertical_flip'] == 'on':
        vertical_flip_enabled = '1'
    else:
        vertical_flip_enabled = '0'

    if input_dict['rotate'] == 'on':
        will_rotate = '1'
        if input_dict['rotate_direction'] == 'clockwise':
            side_of_rotate = 'CW'
        elif input_dict['rotate_direction'] == 'counterclockwise':
            side_of_rotate = 'CCW'
        else:
            side_of_rotate = 'CW'
        rotation_angle = input_dict['rotate_degree']
    else:
        will_rotate = '0'
        side_of_rotate = 'CW'
        rotation_angle = '0'

    entered = f'COMPRESS {input_video_path} {output_video_name} ' \
              f'{resolution} {bitrate} ' \
              f'{output_codec} ' \
              f'{output_format} ' \
              f'{fps} ' \
              f'{will_be_max} {maximum_size_in_mb} ' \
              f'{will_be_crf} {value_if_crf} ' \
              f'{will_be_percentage} {value_if_percentage} ' \
              f'{will_change_speed} {speed_if_change} ' \
              f'{will_change_volume} {volume_if_change} ' \
              f'{will_be_cut} {start_of_cut} {end_of_cut} ' \
              f'{horizontal_flip_enabled} {vertical_flip_enabled} ' \
              f'{will_rotate} {side_of_rotate} {rotation_angle}'

    splitted = entered.split(' ')
    settings = handle_command(splitted)

    return entered, splitted, settings


def main():
    return 0


if __name__ == '__main__':
    main()
