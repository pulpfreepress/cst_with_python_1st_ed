"""Defines the MySQLPersistenceWrapper class."""

from employee_training.application_base import ApplicationBase
from mysql import connector
from mysql.connector.pooling import (MySQLConnectionPool)
import mysql.connector

class MySQLPersistenceWrapper(ApplicationBase):
	"""Implements the MySQLPersistenceWrapper class."""

	def __init__(self, config:dict)->None:
		"""Initializes object. """
		self._config_dict = config
		self.META = dict(config["meta"])
		self.DATABASE = dict(config["database"])
		super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
		
		# Database Configuration Constants
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = self.DATABASE["connection"]["config"]["database"]
		self.DB_CONFIG['user'] = self.DATABASE["connection"]["config"]["user"]
		self.DB_CONFIG['host'] = self.DATABASE["connection"]["config"]["host"]
		self.DB_CONFIG['port'] = self.DATABASE["connection"]["config"]["port"]

		self._logger.log_debug(f'DB Connection Config Dict: {self.DB_CONFIG}')

		# Database Connection
		self._connection_pool = self._initialize_database_connection_pool(self.DB_CONFIG)

		# SQL Query Consants
		self.SELECT_ALL_EMPLOYEES = f"SELECT id, first_name, middle_name, last_name, birthday, gender " \
									f"FROM employees"
		


	def select_all_employees(self)->list:
		"""Returns a list of all employee rows."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_EMPLOYEES)
					results = cursor.fetchall()

			return results

		except Exception as e:
			self._logger.log_error(f'Problem with select_all_employees(): {e}')


	##### Private Utility Methods #####

	def _initialize_database_connection_pool(self, config):
		"""Initializes database connection pool."""
		try:
			self._logger.log_debug(f'Creating connection pool...')
			cnx_pool = MySQLConnectionPool(pool_name = self.DATABASE["pool"]["name"],
											pool_size=self.DATABASE["pool"]["size"],
											pool_reset_session=self.DATABASE["pool"]["reset_session"],
											**config)
			self._logger.log_debug(f'Connection pool successfully created!')
			return cnx_pool
		except connector.Error as err:
			self._logger.log_error(f'Problem creating connection pool: {err}')
		except Exception as e:
			self._logger.log_error(f'Problem creating connection pool: {e}')

