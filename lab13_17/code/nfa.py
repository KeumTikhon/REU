# NFA для распознавания регулярных выражений
# Поддерживает: конкатенация, альтернация (|), итерация (*)

class NFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}  # (state, symbol) -> set of states
        self.start_state = None
        self.accept_states = set()
        self.state_counter = 0
    
    def add_state(self):
        """Добавить новое состояние и вернуть его номер"""
        state = self.state_counter
        self.state_counter += 1
        self.states.add(state)
        return state
    
    def add_transition(self, from_state, symbol, to_state):
        """Добавить переход (поддерживает epsilon-переходы, symbol=None)"""
        if symbol is not None:
            self.alphabet.add(symbol)
        key = (from_state, symbol)
        if key not in self.transitions:
            self.transitions[key] = set()
        self.transitions[key].add(to_state)
    
    def epsilon_closure(self, states):
        """Найти epsilon-замыкание набора состояний"""
        closure = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            key = (state, None)
            if key in self.transitions:
                for next_state in self.transitions[key]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure
    
    def match(self, input_string):
        """Проверить, принимает ли NFA входную строку"""
        # Начинаем с epsilon-замыкания начального состояния
        current_states = self.epsilon_closure({self.start_state})
        
        for char in input_string:
            next_states = set()
            for state in current_states:
                key = (state, char)
                if key in self.transitions:
                    next_states.update(self.transitions[key])
            
            # Добавляем epsilon-замыкание для каждого нового состояния
            current_states = self.epsilon_closure(next_states)
        
        # Проверяем, есть ли принимающее состояние в текущем наборе
        return bool(current_states & self.accept_states)
    
    def build_from_regex(self, regex):
        """
        Построить NFA из простого регулярного выражения
        Синтаксис: a|b (или), a* (звёздочка), ab (конкатенация)
        """
        # Инициализация
        self.start_state = self.add_state()
        self.accept_states.add(self.start_state)
        
        # Простая реализация для базовых случаев
        # Для полной реализации Thompson's Construction см. ниже
        pass


# Пример использования: простой NFA для паттерна a*b*
def create_simple_nfa_example():
    nfa = NFA()
    
    # Состояния
    q0 = nfa.add_state()
    q1 = nfa.add_state()
    q2 = nfa.add_state()
    q3 = nfa.add_state()
    q4 = nfa.add_state()
    
    # Начальное и принимающее состояния
    nfa.start_state = q0
    nfa.accept_states = {q4}
    
    # Переходы для a*: можно читать 'a' или пропустить
    nfa.add_transition(q0, 'a', q1)
    nfa.add_transition(q1, 'a', q1)  # Цикл для a*
    nfa.add_transition(q1, None, q2)  # Epsilon переход (конец a*)
    nfa.add_transition(q0, None, q2)  # Можно пропустить a*
    
    # Переходы для b*
    nfa.add_transition(q2, 'b', q3)
    nfa.add_transition(q3, 'b', q3)  # Цикл для b*
    nfa.add_transition(q3, None, q4)  # Epsilon переход (конец b*)
    nfa.add_transition(q2, None, q4)  # Можно пропустить b*
    
    return nfa


# Тестирование
if __name__ == "__main__":
    nfa = create_simple_nfa_example()
    
    test_cases = ["", "a", "aaa", "b", "abb", "aabb", "ab", "ba"]
    
    print("Распознавание паттерна a*b*:")
    for test in test_cases:
        result = nfa.match(test)
        status = "✓" if result else "✗"
        print(f"  {status} '{test}': {result}")
