AquaDrone Innovations
Guilherme Machado Moreira
RM - 557290
Lucca Campello Rodrigues dos Santos.
RM - 558455
Victório Maia Bastelli
RM - 554723

Descrição do Projeto
A AquaDrone Innovations é uma empresa dedicada ao desenvolvimento de soluções tecnológicas para o monitoramento e proteção ambiental. Nosso projeto envolve a criação de um sistema interativo que permite aos usuários explorar informações sobre nossos produtos e serviços, bem como obter dados importantes sobre o oceano. O sistema é implementado em Python e oferece uma interface de linha de comando para facilitar a navegação.

Instruções de Uso
Clone o repositório do projeto para o seu ambiente local.
Certifique-se de ter o Python instalado (versão 3.6 ou superior).
Instale as dependências necessárias.
Execute o script principal para iniciar o programa.
Passo a Passo:
bash
Copiar código
# Clone o repositório
git clone https://github.com/vbastelli/Global-Solution-Python/tree/master

# Navegue até o diretório do projeto
cd [nome_do_diretório]

# (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

# Instale as dependências 
# Dependências do projeto AquaDrone Innovations

# Biblioteca para manipulação de comandos do sistema
os-sys

# Biblioteca para geração de números aleatórios
random

# Biblioteca para visualização de dados
matplotlib
EOF


# Execute o script principal
python main.py
## Requisitos
- Python 3.6 ou superior
- Bibliotecas listadas em #Instale as dependências

## Dependências
O projeto utiliza as seguintes bibliotecas:
- `os`: Para manipulação de comandos do sistema.
- `random`: Para geração de números aleatórios.
- `matplotlib`: Para visualização de dados.
- `textos`: Módulo personalizado contendo textos descritivos sobre nossos produtos e serviços.
- `dados`: Módulo personalizado para exibir dados sobre o oceano.


Estrutura do Projeto:
├── main.py                # Script principal do projeto
├── textos.py              # Módulo contendo textos descritivos
├── dados.py               # Módulo para exibição de dados
├── README.md              # Este arquivo README
├── requirements.txt       # Lista de dependências (se houver)

Funcionalidades:

Informações sobre nosso drone:
Detalhes sobre a tecnologia e capacidades do nosso drone de monitoramento ambiental.

Sobre nós:
Informações sobre a empresa AquaDrone Innovations, nossa missão e visão.

Serviços e produtos:
Descrição dos nossos principais produtos e serviços, incluindo sensores marinhos avançados, drones aquáticos e aéreos, plataforma de visualização de dados, e iniciativas de engajamento e educação ambiental.

Contato:
Informações de contato para que os usuários possam se comunicar conosco.

Dados sobre o oceano:
Exibição de dados relevantes sobre o estado dos oceanos.
