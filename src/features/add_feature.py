from tkinter import filedialog
from tkinter import messagebox
from utils.common_feature_items import *
from utils.zip_handler import ZipHandler


def new_files_input(new_files_entry):
	new_files = filedialog.askopenfilenames(
		title="Select files to add",
		filetypes=[("All Files", "*.*")]
	)
	new_files_path_str = ""
	for i in range(len(new_files)):
		if i > 0:
			new_files_path_str += "; "
		new_files_path_str += new_files[i]
	new_files_entry.delete(0, END)
	new_files_entry.insert(0, new_files_path_str)


def existing_zip_input(existing_zip_entry, zip_target_entry):
	existing_zip = filedialog.askopenfilename(
		title="Select existing zip",
		filetypes=[("Zip File", "*.zip"), ("Rar File", "*.rar"), ("7z File", "*.7z")]
	)
	existing_zip_entry.delete(0, END)
	existing_zip_entry.insert(0, existing_zip)
	zip_target_entry.delete(0, END)
	zip_target_entry.insert(0, existing_zip)


def save_loc_input(save_loc_entry):
	save_loc = filedialog.askdirectory()
	save_loc_entry.delete(0, END)
	save_loc_entry.insert(0, save_loc)


def perform_add_operation(entries, show_progress_bar):
	new_files = entries['new_files'].get().strip()
	existing_zip = entries['existing_zip'].get().strip()
	zip_target = entries['zip_target'].get().strip()
	save_loc = entries['save_loc'].get().strip()
	pwd = entries['pwd'].get()

	if new_files == "":
		messagebox.showerror("Required field missing", "Please select files to add.")
	elif existing_zip == "":
		messagebox.showerror("Required field missing", "Please select existing zip.")
	elif save_loc == "":
		messagebox.showerror("Required field missing", "Please mention location to save modified zip.")
	else:
		zip_handler = ZipHandler()
		res = zip_handler.add_files_to_existing_zip(existing_zip, pwd)
		if res['status']:
			messagebox.showinfo(res['msg_title'], res['msg_desc'])
		else:
			messagebox.showerror(res['msg_title'], res['msg_desc'])


def main(parent, show_progress_bar):
	entries = {}

	# Creating required Widgets.
	get_label(parent, "Select files to add", False).grid(row=0, column=0, sticky="ew")
	new_files_entry_frame, entries['new_files'] = get_entry_frame(parent).values()
	new_files_entry_frame.grid(row=1, column=0, pady=attr_row_margin, sticky="ew")
	new_files_browse_btn = get_btn(parent, "Browse")
	new_files_browse_btn.grid(row=1, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Select existing zip", False).grid(row=2, column=0, sticky="ew")
	existing_zip_entry_frame, entries['existing_zip'] = get_entry_frame(parent).values()
	existing_zip_entry_frame.grid(row=3, column=0, pady=attr_row_margin, sticky="ew")
	existing_zip_browse_btn = get_btn(parent, "Browse")
	existing_zip_browse_btn.grid(row=3, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Target folder within zip").grid(row=4, column=0, sticky="ew")
	zip_target_entry_frame, entries['zip_target'] = get_entry_frame(parent).values()
	zip_target_entry_frame.grid(row=5, column=0, pady=attr_row_margin, sticky="ew")

	get_label(parent, "Password").grid(row=6, column=0, sticky="ew")
	pwd_entry_frame, entries['pwd'] = get_entry_frame(parent, True).values()
	pwd_entry_frame.grid(row=7, column=0, pady=attr_row_margin, sticky="ew")

	get_label(parent, "Save modified zip at", False).grid(row=8, column=0, sticky="ew")
	save_loc_entry_frame, entries['save_loc'] = get_entry_frame(parent).values()
	save_loc_entry_frame.grid(row=9, column=0, pady=attr_row_margin, sticky="ew")
	save_loc_browse_btn = get_btn(parent, "Browse")
	save_loc_browse_btn.grid(row=9, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	add_btn = get_submit_btn(parent, "Add")
	add_btn.grid(row=10, column=0, pady=15, sticky="w")

	parent.grid_columnconfigure(0, weight=1)

	# Configuring buttons command
	new_files_browse_btn.config(command=lambda: new_files_input(entries['new_files']))
	existing_zip_browse_btn.config(command=lambda: existing_zip_input(entries['existing_zip'], entries['zip_target']))
	save_loc_browse_btn.config(command=lambda: save_loc_input(entries['save_loc']))
	add_btn.config(command=lambda: perform_add_operation(entries, show_progress_bar))
