
from urllib.parse import urlparse, urlsplit

def links(content):
    url = urlparse(content)
    if (url.scheme and url.netloc and url.path is not None) and len(url.netloc.split('.')) > 1:
        url1 = ''
        link_string = '<a href = "'
        link_string = link_string + content
        link_string = link_string + '">'
        link_string = link_string + content + '</a><br>\n'
        url1 += link_string
        return url1
    else:
        return content

