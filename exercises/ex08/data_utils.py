"""Dictionary related utility functions."""

__author__ = "730549088"

# Define your functions below

from csv import DictReader
from unittest import result

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")  # "r" means read
  
    # Prepare to read the data dile as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()
    
    return result


def column_values(table:list[dict[str,str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(not_mutated_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Makes headers for the table."""
    result: dict[str, list[str]] = {}
    for column_names in not_mutated_table:
        table_values: list[str] = []
        count: int = 0 
        while count < rows and count < len(not_mutated_table[column_names]): 
            table_values.append(not_mutated_table[column_names][count])
            count += 1 
        result[column_names] = table_values 
    return result 


def select(not_mutated_table: dict[str, list[str]], given_column_names: list[str]) -> dict[str, list[str]]: 
    """Creates a subset of the table for specific columns."""
    result: dict[str, list[str]] = {}
    for column in given_column_names: 
        for table_values in not_mutated_table[column]:
            table_values: list[str] = []
            result[column] = not_mutated_table[column]
    return result 


def concat(not_mutated_table_1: dict[str, list[str]], not_mutated_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables together without any repitition."""
    result: dict[str, list[str]] = {}
    for column in not_mutated_table_1: 
        new_table_values: list[str] = []
        new_table_values = result[column] = not_mutated_table_1[column]
    for column in not_mutated_table_2:
        if column in not_mutated_table_1:
            result[column] += not_mutated_table_2[column]
        else:
            new_table_values: list[str] = []
            new_table_values = result[column] = not_mutated_table_2[column]
    return result



def count(given_list: list[str]) -> dict[str, int]:
    """Creates a dict where each key is a unique value and the value is the frequency of the key."""
    result: dict[str, list[str]] = {}
    count: int = 0 
    for count in given_list: 
        if count in result: 
            result[count] += 1 
        else: 
            frequencies: list[str] = []
            frequencies = result[count] = 1 
    return result 