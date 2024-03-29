from app import db

def installDB():
	db.create_all()

	db.engine.execute('''
		INSERT OR IGNORE INTO Games (id, name, image) VALUES
			(1, "memory", "assets\images\games\memory.png"),
			(2, "quiz", "assets\images\games\quiz.png");
	''')

	db.engine.execute('''
		INSERT OR IGNORE INTO Words (name, image, video, videoDefinition) VALUES
			("patata","https://static.arasaac.org/lse-images/22979.jpg","https://static.arasaac.org/lse-acepciones/22920.mp4","https://static.arasaac.org/lse-definiciones/631.mp4"),
			("tomate","https://static.arasaac.org/lse-images/13842.jpg","https://static.arasaac.org/lse-acepciones/13749.mp4","https://static.arasaac.org/lse-definiciones/760.mp4"),
			("casa","https://static.arasaac.org/lse-images/12981.jpg","https://static.arasaac.org/lse-acepciones/12561.mp4","https://static.arasaac.org/lse-definiciones/131.mp4"),
			("hola","https://static.arasaac.org/lse-images/13473.jpg","https://static.arasaac.org/lse-acepciones/13396.mp4","https://static.arasaac.org/lse-definiciones/88.mp4"),
			("adiós","https://static.arasaac.org/lse-images/13599.jpg","https://static.arasaac.org/lse-acepciones/13535.mp4","https://static.arasaac.org/lse-definiciones/89.mp4"),
			("sí","https://static.arasaac.org/lse-images/17384.jpg","https://static.arasaac.org/lse-acepciones/17421.mp4","https://static.arasaac.org/lse-definiciones/5260.mp4"),
			("no","https://static.arasaac.org/lse-images/13572.jpg","https://static.arasaac.org/lse-acepciones/13492.mp4","https://static.arasaac.org/lse-definiciones/209.mp4"),
			("mamá","https://static.arasaac.org/lse-images/13851.jpg","https://static.arasaac.org/lse-acepciones/13764.mp4","https://static.arasaac.org/lse-definiciones/542.mp4"),
			("papá","https://static.arasaac.org/lse-images/13822.jpg","https://static.arasaac.org/lse-acepciones/13800.mp4","https://static.arasaac.org/lse-definiciones/622.mp4"),
			("hermana","https://static.arasaac.org/lse-images/15193.jpg","https://static.arasaac.org/lse-acepciones/15152.mp4","https://static.arasaac.org/lse-definiciones/2722.mp4"),
			("hermano","https://static.arasaac.org/lse-images/15176.jpg","https://static.arasaac.org/lse-acepciones/15155.mp4","https://static.arasaac.org/lse-definiciones/2723.mp4"),
			("abuelo","https://static.arasaac.org/lse-images/15188.jpg","https://static.arasaac.org/lse-acepciones/15160.mp4","https://static.arasaac.org/lse-definiciones/2699.mp4"),
			("abuela","https://static.arasaac.org/lse-images/13588.jpg","https://static.arasaac.org/lse-acepciones/13533.mp4","https://static.arasaac.org/lse-definiciones/221.mp4"),
			("novio","https://static.arasaac.org/lse-images/21086.jpg","https://static.arasaac.org/lse-acepciones/21161.mp4","https://static.arasaac.org/lse-definiciones/4161.mp4"),
			("novia","https://static.arasaac.org/lse-images/21043.jpg","https://static.arasaac.org/lse-acepciones/21192.mp4","https://static.arasaac.org/lse-definiciones/4158.mp4"),
			("rojo","https://static.arasaac.org/lse-images/12763.jpg","https://static.arasaac.org/lse-acepciones/12556.mp4","https://static.arasaac.org/lse-definiciones/70.mp4"),
			("azul","https://static.arasaac.org/lse-images/12882.jpg","https://static.arasaac.org/lse-acepciones/12392.mp4","https://static.arasaac.org/lse-definiciones/73.mp4"),
			("amarillo","https://static.arasaac.org/lse-images/12999.jpg","https://static.arasaac.org/lse-acepciones/12600.mp4","https://static.arasaac.org/lse-definiciones/71.mp4"),
			("naranja","https://static.arasaac.org/lse-images/12801.jpg","https://static.arasaac.org/lse-acepciones/12418.mp4","https://static.arasaac.org/lse-definiciones/78.mp4"),
			("verde","https://static.arasaac.org/lse-images/19772.jpg","https://static.arasaac.org/lse-acepciones/19712.mp4","https://static.arasaac.org/lse-definiciones/72.mp4"),
			("rosa","https://static.arasaac.org/lse-images/12979.jpg","https://static.arasaac.org/lse-acepciones/12490.mp4","https://static.arasaac.org/lse-definiciones/79.mp4"),
			("morado","https://static.arasaac.org/lse-images/12980.jpg","https://static.arasaac.org/lse-acepciones/12520.mp4","https://static.arasaac.org/lse-definiciones/77.mp4"),
			("negro","https://static.arasaac.org/lse-images/12953.jpg","https://static.arasaac.org/lse-acepciones/12612.mp4","https://static.arasaac.org/lse-definiciones/75.mp4"),
			("blanco","https://static.arasaac.org/lse-images/13004.jpg","https://static.arasaac.org/lse-acepciones/12475.mp4","https://static.arasaac.org/lse-definiciones/74.mp4"),
			("a","https://static.arasaac.org/lse-images/13562.jpg","https://static.arasaac.org/lse-acepciones/13515.mp4","https://static.arasaac.org/lse-definiciones/187.mp4"),
			("b","https://static.arasaac.org/lse-images/14366.jpg","https://static.arasaac.org/lse-acepciones/14321.mp4","https://static.arasaac.org/lse-definiciones/1334.mp4"),
			("c","https://static.arasaac.org/lse-images/14397.jpg","https://static.arasaac.org/lse-acepciones/14325.mp4","https://static.arasaac.org/lse-definiciones/1335.mp4"),
			("d","https://static.arasaac.org/lse-images/14389.jpg","https://static.arasaac.org/lse-acepciones/14314.mp4","https://static.arasaac.org/lse-definiciones/1336.mp4"),
			("e","https://static.arasaac.org/lse-images/14405.jpg","https://static.arasaac.org/lse-acepciones/14266.mp4","https://static.arasaac.org/lse-definiciones/1337.mp4"),
			("f","https://static.arasaac.org/lse-images/14489.jpg","https://static.arasaac.org/lse-acepciones/14460.mp4","https://static.arasaac.org/lse-definiciones/1338.mp4"),
			("g","https://static.arasaac.org/lse-images/14480.jpg","https://static.arasaac.org/lse-acepciones/14447.mp4","https://static.arasaac.org/lse-definiciones/1339.mp4"),
			("h","https://static.arasaac.org/lse-images/14518.jpg","https://static.arasaac.org/lse-acepciones/14443.mp4","https://static.arasaac.org/lse-definiciones/1340.mp4"),
			("i","https://static.arasaac.org/lse-images/14523.jpg","https://static.arasaac.org/lse-acepciones/14455.mp4","https://static.arasaac.org/lse-definiciones/1341.mp4"),
			("j","https://static.arasaac.org/lse-images/14486.jpg","https://static.arasaac.org/lse-acepciones/14445.mp4","https://static.arasaac.org/lse-definiciones/1342.mp4"),
			("k","https://static.arasaac.org/lse-images/14491.jpg","https://static.arasaac.org/lse-acepciones/14433.mp4","https://static.arasaac.org/lse-definiciones/1343.mp4"),
			("l","https://static.arasaac.org/lse-images/14516.jpg","https://static.arasaac.org/lse-acepciones/14453.mp4","https://static.arasaac.org/lse-definiciones/1344.mp4"),
			("m","https://static.arasaac.org/lse-images/14525.jpg","https://static.arasaac.org/lse-acepciones/14461.mp4","https://static.arasaac.org/lse-definiciones/1346.mp4"),
			("n","https://static.arasaac.org/lse-images/14487.jpg","https://static.arasaac.org/lse-acepciones/14469.mp4","https://static.arasaac.org/lse-definiciones/1347.mp4"),
			("ñ","https://static.arasaac.org/lse-images/14487.jpg","https://static.arasaac.org/lse-acepciones/14469.mp4","https://static.arasaac.org/lse-definiciones/1347.mp4"),
			("o","https://static.arasaac.org/lse-images/14507.jpg","https://static.arasaac.org/lse-acepciones/14444.mp4","https://static.arasaac.org/lse-definiciones/1348.mp4"),
			("p","https://static.arasaac.org/lse-images/14504.jpg","https://static.arasaac.org/lse-acepciones/14442.mp4","https://static.arasaac.org/lse-definiciones/1349.mp4"),
			("q","https://static.arasaac.org/lse-images/14493.jpg","https://static.arasaac.org/lse-acepciones/14450.mp4","https://static.arasaac.org/lse-definiciones/1350.mp4"),
			("r","https://static.arasaac.org/lse-images/14478.jpg","https://static.arasaac.org/lse-acepciones/14439.mp4","https://static.arasaac.org/lse-definiciones/1351.mp4"),
			("s","https://static.arasaac.org/lse-images/14484.jpg","https://static.arasaac.org/lse-acepciones/14432.mp4","https://static.arasaac.org/lse-definiciones/1352.mp4"),
			("t","https://static.arasaac.org/lse-images/14483.jpg","https://static.arasaac.org/lse-acepciones/14465.mp4","https://static.arasaac.org/lse-definiciones/1353.mp4"),
			("u","https://static.arasaac.org/lse-images/14499.jpg","https://static.arasaac.org/lse-acepciones/14428.mp4","https://static.arasaac.org/lse-definiciones/1354.mp4"),
			("v","https://static.arasaac.org/lse-images/14492.jpg","https://static.arasaac.org/lse-acepciones/14459.mp4","https://static.arasaac.org/lse-definiciones/1355.mp4"),
			("w","https://static.arasaac.org/lse-images/14479.jpg","https://static.arasaac.org/lse-acepciones/14440.mp4","https://static.arasaac.org/lse-definiciones/1356.mp4"),
			("x","https://static.arasaac.org/lse-images/14522.jpg","https://static.arasaac.org/lse-acepciones/14473.mp4","https://static.arasaac.org/lse-definiciones/1357.mp4"),
			("y","https://static.arasaac.org/lse-images/13583.jpg","https://static.arasaac.org/lse-acepciones/13516.mp4","https://static.arasaac.org/lse-definiciones/197.mp4"),
			("z","https://static.arasaac.org/lse-images/14485.jpg","https://static.arasaac.org/lse-acepciones/14446.mp4","https://static.arasaac.org/lse-definiciones/1358.mp4"),
			("lunes","https://static.arasaac.org/lse-images/13628.jpg","https://static.arasaac.org/lse-acepciones/13518.mp4","https://static.arasaac.org/lse-definiciones/211.mp4"),
			("martes","https://static.arasaac.org/lse-images/13587.jpg","https://static.arasaac.org/lse-acepciones/13501.mp4","https://static.arasaac.org/lse-definiciones/212.mp4"),
			("miércoles","https://static.arasaac.org/lse-images/13577.jpg","https://static.arasaac.org/lse-acepciones/13514.mp4","https://static.arasaac.org/lse-definiciones/213.mp4"),
			("jueves","https://static.arasaac.org/lse-images/13556.jpg","https://static.arasaac.org/lse-acepciones/13517.mp4","https://static.arasaac.org/lse-definiciones/214.mp4"),
			("viernes","https://static.arasaac.org/lse-images/13581.jpg","https://static.arasaac.org/lse-acepciones/13523.mp4","https://static.arasaac.org/lse-definiciones/215.mp4"),
			("sábado","https://static.arasaac.org/lse-images/13607.jpg","https://static.arasaac.org/lse-acepciones/13532.mp4","https://static.arasaac.org/lse-definiciones/216.mp4"),
			("domingo","https://static.arasaac.org/lse-images/13600.jpg","https://static.arasaac.org/lse-acepciones/13531.mp4","https://static.arasaac.org/lse-definiciones/217.mp4"),
			("verano","https://static.arasaac.org/lse-images/14004.jpg","https://static.arasaac.org/lse-acepciones/13969.mp4","https://static.arasaac.org/lse-definiciones/782.mp4"),
			("primavera","https://static.arasaac.org/lse-images/14350.jpg","https://static.arasaac.org/lse-acepciones/14328.mp4","https://static.arasaac.org/lse-definiciones/1250.mp4"),
			("otoño","https://static.arasaac.org/lse-images/12858.jpg","https://static.arasaac.org/lse-acepciones/12543.mp4","https://static.arasaac.org/lse-definiciones/1249.mp4"),
			("invierno","https://static.arasaac.org/lse-images/14402.jpg","https://static.arasaac.org/lse-acepciones/14289.mp4","https://static.arasaac.org/lse-definiciones/1246.mp4"),
			("derecha","https://static.arasaac.org/lse-images/20681.jpg","https://static.arasaac.org/lse-acepciones/20475.mp4","https://static.arasaac.org/lse-definiciones/1104.mp4"),
			("izquierda","https://static.arasaac.org/lse-images/14156.jpg","https://static.arasaac.org/lse-acepciones/14067.mp4","https://static.arasaac.org/lse-definiciones/1065.mp4"),
			("arriba","https://static.arasaac.org/lse-images/14155.jpg","https://static.arasaac.org/lse-acepciones/14098.mp4","https://static.arasaac.org/lse-definiciones/1137.mp4"),
			("abajo","https://static.arasaac.org/lse-images/14196.jpg","https://static.arasaac.org/lse-acepciones/14088.mp4","https://static.arasaac.org/lse-definiciones/1144.mp4"),
			("delante","https://static.arasaac.org/lse-images/13474.jpg","https://static.arasaac.org/lse-acepciones/13394.mp4","https://static.arasaac.org/lse-definiciones/62.mp4"),
			("detrás","https://static.arasaac.org/lse-images/13433.jpg","https://static.arasaac.org/lse-acepciones/13383.mp4","https://static.arasaac.org/lse-definiciones/63.mp4"),
			("abeja","https://static.arasaac.org/lse-images/14408.jpg","https://static.arasaac.org/lse-acepciones/14322.mp4","https://static.arasaac.org/lse-definiciones/1167.mp4"),
			("águila","https://static.arasaac.org/lse-images/12732.jpg","https://static.arasaac.org/lse-acepciones/12627.mp4","https://static.arasaac.org/lse-definiciones/1169.mp4"),
			("ballena","https://static.arasaac.org/lse-images/14378.jpg","https://static.arasaac.org/lse-acepciones/14282.mp4","https://static.arasaac.org/lse-definiciones/1174.mp4"),
			("burro","https://static.arasaac.org/lse-images/13014.jpg","https://static.arasaac.org/lse-acepciones/12395.mp4","https://static.arasaac.org/lse-definiciones/301.mp4"),
			("caballo","https://static.arasaac.org/lse-images/12982.jpg","https://static.arasaac.org/lse-acepciones/12610.mp4","https://static.arasaac.org/lse-definiciones/1177.mp4"),
			("cabra","https://static.arasaac.org/lse-images/13247.jpg","https://static.arasaac.org/lse-acepciones/13146.mp4","https://static.arasaac.org/lse-definiciones/5823.mp4"),
			("camello","https://static.arasaac.org/lse-images/12920.jpg","https://static.arasaac.org/lse-acepciones/12447.mp4","https://static.arasaac.org/lse-definiciones/1180.mp4"),
			("cerdo","https://static.arasaac.org/lse-images/12868.jpg","https://static.arasaac.org/lse-acepciones/12456.mp4","https://static.arasaac.org/lse-definiciones/3068.mp4"),
			("cocodrilo","https://static.arasaac.org/lse-images/15619.jpg","https://static.arasaac.org/lse-acepciones/15574.mp4","https://static.arasaac.org/lse-definiciones/3069.mp4"),
			("conejo","https://static.arasaac.org/lse-images/12854.jpg","https://static.arasaac.org/lse-acepciones/12669.mp4","https://static.arasaac.org/lse-definiciones/1189.mp4"),
			("delfín","https://static.arasaac.org/lse-images/15240.jpg","https://static.arasaac.org/lse-acepciones/23215.mp4","https://static.arasaac.org/lse-definiciones/2775.mp4"),
			("elefante","https://static.arasaac.org/lse-images/12917.jpg","https://static.arasaac.org/lse-acepciones/12440.mp4","https://static.arasaac.org/lse-definiciones/1193.mp4"),
			("foca","https://static.arasaac.org/lse-images/12714.jpg","https://static.arasaac.org/lse-acepciones/12375.mp4","https://static.arasaac.org/lse-definiciones/1195.mp4"),
			("gallina","https://static.arasaac.org/lse-images/12751.jpg","https://static.arasaac.org/lse-acepciones/12564.mp4","https://static.arasaac.org/lse-definiciones/2777.mp4"),
			("gato","https://static.arasaac.org/lse-images/14403.jpg","https://static.arasaac.org/lse-acepciones/14327.mp4","https://static.arasaac.org/lse-definiciones/1197.mp4"),
			("jirafa","https://static.arasaac.org/lse-images/13285.jpg","https://static.arasaac.org/lse-acepciones/13177.mp4","https://static.arasaac.org/lse-definiciones/3993.mp4"),
			("león","https://static.arasaac.org/lse-images/12872.jpg","https://static.arasaac.org/lse-acepciones/12451.mp4","https://static.arasaac.org/lse-definiciones/519.mp4"),
			("loro","https://static.arasaac.org/lse-images/13283.jpg","https://static.arasaac.org/lse-acepciones/13120.mp4","https://static.arasaac.org/lse-definiciones/4045.mp4"),
			("pájaro","https://static.arasaac.org/lse-images/13566.jpg","https://static.arasaac.org/lse-acepciones/13545.mp4","https://static.arasaac.org/lse-definiciones/163.mp4"),
			("mariposa","https://static.arasaac.org/lse-images/13620.jpg","https://static.arasaac.org/lse-acepciones/13551.mp4","https://static.arasaac.org/lse-definiciones/164.mp4"),
			("mono","https://static.arasaac.org/lse-images/15621.jpg","https://static.arasaac.org/lse-acepciones/15570.mp4","https://static.arasaac.org/lse-definiciones/3077.mp4"),
			("oso","https://static.arasaac.org/lse-images/14396.jpg","https://static.arasaac.org/lse-acepciones/14336.mp4","https://static.arasaac.org/lse-definiciones/1218.mp4"),
			("pato","https://static.arasaac.org/lse-images/12698.jpg","https://static.arasaac.org/lse-acepciones/12532.mp4","https://static.arasaac.org/lse-definiciones/1223.mp4"),
			("perro","https://static.arasaac.org/lse-images/12969.jpg","https://static.arasaac.org/lse-acepciones/12406.mp4","https://static.arasaac.org/lse-definiciones/1227.mp4"),
			("tiburón","https://static.arasaac.org/lse-images/16558.jpg","https://static.arasaac.org/lse-acepciones/16523.mp4","https://static.arasaac.org/lse-definiciones/4504.mp4"),
			("tigre","https://static.arasaac.org/lse-images/14390.jpg","https://static.arasaac.org/lse-acepciones/14276.mp4","https://static.arasaac.org/lse-definiciones/1236.mp4"),
			("toro","https://static.arasaac.org/lse-images/14744.jpg","https://static.arasaac.org/lse-acepciones/14704.mp4","https://static.arasaac.org/lse-definiciones/1779.mp4"),
			("tortuga","https://static.arasaac.org/lse-images/20595.jpg","https://static.arasaac.org/lse-acepciones/20494.mp4","https://static.arasaac.org/lse-definiciones/1237.mp4"),
			("vaca","https://static.arasaac.org/lse-images/12998.jpg","https://static.arasaac.org/lse-acepciones/12415.mp4","https://static.arasaac.org/lse-definiciones/775.mp4"),
			("calor","https://static.arasaac.org/lse-images/13664.jpg","https://static.arasaac.org/lse-acepciones/13720.mp4","https://static.arasaac.org/lse-definiciones/313.mp4"),
			("frío","https://static.arasaac.org/lse-images/13479.jpg","https://static.arasaac.org/lse-acepciones/13400.mp4","https://static.arasaac.org/lse-definiciones/81.mp4"),
			("lluvia","https://static.arasaac.org/lse-images/13840.jpg","https://static.arasaac.org/lse-acepciones/13780.mp4","https://static.arasaac.org/lse-definiciones/530.mp4"),
			("nieve","https://static.arasaac.org/lse-images/13887.jpg","https://static.arasaac.org/lse-acepciones/13776.mp4","https://static.arasaac.org/lse-definiciones/590.mp4"),
			("nube","https://static.arasaac.org/lse-images/16418.jpg","https://static.arasaac.org/lse-acepciones/16404.mp4","https://static.arasaac.org/lse-definiciones/4164.mp4"),
			("nublado","https://static.arasaac.org/lse-images/14354.jpg","https://static.arasaac.org/lse-acepciones/14280.mp4","https://static.arasaac.org/lse-definiciones/1248.mp4"),
			("sol","https://static.arasaac.org/lse-images/12922.jpg","https://static.arasaac.org/lse-acepciones/12536.mp4","https://static.arasaac.org/lse-definiciones/730.mp4"),
			("tormenta","https://static.arasaac.org/lse-images/16544.jpg","https://static.arasaac.org/lse-acepciones/16502.mp4","https://static.arasaac.org/lse-definiciones/4529.mp4"),
			("viento","https://static.arasaac.org/lse-images/13993.jpg","https://static.arasaac.org/lse-acepciones/13956.mp4","https://static.arasaac.org/lse-definiciones/787.mp4"),
			("bien","https://static.arasaac.org/lse-images/22365.jpg","https://static.arasaac.org/lse-acepciones/22403.mp4","https://static.arasaac.org/lse-definiciones/284.mp4"),
			("mal","https://static.arasaac.org/lse-images/22648.jpg","https://static.arasaac.org/lse-acepciones/22702.mp4","https://static.arasaac.org/lse-definiciones/538.mp4"),
			("boca","https://static.arasaac.org/lse-images/12822.jpg","https://static.arasaac.org/lse-acepciones/12409.mp4","https://static.arasaac.org/lse-definiciones/3180.mp4"),
			("brazo","https://static.arasaac.org/lse-images/12831.jpg","https://static.arasaac.org/lse-acepciones/12545.mp4","https://static.arasaac.org/lse-definiciones/3209.mp4"),
			("cabeza","https://static.arasaac.org/lse-images/12948.jpg","https://static.arasaac.org/lse-acepciones/12654.mp4","https://static.arasaac.org/lse-definiciones/3165.mp4"),
			("culo","https://static.arasaac.org/lse-images/15695.jpg","https://static.arasaac.org/lse-acepciones/15680.mp4","https://static.arasaac.org/lse-definiciones/3205.mp4"),
			("dedo","https://static.arasaac.org/lse-images/13008.jpg","https://static.arasaac.org/lse-acepciones/12498.mp4","https://static.arasaac.org/lse-definiciones/3216.mp4"),
			("dientes","https://static.arasaac.org/lse-images/12731.jpg","https://static.arasaac.org/lse-acepciones/12426.mp4","https://static.arasaac.org/lse-definiciones/184.mp4"),
			("lengua","https://static.arasaac.org/lse-images/14362.jpg","https://static.arasaac.org/lse-acepciones/14333.mp4","https://static.arasaac.org/lse-definiciones/1308.mp4"),
			("mano","https://static.arasaac.org/lse-images/12828.jpg","https://static.arasaac.org/lse-acepciones/12463.mp4","https://static.arasaac.org/lse-definiciones/3215.mp4"),
			("nariz","https://static.arasaac.org/lse-images/12827.jpg","https://static.arasaac.org/lse-acepciones/12414.mp4","https://static.arasaac.org/lse-definiciones/3179.mp4"),
			("oreja","https://static.arasaac.org/lse-images/16419.jpg","https://static.arasaac.org/lse-acepciones/16394.mp4","https://static.arasaac.org/lse-definiciones/4182.mp4"),
			("pelo","https://static.arasaac.org/lse-images/15631.jpg","https://static.arasaac.org/lse-acepciones/15608.mp4","https://static.arasaac.org/lse-definiciones/3168.mp4"),
			("pie","https://static.arasaac.org/lse-images/12745.jpg","https://static.arasaac.org/lse-acepciones/12664.mp4","https://static.arasaac.org/lse-definiciones/3222.mp4"),
			("pierna","https://static.arasaac.org/lse-images/19890.jpg","https://static.arasaac.org/lse-acepciones/19942.mp4","https://static.arasaac.org/lse-definiciones/3219.mp4");
	''')

def create_test_data():
	db.engine.execute('''
		INSERT OR IGNORE INTO User (id, name, password, email, role) VALUES
			(1, "existing_teacher_test", "111111", "existing_teacher_test@yopmail.com", "TEACHER"),
			(2, "existing_student_test", "111111", "existing_student_test@yopmail.com", "STUDENT");
	''')

	db.engine.execute('''
		INSERT OR IGNORE INTO Teacher (id, userId, schoolName) VALUES
			(1, 1, "existing_school_test");
	''')

	db.engine.execute('''
		INSERT OR IGNORE INTO Classroom (id, teacherId, name, classroomCode) VALUES
			(1, 1, "existing_classroom_test", "codeTest");
	''')

	db.engine.execute('''
		INSERT OR IGNORE INTO Student (id, userId, classroomId) VALUES
			(1, 2, 1);
	''')

installDB()