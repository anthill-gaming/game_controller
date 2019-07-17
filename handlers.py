from anthill.framework.handlers.streaming.uploadfile import UploadFileStreamHandler
from anthill.platform.handlers import UserHandlerMixin


# noinspection PyAbstractClass
class DeployHandler(UploadFileStreamHandler, UserHandlerMixin):
    pass
