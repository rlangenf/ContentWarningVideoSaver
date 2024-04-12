import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def main():
    # get the path to the temp folder
    temp_folder = Path(os.getenv('LOCALAPPDATA')) / 'Temp' / 'rec'

    # get the path to the desktop folder
    desktop_folder = Path(os.getenv('USERPROFILE')) / 'Desktop'

    # get all main folders
    main_folders = [f for f in temp_folder.iterdir() if f.is_dir()]

    # sort main folder list oldest first
    main_folders.sort(key=os.path.getctime)

    print(f'Found {len(main_folders)} Folders')

    # print list of main folders
    for main_folder in main_folders:
        dt = datetime.fromtimestamp(main_folder.stat().st_ctime)
        print(f'  {main_folders.index(main_folder) + 1}. {main_folder.name} (created: {dt})')

    print('\nPlease ensure that the listed folder names are actually part of your local temp folder under:\n    '
          f'    {Path(os.getenv("LOCALAPPDATA")) / "Temp" / "rec"}\n')

    # press enter to continue
    input('Press Enter to continue...')

    # to ensure we are not messing with some files we don't want to mess with, we will ask the user to confirm the operation
    while True:
        user_input = input('Enter the number of the folder to concatenate, "all" to concatenate all, or "none" to exit:')
        if user_input.lower() == 'none':
            sys.exit(0)
        elif user_input.lower() == 'all':
            break
        elif user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= len(main_folders):
                main_folders = [main_folders[user_input - 1]]
                break
            else:
                print('Invalid input. Please enter a valid number.')
        else:
            print('Invalid input. Please enter a valid number or "all" or "none".')

    day = 1

    # iterate over all main folders
    for main_folder in main_folders:
        # get the name of the main folder
        main_folder_name = main_folder.name

        # if the main folder contains a file "videoList.txt", use it to concatenate the video files
        video_list_file = main_folder / 'videoList.txt'
        if video_list_file.exists():
            print(f'Found videoList.txt in {main_folder_name}')

            # create a folder for the output video
            output_folder = desktop_folder / 'output' / f"day {day} - {main_folder_name}"
            output_folder.mkdir(parents=True, exist_ok=True)

            # concatenate the video files
            # ffmpeg -f concat -safe 0 -i input.txt -c copy output.webm
            input_file = video_list_file
            output_file = output_folder / 'output.webm'

            print(input_file)

            subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', input_file, '-c', 'copy', output_file])

            print(f'Concatenated video files from {main_folder} into {output_file}')
        else:
            # get all subfolders
            subfolders = [f for f in main_folder.iterdir() if f.is_dir()]

            # create a list of all video files
            video_files = []
            for subfolder in subfolders:
                video_file = subfolder / 'output.webm'
                if video_file.exists():
                    video_files.append(video_file)
                    # after adding, sort the list oldest video first
                    video_files.sort(key=os.path.getmtime)

            # check if there are any video files
            if len(video_files) == 0:
                print(f'No video files found in {main_folder_name}')
                continue

            # create a folder for the output video; the folder name is output-{date-of-newest-video}
            output_folder = desktop_folder / 'output' / f"day {day} - {main_folder_name}"
            output_folder.mkdir(parents=True, exist_ok=True)

            # concatenate the video files
            # ffmpeg -f concat -safe 0 -i input.txt -c copy output.webm
            input_file = output_folder / 'input.txt'
            with open(input_file, 'w') as f:
                for video_file in video_files:
                    f.write(f"file '{video_file}'\n")

            output_file = output_folder / 'output.webm'
            print(input_file)

            subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', input_file, '-c', 'copy', output_file])

            print(f'Concatenated {len(video_files)} video files into {output_file}')

        day += 1

    print(f'\nSaved output video(s) to {desktop_folder / "output"}')
    input('Press Enter to exit...')


if __name__ == '__main__':
    main()
