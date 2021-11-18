-- script that lists all shows contained in the database hbtn_0d_tvshows with theirs genres id's.
SELECT s.title, sg.genre_id FROM tv_shows AS s LEFT JOIN tv_show_genres AS sg ON s.id = sg.show_id ORDER BY s.title, sg.genre_id;
