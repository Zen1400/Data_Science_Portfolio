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
        
6) #22, the syntax to use SUM(CASE.......END) AS col_name

7) #24, instead of creating a column or CTE I used :
                                                        ROW_NUMBER() OVER(PARTITION BY TO_CHAR(measurement_time, 'DD-MM-YYYY')
                                                  Also ;   Date_Trunc('day', measurement_time)   will give the time as 00:00:00  at the end
                                                  