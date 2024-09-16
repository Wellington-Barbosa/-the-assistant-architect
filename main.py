from app.chatbot import responder_pergunta


def main():
    print("Bem-vindo ao Chatbot da Empresa!")

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ['sair', 'exit']:
            print("Encerrando o chatbot. Até mais!")
            break

        resposta = responder_pergunta(pergunta)
        print(f"Chatbot: {resposta}")


if __name__ == "__main__":
    main()
