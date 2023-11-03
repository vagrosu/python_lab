def build_xml_element(tag, content, **params):
    el = f'<{tag}'
    for key, val in params.items():
        el += f' {key}="{val}"'

    el += f'>{content}</{tag}>'
    return el


if __name__ == '__main__':
    print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))