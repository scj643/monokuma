create view monokuma.vw_appearances AS select
c.first_name, c.last_name, m.english_name
from monokuma.appearances
inner join monokuma.characters c on monokuma.appearances.character_id = c.id
inner join monokuma.media m on monokuma.appearances.media_id = m.id;

insert into monokuma.vw_appearances (first, last, english_name)
VALUES