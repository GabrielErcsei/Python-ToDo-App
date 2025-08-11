import FreeSimpleGUI as simpleGui
import archiver

file_select_label = simpleGui.Text("Select files to compress")
file_select_input_box =  simpleGui.Input()
select_button = simpleGui.FileBrowse("Select file", key="select_file_button")

destination_label = simpleGui.Text("Select files to compress")
destination_input_box =  simpleGui.Input()
folder_select_button = simpleGui.FolderBrowse("Select destination", key="folder_select_button")

compress_button = simpleGui.Button("Compress", key="compress_button")
compress_successful = simpleGui.Text(key="compress_success")

window = simpleGui.Window("File compressor", layout=[[file_select_label, file_select_input_box, select_button],
                                                     [destination_label, destination_input_box, folder_select_button],
                                                     [compress_button, compress_successful]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["file_select_button"].split(";")
    folder_path = values["folder_select_button"][0]
    archiver.create_archive(filepaths, folder_path)
    window["compress_success"].update("Compression successful")

    match event:
        case simpleGui.WIN_CLOSED:
            break

window.close()
