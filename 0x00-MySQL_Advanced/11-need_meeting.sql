-- Create a view need_meeting that lists all students who need a meeting

CREATE VIEW need_meeting AS
SELECT student_id, student_name, meeting_date
FROM students
WHERE meeting_date IS NOT NULL;

