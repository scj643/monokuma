-- using sql functions to make inserting in bulk easier

CREATE OR REPLACE FUNCTION get_character_appearance(in_first_name varchar(40), in_last_name varchar(40),
                                                    in_media_name varchar(255), is_spoiler bool default false,
                                                    is_primary bool default true) RETURNS TABLE
                                                                                          (
                                                                                              character_id  int,
                                                                                              media_id      int,
                                                                                              spoiler       bool,
                                                                                              primary_media bool
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
               first_value(cm.id) over (PARTITION BY cm.id) as media_id,
               is_spoiler,
               is_primary
        from monokuma.characters
                 inner join char_media_id cm on 1 = cm.n
        where first_name = in_first_name
          and last_name = in_last_name;
end;
$$ language plpgsql;

CREATE OR REPLACE FUNCTION get_character_appearance(names varchar(40)[][],
                                                    in_media_name varchar(255), is_spoiler bool default false,
                                                    is_primary bool default true) RETURNS TABLE
                                                                                          (
                                                                                              character_id  int,
                                                                                              media_id      int,
                                                                                              spoiler       bool,
                                                                                              primary_media bool
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
               first_value(cm.id) over (PARTITION BY cm.id) as media_id,
               is_spoiler,
               is_primary
        from monokuma.characters
                 inner join char_media_id cm on 1 = cm.n
        where first_name = any (names)
          and last_name = any (names);
end;
$$ language plpgsql;

-- add Danganronpa 1 character appearances
with dr1 as (
    select *
    from get_character_appearance(array [['Kyoko', 'Kirigiri'], ['Toko', 'Fukawa'], ['Makoto', 'Naegi']],
                                  'Danganronpa: Trigger Happy Havoc')
)
INSERT INTO monokuma.appearances
select * from dr1
where not exists(select * from monokuma.appearances where character_id = dr1.character_id and media_id = dr1.media_id)
;