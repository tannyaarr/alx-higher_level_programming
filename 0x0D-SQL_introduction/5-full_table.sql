-- Prints the full description of the table first_table from the database hbtn_0c_0


SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = hbtn_0c_0 and first_table = 'first_table'
