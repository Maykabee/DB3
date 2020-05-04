CREATE VIEW sales_game AS
SELECT
 sales.game_name,
 sales.region_name,
 sales.sales,
 game.genre_name,
 game.publisher_name
FROM
 sales
 JOIN game ON game.game_name=sales.game_name;