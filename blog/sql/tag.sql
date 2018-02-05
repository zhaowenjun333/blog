


-- DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tag` varchar(16)  NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE key `tag` (`tag`)
) ENGINE = InnoDB DEFAULT CHARSET=UTF8;

-- SET FOREIGN_KEY_CHECKS = 1;

-- DROP TABLE IF EXISTS `post_tag`;
CREATE TABLE `post_tag`(
  `post_id` bigint(20) NOT NULL ,
  `tag_id` bigint(20) NOT  NULL ,
  PRIMARY KEY (`post_id`,`tag_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `post_tag_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`),
  CONSTRAINT `post_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
)ENGINE = InnoDB DEFAULT CHARSET=utf8;

-- SET FOREIGN_KEY_CHECKS = 1;