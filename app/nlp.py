def gerar_sql(pergunta):
    if "total de pacientes" in pergunta.lower():
        return "SELECT COUNT(*) FROM tasy.pacientes"
    elif "nome dos pacientes" in pergunta.lower():
        return "SELECT nome FROM tasy.pacientes WHERE ROWNUM <= 10"
    else:
        return None
