from tkinter import filedialog
from tkinter import messagebox
from utils.common_feature_items import *
from utils.zip_handler import ZipHandler


def new_files_input(new_files_entry):
	new_files_path = filedialog.askopenfilenames(
		title="Select Files to Add",
		filetypes=[("All Files", "*.*")]
	)
	new_files_path_str = ""
	for i in range(len(new_files_path)):
		if i > 0:
			new_files_path_str += "; "
		new_files_path_str += new_files_path[i]
	new_files_entry.delete(0, END)
	new_files_entry.insert(0, new_files_path_str)


def existing_zip_input(existing_zip_entry, dest_path_entry):
	existing_zip_path = filedialog.askopenfilename(
		title="Select Existing Zip",
		filetypes=[("Zip File", "*.zip"), ("Rar File", "*.rar"), ("7z File", "*.7z")]
	)
	existing_zip_entry.delete(0, END)
	existing_zip_entry.insert(0, existing_zip_path)
	dest_path_entry.delete(0, END)
	dest_path_entry.insert(0, existing_zip_path)


def perform_add_operation(entries, show_progress_bar):
	new_files_path = entries['new_files'].get().strip()
	existing_zip_path = entries['existing_zip'].get().strip()
	dest_path = entries['dest_path'].get().strip()
	password = entries['pass'].get()

	if new_files_path == "":
		messagebox.showerror("Required field missing", "Please select files to add.")
	elif existing_zip_path == "":
		messagebox.showerror("Required field missing", "Please select existing zip.")
	else:
		zip_handler = ZipHandler()
		if not zip_handler.extract_all_files(existing_zip_path, password):
			messagebox.showerror("Password required", "Zip is password protected. Please enter correct password.")


def main(parent, show_progress_bar):
	entries = {}

	# Creating required Widgets.
	get_label(parent, "Files to Add", False).grid(row=0, column=0, sticky="ew")
	new_files_entry_frame, entries['new_files'] = get_entry_frame(parent).values()
	new_files_entry_frame.grid(row=1, column=0, pady=attr_row_margin, sticky="ew")
	new_files_browse_btn = get_btn(parent, "Browse")
	new_files_browse_btn.grid(row=1, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Existing Zip", False).grid(row=2, column=0, sticky="ew")
	existing_zip_entry_frame, entries['existing_zip'] = get_entry_frame(parent).values()
	existing_zip_entry_frame.grid(row=3, column=0, pady=attr_row_margin, sticky="ew")
	existing_zip_browse_btn = get_btn(parent, "Browse")
	existing_zip_browse_btn.grid(row=3, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Destination Folder within Zip").grid(row=4, column=0, sticky="ew")
	dest_path_entry_frame, entries['dest_path'] = get_entry_frame(parent).values()
	dest_path_entry_frame.grid(row=5, column=0, pady=attr_row_margin, sticky="ew")

	get_label(parent, "Password").grid(row=6, column=0, sticky="ew")
	pass_entry_frame, entries['pass'] = get_entry_frame(parent, True).values()
	pass_entry_frame.grid(row=7, column=0, pady=attr_row_margin, sticky="ew")

	add_btn = get_submit_btn(parent, "Add")
	add_btn.grid(row=8, column=0, pady=15, sticky="w")

	parent.grid_columnconfigure(0, weight=1)

	# Configuring buttons command
	new_files_browse_btn.config(command=lambda: new_files_input(entries['new_files']))
	existing_zip_browse_btn.config(command=lambda: existing_zip_input(entries['existing_zip'], entries['dest_path']))
	add_btn.config(command=lambda: perform_add_operation(entries, show_progress_bar))
