from peewee import CharField, IntegerField, SqliteDatabase, Model, DateField, SmallIntegerField

db = SqliteDatabase('database.db')


class Card(Model):
    number = IntegerField(verbose_name='Номер карты')
    person = CharField(max_length=127, verbose_name='Имя пользователя')
    end_data = DateField(verbose_name='Дата окончания карты', help_text='yyyy-MM-dd')
    cvv = SmallIntegerField(verbose_name='CVV код')

    class Meta:
        database = db


db.connect()
db.create_tables([Card])
