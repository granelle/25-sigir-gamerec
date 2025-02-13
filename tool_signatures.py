# Lookup tools

def get_game_name(game_id: int) -> str:
    """
    Given a game ID, return the game name.
    """

def get_game_genre(game_id: int) -> str:
    """
    Given a game ID, return the game genre.
    """

def get_game_description(game_id: int) -> str:
    """
    Given a game ID, return a short summary of what this game is about.
    """

def get_game_rank(game_id: int) -> int:
    """
    Given a game ID, return its rank by overall popularity.
    """

def is_device_compatible(game_id: int, device_type: str) -> bool:
    """
    Given a game ID and a device among ['DESKTOP', 'PHONE', 'TABLET', 'CONSOLE', 'VR'],
    return whether the game is compatible with the device.
    """

# Linking tools

def get_game_id_from_fuzzy_name(fuzzy_name: str) -> int:
    """
    Given a fuzzy game name, return the corresponding game ID. Return None if not found.
    Example: 'MM2' -> ID for 'Murder Mystery 2'
    """

def fuzzy_genre_to_genres(fuzzy_genre:str) -> list[str]:
    """
    Given a fuzzy genre name, return a list of official genre names.
    Example: 'simulation' -> ['Simulator/Clicker', 'Tycoon/Management Sim']
    """

# Retrieval tools

def get_search_results(query: str) -> list[int]:
    """
    Given a simple search query, retrieve a list of game IDs from results. (Max: 30)
    """

def get_similar_games_cf(game_id: int) -> list[int]:
    """
    Given a game ID, get similar games based on "users who played this game also played..."
    (Use the collaborative filtering API)
    """

def get_similar_games_content(game_id: int) -> list[int]:
    """
    Given a game ID, get similar games based on similar descriptions.
    (Use SBERT embeddings)
    """

def get_games_by_age_group() -> list[int]:
    """
    Get games commonly played among the given age group, e.g., '18-24'.
    """

def get_default_games(num_games: int) -> list[int]:
    """
    Randomly sample games from the top 100 games.
    May be needed when a user request is too generic.
    """

# Formatting tools

def get_game_info_str(gid, include_descriptions=True):
    """
    Given a game ID, return a formatted string containing its info:
    '{game name} - {genre}. {description}'    
    """

def game_ids_to_enum_game_info(game_ids, max_enum_size=20, include_descriptions=True):
    """
    Given an ordered list of game IDs, return a string of enumerated game information
    in the order of the given list.
    """