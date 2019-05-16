-- Characters table
CREATE TABLE monokuma.characters
(
    id             serial NOT NULL primary key,
    first_name     varchar(40),
    last_name      varchar(40),
    gender         varchar(10),
    talent         varchar(255),
    spoiler_talent varchar(255),
    height         smallint,
    birth_month    smallint,
    birth_day      smallint,
    chest          smallint,
    weight         smallint,
    kanji          varchar(10),
    sprite_url     varchar(1024)
);

COMMENT ON COLUMN monokuma.characters.first_name IS 'First Name';
COMMENT ON COLUMN monokuma.characters.last_name IS 'Last Name';
COMMENT ON COLUMN monokuma.characters.height IS 'Height in centimeters';
COMMENT ON COLUMN monokuma.characters.chest IS 'Chest size in centimeters';
COMMENT ON COLUMN monokuma.characters.weight IS 'Weight in kilograms';
COMMENT ON COLUMN monokuma.characters.spoiler_talent IS 'Talent that is a spoiler in the media';


CREATE TABLE monokuma.media
(
    id              serial NOT NULL PRIMARY KEY,
    english_name    varchar(255),
    jp_name         varchar(255),
    us_release_date date,
    jp_release_date date,
    media_type      varchar(20) DEFAULT 'game'::varchar(20),
    cover_url       varchar(1024)
);


-- Appearances table
-- Character IDs are mapped to the media that they appear in

CREATE TABLE monokuma.appearances
(
    character_id  smallint
        constraint appearances_characters_id_fk
            references monokuma.characters,
    media_id      smallint
        constraint appearances_media_id_fk
            references monokuma.media,
    spoiler       boolean DEFAULT false,
    primary_media boolean DEFAULT true
);


-- Information on the chapters in the games
CREATE TABLE monokuma.chapters
(
    id       serial NOT NULL PRIMARY KEY,
    media_id smallint
        constraint chapters_media_id_fk
            references monokuma.media,
    name     varchar(256),
    number   smallint
);
COMMENT ON COLUMN monokuma.chapters.number IS 'Numbering starts at 0 for prologue';

CREATE TABLE monokuma.murders
(
    murderer_id smallint
        constraint murderer_characters_id_fk
            references monokuma.characters,
    murdered_id smallint
        constraint murdered_characters_id_fk
            references monokuma.characters,
    media_id    smallint
        constraint murder_media_id_fk
            references monokuma.media,
    chapter_id  smallint
        constraint murder_chapter_id_fk
            references monokuma.chapters
);

CREATE TABLE monokuma.quotes
(
    id           serial NOT NULL PRIMARY KEY,
    character_id smallint
        constraint quotes_character_id_fk
            references monokuma.characters,
    media_id     smallint
        constraint quotes_media_id_fk
            references monokuma.media,
    quote        text,
    spoiler      bool default TRUE,
    chapter_id   smallint
        constraint quotes_chapter_id_fk
            references monokuma.chapters
);

CREATE TABLE monokuma.talents
(
    character_id smallint
        constraint talents_character_id_fk
            references monokuma.characters,
    talent       varchar(40),
    spoiler      bool default false,
    media_id     smallint
        constraint talents_media_id_fk
            references monokuma.media
)