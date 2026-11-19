"""Dias 47-53: tanda 7. Datos verificados contra resumenes/notas de prensa el 18/11/2026."""
from reels_more import L, hook, cta, caption
from reels_more2 import tips3
from reels_more3 import stat, out

# ------------------------------------------------------------------ DIA 47
def reel_habit(handle):
    S = [
        hook(47, "forty-seven", "cuarenta y siete", "TEACHING YOU: HABITS", "Enseñándote: hábitos", ["HOW LONG TO BUILD", "A NEW HABIT?"],
             "building a habit", "crear un hábito",
             ("How long does it really take to build a habit?", ["How long does it really", "take to build a habit?"]),
             ("¿Cuánto tarda realmente en formarse un hábito?", ["¿Cuánto tarda realmente", "en formarse un hábito?"]), icon="calendar"),
        stat("HABIT STUDY · 82 PEOPLE", "66", 190, 0.66, "calendar", ["days on average to feel", "automatic (range 18–254)"],
             [L("In a study, eighty-two people tried to turn one daily action into a habit for eighty-four days.", "En un estudio, 82 personas intentaron convertir una acción diaria en hábito durante 84 días.",
                ["82 people tried to make one", "daily action a habit for 84 days."], ["82 personas intentaron hacer de una", "acción diaria un hábito por 84 días."]),
              L("On average, it took sixty-six days for the habit to feel automatic.", "En promedio, tardó 66 días en sentirse automático.",
                ["On average, it took 66 days", "for it to feel automatic."], ["En promedio tardó 66 días", "en sentirse automático."]),
              L("But it varied a lot, from eighteen days to a predicted two hundred fifty-four.", "Pero varió mucho, de 18 días a unos 254 estimados.",
                ["It varied a lot: from 18 days", "to a predicted 254."], ["Varió mucho: de 18 días", "a unos 254 estimados."])],
             count=(66, "{:.0f}")),
        tips3("READ THE FINE PRINT", ["calendar", "dumbbell", "flask"],
              [("Exercise took about 1.5× longer", "El ejercicio tardó ~1,5× más"),
               ("One missed day: little impact", "Un día perdido: poco impacto"),
               ("Small study, self-reported", "Estudio pequeño, autorreportado")],
              [L("Exercise took about one and a half times longer to become a habit than eating or drinking.", "Los hábitos de ejercicio tardaron cerca de una vez y media más que los de comer o beber.",
                 ["Exercise habits took ~1.5× longer", "than eating or drinking habits."], ["Los de ejercicio tardaron ~1,5× más", "que los de comer o beber."]),
               L("A single missed day had little impact, but many missed days lowered the result.", "Un solo día perdido tuvo poco impacto, pero muchos días perdidos bajaron el resultado.",
                 ["One missed day: little impact.", "Many missed days: lower result."], ["Un día perdido: poco impacto.", "Muchos días perdidos: peor resultado."]),
               L("It was a small study, and automaticity was self-reported. So keep going and be patient.", "Fue un estudio pequeño y la automaticidad fue autorreportada. Así que sigue y ten paciencia.",
                 ["Small study, self-reported.", "Keep going and be patient."], ["Estudio pequeño, autorreportado.", "Sigue y ten paciencia."])]),
        cta(47, "forty-eight", "cuarenta y ocho", "DAY 48 TOMORROW: PUSH-UPS AND HEART", "Mañana, día 48: flexiones y corazón"),
    ]
    cap = caption(47, "building a habit", "crear un hábito",
                  "How long does it really take to build a habit? In a study of 96 recruited people (82 completed it), participants tried to turn one daily action (eating, drinking or exercise) into a habit over 84 days. The average time to reach the automaticity plateau was 66 days, with individuals ranging from 18 days to a predicted 254. Exercise habits took about 1.5 times as long as eating or drinking habits, and a single missed day had little impact, though many missed days lowered the level reached. About half did not reach a high automaticity score within 84 days, and automaticity was self-reported. So be patient and keep going.",
                  "¿Cuánto tarda realmente en formarse un hábito? En un estudio con 96 personas reclutadas (82 lo completaron), los participantes intentaron convertir una acción diaria (comer, beber o hacer ejercicio) en hábito durante 84 días. El tiempo promedio para llegar a la meseta de automaticidad fue de 66 días, con diferencias individuales de 18 días a unos 254 estimados. Los hábitos de ejercicio tardaron cerca de 1,5 veces más que los de comer o beber, y un solo día perdido tuvo poco impacto, aunque muchos días perdidos bajaron el nivel alcanzado. Cerca de la mitad no llegó a una automaticidad alta en 84 días y la automaticidad fue autorreportada. Así que ten paciencia y sigue.",
                  handle, "Lally et al., Eur J Soc Psychol, 2010")
    return out(47, "habit", S, cap, "#habits #consistency #discipline #motivation #fitness", "Lally et al., Eur J Soc Psychol, 2010")

# ------------------------------------------------------------------ DIA 48
def reel_pushups(handle):
    S = [
        hook(48, "forty-eight", "cuarenta y ocho", "TEACHING YOU: PUSH-UPS AND HEART", "Enseñándote: flexiones y corazón", ["CAN PUSH-UPS", "PREDICT HEART RISK?"],
             "your push-up count and your heart", "las flexiones y la salud del corazón",
             ("Can your push-up count say something about your heart?", ["Can your push-up count say", "something about your heart?"]),
             ("¿Tus flexiones dicen algo sobre tu corazón?", ["¿Tus flexiones dicen algo", "sobre tu corazón?"]), icon="heart"),
        stat("40+ PUSH-UPS VS UNDER 10", "-96%", 150, 0.96, "heart", ["lower risk of heart events,", "1,104 male firefighters"],
             [L("A ten-year study followed one thousand one hundred four active male fire fighters.", "Un estudio de diez años siguió a 1.104 bomberos varones activos.",
                ["10-year study of 1,104", "active male firefighters."], ["Estudio de 10 años con 1.104", "bomberos varones activos."]),
              L("Men who could do more than forty in a row had a ninety-six percent lower risk of heart problems than men who managed fewer than ten.",
                "Los que hacían más de 40 flexiones tuvieron un 96 por ciento menos de riesgo de eventos cardíacos que quienes hacían menos de 10.",
                ["40+ push-ups: 96% lower risk of", "heart events vs fewer than 10."], ["40+ flexiones: 96 % menos riesgo de", "eventos cardíacos vs menos de 10."]),
              L("There were only thirty-seven cases, almost all in men who did forty or fewer.", "Hubo solo 37 eventos, casi todos en hombres que hacían 40 o menos.",
                ["Only 37 events, almost all in", "men who did 40 or fewer."], ["Solo 37 eventos, casi todos en", "hombres que hacían 40 o menos."])],
             count=(96, "-{:.0f}%")),
        tips3("READ THE FINE PRINT", ["heart", "flask", "check"],
              [("Only active men, average age 39.6", "Solo hombres activos, edad media 39,6"),
               ("May not apply to women or other ages", "Puede no aplicar a mujeres ni otras edades"),
               ("A marker, not a proven cause", "Un indicador, no una causa probada")],
              [L("Everyone was an active man, with an average age of about forty.", "Todos eran hombres activos, con una edad media de cerca de cuarenta años.",
                 ["All were active men, average", "age about 40."], ["Todos hombres activos, edad", "media cerca de 40."]),
              L("The authors say it may not apply to women, other ages, or less active men.", "Los autores dicen que puede no aplicar a mujeres, otras edades u hombres menos activos.",
                 ["It may not apply to women,", "other ages or less active men."], ["Puede no aplicar a mujeres,", "otras edades u hombres menos activos."]),
               L("The push-up is a fitness marker here. This does not prove it causes the lower risk.", "Las flexiones son un indicador de forma física aquí. Esto no prueba que causen el menor riesgo.",
                 ["Push-ups are a fitness marker.", "It does not prove cause."], ["Las flexiones son un indicador.", "No prueba la causa."])]),
        cta(48, "forty-nine", "cuarenta y nueve", "DAY 49 TOMORROW: GRIP STRENGTH", "Mañana, día 49: fuerza de agarre"),
    ]
    cap = caption(48, "push-ups and heart health", "flexiones y salud del corazón",
                  "Can your push-up count say something about your heart? In a 10-year study of 1,104 active male firefighters (mean age 39.6), men who could do more than 40 push-ups at baseline had a 96% lower risk of cardiovascular disease events than those who could do fewer than 10. There were only 37 events, all but one in men who completed 40 or fewer push-ups. The authors say the results may not generalize to women, men of other ages, or less active men. Push-ups are a fitness marker here, not a proven cause: do not chase a number, build up gradually.",
                  "¿Tus flexiones dicen algo sobre tu corazón? En un estudio de 10 años con 1.104 bomberos varones activos (edad media 39,6), los hombres que podían hacer más de 40 flexiones al inicio tuvieron un 96 % menos de riesgo de eventos cardiovasculares que quienes podían hacer menos de 10. Hubo solo 37 eventos, todos menos uno en hombres que hacían 40 o menos. Los autores dicen que los resultados pueden no generalizarse a mujeres, hombres de otras edades u hombres menos activos. Las flexiones son aquí un indicador de forma física, no una causa probada: no persigas un número, avanza de a poco.",
                  handle, "Yang et al., JAMA Netw Open, 2019")
    return out(48, "pushups", S, cap, "#pushups #heart #cardio #bodyweight #fitness", "Yang et al., JAMA Netw Open, 2019")

# ------------------------------------------------------------------ DIA 49
def reel_grip(handle):
    S = [
        hook(49, "forty-nine", "cuarenta y nueve", "TEACHING YOU: GRIP STRENGTH", "Enseñándote: fuerza de agarre", ["WHAT CAN YOUR", "GRIP TELL YOU?"],
             "grip strength", "la fuerza de agarre",
             ("Does your grip strength say something about your health?", ["Does your grip strength say", "something about your health?"]),
             ("¿Tu fuerza de agarre dice algo de tu salud?", ["¿Tu fuerza de agarre dice", "algo de tu salud?"]), icon="dumbbell"),
        stat("EACH 5 KG LOWER GRIP", "+16%", 150, 0.16, "dumbbell", ["higher risk of death,", "140,000 adults, 17 countries"],
             [L("The PURE study measured grip strength in nearly one hundred forty thousand adults in seventeen nations, for about four years.",
                "El estudio PURE midió la fuerza de agarre en casi 140.000 adultos de 17 países, durante unos cuatro años.",
                ["~140,000 adults, 17 countries,", "followed about 4 years."], ["~140.000 adultos, 17 países,", "seguidos unos 4 años."]),
              L("Each five kilogram drop in grip strength was linked to a sixteen percent higher risk of death from any cause.",
                "Cada caída de cinco kilos en la fuerza de agarre se asoció con un 16 por ciento más de riesgo de muerte por cualquier causa.",
                ["Each 5 kg drop in grip: 16%", "higher risk of death, any cause."], ["Cada 5 kg menos de agarre: 16 %", "más riesgo de muerte, cualquier causa."]),
              L("And a seventeen percent higher risk of death from heart disease.", "Y un 17 por ciento más de riesgo de muerte por enfermedad cardíaca.",
                ["And 17% higher risk of death", "from heart disease."], ["Y 17 % más riesgo de muerte", "por enfermedad cardíaca."])],
             count=(16, "+{:.0f}%")),
        tips3("READ THE FINE PRINT", ["dumbbell", "heart", "flask"],
              [("Stroke +9%, heart attack +7%", "ACV +9 %, infarto +7 %"),
               ("No link with diabetes or cancer", "Sin relación con diabetes ni cáncer"),
               ("Association, not proof", "Asociación, no prueba")],
              [L("Each drop was also linked to a nine percent higher stroke risk, and seven percent for heart attack.", "Cada caída también se asoció con un 9 por ciento más de riesgo de ACV y un 7 por ciento de infarto.",
                 ["Also +9% stroke risk and", "+7% heart attack risk."], ["También +9 % riesgo de ACV y", "+7 % de infarto."]),
               L("Weaker grip was not linked to diabetes or cancer.", "Un agarre más débil no se asoció con diabetes ni cáncer.",
                 ["Weaker grip: no link with", "diabetes or cancer."], ["Agarre más débil: sin relación con", "diabetes ni cáncer."]),
               L("These are links, not proof that grip itself causes them.", "Son asociaciones, no prueba de que el agarre las cause.",
                 ["Associations, not proof that", "grip itself causes them."], ["Asociaciones, no prueba de que", "el agarre las cause."])]),
        cta(49, "fifty", "cincuenta", "DAY 50 TOMORROW: REST BETWEEN SETS", "Mañana, día 50: descanso entre series"),
    ]
    cap = caption(49, "grip strength", "fuerza de agarre",
                  "Does your grip strength say something about your health? The PURE study measured grip strength with a dynamometer in nearly 140,000 adults in 17 countries and followed them for about four years. Each 5 kg decrease in grip strength was associated with a 16% higher risk of death from any cause, 17% higher risk of cardiovascular death, 9% higher risk of stroke and 7% higher risk of heart attack. Weaker grip was not linked to diabetes or cancer. These are associations, not proof that grip strength itself causes these outcomes.",
                  "¿Tu fuerza de agarre dice algo de tu salud? El estudio PURE midió la fuerza de agarre con un dinamómetro en casi 140.000 adultos de 17 países y los siguió durante unos cuatro años. Cada caída de 5 kg en la fuerza de agarre se asoció con un 16 % más de riesgo de muerte por cualquier causa, 17 % más de riesgo de muerte cardiovascular, 9 % más de riesgo de ACV y 7 % más de riesgo de infarto. Un agarre más débil no se asoció con diabetes ni cáncer. Son asociaciones, no prueba de que la fuerza de agarre misma cause estos resultados.",
                  handle, "Leong et al., Lancet, 2015")
    return out(49, "grip", S, cap, "#gripstrength #strength #health #longevity #fitness", "Leong et al., Lancet, 2015")

# ------------------------------------------------------------------ DIA 50
def reel_restsets(handle):
    S = [
        hook(50, "fifty", "cincuenta", "TEACHING YOU: REST BETWEEN SETS", "Enseñándote: descanso entre series", ["HOW LONG SHOULD YOU", "REST BETWEEN SETS?"],
             "rest between sets", "el descanso entre series",
             ("Does resting longer between sets help you grow?", ["Does resting longer between", "sets help you grow?"]),
             ("¿Descansar más entre series ayuda a crecer?", ["¿Descansar más entre series", "ayuda a crecer?"]), icon="clock"),
        stat("1 MIN VS 3 MIN RESTS", "21", 190, 0.4, "clock", ["trained men,", "8 weeks"],
             [L("In an eight-week trial, twenty-one trained men did the same workout three days a week.", "En un ensayo de ocho semanas, 21 hombres entrenados hicieron el mismo entrenamiento tres días por semana.",
                ["8 weeks, 21 trained men,", "same workout 3 days a week."], ["8 semanas, 21 hombres entrenados,", "mismo entrenamiento 3 días por semana."]),
              L("One group took short one-minute rests, the other took longer three-minute rests between sets.", "Un grupo descansó un minuto entre series y el otro tres minutos.",
                ["One group rested 1 minute,", "the other rested 3 minutes."], ["Un grupo descansó 1 minuto,", "el otro 3 minutos."]),
              L("The three-minute group gained more strength in the squat and bench press, and more thigh muscle thickness.", "El grupo de tres minutos ganó más fuerza en sentadilla y press de banca, y más grosor muscular en el muslo.",
                ["3-minute group: more squat and", "bench strength, thicker quads."], ["Grupo de 3 minutos: más fuerza en", "sentadilla y banca, cuádriceps más gruesos."])],
             count=(21, "{:.0f}")),
        tips3("READ THE FINE PRINT", ["clock", "flask", "check"],
              [("Upper-body endurance: no difference", "Resistencia de tren superior: sin diferencia"),
               ("Triceps size: a trend, not significant", "Tríceps: una tendencia, no significativa"),
               ("Only 21 young trained men", "Solo 21 hombres jóvenes entrenados")],
              [L("Both groups improved upper-body endurance, with no difference between them.", "Ambos grupos mejoraron la resistencia del tren superior, sin diferencia entre ellos.",
                 ["Both improved upper-body", "endurance, no difference."], ["Ambos mejoraron la resistencia", "del tren superior, sin diferencia."]),
               L("Triceps growth showed only a trend toward longer rests, not a significant one.", "El crecimiento del tríceps solo mostró una tendencia hacia descansos más largos, no significativa.",
                 ["Triceps: only a trend toward", "longer rests, not significant."], ["Tríceps: solo una tendencia hacia", "descansos largos, no significativa."]),
               L("It was only twenty-one young trained men, so treat it as one clue.", "Fueron solo 21 hombres jóvenes entrenados, así que tómalo como una pista.",
                 ["Only 21 young trained men:", "treat it as one clue."], ["Solo 21 hombres jóvenes entrenados:", "tómalo como una pista."])]),
        cta(50, "fifty-one", "cincuenta y uno", "DAY 51 TOMORROW: ONE-MINUTE BURSTS", "Mañana, día 51: ráfagas de un minuto"),
    ]
    cap = caption(50, "rest between sets", "descanso entre series",
                  "Does resting longer between sets help you grow? In an 8-week trial, 21 young resistance-trained men did the same total-body program (3 sessions a week, 3 sets of 8–12 repetition maximum across 7 exercises) with either 1-minute or 3-minute rests between sets. The 3-minute group gained significantly more strength in the back squat and bench press and more anterior-thigh muscle thickness. Triceps thickness showed only a non-significant trend, and upper-body endurance improved equally in both groups. With only 21 participants, it is one clue, not the final word.",
                  "¿Descansar más entre series ayuda a crecer? En un ensayo de 8 semanas, 21 hombres jóvenes entrenados en fuerza hicieron el mismo programa de cuerpo completo (3 sesiones por semana, 3 series de 8–12 repeticiones máximas en 7 ejercicios) con descansos de 1 o de 3 minutos entre series. El grupo de 3 minutos ganó significativamente más fuerza en sentadilla y press de banca y más grosor muscular en la parte anterior del muslo. El grosor del tríceps solo mostró una tendencia no significativa y la resistencia del tren superior mejoró igual en ambos grupos. Con solo 21 participantes, es una pista, no la última palabra.",
                  handle, "Schoenfeld et al., J Strength Cond Res, 2016")
    return out(50, "rest-sets", S, cap, "#hypertrophy #musclebuilding #gym #strengthtraining #fitness", "Schoenfeld et al., J Strength Cond Res, 2016")

# ------------------------------------------------------------------ DIA 51
def reel_bursts(handle):
    S = [
        hook(51, "fifty-one", "cincuenta y uno", "TEACHING YOU: ONE-MINUTE BURSTS", "Enseñándote: ráfagas de un minuto", ["CAN ONE-MINUTE BURSTS", "LOWER YOUR RISK?"],
             "one-minute bursts of activity", "las ráfagas de actividad de un minuto",
             ("Can one-minute bursts of effort help you live longer?", ["Can one-minute bursts of", "effort help you live longer?"]),
             ("¿Ráfagas de un minuto ayudan a vivir más?", ["¿Ráfagas de un minuto", "ayudan a vivir más?"]), icon="bolt"),
        stat("VIGOROUS BURSTS · UK BIOBANK", "-40%", 150, 0.4, "bolt", ["lower risk of death, up to,", "25,000+ non-exercisers"],
             [L("Scientists followed over twenty-five thousand adults who did not exercise, using wearable trackers, for about seven years.", "Se siguió a más de 25.000 adultos que no hacían ejercicio, con pulseras de muñeca, durante unos siete años.",
                ["25,000+ non-exercisers, wrist", "trackers, about 7 years."], ["25.000+ adultos sin ejercicio,", "pulseras de muñeca, ~7 años."]),
              L("Three to four one-minute bursts of vigorous activity a day were linked to large drops in risk.", "De tres a cuatro ráfagas de un minuto de actividad vigorosa al día se asociaron con grandes reducciones de riesgo.",
                ["3–4 one-minute vigorous bursts", "a day: large risk reductions."], ["3–4 ráfagas vigorosas de un minuto", "al día: grandes reducciones de riesgo."]),
              L("Up to about forty percent lower risk of death from any cause, and up to forty-nine percent for heart disease.", "Hasta cerca de un cuarenta por ciento menos de riesgo de muerte por cualquier causa, y hasta un cuarenta y nueve por ciento por enfermedad cardíaca.",
                ["Up to ~40% lower risk of death,", "up to 49% for heart disease."], ["Hasta ~40 % menos riesgo de muerte,", "hasta 49 % por enfermedad cardíaca."])],
             count=(40, "-{:.0f}%")),
        tips3("READ THE FINE PRINT", ["bolt", "flask", "check"],
              [("More bursts, bigger drop", "Más ráfagas, mayor descenso"),
               ("Activity estimated by wrist trackers", "Actividad estimada con pulseras"),
               ("Observational: not proof", "Observacional: no prueba")],
              [L("The steepest gains came from going from none to four or five bursts a day.", "Las mayores mejoras llegaron al pasar de ninguna a cuatro o cinco ráfagas al día.",
                 ["Steepest gains: from none to", "4–5 bursts a day."], ["Mayores mejoras: de ninguna a", "4–5 ráfagas al día."]),
               L("Activity was estimated from wearable trackers, and the no-exercise status was self-reported.", "La actividad se estimó con pulseras y el no hacer ejercicio fue autorreportado.",
                 ["Activity estimated by wrist", "trackers; self-reported status."], ["Actividad estimada con pulseras;", "estado autorreportado."]),
               L("It is observational, so it cannot prove cause and effect.", "Es observacional, así que no puede probar causa y efecto.",
                 ["Observational: it cannot", "prove cause and effect."], ["Observacional: no puede", "probar causa y efecto."])]),
        cta(51, "fifty-two", "cincuenta y dos", "DAY 52 TOMORROW: WEIGHTS AND MOOD", "Mañana, día 52: pesas y ánimo"),
    ]
    cap = caption(51, "one-minute bursts of activity", "ráfagas de actividad de un minuto",
                  "Can one-minute bursts of effort help you live longer? Researchers followed more than 25,000 UK Biobank adults who did not exercise, using wrist-worn trackers, for about 7 years. Three to four one-minute bursts of vigorous activity per day during daily tasks were linked to large risk reductions: up to about 40% lower all-cause mortality and up to about 49% lower cardiovascular mortality. The steepest gains were between none and four to five bursts. The study is observational and cannot establish cause and effect; activity was estimated from wrist trackers. If you are not used to vigorous effort, build up gradually.",
                  "¿Ráfagas de un minuto de esfuerzo ayudan a vivir más? Se siguió a más de 25.000 adultos del UK Biobank que no hacían ejercicio, con pulseras de muñeca, durante unos 7 años. De tres a cuatro ráfagas de un minuto de actividad vigorosa al día durante tareas cotidianas se asociaron con grandes reducciones de riesgo: hasta cerca de un 40 % menos de mortalidad por cualquier causa y hasta cerca de un 49 % menos de mortalidad cardiovascular. Las mayores mejoras fueron entre ninguna y cuatro a cinco ráfagas. El estudio es observacional y no puede establecer causa y efecto; la actividad se estimó con pulseras. Si no estás acostumbrado al esfuerzo vigoroso, avanza de a poco.",
                  handle, "Stamatakis et al., Nat Med, 2022")
    return out(51, "bursts", S, cap, "#exercisesnacks #longevity #health #hiit #fitness", "Stamatakis et al., Nat Med, 2022")

# ------------------------------------------------------------------ DIA 52
def reel_depression(handle):
    S = [
        hook(52, "fifty-two", "cincuenta y dos", "TEACHING YOU: WEIGHTS AND MOOD", "Enseñándote: pesas y ánimo", ["CAN LIFTING WEIGHTS", "LIFT YOUR MOOD?"],
             "resistance training and depressive symptoms", "el entrenamiento de fuerza y los síntomas depresivos",
             ("Can lifting weights ease depressive symptoms?", ["Can lifting weights ease", "depressive symptoms?"]),
             ("¿Levantar pesas puede aliviar los síntomas depresivos?", ["¿Levantar pesas puede aliviar", "los síntomas depresivos?"]), icon="heart"),
        stat("RESISTANCE TRAINING · META-ANALYSIS", "33", 190, 0.4, "heart", ["trials, 1,877 people,", "depressive symptoms"],
             [L("A meta-analysis pooled thirty-three trials with one thousand eight hundred seventy-seven people.", "Un metaanálisis reunió 33 ensayos con 1.877 personas.",
                ["33 trials with", "1,877 people."], ["33 ensayos con", "1.877 personas."]),
              L("Resistance training lowered depressive symptoms, a moderate-sized effect.", "El entrenamiento de fuerza redujo los síntomas depresivos, un efecto de tamaño moderado.",
                ["Weights lowered depressive", "symptoms: a moderate effect."], ["Las pesas redujeron los síntomas", "depresivos: efecto moderado."]),
              L("It worked regardless of health status.", "Funcionó sin importar el estado de salud de la persona.",
                ["It worked regardless of", "health status."], ["Funcionó sin importar", "el estado de salud."])],
             count=(33, "{:.0f}")),
        tips3("WHAT THE TRIALS SHOWED", ["heart", "calendar", "check"],
              [("Biggest in mild to moderate depression", "Mayor en depresión leve a moderada"),
               ("About 16 weeks, usually 3 days a week", "Unas 16 semanas, casi siempre 3 días/semana"),
               ("Can complement treatment, not replace it", "Puede complementar, no reemplazar, el tratamiento")],
              [L("The biggest effect was in people with mild to moderate depression.", "El mayor efecto fue en personas con depresión leve a moderada.",
                 ["Biggest effect: people with", "mild to moderate depression."], ["Mayor efecto: personas con", "depresión leve a moderada."]),
               L("Plans lasted about sixteen weeks on average, most often three days a week.", "Los programas duraron unas 16 semanas en promedio, casi siempre tres días por semana.",
                 ["Programs: about 16 weeks,", "most often 3 days a week."], ["Programas: unas 16 semanas,", "casi siempre 3 días por semana."]),
               L("The authors see it as an add-on or alternative. If you struggle, talk to a professional.", "Los autores lo ven como complemento o alternativa. Si estás pasando un mal momento, habla con un profesional.",
                 ["Authors see it as an add-on or", "alternative. Struggling? Talk to a professional."], ["Los autores lo ven como complemento", "o alternativa. ¿Mal momento? Habla con un profesional."])]),
        cta(52, "fifty-three", "cincuenta y tres", "DAY 53 TOMORROW: ACTIVE COMMUTING", "Mañana, día 53: ir al trabajo activo"),
    ]
    cap = caption(52, "weights and mood", "pesas y ánimo",
                  "Can lifting weights ease depressive symptoms? A meta-analysis of 33 randomized clinical trials (54 effects, 1,877 participants) found that resistance exercise training significantly reduced depressive symptoms, with a moderate-sized mean effect (Hedges' g = 0.66). The benefit did not depend on participants' health status and was greatest in people with mild to moderate depression; programs averaged about 16 weeks, most often 3 days a week. The authors see resistance training as an alternative or adjuvant therapy, and call for better-quality trials. If you are struggling, talk to a health professional.",
                  "¿Levantar pesas puede aliviar los síntomas depresivos? Un metaanálisis de 33 ensayos clínicos aleatorizados (54 efectos, 1.877 participantes) halló que el entrenamiento de fuerza redujo significativamente los síntomas depresivos, con un efecto medio de tamaño moderado (g de Hedges = 0,66). El beneficio no dependió del estado de salud de los participantes y fue mayor en personas con depresión leve a moderada; los programas duraron unas 16 semanas en promedio, casi siempre 3 días por semana. Los autores lo ven como terapia alternativa o complementaria y piden ensayos de mejor calidad. Si estás pasando un mal momento, habla con un profesional de la salud.",
                  handle, "Gordon et al., JAMA Psychiatry, 2018")
    return out(52, "depression", S, cap, "#mentalhealth #depression #strengthtraining #wellbeing #fitness", "Gordon et al., JAMA Psychiatry, 2018")

# ------------------------------------------------------------------ DIA 53
def reel_commute(handle):
    S = [
        hook(53, "fifty-three", "cincuenta y tres", "TEACHING YOU: ACTIVE COMMUTING", "Enseñándote: ir al trabajo activo", ["DOES WALKING OR CYCLING", "TO WORK COUNT?"],
             "active commuting", "el traslado activo",
             ("Does cycling or walking to work really matter?", ["Does cycling or walking", "to work really matter?"]),
             ("¿Ir al trabajo en bici o caminando realmente importa?", ["¿Ir al trabajo en bici o", "caminando realmente importa?"]), icon="walk"),
        {"type": "vs", "tail": 0.7, "head": "LOWER RISK OF HEART DISEASE VS NON-ACTIVE", "sub": "263,450 people · about 5 years",
         "rows": [{"title": "Cycling to work", "sub": "heart disease", "es": "En bici al trabajo", "val": 46, "fmt": "-{:.0f}%", "win": True},
                  {"title": "Walking to work", "sub": "heart disease", "es": "Caminando al trabajo", "val": 27, "fmt": "-{:.0f}%"}],
         "lines": [L("The British Biobank followed two hundred sixty-three thousand people for about five years.", "UK Biobank siguió a unas 263.000 personas durante unos cinco años.",
                     ["UK Biobank: 263,450 people,", "about 5 years."], ["UK Biobank: 263.450 personas,", "unos 5 años."]),
                   L("Compared with an inactive commute, cycling was linked to forty-six percent lower risk of heart disease, and walking to twenty-seven percent.",
                     "Frente a un traslado no activo, la bici se asoció con un 46 por ciento menos de riesgo de enfermedad cardíaca, y caminar con un 27 por ciento.",
                     ["Vs non-active commute: cycling", "-46% heart disease, walking -27%."], ["Vs traslado no activo: bici -46 %", "enfermedad cardíaca, caminar -27 %."]),
                   L("Cycling was also linked to forty-one percent lower risk of death, and forty-five percent lower cancer risk.",
                     "La bici también se asoció con un 41 por ciento menos de riesgo de muerte y un 45 por ciento menos de riesgo de cáncer.",
                     ["Cycling also: -41% risk of death,", "-45% cancer risk."], ["La bici también: -41 % riesgo de muerte,", "-45 % riesgo de cáncer."])]},
        tips3("READ THE FINE PRINT", ["walk", "flask", "check"],
              [("Walking: no clear link to death or cancer", "Caminar: sin relación clara con muerte o cáncer"),
               ("Cyclists commuted farther each week", "Los ciclistas recorrían más cada semana"),
               ("Observational: only if causal", "Observacional: solo si es causal")],
              [L("Walking to work showed no significant link with death or cancer.", "Caminar al trabajo no mostró una relación significativa con la muerte ni el cáncer.",
                 ["Walking: no significant link", "with death or cancer."], ["Caminar: sin relación significativa", "con muerte ni cáncer."]),
               L("Cyclists commuted farther, about thirty miles a week versus six for walkers.", "Los ciclistas recorrían más, unas treinta millas por semana frente a seis de los que caminaban.",
                 ["Cyclists: about 30 miles a week.", "Walkers: about 6."], ["Ciclistas: unas 30 millas por semana.", "Caminantes: unas 6."]),
               L("It is observational, so the gains hold only if the link is causal.", "Es observacional, así que los beneficios valen solo si la relación es causal.",
                 ["Observational: benefits hold", "only if the link is causal."], ["Observacional: los beneficios valen", "solo si la relación es causal."])]),
        {"type": "cta", "tail": 1.0, "next_en": "MORE LESSONS COMING", "next_es": "Vienen más lecciones",
         "lines": [L("Save this, and send it to a friend who commutes every day.", "Guárdalo y envíaselo a un amigo que se traslada todos los días.",
                     ["Save this, and send it to a", "friend who commutes every day."], ["Guárdalo y envíaselo a un amigo", "que se traslada todos los días."]),
                   L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
                     ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]},
    ]
    cap = (f"Day 53 teaching you: active commuting 💪\n"
           f"Does cycling or walking to work really matter? A UK Biobank cohort of 263,450 people followed for about 5 years found that, compared with non-active commuting, cycling to work was associated with about 46% lower risk of cardiovascular disease, 41% lower risk of death from any cause and 45% lower cancer risk. Walking to work was associated with about 27% lower risk of cardiovascular disease, with no significant link to death or cancer. Cyclists commuted farther (about 30 miles a week vs 6 for walkers). This is an observational study: the benefits hold only if the associations are causal.\n\n"
           f"Día 53 enseñándote: ir al trabajo activo 💪\n"
           f"¿Ir al trabajo en bici o caminando realmente importa? Una cohorte del UK Biobank de 263.450 personas seguidas unos 5 años halló que, frente a un traslado no activo, ir en bici al trabajo se asoció con cerca de un 46 % menos de riesgo de enfermedad cardiovascular, un 41 % menos de riesgo de muerte por cualquier causa y un 45 % menos de riesgo de cáncer. Caminar al trabajo se asoció con cerca de un 27 % menos de riesgo cardiovascular, sin relación significativa con la muerte ni el cáncer. Los ciclistas recorrían más (unas 30 millas por semana frente a 6 de quienes caminaban). Es un estudio observacional: los beneficios valen solo si las asociaciones son causales.\n\n"
           f"Save this 📌 and follow {handle}. / Guárdalo y sigue a {handle}.\n"
           f"Source / Fuente: Celis-Morales et al., BMJ, 2017.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return out(53, "commute", S, cap, "#activecommuting #cycling #walking #health #fitness", "Celis-Morales et al., BMJ, 2017")

REELS_MORE7 = {47: reel_habit, 48: reel_pushups, 49: reel_grip, 50: reel_restsets, 51: reel_bursts, 52: reel_depression, 53: reel_commute}
