# Configurações de conexão com o banco de dados Oracle
db_config = {
    "user": "tasy",
    "password": "aloisk",
    "dsn": "172.25.1.4:1521/DBTASY"
}

# Se for usar o Oracle Instant Client, descomente a linha abaixo:
# oracle_client_path = r"Caminho/para/o/instant/client"

# Habilita o modo thick, necessário para suportar versões antigas do Oracle Database
oracledb.init_oracle_client(lib_dir=r"C:\instantclient_23_4")  # Altere para o caminho correto do Instant Client