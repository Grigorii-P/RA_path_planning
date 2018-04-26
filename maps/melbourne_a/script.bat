netconvert --node-files=melbourne_a_50.nod.xml --edge-files=melbourne_a_50.edg.xml --output-file=melbourne_a_50.net.xml  --proj.utm
sumo -c melbourne_a_50.sumocfg --vehroute-output results_a_50.xml

netconvert --node-files=melbourne_a_100.nod.xml --edge-files=melbourne_a_100.edg.xml --output-file=melbourne_a_100.net.xml  --proj.utm
sumo -c melbourne_a_100.sumocfg --vehroute-output results_a_100.xml

netconvert --node-files=melbourne_a_200.nod.xml --edge-files=melbourne_a_200.edg.xml --output-file=melbourne_a_200.net.xml  --proj.utm
sumo -c melbourne_a_200.sumocfg --vehroute-output results_a_200.xml

netconvert --node-files=melbourne_a_500.nod.xml --edge-files=melbourne_a_500.edg.xml --output-file=melbourne_a_500.net.xml  --proj.utm
sumo -c melbourne_a_500.sumocfg --vehroute-output results_a_500.xml

netconvert --node-files=melbourne_a_1000.nod.xml --edge-files=melbourne_a_1000.edg.xml --output-file=melbourne_a_1000.net.xml  --proj.utm
sumo -c melbourne_a_1000.sumocfg --vehroute-output results_a_1000.xml

netconvert --node-files=melbourne_a_1500.nod.xml --edge-files=melbourne_a_1500.edg.xml --output-file=melbourne_a_1500.net.xml  --proj.utm
sumo -c melbourne_a_1500.sumocfg --vehroute-output results_a_1500.xml

netconvert --node-files=melbourne_a_2000.nod.xml --edge-files=melbourne_a_2000.edg.xml --output-file=melbourne_a_2000.net.xml  --proj.utm
sumo -c melbourne_a_2000.sumocfg --vehroute-output results_a_2000.xml