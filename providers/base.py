class BaseProvider:
    name: str = "base"

    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Provider must implement generate()")
