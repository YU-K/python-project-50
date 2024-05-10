def do_intend(depth):
    return "  " * depth


def stringify(node, depth):
    if isinstance(node, bool):
        return str(node).lower()

    if node is None:
        return 'null'

    if isinstance(node, dict):
        new_node = ['{']
        for key, value in node.items():
            if isinstance(value, dict):
                new_node.append(f"        {do_intend(depth)}{key}: "
                                f"{stringify(value, depth + 2)}")
            else:
                new_node.append(f"        {do_intend(depth)}{key}: "
                                f"{str(value)}")
        new_node.append(f"    {do_intend(depth)}}}")
        return '\n'.join(new_node)

    return str(node)


def stylish(diff):
    def walk(tree, depth):
        nodes = []
        for node in tree:
            key = node.get('key')
            type_ = node.get('type_')
            value = node.get('value')

            match type_:
                case "updated":
                    nodes.append(f"  {do_intend(depth)}- {key}: "
                                 f"{stringify(node['before'], depth)}")
                    nodes.append(f"  {do_intend(depth)}+ {key}: "
                                 f"{stringify(node['after'], depth)}")
                case "added":
                    nodes.append(f"  {do_intend(depth)}+ {key}: "
                                 f"{stringify(value, depth)}")
                case 'removed':
                    nodes.append(f"  {do_intend(depth)}- {key}: "
                                 f"{stringify(value, depth)}")
                case 'same':
                    nodes.append(f"  {do_intend(depth)}  {key}: "
                                 f"{stringify(value, depth)}")
                case "nested":
                    nodes.append(f"    {do_intend(depth)}{key}: {{")
                    nodes.append(f"{walk(node['children'], depth + 2)}")
                    nodes.append(f"    {do_intend(depth)}}}")
                case _:
                    nodes.append("")
        return '\n'.join(nodes)

    return '{\n' + walk(diff, 0) + '\n}'
