import binascii
import base64
import json

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
		cacert = base64.urlsafe_b64encode(content)
except FileNotFoundError:
	print("File not found.")
except Exception as e:
	print(f"An error occurred: {e}")


try:
	with open('ESPICOHSMDV00001.cvcert', 'rb') as dvfile:
		content = dvfile.read()
		dvcert = base64.urlsafe_b64encode(content)
except FileNotFoundError:
	print("File not found.")
except Exception as e:
	print(f"An error occurred: {e}")

try:
	with open('ESPICOHSMTR00002.cvcert', 'rb') as cvfile:
		content = cvfile.read()
		cvcert = base64.urlsafe_b64encode(content)
except FileNotFoundError:
	print("File not found.")
except Exception as e:
	print(f"An error occurred: {e}")

data = {}
data['cvcert'] = cvcert
data['dvcert'] = dvcert
data['cacert'] = cacert
json_data = json.dumps(data, separators=(',', ':'))
print("Json:")
print("===================================")
print(json_data)
print("===================================")
