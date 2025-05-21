
import logging
import os
import pandas as pd
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Ativa o log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Carrega a planilha
df = pd.read_excel("Pedidos.xlsx")
df["Código"] = df["Código"].astype(str)

# Mensagem de boas-vindas
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Envie o código do pedido para consultar o status.")

# Consulta o código do pedido
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()
    today = pd.Timestamp.now().normalize()
    result = df[df["Código"] == user_input]

    if not result.empty:
        pedido_hoje = result[result["Data"].dt.normalize() == today]
        if not pedido_hoje.empty:
            row = pedido_hoje.iloc[0]
            response = f'O {row["Código"]} - {row["Cliente"]} tem pedido para hoje {row["Data"].strftime("%d/%m/%Y")} e o veículo está com o seguinte status: {row["Status"]}. O motorista é o {row["Motorista"]} e o contato é {row["Telefone Motorista"]}. Caso precise contactar o vendedor o contato é {row["Contato Vendedor"]}.'
        else:
            row = result.iloc[0]
            response = f'O {row["Código"]} - {row["Cliente"]} NÃO tem pedido para hoje {today.strftime("%d/%m/%Y")}. Caso precise contactar o vendedor o contato é {row["Contato Vendedor"]}.'
    else:
        response = "Código não encontrado. Verifique se digitou corretamente."

    await update.message.reply_text(response)

# Função principal
def main():
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
