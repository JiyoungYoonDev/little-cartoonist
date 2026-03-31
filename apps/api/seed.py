"""Seed database with initial teachers and themes."""
import asyncio

from sqlalchemy import select

from app.core.database import async_session
from app.models.teacher import TeacherCharacter
from app.models.theme import Theme

TEACHERS = [
    {
        "code": "rabbit",
        "name": "Momo Rabbit",
        "animal_type": "rabbit",
        "personality_summary": "Gentle and encouraging",
        "voice_style": "soft, warm",
    },
    {
        "code": "dog",
        "name": "Bobo Dog",
        "animal_type": "dog",
        "personality_summary": "Playful and cheerful",
        "voice_style": "excited, upbeat",
    },
    {
        "code": "panda",
        "name": "Pipi Panda",
        "animal_type": "panda",
        "personality_summary": "Calm and thoughtful",
        "voice_style": "slow, thoughtful",
    },
    {
        "code": "fox",
        "name": "Fifi Fox",
        "animal_type": "fox",
        "personality_summary": "Creative storyteller",
        "voice_style": "dramatic, expressive",
    },
]

THEMES = [
    {"code": "animals", "name": "Animals", "description": "Draw your favorite animals"},
    {"code": "space", "name": "Space Adventure", "description": "Rockets, planets, and stars"},
    {"code": "ocean", "name": "Under the Sea", "description": "Fish, whales, and ocean life"},
    {"code": "fairy_tale", "name": "Fairy Tale", "description": "Castles, dragons, and magic"},
    {"code": "my_day", "name": "My Day", "description": "Draw about your day"},
    {"code": "free", "name": "Free Drawing", "description": "Draw anything you want"},
]


async def seed():
    async with async_session() as db:
        # Seed teachers
        for t in TEACHERS:
            result = await db.execute(
                select(TeacherCharacter).where(TeacherCharacter.code == t["code"])
            )
            if not result.scalar_one_or_none():
                db.add(TeacherCharacter(**t))
                print(f"  Added teacher: {t['name']}")
            else:
                print(f"  Skipped teacher (exists): {t['name']}")

        # Seed themes
        for t in THEMES:
            result = await db.execute(
                select(Theme).where(Theme.code == t["code"])
            )
            if not result.scalar_one_or_none():
                db.add(Theme(**t))
                print(f"  Added theme: {t['name']}")
            else:
                print(f"  Skipped theme (exists): {t['name']}")

        await db.commit()
        print("\nSeed complete!")


if __name__ == "__main__":
    asyncio.run(seed())
