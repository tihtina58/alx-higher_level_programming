-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT title, genre_id FROM tv_shows AS s INNER JOIN tv_show_genres AS sg ON s.id = sg.show_id ORDER BY title, genre_id;
