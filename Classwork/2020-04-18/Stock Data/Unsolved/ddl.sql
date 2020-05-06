CREATE TABLE "merchant_category" (
  "category_id" INT,
  "category" VARCHAR(25),
  PRIMARY KEY ("category_id")
);

CREATE TABLE "merchant" (
  "merchant_id" INT,
  "Owner_name" VARCHAR(150),
  "category_id" INT,
  PRIMARY KEY ("merchant_id"), 
foreign key ("category_id") references "merchant_category"("category_id")
);

CREATE TABLE "card_holder" (
  "cardholder_id" INT,
  "Name_cardholder" VARCHAR(50),
  PRIMARY KEY ("cardholder_id")
);

CREATE TABLE "credit_card" (
  "card_#" VARCHAR(50),
  "cardholder_id" INT,
  PRIMARY KEY ("card_#"),
foreign key (cardholder_id) references card_holder(cardholder_id)
);

CREATE TABLE "transaction" (
  "transaction_id" INT,
  "Date_Time_stamp" DATE,
  "Amount" INT,
  "card_#" VARCHAR(50),
  "merchant_id" INT,
  PRIMARY KEY ("transaction_id"),
foreign key ("card_#") references credit_card ("card_#"), 
foreign key (merchant_id)  references merchant(merchant_id)
);


