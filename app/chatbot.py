from app.nlp import gerar_sql
from app.banco import executar_consulta


def responder_pergunta(pergunta):
    sql = gerar_sql(pergunta)

    if sql:
        resultado = executar_consulta(sql)
        if resultado:
            return f"Resultado: {resultado}"
        else:
            return "Nenhum dado encontrado."
    else:
        return "Desculpe, não entendi sua pergunta."
