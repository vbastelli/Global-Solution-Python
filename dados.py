import random
import matplotlib.pyplot as plt

def gerar_dados_ficticios(num_dias):
    dados = []
    for dia in range(1, num_dias + 1):
        poluicao = round(random.uniform(0, 100), 2)  # Níveis de poluição por plástico (0 a 100)
        ph_agua = round(random.uniform(7.5, 8.5), 2)  # pH da água (7.5 a 8.5)
        temperatura_mar = round(random.uniform(15, 30), 2)  # Temperatura da superfície do mar (15 a 30 graus Celsius)
        dados.append({"Dia": dia, "Poluição": poluicao, "pH da Água": ph_agua, "Temp. do Mar (C)": temperatura_mar})
    return dados

def exibir_dados(dados):
    print("Dia | Poluição (plástico) | pH da Água | Temp. do Mar (C)")
    print("-" * 53)
    for dado in dados:
        print(f"{dado['Dia']:3} | {dado['Poluição']:19} | {dado['pH da Água']:11} | {dado['Temp. do Mar (C)']:15}")

def plotar_grafico(dados):
    dias = [dado['Dia'] for dado in dados]
    poluicao = [dado['Poluição'] for dado in dados]
    ph_agua = [dado['pH da Água'] for dado in dados]
    temperatura_mar = [dado['Temp. do Mar (C)'] for dado in dados]

    plt.figure(figsize=(10, 6))
    plt.plot(dias, poluicao, marker='o', label='Poluição por plástico')
    plt.plot(dias, ph_agua, marker='s', label='pH da Água')
    plt.plot(dias, temperatura_mar, marker='^', label='Temp. do Mar (C)')
    plt.xlabel('Dia')
    plt.ylabel('Valor')
    plt.title('Variação dos indicadores ao longo dos dias')
    plt.legend()
    plt.grid(True)
    plt.show()

def mostrar_dados():
    num_dias = 7
    dados = gerar_dados_ficticios(num_dias)
    exibir_dados(dados)
    plotar_grafico(dados)

if __name__ == "__main__":
    main()
