import csv
import logging

from django.core.management.base import BaseCommand, CommandError

from code_parser.models import LocodeCode

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Initialize db"

    def add_arguments(self, parser):
        parser.add_argument(
            "filename_path",
            nargs="?",
            type=str,
            help="Please use UNLOCODE CodeList csv table for upload info to DB",
        )

    def handle(self, *args, **options):
        logger.info("Started import db command")
        if options["filename_path"]:
            filename_path = options["filename_path"]
            if not filename_path.split(".")[-1] == "csv":
                raise CommandError("Input file not csv table")
        else:
            filename_path = "2020-1 UNLOCODE CodeListPart1.csv"
        try:
            with open(filename_path, encoding="cp1252", newline="") as csvfile:
                rows = csv.reader(csvfile, delimiter=",", quotechar='"')
                for row in rows:
                    LocodeCode.objects.create(
                        change_indicator=row[0],
                        locode_country_code=row[1],
                        locode_location_code=row[2],
                        name=row[3],
                        name_wo_diacritics=row[4],
                        sub_division=row[5],
                        function=row[6],
                        status=row[7],
                        date=row[8],
                        iata=row[9],
                        coordinates=row[10],
                        remarks=row[11],
                    )
            logger.info("Finished import db command")
        except Exception as e:
            logger.error(f"Something was incorrect {e}")
