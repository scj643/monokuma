import asyncpg
import os


async def get_character(name):
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch(
        "select first, last, gender, talent, kanji from monokuma.characters "
        "where first ilike $1::text or last ilike $1::text",
        name)
    await conn.close()
    return results


async def get_character_media(name):
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch(
        "select first_name, last_name, gender, talent, m.english_name as media_name "
        "from monokuma.appearances a "
        "inner join monokuma.characters c on a.character_id = c.id "
        "inner join monokuma.media m on a.media_id = m.id "
        " where c.first_name ilike $1::text or c.last_name ilike $1::text and a.primary_media = true",
        name)
    await conn.close()
    return results


async def list_characters():
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch(
        "select first, last from monokuma.characters")
    await conn.close()
    return results
