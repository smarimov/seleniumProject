def test_search_text_field_max_length(self):
    # get the search box
    search_field = self.driver.find_element_by_id("search")
    # check maxlength attribute is set to 128
    self.assertEqual("128", search_field.get_attribute("maxlength"))


def test_search_text_field_max_length(self):
    # get the search box
    search_field = self.driver.find_element_by_name("q")
    # check maxlength attribute is set to 128
    self.assertEqual("128", search_field.get_attribute("maxlength"))
