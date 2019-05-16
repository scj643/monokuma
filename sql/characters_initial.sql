with data (first_name, last_name, gender, height, birth_month, birth_day, chest, weight, kanji)
         as (
        VALUES ('Chiaki', 'Nanami', 'Female', 160, 3, 14, 88, 46, '七海 千秋'),
               ('Toko', 'Fukawa', 'Female', 165, 3, 3, 79, 47, '腐川 冬子'),
               ('Hajime', 'Hinata', 'Male', 179, 1, 1, 91, 67, '日向 創'),
               ('Mikan', 'Tsumiki', 'Female', 165, 5, 12, 89, 57, '罪木 蜜柑'),
               ('Kokichi', 'Oma', 'Male', 156, 6, 21, 70, 44, '王馬 小吉'),
               ('Kyoko', 'Kirigiri', 'Female', 167, 10, 6, 82, 48, '霧切 響子'),
               ('Makoto', 'Naegi', 'Male', 160, 2, 5, 75, 52, '苗木 誠'),
               ('Junko', 'Enoshima', 'Female', 169, 12, 24, 90, 45, '江ノ島 盾子')
    )
INSERT
INTO monokuma.characters (first_name, last_name, gender, height, birth_month, birth_day, chest, weight, kanji)
select *
from data d
where not exists(select 1
                 from monokuma.characters
                 where d.first_name = monokuma.characters.first_name
                   and d.last_name = monokuma.characters.last_name);