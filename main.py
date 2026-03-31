from j01_mad_libs.mad_libs import jogar_mad_libs
from j02_jokenpo.fogo_agua_planta import jogar_fogo_agua_planta
from j03_calculadora.calculadora import jogar_calculadora
from j04_impar_par.impar_par import jogar_impar_par


print (r"""
   __     ______     ______     ______     ______   ______     ______     ______    
  /\ \   /\  __ \   /\  ___\   /\  __ \   /\__  _\ /\  ___\   /\  ___\   /\  __ \   
 _\_\ \  \ \ \/\ \  \ \ \__ \  \ \ \/\ \  \/_/\ \/ \ \  __\   \ \ \____  \ \  __ \  
/\_____\  \ \_____\  \ \_____\  \ \_____\    \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
\/_____/   \/_____/   \/_____/   \/_____/     \/_/   \/_____/   \/_____/   \/_/\/_/ 
                                                                                    
""")
print ("""
╔═╗┌─┐┬┌┬┐┌─┐  ┌─┐┌─┐┬─┐  ╦┌─┐┌─┐┌┬┐┌─┐┬─┐┌─┐
╠╣ ├┤ │ │ │ │  ├─┘│ │├┬┘  ║└─┐├─┤ │││ │├┬┘├─┤
╚  └─┘┴ ┴ └─┘  ┴  └─┘┴└─  ╩└─┘┴ ┴─┴┘└─┘┴└─┴ ┴
""")

jogo = input ("""
---------------------------------
*         01 - Mad Libs         *
*         02 - Calculadora      *
*         03 - Impar ou par     *
*         04 - Jokenpô          *
---------------------------------

Qual você deseja jogar? """)

if jogo== 1: 
    jogar_mad_libs
elif jogo==2:
    jogar_calculadora
elif jogo==3:
    jogar_impar_par
elif jogo==4:
    jogar_jokenpo