from bs4 import BeautifulSoup

def get_full_html():
    file = open(r'cp_i.html','r')
    lines = file.readlines()
    return ''.join(lines)

def test_get_full_html():
    try:
        return_value = get_full_html()
        if not type(return_value) is str:
            raise Exception('not a string!')
        if len(return_value) == 0:
            raise Exception('empty string')
    except:
        print('Not working!')

def get_inner_content_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    inner_contents = soup.find_all('div', class_='inner-content')
    links = inner_contents[0].find_all('a')
    return list(map(lambda link: "http://composingprograms.com" + link['href'][1:], links))

def test_get_inner_content_text():
    html = get_full_html()
    links = get_inner_content_text(html)
    if "http://composingprograms.com/pages/47-distributed-data-processing.html" not in links:
        raise Exception('Example not in links')

print(get_inner_content_text(get_full_html()))
# TODO - still gives back some strange urls as well - we need to get rid of them:
#  'http://composingprograms.comttp://mitpress.mit.edu/sicp/' ??
