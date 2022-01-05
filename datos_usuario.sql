BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "datos_usuario" (
	"usuario"	TEXT NOT NULL UNIQUE,
	"contrasena"	TEXT NOT NULL,
	PRIMARY KEY("usuario")
);
INSERT INTO "datos_usuario" VALUES ('spyder_23_man','S29tw@/31');
INSERT INTO "datos_usuario" VALUES ('secretmen85','185Ws+ln');
COMMIT;
