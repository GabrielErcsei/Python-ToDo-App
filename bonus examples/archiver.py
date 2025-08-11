import zipfile as archiver
import pathlib

def create_archive(filepaths: list, destination: str):
    with archiver.ZipFile(pathlib.Path(destination, "compressed.zip"), 'w') as archive:
        for path in filepaths:
            path = pathlib.Path(path)
            archive.write(path, arcname=path.name)


# for testing purposes
if __name__ == "__main__":
    create_archive(filepaths=["bonus1.py", "bonus2.py"], destination="zip_destination")