# Download_m3u8.py

## Descrição
O `download_m3u8.py` é um script em Python que possibilita o download de vídeos no formato m3u8 a partir de uma URL fornecida pelo usuário. O programa utiliza as bibliotecas `re` para tratamento de entradas e `subprocess` para executar comandos no sistema, além de requerer o utilitário `ffmpeg` presente na pasta do arquivo `.py` para a conversão do arquivo m3u8 em um formato de vídeo mais convencional, permitindo assim o download do vídeo.

## Requisitos
- Python 3 instalado no sistema.
- O utilitário `ffmpeg` deve estar presente na mesma pasta onde o arquivo `download_m3u8.py` está localizado.
- É necessário fornecer uma URL de vídeo no formato m3u8 para fazer o download. Recomenda-se o uso de um "M3U8 Sniffer" para obter o link apropriado.
  

## Instruções de Uso
1. Certifique-se de que o Python 3 esteja instalado em seu sistema.
2. Baixe o arquivo `download_m3u8.py`.
3. Instale o utilitário `ffmpeg` na mesma pasta onde o arquivo `download_m3u8.py` está localizado.
4. Utilize um "M3U8 Sniffer" para capturar o link do vídeo no formato m3u8 que você deseja baixar.
5. Abra o terminal ou prompt de comando no diretório onde o arquivo `download_m3u8.py` está localizado.
6. Execute o programa digitando o seguinte comando:
   ```bash
   python download_m3u8.py
O programa solicitará que você insira a URL do vídeo m3u8. Cole o link obtido anteriormente do "M3U8 Sniffer".
Em seguida, o programa perguntará se você deseja baixar o vídeo completo ou segmentos específicos. Escolha uma das opções digitando o número correspondente.
Dependendo da opção escolhida, o programa solicitará mais informações, como o formato de saída e o nome do arquivo de saída (sem extensão).
O programa usará o ffmpeg para realizar o download do vídeo m3u8, convertendo-o para o formato escolhido, e o salvará com o nome fornecido por você.
## Responsabilidade do Usuário
O uso deste programa é de responsabilidade do usuário. Ao utilizá-lo, você concorda em assumir total responsabilidade por quaisquer consequências decorrentes do download e uso de vídeos a partir de URLs fornecidas. Certifique-se sempre de estar em conformidade com as políticas do site, respeitar os direitos autorais e cumprir as leis aplicáveis antes de fazer o download de qualquer conteúdo.
