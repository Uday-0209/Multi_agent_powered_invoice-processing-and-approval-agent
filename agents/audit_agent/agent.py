class AuditAgent:

    def run(self, state):

        print("AUDIT LOG")

        for key, value in state.items():
            print(f"{key} : {value}")

        return state