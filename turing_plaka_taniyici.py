import time

class TuringMachine:
    def __init__(self, tape_input):
        self.tape = list(tape_input) + ['_']
        self.head = 0
        self.state = 'q0'
        
        self.digits = "0123456789"
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        self.transitions = {}
        self.setup_transitions()

    def setup_transitions(self):
        for d in self.digits:
            self.transitions[('q0', d)] = ('q1', d, 'R')
        
        for d in self.digits:
            self.transitions[('q1', d)] = ('q2', d, 'R')
            
        for l in self.letters:
            self.transitions[('q2', l)] = ('q3', l, 'R')
            
        for l in self.letters:
            self.transitions[('q3', l)] = ('q4', l, 'R')
            
        for d in self.digits:
            self.transitions[('q4', d)] = ('q5', d, 'R')
            
        for d in self.digits:
            self.transitions[('q5', d)] = ('q6', d, 'R')
            
        for d in self.digits:
            self.transitions[('q6', d)] = ('q7', d, 'R')
            
        self.transitions[('q7', '_')] = ('q_accept', '_', 'R')

    def print_step(self, read_sym, write_sym, move):
        tape_str = "".join(self.tape)
        head_indicator = [" "] * len(self.tape)
        if self.head < len(head_indicator):
            head_indicator[self.head] = "^"
        
        print(f"Durum: {self.state:<5} | Okunan: {read_sym:<3} | Yazılan: {write_sym:<3} | Yön: {move:<2} | Bant: {tape_str}")
        print(" " * 49 + "".join(head_indicator))

    def run(self):
        print(f"\n--- Girdi Kontrol Ediliyor: {''.join(self.tape[:-1])} ---")
        
        while self.state not in ['q_accept', 'q_reject']:
            if self.head < len(self.tape):
                read_symbol = self.tape[self.head]
            else:
                read_symbol = '_'

            if (self.state, read_symbol) in self.transitions:
                next_state, write_symbol, move = self.transitions[(self.state, read_symbol)]
                self.print_step(read_symbol, write_symbol, move)
                
                self.tape[self.head] = write_symbol
                self.state = next_state
                
                if move == 'R':
                    self.head += 1
                elif move == 'L':
                    self.head -= 1
            else:
                self.print_step(read_symbol, read_symbol, 'R')
                self.state = 'q_reject'
            
            time.sleep(0.3)

        print("-" * 40)
        if self.state == 'q_accept':
            print("Sonuç: KABUL (Geçerli Plaka Formatı)")
        else:
            print("Sonuç: RED (Geçersiz Plaka Formatı)")
        print("-" * 40)

def main():
    while True:
        girdi = input("\nPlaka giriniz (Çıkmak için 'q'): ")
        if girdi.lower() == 'q':
            break
        tm = TuringMachine(girdi)
        tm.run()

if __name__ == "__main__":
    main()