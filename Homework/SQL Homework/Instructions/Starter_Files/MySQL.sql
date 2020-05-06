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
--Transactions 1 thru 7 appear suspicious b/c of amount during the time frame

