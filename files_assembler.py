from io import FileIO
from os import system
from base64 import b64encode, b64decode

exe_assembler_text = """
███████╗██╗██╗     ███████╗███████╗     █████╗ ███████╗███████╗███████╗███╗   ███╗██████╗ ██╗     ███████╗██████╗ 
██╔════╝██║██║     ██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗
█████╗  ██║██║     █████╗  ███████╗    ███████║███████╗███████╗█████╗  ██╔████╔██║██████╔╝██║     █████╗  ██████╔╝
██╔══╝  ██║██║     ██╔══╝  ╚════██║    ██╔══██║╚════██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══██╗██║     ██╔══╝  ██╔══██╗
██║     ██║███████╗███████╗███████║    ██║  ██║███████║███████║███████╗██║ ╚═╝ ██║██████╔╝███████╗███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
"""

def exe2binary(files_list:list):
	binary_list = []

	for file in files_list:

		with open(file, "rb") as f:
			exe_binary = b64encode(f.read())
			binary_list.append(exe_binary)

	print("\nSuccessfully get binary of files!")
	return binary_list

def exe_assembler(file_directory:str, files_name:list, binary_list:list):
	file_text = fr"""from ctypes import windll
from base64 import b64decode
from subprocess import Popen
from sys import argv, executable

def make_admin():
	if not windll.shell32.IsUserAnAdmin():
		input("You aren't admin!")
		
		windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv), None, 1)
		return exit()

def exe_assembled():
	binary_list = {binary_list}
	files_name = {files_name}

	i = 0
	for file in binary_list:
		file_decode = b64decode(file)
		file_directory = r"C:\Windows\Temp\ " + files_name[i].split("\\")[-1]

		with open(file_directory, "wb") as f:
			f.write(file_decode)

		Popen(file_directory)
		i += 1

if __name__ == "__main__":
	make_admin()
	exe_assembled()
	exit()"""

	with open(file_directory + ".pyw" , "w") as f:
		f.write(file_text)

	return "Successfully assembled files!"

def main():
	system("color d")

	while True:
		system("cls")
		files_list = []

		while True:
			system("cls")

			print(exe_assembler_text)
			print("files list = " + str(files_list))
			print("Enter file directory or 'stop'")

			file = input("\n>>> ")
			if file.lower() in ["stop", "s", "false"]:

				if len(files_list) <= 1:
					input("No good files specified!")
					main()

				else:
					break

			try:
				FileIO(file)

			except FileNotFoundError as e:
				input(e)
				continue

			else:
				files_list.append(file)

		file_directory = input("What file name / file directory do you want? >>> ")
		binary_list = exe2binary(files_list=files_list)

		print(exe_assembler(file_directory=file_directory, files_name=files_list, binary_list=binary_list))

		restart = input("\ndo you want restart? [y/n] >>> ").lower()

		if restart not in ["true", "yes", "y", "ok"]:
			exit("Ok, bye :D")

if __name__ == "__main__":
	main()