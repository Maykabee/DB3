DECLARE
    games_name         game.game_name%TYPE;
    genres_name        game.genre_name%TYPE;
    years              game.year%TYPE;
    publishers_name    game.publisher_name%TYPE;
    game_count         INTEGER := 9;
BEGIN
    games_name:='name';  
    genres_name:='genre';      
    years:='200';      
    publishers_name:='publisher';
    
    FOR i IN 1..game_count LOOP
        INSERT INTO genre (genre_name) 
        VALUES (TRIM(genres_name) || i);
    END LOOP;
    
    FOR i IN 1..game_count LOOP
        INSERT INTO publisher(publisher_name) 
        VALUES (TRIM(publishers_name) || i);
    END LOOP;
    
    
    INSERT INTO Region(region_name) VALUES ('North_America');
    INSERT INTO Region(region_name) VALUES ('Europe');
    INSERT INTO Region(region_name) VALUES ('Japan');
    INSERT INTO Region(region_name) VALUES ('Rest_of_world');
    
    FOR i IN 1..game_count LOOP
    INSERT INTO game(game_name,year,genre_name,publisher_name) 
    VALUES(TRIM(games_name) || i,TRIM(years) || i,TRIM(genres_name) || i,TRIM(publishers_name) || i);
    END LOOP;
    

    FOR i IN 1..game_count LOOP
    INSERT INTO sales(game_name,region_name,sales) VALUES(TRIM(games_name) || i,'North_America',1*i);
    INSERT INTO sales(game_name,region_name,sales) VALUES(TRIM(games_name) || i,'Europe',3*i);
    INSERT INTO sales(game_name,region_name,sales) VALUES(TRIM(games_name) || i,'Japan',2*i);
    INSERT INTO sales(game_name,region_name,sales) VALUES(TRIM(games_name) || i,'Rest_of_world',4*i);
    END LOOP;
    
    
END;
