<h1>WGPark</h1>
<ul>
    <ul>
        <li><h2>Informações:</h2></li>
        <li><strong>Projeto criado por Willian Bello e Giovani Lima</strong></li>
        <li><a href="https://github.com/willianbello">Willian Bello</a></li>
        <li><a href="https://github.com/xEveRLasT">Giovani Lima</a></li>
        <li>Aplicativo para controle de entrada e saída de veículos de um estacionamento</li>
    </ul>
    <ul>
        <li><h2>Objetivos:</h2></li>
        <li>Pesquisar e colocar em prática os conhecimentos adquiridos ao longo do tempo em HTML, CSS, Javascript, Bootstrap, Python, MySQL e Flask.</li>
    </ul>
    <ul>
        <li><h2>Requisitos:</h2></li>
        <li>Deve ser exigido login e senha do administrador para ter acesso as informações e ações do app</li>
        <li>Deve mostrar os veículos que estão dentro do pátio com a data e hora de entrada</li>
        <li>Deve guardar no banco de dados todos as informações dos carros que já estiveram no estacionamento com os horários e datas de entrada e saída</li>
        <li>Enquanto o veículo estiver no pátio deverá ter um status que será "ativo" se ainda está no patio e continua contando o tempo até sua saída e o status "finalizado" o cliente fez o pagamento e o veículo está pronto pra ser retirado</li>
    </ul>
    <ul>
        <li><h2>Instruções para instalação:</h2></li>
        <li>Para rodar, é necessário instalar o Python3.x, Flask e frameworks necessários. É recomendado fazer em uma máquina virtual a modo de evitar conflitos com arquivos do seu SO</li>
        <ul>
            <li><h3>Instalando Flask e demais frameworks utilizados no Windows:</h3></li>
            <li>Verifique se o Python está instalado no sistema. Caso não esteja:
            <br>https://www.python.org/downloads/</li>
        </ul>
        <ul>
            <li><h3>Com o Python instalado:</h3></li>
            <li>pip install Flask</li>
            <li>pip install flask_wtf</li>
            <li>pip install wtforms</li>
            <li>pip install mysqlconnector</li>
        </ul>
         <ul>
            <li><h3>Instalando Flask no Linux:</h3></li>
            <li>Verifique se existe o Python instalado no sistema(geralmente vem instalado), mas caso não esteja:
             <br><br>apt-get install python (debian e derivados)</li>
        </ul>
        <ul>
            <li><h3>Verifique se o "pip" está instalado. Caso não esteja:</h3></li>
            <li>apt install python3-pip</li>
            <li>pip install Flask</li>
        </ul>
         <ul>
            <li><h3>Com o Python instalado:</h3></li>
            <li>pip install Flask</li>
            <li>pip install flask_wtf</li>
            <li>pip install wtforms</li>
            <li>pip install mysqlconnector</li>
            </ul>
            <ul>
            <li><h3>Executando o programa:</h3></li>
            <li>Execute o server.py com "python3 server.py" e como um passe de mágica, ele irá gerar um sevidor web de endereço: http://127.0.0.1:5000/
        </ul>
    </ul>
</ul>

<li><h2> Utilizando o site:</h2></li>
<li>Para iniciar a utilização do site, será necessário criar uma conta de ADMIN. O motivo? O motivo é que somente uma conta de administrador pode criar usuários para o site.</li>
<li><h3>Criando uma conta de administrador:</h3></li>
<ul>
    <li>Em bd.py, existe uma função chamada cadastro_admin. Para utiliza-la, basta ir até o rodapé do arquivo e declarar a mesma desta forma: "cadastro_admin()" sem as aspas, sem identação, sem nada, somente isso.</li>
    <li>Abra um terminal conforme sua IDE. No meu caso, é o VSCODE(recomendo o uso do memso, pois é easy de usar). Vá em "Terminal" depois "New terminal". Navegue até a pasta onde está o bd.py e digite no terminal: "python3 bd.py" sem aspas.</li>
    <li>No terminal aparecerão solicitações de criação de login e senha. Faça a criação conforme desejar.</li>
    <li>Execute o server.py com "python3 server.py" e como um passe de mágica, ele irá gerar um sevidor web de endereço: http://127.0.0.1:5000/</li>
    <li>Digite /admin ao lado do endereço e você será direcionado para a página de admin. Faça login com o usuário e senha que acabou de criar e terá acesso a página de criação de usuários para o site. Note que o layout foi feito pelo responsável pelo backend, releve.</li>
    <li>Depois de criar os usuários desejados, também será possível deletar os mesmos. Usuários administradores não podem ser deletados até o momento, mas em breve essa funcionalidade vai surgir.<li>
    <li>Volte ao endereço http://127.0.0.1:5000, logue com o usuario de acesso recém criado e aproveite esta bela obra de arte</li>
</ul>