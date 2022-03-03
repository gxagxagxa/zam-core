from contextlib import contextmanager
from resource_identifier.unique_identifier import ZamResourceIdenrtifier


@contextmanager
def create_cursor(resource_id, factory_class=None):
    if not factory_class:
        factory_class = ZamResourceIdentifierCursor
    cursor = factory_class()
    
    try:
        cursor.open(resource_id)
        yield cursor
    finally:
        cursor.close()


class ZamResourceIdentifierCursor(object):
    _resource = None
    _factor_class = ZamResourceIdenrtifier

    def __init__(self) -> None:
        pass

    @property
    def resource(self):
        return self._resource

    @resource.setter
    def resource(self, resource_id):
        if resource_id:
            self._resource = __class__._factor_class(resource_id)
            self._resource.cursors.add(self)

    def open(self, resource_id):
        self.resource = resource_id

    def close(self):
        if self._resource:
            try:
                self._resource.cursors.remove(self)
            finally:
                self._resource = None

    def exists(self) -> bool:
        return True
