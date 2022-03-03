

from resource_identifier.solver import (ZamResouceIdentifierBaseSolverMixin,
                                        ZamResouceIdentifierRestApiSolverMixin,
                                        ZamResourceIdentifierDataBaseSolverMixin, 
                                        ZamResourceIdentifierFilePathSolverMixin)


class ZamResourceIdentifierAbstractBase(str):
    _cursors = set()

    def _validate_resource_syntax(self) -> bool:
        raise NotImplementedError


class ZamResourceIdentifierBase(ZamResourceIdentifierAbstractBase):
    def __new__(cls, *args, **kwargs):
        if args:
            if isinstance(args[0], ZamResourceIdentifierBase):
                return args[0]
            else:
                return super(ZamResourceIdentifierBase, cls).__new__(cls, *args, **kwargs)

    def _validate_resource_syntax(self) -> bool:
        return super()._validate_resource_syntax()

    @property
    def cursors(self):
        return self._cursors

    def clear_all_cursors(self):
        for cursor in self._cursors:
            cursor.close()
        self._cursors.clear()


class ZamResourceIdenrtifier(ZamResourceIdentifierBase,
                             ZamResouceIdentifierBaseSolverMixin,
                             ZamResourceIdentifierDataBaseSolverMixin,
                             ZamResourceIdentifierFilePathSolverMixin,
                             ZamResouceIdentifierRestApiSolverMixin):

    pass
