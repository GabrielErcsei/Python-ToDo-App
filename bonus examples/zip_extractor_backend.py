import zipfile

def extract_archive(archive_path: str, destination_directory: str):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(destination_directory)


if __name__ == "__main__":
    extract_archive("bonus examples/zip_destination/compressed.zip", "bonus examples/files")