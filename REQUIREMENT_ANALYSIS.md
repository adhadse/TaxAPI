- List, view and edit `TaxPayers`   
    - **ONLY DONE** by `TaxAccountant` and `Admin` roles
- One `TaxAccountant` MANAGE DIFFERENT `TaxPayers`.
- Full tax is dependent on which state the `TaxPayer` belongs to.
  
  Total tax = state tax + central tax. 
    - If it is a union territory, then no state tax (we expect you do some googling on your own to understand GST system)
> NOTE: we expect you to figure out what a "tax" object will look like. 
> SGST, CGST, state tax, arrears, fines, etc. 
> 
> This is domain knowledge that we expect our engineers to figure out by themeselves. 
> Will you use reducing interest rates, etc ? Especially tricky question is 
> 
> **how will you handle dates** - we are especially interested to see this code, since date handling is one of the trickiest things here (is it needed to handle timezone information in your database ?)
- Create a tax due
  - **ONLY DONE** by `TaxAccountant` role. 
  - The system will take certain inputs (PAN card of tax-payer, income from salary, income from share market, etc etc) 
  - and calculate the total tax due. 
  - It also sets status as NEW or DELAYED based on due date.
- Edit tax due. 
  - **ONLY DONE** by `TaxAccountant`. 
  - But it <mark>**cannot be done if tax is already paid**</mark>. 
  - **IMPORTANT**: We want to see how you design this. 
    - Can you save previous history ? In an extreme situation, can you "rollback" the changes ? 
  - **Hint: the best designs here use "double safety"** - logic in the code as well as database constraints.
- Mark tax as paid. 
  - **ONLY DONE** by `TaxPayer`. 
  - P.S. you don't need to do any UPI integration. Just create a dummy !</li>
- Ability to list and view tax due based on the filter applied 
  - By "filter" we mean select by date of creation, date of update, state of tax (`NEW`, `PAID`, `DELAYED`), etc. 
  - **DONE BY ALL** : `TaxPayer`, `TaxAccountant` and `Admin` roles. 
  - **HOWEVER** - `TaxPayer` can only see his own taxes...while `TaxAccountant` 
    and `admin` can see everyone's taxes. The way you design your data model above will allow you to do this. 
 
Make sure there are no security loopholes here. (P.S. you have to show us by writing the testcases to illustrate this)
