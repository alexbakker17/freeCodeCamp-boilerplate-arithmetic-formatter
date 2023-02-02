def arithmetic_arranger(problems, result=False):
  """
    From a list of strings it creates arranged arithmetic problems.
    If result = True, the answers are also displayed.
    
    Input: a list of arithmetic problems as strings
    Output: returns the arranged arithmetic problems 
    
    Possible Errors:
    - *Error: Too many problems.* : 
      No more than 5 problems can be inputted into the function.
    - *Error: Operator must be '+' or '-'.* : 
      The function only accepts addition (+) and subtraction (-) operators. 
    - *Error: Numbers must only contain digits.* : 
      Each number can only contain digits.
    - *Error: Numbers cannot be more than four digits.* : 
      Each number can only have a maximum width of 4 digits.
    """

  # assign local variables
  max_problems = 5
  op_space = 2
  op_len = 1
  max_digits = 4
  dash = '-'
  space = ' '
  large_space = ' ' * 4

  # assign local collections
  arranged_problems = []
  row1 = []
  row2 = []
  lines = []
  results = []
  ops = ['+', '-']

  # Error 1
  if len(problems) > max_problems:
    return "Error: Too many problems."

  # loop through problems list
  for problem in problems:
    parts = problem.split()
    max_len = len(max(parts, key=len))

    # Error 2
    if parts[1] not in ops:
      return "Error: Operator must be '+' or '-'."

    # Error 3
    if not all([item.isnumeric() for item in parts[::2]]):
      return "Error: Numbers must only contain digits."

    # Error 4
    if max_len > max_digits:
      return "Error: Numbers cannot be more than four digits."

    # get row1, row2 and lines
    line_len = op_space + max_len
    line = dash * line_len
    first_num = parts[0].rjust(line_len)
    spaces = space * (line_len - len(parts[2]) - op_len)
    second_num = parts[1] + spaces + parts[2]
    row1.append(first_num)
    row2.append(second_num)
    lines.append(line)

    # get results row
    single_result = ''
    if result == True:
      if parts[1] == ops[0]:
        single_result = int(parts[0]) + int(parts[2])
      else:
        single_result = int(parts[0]) - int(parts[2])
    results.append(str(single_result).rjust(line_len))

  # join row1 and row2
  arranged_problems = ''
  for i in (row1, row2):
    row = large_space.join(i)
    arranged_problems += row + '\n'

  # join the lines and results row
  if result == True:
    lines_row = large_space.join(lines)
    arranged_problems += lines_row + '\n'
    results_row = large_space.join(results)
    arranged_problems += results_row
  else:
    lines_row = large_space.join(lines)
    arranged_problems += lines_row

  return arranged_problems
