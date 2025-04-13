from site_visitor import SiteVisitor
from parser import Parser
from config import Config
from bot import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
from zoneinfo import ZoneInfo

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info("program start")
    print("program start")
    conf = Config("./","config.toml")
    bot = Bot(conf.get_param("bot", "token"), conf.get_param("bot", "chat_id"))
    site_vis = SiteVisitor(conf.get_param("site", "url"))
    parser = Parser()
    def send_daily_rates():
        html = site_vis.getHtml()
        courses = parser.get_usd_course(html)
        message = "\n".join([f"{date}: {rate} руб/долл" for date, rate in courses.items()])
        bot.send_message(message)
        print("✅ Сообщение отправлено:", message)
    scheduler = BlockingScheduler(timezone=ZoneInfo("Europe/Moscow"))
    scheduler.add_job(send_daily_rates, 'cron', hour=conf.get_param("scheduler", "hour"), minute=conf.get_param("scheduler", "minute"))
    scheduler.start()
    logger.info("program end")


if __name__ == "__main__":
    main()

