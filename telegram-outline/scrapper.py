import json
import logging
import requests


logging.basicConfig(
    format='%(asctime)s | %(levelname)-8s | %(name)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

url_src = 'https://www1.folha.uol.com.br/poder/2021/10/pf-e-ministerio-publico-agora-escondem-nome-da-lava-jato-ate-em-fase-da-operacao.shtml'
url_outline = (
    'https://api.outline.com/v3/' +
    'parse_article?' +
    f'source_url={url_src}'
)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,pt-BR;q=0.8,pt;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br'
}

result = requests.get(url_outline, headers=headers)
data, success = json.loads(result.content).values()

if not success:
    logger.error(f'Could not load outline url {url_src}')

microdata = data['meta']['microdata']

microdata['itemprop:description']
data['author'], data['date']
data['article_url']

microdata['itemprop:articleBody']
