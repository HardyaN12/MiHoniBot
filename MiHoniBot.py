from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hola {update.effective_user.name} tembo lgm poporopopo ñembocu Luison')


app = ApplicationBuilder().token("6612802958:AAFSrvJTTcmLj--c7vlWiwvNMCTKB5Gv-sQ").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()