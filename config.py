# coding: utf8

import sys


class LocalConfig(object):
    py3 = sys.version_info[0] >= 3

    LOGGING_CONF = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                'format': '%(message)s'
            },
            'file': {
                'format': '[%(asctime)s][%(levelname)s][%(pathname)s:%(lineno)s][%(funcName)s]: %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'console'
            },
            'log_file': {
                'class': 'logging.handlers.WatchedFileHandler',
                'level': 'DEBUG',
                'formatter': 'file',
                'filename': 'log/renrenBackup.log',
                'encoding': 'utf-8'
            }
        },
        'loggers': {
            '': {
                'handlers': ['console', 'log_file'],
                'level': 'DEBUG',
            }
        }
    }

    crawler = None
    DATABASE = 'renren_bak.db'

    BAK_OUTPUT_TAR = 'backup.tar'

    BAD_IMAGE_MD5 = 'ced9341d5a30f1a00256488285612337'

    COOKIE_FILE = "./.cookies.json"
    HEADERS_FILE = './.headers.json'

    ITEMS_PER_PAGE = 20
    TIMEOUT = 15
    RETRY_TIMES = 10

    DEFAULT_HEAD_PIC = './static/men_tiny.gif'

    ENCRYPT_KEY_URL = "http://login.renren.com/ajax/getEncryptKey"
    LOGIN_URL = "https://rrwapi.renren.com/account/v1/loginByPassword"
    ICODE_URL = "https://rrwapi.renren.com/icode/v1/getBase64ImgCode"
    ICODE_FILEPATH = "./static/icode.jpg"

    HOMEPAGE_URL = "http://www.renren.com/personal/{uid}/details"

    COMMENT_URL = "http://comment.renren.com/comment/xoa2"
    GLOBAL_COMMENT_URL = "http://comment.renren.com/comment/xoa2/global"
    LIKE_URL = "http://like.renren.com/showlikedetail"

    STATUS_URL = "https://rrwapi.renren.com/feed/v1/homepage"

    GOSSIP_PAGE_URL = "http://gossip.renren.com/list/{uid}"
    GOSSIP_URL = "https://rrwapi.renren.com/messageboard/v1/getMessageList"

    ALBUM_LIST_URL = "https://rrwapi.renren.com/feed/v1/albums"
    ALBUM_SUMMARY_URL = "https://rrwapi.renren.com/feed/v1/album"
    PHOTO_INFO_URL = "http://photo.renren.com/photo/{uid}/photo-{photo_id}/layer"

    BLOG_LIST_URL = "https://rrwapi.renren.com/feed/v1/blogs"
    # BLOGS_PER_PAGE = 10
    BLOG_DETAIL_URL = "https://renren.com/feed/{blog_id}/{uid}"


config = LocalConfig
