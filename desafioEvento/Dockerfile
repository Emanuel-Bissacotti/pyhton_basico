# Use a imagem oficial do Visual Studio Code
FROM codercom/code-server

# Instale o Python e algumas extensões úteis
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install pylint flake8 black

# Exponha a porta 8080 para o VSCode
EXPOSE 8080

# Configure o usuário para evitar erros de permissão
RUN mkdir -p /home/coder/project && chown -R coder:coder /home/coder
USER coder

# Execute o VSCode Server no início
CMD ["code-server", "--auth=none", "--no-auth", "--host=0.0.0.0"]
