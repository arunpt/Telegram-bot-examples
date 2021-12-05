import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, Filters, CallbackContext, ChatJoinRequestHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

BOT_TOKEN = ''

def start(update: Update, ctx: CallbackContext) -> None:
    update.message.reply_text('Hi!')

def approve_user(update: Update, ctx: CallbackContext) -> None:
    ctx.bot.approve_chat_join_request(
        chat_id=update.effective_chat.id,
        user_id=update.effective_user.id
    )

def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(ChatJoinRequestHandler(approve_user))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
