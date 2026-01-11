import binascii
import base64

try:
	with open('ESPICOHSMCA00001.cvcert', 'rb') as cafileh:
		content = cafileh.read()
		print("SCS3:")
		print("===================================")
		print(binascii.hexlify(content).upper())
		print("===================================")
except FileNotFoundError:
	print("File not found.")
except Exception as e:
	print(f"An error occurred: {e}")

try:
	with open('ESPICOHSMCA00001.cvcert', 'rb') as cafile:
		content = cafile.read()
		print("cacert:")
		print("===================================")
		print(base64.urlsafe_b64encode(content))
		print("===================================")
except FileNotFoundError:
	print("File not found.")
except Exception as e:
	print(f"An error occurred: {e}")


try:
	with open('ESPICOHSMDV00001.cvcert', 'rb') as dvfile:
		content = dvfile.read()
		print("dvcert:")
		print("===================================")
		print(base64.urlsafe_b64encode(content))
		print("===================================")
except FileNotFoundError:
	print("File not found.")
except Exception as e:
	print(f"An error occurred: {e}")

try:
	with open('ESPICOHSMTR00002.cvcert', 'rb') as cvfile:
		content = cvfile.read()
		print("cvcert:")
		print("===================================")
		print(base64.urlsafe_b64encode(content))
		print("===================================")
except FileNotFoundError:
	print("File not found.")
except Exception as e:
	print(f"An error occurred: {e}")
