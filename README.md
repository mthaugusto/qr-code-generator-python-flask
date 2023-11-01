<h1>Gerador de QR Code Wi-Fi com Flask</h1>

Este é um aplicativo web simples que permite gerar códigos QR para redes Wi-Fi. Os códigos QR contêm informações de rede, como SSID, senha e protocolo de segurança, para facilitar a conexão de dispositivos a redes Wi-Fi.

<h2>Pré-requisitos</h2>

Antes de executar o aplicativo, você precisará ter o Python e as seguintes bibliotecas instaladas:
- Flask
- qrcode

Você pode instalá-los usando o seguinte comando: pip install Flask qrcode

<h2>Executando o aplicativo:</h2>
Clone este repositório: git clone https://github.com/seu-nome/gerador-qr-code-wifi-flask.git
Navegue até o diretório do projeto: cd gerador-qr-code-wifi-flask
Inicie o aplicativo: python app.py

O aplicativo estará disponível em http://127.0.0.1:5000/ em seu navegador.

<h2>Uso</h2>

Abra o aplicativo no navegador.
Preencha as informações da rede Wi-Fi, incluindo SSID, senha e protocolo de segurança.
Escolha o protocolo de segurança entre WPA, WEP ou None.
Clique no botão "GENERATE" para gerar o código QR.
O código QR gerado será exibido na página e salvo como qrcode_wifi.png no diretório static.

<h2>Personalização</h2>
Você pode personalizar o aplicativo da seguinte forma:

Altere o título do aplicativo em app.py no método inicio().
Personalize atributos do QR Code como o tamanho, borda, correção de erro (quantos % do QR Code pode estar danificado para ele ainda sim ser legível) e outros.
Personalize o estilo da página HTML em static/styles.css.

<h2>Contribuições</h2>
Contribuições são bem-vindas! Se você encontrar problemas ou tiver melhorias para sugerir, sinta-se à vontade para abrir uma solicitação de pull.

<h2>Autor</h2>
Matheus Leite

<h2>Projeto Figma</h2>
Bianca Nannini

<h2>Documentaçoes</h2>

Flask: https://flask.palletsprojects.com/
qrcode: https://pypi.org/project/qrcode/
