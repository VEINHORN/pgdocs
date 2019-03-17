-- Table: public.client

-- DROP TABLE public.client;

CREATE TABLE public.client
(
    id bigint NOT NULL,
    name character varying COLLATE pg_catalog."default",
    address character varying COLLATE pg_catalog."default",
    CONSTRAINT client_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.client
    OWNER to veinhorn;
COMMENT ON TABLE public.client
    IS 'Contains all client info.';

COMMENT ON COLUMN public.client.id
    IS 'Client unique identifier.';

COMMENT ON COLUMN public.client.name
    IS 'Contains client name.';

COMMENT ON COLUMN public.client.address
    IS 'Contains client address.';

-- Index: idx_name

-- DROP INDEX public.idx_name;

CREATE INDEX idx_name
    ON public.client USING btree
    (name COLLATE pg_catalog."default")
    TABLESPACE pg_default;

COMMENT ON INDEX public.idx_name
    IS 'Index for client name.';


-- View: public.most_active_clients

-- DROP VIEW public.most_active_clients;

CREATE OR REPLACE VIEW public.most_active_clients AS
 SELECT client.id,
    client.name,
    client.address
   FROM client;

ALTER TABLE public.most_active_clients
    OWNER TO veinhorn;
COMMENT ON VIEW public.most_active_clients
    IS 'Show top 5 most active clients.';


