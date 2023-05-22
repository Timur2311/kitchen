
import os
import subprocess
import shutil
import zipfile
import telegram
from telegram import Bot



def perform_backup(request):
    # Step 1: Backup PostgreSQL data
    username = 'YOUR_POSTGRES_USERNAME'
    database_name = 'YOUR_DATABASE_NAME'
    backup_file_path = 'path/to/backup.sql'
    pg_dump_command = f'pg_dump -U {username} -d {database_name} > {backup_file_path}'
    subprocess.call(pg_dump_command, shell=True)

    # Step 2: Backup Django media files
    media_root_path = 'path/to/media_root'
    backup_directory_path = 'path/to/media_backup'
    shutil.copytree(media_root_path, backup_directory_path)

    # Step 3: Create a zip archive
    zip_file_path = 'path/to/backup.zip'
    with zipfile.ZipFile(zip_file_path, 'w') as backup_zip:
        backup_zip.write(backup_file_path, 'backup.sql')
        for folder_name, subfolders, filenames in os.walk(backup_directory_path):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                arcname = os.path.relpath(file_path, backup_directory_path)
                backup_zip.write(file_path, arcname)

    # Step 4: Send the zip file to Telegram
    bot_token = 'YOUR_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'
    bot = Bot(token=bot_token)
    zip_file = open(zip_file_path, 'rb')
    bot.send_document(chat_id=chat_id, document=zip_file)

    # Step 5: Clean up temporary files
    os.remove(backup_file_path)
    shutil.rmtree(backup_directory_path)
    os.remove(zip_file_path)
