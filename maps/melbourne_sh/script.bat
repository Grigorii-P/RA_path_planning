netconvert --node-files=melbourne_sh_50.nod.xml --edge-files=melbourne_sh_50.edg.xml --output-file=melbourne_sh_50.net.xml --proj.utm
sumo -c melbourne_sh_50.sumocfg --vehroute-output results_sh_50.xml

netconvert --node-files=melbourne_sh_100.nod.xml --edge-files=melbourne_sh_100.edg.xml --output-file=melbourne_sh_100.net.xml --proj.utm
sumo -c melbourne_sh_100.sumocfg --vehroute-output results_sh_100.xml

netconvert --node-files=melbourne_sh_200.nod.xml --edge-files=melbourne_sh_200.edg.xml --output-file=melbourne_sh_200.net.xml --proj.utm
sumo -c melbourne_sh_200.sumocfg --vehroute-output results_sh_200.xml

netconvert --node-files=melbourne_sh_500.nod.xml --edge-files=melbourne_sh_500.edg.xml --output-file=melbourne_sh_500.net.xml --proj.utm
sumo -c melbourne_sh_500.sumocfg --vehroute-output results_sh_500.xml

netconvert --node-files=melbourne_sh_1000.nod.xml --edge-files=melbourne_sh_1000.edg.xml --output-file=melbourne_sh_1000.net.xml --proj.utm
sumo -c melbourne_sh_1000.sumocfg --vehroute-output results_sh_1000.xml

netconvert --node-files=melbourne_sh_1500.nod.xml --edge-files=melbourne_sh_1500.edg.xml --output-file=melbourne_sh_1500.net.xml --proj.utm
sumo -c melbourne_sh_1500.sumocfg --vehroute-output results_sh_1500.xml

netconvert --node-files=melbourne_sh_2000.nod.xml --edge-files=melbourne_sh_2000.edg.xml --output-file=melbourne_sh_2000.net.xml --proj.utm
sumo -c melbourne_sh_2000.sumocfg --vehroute-output results_sh_2000.xml