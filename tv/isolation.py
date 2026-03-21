class IsolatedBotLogic:
    """
    A 'bot' that in reality spawns a docker container with the actual bot running inside it.
    """
    def __init__(self, name, bot_type, turn_timeout):
        self.name = name
        self.bot_type = bot_type
        self.turn_timeout = turn_timeout

    def start_bot(self):
        """
        Start the bot container.
        """
        ...

    def initialize(self, map_radius, players, turns, home_base_positions):
        """
        Initialize the bot running inside the container.
        """
        # TODO
        ...

    def turn(self, turn_number, hp, ship_number, cargo, position, power_distribution, radar_contacts, leader_board):
        """
        Ask the bot in the container for an action and return it.
        """
        # TODO
        ...

    def stop_bot(self):
        """
        Stop the bot container.
        """
        # TODO
        ...

