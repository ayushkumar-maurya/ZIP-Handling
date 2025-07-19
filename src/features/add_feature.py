import os
from tkinter import filedialog
from tkinter import messagebox
from utils.common_feature_items import *
from zip_handler import ZipHandler


def new_files_input(new_files_entry):
	new_files = filedialog.askopenfilenames(
		title="Select files to add",
		filetypes=[("All Files", "*.*")]
	)
	new_files_path_str = ""
	for i in range(len(new_files)):
		if i > 0:
			new_files_path_str += " | "
		new_files_path_str += new_files[i]
	new_files_entry.delete(0, END)
	new_files_entry.insert(0, new_files_path_str)


def existing_zip_input(existing_zip_entry):
	existing_zip = filedialog.askopenfilename(
		title="Select existing zip",
		filetypes=[("ZIP File", "*.zip")]
	)
	existing_zip_entry.delete(0, END)
	existing_zip_entry.insert(0, existing_zip)


def save_loc_input(save_loc_entry):
	save_loc = filedialog.askdirectory()
	save_loc_entry.delete(0, END)
	save_loc_entry.insert(0, save_loc)


def validate_and_get_inputs(entries):
	res = {'inputs': None, 'error': None}

	new_files = entries['new_files'].get()
	existing_zip = entries['existing_zip'].get()
	zip_target = entries['zip_target'].get()
	pwd = entries['pwd'].get()
	save_loc = entries['save_loc'].get()

	new_files_list = new_files.split("|")
	for i in range(len(new_files_list)):
		new_files_list[i] = new_files_list[i].strip()
		if not os.path.isfile(new_files_list[i]):
			res['error'] = "Please select valid files to add."
			return res

	existing_zip = existing_zip.strip()
	existing_zip_name, existing_zip_ext = os.path.splitext(existing_zip)
	if not os.path.isfile(existing_zip) or existing_zip_ext != ".zip":
		res['error'] = "Please select valid zip."
		return res

	zip_target = zip_target.strip()

	save_loc = save_loc.strip()
	if not os.path.isdir(save_loc):
		res['error'] = "Please mention valid location to save modified zip."
		return res
	dest_zip = os.path.join(save_loc, "{} Modified.zip".format(os.path.basename(existing_zip_name)))

	res['inputs'] = {
		'src_files': new_files_list,
		'src_zip': existing_zip,
		'zip_target_dir': zip_target,
		'pwd': pwd,
		'dest_zip': dest_zip
	}

	return res


def perform_add_operation(entries, show_progress_bar):
	show_progress_bar()
	inputs, error = validate_and_get_inputs(entries).values()
	if error:
		messagebox.showerror("Invalid Input", error)
	else:
		zip_handler = ZipHandler()
		res = zip_handler.add_files_to_existing_zip(**inputs)
		if res['status']:
			messagebox.showinfo(res['msg_title'], res['msg_desc'])
		else:
			messagebox.showerror(res['msg_title'], res['msg_desc'])
	show_progress_bar(False)


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
	existing_zip_browse_btn.config(command=lambda: existing_zip_input(entries['existing_zip']))
	save_loc_browse_btn.config(command=lambda: save_loc_input(entries['save_loc']))
	add_btn.config(command=lambda: perform_add_operation(entries, show_progress_bar))
