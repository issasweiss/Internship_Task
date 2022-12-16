import pandapower as pp

def run_simulation():
    #create empty net
    net = pp.create_empty_network()

    #create buses
    b1 = pp.create_bus(net, vn_kv=20., name="Bus 1") # trafo1 med-voltage side
    b2 = pp.create_bus(net, vn_kv=0.4, name="Bus 2")  #trafo1 low-voltage side
    b3 = pp.create_bus(net, vn_kv=0.4, name="Bus 3") # first load
    b4 = pp.create_bus(net, vn_kv=0.4, name="Bus 4") # second trafo low voltage side
    b5 = pp.create_bus(net, vn_kv=0.4, name="Bus 5") # Bus for PV plant
    b6 = pp.create_bus(net, vn_kv=0.4, name="Bus 5") # Bus for second Load

    #create bus elements
    pp.create_ext_grid(net, bus=b1, vm_pu=1.02, name="Grid Connection1")
    pp.create_ext_grid(net, bus=b4, vm_pu=1.02, name="Grid Connection2")
    pp.create_load(net, bus=b3, p_mw=0.1, q_mvar=0.05, name="Load1")
    pp.create_load(net, bus=b6, p_mw=0.1, q_mvar=0.05, name="Load2")
    for i in range(5):
        pp.create_sgen(net, bus=b5, p_mw=0.1, q_mvar=0, name=f"PV Plant {i + 1}")

    #create branch elements
    pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV", name="Trafo1")
    pp.create_transformer(net, hv_bus=b1, lv_bus=b4, std_type="0.4 MVA 20/0.4 kV", name="Trafo2")
    pp.create_line(net, from_bus=b2, to_bus=b3, length_km=0.1, name="Line1",std_type="NAYY 4x50 SE")
    pp.create_line(net, from_bus=b4, to_bus=b5, length_km=0.1, name="Line2", std_type="NAYY 4x50 SE") # Type of Cables used assumed the same
    pp.create_line(net, from_bus=b4, to_bus=b6, length_km=0.1, name="Line3", std_type="NAYY 4x50 SE") # Type of Cables used assumed the same

    pp.runpp(net)
    return net


