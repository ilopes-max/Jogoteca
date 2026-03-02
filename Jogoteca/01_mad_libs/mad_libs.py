print ("""
       _=,_         
    o_/6 /#\        
    \__ |##/        
     ='|--\         
       /   #'-.     
       \#|_   _'-. /
        |/ \_( # |" 
       C/ ,--___/        


                   
                
 """)


print ("                                     Seja-bem vindo(a) ao Mad Libs, hoje nós iremos montar a sua história maluca!!!!                      ")





animal = input("Qual vai ser o seu animal?")

lugar = input ("Qual vai ser o lugar?")

verbo = input ("Qual verbo você gostaria de adicionar a sua história?")

objeto = input ("Qual vai ser o seu objeto?")

adjetivo = input ("Qual vai ser o seu adjetivo?")

emoção = input ("qual vai ser a emoção para sua história?")


resultado = (f"""Em uma manhã tranquila, o {animal} acordou sentido uma intensa {emoção} e decidiu {verbo} para o {lugar}, em busca de algo novo. Ele era muito {adjetivo} e, antes de sair
             pegou o seu {objeto} favorito para levar na aventura. 
             Ao chegar no {lugar}, o {animal} começou a {verbo} lentamente observando cada detalhe ao seu redor. Tudo parecia muito {adjetivo}, o que aumentava sua {emoção}
             a cada passo. O {objeto} que carregava  se mostrou útil em vários momentos no caminho. 
             Depois de algum tempo, já um pouco cansado, mas ainda {adjetivo}, o {animal} resolveu {verbo} novamente e seguir em frente pelo {lugar}. No fim do dia, sintindo uma grande 
             {emoção}, ele voltou para casa entendendo que aquela jornada, ao lado do {objeto}, tinha sido especial e cheia de aprendizados. """)

print(f"Sua história ficou pronta= {resultado}")
