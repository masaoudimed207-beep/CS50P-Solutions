import pytest
from datetime import date, timedelta
from seasons import Switch

def test_switch_string_representation():
    
    one_year_ago_str = str(date.today() - timedelta(days=365))
    
    instance = Switch(one_year_ago_str)
    
    assert str(instance) == "Five hundred twenty-five thousand, six hundred minutes"


def test_invalid_date_format():
    with pytest.raises(SystemExit):
        Switch("invalid-date-text")