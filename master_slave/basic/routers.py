import logging

logger = logging.getLogger(__name__)

class AuthRouter:
    route_app_labels = {"admin", "auth", "contenttypes", "sessions"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "default"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "default"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return False 

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "default"
        return False  


class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        print("read from slave db")
        return "slave"

    def db_for_write(self, model, **hints):
        print("written into master")
        return "master"

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {"master", "slave"}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'master':
            return True 
        return False  
