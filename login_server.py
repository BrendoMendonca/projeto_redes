import http.server
import socketserver

class LoginHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/login':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            login_form = """
            <html>
            <head>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    form {
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <form method="POST" action="/auth">
                    <h2>Login</h2>
                    <label for="username">Username: </label>
                    <input type="text" name="username" id="username"><br><br>
                    <label for="password">Password: </label>
                    <input type="password" name="password" id="password"><br><br>
                    <input type="submit" value="Login"><br><br>
                    <p>Use username 'user' and password 'password' to login.</p>
                </form>
            </body>
            </html>
            """
            self.wfile.write(login_form.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        username, password = self.extract_credentials(post_data)
        
        if username == 'user' and password == 'password':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Substitua as mensagens pela página HTML sobre a Paraíba
            paraiba_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Paraíba</title>
            </head>
            <body>
                <h1>Bem vindos à Paraíba!</h1>
                <p>
                    A Paraíba é um estado localizado na região Nordeste do Brasil. É conhecido por sua rica cultura, belezas naturais, história e tradições únicas. Aqui estão alguns aspectos notáveis sobre a Paraíba:
                </p>

                <h2>Capital e cidades importantes:</h2>
                <p>
                    A capital do estado é João Pessoa, que é também a cidade mais populosa da Paraíba. Outras cidades significativas incluem Campina Grande, Patos, Bayeux e Santa Rita.
                </p>

                <h2>Belezas naturais:</h2>
                <p>
                    A Paraíba é conhecida por suas praias deslumbrantes ao longo de sua costa, incluindo a Praia de Tambaba, que é famosa por ser uma das primeiras praias de nudismo oficial do Brasil. O estado possui um litoral de aproximadamente 138 km banhado pelo Oceano Atlântico.
                </p>

                <h2>Cultura e tradições:</h2>
                <p>
                    A cultura paraibana é rica e diversificada, influenciada pela herança indígena, africana e europeia. O estado é conhecido por suas festas populares, como o "Carnaval de rua de João Pessoa" e o "São João" de Campina Grande, um dos maiores festejos juninos do Brasil. A música, a dança e a culinária também desempenham um papel importante na cultura paraibana.
                </p>

                <h2>História:</h2>
                <p>
                    A Paraíba possui uma história rica e desempenhou um papel importante no contexto histórico do Brasil. A cidade de João Pessoa foi o local onde, em 1930, ocorreu a Revolução de 1930, que levou Getúlio Vargas ao poder. Além disso, a cidade de Cabedelo foi o ponto de partida da chamada "Revolução de 1817", um movimento de caráter emancipacionista e liberal.
                </p>

                <h2>Economia:</h2>
                <p>
                    A economia da Paraíba é diversificada, incluindo setores como agricultura, pecuária, indústria, comércio e serviços. A agricultura é importante na produção de cana-de-açúcar, algodão, milho e frutas, e a pecuária desempenha um papel significativo na produção de carne e leite.
                </p>

                <h2>Universidades e Educação:</h2>
                <p>
                    A Paraíba é sede de várias instituições de ensino superior, incluindo a Universidade Federal da Paraíba (UFPB) e a Universidade Estadual da Paraíba (UEPB), que desempenham um papel crucial na educação e pesquisa na região.
                </p>

                <h2>Turismo:</h2>
                <p>
                    Além das praias, a Paraíba oferece atrações turísticas como o Parque Estadual do Pico do Jabre, onde está localizado o ponto mais alto do estado, e o Lajedo de Pai Mateus, uma formação rochosa única. A cidade de Areia é conhecida por sua arquitetura colonial bem preservada.
                </p>

                <p>
                    A Paraíba é um estado que combina cultura, história, belezas naturais e uma população acolhedora. É um destino atraente para quem deseja explorar o Nordeste do Brasil e desfrutar de suas diversas atrações.
                </p>
            </body>
            </html>
            """
            self.wfile.write(paraiba_html.encode('utf-8'))
        else:
            self.send_response(401)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Login failed.')
            
    def extract_credentials(self, post_data):
        credentials = post_data.split('&')
        username = credentials[0].split('=')[1]
        password = credentials[1].split('=')[1]
        return username, password

port = 8000
with socketserver.TCPServer(("", port), LoginHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
