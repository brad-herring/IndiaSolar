from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn import preprocessing
from numpy import nan
from matplotlib import pyplot as plt

INVERTERS = {1: '1BY6WEcLGh8j5v7', 2: '1IF53ai7Xc0U56Y', 3: '3PZuoBAID5Wc2HD', 4: '7JYdWkrLSPkdwr4',
             5: 'McdE0feGgRqW7Ca', 6: 'VHMLBKoKgIrUVDU', 7: 'WRmjgnKYAwPKWDb', 8: 'ZnxXDlPa8U1GXgE',
             9: 'ZoEaEvLYb1n2sOq', 10: 'adLQvlD726eNBSB', 11: 'bvBOhCH3iADSZry', 12: 'iCRJl6heRkivqQ3',
             13: 'ih0vzX44oOqAx2f', 14: 'pkci93gMrogZuBj', 15: 'rGa61gmuvPhdLxV', 16: 'sjndEbLyjtCKgGv',
             17: 'uHbuxQJl8lW7ozc', 18: 'wCURE6d3bPkepu2', 19: 'z9Y9gH1T5YWrNuG', 20: 'zBIq5rxdHJRwDNY',
             21: 'zVJPv84UY57bAof', 22: 'YxYtjZvoooNbGkE'}

INVERTERS_REV = {'1BY6WEcLGh8j5v7': 1,'1IF53ai7Xc0U56Y': 2,'3PZuoBAID5Wc2HD': 3,'7JYdWkrLSPkdwr4': 4,
             'McdE0feGgRqW7Ca': 5,'VHMLBKoKgIrUVDU': 6,'WRmjgnKYAwPKWDb': 7,'ZnxXDlPa8U1GXgE': 8,
             'ZoEaEvLYb1n2sOq': 9,'adLQvlD726eNBSB': 10,'bvBOhCH3iADSZry': 11,'iCRJl6heRkivqQ3': 12,
             'ih0vzX44oOqAx2f': 13,'pkci93gMrogZuBj': 14,'rGa61gmuvPhdLxV': 15,'sjndEbLyjtCKgGv': 16,
             'uHbuxQJl8lW7ozc': 17,'wCURE6d3bPkepu2': 18,'z9Y9gH1T5YWrNuG': 19,'zBIq5rxdHJRwDNY': 20,
             'zVJPv84UY57bAof': 21,'YxYtjZvoooNbGkE': 22}

# Create training and testing datasets
train = pd.read_csv(r"C:\Users\Admin\Desktop\Programming Applications and Projects\Datasets\Plant_1_Generation_Data.csv")

test = pd.read_csv(r"C:\Users\Admin\Desktop\Programming Applications and Projects\Datasets\Plant_1_Generation_Data.csv")

# Replaces inverter source key with numerical value 1-22
train.SOURCE_KEY = [INVERTERS_REV[item] for item in train.SOURCE_KEY]
test.SOURCE_KEY = [INVERTERS_REV[item] for item in test.SOURCE_KEY]

plt.scatter(train['SOURCE_KEY'][-22:], train['TOTAL_YIELD'][-22:])
plt.xlabel('Inverter')
plt.ylabel('Total Power Output')
plt.xticks(np.arange(1, 23, step=1))
plt.title('Total Power Output per Inverter - May 2015')
plt.show()
