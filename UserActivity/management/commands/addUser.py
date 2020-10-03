import names
import random
from datetime import datetime, timedelta
from UserActivity.models import UserProfile
from django.core.management.base import BaseCommand


def time_zone_func():
    zone = ['Asia/Kolkata', 'America/New_York',
            'Africa/Maseru', 'US/Central',
            'Europe/Athens']
    return random.choice(zone)


def random_name():
    first = ("Super", "Retarded", "Great", "Elon", "Elona", "Brave", "Shelly", "Cool", "Poor", "Richy", 'James'
             "Fast", "Gummy", "Monty", "Masked", "Unusual", "Hilis", "Sherlok", "MLG", "Mlg", "lilput", "Lil")
    second = ("Codey", "Velly", "Mantis", "Musk", "Holly", "Bear", "Gery", "Goblin", "Legis", "Holmes",
              "William", "Pris", "Spy", "Bond", "Spooderman", "Carrot", "Rich", "Quickscoper", "Quickscoper")
    firrst = random.choice(first)
    seccond = random.choice(second)
    name = (firrst + " " + seccond)
    return name


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('--id', type=str,
                            help='Indicates the Id User')
        parser.add_argument('--full_name', type=str,
                            help='Indicates the Full Name')
        parser.add_argument('--start_time', type=str,
                            help='Indicates the Start Time')
        parser.add_argument('--end_time', type=str,
                            help='Indicates the End Time')
        parser.add_argument('--time_zone', type=str,
                            help='Indicates the Time Zone')

    def handle(self, *args, **options):
        today = datetime.now()
        id = options['id']
        full_name = options['full_name'] if options['full_name'] \
            else names.get_full_name()
        start_time = options['start_time'] if options['start_time'] \
            else today.strftime("%B %d, %Y %H:%M:%p")
        end_time = options['end_time'] if options['end_time'] \
            else (today + timedelta(hours=2)).strftime("%B %d, %Y %H:%M:%p")
        time_zone = options['time_zone'] if options['time_zone'] \
            else time_zone_func()
        # if id:
        #     user = UserProfile.objects.filter(id=id)
        #     if user:
        #         user.update(
        #             full_name=full_name, start_time=start_time,
        #             end_time=end_time, time_zone=time_zone)
        #         print('User is successfully updated', user[0].id)
        #     else:
        #         user = UserProfile.objects.create(
        #             full_name=full_name, start_time=start_time,
        #             end_time=end_time, time_zone=time_zone)
        #         print('User is successfully created', user.id)
        # else:
        user = UserProfile.objects.create(
            full_name=full_name, start_time=start_time,
            end_time=end_time, time_zone=time_zone)
        print('User Activity is Successfully Created', user.id)  
