from printing_functions import print_models
from printing_functions import show_completed_models

designs_in_queue = [
    'celtic braid pendant',
    'necklace chain',
    'pedal wrench',
    'semi-sticky pedal',
]
printed_designs = []

print_models(designs_in_queue, printed_designs)
show_completed_models(printed_designs)