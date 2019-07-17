create view monokuma.vw_talents AS select
c.first_name, c.last_name, m.english_name as game_name, monokuma.talents.talent, monokuma.talents.spoiler
from monokuma.talents
inner join monokuma.characters c on monokuma.talents.character_id = c.id
inner join monokuma.media m on monokuma.talents.media_id = m.id;
