def make_ast(data1, data2):
    ast = []
    keys1 = data1.keys()
    keys2 = data2.keys()
    all_keys = sorted(keys1 | keys2)

    for key in all_keys:
        data1_value = data1.get(key)
        data2_value = data2.get(key)

        if key not in data1:
            ast.append({
                'key': key,
                'value': data2_value,
                'type_': 'added'
            })
        elif key not in data2:
            ast.append({
                'key': key,
                'value': data1_value,
                'type_': 'removed'
            })

        elif isinstance(data1_value, dict) and isinstance(data2_value, dict):
            ast.append({
                'key': key,
                'children': make_ast(data1_value, data2_value),
                'type_': 'nested'
            })

        elif data1_value != data2_value:
            ast.append({
                'key': key,
                'before': data1_value,
                'after': data2_value,
                'type_': 'updated'
            })
        else:
            ast.append({
                'key': key,
                'value': data1_value,
                'type_': 'same'
            })
    return ast
