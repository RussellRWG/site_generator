from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            delimiter_count = node.text.count(delimiter)
            if delimiter_count == 0:
                new_nodes.append(node)
            elif (delimiter_count % 2) != 0:
                raise Exception("Invalid markdown text: Mismatched delimiters")
            else:
                split_text = node.text.split(delimiter)
                even_odd = "odd"
                for text in split_text:
                    if len(text) == 0:
                        continue
                    elif even_odd == "odd":
                        new_nodes.append(TextNode(text, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(text, text_type))
                    even_odd = "even" if even_odd == "odd" else "odd"
        else:
            new_nodes.append(node)
    return new_nodes
