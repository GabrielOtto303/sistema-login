create table if not exists usuarios(id integer primary key auto_increment,
							usuario  varchar(255)unique,
							senha varchar(255));