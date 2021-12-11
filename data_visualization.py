import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from common.common import CommonKeys


class DataVisualizeManager:
    def __init__(self, flight_data="2008.csv", airport_data="airports.csv", carrier_data="carriers.csv",
                 plane_data="plane-data.csv"):
        dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
        self._flight_data = pd.read_csv(os.path.join(dir_path, flight_data))
        self._airport_data = pd.read_csv(os.path.join(dir_path, airport_data))
        self._carrier_data = pd.read_csv(os.path.join(dir_path, carrier_data))
        self._plane_data = pd.read_csv(os.path.join(dir_path, plane_data))

    def monthly_plot(self):
        month_set = list(set(self._flight_data[CommonKeys.MONTH].tolist()))
        monthly_data = {}
        for month in month_set:
            monthly_data[month] = {}
            monthly_data[month][CommonKeys.TOTAL] = self._flight_data.loc[self._flight_data[CommonKeys.MONTH] == month]
            monthly_data[month][CommonKeys.DELAY_COUNT] = self._flight_data.loc[
                (self._flight_data[CommonKeys.MONTH] == month) & (self._flight_data[CommonKeys.ARRIVAL_DELAY] > 0)]


if __name__ == '__main__':
    visualizer = DataVisualizeManager()
    visualizer.monthly_plot()
