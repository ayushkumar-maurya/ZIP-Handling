import os
import shutil
import pyzipper


class ZipHandler:
	def __init__(self):
		self.__path = os.path.join(os.getcwd(), "temp_zip_operations")
		self.clear()
		os.mkdir(self.__path)

	@staticmethod
	def __generate_response(status=True, msg_title=None, msg_desc=None):
		return {'status': status, 'msg_title': msg_title, 'msg_desc': msg_desc}

	@staticmethod
	def __copy_files(src_files, dest_dir):
		for file in src_files:
			shutil.copy(file, dest_dir)

	def extract_zip_files(self, src_zip, dest_dir, pwd=""):
		try:
			with pyzipper.AESZipFile(src_zip) as zf:
				if pwd != "":
					zf.setpassword(pwd.encode('utf-8'))
				zf.extractall(path=dest_dir)
		except RuntimeError:
			return self.__generate_response(
				status=False,
				msg_title="Password required",
				msg_desc="Zip is password protected. Please enter correct password."
			)
		return self.__generate_response(
			status=True,
			msg_title="Files extraction completed",
			msg_desc="Files are extracted successfully at {}".format(dest_dir)
		)

	def add_files_to_existing_zip(self, src_files, src_zip, zip_target_dir, pwd, dest_dir):
		extracted_files_path = os.path.join(self.__path, "extracted_files")
		# Extracting zip files.
		res = self.extract_zip_files(src_zip, extracted_files_path, pwd)

		if res['status']:
			zip_target_dir_path = os.path.join(extracted_files_path, zip_target_dir)
			if os.path.isdir(zip_target_dir_path):
				# Copying source files to target folder present under extracted zip directory.
				self.__copy_files(src_files, zip_target_dir_path)

			else:
				return self.__generate_response(
					status=False,
					msg_title="Invalid target folder within zip",
					msg_desc="{} is not present under existing zip.".format(zip_target_dir)
				)

		return res

	def clear(self):
		if os.path.exists(self.__path):
			shutil.rmtree(self.__path)
