-- using sql functions to make inserting in bulk easier

CREATE OR REPLACE FUNCTION get_character_talent(in_first_name varchar(40), in_last_name varchar(40),
                                                in_media_name varchar(255), in_talent_name varchar(40),
                                                is_spoiler bool default false) RETURNS TABLE
                                                                                       (
                                                                                           character_id int,
                                                                                           talent       varchar(40),
                                                                                           spoiler      bool,
                                                                                           media_id     int
                                                                                       ) AS
$$
BEGIN
    RETURN QUERY
        with char_media_id as (
            select id, 1 as n
            from monokuma.media
            where english_name = in_media_name
        )
        select monokuma.characters.id,
               -- get the media id
               in_talent_name,
               is_spoiler,
               first_value(cm.id) over (PARTITION BY cm.id) as media_id
        from monokuma.characters
                 inner join char_media_id cm on 1 = cm.n
        where first_name = in_first_name
          and last_name = in_last_name;
end;
$$ language plpgsql;

with dr1 as (
    select *
    from get_character_talent('Kyoko', 'Kirigiri', 'Danganronpa: Trigger Happy Havoc', 'Ultimate ???', false)
    union
    select *
    from get_character_talent('Kyoko', 'Kirigiri', 'Danganronpa: Trigger Happy Havoc', 'Ultimate Detective', true)
    union
    select *
    from get_character_talent('Toko', 'Fukawa', 'Danganronpa: Trigger Happy Havoc', 'Ultimate Writing Prodigy', false)
    union
    select *
    from get_character_talent('Makoto', 'Naegi', 'Danganronpa: Trigger Happy Havoc', 'Ultimate Lucky Student', false)
    union
    select *
    from get_character_talent('Makoto', 'Naegi', 'Danganronpa: Trigger Happy Havoc', 'Ultimate Hope', true)
    union
    select *
    from get_character_talent('Junko', 'Enoshima', 'Danganronpa: Trigger Happy Havoc', 'Ultimate Fashionista', false)
    union
    select *
    from get_character_talent('Junko', 'Enoshima', 'Danganronpa: Trigger Happy Havoc', 'Ultimate Despair', true)
)
insert
into talents
select *
from dr1
where not exists(select *
                 from monokuma.talents
                 where character_id = dr1.character_id
                   and talent = dr1.talent
                   and media_id = dr1.media_id);


