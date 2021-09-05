#!/usr/bin/env python3
import os
import logging
from uuid import uuid4
from pokedex import pokedex
from configparser import ConfigParser
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'Utils/Config/config.ini')
config = ConfigParser()
config.read(initfile)

TOKEN = config.get('telegram_bot',"token")

# Enable logging
logging.basicConfig( format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query

    if query == "":
        return

    pokemones = []

    search = pokedex(query)

    if "error" in search:
        logger.error(search["error"])
        response = search["error"]
    else:
        if isinstance(search,list):
            for element in search:
                pokemones.append(
                        InlineQueryResultArticle(
                            id=str(uuid4()),
                            title=element["name"],
                            thumb_url=element["image"],
                            description=element["type"],
                            input_message_content=InputTextMessageContent(
                                "Name: " + element["name"] + " (#"+ element["number"]+ 
                                ") \nType: "+ element["type"] + 
                                "\nWeight: " + element["weight"] +
                                "\nHeight: " + element["height"] + 
                                "\nAbilities: " + element["abilities"] +
                                "\nWeakness: " + element["weakness"] +
                                "\n" + element["image"]),
                        ))
        elif isinstance(search,dict):
            pokemones.append(
                        InlineQueryResultArticle(
                            id=str(uuid4()),
                            title=search["name"],
                            thumb_url=search["image"],
                            description=search["type"],
                            input_message_content=InputTextMessageContent(
                                "Name: " + search["name"] + " (#"+ search["number"]+ 
                                ") \nType: "+ search["type"] + 
                                "\nWeight: " + search["weight"] +
                                "\nHeight: " + search["height"] + 
                                "\nAbilities: " + search["abilities"] +
                                "\nWeakness: " + search["weakness"] +
                                "\n" + search["image"]),
                        ))                
    update.inline_query.answer(pokemones)

def message_response(update,context):

    text = str(update.message.text).lower()
    username = update.message.chat.first_name
    logger.info("User: "+username)
    response = ""
    if "Name: " in update.message.text:
        logger.info("Se detecto respuesta de un Query")
        response = "Waiting for a new search ..."
    else: 
        search = pokedex(text)
        if "error" in search:
            logger.error(search["error"])
            response = search["error"]
        else:
            if isinstance(search,list):
                search = search[0]
            response = "<b>Name: " + search["name"] + " (#"+ search["number"]+ ")</b> \nType: "+ search["type"] + "\nWeight: " + str(search["weight"]) +"\nHeight: " + str(search["height"]) + "\nAbilities: " + search["abilities"] +"\nWeakness: " + search["weakness"] +"\n" + search["image"]
    
    update.message.reply_text(response,parse_mode='HTML')

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(InlineQueryHandler(inlinequery))
    dispatcher.add_handler(MessageHandler(Filters.text,message_response))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()