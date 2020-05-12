Select 
From
Where
group by
having
order by


--This is transactions by cardholder
Select "Name_cardholder", t.* 
From "transaction" t
inner join credit_card cc on t."card_#"=cc."card_#"
inner join card_holder ch on cc.cardholder_id=ch.cardholder_id;

--The top 100 highest transactions between 7:00 and 9:00
Select *
From "transaction" t
where extract(hour from "Date_Time_stamp") between 7 and 8 
order by "Amount" desc 
limit 100;
--Transactions 1 thru 7 appear suspicious b/c of large  dollar amounts during the time frame; 
--amounts are larger than typically spent on meals during that time, does not follow typical pattern;

Select * From transaction where "Amount" <=2;


Select "card_#", count(*) From transaction where "Amount" <=2 group by "card_#";

Select "card_#", count(*) From transaction where "Amount" <=2 group by "card_#" order by count(*) desc;

--17 tranactions under $2 is suspiciously high

Select "merchant_id", count(*) From transaction where "Amount" <=2 group by "merchant_id" order by count(*) desc;

Select t."merchant_id", count(*) From transaction t inner join merchant m on t."merchant_id" = m."merchant_id"
where "Amount" <=2 group by t."merchant_id" order by count(*) desc;

SELECT * FROM card_holder ch WHERE cardholder_id = 2 or cardholder_id = 18

SELECT ch.cardholder_id AS cardholder, t."Date_Time_stamp" AS hour, t."Amount"
        FROM transaction AS t
        JOIN credit_card AS cc ON cc."card_#" = t."card_#"
        JOIN card_holder AS ch ON ch.cardholder_id = cc.cardholder_id
        WHERE ch.cardholder_id in (2, 18);

SELECT date_part('month', t."Date_Time_stamp"), t."Amount", t."Date_Time_stamp" 
FROM transaction as t JOIN credit_card AS cc ON cc."card_#" = t."card_#"
WHERE cc.cardholder_id in (25)
and t."Date_Time_stamp" between '01/01/2018' and '06/30/2018'