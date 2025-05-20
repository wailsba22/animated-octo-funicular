import random
import asyncio
from datetime import datetime, timedelta
from telegram import Bot
from telegram.ext import ApplicationBuilder

BOT_TOKEN = '7526799568:AAGI-xF6clTfWuUDm5yfVCFsx4U-v6adBbs'  # Replace with your bot token
CHAT_ID = 5091229212  # Replace with your chat ID as integer

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

async def send_daily_workout(bot: Bot):
    workout = random.sample(EXERCISES, 3)
    message = "🏋️‍♂️ Today's Home Workout:\n\n" + "\n".join(f"- {ex}" for ex in workout)
    await bot.send_message(chat_id=CHAT_ID, text=message)

async def schedule_daily(app):
    while True:
        now_dt = datetime.now()
        target = now_dt.replace(hour=5, minute=0, second=0, microsecond=0)
        if now_dt > target:
            target += timedelta(days=1)
        wait_seconds = (target - now_dt).total_seconds()
        await asyncio.sleep(wait_seconds)
        await send_daily_workout(app.bot)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.create_task(schedule_daily(app))
    print("Bot started, waiting to send daily workouts at 5 AM...")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
