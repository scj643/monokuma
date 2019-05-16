import asyncpg
import os


async def get_character(name):
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch(
        "select first_name, last_name, gender, t.talent as talent , kanji from monokuma.characters "
        "left join monokuma.talents t on characters.id = t.character_id "
        "where first_name ilike $1::text or last_name ilike $1::text and t.spoiler = false",
        name)
    await conn.close()
    return results


async def get_character_media(name):
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch(
        "select first_name, last_name, gender, m.english_name as media_name "
        "from monokuma.appearances a "
        "inner join monokuma.characters c on a.character_id = c.id "
        "inner join monokuma.media m on a.media_id = m.id "
        "inner join monokuma.talents t on c.id = t.character_id "
        "where c.first_name ilike $1::text or c.last_name ilike $1::text and a.primary_media = true "
        "and t.spoiler = false",
        name)
    await conn.close()
    return results


async def list_characters():
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch(
        "select first_name, last_name from monokuma.characters")
    await conn.close()
    return results


async def get_db():
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch("select current_database();")
    await conn.close()
    return results
