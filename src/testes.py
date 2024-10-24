listaUpgrade = ["THALLES", "TECNOLOGIA DA INFORMAÇÃO", "028.254.640-26", "(21)3638-8532","(21)9810-82817",
                "22/05/1999", "AFONSO MELLO", "RIO VARZEA", "RJ", 200, "CASA 207", "THALLESRJ@GMAIL.COM", 40]

colunas = [" ", "nome_funcionario", "idEspecialidade", "cpf", "telefone", 
                "celular", "data_nascimento", "rua", "bairro", "uf", "numero", "complemento", "email", "percentil"]

listaFuncionario = [1 ,"THALLES RIBEIRO NASCIMENTO", "GERENTE", "028.254.640-26", "(21)3638-8532","(21)9810-82817",
                "22/05/1999", "AFONSO MELLO", "RIO VARZEA", "RJ", 200, "CASA 207", "THALLESRJ@GMAIL.COM", 50, 1]

indices = []

for old, new in zip(listaFuncionario[1:14], listaUpgrade):
    if old == new:
        print("Iguais")
        print(f"Old: {old}")
        print(f"New: {new}")
        print()
    
    else:
        print()
        print("Diferentes") 
        print(f"Dado Selecionado: {old}")
        print(f"Novo Dado (Diferente): {new}")
        print(f"Index Old: {listaFuncionario.index(old)}")
        print(f"Index New: {listaUpgrade.index(new)}")
        indices.append(listaFuncionario.index(old))
        print()
        continue
    
if len(indices) < 1:
    print("Nenhum campo  foi alterado!")
    
else:
    validacao = True
    funcionarioUpgrade = dict()
    
    for i in indices:
        if validacao == True:
            print(validacao)
        else:
            break
        for c in colunas[1:14]:
            if i == colunas.index(c):
                if i == 12:
                    if "@" in listaUpgrade[11]:
                        validacao = True
                        funcionarioUpgrade.update({c:listaUpgrade[i - 1]})
                        print(funcionarioUpgrade)
                        # indices.remove(i)
                    
                    else:
                        print("Email Inválido")
                        validacao = False
                        print(validacao)
                        break
                
                else:
                    validacao = True
                    funcionarioUpgrade.update({c:listaUpgrade[i - 1]})
                    # indices.remove(i)
                    
                    continue
                            
            else:
                
                continue
                        
    
print(f"Validação: {validacao}")
if validacao == False:
    indices.clear()
    funcionarioUpgrade.clear()
    print("Deu merda")
    
    
else:
    for k, v in zip(funcionarioUpgrade.keys(), funcionarioUpgrade.values()):
        print(f"Chaves: {k}\nValores: {v}\n")
        if k == "idEspecialidade":
            print("especialidade")
            
        print(f"Inserindo novo dado...\nDado: {v}\nColuna: {k}\n")
        
    print("Alterações Realizadas")  
      
indices.clear()
funcionarioUpgrade.clear()
