class InstantiateCSVError(Exception):

    def __init__(self, message="Файл item.csv поврежден", *args):
        super().__init__(message, *args)