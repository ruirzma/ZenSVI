import unittest
import os
import shutil
from pathlib import Path

from zensvi.cv import ClassifierWeather


class TestClassifierWeather(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.output = "tests/data/output/classification/weather"
        Path(self.output).mkdir(parents=True, exist_ok=True)

    # def tearDown(self):
    #     # remove output directory
    #     shutil.rmtree(self.output, ignore_errors=True)

    def test_classify_directory(self):
        classifier = ClassifierWeather()
        image_input = "tests/data/input/images"
        dir_summary_output = str(Path(self.output) / "directory/summary")
        classifier.classify(
            image_input,
            dir_summary_output=dir_summary_output,
            batch_size=3,
        )
        # assert True if files in dir_image_output and dir_summary_output are not empty
        self.assertTrue(os.listdir(dir_summary_output))

    def test_classify_single_image(self):
        classifier = ClassifierWeather()
        image_input = "tests/data/input/images/-3vfS0_iiYVZKh_LEVlHew.jpg"
        dir_summary_output = str(Path(self.output) / "single/summary")
        classifier.classify(
            image_input,
            dir_summary_output=dir_summary_output,
        )
        # assert True if files in dir_image_output and dir_summary_output are not empty
        self.assertTrue(os.listdir(dir_summary_output))

    def test_classify_with_mps_device(self):
        device = "mps"
        classifier = ClassifierWeather(device=device)
        image_input = "tests/data/input/images"
        dir_summary_output = str(Path(self.output) / "mps/summary")
        classifier.classify(
            image_input,
            dir_summary_output=dir_summary_output,
            batch_size=3,
        )
        # assert True if files in dir_image_output and dir_summary_output are not empty
        self.assertTrue(os.listdir(dir_summary_output))


if __name__ == "__main__":
    unittest.main()
