from .constants import RESULTS_DIR_NAME, SPIDERS_DIR


BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = SPIDERS_DIR
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS_DIR_NAME}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

LOG_ENABLED = False
LOG_LEVEL = 'ERROR'
HTTP_CACHE = True
HTTPCACHE_ENABLED = True
