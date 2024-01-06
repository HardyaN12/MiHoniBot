import logging
import time
import asyncio
from typing import List
from telegram import *
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, WebAppInfo, Message, InputFile
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

import asyncio
from typing import List
from telegram import Message, Update, InputFile

async def delete_messages_after_delay(messages: List[Message], delay: int) -> None:
    """Eliminar todos los mensajes después de un cierto período de tiempo."""
    await asyncio.sleep(delay)
    
    # Mantén solo el último mensaje
    last_message = messages[-1]

    # Elimina todos los mensajes anteriores
    for message in messages[:-1]:
        await message.delete()

    # Elimina el último mensaje después de otro periodo de tiempo
    await asyncio.sleep(delay)
    await last_message.delete()

async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Enviar mensaje de bienvenida y actualizar después de 3 segundos."""
    # Verificar si el comando se ejecuta en un grupo
    if update.message.chat.type == "group" or update.message.chat.type == "supergroup":
        # Enviar el primer mensaje de bienvenida
        mensaje1 = await update.message.reply_text("Hola, soy Anthoni 😼")

        # Esperar 3 segundos
        await asyncio.sleep(3)

        # Obtener el ID del mensaje y actualizar con el segundo mensaje de bienvenida
        mensaje2 = await update.message.reply_text("Hola, soy Yezz 💋")

        # Mantener una lista de los mensajes enviados
        mensajes_enviados = [mensaje1, mensaje2]

        # Eliminar todos los mensajes anteriores después de 3 segundos
        await delete_messages_after_delay(mensajes_enviados, 0.5)





async def horarios(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with a button that opens the web app or provides a link."""
    if update.message.chat.type == "private":
        # For private chats, use the web app button
        await update.message.reply_text(
            "Por favor, presiona el botón para abrir la página de horarios de eventos en Sky:",
            reply_markup=ReplyKeyboardMarkup.from_button(
                KeyboardButton(
                    text="Abrir horarios!",
                    web_app=WebAppInfo(url="https://sky-clock.netlify.app/"),
                )
            ),
        )
        
        # Send a sticker as a response
        sticker_id = "CAACAgIAAxkBAREuFGWZsGzVqtyGL8OCNsqbLgcBrb24AALsJgACCUHxSVSfLuPPtzxVNAQ"  # Reemplaza con el ID real de tu sticker
        await update.message.reply_sticker(sticker=sticker_id)

    else:
        # For groups, provide a link
        await update.message.reply_text("Puedes abrir la página de horarios de eventos en Sky con el enlace proporcionado:\n"
                                       "https://sky-clock.netlify.app/")
       
        # Send a sticker as a response
        sticker_id = "CAACAgIAAxkBAREuFGWZsGzVqtyGL8OCNsqbLgcBrb24AALsJgACCUHxSVSfLuPPtzxVNAQ"  # Reemplaza con el ID real de tu sticker
        await update.message.reply_sticker(sticker=sticker_id)
        

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("6612802958:AAFSrvJTTcmLj--c7vlWiwvNMCTKB5Gv-sQ").build()

    application.add_handler(CommandHandler("horarios", horarios))
    application.add_handler(CommandHandler("bienvenida", bienvenida))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
