class Card:
    def __init__(self, string_value: str):
        string_value = string_value.lower()

        self.is_number = False
        self.number_value = 0

        self.is_action = False
        self.is_freeze = False
        self.is_flip_3 = False
        self.is_second_chance = False

        self.is_modifier = False
        self.is_modifier_add = False
        self.is_modifier_double = False
        self.modifier_value = 0


        try:
            if string_value.startswith('+'):
                self.is_modifier = True
                self.is_modifier_add = True

                self.modifier_value = str(string_value[1:])

            elif string_value.startswith('x'):
                self.is_modifier = True
                self.is_modifier_double = True

            elif string_value == 'freeze' or string_value == 'f':
                self.is_action = True
                self.is_freeze = True

            elif string_value == 'flip three' or string_value == 'flip 3' or string_value == 'f3' or string_value == 'flip3':
                self.is_action = True
                self.is_flip_3 = True

            elif string_value == 'second chance' or string_value == 'sc':
                self.is_action = True
                self.is_second_chance = True

            else:
                self.is_number = True
                self.number_value = int(string_value)
        except ValueError:
            raise ValueError('Unknown card type!')


    def __eq__(self, other):
        if not isinstance(other, Card):
            return False

        return (
            self.is_number == other.is_number and
            self.number_value == other.number_value and
            self.is_action == other.is_action and
            self.is_freeze == other.is_freeze and
            self.is_flip_3 == other.is_flip_3 and
            self.is_second_chance == other.is_second_chance and
            self.is_modifier == other.is_modifier and
            self.is_modifier_add == other.is_modifier_add and
            self.is_modifier_double == other.is_modifier_double and
            self.modifier_value == other.modifier_value
        )


    def __hash__(self):
        return hash((
            self.is_number,
            self.number_value,
            self.is_action,
            self.is_freeze,
            self.is_flip_3,
            self.is_second_chance,
            self.is_modifier,
            self.is_modifier_add,
            self.is_modifier_double,
            self.modifier_value
        ))


    def __repr__(self):
        if self.is_modifier:
            if self.is_modifier_add:
                return f"Card(+{self.modifier_value})"
            elif self.is_modifier_double:
                return "Card(x2)"
        elif self.is_action:
            if self.is_freeze:
                return "Card(freeze)"
            elif self.is_flip_3:
                return "Card(flip 3)"
            elif self.is_second_chance:
                return "Card(second chance)"
        elif self.is_number:
            return "Card(" + str(self.number_value) + ")"

        return "Card(Unknown)"