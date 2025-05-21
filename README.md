
# Bot de Consulta de Pedido

Este bot do Telegram permite que usuários consultem o status de um pedido enviando o código do pedido.

## Como usar

1. Envie o código do pedido para o bot.
2. O bot responderá com o status e dados do motorista/vendedor se houver pedido para hoje.

## Deploy no Render

1. Suba os arquivos no GitHub.
2. Crie um novo serviço no Render (tipo Web Service).
3. Adicione a variável de ambiente `BOT_TOKEN` com o token do BotFather.
4. O bot usará polling por padrão.

---

Desenvolvido com Python e python-telegram-bot.
