#
prompt_1 = """
You are skilled at describing routes that are given in a JSON format. You need to discuss how many routes can be found 
from the JSON data. For each route, you should describe the starting and ending locations, along with the duration and 
distance. Additionally, you should clearly mention each step in the route, as well as the order in which they should be 
taken. For each step, you should describe the time needed and the distance to be covered. Finally, you should also 
mention the fastest route.The information should be contained in a single paragraph, with no more than 150 words.
Read the following json data and describe all route according to the rules.
"""

prompt_2 = """
You are skilled at describing routes that are given in a JSON format. You need to discuss how many routes can be found 
from the JSON data. For each route, you should describe the starting and ending locations, along with the duration and 
distance. Additionally, you should clearly mention each step in the route, as well as the order in which they should be 
taken. For each step, you should describe the time needed and the distance to be covered. Finally, you should also 
mention the fastest route.

Information:
{
    "number of route": 1,
    "route_number_1": {
        "bounds": {
            "northeast": {
                "lat": 39.9581711,
                "lng": -82.9399664
            },
            "southwest": {
                "lat": 39.9431651,
                "lng": -82.99788649999999
            }
        },
        "copyrights": "Map data \u00a92024 Google",
        "legs": [
            {
                "distance": {
                    "text": "1.8 mi",
                    "value": 2950
                },
                "duration": {
                    "text": "42 mins",
                    "value": 2524
                },
                "end_address": "Parsons Ave & E Main St, Columbus, OH 43215, USA",
                "end_location": {
                    "lat": 39.957994,
                    "lng": -82.9821264
                },
                "start_address": "919 S High St, Columbus, OH 43206, USA",
                "start_location": {
                    "lat": 39.9432437,
                    "lng": -82.9973455
                },
                "steps": [
                    {
                        "distance": {
                            "text": "144 ft",
                            "value": 44
                        },
                        "duration": {
                            "text": "1 min",
                            "value": 35
                        },
                        "end_location": {
                            "lat": 39.9431651,
                            "lng": -82.9978474
                        },
                        "html_instructions": "Head <b>west</b> toward <b>S Wall St</b>",
                        "polyline": {
                            "points": "glxrFllqyN?^LbA"
                        },
                        "start_location": {
                            "lat": 39.9432437,
                            "lng": -82.9973455
                        },
                        "travel_mode": "WALKING"
                    },
                    {
                        "distance": {
                            "text": "82 ft",
                            "value": 25
                        },
                        "duration": {
                            "text": "1 min",
                            "value": 21
                        },
                        "end_location": {
                            "lat": 39.94338339999999,
                            "lng": -82.99788649999999
                        },
                        "html_instructions": "Turn <b>right</b> onto <b>S Wall St</b>",
                        "maneuver": "turn-right",
                        "polyline": {
                            "points": "ykxrFpoqyNi@F"
                        },
                        "start_location": {
                            "lat": 39.9431651,
                            "lng": -82.9978474
                        },
                        "travel_mode": "WALKING"
                    },
                    {
                        "distance": {
                            "text": "246 ft",
                            "value": 75
                        },
                        "duration": {
                            "text": "1 min",
                            "value": 63
                        },
                        "end_location": {
                            "lat": 39.9434827,
                            "lng": -82.99692089999999
                        },
                        "html_instructions": "Turn <b>right</b> onto <b>Shumacher Alley</b>",
                        "maneuver": "turn-right",
                        "polyline": {
                            "points": "cmxrFxoqyNOwCCi@"
                        },
                        "start_location": {
                            "lat": 39.94338339999999,
                            "lng": -82.99788649999999
                        },
                        "travel_mode": "WALKING"
                    },
                    {
                        "distance": {
                            "text": "138 ft",
                            "value": 42
                        },
                        "duration": {
                            "text": "1 min",
                            "value": 53
                        },
                        "end_location": {
                            "lat": 39.943849,
                            "lng": -82.996994
                        },
                        "html_instructions": "Turn <b>left</b> onto <b>S High St</b>",
                        "maneuver": "turn-left",
                        "polyline": {
                            "points": "wmxrFviqyNiAL"
                        },
                        "start_location": {
                            "lat": 39.9434827,
                            "lng": -82.99692089999999
                        },
                        "travel_mode": "WALKING"
                    },
                    {
                        "distance": {
                            "text": "0.8 mi",
                            "value": 1211
                        },
                        "duration": {
                            "text": "17 mins",
                            "value": 1010
                        },
                        "end_location": {
                            "lat": 39.9441362,
                            "lng": -82.9831
                        },
                        "html_instructions": "Turn <b>right</b> onto <b>E Whittier St</b>",
                        "maneuver": "turn-right",
                        "polyline": {
                            "points": "apxrFdjqyNG]Cm@G{@Am@O_C?c@OuCC_@E_AIsACQIyAGkAKeBEw@CUCi@Ei@AWGgA@S?S@u@@g@@S@I?QDwA?S@m@@SB{@?S?ULmF?SJeFAU@g@?YDwAFyC@YDoCBUByA"
                        },
                        "start_location": {
                            "lat": 39.943849,
                            "lng": -82.996994
                        },
                        "travel_mode": "WALKING"
                    },
                    {
                        "distance": {
                            "text": "1.0 mi",
                            "value": 1553
                        },
                        "duration": {
                            "text": "22 mins",
                            "value": 1342
                        },
                        "end_location": {
                            "lat": 39.957994,
                            "lng": -82.9821264
                        },
                        "html_instructions": "Turn <b>left</b> onto <b>Parsons Ave</b><div style=\"font-size:0.9em\">Pass by Family Dollar (on the left in 0.1 mi)</div>",
                        "maneuver": "turn-left",
                        "polyline": {
                            "points": "{qxrFjsnyNSA?EiCKO?qCKOAW?OA]CO?qAEOAoAEO?oAEQ?E?MAe@AOAM?QAUAOAg@COA]AO?MAm@CK?o@CQ?s@CSGSBqAEQCa@CmACE?U?U@C?U?M@[@M?M?E@g@?ARa@@?MmADSAWAE?SGi@CQD}@CSAKAUAU?OAQGc@AYAE?_BGUCKAUGKCMAKEC?iACSAa@Ac@Cc@AYAo@AUB_@Ce@CG?I?]ASEO?o@A"
                        },
                        "start_location": {
                            "lat": 39.9441362,
                            "lng": -82.9831
                        },
                        "travel_mode": "WALKING"
                    }
                ],
                "traffic_speed_entry": [],
                "via_waypoint": []
            },
            {
                "distance": {
                    "text": "2.2 mi",
                    "value": 3608
                },
                "duration": {
                    "text": "50 mins",
                    "value": 2991
                },
                "end_address": "2212 E Main St, Bexley, OH 43209, USA",
                "end_location": {
                    "lat": 39.9574424,
                    "lng": -82.9399664
                },
                "start_address": "Parsons Ave & E Main St, Columbus, OH 43215, USA",
                "start_location": {
                    "lat": 39.9581711,
                    "lng": -82.98203939999999
                },
                "steps": [
                    {
                        "distance": {
                            "text": "2.2 mi",
                            "value": 3584
                        },
                        "duration": {
                            "text": "49 mins",
                            "value": 2969
                        },
                        "end_location": {
                            "lat": 39.9573033,
                            "lng": -82.9400077
                        },
                        "html_instructions": "Head <b>east</b> on <b>E Main St</b> toward <b>Allen Ave</b><div style=\"font-size:0.9em\">Pass by Dollar General (on the right in 1.1 mi)</div>",
                        "polyline": {
                            "points": "qi{rFvlnyN?]@i@@oD?UD_G?_A@u@?Y?E@gBBaAA[?Q@UD}F?UB}BAUBcC?S?_@?U@i@?U?q@@i@?U@}@@sA@Y@eA?]?e@?S@g@@aC@]@qC?c@@aA?c@DcFAW?O@S?[@U?_A?U@sB@uCBqBAY@kA@qA@S?cA?U?E@S?_A@S?k@@oB@i@?mA@S@yA?Q?mB@U@gB@YBoFF_@GS?]@a@?mA?S?I@_@?U@U?_@AWBmCBY@cE@E?eA@_A?Y?u@@_@@g@?c@BwBIA?UH@BcE?e@@qA?e@@yB@yA@g@?Y@}@?a@@iB?_@?aA@]@gBK??C?UN?@}@?mA@eA?a@BuAEQ?yB?e@?K?[@mA@{@?_@@e@@o@?q@?K@U?o@@{@?[BkB?Y@w@@W@mA?S@_A@U@s@"
                        },
                        "start_location": {
                            "lat": 39.9581711,
                            "lng": -82.98203939999999
                        },
                        "travel_mode": "WALKING"
                    },
                    {
                        "distance": {
                            "text": "62 ft",
                            "value": 19
                        },
                        "duration": {
                            "text": "1 min",
                            "value": 17
                        },
                        "end_location": {
                            "lat": 39.9574056,
                            "lng": -82.94000520000002
                        },
                        "html_instructions": "Turn <b>left</b> onto <b>College Ave</b>",
                        "maneuver": "turn-left",
                        "polyline": {
                            "points": "cd{rF`ffyNQ?C?"
                        },
                        "start_location": {
                            "lat": 39.9573033,
                            "lng": -82.9400077
                        },
                        "travel_mode": "WALKING"
                    },
                    {
                        "distance": {
                            "text": "16 ft",
                            "value": 5
                        },
                        "duration": {
                            "text": "1 min",
                            "value": 5
                        },
                        "end_location": {
                            "lat": 39.9574424,
                            "lng": -82.9399664
                        },
                        "html_instructions": "Slight <b>right</b><div style=\"font-size:0.9em\">Destination will be on the right</div>",
                        "maneuver": "turn-slight-right",
                        "polyline": {
                            "points": "yd{rF`ffyNEG"
                        },
                        "start_location": {
                            "lat": 39.9574056,
                            "lng": -82.94000520000002
                        },
                        "travel_mode": "WALKING"
                    }
                ],
                "traffic_speed_entry": [],
                "via_waypoint": []
            }
        ],
        "overview_polyline": {
            "points": "glxrFllqyN?^LbAi@FOwCCi@iALKkAIiBOcDc@iIu@_MI_B@g@F{BLeHV}NNsHNyGSA?EyCKiEOoCKaEKiAEkDMwBIeACSGSBcBIoBGu@@mABS@g@?ARa@@?MaBB]ASGi@CQD}@C_@Ck@Aa@IcDKa@Ea@KYGmAC}BIiACUB_@Cm@Cg@Ac@Eo@Ac@Q@gA@eEFoKBkELgRDeHBmB@cBBcFDuGBoHJwOD_IHuMB}FDiGF_@GS@_A?aBBuAAw@FgDDoIBwCB{CIA?UH@BcE@wBDaHFkMK??C?UN?@kC@gBBuAEQ?_DBqDFuHDyEDyDBiAU?EG"
        },
        "summary": "E Whittier St and Parsons Ave",
        "warnings": [
            "Walking directions are in beta. Use caution \u2013 This route may be missing sidewalks or pedestrian paths."
        ],
        "waypoint_order": [
            0
        ]
    }
}

Description:
There is only one route provided in the JSON data.
Route 1:
Start location: 919 S High St, Columbus, OH 43206, USA
End location: 2212 E Main St, Bexley, OH 43209, USA
Total distance: 4.0 miles
Estimated time: 92 minutes
Steps:
Head west toward S Wall St (144 ft, 1 min)
Turn right onto S Wall St (82 ft, 1 min)
Turn right onto Schumacher Alley (246 ft, 1 min)
Turn left onto S High St (138 ft, 1 min)
Turn right onto E Whittier St (0.8 mi, 17 mins)
Turn left onto Parsons Ave (1.0 mi, 22 mins)
Head east on E Main St toward Allen Ave (2.2 mi, 49 mins)
Turn left onto College Ave (62 ft, 1 min)
Slight right (16 ft, 1 min)
This is the only route provided in the JSON data, so it is also the fastest route.

Read the following json data and describe all route according to the rules.

Information:
"""