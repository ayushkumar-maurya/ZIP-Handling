from utils.common_feature_items import *


def main(parent):
	get_label(parent, "Files to Add", False).grid(row=0, column=0, sticky="ew")
	new_files_entry_frame, new_files_entry = get_entry_frame(parent).values()
	new_files_entry_frame.grid(row=1, column=0, pady=attr_row_margin, sticky="ew")
	new_files_browse_btn = get_btn(parent, "Browse")
	new_files_browse_btn.grid(row=1, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Existing Zip", False).grid(row=2, column=0, sticky="ew")
	existing_zip_entry_frame, existing_zip_entry = get_entry_frame(parent).values()
	existing_zip_entry_frame.grid(row=3, column=0, pady=attr_row_margin, sticky="ew")
	existing_zip_browse_btn = get_btn(parent, "Browse")
	existing_zip_browse_btn.grid(row=3, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Destination Folder within Zip").grid(row=4, column=0, sticky="ew")
	dest_path_entry_frame, dest_path_entry = get_entry_frame(parent).values()
	dest_path_entry_frame.grid(row=5, column=0, pady=attr_row_margin, sticky="ew")
	dest_path_browse_btn = get_btn(parent, "Browse")
	dest_path_browse_btn.grid(row=5, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Password").grid(row=6, column=0, sticky="ew")
	pass_entry_frame, pass_entry = get_entry_frame(parent, True).values()
	pass_entry_frame.grid(row=7, column=0, pady=attr_row_margin, sticky="ew")

	add_btn = get_submit_btn(parent, "Add")
	add_btn.grid(row=8, column=0, pady=15, sticky="w")

	parent.grid_columnconfigure(0, weight=1)
