# Generated by Django 2.2.24 on 2024-11-26 03:05

import bestiary.models.base
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AwakenCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dungeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com2us_id', models.IntegerField(db_index=True)),
                ('enabled', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.IntegerField(blank=True, choices=[(0, 'Scenario'), (1, 'Cairos Dungeon'), (2, 'Tower of Ascension'), (3, 'Rift Raid'), (4, 'Rift Beast'), (5, 'Hall of Heroes'), (6, 'Arena'), (7, 'Guild Content'), (8, 'Secret Dungeon'), (9, 'World Boss'), (10, 'Dimensional Hole'), (99, 'Other')], null=True)),
                ('icon', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ['category', 'com2us_id'],
                'unique_together': {('com2us_id', 'category')},
            },
        ),
        migrations.CreateModel(
            name='GameItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com2us_id', models.IntegerField(db_index=True)),
                ('category', models.IntegerField(choices=[(1, 'Monster'), (6, 'Currency'), (9, 'Summoning Scroll'), (10, 'Booster'), (11, 'Essence'), (12, 'Monster Piece'), (19, 'Guild Monster Piece'), (25, 'Rainbowmon'), (27, 'Rune Craft'), (29, 'Craft Material'), (30, 'Secret Dungeon'), (61, 'Enhancing Monster'), (73, 'Artifact'), (75, 'Artifact Craft Material'), (82, 'Unknown Category'), (101, 'Witcher')], db_index=True, help_text='Typically corresponds to `item_master_type` field')),
                ('name', models.CharField(max_length=200)),
                ('icon', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('slug', models.CharField(max_length=200)),
                ('sell_value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('category', 'com2us_id'),
                'unique_together': {('com2us_id', 'category')},
            },
        ),
        migrations.CreateModel(
            name='HomunculusSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LeaderSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.IntegerField(choices=[(1, 'HP'), (2, 'Attack Power'), (3, 'Defense'), (4, 'Attack Speed'), (5, 'Critical Rate'), (6, 'Resistance'), (7, 'Accuracy'), (8, 'Critical DMG')], help_text='Monster stat which is granted the bonus')),
                ('amount', models.IntegerField(help_text='Amount of bonus granted')),
                ('area', models.IntegerField(choices=[(1, 'General'), (2, 'Dungeon'), (3, 'Element'), (4, 'Arena'), (5, 'Guild')], default=1, help_text='Where this leader skill has an effect')),
                ('element', models.CharField(blank=True, choices=[('pure', 'Pure'), ('fire', 'Fire'), ('wind', 'Wind'), ('water', 'Water'), ('light', 'Light'), ('dark', 'Dark'), ('intangible', 'Intangible')], help_text='Element of monster which this leader skill applies to', max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Leader Skill',
                'verbose_name_plural': 'Leader Skills',
                'ordering': ['attribute', 'amount', 'element'],
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField()),
                ('difficulty', models.IntegerField(blank=True, choices=[(1, 'Normal'), (2, 'Hard'), (3, 'Hell')], null=True)),
                ('energy_cost', models.IntegerField(blank=True, help_text='Energy cost to start a run', null=True)),
                ('xp', models.IntegerField(blank=True, help_text='XP gained by fully clearing the level', null=True)),
                ('frontline_slots', models.IntegerField(default=5)),
                ('backline_slots', models.IntegerField(blank=True, help_text='Leave null for normal dungeons', null=True)),
                ('total_slots', models.IntegerField(default=5, help_text='Maximum monsters combined front/backline.')),
                ('dungeon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Dungeon')),
            ],
            options={
                'ordering': ('dungeon', 'difficulty', 'floor'),
                'unique_together': {('dungeon', 'floor', 'difficulty')},
            },
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('com2us_id', models.IntegerField(blank=True, db_index=True, help_text='ID given in game data files', null=True)),
                ('family_id', models.IntegerField(blank=True, help_text='Identifier that matches same family monsters', null=True)),
                ('skill_group_id', models.IntegerField(blank=True, help_text='Identifier that matches same skillup monsters (i.e. Street Figher monsters with C2U counterparts)', null=True)),
                ('image_filename', models.CharField(blank=True, max_length=250, null=True)),
                ('element', models.CharField(choices=[('pure', 'Pure'), ('fire', 'Fire'), ('wind', 'Wind'), ('water', 'Water'), ('light', 'Light'), ('dark', 'Dark'), ('intangible', 'Intangible')], default='fire', max_length=10)),
                ('archetype', models.CharField(choices=[('attack', 'Attack'), ('hp', 'HP'), ('support', 'Support'), ('defense', 'Defense'), ('material', 'Material'), ('intangible', 'Intangible')], default='attack', max_length=10)),
                ('base_stars', models.IntegerField(choices=[(1, '1⭐'), (2, '2⭐'), (3, '3⭐'), (4, '4⭐'), (5, '5⭐'), (6, '6⭐')], help_text='Display stars in game')),
                ('natural_stars', models.IntegerField(choices=[(1, '1⭐'), (2, '2⭐'), (3, '3⭐'), (4, '4⭐'), (5, '5⭐'), (6, '6⭐')], help_text="Stars of the monster's lowest awakened form")),
                ('obtainable', models.BooleanField(default=True, help_text='Is available for players to acquire')),
                ('can_awaken', models.BooleanField(default=True, help_text='Has an awakened form')),
                ('is_awakened', models.BooleanField(default=False, help_text='Is the awakened form')),
                ('awaken_level', models.IntegerField(choices=[(0, 'Unawakened'), (1, 'Awakened'), (2, 'Second Awakening'), (-1, 'Incomplete')], default=0, help_text='Awakening level')),
                ('awaken_bonus', models.TextField(blank=True, help_text='Bonus given upon awakening')),
                ('skill_ups_to_max', models.IntegerField(blank=True, help_text='Number of skill-ups required to max all skills', null=True)),
                ('raw_hp', models.IntegerField(blank=True, help_text='HP value from game data files', null=True)),
                ('raw_attack', models.IntegerField(blank=True, help_text='ATK value from game data files', null=True)),
                ('raw_defense', models.IntegerField(blank=True, help_text='DEF value from game data files', null=True)),
                ('base_hp', models.IntegerField(blank=True, help_text='HP at base_stars lvl 1', null=True)),
                ('base_attack', models.IntegerField(blank=True, help_text='ATK at base_stars lvl 1', null=True)),
                ('base_defense', models.IntegerField(blank=True, help_text='DEF at base_stars lvl 1', null=True)),
                ('max_lvl_hp', models.IntegerField(blank=True, help_text='HP at 6-stars lvl 40', null=True)),
                ('max_lvl_attack', models.IntegerField(blank=True, help_text='ATK at 6-stars lvl 40', null=True)),
                ('max_lvl_defense', models.IntegerField(blank=True, help_text='DEF at 6-stars lvl 40', null=True)),
                ('speed', models.IntegerField(blank=True, null=True)),
                ('crit_rate', models.IntegerField(blank=True, null=True)),
                ('crit_damage', models.IntegerField(blank=True, null=True)),
                ('resistance', models.IntegerField(blank=True, null=True)),
                ('accuracy', models.IntegerField(blank=True, null=True)),
                ('homunculus', models.BooleanField(default=False)),
                ('craft_cost', models.IntegerField(blank=True, help_text='Mana cost to craft this monster', null=True)),
                ('awaken_mats_fire_low', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_fire_mid', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_fire_high', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_water_low', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_water_mid', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_water_high', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_wind_low', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_wind_mid', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_wind_high', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_light_low', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_light_mid', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_light_high', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_dark_low', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_dark_mid', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_dark_high', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_magic_low', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_magic_mid', models.IntegerField(blank=True, default=0)),
                ('awaken_mats_magic_high', models.IntegerField(blank=True, default=0)),
                ('farmable', models.BooleanField(default=False, help_text='Monster can be acquired easily without luck')),
                ('fusion_food', models.BooleanField(default=False, help_text='Monster is used as a fusion ingredient')),
                ('bestiary_slug', models.SlugField(editable=False, max_length=255, null=True)),
                ('awaken_cost', models.ManyToManyField(related_name='_monster_awaken_cost_+', through='bestiary.AwakenCost', to='bestiary.GameItem')),
                ('awakens_from', models.ForeignKey(blank=True, help_text='Unawakened form of this monster', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='bestiary.Monster')),
                ('awakens_to', models.ForeignKey(blank=True, help_text='Awakened form of this monster', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='bestiary.Monster')),
            ],
            options={
                'ordering': ['name', 'element'],
            },
            bases=(models.Model, bestiary.models.base.Elements, bestiary.models.base.Stars, bestiary.models.base.Archetype),
        ),
        migrations.CreateModel(
            name='ScalingStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(max_length=20)),
                ('com2us_desc', models.CharField(blank=True, db_index=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Scaling Stat',
                'verbose_name_plural': 'Scaling Stats',
                'ordering': ['stat'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com2us_id', models.IntegerField(blank=True, db_index=True, help_text='ID given in game data files', null=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('slot', models.IntegerField(default=1, help_text='Which button position the skill is in during battle')),
                ('cooltime', models.IntegerField(blank=True, help_text='Number of turns until skill can be used again', null=True)),
                ('hits', models.IntegerField(default=1, help_text='Number of times this skill hits an enemy')),
                ('aoe', models.BooleanField(default=False, help_text='Skill affects all enemies or allies')),
                ('random', models.BooleanField(default=False, help_text='Skill attacks randomly')),
                ('passive', models.BooleanField(default=False, help_text='Skill activates automatically')),
                ('max_level', models.IntegerField()),
                ('icon_filename', models.CharField(blank=True, max_length=100, null=True)),
                ('multiplier_formula', models.TextField(blank=True, help_text='Parsed multiplier formula', null=True)),
                ('multiplier_formula_raw', models.CharField(blank=True, help_text='Multiplier formula given in game data files', max_length=150, null=True)),
                ('level_progress_description', models.TextField(blank=True, help_text='Description of bonus each skill level', null=True)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ['slot', 'name'],
            },
        ),
        migrations.CreateModel(
            name='SkillEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(-1, 'Debuff'), (0, 'Neutral'), (1, 'Buff')], db_index=True, default=0)),
                ('is_buff', models.BooleanField(default=True, help_text='Effect is beneficial to affected monster')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('icon_filename', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Skill Effect',
                'verbose_name_plural': 'Skill Effects',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon_filename', models.CharField(blank=True, max_length=100, null=True)),
                ('farmable_source', models.BooleanField(default=False)),
                ('meta_order', models.IntegerField(db_index=True, default=0)),
            ],
            options={
                'ordering': ['meta_order', 'icon_filename', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Wave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Level')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillUpgrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('effect', models.IntegerField(choices=[(0, 'Effect Rate +{0}%'), (1, 'Damage +{0}%'), (2, 'Recovery +{0}%'), (3, 'Cooltime Turn -{0}'), (4, 'Shield +{0}%'), (5, 'Attack Bar Recovery +{0}%'), (6, 'Harmful Effect Rate +{0} Turns')])),
                ('amount', models.IntegerField()),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upgrades', to='bestiary.Skill')),
            ],
            options={
                'ordering': ('level',),
            },
        ),
        migrations.CreateModel(
            name='SkillEffectDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aoe', models.BooleanField(default=False, help_text='Effect applies to entire friendly or enemy group')),
                ('single_target', models.BooleanField(default=False, help_text='Effect applies to a single monster')),
                ('self_effect', models.BooleanField(default=False, help_text='Effect applies to the monster using the skill')),
                ('chance', models.IntegerField(blank=True, help_text='Chance of effect occuring per hit', null=True)),
                ('on_crit', models.BooleanField(default=False)),
                ('on_death', models.BooleanField(default=False)),
                ('random', models.BooleanField(default=False, help_text='Skill effect applies randomly to the target')),
                ('quantity', models.IntegerField(blank=True, help_text='Number of items this effect affects on the target', null=True)),
                ('all', models.BooleanField(default=False, help_text='This effect affects all items on the target')),
                ('self_hp', models.BooleanField(default=False, help_text="Amount of this effect is based on casting monster's HP")),
                ('target_hp', models.BooleanField(default=False, help_text="Amount of this effect is based on target monster's HP")),
                ('damage', models.BooleanField(default=False, help_text='Amount of this effect is based on damage dealt')),
                ('note', models.TextField(blank=True, help_text="Explain anything else that doesn't fit in other fields", null=True)),
                ('effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.SkillEffect')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Skill')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='effect',
            field=models.ManyToManyField(blank=True, help_text='Detailed skill effect information', related_name='effect', through='bestiary.SkillEffectDetail', to='bestiary.SkillEffect'),
        ),
        migrations.AddField(
            model_name='skill',
            name='other_skill',
            field=models.ForeignKey(blank=True, help_text='Twin Angel mechanic', null=True, on_delete=django.db.models.deletion.SET_NULL, to='bestiary.Skill'),
        ),
        migrations.AddField(
            model_name='skill',
            name='scaling_stats',
            field=models.ManyToManyField(blank=True, help_text='Monster stats which this skill scales on', to='bestiary.ScalingStat'),
        ),
        migrations.CreateModel(
            name='MonsterCraftCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.GameItem')),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Monster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='monster',
            name='craft_materials',
            field=models.ManyToManyField(related_name='_monster_craft_materials_+', through='bestiary.MonsterCraftCost', to='bestiary.GameItem'),
        ),
        migrations.AddField(
            model_name='monster',
            name='leader_skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bestiary.LeaderSkill'),
        ),
        migrations.AddField(
            model_name='monster',
            name='skills',
            field=models.ManyToManyField(blank=True, to='bestiary.Skill'),
        ),
        migrations.AddField(
            model_name='monster',
            name='source',
            field=models.ManyToManyField(blank=True, help_text='Where this monster can be acquired from', to='bestiary.Source'),
        ),
        migrations.AddField(
            model_name='monster',
            name='transforms_to',
            field=models.ForeignKey(blank=True, help_text='Monster which this monster can transform into during battle', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transforms_from', to='bestiary.Monster'),
        ),
        migrations.CreateModel(
            name='HomunculusSkillCraftCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.GameItem')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.HomunculusSkill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='homunculusskill',
            name='craft_materials',
            field=models.ManyToManyField(help_text='Crafting materials required to purchase', through='bestiary.HomunculusSkillCraftCost', to='bestiary.GameItem'),
        ),
        migrations.AddField(
            model_name='homunculusskill',
            name='monsters',
            field=models.ManyToManyField(to='bestiary.Monster'),
        ),
        migrations.AddField(
            model_name='homunculusskill',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, help_text='Skills which must be acquired first', related_name='homunculus_prereq', to='bestiary.Skill'),
        ),
        migrations.AddField(
            model_name='homunculusskill',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Skill'),
        ),
        migrations.CreateModel(
            name='Fusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('meta_order', models.IntegerField(db_index=True, default=0)),
                ('ingredients', models.ManyToManyField(related_name='fusion_ingredient_for', to='bestiary.Monster')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fusion', to='bestiary.Monster')),
            ],
            options={
                'ordering': ['meta_order'],
            },
        ),
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('com2us_id', models.IntegerField(db_index=True)),
                ('boss', models.BooleanField(default=False)),
                ('stars', models.IntegerField(choices=[(1, '1⭐'), (2, '2⭐'), (3, '3⭐'), (4, '4⭐'), (5, '5⭐'), (6, '6⭐')])),
                ('level', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('resist', models.IntegerField()),
                ('accuracy_bonus', models.IntegerField()),
                ('crit_bonus', models.IntegerField()),
                ('crit_damage_reduction', models.IntegerField()),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Monster')),
                ('wave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Wave')),
            ],
            options={
                'verbose_name_plural': 'Enemies',
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model, bestiary.models.base.Stars),
        ),
        migrations.AddField(
            model_name='awakencost',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.GameItem'),
        ),
        migrations.AddField(
            model_name='awakencost',
            name='monster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Monster'),
        ),
        migrations.CreateModel(
            name='SecretDungeon',
            fields=[
                ('dungeon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bestiary.Dungeon')),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Monster')),
            ],
            bases=('bestiary.dungeon',),
        ),
    ]
