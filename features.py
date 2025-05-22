from tkinter import *
from utils import colours


def create_feature_frame(parent):
	feature_frame = Frame(parent, bg=colours.bg2)
	feature_frame.place(x=200, y=0, relwidth=1, relheight=1)
	return feature_frame


# Add new File to the existing zip.
def add_feature(parent):
	feature_frame = create_feature_frame(parent)
	Label(feature_frame, text="Add Frame").pack()
	return feature_frame


# Merge two zips together.
def merge_feature(parent):
	feature_frame = create_feature_frame(parent)
	Label(feature_frame, text="Merge Frame").pack()
	return feature_frame
