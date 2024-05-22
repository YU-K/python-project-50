def stringify(node):
    if isinstance(node, bool):
        return str(node).lower()

    if isinstance(node, int):
        return node

    if isinstance(node, dict):
        return '[complex value]'

    if node is None:
        return 'null'

    return f"'{node}'"


def plain(ast):
    def walk(tree, ancestry):
        nodes = []
        for node in tree:
            key = node.get('key')
            type_ = node.get('type_')
            value = node.get('value')
            new_ancestry = f"{ancestry}{key}"

            match type_:
                case "updated":
                    nodes.append(f"Property '{new_ancestry}' was updated. "
                                 f"From {stringify(node['before'])} "
                                 f"to {stringify(node['after'])}")
                case "added":
                    nodes.append(f"Property '{new_ancestry}' "
                                 f"was added with value: {stringify(value)}")
                case "removed":
                    nodes.append(f"Property '{new_ancestry}' was removed")
                case "nested":
                    nodes.append(
                        f"{walk(node['children'], new_ancestry + '.')}")
                case "same":
                    nodes.append('')
                case _:
                    raise Exception(f"Unknown type {type_}!")

        new_nodes = list(filter(lambda x: x != '', nodes))
        return '\n'.join(new_nodes)

    return f"{walk(ast, '')}"
