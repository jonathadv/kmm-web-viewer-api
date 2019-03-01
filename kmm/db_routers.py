class KmmDBRouter(object):
    app_name = "kmm"
    db_name = "kmm_db"

    """
    A router to control Kmm db operations
    """

    def db_for_read(self, model, **kwargs):
        if model._meta.app_label == self.app_name:
            return self.db_name
        return None

    def db_for_write(self, model, **kwargs):
        if model._meta.app_label == self.app_name:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **kwargs):
        if (
            obj1._meta.app_label == self.app_name
            or obj2._meta.app_label == self.app_name
        ):
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == self.db_name:

            return model._meta.app_label == self.app_name
        elif model._meta.app_label == self.app_name:
            return False
        return None


class DjangoDBRouter(object):
    app_names = ["admin", "auth", "contenttypes", "sessions"]
    db_name = "django_db"

    """
    A router to control Kmm db operations
    """

    def db_for_read(self, model, **kwargs):
        if model._meta.app_label in self.app_names:
            return self.db_name
        return None

    def db_for_write(self, model, **kwargs):
        if model._meta.app_label in self.app_names:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **kwargs):
        if (
            obj1._meta.app_label in self.app_names
            or obj2._meta.app_label in self.app_names
        ):
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == self.db_name:
            return model._meta.app_label in self.app_names
        elif model._meta.app_label in self.app_names:
            return False
        return None
