
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
            # Connect to MongoDB using pymongo for raw operations
            client = MongoClient('mongodb://localhost:27017')
            db = client['octofit_db']

            # Diagnostic: print collection names and counts before deletion
            print("Collections before deletion:")
            collections_to_clear = [
                'octofit_tracker_user',
                'octofit_tracker_team',
                'octofit_tracker_activity',
                'octofit_tracker_leaderboard',
                'octofit_tracker_workout',
                'auth_user_user_permissions',
                'auth_permission',
                'django_session',
                'auth_group',
                'django_migrations',
                '__schema__',
                'auth_user_groups',
                'auth_user',
                'auth_group_permissions',
                'django_admin_log',
                'django_content_type'
            ]
            for coll in collections_to_clear:
                if coll in db.list_collection_names():
                    db[coll].delete_many({})
            print("Collections after deletion:", db.list_collection_names())

            # Create teams
            Team.objects.create(name='Marvel', description='Marvel Superheroes')
            Team.objects.create(name='DC', description='DC Superheroes')

            # Reload teams from DB
            marvel = Team.objects.get(name='Marvel')
            dc = Team.objects.get(name='DC')

            # Create users
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
            User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True)
            User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', is_superhero=True)

            # Ensure DB commit and reload users from DB
            ironman = User.objects.get(email='ironman@marvel.com')
            captain = User.objects.get(email='captain@marvel.com')
            batman = User.objects.get(email='batman@dc.com')
            wonderwoman = User.objects.get(email='wonderwoman@dc.com')

            # Create activities
            Activity.objects.create(user_email='ironman@marvel.com', type='Running', duration=30, date='2025-10-01')
            Activity.objects.create(user_email='captain@marvel.com', type='Cycling', duration=45, date='2025-10-02')
            Activity.objects.create(user_email='batman@dc.com', type='Swimming', duration=60, date='2025-10-03')
            Activity.objects.create(user_email='wonderwoman@dc.com', type='Yoga', duration=50, date='2025-10-04')

            # Create leaderboard
            Leaderboard.objects.create(team_name='Marvel', points=100)
            Leaderboard.objects.create(team_name='DC', points=90)

            # Create workouts
            Workout.objects.create(name='Super Strength', description='Strength training for superheroes', suggested_for='marvel')
            Workout.objects.create(name='Agility Boost', description='Agility training for superheroes', suggested_for='dc')

            print("Collections after repopulation:", db.list_collection_names())
            self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
