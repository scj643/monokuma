with data (first_name, last_name, gender, talent, height, birth_month, birth_day, chest, weight, kanji, spoiler_talent)
         as (
        VALUES ('Chiaki', 'Nanami', 'Female', 'Ultimate Gamer', 160, 3, 14, 88, 46, '七海 千秋', NULL),
               ('Toko', 'Fukawa', 'Female', 'Ultimate Writing Prodigy', 165, 3, 3, 79, 47, '腐川 冬子', NULL),
               ('Hajime', 'Hinata', 'Male', 'Ultimate ???', 179, 1, 1, 91, 67, '日向 創', 'Ultimate Hope'),
               ('Mikan', 'Tsumiki', 'Female', 'Ultimate Nurse', 165, 5, 12, 89, 57, '罪木 蜜柑', NULL),
               ('Kokichi', 'Oma', 'Male', 'Ultimate Supreme Leader', 156, 6, 21, 70, 44, '王馬 小吉', NULL),
               ('Kyoko', 'Kirigiri', 'Female', 'Ultimate ???', 167, 10, 6, 82, 48, '霧切 響子', 'Ultimate Detective'),
               ('Makoto', 'Naegi', 'Male', 'Ultimate Lucky Student', 160, 2, 5, 75, 52, '苗木 誠', NULL),
               ('Junko', 'Enoshima', 'Female', 'Ultimate Fashionista', 169, 12, 24, 90, 45, '江ノ島 盾子',
                'Ultimate Despair')
    )
INSERT
INTO monokuma.characters (first_name, last_name, gender, talent, height, birth_month, birth_day, chest, weight, kanji,
                          spoiler_talent)
select *
from data d
where not exists(select 1
                 from monokuma.characters
                 where d.first_name = monokuma.characters.first_name
                   and d.last_name = monokuma.characters.last_name);