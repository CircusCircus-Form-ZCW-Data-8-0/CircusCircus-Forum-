from urllib.parse import urlparse, urlsplit
import re

def links(content):
    split_content = re.split(r'(\s+)', content)
    new_string = ''
    for word in split_content:
        url = urlparse(word)
        if (url.scheme and url.netloc and url.path is not None) and len(url.netloc.split('.')) > 1 \
                and url.scheme in ['http', 'https']:
            url1 = ''
            link_string = '<a href = "'
            link_string = link_string + word
            link_string = link_string + '">'
            link_string = link_string + word + '</a><br>\n'
            url1 += link_string
            new_string += url1
        else:
            new_string += word
    return new_string
#
# content = 'this link      is https://yoda.zipcode.rocks/apache-spark-for-zcw-data/'
#
# print(links(content))