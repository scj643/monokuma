from monokuma import bot
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    token = os.environ.get('DISCORD_API_TOKEN')
    if not token:
        raise ValueError('No API token provided.')
    logger.info("starting")
    bot.run(token)
