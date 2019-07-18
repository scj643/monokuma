import asyncpg
import os


async def get_character(name):
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch(
        "select first_name, last_name, gender, t.talent as talent , kanji from monokuma.char_info_character "
        "left join monokuma.char_info_talent t on char_info_character.id = t.character_id "
        "where first_name ilike $1::text or last_name ilike $1::text and t.spoiler = false",
        name)
    await conn.close()
    return results


async def get_character_media(name):
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch(
        "select first_name, last_name, gender, m.english_name as media_name "
        "from monokuma.char_info_appearance a "
        "inner join monokuma.char_info_character c on a.character_id = c.id "
        "inner join monokuma.char_info_media m on a.media_id = m.id "
        "inner join monokuma.char_info_talent t on c.id = t.character_id "
        "where c.first_name ilike $1::text or c.last_name ilike $1::text and a.primary_media = true "
        "and t.spoiler = false",
        name)
    await conn.close()
    return results


async def get_character_next_bday(name):
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch("""select 
    CASE
    -- check when the next occurrence is this year
    WHEN birth_month >= extract(month from now()) AND birth_day > extract(day from now())
        then first_name || ' ' || last_name || ' birthday is in ' || 
        make_date(extract(year from now())::int, birth_month, birth_day) - now()
    WHEN birth_month > extract(month from now()) AND birth_day < extract(day from now())
        then first_name || ' ' || last_name || ' birthday is in ' || 
        make_date(extract(year from now())::int, birth_month, birth_day) - now()
    WHEN birth_month = extract(month from now()) AND birth_day = extract(day from now())
    THEN first_name || ' ' || last_name || ' birthday is today!!!!'
    ELSE
    first_name || ' ' || last_name || ' birthday is in ' || 
        make_date(extract(year from now())::int + 1::int, birth_month, birth_day) - now()
    END
    from monokuma.char_info_character c
    where c.first_name ilike $1::text or c.last_name ilike $1::text;
    """, name)
    await conn.close()
    return results


async def list_characters():
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch(
        "select first_name, last_name from monokuma.char_info_character")
    await conn.close()
    return results


async def get_db():
    conn = await asyncpg.connect(os.environ.get('PG_CONNECTION'))
    results = await conn.fetch("select current_database();")
    await conn.close()
    return results
