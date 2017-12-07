drop table if exists question;
drop table if exists option;
CREATE TABLE `question` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `question` TEXT NOT NULL,
    `answer` INT(10) UNSIGNED NOT NULL,
    `level` INT(10) UNSIGNED NOT NULL,
    `correct_count` INT(10) UNSIGNED NOT NULL,
    `total_count` INT(10) UNSIGNED NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `option` (
    `option` TEXT NOT NULL,
    `question_id` INT UNSIGNED NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=utf8;

