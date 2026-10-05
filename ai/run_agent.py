from crewai import Agent, Crew, Task

from ai.llm_factory import get_llm
from ai.tools.math_condition import math_condition

agent = Agent(
    role="Помощник по проверке математических условий",
    goal="Проверять числа с помощью math_condition и объяснять результат.",
    backstory=(
        "Ты проверяешь математические условия. "
        "Для каждой проверки вызывай math_condition "
        "и формулируй ответ на основе результата инструмента."
    ),
    tools=[math_condition],
    llm=get_llm(),
    verbose=True,
    max_iter=5,
)

task = Task(
    description=(
       "Вызови math_condition с value=3.5 и condition='even'. "
    "Не округляй и не изменяй число. "
    "Объясни пользователю результат инструмента."
    ),
    expected_output="Краткий ответ по-русски на основе результата инструмента.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task], verbose=True)

if __name__ == "__main__":
    print(crew.kickoff())