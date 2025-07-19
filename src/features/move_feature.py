import os
from tkinter import filedialog
from tkinter import messagebox
from utils.common_feature_items import *
from zip_handler import ZipHandler


def src_zip_input(src_zip_entry):
	selected_zip = filedialog.askopenfilename(
		title="Select zip",
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
	src_file = entries['src_file'].get()
	dest_dir = entries['dest_dir'].get()
	pwd = entries['pwd'].get()
	save_loc = entries['save_loc'].get()

	src_zip = src_zip.strip()
	src_zip_name, src_zip_ext = os.path.splitext(src_zip)
	if not os.path.isfile(src_zip) or src_zip_ext != ".zip":
		res['error'] = "Please select valid zip."
		return res

	src_file = src_file.strip()
	dest_dir = dest_dir.strip()

	save_loc = save_loc.strip()
	if not os.path.isdir(save_loc):
		res['error'] = "Please mention valid location to save modified zip."
		return res
	dest_zip = os.path.join(save_loc, "{} Modified.zip".format(os.path.basename(src_zip_name)))

	res['inputs'] = {
		'src_zip': src_zip,
		'src_file': src_file,
		'dest_dir': dest_dir,
		'pwd': pwd,
		'dest_zip': dest_zip
	}

	return res


def perform_move_operation(entries, show_progress_bar):
	show_progress_bar()
	inputs, error = validate_and_get_inputs(entries).values()
	if error:
		messagebox.showerror("Invalid Input", error)
	else:
		zip_handler = ZipHandler()
		res = zip_handler.move_file_within_zip(**inputs)
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

	get_label(parent, "File to move (Relative path)", False).grid(row=2, column=0, sticky="ew")
	src_file_entry_frame, entries['src_file'] = get_entry_frame(parent).values()
	src_file_entry_frame.grid(row=3, column=0, pady=attr_row_margin, sticky="ew")

	get_label(parent, "Target folder within zip").grid(row=4, column=0, sticky="ew")
	dest_dir_entry_frame, entries['dest_dir'] = get_entry_frame(parent).values()
	dest_dir_entry_frame.grid(row=5, column=0, pady=attr_row_margin, sticky="ew")

	get_label(parent, "Password").grid(row=6, column=0, sticky="ew")
	pwd_entry_frame, entries['pwd'] = get_entry_frame(parent, True).values()
	pwd_entry_frame.grid(row=7, column=0, pady=attr_row_margin, sticky="ew")

	get_label(parent, "Save modified zip at", False).grid(row=8, column=0, sticky="ew")
	save_loc_entry_frame, entries['save_loc'] = get_entry_frame(parent).values()
	save_loc_entry_frame.grid(row=9, column=0, pady=attr_row_margin, sticky="ew")
	save_loc_browse_btn = get_btn(parent, "Browse")
	save_loc_browse_btn.grid(row=9, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	move_btn = get_submit_btn(parent, "Move")
	move_btn.grid(row=10, column=0, pady=15, sticky="w")

	parent.grid_columnconfigure(0, weight=1)

	# Configuring buttons command
	src_zip_browse_btn.config(command=lambda: src_zip_input(entries['src_zip']))
	save_loc_browse_btn.config(command=lambda: save_loc_input(entries['save_loc']))
	move_btn.config(command=lambda: perform_move_operation(entries, show_progress_bar))
