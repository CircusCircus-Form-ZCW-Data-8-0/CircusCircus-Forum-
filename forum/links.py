
import re


def links(content):
    new_content = ''
    pattern = re.compile(r'(https?://[^\s]+)')
    if re.search(pattern, content) is not None:
        word2 = re.search(pattern, content).group(1)
        link_string = '<a href = "'
        link_string = link_string + word2
        link_string = link_string + '">'
        link_string = link_string + word2 + '</a><br>\n'
        new_content += link_string
        return new_content
    else:
        return content
