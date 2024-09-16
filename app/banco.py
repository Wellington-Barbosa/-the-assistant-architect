import oracledb
from app.config import db_config


def conectar_banco():
    try:
        # Se for usar o Oracle Instant Client:
        # oracledb.init_oracle_client(lib_dir=oracle_client_path)

        conexao = oracledb.connect(
            user=db_config['user'],
            password=db_config['password'],
            dsn=db_config['dsn']
        )
        return conexao
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro na conexão: {erro.message}")
        return None


def executar_consulta(sql):
    conexao = conectar_banco()
    if conexao is None:
        return "Erro ao conectar ao banco de dados."

    cursor = conexao.cursor()
    try:
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return resultado
    except oracledb.DatabaseError as e:
        erro, = e.args
        return f"Erro ao executar a consulta: {erro.message}"
    finally:
        cursor.close()
        conexao.close()
