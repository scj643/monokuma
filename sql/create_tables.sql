--
-- Name: appearances; Type: TABLE; Schema: monokuma; Owner: scj643
--

CREATE TABLE monokuma.appearances (
    character_id integer,
    media_id integer,
    spoiler boolean DEFAULT false,
    primary_media boolean DEFAULT true
);


--
-- Name: characters; Type: TABLE; Schema: monokuma; Owner: scj643
--

CREATE TABLE monokuma.characters (
    id integer NOT NULL,
    first character varying(40),
    last character varying(40),
    gender character varying(10),
    talent character varying(64),
    height smallint,
    birth_month smallint,
    birth_day smallint,
    chest smallint,
    weight smallint,
    kanji character varying(10)
);


--
-- Name: COLUMN characters.first; Type: COMMENT; Schema: monokuma; Owner: scj643
--

COMMENT ON COLUMN monokuma.characters.first IS 'First Name';


--
-- Name: COLUMN characters.last; Type: COMMENT; Schema: monokuma; Owner: scj643
--

COMMENT ON COLUMN monokuma.characters.last IS 'Last Name';


--
-- Name: COLUMN characters.height; Type: COMMENT; Schema: monokuma; Owner: scj643
--

COMMENT ON COLUMN monokuma.characters.height IS 'Height in centimeters';


--
-- Name: COLUMN characters.chest; Type: COMMENT; Schema: monokuma; Owner: scj643
--

COMMENT ON COLUMN monokuma.characters.chest IS 'Chest size in centimeters
';


--
-- Name: COLUMN characters.weight; Type: COMMENT; Schema: monokuma; Owner: scj643
--

COMMENT ON COLUMN monokuma.characters.weight IS 'Weight in killograms';


--
-- Name: characters_id_seq; Type: SEQUENCE; Schema: monokuma; Owner: scj643
--

CREATE SEQUENCE monokuma.characters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: characters_id_seq; Type: SEQUENCE OWNED BY; Schema: monokuma;
--

ALTER SEQUENCE monokuma.characters_id_seq OWNED BY monokuma.characters.id;


--
-- Name: media; Type: TABLE; Schema: monokuma;
--

CREATE TABLE monokuma.media (
    id integer NOT NULL,
    english_name character varying(255),
    jp_name character varying(255),
    us_release_date date,
    jp_release_date date,
    media_type character varying(20) DEFAULT 'game'::character varying
);


--
-- Name: games_id_seq; Type: SEQUENCE; Schema: monokuma;
--

CREATE SEQUENCE monokuma.games_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: games_id_seq; Type: SEQUENCE OWNED BY; Schema: monokuma;
--

ALTER SEQUENCE monokuma.games_id_seq OWNED BY monokuma.media.id;


--
-- Name: characters id; Type: DEFAULT; Schema: monokuma;
--

ALTER TABLE ONLY monokuma.characters ALTER COLUMN id SET DEFAULT nextval('monokuma.characters_id_seq'::regclass);


--
-- Name: media id; Type: DEFAULT; Schema: monokuma; Owner: scj643
--

ALTER TABLE ONLY monokuma.media ALTER COLUMN id SET DEFAULT nextval('monokuma.games_id_seq'::regclass);



--
-- Name: characters characters_pk; Type: CONSTRAINT; Schema: monokuma; Owner: scj643
--

ALTER TABLE ONLY monokuma.characters
    ADD CONSTRAINT characters_pk PRIMARY KEY (id);


--
-- Name: media games_pk; Type: CONSTRAINT; Schema: monokuma; Owner: scj643
--

ALTER TABLE ONLY monokuma.media
    ADD CONSTRAINT games_pk PRIMARY KEY (id);


--
-- Name: characters_id_uindex; Type: INDEX; Schema: monokuma; Owner: scj643
--

CREATE UNIQUE INDEX characters_id_uindex ON monokuma.characters USING btree (id);


--
-- Name: games_id_uindex; Type: INDEX; Schema: monokuma; Owner: scj643
--

CREATE UNIQUE INDEX games_id_uindex ON monokuma.media USING btree (id);


--
-- Name: appearances appearances_characters_id_fk; Type: FK CONSTRAINT; Schema: monokuma; Owner: scj643
--

ALTER TABLE ONLY monokuma.appearances
    ADD CONSTRAINT appearances_characters_id_fk FOREIGN KEY (character_id) REFERENCES monokuma.characters(id);


--
-- Name: appearances appearances_media_id_fk; Type: FK CONSTRAINT; Schema: monokuma; Owner: scj643
--

ALTER TABLE ONLY monokuma.appearances
    ADD CONSTRAINT appearances_media_id_fk FOREIGN KEY (media_id) REFERENCES monokuma.media(id);


--
-- PostgreSQL database dump complete
--

