class BallotBox:
    def __init__(self, candidates: list[str]):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}
        self.total_votes = 0

    def cast_vote(self, candidate: str):
        if candidate in self.votes:
            self.votes[candidate] += 1
            self.total_votes += 1
        else:
            raise ValueError(f"Candidato {candidate} não encontrado.")

    def get_results(self) -> dict[str, float]:
        if self.total_votes == 0:
            return {candidate: 0.0 for candidate in self.candidates}

        results = {
            candidate: (votes / self.total_votes) * 100
            for candidate, votes in self.votes.items()
        }
        return results


if __name__ == "__main__":
    ballot_box = BallotBox(
        ["Eymael", "Levy Fidelix", "Cabo Daciolo", "Voto nulo", "Voto em branco"]
    )

    print("0: Encerrar votação")
    for i, candidate in enumerate(ballot_box.candidates, start=1):
        print(f"{i}: {candidate}")

    while True:
        try:
            choice = int(input("Escolha um candidato: "))
            if choice == 0:
                break
            elif 1 <= choice <= len(ballot_box.candidates):
                ballot_box.cast_vote(ballot_box.candidates[choice - 1])
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError as e:
            print(f"Erro: {e}")

    results = ballot_box.get_results()
    print("\nResultados da votação:")
    for candidate, percentage in results.items():
        print(
            f"{candidate}: {ballot_box.votes[candidate]} votos com {percentage:.2f}% do total de votos"
        )