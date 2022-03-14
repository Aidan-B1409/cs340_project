-- Data Defintions
-- TABLE

-- University
-- 		student count - int
-- 		ranking - int
-- 		name - varchar 
--		est date - date 
-- 		street name - varchar
--      street num - int
--      zip code - int
CREATE TABLE `university`(
	`id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`student_count` INT NOT NULL,
	`ranking` INT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`est_date` DATE NOT NULL,
	`street_name` VARCHAR(255) NOT NULL,
	`street_num` INT NOT NULL,
	`zip_code` INT NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;	
	
--Major
--		name - varchar
--		major_code - int
--		description - varchar
CREATE TABLE `major`(
	`pid` INT,
	`id` INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(255) NOT NULL,
	`major_code` INT NOT NULL,
	`description` VARCHAR(255)
	FOREIGN KEY(`pid`) REFERENCES university (`id`)
	
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--Course
--		course_code - int
--		course_name - varchar
--		course_description - varchar
--		start_date - date
--		end_date - date
--		start_time - time
--		end_time - time
CREATE TABLE `course`(
	`pid` INT,
	`eid` INT,
	`cid` INT,
	`id` INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`course_code` INT NOT NULL,
	`course_name` VARCHAR(255) NOT NULL,
	`course_description` VARCHAR(255) NOT NULL,
	`start_date` DATE NOT NULL,
	`end_date` DATE NOT NULL,
	`start_time` TIME NOT NULL,
	`end_time` TIME NOT NULL
	FOREIGN KEY(`pid`) REFERENCES university (`id`),
	FOREIGN KEY(`eid`) REFERENCES faculty (`id`),
	FOREIGN KEY(`cid`) REFERENCES major (`major_code`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--Faculty
--		first_name - varchar
--		last_name - varchar
--		date_of_birth - date
--		street_name - varchar
--		street_num - int
--		zip_code - int
CREATE TABLE `faculty`(
	`pid` INT,
	`id` INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`first_name` VARCHAR(255) NOT NULL,
	`last_name` VARCHAR(255) NOT NULL,
	`date_of_birth` DATE NOT NULL,
	`street_name` VARCHAR(255) NOT NULL,
	`street_num` INT NOT NULL,
	`zip_code` INT NOT NULL
	FOREIGN KEY(`pid`) REFERENCES university (`id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--Student
-- 		first_name - varchar
--		last_name - varchar
--		date_of_birth - date
--		gpa - float
--		street_name - varchar
--		street_num - int
--    	zip_code - int
CREATE TABLE `student`(
	`pid` INT,
	`eid` INT,
	`id` INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`first_name` VARCHAR(255) NOT NULL,
	`last_name` VARCHAR(255) NOT NULL,
	`date_of_birth` DATE NOT NULL,
	`gpa` FLOAT NOT NULL,
	`street_name` VARCHAR(255) NOT NULL,
	`street_num` INT NOT NULL,
	`zip_code` INT NOT NULL,
	FOREIGN KEY(`pid`) REFERENCES university(`id`),
	FOREIGN KEY(`eid`) REFERENCES major(`major_code`)
		
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--student_course
--		pid - int
--		eid - int
CREATE TABLE `student_course(
	`pid` INT,
	`eid` INT,
	FOREIGN KEY (`pid`) REFERENCES student(`id`),
	FOREIGN KEY (`eid`) REFERENCES course(`course_code`),
	PRIMARY KEY (`pid`, `eid)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO university(
	student_count, 
	ranking, 
	name, 
	est_date, 
	street_name, 
	street_num, 
	zip_code
) VALUES(
	25000,
	110,
	'John Terry',
	'2015-07-19',
	'6342 Cherry Drive',
	'64733'
);

INSERT INTO major(
	name,
	major_code,
	description,
	pid
) VALUES(
	'Underwater Basket Weaving',
	4113902,
	'Learn how to hold your breathe and weave baskets all at the same time!',
	(SELECT id FROM university WHERE name = 'something')
);

INSERT INTO course(
	course_code,
	course_name,
	course_description,
	start_date,
	end_date,
	start_time,
	end_time,
	pid,
	eid,
	cid
)VALUES(
	124134,
	'Basket Weaving 101',
	'Learn the basics of basket weaving',
	'2022-06-01',
	'2022-09-01',
	00:00:00,
	20:20:20,
	(SELECT id FROM university WHERE name = 'something'),
	(SELECT id FROM faculty WHERE first_name = 'John' AND last_name = 'Adams'),
	(SELECT major_code FROM major WHERE name = 'else')
);

INSERT INTO faculty(
	first_name,
	last_name,
	date_of_birth,
	street_name,
	street_num,
	zip_code,
	pid
) VALUES(
	'Jerry',
	'Smith',
	'1990-06-01',
	'Greenwood',
	1232,
	13423,
	(SELECT id FROM university WHERE name = 'somthing')
);

INSERT INTO student(
	first_name,
	last_name,
	date_of_birth,
	gpa,
	street_name,
	street_num,
	zip_code,
	pid,
	eid
) VALUES(
	'Olivia',
	'Smith',
	'2001-05-07',
	3.32421,
	'Orangewood',
	5434,
	13523,
	(SELECT id FROM university WHERE name = 'something'),
	(SELECT major_code FROM major WHERE name = 'else')
);

INSERT INTO student_course(
	pid
	eid
) VALUES(
	(SELECT id FROM student WHERE first_name = 'John' AND last_name = 'Smith')
	(SELECT major_code FROM major WHERE name = 'else')
);











