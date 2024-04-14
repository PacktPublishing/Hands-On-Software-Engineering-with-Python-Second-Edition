def space_indented_function_1():
    ...  # This is indented with four spaces

def space_indented_function_2():
      ...  # This is indented with six spaces

def tab_indented_function():
	...  # This is indented with a single tab

def mixed_indented_function():
	...  # This is indented with a single tab
    ...  # This is indented with four spaces

# File ".../indentation_consistency_example.py", line 12
#     ...  # This is indented with four spaces
#                                             ^
# IndentationError: unindent does not match any outer
# indentation level
