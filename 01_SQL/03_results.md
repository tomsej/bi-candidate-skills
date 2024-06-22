# Results

Please paste your SQL scripts here:

### 1) Average number of finished courses to every active B2B student.

SELECT AVG(courses) AS finished_courses 
FROM
(
	SELECT  student_id
		   ,COUNT(course_id) AS courses
	FROM
	(
		SELECT co.student_id
			   ,co.course_id
			   ,ROW_NUMBER() OVER (PARTITION BY co.student_id,co.course_id,co.event_timestamp ORDER BY co.event_timestamp DESC) AS rn
		FROM courses co
		LEFT JOIN students st ON co.student_id  = st.student_id
		WHERE st.is_active = 1 AND st.student_type = 'b2b' AND event_type = 'finished'
	)
	WHERE rn = 1
	GROUP BY 1
)

### 2) Average number of started courses to every B2C student.

SELECT AVG(courses) AS started_courses 
FROM
(
	SELECT  student_id
		   ,COUNT(course_id) AS courses
	FROM
	(
		SELECT co.student_id
			   ,co.course_id
			   ,ROW_NUMBER() OVER (PARTITION BY co.student_id,co.course_id,co.event_timestamp ORDER BY co.event_timestamp DESC) AS rn
		FROM courses co
		LEFT JOIN students st ON co.student_id  = st.student_id
		WHERE st.student_type = 'b2c' AND event_type = 'start'
	)
	WHERE rn = 1
	GROUP BY 1
)

### 3) Overall study length of every student.
WITH abc_start AS
(
	SELECT *
		,ROW_NUMBER() OVER (PARTITION BY student_id,course_id ORDER BY event_timestamp ASC) AS rn_2
	FROM	   
	(
		SELECT co.student_id
			,co.course_id
			,co.event_type 
			,co.event_timestamp
			,ROW_NUMBER() OVER (PARTITION BY co.student_id,co.course_id,co.event_timestamp ORDER BY co.event_timestamp DESC) AS rn
		FROM courses co
		LEFT JOIN students st ON co.student_id  = st.student_id
		WHERE event_type = 'start'
		ORDER BY co.student_id,event_timestamp,course_id
	)
	WHERE rn = 1
	ORDER BY student_id,course_id
)


,abc_end
AS
(
SELECT *
	   ,ROW_NUMBER() OVER (PARTITION BY student_id,course_id ORDER BY event_timestamp ASC) AS rn_2
FROM	   
(
	SELECT co.student_id
		   ,co.course_id
		   ,co.event_type 
		   ,co.event_timestamp
		   ,ROW_NUMBER() OVER (PARTITION BY co.student_id,co.course_id,co.event_timestamp ORDER BY co.event_timestamp DESC) AS rn
	FROM courses co
	LEFT JOIN students st ON co.student_id  = st.student_id
	WHERE event_type = 'end'
	ORDER BY co.student_id,event_timestamp,course_id
)
WHERE rn = 1
ORDER BY student_id,course_id

)

------------------------------------
SELECT st.student_id
      ,SUM(hrs.study_hours) AS study_length_mins
FROM students st
LEFT JOIN
(
    SELECT  st.student_id
        ,st.course_id
        ,st.event_timestamp AS start
        ,ed.event_timestamp AS end
        ,ed.event_timestamp - st.event_timestamp AS study_interval
        ,DATEDIFF('MINUTES',st.event_timestamp,ed.event_timestamp) AS study_hours
    FROM abc_start st
    LEFT JOIN abc_end ed ON st.student_id = ed.student_id AND st.course_id = ed.course_id AND st.rn_2  = ed.rn_2
) hrs ON st.student_id  = hrs.student_id

GROUP BY 1


Create new branch e.g. `novakj` (user surname + first letter of your name - e.g. Jan Novák => `novakj`) and push this branch to git.

🎉 **You just finished SQL test!!** 🎉