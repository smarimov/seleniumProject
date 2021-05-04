import logging

logging.basicConfig(filename="C:\\Users\\shoki\\OneDrive\\Desktop\\selenium_logs\\test.log",
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is info message")

logging.warning("This is a warning message")
logging.error("This is error message")
logging.critical("This is a critical message")
