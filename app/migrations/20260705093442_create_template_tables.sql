-- +goose Up
CREATE TABLE IF NOT EXISTS public."Templates" (
    "Id" UUID PRIMARY KEY,
    "Name" VARCHAR(200) NOT NULL,
    "CreatedTimestamp" TIMESTAMPTZ NOT NULL DEFAULT now(),
    "UpdatedTimestamp" TIMESTAMPTZ NOT NULL DEFAULT now(),
    "Deleted" BOOLEAN NOT NULL DEFAULT FALSE
);

-- +goose Down
DROP TABLE IF EXISTS public."Templates"
