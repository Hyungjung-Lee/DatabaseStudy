
USE classicmodels;

start transaction;

update orders set status = 'TEST' where orders.orderNumber = 10420;

update orders set status = 'TEST' where orders.orderNumber = 10421;

##constraint error
#update orders set customerNumber = 'TEST' where orders.orderNumber = 10420;

##duplication error
#insert  into `orders`(`orderNumber`,`orderDate`,`requiredDate`,`shippedDate`,`status`,`comments`,`customerNumber`) values (10100,'2003-01-06','2003-01-13','2003-01-10','Shipped',NULL,363);

commit;