import inspect
import logging

import pytest

from hubspot.testdata.Testdata import Testdata


@pytest.mark.usefixtures("setup")
class Basetest:

    def logModule(self):
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        filehandler = logging.FileHandler('files.log')
        formatter = logging.Formatter('%(asctime)s : %(name)s: %(levelname)s: %(message)s')
        logger.addHandler(filehandler)

        logger.setLevel('DEBUG')

        return logger







