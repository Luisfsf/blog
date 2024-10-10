ambiente = 'teste' #teste ou produção

if ambiente == 'teste':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'

if ambiente == 'producao':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'lf7fogaca.mysql.pythonanywhere-services.com'
    DB_USER = 'lf7fogaca'
    DB_PASSWORD = 'luisteste'
    DB_NAME = 'lf7fogaca$default'

#CONFIG CHAVE SECRETA DA SESSÃO
SECRET_KEY = 'blog'

#SENHA DO ADM
MASTER_EMAIL = 'luis@email.com'
MASTER_PASSWORD = 'luisteste'