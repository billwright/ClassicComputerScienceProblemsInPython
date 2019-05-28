from typing import Dict

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.geneToEncodeMapping: Dict[str:int] = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
        self.encodeToGeneMapping: Dict[int:str] = {0b00: 'A', 0b01: 'C', 0b10: 'G', 0b11: 'T'}
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1

    def decompression(self) -> str:
        return "Implement me"

    def __str__(self) -> str:
        return "Implement me"


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTATATATATATATAGCCATGGATGCAA" * 100