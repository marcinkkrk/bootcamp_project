class Game_stats:
    def __init__(self, time_played:float, goals:int, assists:int, yellows:int, reds:int):
        self._time_played = time_played
        self._goals = goals
        self._assists = assists
        self._yellows = yellows
        self._reds = reds


    @property
    def time_played(self):
        return self._time_played


    @time_played.setter
    def time_played(self, time_played):
        self._time_played = time_played

    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, goals):
        self._goals = goals

    @property
    def assists(self):
        return self._assists

    @assists.setter
    def assists(self, assists):
        self._assists = assists

    @property
    def yellows(self):
        return self._yellows

    @yellows.setter
    def yellows(self, yellows):
        self._yellows = yellows

    @property
    def reds(self):
        return self._reds

    @reds.setter
    def reds(self, reds):
        self._reds = reds