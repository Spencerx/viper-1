# This file is part of Viper - https://github.com/viper-framework/viper
# See the file 'LICENSE' for copying permission.

import socket

from fake_useragent import UserAgent
from viper.common.out import print_error

try:
    from urllib.request import Request, urlopen
except:
    from urllib2 import Request, urlopen

try:
    from urllib.error import HTTPError, URLError
except:
    from urllib2 import HTTPError, URLError

try:
    import socks
    HAVE_SOCKS = True
except ImportError:
    HAVE_SOCKS = False


def download(url, tor=False):
    def create_connection(address, timeout=None, source_address=None):
        sock = socks.socksocket()
        sock.connect(address)
        return sock

    if tor:
        if not HAVE_SOCKS:
            print_error(
                "Missing dependency, install socks (`pip install SocksiPy`)")
            return None

        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
        socket.socket = socks.socksocket
        socket.create_connection = create_connection

    try:
        ua = UserAgent()
        req = Request(url)
        req.add_header('User-Agent', ua.random)
        res = urlopen(req)

        data = res.read()
    except HTTPError as e:
        print_error(e)
    except URLError as e:
        if tor and e.reason.errno == 111:
            print_error("Connection refused, maybe Tor is not running?")
        else:
            print_error(e)
    except Exception as e:
        print_error("Failed download: {0}".format(e))
    else:
        return data
