import Oslo_model as om
import pickle

approx_t_c = {8:100, 16:300, 32:1000, 64:5000, 128:16000, 256:58000}
objdict = om.create_oslo_obj(6)
objlist = [objdict.keys()]
for key in objdict.keys():
    objdict[key].add_grain(int(1e6+approx_t_c[key]))
    objlist.append(objdict[key])

with open('obj8to256.pickle', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump(objlist, f)

# grains = 1e6 + 16000
#
# Obj = om.Oslo(8)
# Obj.add_grain(int(200))
# A = Obj.avalanches[Obj.t_c + 1000:]



# Getting back the objects:
# with open('objs256.pickle') as f:  # Python 3: open(..., 'rb')
#     obj0, obj1, obj2 = pickle.load(f)
