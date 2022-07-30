import pytest
from scipy.io import loadmat
import numpy as np
import os

from kwave.utils.colormap import get_color_map


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_color_map():
    collected_values_folder = '/data/code/Work/black_box_testing/collectedValues_getColorMap'
    num_collected_values = len(os.listdir(collected_values_folder))

    for i in range(num_collected_values):
        print(i)
        # Read recorded data
        filepath = os.path.join(collected_values_folder, f'{i:06d}.mat')
        recorded_data = loadmat(filepath)

        num_colors = int(recorded_data['num_colors'])
        expected_color_map = recorded_data['color_map']

        # Execute implementation
        color_map = get_color_map(num_colors)

        # Check correctness
        assert np.allclose(color_map, expected_color_map)

    print('get_color_map(..) works as expected!')
