import random

def jogar_forca():
    print("=" * 30)
    print("   BEM-VINDO AO JOGO DA FORCA   ")
    print("=" * 30)

    # Lista de palavras para o jogo (tema: Tecnologia/Programação)
    palavras = ["python", "programacao", "desenvolvedor", "algoritmo", "codigo", "computador"]
    
    # Escolhe uma palavra aleatoriamente
    palavra_secreta = random.choice(palavras).upper()
    
    # Cria uma lista de traços para representar as letras oculta
    letras_descobertas = ["_" for _ in palavra_secreta]
    
    tentativas = 6
    letras_digitadas = []

    # Loop principal do jogo
    while tentativas > 0 and "_" in letras_descobertas:
        print(f"\nPalavra: {' '.join(letras_descobertas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras já tentadas: {', '.join(letras_digitadas)}")
        
        chute = input("Digite uma letra: ").strip().upper()

        # Validação da entrada do usuário
        if len(chute) != 1 or not chute.isalpha():
            print("⚠️ Por favor, digite apenas uma única letra válida.")
            continue
            
        if chute in letras_digitadas:
            print("⚠️ Você já tentou essa letra. Tente outra!")
            continue

        letras_digitadas.append(chute)

        # Verifica se a letra está na palavra
        if chute in palavra_secreta:
            print(f"✅ Boa! A letra '{chute}' está na palavra.")
            for indice, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[indice] = chute
        else:
            print(f"❌ A letra '{chute}' não está na palavra.")
            tentativas -= 1

    # Final do jogo
    print("\n" + "=" * 30)
    if "_" not in letras_descobertas:
        print(f"🎉 PARABÉNS! Você venceu! A palavra era: {palavra_secreta}")
    else:
        print(f"💀 GAME OVER! Suas tentativas acabaram. A palavra era: {palavra_secreta}")
    print("=" * 30)

if __name__ == "__main__":
    jogar_forca()