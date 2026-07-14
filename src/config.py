from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    bot_token: str
    admin_ids: List[int] = []
    blocked_ids: List[int] = []
    database_url: str = "sqlite+aiosqlite:///users.db"
    
    # Aliases
    cock_top_aliases: List[str] = ["топ", "т", "top", "t"]
    cock_atop_aliases: List[str] = ["антитоп", "атоп", "ат", "antitop", "atop", "at"]
    cock_lngst_aliases: List[str] = ["lngst", "лнгст", "лтоп", "otv", "отв", "otval", "отвал", "лонгест", "longest"]
    cock_ttop_aliases: List[str] = ["трутоп", "ттоп", "тт", "truetop", "ttop", "tt"]

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Settings()
