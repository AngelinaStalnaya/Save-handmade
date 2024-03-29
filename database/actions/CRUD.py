from database.models.models import *


def _create_data(model, data, db=handmade_database) -> None:
    db.connect(reuse_if_open=True)
    if model == Auth:
        model.create(user_id=data[0], token=data[1], token_lifetime=data[3])
    elif model == Users:
        model.create(user_name=data[0], login=data[1], password=data[2])
    elif model == Sections:
        model.create(section_name=data[0], user_id=data[1])
    elif model == Subsections:
        model.create(section_id=data[0],
                     subsection_name=data[1], user_id=data[2])
    elif model == PatternPage:
        model.create(section_id=data[0], subsection_id=data[1], pattern_name=data[2],
                     comments=data[3], files_ids=data[4], description=data[5])
    db.close()


def _retrieve_all_data(model, db=handmade_database) -> peewee.ModelSelect | bool:
    with db.atomic():
        db.connect(reuse_if_open=True)
        response = model.select().order_by(model.id.desc()).limit(1)
        if response:
            return response
        else:
            return False


def _retrieve_user_in_database(user_id: int, model=Users, db=handmade_database) -> peewee.ModelSelect | bool:
    db.connect(reuse_if_open=True)
    response = model.select().where(model.id == user_id)
    if response:
        return response
    else:
        return False


def _retrieve_pattern(id: int, model=PatternPage, db=handmade_database) -> peewee.ModelSelect | bool:
    db.connect(reuse_if_open=True)
    response = model.select(model.section_id, model.subsection_id, model.pattern_name, model.comments,
                            model.files_ids, model.description).where(model.id == id).limit(1)
    if response:
        return response
    else:
        return False


def _update(model, id: int, section_name: str = None, user_name: str = None,
            password: str = None, subsection_name: str = None,
            pattern_name: str = None, comments: str = None,
            files_ids: str = None, description: str = None,
            db=handmade_database) -> None:
    db.connect(reuse_if_open=True)
    if model == Users and user_name is not None:
        model.update({model.user_name: user_name}).where(
            model.id == id).execute()
    elif model == Users and password is not None:
        model.update({model.password: password}).where(
            model.id == id).execute()
    elif model == Sections:
        model.update({model.section_name: section_name}
                     ).where(model.id == id).execute()
    elif model == Subsections:
        model.update({model.subsection_name: subsection_name}
                     ).where(model.id == id).execute()
    elif model == PatternPage and pattern_name is not None:
        model.update({model.pattern_name: pattern_name}
                     ).where(model.id == id).execute()
    elif model == PatternPage and comments is not None:
        model.update({model.comments: comments}).where(
            model.id == id).execute()
    elif model == PatternPage and files_ids is not None:
        model.update({model.files_ids: files_ids}).where(
            model.id == id).execute()
    elif model == PatternPage and description is not None:
        model.update({model.description: description}
                     ).where(model.id == id).execute()
    db.close()


class CRUDInterface:
    @staticmethod
    def create(model, data):
        return _create_data(model=model, data=data)

    @staticmethod
    def retrieve_all(model):
        return _retrieve_all_data(model=model)

    @staticmethod
    def retrieve_user(user_id):
        return _retrieve_user_in_database(user_id=user_id)

    @staticmethod
    def retrieve_pattern(id):
        return _retrieve_pattern(id=id)

    @staticmethod
    def upate(model, id, section_name=None, user_name=None, password=None,
              subsection_name=None, pattern_name=None, comments=None,
              files_ids=None, description=None):
        return _update(model=model, id=id, section_name=section_name,
                       user_name=user_name, password=password,
                       subsection_name=subsection_name, pattern_name=pattern_name,
                       comments=comments, files_ids=files_ids, description=description)

if __name__ == '_main__':
    CRUDInterface()