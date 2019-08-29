import urllib.request
from urllib.error import URLError

from bs4 import BeautifulSoup
from django.core.cache import cache
from sentry_sdk import capture_exception

from .blocks_ui_text import _ChartBlockStrings

# CACHE_TIMEOUT is in seconds.
CACHE_TIMEOUT = 60 * 10
CHARTS_CACHE_KEY = "superset_charts"


class SupersetChartRefs:
    def __init__(self, url="https://superset-myeqip.catalpa.build/chart/list/"):
        self.url = url

    def _scrape_links_with_beautiful_soup(self):
        with urllib.request.urlopen(self.url) as response:
            html = response.read()
        soup = BeautifulSoup(html)
        all_links = soup("a")
        return all_links

    def _get_superset_chart_page_anchors(self):
        try:
            return self._scrape_links_with_beautiful_soup()
        except URLError:
            raise URLError("Could not connect to My-EQIP's Superset.")

    def __iter__(self):
        page_anchors = self._get_superset_chart_page_anchors()

        for chart_anchor in page_anchors:
            if "slice_id" not in chart_anchor["href"]:
                # Ignore page anchors that don't link to charts.
                continue

            yield (chart_anchor["href"], chart_anchor.text.strip())


def get_superset_chart_choices():
    chart_names_and_urls = cache.get(CHARTS_CACHE_KEY)

    if chart_names_and_urls is not None:
        return chart_names_and_urls

    try:
        chart_names_and_urls = tuple(SupersetChartRefs())
        cache.set(CHARTS_CACHE_KEY, chart_names_and_urls, timeout=CACHE_TIMEOUT)

    except URLError as e:
        capture_exception(e)
        chart_names_and_urls = [(None, _ChartBlockStrings.superset_connection_error)]
    return chart_names_and_urls
