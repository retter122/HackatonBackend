from sqlalchemy import select, Select

class CRUD:
    @classmethod
    def get_by_id(cls, id):
        query = (select(cls).where(cls.id == id))
        return query