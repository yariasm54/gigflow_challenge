"""Populating the database with test records"""

# Django Libraries
from django.core.management import call_command
from django.core.management.base import BaseCommand

# Own Libraries
from server.apps.service.models import Package
from server.apps.service.models import ServiceType
from server.apps.service.models import Deliverable
from server.apps.service.factory.package import PackageFactory
from server.apps.service.factory.service_type import ServiceTypeFactory
from server.apps.service.factory.deliverable import DeliverableFactory

DEFAULT_VALUE = 100


class Command(BaseCommand):
    """Command to seed the database.

    With this class the population of the test tables for local environments
    is carried out.

    Args:
        BaseCommand: The base class from which all management commands ultimately
                     derive.
    """

    help = "Seeds the database."

    @staticmethod
    def add_arguments(parser):
        """add_arguments

        Args:
            parser:.
        """
        parser.add_argument(
            "--seeds",
            default=DEFAULT_VALUE,
            type=int,
            help=f"The number of registers to create. {DEFAULT_VALUE} records by default",
        )

    def handle(self, *args, **options):
        """Handle Database Population.

        This method executes each population of the necessary tables in an orderly manner,
        from a factory from the fatboy library.
        """

        # =============================== Migrating DataBase =========================== #
        self.stdout.write(self.style.MIGRATE_HEADING("Migrating the database..."))
        call_command("migrate", interactive=False)

        # =============================== Migrating DataBase =========================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING("Populating GigFlowTest models..."),
        )

        # ======================= Loading Service types objects ======================= #
        if ServiceType.objects.all().exists():
            self.stdout.write(
                self.style.NOTICE("Service type objects already "
                                  "exist in the database."),
            )
            self.stdout.flush()
        else:
            self.stdout.write("  Loading Service type objects...", ending="")
            self.stdout.flush()
            for count in range(options["seeds"]):
                ServiceTypeFactory.create()
            self.stdout.flush()
            self.stdout.write(self.style.SUCCESS("OK"))

        # ======================= Loading Packages objects ======================= #
        if Package.objects.all().exists():
            self.stdout.write(
                self.style.NOTICE("Package objects already "
                                  "exist in the database."),
            )
            self.stdout.flush()
        else:
            self.stdout.write("  Loading Package objects...", ending="")
            self.stdout.flush()
            for count in range(options["seeds"]*3):
                PackageFactory.create()
            self.stdout.flush()
            self.stdout.write(self.style.SUCCESS("OK"))

        # ======================= Loading Deliverable objects ======================= #
        if Deliverable.objects.all().exists():
            self.stdout.write(
                self.style.NOTICE("Deliverable objects already "
                                  "exist in the database."),
            )
            self.stdout.flush()
        else:
            self.stdout.write("  Loading Deliverable objects...", ending="")
            self.stdout.flush()
            for count in range(options["seeds"]*3*3):
                DeliverableFactory.create()
            self.stdout.flush()
            self.stdout.write(self.style.SUCCESS("OK"))
