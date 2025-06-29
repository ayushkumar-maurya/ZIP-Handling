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
			msg_title="Files Extraction completed",
			msg_desc="Files are extracted successfully at {}".format(dest_dir)
		)

	def add_files_to_existing_zip(self, src_zip, pwd=""):
		extracted_files_path = os.path.join(self.__path, "extracted_files")
		res = self.extract_zip_files(src_zip, extracted_files_path, pwd)
		return res

	def clear(self):
		if os.path.exists(self.__path):
			shutil.rmtree(self.__path)
