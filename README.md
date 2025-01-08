\# Space Invaders Clone

!\[Space Invaders\](assets/SpaceBK.jpg)

\## Descrição

Este é um clone do clássico jogo \*\*Space Invaders\*\* desenvolvido em
Python utilizando a biblioteca \*\*Pygame\*\*. O jogo permite que um ou
dois jogadores controlarem suas naves para defender a Terra contra ondas
de alienígenas invasores. Com gráficos simples e jogabilidade
envolvente, este projeto é uma ótima maneira de aprender programação de
jogos e conceitos de Pygame.

\## Funcionalidades

\- \*\*Modo 1 Jogador:\*\* Controle uma nave para eliminar as ondas de
alienígenas. - \*\*Modo 2 Jogadores:\*\* Dois jogadores podem jogar
simultaneamente, cada um controlando sua própria nave. - \*\*Contagem de
Vidas:\*\* Cada jogador possui um número limitado de vidas. -
\*\*Pontuação:\*\* Sistema de pontuação baseado no número de alienígenas
eliminados. - \*\*Aumento de Dificuldade:\*\* A velocidade dos
alienígenas aumenta conforme o jogo avança. - \*\*Menu Intuitivo:\*\*
Interface de menu para selecionar modos de jogo e sair. - \*\*Efeitos
Sonoros:\*\* Sons de tiro e explosão para uma melhor experiência de
jogo.

\## Capturas de Tela

!\[Menu Inicial\](assets/Game_over1.jpg) \*Menu Inicial\*

!\[Jogo em Andamento\](assets/Gameplay.png) \*Jogo em Andamento\*

\## Instalação

\### Pré-requisitos

\- \*\*Python 3.6+\*\*: Certifique-se de ter o Python instalado.
\[Download Python\](https://www.python.org/downloads/) - \*\*Pygame\*\*:
Biblioteca para desenvolvimento de jogos em Python.

\### Passo a Passo

1\. \*\*Clone o Repositório:\*\*

\`\`\`bash git clone
https://github.com/seu-usuario/space-invaders-clone.git cd
space-invaders-clone \`\`\`

2\. \*\*Crie um Ambiente Virtual (Opcional, mas Recomendado):\*\*

\`\`\`bash python -m venv venv source venv/bin/activate \# Para
Linux/Mac venv\\Scripts\\activate \# Para Windows \`\`\`

3\. \*\*Instale as Dependências:\*\*

\*instale o Pygame:\*

\`\`\`bash pip install pygame \`\`\`

4\. \*\*Execute o Jogo:\*\*

\`\`\`bash python Space_invaders.py \`\`\`

\## Como Jogar

1\. \*\*Inicie o Jogo:\*\*  - Execute o script principal para iniciar o
jogo.

2\. \*\*Menu Principal:\*\*  - Selecione \*\*\"1 Player\"\*\* para jogar
sozinho.  - Selecione \*\*\"2 Players\"\*\* para jogar com um amigo.  -
Selecione \*\*\"Sair\"\*\* para fechar o jogo.

3\. \*\*Controles:\*\*  - \*\*Jogador 1:\*\*  - \*\*Mover para
Esquerda:\*\* \`A\` ou \`Seta Esquerda\`  - \*\*Mover para Direita:\*\*
\`D\` ou \`Seta Direita\`  - \*\*Atirar:\*\* \`Espaço\`  - \*\*Jogador
2:\*\* (Se estiver jogando em modo 2 jogadores)  - \*\*Mover para
Esquerda:\*\* \`Left Arrow\` (Seta Esquerda)  - \*\*Mover para
Direita:\*\* \`Right Arrow\` (Seta Direita)  - \*\*Atirar:\*\* \`Ctrl
direito\` (Control direito)

4\. \*\*Objetivo:\*\*  - Elimine todos os alienígenas antes que eles
alcancem a base.  - Evite ser atingido pelos tiros dos alienígenas e
faça a maior pontuação que conseguir.

\## Estrutura do Projeto

\`\`\` space-invaders-clone/ ├── assets/ │ ├── Explosion.mp3 │ ├──
Life.png │ ├── Menu.jpg │ ├── PressStart2P.ttf │ ├── SpaceBK.jpg │ └──
Title.png ├── Aliens.py ├── Player.py ├── Sprites.py ├── Menu.py ├──
Space_invaders.py ├── Method.py ├── Config.py ├── README.md └──
requirements.txt \`\`\`

\- \*\*Aliens.py:\*\* Define a classe Alien e sua lógica de
comportamento. - \*\*Player.py:\*\* Define a classe Player e Player2,
controlando as naves dos jogadores. - \*\*Sprites.py:\*\* Gerencia os
grupos de sprites para aliens, balas, etc. - \*\*Menu.py:\*\* Gerencia a
interface do menu principal. - \*\*Space_invaders.py:\*\* Script
principal que inicializa e executa o jogo. - \*\*Method.py:\*\* Contém
métodos auxiliares para gerenciar fases, pontuação, etc. -
\*\*Config.py:\*\* Define configurações como largura e altura da tela. -
\*\*assets/:\*\* Contém todos os recursos gráficos e sonoros do jogo. -
\*\*requirements.txt:\*\* Lista de dependências do projeto.

\## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou
enviar pull requests para melhorar o projeto.

1\. \*\*Fork o Repositório\*\* 2. \*\*Crie uma Branch para sua
Feature:\*\*

\`\`\`bash git checkout -b feature/nova-feature \`\`\`

3\. \*\*Commit suas Alterações:\*\*

\`\`\`bash git commit -m \"Adiciona nova feature\" \`\`\`

4\. \*\*Push para a Branch:\*\*

\`\`\`bash git push origin feature/nova-feature \`\`\`

5\. \*\*Abra um Pull Request\*\*

\## Agradecimentos

\- \*\*Pygame:\*\* Obrigado à equipe do Pygame por criar uma excelente
biblioteca para desenvolvimento de jogos em Python. -
\*\*Inspiração:\*\* Baseado no clássico jogo Space Invaders desenvolvido
pela Taito em 1978.

\*Desenvolvido por \[Philipe\](https://github.com/Phill-Chil))\*
