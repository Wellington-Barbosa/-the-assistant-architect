# Chatbot de Assistência para Sistema de Gestão de Saúde

## Visão Geral

Este projeto consiste em um **chatbot de assistência** para consulta de informações relacionadas ao sistema de gestão de saúde **Tasy**, utilizado em uma base de dados Oracle. O chatbot é capaz de responder perguntas sobre o número de beneficiários ativos, total de beneficiários por gênero (masculino/feminino), e outras consultas relacionadas ao negócio. 

O foco principal é integrar um sistema de perguntas e respostas que consulta diretamente a base de dados Oracle, interpretando perguntas do usuário e gerando as consultas SQL apropriadas.

## Funcionalidades Implementadas

### Perguntas Suportadas Até o Momento
O chatbot consegue responder às seguintes perguntas:
- **Total de Beneficiários Ativos**:
  - "Quantos beneficiários ativos temos hoje na empresa?"
  - "Qual o número de beneficiários ativos?"
  
- **Total de Beneficiários Masculinos**:
  - "Quantos beneficiários são do sexo masculino?"
  - "Quantos homens estão cadastrados?"

- **Total de Beneficiários Femininos**:
  - "Quantos beneficiários são do sexo feminino?"
  - "Quantas mulheres estão cadastradas?"

### Tecnologias Utilizadas
- **Python 3.x**
- **Oracle Database** usando a biblioteca `oracledb`
- **Variáveis de ambiente** utilizando `dotenv`
- **Processamento básico de linguagem natural** para interpretação das perguntas


## Configuração do Ambiente

### 1. Pré-requisitos

- **Python 3.x**
- **Oracle Database** (versão compatível)
- **Oracle Instant Client** (se utilizar o modo thick)
- Instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```
### 2. Configuração do Banco de Dados

Para conectar ao banco de dados Oracle, é necessário configurar as credenciais de acesso. Essas informações serão armazenadas no arquivo `.env` para maior segurança.

Exemplo de arquivo `.env`:

Crie um arquivo chamado `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:

```bash
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_DSN=oracle_host:1521/nome_do_servico
```
Atenção: O arquivo `.env` é sensível e não deve ser versionado. Ele já está incluído no arquivo `.gitignore`.

### 3. Configuração do Cliente Oracle (Modo Thick)

Se estiver utilizando o Oracle Instant Client para o modo thick, configure o caminho no arquivo `config.py`:
    
```python
oracledb.init_oracle_client(lib_dir=r"C:\caminho_para_instantclient")
```
Se não for utilizar o Instant Client, comente ou remova essa linha para usar o modo thin, que não requer instalação adicional.

### 4. Execução do Chatbot

Após configurar o ambiente e o banco de dados, execute o arquivo `main.py` para iniciar o chatbot:
    
```bash
python main.py
```

## Próximos Passos

- Melhorar o processamento de linguagem natural para interpretar perguntas mais complexas e diferentes variações.


- Adicionar novas funcionalidades, como consultas detalhadas sobre outros aspectos do sistema de gestão de saúde.


- Desenvolver uma interface gráfica ou integração com aplicativos de chat, como Slack ou Microsoft Teams.

## Contribuições

Para contribuir com o projeto:

1. Faça um fork do repositório.
2. Crie uma branch para suas mudanças: git checkout -b minha-nova-funcionalidade.
3. Faça commit das suas mudanças: git commit -m 'Adiciona nova funcionalidade'.
4. Envie suas alterações: git push origin minha-nova-funcionalidade.
5. Abra um Pull Request.

## Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar conforme necessário.