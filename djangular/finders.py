from . import storage
from django.contrib.staticfiles import finders


class NamespacedAngularAppDirectoriesFinder(finders.AppDirectoriesFinder):
    storage_class = storage.NamespacedAngularAppStorage

    def find_in_app(self, app, path):
        """
        Find a requested static file in an app's static locations.
        """
        path = path.replace("\\", "/").replace("//", "/").replace("\\", "/").replace("//", "/")
        storage = self.storages.get(app, None)
        if storage:
            if storage.prefix:
                prefix = '%s%s' % (storage.prefix, "/")
                if not path.startswith(prefix):
                    return None
                path = path[len(prefix):]
                # only try to find a file if the source dir actually exists
            if storage.exists(path):
                matched_path = storage.path(path)
                if matched_path:
                    return matched_path


class NamespacedE2ETestAppDirectoriesFinder(finders.AppDirectoriesFinder):
    """
    A static files finder that looks in the tests/e2e directory of each app.
    """
    storage_class = storage.NamespacedE2ETestAppStorage


class NamespacedLibTestAppDirectoriesFinder(finders.AppDirectoriesFinder):
    """
    A static files finder that looks in the tests/lib directory of each app.
    """
    storage_class = storage.NamespacedLibTestAppStorage