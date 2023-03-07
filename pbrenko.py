# flake8: noqa
import math

class PbRenko:
    """Renko initialization class
    """
    def __init__(self, percent, data):
        self.percent = percent
        self.data = data
        self.bricks = []
        self.low_wick = 0
        self.high_wick = 0
    
    def create_pbrenko(self):
        gap = float(self.data[0]) * self.percent / 100

        for i, d in enumerate(self.data):
            if i == 0:
                if len(self.bricks) == 0:
                    self.bricks.append({"type":"first", "open":float(d), "close":float(d)})
            else:
                if self.bricks[-1]["type"] == "up":
                    print("first up")
                elif self.bricks[-1]["type"] == "down":
                    print("fist down")
                else:
                    if d > self.bricks[-1]["close"]:
                        delta = d - self.bricks[-1]["close"]
                        fcount = math.floor(delta / gap)
                        if fcount != 0:
                            self.add_bricks("up", fcount, gap)
                            gap = d * self.percent / 100
                    if d < self.bricks[-1]["close"]:
                        delta = self.bricks[-1]["close"] - d
                        fcount = math.floor(delta / gap)
                        if fcount != 0:
                            self.add_bricks("down", fcount, gap)
                            gap = d * self.percent / 100
                    break


    def add_bricks(self, type, count, brick_size, wick=0):
        """Adds brick(s) to the bricks list
        :param type: type of brick (up or down)
        :type type: string
        :param count: number of bricks to add
        :type count: int
        :param brick_size: brick size
        :type brick_size: float
        """
        for i in range(count):
            if type == "up":
                if self.bricks[-1]["type"] == "up" or self.bricks[-1]["type"] == "first":
                    if wick == 0:
                        self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] + brick_size)})
                    else:
                        if i == 0:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] + brick_size), "low": wick})
                        else:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] + brick_size)})
                elif self.bricks[-1]["type"] == "down":
                    if wick == 0:
                        self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] + brick_size)})
                    else:
                        if i == 0:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] + brick_size), "low": wick})
                        else:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] + brick_size)})
            elif type == "down":
                if self.bricks[-1]["type"] == "up":
                    if wick == 0:
                        self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] - brick_size)})
                    else:
                        if i == 0:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] - brick_size), "high": wick})
                        else:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] - brick_size)})
                elif self.bricks[-1]["type"] == "down" or self.bricks[-1]["type"] == "first":
                    if wick == 0:
                        self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] - brick_size)})
                    else:
                        if i == 0:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] - brick_size), "high": wick})
                        else:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] - brick_size)})