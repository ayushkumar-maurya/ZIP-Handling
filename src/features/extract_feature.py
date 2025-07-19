import os
from tkinter import filedialog
from tkinter import messagebox
from utils.common_feature_items import *
from zip_handler import ZipHandler


def src_zip_input(src_zip_entry):
	selected_zip = filedialog.askopenfilename(
		title="Select existing zip",
		filetypes=[("ZIP File", "*.zip")]
	)
	src_zip_entry.delete(0, END)
	src_zip_entry.insert(0, selected_zip)


def save_loc_input(save_loc_entry):
	save_loc = filedialog.askdirectory()
	save_loc_entry.delete(0, END)
	save_loc_entry.insert(0, save_loc)


def validate_and_get_inputs(entries):
	res = {'inputs': None, 'error': None}

	src_zip = entries['src_zip'].get()
	pwd = entries['pwd'].get()
	save_loc = entries['save_loc'].get()

	src_zip = src_zip.strip()
	src_zip_name, src_zip_ext = os.path.splitext(src_zip)
	if not os.path.isfile(src_zip) or src_zip_ext != ".zip":
		res['error'] = "Please select valid source zip."
		return res

	save_loc = save_loc.strip()
	if not os.path.isdir(save_loc):
		res['error'] = "Please mention valid location to save extracted files."
		return res
	dest_dir = os.path.join(save_loc, os.path.basename(src_zip_name))

	res['inputs'] = {
		'src_zip': src_zip,
		'pwd': pwd,
		'dest_dir': dest_dir
	}

	return res


def perform_extract_operation(entries, show_progress_bar):
	show_progress_bar()
	inputs, error = validate_and_get_inputs(entries).values()
	if error:
		messagebox.showerror("Invalid Input", error)
	else:
		zip_handler = ZipHandler()
		res = zip_handler.extract_zip_files(**inputs)
		if res['status']:
			messagebox.showinfo(res['msg_title'], res['msg_desc'])
		else:
			messagebox.showerror(res['msg_title'], res['msg_desc'])
	show_progress_bar(False)


def main(parent, show_progress_bar):
	entries = {}

	# Creating required Widgets.
	get_label(parent, "Select zip", False).grid(row=0, column=0, sticky="ew")
	src_zip_entry_frame, entries['src_zip'] = get_entry_frame(parent).values()
	src_zip_entry_frame.grid(row=1, column=0, pady=attr_row_margin, sticky="ew")
	src_zip_browse_btn = get_btn(parent, "Browse")
	src_zip_browse_btn.grid(row=1, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Password").grid(row=2, column=0, sticky="ew")
	pwd_entry_frame, entries['pwd'] = get_entry_frame(parent, True).values()
	pwd_entry_frame.grid(row=3, column=0, pady=attr_row_margin, sticky="ew")

	get_label(parent, "Save extracted files at", False).grid(row=4, column=0, sticky="ew")
	save_loc_entry_frame, entries['save_loc'] = get_entry_frame(parent).values()
	save_loc_entry_frame.grid(row=5, column=0, pady=attr_row_margin, sticky="ew")
	save_loc_browse_btn = get_btn(parent, "Browse")
	save_loc_browse_btn.grid(row=5, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	extract_btn = get_submit_btn(parent, "Extract")
	extract_btn.grid(row=6, column=0, pady=15, sticky="w")

	parent.grid_columnconfigure(0, weight=1)

	# Configuring buttons command
	src_zip_browse_btn.config(command=lambda: src_zip_input(entries['src_zip']))
	save_loc_browse_btn.config(command=lambda: save_loc_input(entries['save_loc']))
	extract_btn.config(command=lambda: perform_extract_operation(entries, show_progress_bar))
