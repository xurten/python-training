# Tip 87 define a master exception to isolate the calling component from the api
# Benefits of isolation:
# 1) the main exception gives the information of exception in concrete API
# 2) helps with finding of errors in the API module
# 3) need of extending it
import logging

from src.library.error_handling import mymodule


def example():
    try:
        weight = mymodule.determine_weight(0, 1)
    except mymodule.InvalidDensityError:
        weight = 0
    except mymodule.Error:
        logging.exception('there is error in code that is executing')
    except Exception:
        logging.exception('error in API')
        raise


example()
