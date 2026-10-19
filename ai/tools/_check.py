from ai.tools.math_condition import math_condition

print("name:", math_condition.name)
print("ok  :", math_condition.run(value=4, condition="even"))
print("err :", math_condition.run(value=4, condition="super-positive"))