Linkedlist koduna ek olarak find_cycle ve do_cycle methodlar� var.
 find_cycle methodunda slowptr ve fastptr olmak �zere 2 adet pointer linkedlist elemanlar�n� g�sterir. 
slowptr bir birim ilerlerken fastptr iki birim ilerler. fastptr None olursa cycle yoktur. 
fastptr none olmazsa veya slowptr e�it olursa cycle vard�r. do_cycle methodunda linkedlist'in ka� elemanl� oldu�unu bulur. 
Random olarak ilerleyerek bir Node'un nextnode'u ba�ka bir node'u g�sterir ve cycle olu�turur.

