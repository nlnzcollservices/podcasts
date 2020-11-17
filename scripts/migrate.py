from playhouse.migrate import *

from settings import database_fullname

my_db = SqliteDatabase(database_fullname)
migrator = SqliteMigrator(my_db)

def add_column(table_name, field_name, field_content)):
	"""Adds new column to existing table
	Parameters:
		table_name(str) - name of the table with lower letter.
		field_name(str) - name of the new field to add_column.
		field_content(obj db field) - settings for field
	Returns:
		None
	"""
	
	migrate(
	migrator.add_column(table_name, field_name, sip)
	)

def drop_column(table_name, field_name):
	"""Deletes existing column from table
	Parameters:
		table_name(str) - name of the table with lower letter.
		field_name(str) - name of the new field to add_column.
	Returns:
		None
	"""
   migrate(
        migrator.drop_column(table_name, field_name),
    )

 def main():

 	"""This is support tool for modifying database structure"""

 	table_name = "episode"
 	field_name = "sip"
 	field_content = BooleanField(default=False)
 	#field_name2= "seas_n"
	#drop_column(table_name, field_name2)
	add_column(table_name, field_name, field_content)

if __name__ == '__main__':
	main()