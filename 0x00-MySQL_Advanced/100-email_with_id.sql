-- Create a trigger to automatically fill in the email_id field when a new user is inserted

DELIMITER //

CREATE TRIGGER fill_email_id BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    SET NEW.email_id = CONCAT(NEW.id, '-', NEW.email);
END //

DELIMITER ;

