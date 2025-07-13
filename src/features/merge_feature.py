import os
from tkinter import filedialog
from tkinter import messagebox
from utils.common_feature_items import *
from utils.zip_handler import ZipHandler


def zip_input(zip_entry):
	selected_zip = filedialog.askopenfilename(
		title="Select existing zip",
		filetypes=[("ZIP File", "*.zip")]
	)
	zip_entry.delete(0, END)
	zip_entry.insert(0, selected_zip)


def save_loc_input(save_loc_entry):
	save_loc = filedialog.askdirectory()
	save_loc_entry.delete(0, END)
	save_loc_entry.insert(0, save_loc)


def validate_and_get_inputs(entries):
	res = {'inputs': None, 'error': None}

	src_zip = entries['src_zip'].get()
	target_zip = entries['target_zip'].get()
	src_pwd = entries['src_pwd'].get()
	target_pwd = entries['target_pwd'].get()
	save_loc = entries['save_loc'].get()

	src_zip = src_zip.strip()
	_, src_zip_ext = os.path.splitext(src_zip)
	if not os.path.isfile(src_zip) or src_zip_ext != ".zip":
		res['error'] = "Please select valid source zip."
		return res

	target_zip = target_zip.strip()
	target_zip_name, target_zip_ext = os.path.splitext(target_zip)
	if not os.path.isfile(target_zip) or target_zip_ext != ".zip":
		res['error'] = "Please select valid target zip."
		return res

	save_loc = save_loc.strip()
	if not os.path.isdir(save_loc):
		res['error'] = "Please mention valid location to save modified zip."
		return res
	dest_zip = os.path.join(save_loc, "{} Modified.zip".format(os.path.basename(target_zip_name)))

	res['inputs'] = {
		'src_zip': src_zip,
		'target_zip': target_zip,
		'src_pwd': src_pwd,
		'target_pwd': target_pwd,
		'dest_zip': dest_zip
	}

	return res


def perform_merge_operation(entries, show_progress_bar):
	show_progress_bar()
	inputs, error = validate_and_get_inputs(entries).values()
	if error:
		messagebox.showerror("Invalid Input", error)
	else:
		zip_handler = ZipHandler()
		res = zip_handler.merge_zips(**inputs)
		if res['status']:
			messagebox.showinfo(res['msg_title'], res['msg_desc'])
		else:
			messagebox.showerror(res['msg_title'], res['msg_desc'])
	show_progress_bar(False)


def main(parent, show_progress_bar):
	entries = {}

	# Creating required Widgets.
	get_label(parent, "Select source zip", False).grid(row=0, column=0, sticky="ew")
	src_zip_entry_frame, entries['src_zip'] = get_entry_frame(parent).values()
	src_zip_entry_frame.grid(row=1, column=0, pady=attr_row_margin, sticky="ew")
	src_zip_browse_btn = get_btn(parent, "Browse")
	src_zip_browse_btn.grid(row=1, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Select target zip", False).grid(row=2, column=0, sticky="ew")
	target_zip_entry_frame, entries['target_zip'] = get_entry_frame(parent).values()
	target_zip_entry_frame.grid(row=3, column=0, pady=attr_row_margin, sticky="ew")
	target_zip_browse_btn = get_btn(parent, "Browse")
	target_zip_browse_btn.grid(row=3, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Source zip's password").grid(row=4, column=0, sticky="ew")
	src_pwd_entry_frame, entries['src_pwd'] = get_entry_frame(parent, True).values()
	src_pwd_entry_frame.grid(row=5, column=0, pady=attr_row_margin, sticky="ew")

	get_label(parent, "Target zip's password").grid(row=6, column=0, sticky="ew")
	target_pwd_entry_frame, entries['target_pwd'] = get_entry_frame(parent, True).values()
	target_pwd_entry_frame.grid(row=7, column=0, pady=attr_row_margin, sticky="ew")

	get_label(parent, "Save modified target zip at", False).grid(row=8, column=0, sticky="ew")
	save_loc_entry_frame, entries['save_loc'] = get_entry_frame(parent).values()
	save_loc_entry_frame.grid(row=9, column=0, pady=attr_row_margin, sticky="ew")
	save_loc_browse_btn = get_btn(parent, "Browse")
	save_loc_browse_btn.grid(row=9, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	merge_btn = get_submit_btn(parent, "Merge")
	merge_btn.grid(row=10, column=0, pady=15, sticky="w")

	parent.grid_columnconfigure(0, weight=1)

	# Configuring buttons command
	src_zip_browse_btn.config(command=lambda: zip_input(entries['src_zip']))
	target_zip_browse_btn.config(command=lambda: zip_input(entries['target_zip']))
	save_loc_browse_btn.config(command=lambda: save_loc_input(entries['save_loc']))
	merge_btn.config(command=lambda: perform_merge_operation(entries, show_progress_bar))
