import urllib.request

from bs4 import BeautifulSoup
from django.core.cache import cache

#CACHE_TIMEOUT is in seconds.
CACHE_TIMEOUT = 60 * 10
CHARTS_CACHE_KEY = 'superset_charts'


class _SupersetChartRefs:

    def __init__(self,
                 url="https://superset-myeqip.catalpa.build/chart/list/"):
        self.url = url

    def _get_chart_anchors(self):
        with urllib.request.urlopen(self.url) as response:
            html = response.read()

        soup = BeautifulSoup(html)
        all_links = soup("a")
        return all_links

    def __iter__(self):
        anchors = self._get_chart_anchors()
        for chart_anchor in anchors:
            if "slice_id" in chart_anchor["href"]:
                yield (chart_anchor["href"], chart_anchor.text.strip(),)


def get_superset_chart_choices():
    chart_names_and_urls = cache.get(CHARTS_CACHE_KEY)
    if chart_names_and_urls is None:
        chart_names_and_urls = tuple(_SupersetChartRefs())
        cache.set(CHARTS_CACHE_KEY, chart_names_and_urls,
                  timeout=CACHE_TIMEOUT)
    return chart_names_and_urls
