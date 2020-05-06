DECLARE
    games_name         game.game_name%TYPE;
    genres_name        game.genre_name%TYPE;
    years              game.year%TYPE;
    publishers_name    game.publisher_name%TYPE;
    game_count        INTEGER := 100;
BEGIN
    games_name:='My cafe';  
    genres_name:='Simulation';      
    years:='2010';      
    publishers_name:='Atari';
    
    INSERT INTO genre(genre_name) VALUES(genres_name);
    
    INSERT INTO publisher(publisher_name) VALUES(publishers_name);
    
    INSERT INTO Region(region_name) VALUES ('North_America');
    INSERT INTO Region(region_name) VALUES ('Europe');
    INSERT INTO Region(region_name) VALUES ('Japan');
    INSERT INTO Region(region_name) VALUES ('Rest_of_world');
    
    LOOP
    INSERT INTO game(game_name,year,genre_name,publisher_name) VALUES(games_name,years,genres_name,publishers_name);
    EXIT;
    END LOOP;
    
    LOOP
    INSERT INTO sales(game_name,region_name,sales) VALUES(games_name,'North_America','3.04');
    INSERT INTO sales(game_name,region_name,sales) VALUES(games_name,'Europe','6.08');
    INSERT INTO sales(game_name,region_name,sales) VALUES(games_name,'Japan','1.11');
    INSERT INTO sales(game_name,region_name,sales) VALUES(games_name,'Rest_of_world','2.35');
    EXIT;
    END LOOP;

END;
