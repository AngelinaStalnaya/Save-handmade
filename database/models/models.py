import peewee

handmade_database = peewee.SqliteDatabase('save-handmade.db', autoconnect=True)


def make_table_name(class_name):
    model_name = class_name.__name__
    return model_name.lower() + 'tbl'


class BaseModel(peewee.Model):
    class Meta:
        database = handmade_database
        legacy_table_names = False
        table_function = make_table_name
        
class Auth(BaseModel):
    id = peewee.AutoField()
    user_id = peewee.IntegerField()
    token = peewee.TextField()
    token_lifetime = peewee.TextField()
      
class Users(BaseModel):
    id = peewee.AutoField()
    user_name = peewee.TextField()
    login = peewee.TextField()
    password = peewee.TextField()
    
class Sections(BaseModel):
    id = peewee.AutoField()
    section_name = peewee.TextField()
    user_id = peewee.IntegerField()
    
class Subsections(BaseModel):
    id = peewee.AutoField()
    section_id = peewee.IntegerField()
    subsection_name = peewee.TextField()
    user_id = peewee.IntegerField()      
    
class PatternPage(BaseModel):
    id = peewee.AutoField()
    section_id= peewee.IntegerField()
    subsection_id = peewee.IntegerField(None)
    pattern_name = peewee.TextField()
    comments = peewee.TextField()
    files_ids = peewee.TextField()
    description = peewee.TextField()