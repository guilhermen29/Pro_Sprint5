🚗 Dashboard de Vendas de Veículos – Projeto de Deploy com Streamlit e Render








🔗 Aplicativo Web Online: https://pro-sprint5.onrender.com

📖 Descrição do Projeto

Este projeto foi desenvolvido como parte do curso de Ferramentas de Desenvolvimento de Software da TripleTen.
O objetivo principal foi criar, configurar e publicar um aplicativo web interativo utilizando Streamlit, a partir de uma análise exploratória de dados (EDA) feita em Python.

O app permite ao usuário interagir com os dados de vendas de veículos — visualizando histogramas e gráficos de dispersão dinâmicos — diretamente em um navegador, sem necessidade de rodar código localmente.

Além da análise, o foco principal deste projeto foi demonstrar domínio em boas práticas de engenharia de software, incluindo:

Criação e gerenciamento de ambientes virtuais;

Estruturação de repositórios Git e GitHub;

Deploy de aplicativos web em serviços de nuvem (Render);

Uso de bibliotecas populares para visualização e manipulação de dados.

🧩 Funcionalidades Principais

✅ Interface interativa desenvolvida com Streamlit
✅ Visualizações com Plotly Express
✅ Leitura e exibição de dados em tempo real via Pandas
✅ Geração de histograma e gráfico de dispersão com um clique
✅ Layout leve e responsivo, acessível via web

📊 Conjunto de Dados

O conjunto de dados utilizado contém informações de anúncios de vendas de veículos nos Estados Unidos, como:

Preço (price)

Quilometragem (odometer)

Tipo de combustível (fuel)

Tipo de transmissão (transmission)

Estado do veículo (condition)

Arquivo principal:
vehicles_us.csv

⚙️ Estrutura do Projeto

├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── notebooks
│   └── EDA.ipynb
└── .streamlit
    └── config.toml

🔍 Arquivos principais:

app.py → Script principal do Streamlit responsável pela interface e interatividade.

EDA.ipynb → Notebook Jupyter com a análise exploratória inicial (histogramas e dispersões).

requirements.txt → Lista de dependências necessárias para execução do app.

config.toml → Configuração do Streamlit para compatibilidade com o Render.

🧠 Tecnologias Utilizadas
Categoria	Ferramenta
Linguagem	Python 3.11
Web Framework	Streamlit
Visualização	Plotly Express
Análise de Dados	Pandas
Deploy	Render
IDE	Visual Studio Code
Controle de Versão	Git & GitHub
🚀 Deploy na Nuvem (Render)

O aplicativo foi publicado no Render, um serviço de hospedagem gratuito para aplicações web Python.

Configurações de deploy utilizadas:

Build Command:

pip install --upgrade pip && pip install -r requirements.txt


Start Command:

streamlit run app.py --server.port 10000 --server.address 0.0.0.0


O arquivo de configuração do Streamlit (.streamlit/config.toml) garante a compatibilidade da porta com o ambiente Render:

[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000

🧮 Passos Principais do Desenvolvimento

Criação do ambiente virtual e instalação das bibliotecas:

python -m venv venv
pip install pandas plotly_express streamlit


Análise exploratória (EDA) no Jupyter Notebook:

Geração de histogramas e scatter plots com plotly.express.

Desenvolvimento do dashboard no app.py com Streamlit:

Leitura do CSV com pandas.

Criação de botões e gráficos interativos.

Configuração do GitHub:

Versionamento e commits regulares.

Publicação do código no repositório remoto.

Deploy na nuvem (Render):

Integração direta com o repositório GitHub.

Execução automática a cada novo commit.

🧑‍💻 Como Executar Localmente

Clone este repositório:

git clone https://github.com/guilhermen29/Pro_Sprint5.git
cd Pro_Sprint5


Crie o ambiente virtual e ative-o:

python -m venv venv
venv\Scripts\activate  # Windows


Instale as dependências:

pip install -r requirements.txt


Execute o app localmente:

streamlit run app.py


O dashboard será aberto automaticamente no navegador padrão em:
👉 http://localhost:8501

📈 Demonstração Visual

O aplicativo exibe gráficos interativos como:

Histograma da quilometragem dos veículos (odometer)

Gráfico de dispersão relacionando preço e quilometragem (price × odometer)

🏁 Conclusão

Este projeto demonstrou o processo completo de desenvolvimento, versionamento e publicação de um aplicativo de dados na nuvem.
Foram aplicadas boas práticas de engenharia de software, manipulação de dados com Pandas, visualizações com Plotly, e deploy com Streamlit + Render.

O resultado é um dashboard dinâmico, leve e acessível publicamente, que serve como um excelente exemplo de integração entre análise de dados e desenvolvimento web.

✉️ Autor

Guilherme Marques
📍 Brasil
💼 Projeto desenvolvido para a TripleTen
