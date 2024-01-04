import argparse
import json
import os

parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()

first_file_path = f"{os.getcwd()}/{args.first_file}"
second_file_path = f"{os.getcwd()}/{args.second_file}"


def convert_to_str(tup):
	key, value = tup
	return str(key), str(value)


def generate_diff(file_path1, file_path2):
	result = ['{']
	data1 = json.load(open(file_path1))
	data2 = json.load(open(file_path2))
	keys1 = list(data1.keys())
	keys2 = list(data2.keys())
	all_keys = sorted(set(keys1 + keys2))

	for key in all_keys:
		if key in data1 and key in data2:
			if data1[key] != data2[key]:
				result.append(f"  - {key}: {str(data1[key])}")
				result.append(f"  + {key}: {str(data2[key])}")
			else:
				result.append(f"    {key}: {str(data1[key])}")

		elif key in data1 and key not in data2:
			result.append(f"  - {key}: {str(data1[key])}")
		else:
			result.append(f"  + {key}: {str(data2[key])}")

	result.append('}')
	# print('Result', result)
	output = ' '.join(result)
	# print('Output ', output)
	for entry in result:
		print(entry)


def main():
	generate_diff(first_file_path, second_file_path)


if __name__ == "main":
	main()
