# Auto Clicker

Um auto-clicker de código aberto com uma interface gráfica amigável, desenvolvido em Python. Este projeto foi criado para fins educativos e como parte do meu portfólio.

## Funcionalidades

- Intervalo de cliques personalizável em milissegundos.
- Funcionalidade de iniciar e parar usando botões ou atalhos de teclado.
- Design leve, eficiente e intuitivo.

## Como Usar

1. **Baixar o Executável**  
   Se preferir não executar o código-fonte, faça o download do arquivo `.exe`.

2. **Executar o Programa**  
   Abra o programa e você verá uma interface onde poderá:
   - Definir o número de horas para clicar.
   - Configurar o intervalo entre os cliques em milissegundos.
   - Iniciar e parar o processo de cliques.

3. **Atalhos de Teclado**  
   - Pressione **F8** para iniciar os cliques.
   - Pressione **F9** para parar os cliques.


## Aviso sobre Falso Positivo do Antivírus

Alguns antivírus podem identificar o executável gerado como um **falso positivo**. Isso significa que o arquivo é detectado como uma ameaça, mas na verdade ele é seguro. Esse comportamento ocorre devido a alguns fatores comuns:

- **Compactação de Executáveis**: Ferramentas como o **Nuitka** ou **PyInstaller** compactam e empacotam o código Python em um único arquivo `.exe`. Essa técnica é semelhante à usada por malwares para ocultar seu código, o que pode confundir os antivírus.
- **Automação de Cliques**: Softwares que simulam cliques automáticos podem ser marcados como potencialmente indesejados, já que podem ser mal utilizados por outras pessoas.
- **Uso de Bibliotecas Dinâmicas**: O executável inclui dependências externas (como Tkinter e PyAutoGUI), o que pode ser interpretado como comportamento suspeito.

### Como Garantir que o Programa é Seguro

1. **Código Aberto**  
   O código-fonte do programa está disponível neste repositório. Você pode inspecioná-lo para verificar que ele não realiza nenhuma atividade maliciosa.

2. **Compile Você Mesmo**  
   Para máxima segurança, você pode compilar o executável diretamente no seu computador.

3. **Assinatura Digital (Opcional)**  
   Uma assinatura digital pode ser adicionada ao executável para aumentar a confiança em ambientes que exigem maior segurança.

Se você encontrar problemas com o antivírus, é possível adicionar o arquivo à lista de exclusões do antivírus, ou, se preferir, usar o código-fonte diretamente.


## Instalação (para Desenvolvedores)

1. Clone o repositório:
   ```bash
   git clone https://github.com/FilipeLacerda738/autoClicker.git
   git clone git@github.com:FilipeLacerda738/autoClicker.git
   cd auto-clicker
