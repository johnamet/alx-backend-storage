-- Create a function SafeDivide that returns 0 if the divisor is zero, otherwise performs the division

DELIMITER //

CREATE FUNCTION SafeDivide(numerator DOUBLE, denominator DOUBLE) RETURNS DOUBLE
BEGIN
    IF denominator = 0 THEN
        RETURN 0;
    ELSE
        RETURN numerator / denominator;
    END IF;
END //

DELIMITER ;

