class ZamResourceIdentifierUnaryOp(object):
    @staticmethod
    def run(resource_id):
        pass


class ZamResourceIdentifierBinaryOp(object):
    @staticmethod
    def run(left_resource_id, right_resource_id):
        pass


class ZamResourceIdentifierTernaryOp(object):
    @staticmethod
    def run(condition_resource_id, true_condition, false_condition):
        if condition_resource_id:
            return true_condition
        else:
            return false_condition
