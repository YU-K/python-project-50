def generate_diff(data1, data2):
    result = ['{']
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
    for el in result:
        print(el)
    output = ''.join(result)

    return output
