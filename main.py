from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
import tensorflow as tf
from sklearn import preprocessing
from numpy import nan

# Create training and testing datasets
train = pd.read_csv(r"C:\Users\Admin\Desktop\Programming Applications and Projects\Datasets\Plant_1_Generation_Data.csv")

test = pd.read_csv(r"C:\Users\Admin\Desktop\Programming Applications and Projects\Datasets\Plant_1_Generation_Data.csv")

print(train.head())