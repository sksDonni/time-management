from abc import ABC


class AbcFacade(ABC):
    """Any `~interface_abc` will expect to be able to invoke the following methods.
    """

    def count_rows(self):
        pass

    def get_rows(self):
        pass

    def delete_history(self):
        pass

    def disconnect(self):
        pass
