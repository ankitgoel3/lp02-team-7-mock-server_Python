# Include this in your model classes
# It easily converts any of the SqlAlchemy models to a JSON object
class ToJson:
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
