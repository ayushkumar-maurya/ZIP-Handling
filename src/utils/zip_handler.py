import os
import shutil
import pyzipper


class ZipHandler:
	def __init__(self):
		self.__path = os.path.join(os.getcwd(), "zip_operations_temp")
		self.__extracted_files_path = None
		self.clear()
		os.mkdir(self.__path)

	def extract_all_files(self, zip_path, password=""):
		self.__extracted_files_path = os.path.join(self.__path, "extracted_files")
		os.mkdir(self.__extracted_files_path)
		try:
			with pyzipper.AESZipFile(zip_path) as zf:
				if password != "":
					zf.setpassword(password.encode('utf-8'))
				zf.extractall(path=self.__extracted_files_path)
			return True
		except RuntimeError:
			return False

	def clear(self):
		if os.path.exists(self.__path):
			shutil.rmtree(self.__path)
