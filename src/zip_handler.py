import os
import shutil
import pyzipper
from config import APP_PATH


class ZipHandler:
	def __init__(self):
		self.__path = os.path.join(APP_PATH, "temp_zip_operations")
		self.clear()
		os.mkdir(self.__path)

	@staticmethod
	def __generate_response(status=True, msg_title=None, msg_desc=None):
		return {'status': status, 'msg_title': msg_title, 'msg_desc': msg_desc}

	@staticmethod
	def __copy_files(src_files, dest_dir):
		for file in src_files:
			shutil.copy(file, dest_dir)

	@staticmethod
	def __remove_file(file_path):
		if os.path.exists(file_path):
			os.remove(file_path)

	def create_zip(self, src_dir, dest_zip, pwd=""):
		self.__remove_file(dest_zip)
		with pyzipper.AESZipFile(dest_zip, 'w') as zf:
			if pwd != "":
				zf.setpassword(pwd.encode())
				zf.setencryption(pyzipper.WZ_AES, nbits=256)
			for (root, dirs, files) in os.walk(src_dir, topdown=True):
				for dir in dirs:
					dir_path = os.path.join(root, dir)
					arcname = os.path.relpath(dir_path, start=src_dir).replace(os.sep, "/").rstrip("/") + "/"
					zf.writestr(arcname, b"")
				for file in files:
					file_path = os.path.join(root, file)
					arcname = os.path.relpath(file_path, start=src_dir)
					zf.write(file_path, arcname=arcname)

	def extract_zip_files(self, src_zip, dest_dir, pwd=""):
		if os.path.exists(dest_dir):
			shutil.rmtree(dest_dir)
		try:
			with pyzipper.AESZipFile(src_zip) as zf:
				if pwd != "":
					zf.setpassword(pwd.encode('utf-8'))
				zf.extractall(path=dest_dir)
		except RuntimeError:
			return self.__generate_response(
				status=False,
				msg_title="Password required",
				msg_desc="ZIP is password protected. Please enter correct password."
			)
		return self.__generate_response(
			status=True,
			msg_title="Files extraction completed",
			msg_desc="Files are extracted successfully at {}".format(os.path.basename(dest_dir))
		)

	def add_files_to_existing_zip(self, src_files, src_zip, zip_target_dir, pwd, dest_zip):
		extracted_files_path = os.path.join(self.__path, "extracted_files")
		# Extracting zip files.
		res = self.extract_zip_files(src_zip, extracted_files_path, pwd)
		if res['status']:
			zip_target_dir_path = os.path.join(extracted_files_path, zip_target_dir)
			if os.path.isdir(zip_target_dir_path):
				# Copying source files to target folder present under extracted zip directory.
				self.__copy_files(src_files, zip_target_dir_path)
				# Creating zip based on files present under extracted zip directory.
				self.create_zip(extracted_files_path, dest_zip, pwd)
				res = self.__generate_response(
					status=True,
					msg_title="Files added successfully",
					msg_desc="Files added successfully. ZIP Name: {}".format(os.path.basename(dest_zip))
				)
			else:
				res = self.__generate_response(
					status=False,
					msg_title="Invalid target folder within zip",
					msg_desc="{} is not present under existing zip.".format(zip_target_dir)
				)

		self.clear()
		return res

	def merge_zips(self, src_zip, target_zip, src_pwd, target_pwd, dest_zip):
		extracted_src_files_path = os.path.join(self.__path, "extracted_src_files")
		extracted_target_files_path = os.path.join(self.__path, "extracted_target_files")
		# Extracting source zip files.
		res = self.extract_zip_files(src_zip, extracted_src_files_path, src_pwd)
		if res['status']:
			# Extracting target zip files.
			res = self.extract_zip_files(target_zip, extracted_target_files_path, target_pwd)
			if res['status']:
				# Copying source folder to target folder.
				shutil.copytree(extracted_src_files_path, extracted_target_files_path, dirs_exist_ok=True)
				# Creating zip based on files present under extracted target zip directory.
				self.create_zip(extracted_target_files_path, dest_zip, target_pwd)
				res = self.__generate_response(
					status=True,
					msg_title="ZIP merged successfully",
					msg_desc="ZIP merged successfully. ZIP Name: {}".format(os.path.basename(dest_zip))
				)

		self.clear()
		return res

	def move_file_within_zip(self, src_zip, src_file, dest_dir, pwd, dest_zip):
		extracted_files_path = os.path.join(self.__path, "extracted_files")
		# Extracting zip files.
		res = self.extract_zip_files(src_zip, extracted_files_path, pwd)
		if res['status']:
			src_file_path = os.path.join(extracted_files_path, src_file)
			if os.path.isfile(src_file_path):
				dest_dir_path = os.path.join(extracted_files_path, dest_dir)
				if os.path.isdir(dest_dir_path):
					# Moving file to target folder present under extracted zip directory.
					self.__remove_file(os.path.join(dest_dir_path, os.path.basename(src_file)))
					shutil.move(src_file_path, dest_dir_path)
					# Creating zip based on files present under extracted zip directory.
					self.create_zip(extracted_files_path, dest_zip, pwd)
					res = self.__generate_response(
						status=True,
						msg_title="File moved successfully",
						msg_desc="File moved successfully. ZIP Name: {}".format(os.path.basename(dest_zip))
					)
				else:
					res = self.__generate_response(
						status=False,
						msg_title="Invalid target folder within zip",
						msg_desc="{} is not present under existing zip.".format(dest_dir)
					)
			else:
				res = self.__generate_response(
					status=False,
					msg_title="Invalid file to move",
					msg_desc="{} is not present under existing zip.".format(src_file)
				)

		self.clear()
		return res

	def clear(self):
		if os.path.exists(self.__path):
			shutil.rmtree(self.__path)
