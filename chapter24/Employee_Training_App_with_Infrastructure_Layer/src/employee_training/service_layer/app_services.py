"""Implements the application service layer."""

from employee_training.application_base import ApplicationBase
from employee_training.persistence_layer.mysql_persistence_wrapper \
    import MySQLPersistenceWrapper
from employee_training.infrastructure_layer.employee \
    import Employee
import inspect
from typing import List

class AppServices(ApplicationBase):
    """AppServices Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = MySQLPersistenceWrapper(config)
        


    def get_all_employees(self)->List[Employee]:
        """Returns a list of employee objects."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        employee_dict = {}
        employee_dict['employees'] = []

        try:
            results = self.DB.select_all_employees()
            return results
            
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:{e}')
