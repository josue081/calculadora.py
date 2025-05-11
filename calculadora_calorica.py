# === Função para calcular o Gasto Calórico Total (TMB ajustado ao nível de atividade) ===
def calcular_gasto_calorico(sexo, peso, altura, idade, nivel_atividade):
    if sexo.lower() == 'masculino':
        tmb = 10 * peso + 6.25 * altura - 5 * idade + 5
    else:
        tmb = 10 * peso + 6.25 * altura - 5 * idade - 161

    fator_atividade = {
        'sedentario': 1.2,
        'levemente ativo': 1.375,
        'moderadamente ativo': 1.55,
        'muito ativo': 1.725,
        'extremamente ativo': 1.9
    }

    gasto_total = tmb * fator_atividade.get(nivel_atividade.lower(), 1.2)
    return round(gasto_total, 2)

# === Função para calcular os Macronutrientes a partir das calorias e objetivo ===
def calcular_macros(calorias, objetivo):
    if objetivo == 'perder':
        calorias *= 0.8  # Redução para déficit calórico
    elif objetivo == 'ganhar':
        calorias *= 1.1  # Aumento para superávit calórico

    proteinas = round((calorias * 0.3) / 4, 1)
    carboidratos = round((calorias * 0.4) / 4, 1)
    gorduras = round((calorias * 0.3) / 9, 1)

    return calorias, proteinas, carboidratos, gorduras

# === Interface com o usuário no terminal ===
print("Olá! Seja bem-vindo(a) à sua Calculadora Nutricional Personalizada.\n")

# Coletando dados do usuário
sexo = input("Digite seu sexo (masculino/feminino): ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em cm: "))
idade = int(input("Digite sua idade: "))

print("\nNíveis de atividade física disponíveis:")
print(" - sedentario")
print(" - levemente ativo")
print(" - moderadamente ativo")
print(" - muito ativo")
print(" - extremamente ativo")
nivel_atividade = input("Digite seu nível de atividade: ")

objetivo = input("\nSeu objetivo é perder, manter ou ganhar peso? ").lower()

# Cálculos
gasto_total = calcular_gasto_calorico(sexo, peso, altura, idade, nivel_atividade)
calorias, proteinas, carboidratos, gorduras = calcular_macros(gasto_total, objetivo)

# Resultado final
print("\n=========== RESULTADO ===========")
print(f"Gasto calórico total diário estimado: {gasto_total} kcal")
print(f"Meta de calorias para seu objetivo: {round(calorias)} kcal")
print(f"Proteínas: {proteinas} g")
print(f"Carboidratos: {carboidratos} g")
print(f"Gorduras: {gorduras} g")
print("=================================")
