import logging
class Logclass:
    def get_the_logs(self):
        # logs_directory = "Logs"
        # os.makedirs(logs_directory, exist_ok=True)
        logger = logging.getLogger()
        file_handler = logging.FileHandler("D:\\Users\\eventzworld_page_object_model\\eventzworld\\Logs\\logsfile.log",mode="w")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s:%(module)s:%(funcName)s: %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
