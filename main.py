# Resolucion ejercicio opcional modulo 2
# Contrario a review que era paralelo. Se hace secuencial esto
# Mezcla tambien abatch
import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Sos un profesor de fisica teorica - Maximo 150 palabras"
    ),
    (
        "human",
        "{pregunta}"
    )
])


model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=1
    )

# Esto asegura que la devolucion sea un string de python
parser = StrOutputParser()

chain = prompt | model | parser

async def main():
    resultado = await chain.ainvoke({"pregunta": "Que es la entropia?"})
    print(resultado)

if __name__ == "__main__":
    asyncio.run(main())
