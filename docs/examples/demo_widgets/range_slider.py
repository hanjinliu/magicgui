"""# Range slider widget

A double ended range slider widget.
"""

from magicgui import magicgui


@magicgui(auto_call=True, range_value={"widget_type": "RangeSlider", "max": 500})
def func(range_value: tuple[int, int] = (20, 380)):
    """Double ended range slider."""
    print(range_value)


func.show(run=True)
