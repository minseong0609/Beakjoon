-- 코드를 입력하세요
SELECT date_format(SALES_DATE, '%Y-%m-%d') as sales_date, PRODUCT_ID, USER_ID, SALES_AMOUNT  
from online_sale
where sales_date >= '2022-03-01' and sales_date < '2022-04-01'

union all

SELECT date_format(SALES_DATE, '%Y-%m-%d') as sales_date, PRODUCT_ID, NULL as USER_ID ,SALES_AMOUNT
from offline_sale
where sales_date >= '2022-03-01' and sales_date < '2022-04-01'

order by sales_date asc, PRODUCT_ID asc, USER_ID asc;