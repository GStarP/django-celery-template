from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from audio_score.tasks import t_ping
        t_ping.delay()
