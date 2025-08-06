import FreeSimpleGUI as simpleGui


file_select_label = simpleGui.Text("Select files to compress")
file_select_input_box =  simpleGui.Input()
select_button = simpleGui.FileBrowse("Select file")

destination_label = simpleGui.Text("Select files to compress")
destination_input_box =  simpleGui.Input()
folder_select_button = simpleGui.FolderBrowse("Select destination")

compress_button = simpleGui.Button("Compress")
window = simpleGui.Window("File compressor", layout=[[file_select_label, file_select_input_box, select_button],
                                                     [destination_label, destination_input_box, folder_select_button],
                                                     [compress_button]])

window.read()
window.close()
