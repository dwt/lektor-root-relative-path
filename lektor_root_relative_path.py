# -*- coding: utf-8 -*-
from urlparse import urljoin
import urllib

from lektor.pluginsystem import Plugin
from furl import furl


class RootRelativePathPlugin(Plugin):
    name = u'root-relative-path'
    description = u'Returns root relative path list as tuple like \
[(toppage_url, toppage_name), ...(parent_url, parent_name), (url, name)]'

    def on_setup_env(self, **extra):
        navi_top_page_name = self.get_config().get('navi_top_page_name') or 'Top Page'
        def root_relative_path_list(url):
            # If current page is root, returns []
            if url == '/':
                return []
            lis = furl(url).path.segments
            url = '/'
            name = navi_top_page_name
            path_list = [(url, name)]
            for i in lis:
                url = urllib.quote(urljoin(url, '%s' % i))
                name = i
                path_list.append((url, name))
                url = url + '/'

            return path_list
        self.env.jinja_env.filters['root_relative_path_list'] = root_relative_path_list