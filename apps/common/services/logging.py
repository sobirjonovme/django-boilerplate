import traceback

from apps.common.services.telegram import TelegramService


class LoggingException(Exception):
    def __init__(self, message, extra_kwargs: dict = None):
        self.message = message
        self.extra_kwargs = extra_kwargs
        super().__init__(self.message)


class TelegramLogging:
    def __init__(self, exception):
        self.bot_token = "-"
        self.chat_id = "-"
        self.exception = exception

        self.telegram_service = TelegramService(bot_token=self.bot_token)

    def send_log_to_admin(self):
        # Send the exception details to the admin
        extra = getattr(self.exception, "extra_kwargs", None)

        try:
            tb_list = traceback.format_exception(None, self.exception, self.exception.__traceback__)
            tb_string = "".join(tb_list)
            msg = "<b>ERROR | Kindergarten MS</b>\n\n"
            if extra:
                for key, value in extra.items():
                    msg += f"{key}: {value}\n"
            msg += f"\n<code>{tb_string[-4000 + len(msg):]}</code>"
            self.telegram_service.send_message(self.chat_id, msg)
        except Exception as e:
            print(e)
