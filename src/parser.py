from bs4 import BeautifulSoup
from datetime import datetime
import re

class Parser:
    def __init__(self):
        pass

    def parse(self, html_text):
        return BeautifulSoup(html_text, 'html.parser')

    def get_usd_course(self, html_text):
        parsed_html = self.parse(html_text)
        tables = parsed_html.find_all("table", class_="mod_rate_day")
        tables += parsed_html.find_all("table", class_="mod_rate_today")
        result = dict()
        for table in tables:
            caption = table.find("caption")
            if not caption:
                continue
            date = caption.get_text(strip=True)

            rows = table.find_all("tr")
            for row in rows:
                td = row.find("td", class_="mod_rate_oper")
                if td and "Корал Тревел" in td.get_text(strip=True):
                    cells = row.find_all("td")
                    euro = cells[1].text.strip()
                    usd = cells[4].text.strip()
                    normal_date = re.search(r"\d{2}\.\d{2}\.\d{2}", date).group()
                    result[normal_date] = cells[4].text.strip()
                    break
        sorted_rates = dict(sorted(
            result.items(),
            key=lambda item: datetime.strptime(item[0], "%d.%m.%y")
        ))
        return sorted_rates






