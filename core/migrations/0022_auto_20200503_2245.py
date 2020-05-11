# Generated by Django 2.2.11 on 2020-05-03 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200503_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_breed',
            field=models.CharField(choices=[('Abyssinian', 'Abyssinian'), ('Aegean', 'Aegean'), ('American Bobtail', 'American Bobtail'), ('American Curl', 'American Curl'), ('American Shorthair', 'American Shorthair'), ('American Wirehair', 'American Wirehair'), ('Aphrodite Giant', 'Aphrodite Giant'), ('Arabian Mau', 'Arabian Mau'), ('Asian cat', 'Asian cat'), ('Asian Semi-longhair', 'Asian Semi-longhair'), ('Australian Mist', 'Australian Mist'), ('Balinese', 'Balinese'), ('Bambino', 'Bambino'), ('Bengal', 'Bengal'), ('Birman', 'Birman'), ('Bombay', 'Bombay'), ('Brazilian Shorthair', 'Brazilian Shorthair'), ('British Longhair', 'British Longhair'), ('British Shorthair', 'British Shorthair'), ('Burmese', 'Burmese'), ('Burmilla', 'Burmilla'), ('California Spangled', 'California Spangled'), ('Chantilly-Tiffany', 'Chantilly-Tiffany'), ('Chartreux', 'Chartreux'), ('Chausie', 'Chausie'), ('Colourpoint Shorthair', 'Colourpoint Shorthair'), ('Cornish Rex', 'Cornish Rex'), ('Cymric Manx', 'Cymric Manx'), ('Cyprus', 'Cyprus'), ('Devon Rex', 'Devon Rex'), ('Donskoy or', 'Donskoy or'), ('Don Sphynx', 'Don Sphynx'), ('Dragon Li', 'Dragon Li'), ('Chinese Li Hua', 'Chinese Li Hua'), ('Dwelf', 'Dwelf'), ('Egyptian Mau', 'Egyptian Mau'), ('European Shorthair', 'European Shorthair'), ('Exotic Shorthair', 'Exotic Shorthair'), ('Foldex', 'Foldex'), ('German Rex', 'German Rex'), ('Havana Brown', 'Havana Brown'), ('Highlander', 'Highlander'), ('Himalayan', 'Himalayan'), ('Colorpoint Persian[d]', 'Colorpoint Persian[d]'), ('Japanese Bobtail', 'Japanese Bobtail'), ('Javanese or Colorpoint Longhair', 'Javanese or Colorpoint Longhair'), ('Khao Manee', 'Khao Manee'), ('Korat', 'Korat'), ('Korean Bobtail', 'Korean Bobtail'), ('Korn Ja', 'Korn Ja'), ('Kurilian Bobtail', 'Kurilian Bobtail'), ('Kuril Islands Bobtail', 'Kuril Islands Bobtail'), ('LaPerm', 'LaPerm'), ('Lykoi', 'Lykoi'), ('Maine Coon', 'Maine Coon'), ('Manx', 'Manx'), ('Mekong Bobtail', 'Mekong Bobtail'), ('Minskin', 'Minskin'), ('Munchkin', 'Munchkin'), ('Napoleon', 'Napoleon'), ('Nebelung', 'Nebelung'), ('Norwegian Forest Cat', 'Norwegian Forest Cat'), ('Ocicat', 'Ocicat'), ('Ojos Azules', 'Ojos Azules'), ('Oregon Rex', 'Oregon Rex'), ('Oriental Bicolor', 'Oriental Bicolor'), ('Oriental Longhair', 'Oriental Longhair'), ('Foreign Longhair', 'Foreign Longhair'), ('Mandarin', 'Mandarin'), ('British Angora', 'British Angora'), ('Oriental Shorthair', 'Oriental Shorthair'), ('Persian', 'Persian'), ('Peterbald', 'Peterbald'), ('Pixie-bob', 'Pixie-bob'), ('Raas', 'Raas'), ('Ragamuffin', 'Ragamuffin'), ('Liebling', 'Liebling'), ('Ragdoll', 'Ragdoll'), ('Russian Blue', 'Russian Blue'), ('Russian White/Black/Tabby', 'Russian White/Black/Tabby'), ('Sam sawet', 'Sam sawet'), ('Savannah', 'Savannah'), ('Scottish Fold', 'Scottish Fold'), ('Selkirk Rex', 'Selkirk Rex'), ('Serengeti', 'Serengeti'), ('Serrade Petit', 'Serrade Petit'), ('Siamese', 'Siamese'), ('Siberian', 'Siberian'), ('Siberian Forest Cat', 'Siberian Forest Cat'), ('Neva Masquerade', 'Neva Masquerade'), ('Singapura', 'Singapura'), ('Snowshoe', 'Snowshoe'), ('Sokoke', 'Sokoke'), ('Somali', 'Somali'), ('Sphynx', 'Sphynx'), ('Suphalak', 'Suphalak'), ('Thai Lilac', 'Thai Lilac'), ('Thai', 'Thai'), ('Traditional or Classic or Old-style Siamese', 'Traditional or Classic or Old-style Siamese'), ('Wichien Maat', 'Wichien Maat'), ('Tonkinese', 'Tonkinese'), ('Toyger', 'Toyger'), ('Turkish Angora', 'Turkish Angora'), ('Turkish Van', 'Turkish Van'), ('Ukrainian Levkoy', 'Ukrainian Levkoy'), ('Wila Krungthep', 'Wila Krungthep'), ('York Chocolate', 'York Chocolate')], max_length=64),
        ),
    ]