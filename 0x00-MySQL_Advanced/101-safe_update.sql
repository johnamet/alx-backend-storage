-- Create a stored procedure SafeUpdate that updates a user's email only if the new email is not already taken

DELIMITER //

CREATE PROCEDURE SafeUpdate(IN user_id INT, IN new_email VARCHAR(255))
BEGIN
    DECLARE email_count INT;

    -- Check if the new email is already taken by another user
    SELECT COUNT(*) INTO email_count
    FROM users
    WHERE email = new_email AND id <> user_id;

    -- If the email is not taken, update the user's email
    IF email_count = 0 THEN
        UPDATE users
        SET email = new_email
        WHERE id = user_id;
    ELSE
        SELECT 'Email is already taken' AS message;
    END IF;
END //

DELIMITER ;

