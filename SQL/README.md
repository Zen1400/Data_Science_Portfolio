Here I write SQL problems that I've solved and keep notes of what concepts were difficult to practice them more on the future

NOTE :

1) In exercise number 8, I spent some time to figure out that you should use AS only once when combining SUM(CASE)
   ex :  SUM( CASE
                  WHEN     THEN  
                  END) AS col_name
                 
2) In exercise 11, remember to seperate With tables with commas except the last one before SELECT, 
                  and no need to write WITH again, start directly with name AS

3) In exercise 13, Columns Aliases are disallowed in WHERE and CASE

4) Excercise 14, DATE(TIMESTAMP_column) to get time from a timestamp column, and BETWEEN "2010-09-10" AND "2010-09-18"   DONT forget quotes

5) #18, I learnt that you don't have to join With tables, you can just FROM w_1, w_2
        Also,  to get the division in decimal  num_1::decimal / num_2