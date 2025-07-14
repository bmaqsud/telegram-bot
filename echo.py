from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, Dispatcher
from settings import TOKEN

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Assalomu alaykum')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('sizga nima yordam kerak!')

def echo_text(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def echo_photo(update: Update, context: CallbackContext):
    update.message.reply_photo(update.message.photo[-1].file_id)

def echo_video(update: Update, context: CallbackContext):
    update.message.reply_video(update.message.video.file_id)

def echo_voice(update: Update, context: CallbackContext):
    update.message.reply_voice(update.message.voice.file_id)

def echo_audio(update: Update, context: CallbackContext):
    update.message.reply_audio(update.message.audio.file_id)

def echo_document(update: Update, context: CallbackContext):
    update.message.reply_document(update.message.document.file_id)

def echo_sticker(update: Update, context: CallbackContext):
    update.message.reply_sticker(update.message.sticker.file_id)

def echo_location(update: Update, context: CallbackContext):
    update.message.reply_location(update.message.location)

def echo_contact(update: Update, context: CallbackContext):
    update.message.reply_contact(update.message.contact.file_id)

def echo_animation(update: Update, context: CallbackContext):
    update.message.reply_animation(update.message.animation.file_id)

def main():
    updater=Updater(TOKEN)

    dispatcher: Dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, echo_text))
    dispatcher.add_handler(MessageHandler(Filters.photo, echo_photo))
    dispatcher.add_handler(MessageHandler(Filters.video, echo_video))
    dispatcher.add_handler(MessageHandler(Filters.voice, echo_voice))
    dispatcher.add_handler(MessageHandler(Filters.audio, echo_audio))
    dispatcher.add_handler(MessageHandler(Filters.document, echo_document))
    dispatcher.add_handler(MessageHandler(Filters.location, echo_location))
    dispatcher.add_handler(MessageHandler(Filters.contact, echo_contact))
    dispatcher.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dispatcher.add_handler(MessageHandler(Filters.animation, echo_animation))

    updater.start_polling()

    updater.idle()

if __name__=='__main__':
    main()

