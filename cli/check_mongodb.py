import time
import click

from database.mongodb import MongoDB
from utils.logger_utils import get_logger

logger = get_logger('MongoCheck')


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-url', '--connection_url', default=None, type=str, help='Connection url.\nExample: mongodb://username:password@192.168.1.4:27027')
@click.option('-d', '--database', default=None, type=str, help='Database name')
@click.option('-c', '--collection', default=None, type=str, help='Collection name')
def check_mongodb(url, db, coll):
    _db = MongoDB(connection_url=url, database=db, collection=coll)
    logger.info(f'Connected to database {_db.connection_url}')

    logger.info('Done')
