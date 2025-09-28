"""Provides Logger class for logging services."""

import logging
import logging.handlers
from employee_training.settings import Settings
import os

class LoggingService():
    """Provides logging services."""

    _logger = None

    def __init__(self, class_name:str, logfile_prefix_name:str=None)->None:
        """Initialize instance."""
        if not LoggingService._logger:
            LoggingService._logger = logging.getLogger(class_name)
            LoggingService._logger.propagate = False
            self._settings_dict = Settings().read_settings_file_from_location()
            self._logfile_prefix_name = logfile_prefix_name
            self.log_level = logging.ERROR
        
        if self._settings_dict['log_level'] == 'notset':
            LoggingService._logger.setLevel(logging.NOTSET)
            self.log_level = logging.NOTSET
        elif self._settings_dict['log_level'] == 'debug':
            LoggingService._logger.setLevel(logging.DEBUG)
            self.log_level = logging.debug
        elif self._settings_dict['log_level'] == 'info':
            LoggingService._logger.setLevel(logging.INFO)
            self.log_level = logging.INFO
        elif self._settings_dict['log_level'] == 'warning':
            LoggingService._logger.setLevel(logging.WARNING)
            self.log_level = logging.WARNING
        elif self._settings_dict['log_level'] == 'error':
            LoggingService._logger.setLevel(logging.ERROR)
            self.log_level = logging.ERROR
        elif self._settings_dict['log_level'] == 'critical':
            LoggingService._logger.setLevel(logging.CRITICAL)
            self.log_level = logging.CRITICAL
        else:
            LoggingService._logger.setLevel(logging.ERROR)
            self.log_level = logging.ERROR

        self._formatter = logging.Formatter('%(levelname)s:%(name)s:%(asctime)s:%(message)s')

        if not LoggingService._logger.handlers:
            if self._settings_dict['log_to_console']:
                self._ch = logging.StreamHandler()
                self._ch.setLevel(logging.DEBUG)
                self._ch.setFormatter(self._formatter)
                LoggingService._logger.addHandler(self._ch)

            if self._settings_dict['log_to_file']:
                log_file = os.path.join(self._settings_dict['logs_dir'], 
                            f"{self._logfile_prefix_name}_{self._settings_dict['log_filename']}")
                self._fh = logging.handlers.TimedRotatingFileHandler(log_file, 
                            when='midnight', backupCount=20)
                self._fh.setLevel(logging.DEBUG)
                self._fh.setFormatter(self._formatter)
                LoggingService._logger.addHandler(self._fh)
        

    
    def log_debug(self, message):
        """Log to debug."""
        LoggingService._logger.debug(message)

    def log_error(self, message):
        """Log to error."""
        LoggingService._logger.error(message)

    def log_info(self, message):
        """Log to info."""
        LoggingService._logger.info(message)

    def log_warning(self, message):
        """Log to warning."""
        LoggingService._logger.warning(message)

    def log_critical(self, message):
        """Log to critical."""
        LoggingService._logger.critical(message)

