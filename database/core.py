from database.actions.CRUD import CRUDInterface
from database.actions.CRUD import handmade_database
from database.models.models import Auth, Users, Sections, Subsections, PatternPage

handmade_database.connect()
handmade_database.create_tables([Auth, Users, Sections, Subsections, PatternPage])

crud = CRUDInterface()