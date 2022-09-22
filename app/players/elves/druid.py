from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def play_elf_song(self) -> None:
        instrument = self._musical_instrument
        print(f"{self.nickname} is playing a song on the {instrument}")

    def player_info(self) -> str:
        nick = self.nickname
        spell = self._favourite_spell
        return f"Druid {nick}. {nick} has a favourite spell: {spell}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)
