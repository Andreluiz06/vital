# Vital - Sistema de Gestão de Exames Médicos

## Sobre o Projeto

Vital é um sistema web desenvolvido em Django para gestão de exames médicos, permitindo que pacientes e profissionais de saúde gerenciem solicitações, resultados e acesso a exames de forma segura e organizada.

## Funcionalidades Principais

### Para Pacientes
- Cadastro e login de usuários
- Solicitação de exames
- Visualização de resultados com proteção por senha
- Gerenciamento de pedidos de exames
- Acompanhamento do status dos exames

### Para Profissionais de Saúde
- Gerenciamento de clientes
- Upload e controle de resultados de exames
- Geração de senhas de acesso
- Visualização de PDFs de resultados
- Controle de status dos exames

### Para Médicos
- Acesso temporário aos exames do paciente
- Visualização de histórico de exames por período
- Link exclusivo para acesso aos resultados

## Tecnologias Utilizadas

- Django (Framework Python)
- SQLite (Banco de Dados)
- Bootstrap (Frontend)
- HTML/CSS/JavaScript
- PDF.js (Visualização de PDFs)

## Segurança

O sistema conta com:
- Autenticação de usuários
- Proteção de rotas por login
- Senhas exclusivas para exames
- Controle de acesso temporário
- Validação de permissões

## Interface

O projeto utiliza um design moderno com:
- Layout responsivo
- Tema personalizado
- Cores institucionais
- Navegação intuitiva
- Mensagens de feedback

## Estrutura do Projeto

- `usuarios/` - Gestão de usuários e autenticação
- `exames/` - Core do sistema de exames
- `empresarial/` - Área administrativa
- `templates/` - Templates HTML
- `media/` - Arquivos de exames
- `static/` - Arquivos estáticos (CSS, JS, imagens)

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual Python
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute as migrações: `python manage.py migrate`
5. Inicie o servidor: `python manage.py runserver`

## Licença

Este projeto foi desenvolvido por André Kiwi.