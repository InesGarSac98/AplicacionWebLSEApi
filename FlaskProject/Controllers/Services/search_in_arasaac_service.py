from subprocess import check_output
from pyquery import PyQuery


def search(word):
    url = "https://arasaac.org/lse/search/" + word
    arasaacDom = str(check_output([
        'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        '--headless',
        '--dump-dom',
        '--disable-gpu',
        url
    ]))

    pq = PyQuery(arasaacDom)

    image = pq('img[src*="lse-images"]').eq(0).attr('src')
    video = pq('video[src*="lse-acepciones"]').eq(0).attr('src')
    videoDefinition = pq('video[src*="lse-definiciones"]').eq(0).attr('src')

    if image == '' or video == '' or videoDefinition == '':
        return None

    return {
        'name': word,
        'image': image,
        'video': video,
        'videoDefinition': videoDefinition
    }
