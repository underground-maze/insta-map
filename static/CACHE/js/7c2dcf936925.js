var polygons=[[new google.maps.LatLng(85,180),new google.maps.LatLng(85,90),new google.maps.LatLng(85,0),new google.maps.LatLng(85,-90),new google.maps.LatLng(85,-180),new google.maps.LatLng(0,-180),new google.maps.LatLng(-85,-180),new google.maps.LatLng(-85,-90),new google.maps.LatLng(-85,0),new google.maps.LatLng(-85,90),new google.maps.LatLng(-85,180),new google.maps.LatLng(0,180),new google.maps.LatLng(85,180),],[new google.maps.LatLng(55.8993274985153,21.099576388685424),new google.maps.LatLng(55.89712840672199,21.099416266042773),new google.maps.LatLng(55.894943949521746,21.0989369637046),new google.maps.LatLng(55.89278866411682,21.098141671348873),new google.maps.LatLng(55.890676893575986,21.097035681515013),new google.maps.LatLng(55.888622691383766,21.09562635438289),new google.maps.LatLng(55.886639727916844,21.093923068792044),new google.maps.LatLng(55.884741199469914,21.091937159827058),new google.maps.LatLng(55.88293974043657,21.089681843384444),new google.maps.LatLng(55.88124733922944,21.087172128223024),new google.maps.LatLng(55.87967525849935,21.084424716083127),new google.maps.LatLng(55.87823396018417,21.08145789053925),new google.maps.LatLng(55.876933035886395,21.0782913953259),new google.maps.LatLng(55.87578114304259,21.07494630294628),new google.maps.LatLng(55.87478594730958,21.07144487443828),new google.maps.LatLng(55.87395407155077,21.067810411230926),new google.maps.LatLng(55.873291051762095,21.064067100077217),new google.maps.LatLng(55.87280130023085,21.06023985209528),new google.maps.LatLng(55.872488076172665,21.05635413698898),new google.maps.LatLng(55.872353464041986,21.05243581355125),new google.maps.LatLng(55.87239835966032,21.048510957578095),new google.maps.LatLng(55.872622464254746,21.04460568833846),new google.maps.LatLng(55.873024286446146,21.04074599475481),new google.maps.LatLng(55.873601152174146,21.036957562451143),new google.maps.LatLng(55.8743492224925,21.033265602819384),new google.maps.LatLng(55.87526351911666,21.029694685241758),new google.maps.LatLng(55.87633795755344,21.026268573585583),new google.maps.LatLng(55.877565387592306,21.023010068058664),new google.maps.LatLng(55.87893764088888,21.019940853477664),new google.maps.LatLng(55.88044558532386,21.017081354959235),new google.maps.LatLng(55.88207918577584,21.014450601994234),new google.maps.LatLng(55.88382757090332,21.0120661018096),new google.maps.LatLng(55.88567910549176,21.00994372286065),new google.maps.LatLng(55.88762146788394,21.008097589229116),new google.maps.LatLng(55.889641731978614,21.006539986629726),new google.maps.LatLng(55.89172645325155,21.005281280650795),new google.maps.LatLng(55.893861758226635,21.004329847772937),new google.maps.LatLng(55.89603343680155,21.003692019624985),new google.maps.LatLng(55.898227036813694,21.003372040848024),new google.maps.LatLng(55.9004279602169,21.003372040848024),new google.maps.LatLng(55.90262156022904,21.003692019624985),new google.maps.LatLng(55.90479323880396,21.004329847772937),new google.maps.LatLng(55.906928543779046,21.005281280650795),new google.maps.LatLng(55.90901326505198,21.006539986629726),new google.maps.LatLng(55.91103352914666,21.008097589229116),new google.maps.LatLng(55.912975891538835,21.00994372286065),new google.maps.LatLng(55.914827426127275,21.0120661018096),new google.maps.LatLng(55.91657581125476,21.014450601994234),new google.maps.LatLng(55.918209411706734,21.017081354959235),new google.maps.LatLng(55.91971735614172,21.019940853477664),new google.maps.LatLng(55.92108960943829,21.023010068058664),new google.maps.LatLng(55.92231703947716,21.026268573585583),new google.maps.LatLng(55.92339147791394,21.029694685241758),new google.maps.LatLng(55.9243057745381,21.033265602819384),new google.maps.LatLng(55.92505384485645,21.036957562451143),new google.maps.LatLng(55.92563071058445,21.04074599475481),new google.maps.LatLng(55.92603253277585,21.04460568833846),new google.maps.LatLng(55.92625663737027,21.048510957578095),new google.maps.LatLng(55.92630153298861,21.05243581355125),new google.maps.LatLng(55.92616692085793,21.05635413698898),new google.maps.LatLng(55.92585369679975,21.06023985209528),new google.maps.LatLng(55.9253639452685,21.064067100077217),new google.maps.LatLng(55.924700925479826,21.067810411230926),new google.maps.LatLng(55.92386904972101,21.07144487443828),new google.maps.LatLng(55.92287385398801,21.07494630294628),new google.maps.LatLng(55.9217219611442,21.0782913953259),new google.maps.LatLng(55.92042103684643,21.08145789053925),new google.maps.LatLng(55.91897973853125,21.084424716083127),new google.maps.LatLng(55.91740765780116,21.087172128223024),new google.maps.LatLng(55.91571525659403,21.089681843384444),new google.maps.LatLng(55.91391379756068,21.091937159827058),new google.maps.LatLng(55.91201526911375,21.093923068792044),new google.maps.LatLng(55.91003230564683,21.09562635438289),new google.maps.LatLng(55.90797810345461,21.097035681515013),new google.maps.LatLng(55.905866332913774,21.098141671348873),new google.maps.LatLng(55.90371104750885,21.0989369637046),new google.maps.LatLng(55.901526590308606,21.099416266042773),new google.maps.LatLng(55.8993274985153,21.099576388685424),],[new google.maps.LatLng(48.473462956246166,35.0822393002453),new google.maps.LatLng(48.47126386445286,35.08210388992735),new google.maps.LatLng(48.469079407252615,35.08169856010684),new google.maps.LatLng(48.46692412184769,35.08102600818684),new google.maps.LatLng(48.464812351306854,35.08009070988941),new google.maps.LatLng(48.462758149114634,35.07889888947042),new google.maps.LatLng(48.46077518564771,35.07745847829811),new google.maps.LatLng(48.45887665720078,35.0757790620712),new google.maps.LatLng(48.45707519816744,35.073871817027566),new google.maps.LatLng(48.45538279696031,35.07174943556832),new google.maps.LatLng(48.453810716230215,35.06942604179191),new google.maps.LatLng(48.45236941791504,35.066917097500564),new google.maps.LatLng(48.451068493617264,35.06423929930461),new google.maps.LatLng(48.449916600773456,35.061410467509226),new google.maps.LatLng(48.44892140504045,35.0584494275233),new google.maps.LatLng(48.44808952928164,35.05537588457939),new google.maps.LatLng(48.44742650949296,35.052210292598694),new google.maps.LatLng(48.446936757961716,35.04897371807356),new google.maps.LatLng(48.446623533903534,35.04568769987345),new google.maps.LatLng(48.446488921772854,35.04237410590733),new google.maps.LatLng(48.44653381739119,35.03905498759634),new google.maps.LatLng(48.446757921985615,35.035752433125225),new google.maps.LatLng(48.447159744177014,35.03248842044911),new google.maps.LatLng(48.447736609905014,35.029284671033835),new google.maps.LatLng(48.448484680223366,35.02616250530316),new google.maps.LatLng(48.449398976847526,35.023142700754924),new google.maps.LatLng(48.45047341528431,35.02024535369014),new google.maps.LatLng(48.451700845323174,35.017489745475515),new google.maps.LatLng(48.45307309861975,35.01489421422906),new google.maps.LatLng(48.45458104305473,35.012476032783),new google.maps.LatLng(48.456214643506705,35.01025129373587),new google.maps.LatLng(48.45796302863419,35.00823480235899),new google.maps.LatLng(48.45981456322263,35.006439978069764),new google.maps.LatLng(48.46175692561481,35.00487876512772),new google.maps.LatLng(48.46377718970948,35.0035615531474),new google.maps.LatLng(48.46586191098242,35.002497107957204),new google.maps.LatLng(48.4679972159575,35.00169251326426),new google.maps.LatLng(48.47016889453242,35.0011531235135),new google.maps.LatLng(48.47236249454456,35.00088252825472),new google.maps.LatLng(48.47456341794777,35.00088252825472),new google.maps.LatLng(48.47675701795991,35.0011531235135),new google.maps.LatLng(48.47892869653483,35.00169251326426),new google.maps.LatLng(48.481064001509914,35.002497107957204),new google.maps.LatLng(48.48314872278285,35.0035615531474),new google.maps.LatLng(48.485168986877525,35.00487876512772),new google.maps.LatLng(48.4871113492697,35.006439978069764),new google.maps.LatLng(48.48896288385814,35.00823480235899),new google.maps.LatLng(48.49071126898563,35.01025129373587),new google.maps.LatLng(48.4923448694376,35.012476032783),new google.maps.LatLng(48.493852813872586,35.01489421422906),new google.maps.LatLng(48.49522506716916,35.017489745475515),new google.maps.LatLng(48.496452497208026,35.02024535369014),new google.maps.LatLng(48.49752693564481,35.023142700754924),new google.maps.LatLng(48.498441232268966,35.02616250530316),new google.maps.LatLng(48.49918930258732,35.029284671033835),new google.maps.LatLng(48.49976616831532,35.03248842044911),new google.maps.LatLng(48.50016799050672,35.035752433125225),new google.maps.LatLng(48.50039209510114,35.03905498759634),new google.maps.LatLng(48.50043699071948,35.04237410590733),new google.maps.LatLng(48.5003023785888,35.04568769987345),new google.maps.LatLng(48.49998915453062,35.04897371807356),new google.maps.LatLng(48.49949940299937,35.052210292598694),new google.maps.LatLng(48.498836383210694,35.05537588457939),new google.maps.LatLng(48.49800450745188,35.0584494275233),new google.maps.LatLng(48.49700931171888,35.061410467509226),new google.maps.LatLng(48.49585741887507,35.06423929930461),new google.maps.LatLng(48.494556494577296,35.066917097500564),new google.maps.LatLng(48.49311519626212,35.06942604179191),new google.maps.LatLng(48.491543115532025,35.07174943556832),new google.maps.LatLng(48.489850714324895,35.073871817027566),new google.maps.LatLng(48.48804925529155,35.0757790620712),new google.maps.LatLng(48.48615072684462,35.07745847829811),new google.maps.LatLng(48.4841677633777,35.07889888947042),new google.maps.LatLng(48.48211356118548,35.08009070988941),new google.maps.LatLng(48.48000179064464,35.08102600818684),new google.maps.LatLng(48.47784650523972,35.08169856010684),new google.maps.LatLng(48.475662048039474,35.08210388992735),new google.maps.LatLng(48.473462956246166,35.0822393002453),],[new google.maps.LatLng(55.74342335798381,37.61750047704807),new google.maps.LatLng(55.7412242661905,37.617340994751004),new google.maps.LatLng(55.739039808990256,37.6168636091882),new google.maps.LatLng(55.73688452358533,37.61607149728181),new google.maps.LatLng(55.734772753044496,37.61496993040588),new google.maps.LatLng(55.732718550852276,37.61356623930622),new google.maps.LatLng(55.730735587385354,37.61186976531552),new google.maps.LatLng(55.728837058938424,37.609891798188265),new google.maps.LatLng(55.72703559990508,37.60764550096937),new google.maps.LatLng(55.72534319869795,37.605145822396196),new google.maps.LatLng(55.72377111796786,37.60240939741724),new google.maps.LatLng(55.72232981965268,37.59945443648925),new google.maps.LatLng(55.721028895354905,37.59630060438968),new google.maps.LatLng(55.7198770025111,37.5929688893508),new google.maps.LatLng(55.71888180677809,37.5894814633865),new google.maps.LatLng(55.71804993101928,37.585861534741184),new google.maps.LatLng(55.717386911230605,37.58213319344274),new google.maps.LatLng(55.71689715969936,37.578321250987386),new google.maps.LatLng(55.716583935641175,37.57445107522323),new google.maps.LatLng(55.716449323510496,37.57054842153144),new google.maps.LatLng(55.71649421912883,37.566639261428456),new google.maps.LatLng(55.716718323723256,37.56274960972979),new google.maps.LatLng(55.717120145914656,37.55890535142576),new google.maps.LatLng(55.717697011642656,37.5551320694211),new google.maps.LatLng(55.71844508196101,37.55145487428502),new google.maps.LatLng(55.71935937858517,37.54789823714445),new google.maps.LatLng(55.72043381702195,37.54448582683276),new google.maps.LatLng(55.721661247060815,37.541240352377564),new google.maps.LatLng(55.72303350035739,37.5381834118759),new google.maps.LatLng(55.72454144479237,37.53533534876244),new google.maps.LatLng(55.72617504524435,37.532715116427305),new google.maps.LatLng(55.72792343037183,37.530340152084385),new google.maps.LatLng(55.72977496496027,37.52822626072955),new google.maps.LatLng(55.73171732735245,37.52638750996097),new google.maps.LatLng(55.733737591447124,37.524836136361664),new google.maps.LatLng(55.73582231272006,37.52358246406696),new google.maps.LatLng(55.737957617695145,37.522634836059154),new google.maps.LatLng(55.74012929627006,37.52199955864628),new google.maps.LatLng(55.742322896282204,37.5216808594947),new google.maps.LatLng(55.74452381968541,37.5216808594947),new google.maps.LatLng(55.74671741969755,37.52199955864628),new google.maps.LatLng(55.74888909827247,37.522634836059154),new google.maps.LatLng(55.751024403247555,37.52358246406696),new google.maps.LatLng(55.75310912452049,37.524836136361664),new google.maps.LatLng(55.75512938861517,37.52638750996097),new google.maps.LatLng(55.757071751007345,37.52822626072955),new google.maps.LatLng(55.758923285595785,37.530340152084385),new google.maps.LatLng(55.76067167072327,37.532715116427305),new google.maps.LatLng(55.762305271175244,37.53533534876244),new google.maps.LatLng(55.76381321561023,37.5381834118759),new google.maps.LatLng(55.7651854689068,37.541240352377564),new google.maps.LatLng(55.76641289894567,37.54448582683276),new google.maps.LatLng(55.76748733738245,37.54789823714445),new google.maps.LatLng(55.76840163400661,37.55145487428502),new google.maps.LatLng(55.76914970432496,37.5551320694211),new google.maps.LatLng(55.76972657005296,37.55890535142576),new google.maps.LatLng(55.77012839224436,37.56274960972979),new google.maps.LatLng(55.77035249683878,37.566639261428456),new google.maps.LatLng(55.77039739245712,37.57054842153144),new google.maps.LatLng(55.77026278032644,37.57445107522323),new google.maps.LatLng(55.76994955626826,37.578321250987386),new google.maps.LatLng(55.76945980473701,37.58213319344274),new google.maps.LatLng(55.768796784948336,37.585861534741184),new google.maps.LatLng(55.76796490918952,37.5894814633865),new google.maps.LatLng(55.76696971345652,37.5929688893508),new google.maps.LatLng(55.76581782061271,37.59630060438968),new google.maps.LatLng(55.76451689631494,37.59945443648925),new google.maps.LatLng(55.76307559799976,37.60240939741724),new google.maps.LatLng(55.76150351726967,37.605145822396196),new google.maps.LatLng(55.75981111606254,37.60764550096937),new google.maps.LatLng(55.75800965702919,37.609891798188265),new google.maps.LatLng(55.75611112858226,37.61186976531552),new google.maps.LatLng(55.75412816511534,37.61356623930622),new google.maps.LatLng(55.75207396292312,37.61496993040588),new google.maps.LatLng(55.749962192382284,37.61607149728181),new google.maps.LatLng(55.74780690697736,37.6168636091882),new google.maps.LatLng(55.745622449777116,37.617340994751004),new google.maps.LatLng(55.74342335798381,37.61750047704807),],[new google.maps.LatLng(44.650021356715285,33.54394182867877),new google.maps.LatLng(44.651028013022,33.54604709753767),new google.maps.LatLng(44.65210245145878,33.54874611780471),new google.maps.LatLng(44.65301674808294,33.55155921319715),new google.maps.LatLng(44.65376481840129,33.55446766302928),new google.maps.LatLng(44.65434168412929,33.557452112047315),new google.maps.LatLng(44.65474350632069,33.560492699235446),new google.maps.LatLng(44.654967610915115,33.5635691899876),new google.maps.LatLng(44.65501250653345,33.566661110765395),new google.maps.LatLng(44.65487789440277,33.5697478853462),new google.maps.LatLng(44.65463223470952,33.5721486765001),new google.maps.LatLng(44.654714507527196,33.57219865941257),new google.maps.LatLng(44.656656869919374,33.573653380731464),new google.maps.LatLng(44.65850840450781,33.575325778574765),new google.maps.LatLng(44.6602567896353,33.577204723410745),new google.maps.LatLng(44.66189039008727,33.57927771117152),new google.maps.LatLng(44.663398334522256,33.58153094646557),new google.maps.LatLng(44.66477058781883,33.58394943438377),new google.maps.LatLng(44.665998017857696,33.58651708028805),new google.maps.LatLng(44.66707245629448,33.589216796918535),new google.maps.LatLng(44.66798675291864,33.59203061810648),new google.maps.LatLng(44.66873482323699,33.59493981833612),new google.maps.LatLng(44.66931168896499,33.59792503735993),new google.maps.LatLng(44.66971351115639,33.60096640903782),new google.maps.LatLng(44.66993761575081,33.604043693543055),new google.maps.LatLng(44.66998251136915,33.607136412054984),new google.maps.LatLng(44.66984789923847,33.61022398304217),new google.maps.LatLng(44.66953467518029,33.6132858592291),new google.maps.LatLng(44.66904492364904,33.616301664334934),new google.maps.LatLng(44.668381903860364,33.61925132867426),new google.maps.LatLng(44.66755002810155,33.622115222717554),new google.maps.LatLng(44.66655483236855,33.62487428772248),new google.maps.LatLng(44.66540293952474,33.62751016256663),new google.maps.LatLng(44.664102015226966,33.630005305937814),new google.maps.LatLng(44.66266071691179,33.632343113068565),new google.maps.LatLng(44.661088636181695,33.63450802623814),new google.maps.LatLng(44.659396234974565,33.636485638306574),new google.maps.LatLng(44.65759477594122,33.638262788591845),new google.maps.LatLng(44.65569624749429,33.63982765045201),new google.maps.LatLng(44.65371328402737,33.64116980998957),new google.maps.LatLng(44.65165908183515,33.64228033535424),new google.maps.LatLng(44.64954731129431,33.64315183618296),new google.maps.LatLng(44.64739202588939,33.64377851278148),new google.maps.LatLng(44.645207568689145,33.64415619472044),new google.maps.LatLng(44.64300847689584,33.644282368588854),new google.maps.LatLng(44.64080938510253,33.64415619472044),new google.maps.LatLng(44.638624927902285,33.64377851278148),new google.maps.LatLng(44.63646964249736,33.64315183618296),new google.maps.LatLng(44.634357871956524,33.64228033535424),new google.maps.LatLng(44.632303669764305,33.64116980998957),new google.maps.LatLng(44.63032070629738,33.63982765045201),new google.maps.LatLng(44.62842217785045,33.638262788591845),new google.maps.LatLng(44.62662071881711,33.636485638306574),new google.maps.LatLng(44.62492831760998,33.63450802623814),new google.maps.LatLng(44.623356236879886,33.632343113068565),new google.maps.LatLng(44.62191493856471,33.630005305937814),new google.maps.LatLng(44.620614014266934,33.62751016256663),new google.maps.LatLng(44.619462121423126,33.62487428772248),new google.maps.LatLng(44.61846692569012,33.622115222717554),new google.maps.LatLng(44.61763504993131,33.61925132867426),new google.maps.LatLng(44.616972030142634,33.616301664334934),new google.maps.LatLng(44.616482278611386,33.6132858592291),new google.maps.LatLng(44.616169054553204,33.61022398304217),new google.maps.LatLng(44.616034442422524,33.607136412054984),new google.maps.LatLng(44.61607933804086,33.604043693543055),new google.maps.LatLng(44.616303442635285,33.60096640903782),new google.maps.LatLng(44.61642202682887,33.60006885132313),new google.maps.LatLng(44.615350701461686,33.599343916802184),new google.maps.LatLng(44.61345217301476,33.59777945858164),new google.maps.LatLng(44.61165071398141,33.596002766693545),new google.maps.LatLng(44.60995831277428,33.59402566472929),new google.maps.LatLng(44.60838623204419,33.59186130997624),new google.maps.LatLng(44.60694493372901,33.58952410585819),new google.maps.LatLng(44.60564400943124,33.58702960608292),new google.maps.LatLng(44.60449211658743,33.584394411134895),new google.maps.LatLng(44.603496920854425,33.581636057801695),new google.maps.LatLng(44.60266504509561,33.578772902469666),new google.maps.LatLng(44.60200202530694,33.57582399896516),new google.maps.LatLng(44.60151227377569,33.572808971754455),new google.maps.LatLng(44.60119904971751,33.5697478853462),new google.maps.LatLng(44.60106443758683,33.566661110765395),new google.maps.LatLng(44.601109333205166,33.5635691899876),new google.maps.LatLng(44.60133343779959,33.560492699235446),new google.maps.LatLng(44.60163381748027,33.558219727189076),new google.maps.LatLng(44.601220083035365,33.557426459024946),new google.maps.LatLng(44.60006819019156,33.554791464897825),new google.maps.LatLng(44.59907299445855,33.5520333217711),new google.maps.LatLng(44.59824111869974,33.54917038463221),new google.maps.LatLng(44.597578098911065,33.54622170585547),new google.maps.LatLng(44.59708834737982,33.54320690841164),new google.maps.LatLng(44.596775123321635,33.5401460552803),new google.maps.LatLng(44.596640511190955,33.53705951593404),new google.maps.LatLng(44.59668540680929,33.533967830782956),new google.maps.LatLng(44.596909511403716,33.53089157448164),new google.maps.LatLng(44.597311333595115,33.52785121900824),new google.maps.LatLng(44.597888199323116,33.524866997426805),new google.maps.LatLng(44.59863626964147,33.52195876923958),new google.maps.LatLng(44.59955056626563,33.51914588822535),new google.maps.LatLng(44.60062500470241,33.516447073643164),new google.maps.LatLng(44.601852434741275,33.513880285658786),new google.maps.LatLng(44.60322468803785,33.51146260582277),new google.maps.LatLng(44.60473263247283,33.50921012339553),new google.maps.LatLng(44.606366232924806,33.507137828276),new google.maps.LatLng(44.60811461805229,33.50525951124628),new google.maps.LatLng(44.60996615264073,33.5035876721963),new google.maps.LatLng(44.61190851503291,33.50213343693912),new google.maps.LatLng(44.61392877912758,33.50090648317043),new google.maps.LatLng(44.61601350040052,33.499914976065135),new google.maps.LatLng(44.618148805375604,33.49916551393944),new google.maps.LatLng(44.62032048395052,33.498663084340116),new google.maps.LatLng(44.62251408396266,33.498411030853276),new google.maps.LatLng(44.62471500736587,33.498411030853276),new google.maps.LatLng(44.62690860737801,33.498663084340116),new google.maps.LatLng(44.62908028595293,33.49916551393944),new google.maps.LatLng(44.631215590928015,33.499914976065135),new google.maps.LatLng(44.63330031220095,33.50090648317043),new google.maps.LatLng(44.635320576295626,33.50213343693912),new google.maps.LatLng(44.637262938687805,33.5035876721963),new google.maps.LatLng(44.639114473276244,33.50525951124628),new google.maps.LatLng(44.64086285840373,33.507137828276),new google.maps.LatLng(44.6424964588557,33.50921012339553),new google.maps.LatLng(44.64400440329069,33.51146260582277),new google.maps.LatLng(44.64537665658726,33.513880285658786),new google.maps.LatLng(44.64660408662613,33.516447073643164),new google.maps.LatLng(44.64767852506291,33.51914588822535),new google.maps.LatLng(44.64859282168707,33.52195876923958),new google.maps.LatLng(44.64934089200542,33.524866997426805),new google.maps.LatLng(44.64991775773342,33.52785121900824),new google.maps.LatLng(44.65031957992482,33.53089157448164),new google.maps.LatLng(44.65054368451924,33.533967830782956),new google.maps.LatLng(44.65058858013758,33.53705951593404),new google.maps.LatLng(44.6504539680069,33.5401460552803),new google.maps.LatLng(44.65014074394872,33.54320690841164),new google.maps.LatLng(44.650021356715285,33.54394182867877),]],markers=[new google.maps.Marker({position:new google.maps.LatLng(55.8993274985153,21.05145419110454),card_id:"11"}),new google.maps.Marker({position:new google.maps.LatLng(48.473462956246166,35.0415439809143),card_id:"10"}),new google.maps.Marker({position:new google.maps.LatLng(44.64300847689584,33.606362910572784),card_id:"8"}),new google.maps.Marker({position:new google.maps.LatLng(44.62361454566427,33.53628627289959),card_id:"7"}),new google.maps.Marker({position:new google.maps.LatLng(55.74342335798381,37.56957072468572),card_id:"4"}),new google.maps.Marker({position:new google.maps.LatLng(44.62803847206014,33.565887808799744),card_id:"2"}),],cards={"2":{"video":"https://www.youtube.com/embed/75s1iq-OIks","longitude":"33.565887808799744","thumb":"https://i.ytimg.com/vi/75s1iq-OIks/maxresdefault.jpg","description":"\u043c\u043a-\u0440\u043d \u0413\u043e\u043b\u043b\u0430\u043d\u0434\u0438\u044f, \u0433. \u0421\u0435\u0432\u0430\u0441\u0442\u043e\u043f\u043e\u043b\u044c, \u0420\u043e\u0441\u0441\u0438\u044f","card_id":2,"latitude":"44.62803847206014"},"4":{"video":"https://www.youtube.com/embed/GxvYf8egZDA","longitude":"37.56957072468572","thumb":"https://i.ytimg.com/vi/GxvYf8egZDA/maxresdefault.jpg","description":"\u043f\u043b\u043e\u0449\u0430\u0434\u044c \u0415\u0432\u0440\u043e\u043f\u044b, \u0433. \u041c\u043e\u0441\u043a\u0432\u0430, \u0420\u043e\u0441\u0441\u0438\u044f","card_id":4,"latitude":"55.74342335798381"},"7":{"video":"https://www.youtube.com/embed/S7siywRXVFM","longitude":"33.53628627289959","thumb":"https://i.ytimg.com/vi/S7siywRXVFM/maxresdefault.jpg","description":"\u043c\u044b\u0441 \u041a\u043e\u043d\u0442\u0440\u0430\u0444\u043e\u0441, \u0433. \u0421\u0435\u0432\u0430\u0441\u0442\u043e\u043f\u043e\u043b\u044c, \u0420\u043e\u0441\u0441\u0438\u044f. \u0414\u0435\u043d\u044c \u0432\u043e\u0435\u043d\u043d\u043e-\u043c\u043e\u0440\u0441\u043a\u043e\u0433\u043e \u0444\u043b\u043e\u0442\u0430.","card_id":7,"latitude":"44.62361454566427"},"8":{"video":"https://www.youtube.com/embed/BO_vuNbhmqQ","longitude":"33.606362910572784","thumb":"https://i.ytimg.com/vi/BO_vuNbhmqQ/maxresdefault.jpg","description":"\u0412\u044a\u0435\u0437\u0434 \u0432 \u0433\u043e\u0440\u043e\u0434-\u0433\u0435\u0440\u043e\u0439 \u0421\u0435\u0432\u0430\u0441\u0442\u043e\u043f\u043e\u043b\u044c \u0441\u043e \u0441\u0442\u043e\u0440\u043e\u043d\u044b \u0421\u0438\u043c\u0444\u0435\u0440\u043e\u043f\u043e\u043b\u044f. \u041d\u0435\u043f\u043e\u0434\u0430\u043b\u0435\u043a\u0443 \u0440\u0430\u0441\u043f\u043e\u043b\u0430\u0433\u0430\u0435\u0442\u0441\u044f \u041c\u0435\u043a\u0435\u043d\u0437\u0438\u0435\u0432\u0441\u043a\u043e\u0435 \u043b\u0435\u0441\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u043e.","card_id":8,"latitude":"44.64300847689584"},"10":{"video":"https://www.youtube.com/embed/-jdaPS8iGUo","longitude":"35.0415439809143","thumb":"https://i.ytimg.com/vi/-jdaPS8iGUo/maxresdefault.jpg","description":"\u0433\u043e\u0440\u043e\u0434 \u0414\u043d\u0435\u043f\u0440\u043e\u043f\u0435\u0442\u0440\u043e\u0432\u043a, \u041d\u0430\u0431\u0435\u0440\u0435\u0436\u043d\u0430\u044f \u0412.\u0418.\u041b\u0435\u043d\u0438\u043d\u0430, \u0441\u0430\u043c\u0430\u044f \u0434\u043b\u0438\u043d\u043d\u0430\u044f \u043d\u0430\u0431\u0435\u0440\u0435\u0436\u043d\u0430\u044f \u0432 \u0415\u0432\u0440\u043e\u043f\u0435.","card_id":10,"latitude":"48.473462956246166"},"11":{"video":"https://www.youtube.com/embed/9LZM9YU3ens","longitude":"21.05145419110454","thumb":"https://i.ytimg.com/vi/9LZM9YU3ens/maxresdefault.jpg","description":"\u0412\u044b\u0445\u043e\u0434 \u043d\u0430 \u043f\u043b\u044f\u0436 \u0438\u0437 \u0411\u043e\u0442\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0441\u0430\u0434\u0430 \u0433\u043e\u0440\u043e\u0434\u0430 \u041f\u0430\u043b\u0430\u043d\u0433\u0430, \u0441\u0430\u043c\u043e\u0433\u043e \u0432\u043e\u043b\u0448\u0435\u0431\u043d\u043e\u0433\u043e \u043d\u0430 \u043f\u043e\u0431\u0435\u0440\u0435\u0436\u044c\u0435 \u0411\u0430\u043b\u0442\u0438\u0439\u0441\u043a\u043e\u0433\u043e \u043c\u043e\u0440\u044f","card_id":11,"latitude":"55.8993274985153"}};