# import shutil and os
# import shutil, os

# source_dir = 'C:\\Users\\User\\Desktop\\file1'
# destination_dir_audio = 'C:\\Users\\User\\Downloads\\audio'
# destination_dir_video = 'C:\\Users\\User\\Downloads\\video'
# destination_dir_picture = 'C:\\Users\\User\\Downloads\\picture'
# destination_dir_zip = 'C:\\Users\\User\\Downloads\\zip'
# destination_dir_geojson = 'C:\\Users\\User\\Downloads\\geojson'
# destination_dir_pdf = 'C:\\Users\\User\\Downloads\\pdf'


# file_names = os.listdir(source_dir)

# for file_name in file_names:
    # if os.path.join(source_dir, file_name).endswith('.mp3'):
    #     shutil.move(os.path.join(source_dir, file_name), destination_dir_audio)

    # if os.path.join(source_dir, file_name).endswith('.mp4'):
    #     shutil.move(os.path.join(source_dir, file_name), destination_dir_video)

    # if os.path.join(source_dir, file_name).endswith('.zip'):
    #     shutil.move(os.path.join(source_dir, file_name), destination_dir_zip)

    # if os.path.join(source_dir, file_name).endswith('.geojson'):
    #     shutil.move(os.path.join(source_dir, file_name), destination_dir_geojson)

    # if os.path.join(source_dir, file_name).endswith('.pdf'):
    #     shutil.move(os.path.join(source_dir, file_name), destination_dir_pdf)

    # if os.path.join(source_dir, file_name).endswith('.jpg'):
    #     shutil.move(os.path.join(source_dir, file_name), destination_dir_picture)

    # if os.path.join(source_dir, file_name).endswith('.png'):
    #     shutil.move(os.path.join(source_dir, file_name), destination_dir_picture)
    

# print("Success!!!!!")

import shutil, os


def file_manager(source_dir, destination_dir):
    source_dir = 'C:\\Users\\User\\Downloads'
    destination_dir_audio = 'C:\\Users\\User\\Downloads\\audio'
    destination_dir_video = 'C:\\Users\\User\\Downloads\\video'
    destination_dir_picture = 'C:\\Users\\User\\Downloads\\picture'
    destination_dir_zip = 'C:\\Users\\User\\Downloads\\zip'
    destination_dir_geojson = 'C:\\Users\\User\\Downloads\\geojson'
    destination_dir_pdf = 'C:\\Users\\User\\Downloads\\pdf'

    file_names = os.listdir(source_dir)

    for file_name in file_names:
        if os.path.join(source_dir, file_name).endswith('.mp3'):
            shutil.move(os.path.join(source_dir, file_name), destination_dir_audio)

        if os.path.join(source_dir, file_name).endswith('.mp4'):
            shutil.move(os.path.join(source_dir, file_name), destination_dir_video)

        if os.path.join(source_dir, file_name).endswith('.zip'):
            shutil.move(os.path.join(source_dir, file_name), destination_dir_zip)

        if os.path.join(source_dir, file_name).endswith('.geojson'):
            shutil.move(os.path.join(source_dir, file_name), destination_dir_geojson)

        if os.path.join(source_dir, file_name).endswith('.pdf'):
            shutil.move(os.path.join(source_dir, file_name), destination_dir_pdf)

        if os.path.join(source_dir, file_name).endswith('.jpg'):
            shutil.move(os.path.join(source_dir, file_name), destination_dir_picture)

        if os.path.join(source_dir, file_name).endswith('.png'):
            shutil.move(os.path.join(source_dir, file_name), destination_dir_picture)

        print("success!!!!!")



file_manager('C:\\Users\\User\\Downloads', 'C:\\Users\\User\\Downloads\\audio')
file_manager('C:\\Users\\User\\Downloads', 'C:\\Users\\User\\Downloads\\videos')
file_manager('C:\\Users\\User\\Downloads', 'C:\\Users\\User\\Downloads\\picture')
file_manager('C:\\Users\\User\\Downloads', 'C:\\Users\\User\\Downloads\\pdf')
file_manager('C:\\Users\\User\\Downloads', 'C:\\Users\\User\\Downloads\\geojson')
file_manager('C:\\Users\\User\\Downloads', 'C:\\Users\\User\\Downloads\\zip')