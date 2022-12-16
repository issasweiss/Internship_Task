from flask import Flask, jsonify

import test_sim

app = Flask(__name__)

@app.route('/grid-power-analysis/', methods=['GET'])
def grid_power_analysis():
    net = test_sim.run_simulation()
    results = {
        "loads": {},
        "generators": {},
        "external_grid": {}
    }
    # Add the results for loads
    for i, load in net.load.iterrows():
        name = load['name']
        res = net.res_load.loc[i]
        results["loads"][name] = (res['p_mw'], res['q_mvar'])
    # Add the results for external grid connections
    for i, ext_grid in net.ext_grid.iterrows():
        name = ext_grid['name']
        res = net.res_ext_grid.loc[i]
        results["external_grid"][name] = (res['p_mw'], res['q_mvar'])

    # Add the results for PV plants
    for i, sgen in net.sgen.iterrows():
        name = sgen['name']
        res = net.res_sgen.loc[i]
        results["generators"][name] = (res['p_mw'], res['q_mvar'])
    return jsonify(results)

if __name__ == '__main__':
    app.run()

