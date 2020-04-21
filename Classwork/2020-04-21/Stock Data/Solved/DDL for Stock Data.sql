drop table if exists stock_data;

create table stock_data (
	stock_data_id serial not null primary key,
	stock_ticker varchar(10) not null,
	close_date date not null,
	open float,
	high float,
	low float,
	close float,
	volume bigint
);

create unique index stock_data_uq
on stock_data(stock_ticker, close_date);

alter table stock_data
add constraint stock_data_uq 
unique using index stock_data_uq;

