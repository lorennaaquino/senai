estoque = ["caneta","caderno", "borracha", "lapis"]

# adicionar novo item ao estoque
estoque.append("marcador")
print(estoque)

#remover item do estoque
estoque.remove("lapis")
print(estoque)

#verificar se um item esta em estoque
print("borracha" in estoque) # saida: true
