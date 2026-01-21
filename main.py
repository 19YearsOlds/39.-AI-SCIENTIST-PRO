from core.scientist import AIScientist

if __name__ == "__main__":
    with open("data/papers/sample_paper.txt") as f:
        paper = f.read()

    scientist = AIScientist()
    hypothesis = scientist.run(paper)

    print("\nFINAL HYPOTHESIS:")
    print(hypothesis.content)
    print("SCORE:", hypothesis.score)