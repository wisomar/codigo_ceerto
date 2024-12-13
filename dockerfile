# Usando uma imagem oficial do Python como base
FROM python:3.10-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY . /app

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 5000 (padrão do Flask)
EXPOSE 5000

# Comando para rodar o servidor Flask
CMD ["flask", "run", "--host=0.0.0.0"]
