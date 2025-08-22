import FreeSimpleGUI as simpleGui

from main import window
from zip_extractor_backend import extract_archive

simpleGui.theme("Black")

select_archive_label = simpleGui.Text("Select archive")
select_archive_input = simpleGui.Input()
choose_archive_button = simpleGui.FileBrowse("Select", key="select_archive_button")

select_destination_label = simpleGui.Text("Select destination to extract")
select_destination_input = simpleGui.Input()
choose_destination_button = simpleGui.FolderBrowse("Select", key="select_destination_button")

extract_button = simpleGui.Button("Extract", key="extract_button")
output_label = simpleGui.Text(key="output", text_color="green")

window = simpleGui.Window("Archive extractor", layout=[[select_archive_label, select_archive_input, choose_archive_button],
                                                       [select_destination_label, select_destination_input, choose_destination_button],
                                                       [extract_button, output_label]])



while True:
    event, values = window.read()
    archive_path = values["select_archive_button"]
    destination_path = values["select_destination_button"]
    extract_archive(archive_path, destination_path)
    window["output"].update(value="Completed")

window.close()