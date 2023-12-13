-- lists all shows contained in hbtn_0d_tvshows


SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genre ON tv_shows.id = tv_show_genres .show_id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_show.title ASC tv_show_genres.genre_id ASC;
