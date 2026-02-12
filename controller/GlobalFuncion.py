class GlobaFunction:

    @staticmethod
    def valor_valido(value: str) -> bool | None:
        if value is None:
            return None

        value = value.strip().lower()

        if value in ("n", "no"):
            return False
        elif value in ("s", "si", "sí"):
            return True
        else:
            return None
               
