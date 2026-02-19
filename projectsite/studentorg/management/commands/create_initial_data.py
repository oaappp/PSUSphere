from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = "Create initial data for the application"

    def handle(self, *args, **kwargs):
        # These depend on College/Program existing already.
        if not College.objects.exists() or not Program.objects.exists():
            self.stdout.write(self.style.ERROR(
                "Please add Colleges and Programs first (via admin) before running faker."
            ))
            return

        self.create_organization(10)
        self.create_students(50)
        self.create_membership(10)

    def create_organization(self, count):
        fake = Faker()

        for _ in range(count):
            organization_name = " ".join(fake.words(2)).title()
            Organization.objects.create(
                name=organization_name,
                college=College.objects.order_by("?").first(),
                description=fake.sentence(),
            )

        self.stdout.write(self.style.SUCCESS("Initial data for organization created successfully."))

    def create_students(self, count):
        fake = Faker("en_PH")

        for _ in range(count):
            year = fake.random_int(2020, 2025)
            sem = fake.random_int(1, 8)
            num = fake.random_number(digits=4, fix_len=True)

            Student.objects.create(
                student_id=f"{year}-{sem}-{num}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=Program.objects.order_by("?").first(),
            )

        self.stdout.write(self.style.SUCCESS("Initial data for students created successfully."))

    def create_membership(self, count):
        fake = Faker()

        for _ in range(count):
            OrgMember.objects.create(
                student=Student.objects.order_by("?").first(),
                organization=Organization.objects.order_by("?").first(),
                date_joined=fake.date_between(start_date="-2y", end_date="today"),
            )

        self.stdout.write(self.style.SUCCESS("Initial data for student organization created successfully."))