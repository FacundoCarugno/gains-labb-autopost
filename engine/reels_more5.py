"""Dias 33-39: tanda 5. Datos verificados contra resumenes/abstracts el 03/11/2026."""
from reels_more import L, hook, cta, caption
from reels_more2 import tips3
from reels_more3 import stat, out

# ------------------------------------------------------------------ DIA 33
def reel_music(handle):
    S = [
        hook(33, "thirty-three", "treinta y tres", "TEACHING YOU: MUSIC", "Enseñándote: música", ["DOES MUSIC", "BOOST YOUR WORKOUT?"],
             "music and exercise", "la música y el ejercicio",
             ("Does listening to music really help you train?", ["Does listening to music", "really help you train?"]),
             ("¿Escuchar música realmente ayuda a entrenar?", ["¿Escuchar música realmente", "ayuda a entrenar?"]), icon="bolt"),
        stat("MUSIC IN EXERCISE · META-ANALYSIS", "139", 190, 0.6, "bolt", ["studies, 3,599 participants", "pooled together"],
             [L("A meta-analysis pooled one hundred thirty-nine studies, with three thousand five hundred ninety-nine participants.",
                "Un metaanálisis reunió 139 estudios, con 3.599 participantes.",
                ["139 studies,", "3,599 participants."], ["139 estudios,", "3.599 participantes."]),
              L("Listening to music was linked to better physical performance, a small to moderate effect.",
                "Escuchar música se asoció con mejor rendimiento físico, un efecto de pequeño a moderado.",
                ["Music was linked to better", "performance: a small effect."], ["La música se asoció con mejor", "rendimiento: un efecto pequeño."])],
             count=(139, "{:.0f}")),
        tips3("WHAT IMPROVED", ["bolt", "heart", "flask"],
              [("Mood: the biggest effect", "Ánimo: el mayor efecto"),
               ("Perceived effort: a bit lower", "Esfuerzo percibido: algo menor"),
               ("Heart rate: no benefit", "Frecuencia cardíaca: sin beneficio")],
              [L("The biggest effect was on mood, with more positive feelings during exercise.", "El mayor efecto fue sobre el ánimo, con sensaciones más positivas durante el ejercicio.",
                 ["Biggest effect: mood, with more", "positive feelings while exercising."], ["Mayor efecto: el ánimo, con más", "sensaciones positivas al entrenar."]),
               L("Perceived effort was a little lower, and oxygen use slightly more efficient.", "El esfuerzo percibido fue algo menor y el uso de oxígeno, algo más eficiente.",
                 ["Perceived effort a little lower,", "oxygen use slightly more efficient."], ["Esfuerzo percibido algo menor,", "uso de oxígeno algo más eficiente."]),
               L("But heart rate showed no significant benefit.", "Pero la frecuencia cardíaca no mostró un beneficio significativo.",
                 ["But heart rate showed no", "significant benefit."], ["Pero la frecuencia cardíaca no", "mostró beneficio significativo."])]),
        cta(33, "thirty-four", "treinta y cuatro", "DAY 34 TOMORROW: WALKING AFTER MEALS", "Mañana, día 34: caminar después de comer"),
    ]
    cap = caption(33, "music and exercise", "música y ejercicio",
                  "Does listening to music really help you train? A meta-analytic review of 139 studies (598 effect sizes, 3,599 participants) found that music was linked to better physical performance (g = 0.31), more positive affect (g = 0.48), lower perceived exertion (g = 0.22) and slightly more efficient oxygen consumption (g = 0.15). Heart rate showed no significant benefit. The authors conclude the results support music listening across a range of physical activities.",
                  "¿Escuchar música realmente ayuda a entrenar? Una revisión metaanalítica de 139 estudios (598 tamaños de efecto, 3.599 participantes) halló que la música se asoció con mejor rendimiento físico (g = 0,31), afecto más positivo (g = 0,48), menor esfuerzo percibido (g = 0,22) y un consumo de oxígeno algo más eficiente (g = 0,15). La frecuencia cardíaca no mostró un beneficio significativo. Los autores concluyen que los resultados respaldan escuchar música en un rango de actividades físicas.",
                  handle, "Terry et al., Psychol Bull, 2020")
    return out(33, "music", S, cap, "#workoutmusic #gym #motivation #training #fitness", "Terry et al., Psychol Bull, 2020")

# ------------------------------------------------------------------ DIA 34
def reel_walkbreaks(handle):
    S = [
        hook(34, "thirty-four", "treinta y cuatro", "TEACHING YOU: WALKING BREAKS", "Enseñándote: caminar después de comer", ["CAN A SHORT WALK", "LOWER BLOOD SUGAR?"],
             "short walking breaks", "las caminatas cortas",
             ("Can a two-minute walk help your blood sugar?", ["Can a 2-minute walk", "help your blood sugar?"]),
             ("¿Una caminata de dos minutos ayuda a tu glucosa?", ["¿Una caminata de 2 minutos", "ayuda a tu glucosa?"]), icon="walk"),
        stat("WALKING BREAKS VS SITTING", "-17%", 150, 0.17, "walk", ["average blood glucose vs", "prolonged sitting"],
             [L("A meta-analysis of seven studies compared sitting for hours with standing or walking breaks.", "Un metaanálisis de siete estudios comparó estar sentado por horas con pausas de pie o caminando.",
                ["7 studies: sitting for hours vs", "standing or walking breaks."], ["7 estudios: sentado por horas vs", "pausas de pie o caminando."]),
              L("Breaks of two to five minutes every twenty to thirty minutes were used.", "Se usaron pausas de dos a cinco minutos cada veinte a treinta minutos.",
                ["Breaks of 2–5 minutes every", "20–30 minutes."], ["Pausas de 2–5 minutos cada", "20–30 minutos."]),
              L("Light walking lowered average glucose by about seventeen percent. Standing, by about nine and a half.", "Caminar suave bajó la glucosa promedio cerca de un diecisiete por ciento. Estar de pie, cerca de nueve y medio.",
                ["Light walking: about -17% glucose.", "Standing: about -9.5%."], ["Caminar suave: cerca de -17 % glucosa.", "De pie: cerca de -9,5 %."])],
             count=(17, "-{:.0f}%")),
        tips3("READ THE FINE PRINT", ["walk", "flask", "heart"],
              [("Breaks through the day, not only after meals", "Pausas durante el día, no solo tras comer"),
               ("Standing did not lower insulin", "Estar de pie no bajó la insulina"),
               ("Few studies: averages, not guarantees", "Pocos estudios: promedios, no garantías")],
              [L("These were breaks spread through the day, not only after meals.", "Eran pausas repartidas durante el día, no solo después de comer.",
                 ["Breaks spread through the day,", "not only after meals."], ["Pausas repartidas en el día,", "no solo después de comer."]),
               L("Standing did not lower insulin, but short walks helped keep it steadier.", "Estar de pie no bajó la insulina, pero las caminatas cortas ayudaron a mantenerla más estable.",
                 ["Standing did not lower insulin;", "short walks kept it steadier."], ["De pie no bajó la insulina;", "caminar la mantuvo más estable."]),
               L("Only seven studies, so these are averages. If you have diabetes, ask your doctor.", "Solo siete estudios, así que son promedios. Si tienes diabetes, consulta a tu médico.",
                 ["Only 7 studies: averages. If you", "have diabetes, ask your doctor."], ["Solo 7 estudios: promedios. Si", "tienes diabetes, consulta a tu médico."])]),
        cta(34, "thirty-five", "treinta y cinco", "DAY 35 TOMORROW: HYDRATION", "Mañana, día 35: hidratación"),
    ]
    cap = caption(34, "walking breaks", "caminar en pausas",
                  "Can a two-minute walk help your blood sugar? A meta-analysis of 7 studies compared prolonged sitting with standing or light-walking breaks (about 2–5 minutes every 20–30 minutes through the day). Compared with sitting, light-walking breaks lowered average glucose by about 17% and standing by about 9.5%. Standing did not lower insulin, while short walks helped keep it steadier. These were breaks spread across the day, not only after meals, and the evidence base is small. If you have diabetes or take glucose-lowering medication, ask your doctor.",
                  "¿Una caminata de dos minutos ayuda a tu glucosa? Un metaanálisis de 7 estudios comparó estar sentado por mucho tiempo con pausas de pie o caminando suave (unos 2–5 minutos cada 20–30 minutos durante el día). Frente a estar sentado, caminar suave bajó la glucosa promedio cerca de un 17 % y estar de pie cerca de un 9,5 %. Estar de pie no bajó la insulina, mientras que las caminatas cortas ayudaron a mantenerla más estable. Eran pausas repartidas durante el día, no solo después de comer, y la evidencia es pequeña. Si tienes diabetes o tomas medicación para la glucosa, consulta a tu médico.",
                  handle, "Buffey et al., Sports Med, 2022")
    return out(34, "walk-breaks", S, cap, "#walking #bloodsugar #health #sitting #fitness", "Buffey et al., Sports Med, 2022")

# ------------------------------------------------------------------ DIA 35
def reel_hydration(handle):
    S = [
        hook(35, "thirty-five", "treinta y cinco", "TEACHING YOU: HYDRATION", "Enseñándote: hidratación", ["DOES DEHYDRATION", "HURT YOUR LIFTS?"],
             "hydration", "la hidratación",
             ("Does being dehydrated make you lift worse?", ["Does being dehydrated", "make you lift worse?"]),
             ("¿Estar deshidratado te hace levantar peor?", ["¿Estar deshidratado", "te hace levantar peor?"]), icon="flask"),
        stat("BODY MASS LOST AS WATER", "2.5%", 150, 0.25, "flask", ["a squat session got worse", "in the later sets"],
             [L("In a small study, seven trained men lifted while normally hydrated, or after losing about two and a half, or five percent of body mass in fluid.",
                "En un estudio pequeño, siete hombres entrenados levantaron bien hidratados o tras perder cerca de un dos y medio o un cinco por ciento de su masa corporal en líquido.",
                ["7 trained men lifted hydrated, or", "after losing ~2.5% or 5% body mass."], ["7 hombres entrenados levantaron hidratados", "o tras perder ~2,5 % o 5 % de masa."]),
              L("They did six sets of back squats.", "Hicieron seis series de sentadillas.", ["They did six sets of", "back squats."], ["Hicieron seis series de", "sentadillas."]),
              L("Performance dropped in the later sets, in sets two and three at two and a half percent, and two to five at five percent.",
                "El rendimiento cayó en las series posteriores: en las series dos y tres con 2,5 por ciento, y de la dos a la cinco con 5 por ciento.",
                ["Performance dropped: sets 2–3 at", "2.5% loss, sets 2–5 at 5%."], ["El rendimiento cayó: series 2–3 con", "2,5 % de pérdida, 2–5 con 5 %."])]),
        tips3("WHAT IT DID NOT CHANGE", ["flask", "dumbbell", "target"],
              [("Jump height: no significant change", "Altura de salto: sin cambio significativo"),
               ("Peak power: no significant change", "Potencia pico: sin cambio significativo"),
               ("Only 7 men: one small study", "Solo 7 hombres: un estudio pequeño")],
              [L("Jump height did not change significantly.", "La altura de salto no cambió de forma significativa.", ["Jump height did not", "change significantly."], ["La altura de salto no cambió", "de forma significativa."]),
               L("Neither did peak lower-body power or force.", "Tampoco la potencia ni la fuerza pico del tren inferior.", ["Neither did peak lower-body", "power or force."], ["Tampoco la potencia ni la", "fuerza pico del tren inferior."]),
               L("But it was only seven men, so treat it as one small clue. Drink when you are thirsty.", "Pero fueron solo siete hombres, así que tómalo como una pista pequeña. Toma agua cuando tengas sed.",
                 ["Only 7 men: one small clue.", "Drink when you are thirsty."], ["Solo 7 hombres: una pista pequeña.", "Toma agua cuando tengas sed."])]),
        cta(35, "thirty-six", "treinta y seis", "DAY 36 TOMORROW: BLOOD PRESSURE", "Mañana, día 36: presión arterial"),
    ]
    cap = caption(35, "hydration", "hidratación",
                  "Does being dehydrated make you lift worse? In a small crossover study, 7 resistance-trained men did six sets of back squats while normally hydrated or after losing about 2.5% or 5.0% of body mass as fluid (induced by exercise in the heat plus controlled fluid intake). Performance declined significantly in sets 2–3 at 2.5% loss and sets 2–5 at 5.0% loss. Vertical jump height and peak lower-body power and force did not differ significantly. The authors conclude hypohydration reduces resistance exercise performance, but with only 7 participants this is one small clue, not the final word.",
                  "¿Estar deshidratado te hace levantar peor? En un estudio pequeño, 7 hombres entrenados en fuerza hicieron seis series de sentadillas bien hidratados o tras perder cerca de un 2,5 % o un 5,0 % de su masa corporal en líquido (inducido con ejercicio en calor más ingesta de líquido controlada). El rendimiento bajó de forma significativa en las series 2–3 con 2,5 % de pérdida y en las series 2–5 con 5,0 %. La altura de salto vertical y la potencia y fuerza pico del tren inferior no difirieron de forma significativa. Los autores concluyen que la hipohidratación reduce el rendimiento del ejercicio de fuerza, pero con solo 7 participantes es una pista pequeña, no la última palabra.",
                  handle, "Judelson et al., J Strength Cond Res, 2007")
    return out(35, "hydration", S, cap, "#hydration #waterintake #gym #strengthtraining #fitness", "Judelson et al., J Strength Cond Res, 2007")

# ------------------------------------------------------------------ DIA 36
def reel_bp(handle):
    S = [
        hook(36, "thirty-six", "treinta y seis", "TEACHING YOU: BLOOD PRESSURE", "Enseñándote: presión arterial", ["WHICH EXERCISE LOWERS", "BLOOD PRESSURE?"],
             "exercise and blood pressure", "el ejercicio y la presión arterial",
             ("Which type of exercise lowers blood pressure the most?", ["Which exercise lowers", "blood pressure the most?"]),
             ("¿Qué tipo de ejercicio baja más la presión arterial?", ["¿Qué ejercicio baja más", "la presión arterial?"]), icon="heart"),
        {"type": "vs", "tail": 0.7, "head": "SYSTOLIC PRESSURE DROP (mm Hg)", "sub": "93 trials · 5,223 adults",
         "rows": [{"title": "Isometric", "sub": "only 5 groups", "es": "Isométrico", "val": 10.9, "fmt": "-{:.1f}", "win": True},
                  {"title": "Endurance", "sub": "105 groups", "es": "Resistencia aeróbica", "val": 3.5, "fmt": "-{:.1f}"}],
         "lines": [L("A meta-analysis of ninety-three trials and over five thousand adults looked at resting blood pressure.",
                     "Un metaanálisis de 93 ensayos y más de cinco mil adultos analizó la presión arterial en reposo.",
                     ["93 trials, 5,223 adults:", "resting blood pressure."], ["93 ensayos, 5.223 adultos:", "presión arterial en reposo."]),
                   L("Systolic pressure fell about three point five with endurance training, and one point eight with weights.",
                     "La presión sistólica bajó cerca de 3,5 con ejercicio aeróbico y 1,8 con pesas.",
                     ["Systolic: -3.5 mm Hg endurance,", "-1.8 mm Hg weights."], ["Sistólica: -3,5 mm Hg aeróbico,", "-1,8 mm Hg pesas."]),
                   L("Isometric exercise, like wall sits, showed the biggest drop. But that rests on only five groups.",
                     "El ejercicio isométrico, como la sentadilla en pared, mostró la mayor caída. Pero eso se apoya en solo cinco grupos.",
                     ["Isometric (like wall sits): -10.9,", "but based on only 5 groups."], ["Isométrico (como sentadilla en pared):", "-10,9, pero con solo 5 grupos."])]},
        tips3("WHO BENEFITED MOST", ["heart", "walk", "flask"],
              [("Endurance in hypertension: -8.3 / -5.2", "Aeróbico con hipertensión: -8,3 / -5,2"),
               ("Normal blood pressure: only -0.75 / -1.1", "Presión normal: solo -0,75 / -1,1"),
               ("Hypertension: ask your doctor first", "Hipertensión: consulta primero a tu médico")],
              [L("In people with hypertension, endurance training lowered pressure by about eight and five.", "En personas con hipertensión, el ejercicio aeróbico bajó la presión cerca de 8 y 5.",
                 ["With hypertension, endurance", "lowered it ~8.3 / 5.2 mm Hg."], ["Con hipertensión, el aeróbico", "la bajó ~8,3 / 5,2 mm Hg."]),
               L("In people with normal pressure, the drop was small.", "En personas con presión normal, la caída fue pequeña.", ["With normal pressure,", "the drop was small."], ["Con presión normal,", "la caída fue pequeña."]),
               L("If you have high blood pressure, check with your doctor before changing your training.", "Si tienes presión alta, consulta a tu médico antes de cambiar tu entrenamiento.",
                 ["With high blood pressure, check", "with your doctor first."], ["Con presión alta, consulta", "primero a tu médico."])]),
        cta(36, "thirty-seven", "treinta y siete", "DAY 37 TOMORROW: TIME OF DAY", "Mañana, día 37: hora del día"),
    ]
    cap = caption(36, "exercise and blood pressure", "ejercicio y presión arterial",
                  "Which type of exercise lowers blood pressure the most? A meta-analysis of 93 randomized trials (153 groups, 5,223 adults) found that resting systolic/diastolic blood pressure fell by -3.5/-2.5 mm Hg with endurance training, -1.8/-3.2 with dynamic resistance (weights), and -10.9/-6.2 with isometric exercise (only 5 groups, so less certain); combined training lowered only diastolic pressure. In people with hypertension, endurance training lowered pressure by about -8.3/-5.2, versus -0.75/-1.1 in people with normal pressure. If you have high blood pressure or take medication, check with your doctor before changing your training.",
                  "¿Qué tipo de ejercicio baja más la presión arterial? Un metaanálisis de 93 ensayos aleatorizados (153 grupos, 5.223 adultos) halló que la presión sistólica/diastólica en reposo bajó -3,5/-2,5 mm Hg con entrenamiento aeróbico, -1,8/-3,2 con resistencia dinámica (pesas) y -10,9/-6,2 con ejercicio isométrico (solo 5 grupos, por lo que es menos seguro); el entrenamiento combinado solo bajó la presión diastólica. En personas con hipertensión, el aeróbico bajó la presión cerca de -8,3/-5,2, frente a -0,75/-1,1 en personas con presión normal. Si tienes presión alta o tomas medicación, consulta a tu médico antes de cambiar tu entrenamiento.",
                  handle, "Cornelissen & Smart, J Am Heart Assoc, 2013")
    return out(36, "blood-pressure", S, cap, "#bloodpressure #hypertension #heart #health #fitness", "Cornelissen & Smart, J Am Heart Assoc, 2013")

# ------------------------------------------------------------------ DIA 37
def reel_timeofday(handle):
    S = [
        hook(37, "thirty-seven", "treinta y siete", "TEACHING YOU: TIME OF DAY", "Enseñándote: hora del día", ["MORNING OR EVENING", "TRAINING?"],
             "time of day", "la hora del día",
             ("Is there a best time of day to lift?", ["Is there a best", "time of day to lift?"]),
             ("¿Hay una mejor hora del día para entrenar?", ["¿Hay una mejor hora", "del día para entrenar?"]), icon="clock"),
        stat("MORNING VS EVENING LIFTING", "11", 190, 0.55, "clock", ["studies in a meta-analysis,", "all with untrained people"],
             [L("A meta-analysis of eleven studies compared strength training in the morning with training in the evening.", "Un metaanálisis de once estudios comparó el entrenamiento de fuerza por la mañana con el de la tarde-noche.",
                ["11 studies: strength training in", "the morning vs the evening."], ["11 estudios: entrenar fuerza por la", "mañana vs por la tarde-noche."]),
              L("Strength gains were similar in both groups.", "Las ganancias de fuerza fueron similares en ambos grupos.", ["Strength gains were", "similar in both groups."], ["Las ganancias de fuerza fueron", "similares en ambos grupos."]),
              L("Overall, muscle growth was similar too.", "En general, el crecimiento muscular también fue similar.", ["Overall, muscle growth", "was similar too."], ["En general, el crecimiento", "muscular también fue similar."])],
             count=(11, "{:.0f}")),
        tips3("THE FINE PRINT", ["clock", "target", "flask"],
              [("You are stronger in the evening, on average", "En promedio, rindes más fuerza a la tarde-noche"),
               ("All participants were untrained", "Todos los participantes eran principiantes"),
               ("Consistency matters more than the hour", "La constancia importa más que la hora")],
              [L("At baseline, strength was higher in the evening, and training in the morning narrowed that gap.", "Al inicio, la fuerza era mayor a la tarde-noche, y entrenar de mañana redujo esa diferencia.",
                 ["Strength was higher in the evening;", "morning training narrowed the gap."], ["La fuerza era mayor a la tarde-noche;", "entrenar de mañana redujo la brecha."]),
               L("But all participants were untrained, and most studies were short.", "Pero todos los participantes eran principiantes y la mayoría de los estudios eran cortos.",
                 ["But all were untrained, and", "most studies were short."], ["Pero todos eran principiantes y", "la mayoría de los estudios eran cortos."]),
               L("So the best time is the one you can keep up consistently.", "Así que la mejor hora es la que puedes sostener con constancia.",
                 ["So the best time is the one", "you can keep up consistently."], ["Así que la mejor hora es la que", "puedes sostener con constancia."])]),
        cta(37, "thirty-eight", "treinta y ocho", "DAY 38 TOMORROW: BONES", "Mañana, día 38: huesos"),
    ]
    cap = caption(37, "time of day", "hora del día",
                  "Is there a best time of day to lift? A systematic review and meta-analysis of 11 studies (all in untrained participants; most were short, with only one longer than 12 weeks) compared resistance training in the morning versus the evening. Strength gains were similar between groups, and overall muscle growth was similar too. Baseline strength was higher in the evening, and morning training narrowed that gap. The authors conclude that when you train matters less than training consistently. Limits: untrained participants and short studies, so results may differ for experienced lifters.",
                  "¿Hay una mejor hora del día para entrenar? Una revisión sistemática y metaanálisis de 11 estudios (todos con personas no entrenadas; la mayoría cortos, y solo uno de más de 12 semanas) comparó el entrenamiento de fuerza por la mañana contra el de la tarde-noche. Las ganancias de fuerza fueron similares entre grupos y el crecimiento muscular general también. La fuerza basal era mayor a la tarde-noche, y entrenar de mañana redujo esa brecha. Los autores concluyen que importa menos cuándo entrenas que entrenar con constancia. Límites: participantes no entrenados y estudios cortos, así que los resultados pueden ser distintos en personas con experiencia.",
                  handle, "Grgic et al., Chronobiol Int, 2019")
    return out(37, "time-of-day", S, cap, "#morningworkout #eveningworkout #strengthtraining #consistency #gym", "Grgic et al., Chronobiol Int, 2019")

# ------------------------------------------------------------------ DIA 38
def reel_bones(handle):
    S = [
        hook(38, "thirty-eight", "treinta y ocho", "TEACHING YOU: BONES", "Enseñándote: huesos", ["CAN LIFTING WEIGHTS", "STRENGTHEN BONES?"],
             "lifting and bone density", "las pesas y la densidad ósea",
             ("Can lifting weights help your bones after menopause?", ["Can lifting weights help", "your bones after menopause?"]),
             ("¿Levantar pesas ayuda a tus huesos tras la menopausia?", ["¿Levantar pesas ayuda a tus", "huesos tras la menopausia?"]), icon="dumbbell"),
        stat("BONE DENSITY · NETWORK META-ANALYSIS", "19", 190, 0.5, "dumbbell", ["randomized trials, 919", "postmenopausal women"],
             [L("A network meta-analysis pooled nineteen randomized trials with nine hundred nineteen postmenopausal women.", "Un metaanálisis en red reunió 19 ensayos aleatorizados con 919 mujeres posmenopáusicas.",
                ["19 randomized trials,", "919 postmenopausal women."], ["19 ensayos aleatorizados,", "919 mujeres posmenopáusicas."]),
              L("Moderate-intensity resistance training improved bone density in the spine and the femoral neck, compared with usual life.", "El entrenamiento de fuerza de intensidad moderada mejoró la densidad ósea en la columna y el cuello femoral, frente a la vida habitual.",
                ["Moderate-intensity lifting improved", "spine and femoral neck density."], ["La fuerza moderada mejoró la densidad", "de columna y cuello femoral."])],
             count=(19, "{:.0f}")),
        tips3("THE BEST PROTOCOL", ["dumbbell", "calendar", "flask"],
              [("3 days a week at moderate intensity", "3 días por semana a intensidad moderada"),
               ("Moderate = 65–80% of your 1-rep max", "Moderada = 65–80 % de tu 1RM"),
               ("More high-quality studies are needed", "Faltan estudios de mayor calidad")],
              [L("The best-ranked protocol was moderate intensity, three days a week.", "El protocolo mejor ubicado fue de intensidad moderada, tres días por semana.",
                 ["Best-ranked: moderate intensity,", "three days a week."], ["El mejor: intensidad moderada,", "tres días por semana."]),
               L("The authors define moderate as sixty-five to eighty percent of one-rep max.", "Los autores definen moderada como 65 a 80 por ciento del máximo de una repetición.",
                 ["Moderate = 65–80% of", "your one-rep max."], ["Moderada = 65–80 % de", "tu máximo de una repetición."]),
               L("They say more high-quality studies are needed. With osteoporosis, ask your doctor first.", "Dicen que faltan estudios de mayor calidad. Con osteoporosis, consulta primero a tu médico.",
                 ["More quality studies needed. With", "osteoporosis, ask your doctor first."], ["Faltan estudios de calidad. Con", "osteoporosis, consulta a tu médico."])]),
        cta(38, "thirty-nine", "treinta y nueve", "DAY 39 TOMORROW: EXERCISE AND FOCUS", "Mañana, día 39: ejercicio y concentración"),
    ]
    cap = caption(38, "lifting and bones", "pesas y huesos",
                  "Can lifting weights help your bones after menopause? A systematic review and network meta-analysis of 19 randomized controlled trials (919 postmenopausal women) found that moderate-intensity resistance training improved bone mineral density at the lumbar spine and femoral neck compared with a control group living as usual. The top-ranked protocol was moderate intensity (65–80% of 1RM) three days a week; its advantage was significant in programs of 48 weeks or less. The authors say more high-quality studies are needed. If you have osteoporosis or a fracture risk, ask your doctor before starting.",
                  "¿Levantar pesas ayuda a tus huesos tras la menopausia? Una revisión sistemática y metaanálisis en red de 19 ensayos controlados aleatorizados (919 mujeres posmenopáusicas) halló que el entrenamiento de fuerza de intensidad moderada mejoró la densidad mineral ósea en la columna lumbar y el cuello femoral frente a un grupo control que seguía su vida habitual. El protocolo mejor ubicado fue de intensidad moderada (65–80 % del 1RM) tres días por semana; su ventaja fue significativa en programas de 48 semanas o menos. Los autores señalan que faltan estudios de mayor calidad. Si tienes osteoporosis o riesgo de fractura, consulta a tu médico antes de empezar.",
                  handle, "Network meta-analysis, Front Physiol, 2023")
    return out(38, "bones", S, cap, "#bonehealth #osteoporosis #strengthtraining #menopause #fitness", "Network meta-analysis, Front Physiol, 2023")

# ------------------------------------------------------------------ DIA 39
def reel_focus(handle):
    S = [
        hook(39, "thirty-nine", "treinta y nueve", "TEACHING YOU: EXERCISE AND FOCUS", "Enseñándote: ejercicio y concentración", ["WILL ONE WORKOUT", "SHARPEN YOUR MIND?"],
             "exercise and thinking", "el ejercicio y la concentración",
             ("Does one workout make you think better?", ["Does one workout", "make you think better?"]),
             ("¿Una sola sesión te hace pensar mejor?", ["¿Una sola sesión", "te hace pensar mejor?"]), icon="bolt"),
        stat("ONE SESSION · META-ANALYSIS", "79", 190, 0.4, "bolt", ["studies on a single exercise", "session and thinking skills"],
             [L("A meta-analysis pooled seventy-nine studies on a single exercise session and cognitive performance.", "Un metaanálisis reunió 79 estudios sobre una sola sesión de ejercicio y el rendimiento cognitivo.",
                ["79 studies: one exercise session", "and cognitive performance."], ["79 estudios: una sola sesión de", "ejercicio y rendimiento cognitivo."]),
              L("The average effect was positive, but small.", "El efecto promedio fue positivo, pero pequeño.", ["The average effect was", "positive, but small."], ["El efecto promedio fue", "positivo, pero pequeño."]),
              L("It appeared during exercise, right after it, and after a delay.", "Apareció durante el ejercicio, justo después y tras una demora.",
                ["It showed up during, right", "after, and after a delay."], ["Apareció durante, justo", "después y tras una demora."])],
             count=(79, "{:.0f}")),
        tips3("WHAT SHAPED THE RESULT", ["bolt", "clock", "heart"],
              [("Duration and intensity mattered", "La duración y la intensidad importaron"),
               ("So did the type of mental task", "También el tipo de tarea mental"),
               ("And your fitness level", "Y tu nivel de condición física")],
              [L("How long and how hard you exercised changed the result.", "Cuánto tiempo y qué tan fuerte entrenabas cambiaba el resultado.",
                 ["How long and how hard you", "exercised changed the result."], ["Cuánto y qué tan fuerte entrenabas", "cambiaba el resultado."]),
               L("So did the type of mental task, and the person's fitness level.", "También el tipo de tarea mental y el nivel de condición física de la persona.",
                 ["So did the type of mental", "task and your fitness level."], ["También la tarea mental y", "tu nivel de condición física."]),
               L("The authors say effects are generally small, so do not expect miracles.", "Los autores dicen que los efectos son en general pequeños, así que no esperes milagros.",
                 ["The authors say effects are", "generally small. No miracles."], ["Los autores dicen que los efectos", "son pequeños. Sin milagros."])]),
        {"type": "cta", "tail": 1.0, "next_en": "MORE LESSONS COMING", "next_es": "Vienen más lecciones",
         "lines": [L("Save this, and send it to a friend who studies or works long hours.", "Guárdalo y envíaselo a un amigo que estudia o trabaja muchas horas.",
                     ["Save this, and send it to a friend", "who studies or works long hours."], ["Guárdalo y envíaselo a un amigo", "que estudia o trabaja muchas horas."]),
                   L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
                     ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]},
    ]
    cap = (f"Day 39 teaching you: exercise and focus 💪\n"
           f"Does one workout make you think better? A meta-analysis of 79 studies on a single session of exercise and cognitive performance found a positive but small average effect (g ≈ 0.10), seen during exercise, right after it, and after a delay. Exercise duration, intensity, the type of mental task and the person's fitness level all influenced the results. The authors conclude that the effects of acute exercise on cognition are generally small, though larger effects may occur for certain outcomes and exercise parameters.\n\n"
           f"Día 39 enseñándote: ejercicio y concentración 💪\n"
           f"¿Una sola sesión te hace pensar mejor? Un metaanálisis de 79 estudios sobre una sola sesión de ejercicio y el rendimiento cognitivo halló un efecto promedio positivo pero pequeño (g ≈ 0,10), visto durante el ejercicio, justo después y tras una demora. La duración, la intensidad, el tipo de tarea mental y el nivel de condición física influyeron en los resultados. Los autores concluyen que los efectos del ejercicio agudo sobre la cognición son en general pequeños, aunque pueden ser mayores para ciertos resultados y parámetros de ejercicio.\n\n"
           f"Save this 📌 and follow {handle}. / Guárdalo y sigue a {handle}.\n"
           f"Source / Fuente: Chang et al., Brain Res, 2012.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return out(39, "focus", S, cap, "#brainhealth #focus #exercise #productivity #fitness", "Chang et al., Brain Res, 2012")

REELS_MORE5 = {33: reel_music, 34: reel_walkbreaks, 35: reel_hydration, 36: reel_bp, 37: reel_timeofday, 38: reel_bones, 39: reel_focus}
