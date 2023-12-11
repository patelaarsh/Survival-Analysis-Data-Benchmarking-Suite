Query1: Calculate the number of people whose start date is greater than '1991-09-10' and end date is less than  '2010-03-07' and are dead. 

Query2: Calculate the percentage of data that is censored (individuals for whom the exact death time is unknown).

Query3: Calculate the average duration of observations for individuals who are not censored (i.e., those who completed the observation period).

Kaplan-Meier Estimate

Time-to-Event:

"time-to-event" is the difference between "age_end" and "age_start_observed."

Event Status:

If "is_dead" is True, it means an event occurred (death), so set the event status to 1.
If "is_censored" is True and "is_dead" is False, it means the observation was censored (the event did not occur within the observation period), so set the event status to 0.


