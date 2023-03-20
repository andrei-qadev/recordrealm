To handle small typos in search queries, you can use a fuzzy search technique such as trigram similarity or Levenshtein distance. PostgreSQL has built-in support for trigram
similarity through the pg_trgm extension. If you're using PostgreSQL, you can leverage this extension for your search.

First, you'll need to enable the pg_trgm extension in your PostgreSQL database:

CREATE EXTENSION IF NOT EXISTS pg_trgm;

Then, you can modify the find_artist method to use the similarity function from the pg_trgm extension. You'll also need to set a similarity threshold to filter results based on how
close they are to the search query.

