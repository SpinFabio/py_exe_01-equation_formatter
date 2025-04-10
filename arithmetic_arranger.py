import re
from operation_class import Operation

MY_PATTERN = r'(\d+) (\+|-) (\d*)'

    

def add_white_spaces(s:str, max_len:int,op=None):
  WSPACES=" "
  if op:
    needed_wspaces= max_len-len(s)
    return op +WSPACES+ " "*needed_wspaces+s
  else:
    needed_wspaces= max_len-len(s)+1
    return WSPACES+" "*needed_wspaces+s
      

def make_outputs(list_of_outputs,op_obj:Operation):
  space_between= "    "
  if list_of_outputs[0]=="":
    space_between=""
  list_of_outputs[0]+=space_between+op_obj.n1
  list_of_outputs[1]+=space_between+op_obj.n2
  list_of_outputs[2]+=space_between+op_obj.dashed_line
  list_of_outputs[3]+=space_between+op_obj.res

def arithmetic_arranger(problems):
  if len(problems) > 5:
    raise Exception("Too many problems")


  problem_list=[]

  list_of_outputs=["","","",""]
    
  for problem in problems:
    matches=re.findall(MY_PATTERN, problem)
    for (n1,op,n2) in matches:
      #print(n1,op,n2)
      if len(n1)>4 or len(n2)>4:
        raise Exception("Error: Numbers cannot be more than four digits.")
      if op not in ["+","-"]:
        raise Exception("Error: Operator must be '+' or '-'.")
      op_obj=Operation(n1,op,n2)
      problem_list.append(op_obj)
      make_outputs(list_of_outputs,op_obj)

  for output in list_of_outputs:
    print(output)
      
      
  
    
      
      
  return None