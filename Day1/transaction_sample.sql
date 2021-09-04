DELIMITER $$
CREATE PROCEDURE `myprocedure`()
BEGIN

	DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;

	START TRANSACTION;
    update orders set status = '1' where orders.orderNumber = 10420;
    COMMIT WORK;
END$$
DELIMITER ;