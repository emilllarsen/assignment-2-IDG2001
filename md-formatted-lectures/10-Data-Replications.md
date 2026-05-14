 Push vs pull, partial vs full


 Full or partial replica?


 Both replica servers and content


 Consistency protocols


_specific consistency model_


_Wikipedia: Consistency model > Example_


responsible for coordinating write operations on x


initiated and write is carried out locally


 If blocking, process initiating update may be blocked for long time


 Primary can order all writes in globally unique order


 If blocking updates, processes will always see the effects of their most recent

write operation


Client Client









Data store









W1. Write request
W2. Forward request to primary
W3. Tell backups to update
W4. Acknowledge update
W5. Acknowledge write completed



R1. Read request
R2. Response to read


primary has locally performed the updates


 How to organize and maintain data in persistent storage?


 How to find specific records?


 How to update and delete records?


and a process for maintaining the records over time.


data) is treated as a single unit. Either the entire statement is executed, or none
of it is executed. This property prevents data loss and corruption from occurring
if, for example, if your streaming data source fails mid-stream.


predefined, predictable ways. Transactional consistency ensures that corruption
or errors in your data do not create unintended consequences for the integrity
of your table.


once, isolation of their transactions ensures that the concurrent transactions
don't interfere with or affect one another. Each request can occur as though
they were occurring one by one, even though they're actually occurring
simultaneously.


transactions will be saved, even in the event of system failure.


