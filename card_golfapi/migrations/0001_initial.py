# Generated by Django 3.2.5 on 2021-07-28 22:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suite', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=15)),
                ('score', models.IntegerField()),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerCount', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(4)])),
                ('needPlayers', models.BooleanField()),
                ('complete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cardCount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_golfapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.BooleanField()),
                ('name', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Game', to='card_golfapi.game')),
            ],
        ),
        migrations.CreateModel(
            name='RoundScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='card_golfapi.round')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_golfapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HandCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revealed', models.BooleanField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_golfapi.card')),
                ('hand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_golfapi.hand')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='gameType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='card_golfapi.gametype'),
        ),
        migrations.AddField(
            model_name='game',
            name='playerAction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='PlayerAction', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Round', to='card_golfapi.round'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DiscardCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_golfapi.card')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_golfapi.deck')),
            ],
        ),
        migrations.CreateModel(
            name='Discard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_golfapi.game')),
            ],
        ),
        migrations.CreateModel(
            name='DeckCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_golfapi.card')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_golfapi.deck')),
            ],
        ),
        migrations.AddField(
            model_name='deck',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_golfapi.game'),
        ),
    ]
