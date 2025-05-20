import random


from datetime import datetime, time as dtime
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    JobQueue,
)

BOT_TOKEN = '7526799568:AAGI-xF6clTfWuUDm5yfVCFsx4U-v6adBbs'
CHAT_ID = 5091229212

EXERCISES = [
    "Push-ups - 10 reps",
    "Squats - 15 reps",
    "Plank - 30 seconds",
    "Glute Bridges - 15 reps",
    "Lunges - 10 reps each leg",
    "Sit-ups - 15 reps",
    "Wall Sit - 30 seconds",
    "Leg Raises - 15 reps",
    "Superman Hold - 30 seconds",
    "Bird Dog - 10 reps each side",
    "Calf Raises - 15 reps",
    "Side Plank - 20 seconds each side"
]

async def send_daily_workout(context: ContextTypes.DEFAULT_TYPE):
    workout = random.sample(EXERCISES, 3)
    message = "🏋️‍♂️ Today's Home Workout:\n\n" + "\n".join(f"- {ex}" for ex in workout)
    await context.bot.send_message(chat_id=CHAT_ID, text=message)

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(f"🕒 Current time: {now}")

async def name_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Your name is Wail!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()


    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("name", name_command))

    # Schedule daily workout at 5:00 AM server time
    job_queue: JobQueue = app.job_queue
    job_queue.run_daily(send_daily_workout, time=dtime(hour=5, minute=0))

    print("Bot started and running...")
    app.run_polling()

if __name__ == "__main__":
    main()
