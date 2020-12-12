from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
import tensorflow as tf
from sklearn import preprocessing
from numpy import nan
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

# Create training and testing datasets
train = pd.read_csv(r"C:\Users\Admin\Desktop\Programming Applications and Projects\Datasets\Plant_1_Generation_Data.csv")

test = pd.read_csv(r"C:\Users\Admin\Desktop\Programming Applications and Projects\Datasets\Plant_1_Generation_Data.csv")

plt.scatter(train['SOURCE_KEY'], train['TOTAL_YIELD'], s=0.2)
plt.show()
