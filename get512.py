import Oslo_model as om
import pickle

A = om.Oslo(512)
av7, std7, h_dict7 = om.stats_on_height(A, num_grains_stdy_state=228000)
grains = 1e6 - 228000 - 20000
A.add_grain(int(grains))
with open('newobj512.pickle', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([av7, std7, h_dict7, A], f)

## Getting back the objects:
# with open('objs256.pickle') as f:  # Python 3: open(..., 'rb')
#     av7, std7, h_dict7, A = pickle.load(f)