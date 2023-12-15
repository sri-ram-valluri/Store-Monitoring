create table store_status_seq (next_val bigint) engine=InnoDB;
insert into store_status_seq values ( 1 );
create table store_status (store_id bigint not null, status varchar(255), timestamp_utc varchar(255), primary key (store_id)) engine=InnoDB;
create table store_status_seq (next_val bigint) engine=InnoDB;
insert into store_status_seq values ( 1 );
create table store_status (store_id bigint not null, status varchar(255), timestamp_utc varchar(255), primary key (store_id)) engine=InnoDB;
