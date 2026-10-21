"""Dias 19-25: tanda 3. Datos verificados contra resumenes/abstracts el 21/10/2026."""
from reels_more import L, hook, cta, caption
from reels_more2 import tips3

def stat(head, value, vsize, ring, icon, label, lines, count=None, anim=None):
    d = {"type": "stat", "tail": 0.7, "head": head, "value": value, "vsize": vsize, "ring": ring, "icon": icon, "label": label, "lines": lines}
    if count: d["count"] = count
    if anim: d["anim"] = anim
    return d

def out(n, topic, S, cap, tags, src):
    return {"id": n, "day": n, "q": 7, "topic": topic, "scenes": S, "caption": cap, "hashtags": tags, "source": "Source: " + src}

# ------------------------------------------------------------------ DIA 19
def reel_failure(handle):
    S = [
        hook(19, "nineteen", "diecinueve", "TEACHING YOU: TRAINING TO FAILURE", "Enseñándote: entrenar al fallo", ["DO YOU NEED TO", "TRAIN TO FAILURE?"],
             "training to failure", "entrenar al fallo",
             ("Do you have to push every set to failure?", ["Do you have to push", "every set to failure?"]),
             ("¿Hay que llevar cada serie al fallo?", ["¿Hay que llevar cada", "serie al fallo?"]), icon="target"),
        stat("TO FAILURE VS STOPPING SHORT", "15", 190, 0.5, "target", ["studies in a meta-analysis,", "young adults"],
             [L("A meta-analysis of fifteen studies compared sets taken to muscle failure with sets that stopped short of it.",
                "Un metaanálisis de 15 estudios comparó series llevadas al fallo muscular con series que paraban antes.",
                ["15 studies compared sets to", "failure vs sets stopped short."], ["15 estudios compararon series", "al fallo vs series que paraban antes."]),
              L("There was no significant difference in strength or muscle growth.",
                "No hubo diferencia significativa en fuerza ni en crecimiento muscular.",
                ["No significant difference in", "strength or muscle growth."], ["Sin diferencia significativa en", "fuerza ni crecimiento muscular."])],
             count=(15, "{:.0f}")),
        tips3("THE FINE PRINT", ["target", "dumbbell", "check"],
              [("Failure is not necessary for gains", "El fallo no es necesario para progresar"),
               ("Trained lifters: small edge for failure", "Entrenados: pequeña ventaja al fallo"),
               ("It does not appear to be harmful", "No parece ser perjudicial")],
              [L("So training to failure is not necessary to gain strength or size.", "Así que entrenar al fallo no es necesario para ganar fuerza o tamaño.",
                 ["So failure is not necessary to", "gain strength or size."], ["Así que el fallo no es necesario", "para ganar fuerza o tamaño."]),
               L("In resistance-trained people, failure showed a small advantage for muscle growth.", "En personas entrenadas, el fallo mostró una pequeña ventaja para el crecimiento muscular.",
                 ["In trained people, failure had a", "small edge for muscle growth."], ["En entrenados, el fallo tuvo una", "pequeña ventaja en músculo."]),
               L("And it did not appear to be harmful.", "Y no pareció ser perjudicial.", ["And it did not appear", "to be harmful."], ["Y no pareció", "ser perjudicial."])]),
        cta(19, "twenty", "veinte", "DAY 20 TOMORROW: MOOD", "Mañana, día 20: estado de ánimo"),
    ]
    cap = caption(19, "training to failure", "entrenar al fallo",
                  "Do you have to push every set to failure? A meta-analysis of 15 studies in young adults found no significant difference in strength (ES -0.09) or hypertrophy (ES 0.22) between training to failure and non-failure. When volume was not equated, non-failure training gave more strength. In resistance-trained participants, failure showed a small hypertrophy advantage (ES 0.15). Conclusion: failure is not necessary for gains, and it does not appear harmful. More research is needed in older adults and highly trained people.",
                  "¿Hay que llevar cada serie al fallo? Un metaanálisis de 15 estudios en adultos jóvenes no halló diferencia significativa en fuerza (ES -0,09) ni hipertrofia (ES 0,22) entre entrenar al fallo y no hacerlo. Cuando el volumen no estaba igualado, entrenar sin llegar al fallo dio más fuerza. En participantes entrenados, el fallo mostró una pequeña ventaja de hipertrofia (ES 0,15). Conclusión: el fallo no es necesario para progresar y no parece perjudicial. Falta investigación en adultos mayores y muy entrenados.",
                  handle, "Grgic et al., J Sport Health Sci, 2022")
    return out(19, "failure", S, cap, "#trainingtofailure #hypertrophy #strengthtraining #gym #workout", "Grgic et al., J Sport Health Sci, 2022")

# ------------------------------------------------------------------ DIA 20
def reel_mood(handle):
    S = [
        hook(20, "twenty", "veinte", "TEACHING YOU: LIFTING AND MOOD", "Enseñándote: pesas y ánimo", ["CAN LIFTING WEIGHTS", "HELP DEPRESSION?"],
             "lifting and mood", "las pesas y el ánimo",
             ("Can lifting weights help with depressive symptoms?", ["Can lifting weights help with", "depressive symptoms?"]),
             ("¿Levantar pesas puede ayudar con síntomas depresivos?", ["¿Levantar pesas puede ayudar", "con síntomas depresivos?"]), icon="heart"),
        stat("RESISTANCE TRAINING TRIALS", "33", 190, 0.55, "heart", ["randomized trials,", "1,877 participants"],
             [L("A meta-analysis pooled thirty-three randomized trials with one thousand eight hundred seventy-seven participants.",
                "Un metaanálisis reunió 33 ensayos aleatorizados con 1.877 participantes.",
                ["33 randomized trials,", "1,877 participants."], ["33 ensayos aleatorizados,", "1.877 participantes."]),
              L("The programs lasted sixteen weeks on average.", "Los programas duraron 16 semanas en promedio.",
                ["Programs lasted", "16 weeks on average."], ["Los programas duraron", "16 semanas en promedio."]),
              L("Resistance training significantly reduced depressive symptoms.", "El entrenamiento de fuerza redujo de forma significativa los síntomas depresivos.",
                ["It significantly reduced", "depressive symptoms."], ["Redujo de forma significativa", "los síntomas depresivos."])],
             count=(33, "{:.0f}")),
        tips3("WHAT THE REVIEW FOUND", ["heart", "dumbbell", "flask"],
              [("Benefit regardless of health, age, sex", "Beneficio sin importar salud, edad o sexo"),
               ("Seen even without strength gains", "También sin mejoras de fuerza"),
               ("Not a replacement for treatment", "No reemplaza un tratamiento")],
              [L("The benefit held regardless of health status, age, or sex.", "El beneficio se mantuvo sin importar el estado de salud, la edad o el sexo.",
                 ["It held regardless of health", "status, age, or sex."], ["Se mantuvo sin importar salud,", "edad o sexo."]),
               L("And it appeared even when strength did not improve significantly.", "Y apareció incluso cuando la fuerza no mejoró de forma significativa.",
                 ["And even when strength did not", "improve significantly."], ["Y aun cuando la fuerza no", "mejoró de forma significativa."]),
               L("It may help alongside treatment. If you struggle, talk to a professional.", "Puede ayudar junto al tratamiento. Si tienes dificultades, habla con un profesional.",
                 ["It may help alongside treatment.", "If you struggle, talk to a professional."], ["Puede ayudar junto al tratamiento.", "Si lo necesitas, habla con un profesional."])]),
        cta(20, "twenty-one", "veintiuno", "DAY 21 TOMORROW: SITTING", "Mañana, día 21: estar sentado"),
    ]
    cap = caption(20, "lifting and mood", "pesas y ánimo",
                  "Can lifting weights help with depressive symptoms? A meta-analysis of 33 randomized controlled trials (1,877 participants, programs of about 16 weeks on average) found that resistance exercise training significantly reduced depressive symptoms. The benefit held regardless of health status, age or sex, and appeared whether or not strength improved significantly. The authors suggest it may be a useful adjunct or alternative, and call for trials comparing it with other treatments. It is not a replacement for professional care: if you are struggling, talk to a health professional.",
                  "¿Levantar pesas puede ayudar con síntomas depresivos? Un metaanálisis de 33 ensayos controlados aleatorizados (1.877 participantes, programas de ~16 semanas en promedio) halló que el entrenamiento de fuerza redujo de forma significativa los síntomas depresivos. El beneficio se mantuvo sin importar el estado de salud, la edad o el sexo, y apareció tanto si la fuerza mejoraba de forma significativa como si no. Los autores sugieren que puede ser un complemento o alternativa útil y piden ensayos que lo comparen con otros tratamientos. No reemplaza la atención profesional: si estás pasando un mal momento, consulta con un profesional de la salud.",
                  handle, "Gordon et al., JAMA Psychiatry, 2018")
    return out(20, "mood", S, cap, "#mentalhealth #strengthtraining #depression #weightlifting #wellbeing", "Gordon et al., JAMA Psychiatry, 2018")

# ------------------------------------------------------------------ DIA 21
def reel_sitting(handle):
    S = [
        hook(21, "twenty-one", "veintiuno", "TEACHING YOU: SITTING AND EXERCISE", "Enseñándote: estar sentado y ejercicio", ["CAN EXERCISE UNDO", "A DAY OF SITTING?"],
             "sitting and exercise", "estar sentado y el ejercicio",
             ("Does exercise cancel out sitting all day?", ["Does exercise cancel out", "sitting all day?"]),
             ("¿El ejercicio compensa estar sentado todo el día?", ["¿El ejercicio compensa estar", "sentado todo el día?"]), icon="clock"),
        stat("SITTING 8+ HOURS A DAY", "1 h", 190, 0.6, "walk", ["of physical activity a day", "offset the extra risk"],
             [L("A harmonized meta-analysis of data from more than one million men and women looked at sitting time and risk of death.",
                "Un metaanálisis armonizado con datos de más de un millón de hombres y mujeres analizó el tiempo sentado y el riesgo de muerte.",
                ["Data from 1+ million adults:", "sitting time and risk of death."], ["Datos de más de 1 millón de adultos:", "tiempo sentado y riesgo de muerte."]),
              L("About one hour of physical activity a day offset the higher risk linked to sitting more than eight hours.",
                "Alrededor de una hora de actividad física al día compensó el mayor riesgo asociado a estar sentado más de ocho horas.",
                ["~1 hour of activity a day offset", "the risk of sitting 8+ hours."], ["~1 hora de actividad al día compensó", "el riesgo de sentarse 8+ horas."])]),
        tips3("GOOD TO KNOW", ["walk", "clock", "flask"],
              [("Brisk walking or cycling count", "Caminata rápida o bici cuentan"),
               ("Inactive + low sitting was riskier", "Inactivo y poco sentado: más riesgo"),
               ("Observational, mostly rich countries", "Observacional, sobre todo países ricos")],
              [L("Examples of activity are brisk walking or cycling.", "Ejemplos de actividad son caminar rápido o andar en bici.",
                 ["Examples: brisk walking", "or cycling."], ["Ejemplos: caminar rápido", "o andar en bici."]),
               L("Inactive people who sat under four hours still had a higher risk than active people who sat over eight.",
                 "Las personas inactivas que se sentaban menos de cuatro horas tuvieron más riesgo que las activas que se sentaban más de ocho.",
                 ["Inactive, sitting under 4 h: higher", "risk than active, sitting over 8 h."], ["Inactivos, sentados menos de 4 h: más", "riesgo que activos sentados más de 8 h."]),
               L("These are observational data, mostly from developed countries.", "Son datos observacionales, sobre todo de países desarrollados.",
                 ["Observational data, mostly", "from developed countries."], ["Datos observacionales, sobre todo", "de países desarrollados."])]),
        cta(21, "twenty-two", "veintidós", "DAY 22 TOMORROW: EATING WINDOW", "Mañana, día 22: ventana de comida"),
    ]
    cap = caption(21, "sitting and exercise", "estar sentado y ejercicio",
                  "Does exercise cancel out sitting all day? A harmonized meta-analysis of data from more than 1 million men and women found that about one hour of physical activity a day (brisk walking or cycling, for example) offset the increased risk of death associated with sitting more than 8 hours a day. Physically inactive people who sat less than 4 hours a day still had a greater risk than physically active people who sat more than 8. These are observational data, mostly from high-income countries: association, not proof of cause.",
                  "¿El ejercicio compensa estar sentado todo el día? Un metaanálisis armonizado con datos de más de 1 millón de hombres y mujeres halló que cerca de una hora de actividad física al día (caminata rápida o bicicleta, por ejemplo) compensó el mayor riesgo de muerte asociado a estar sentado más de 8 horas al día. Las personas inactivas que se sentaban menos de 4 horas tuvieron igualmente más riesgo que las activas que se sentaban más de 8. Son datos observacionales, sobre todo de países de ingresos altos: asociación, no prueba de causa.",
                  handle, "Ekelund et al., Lancet, 2016")
    return out(21, "sitting", S, cap, "#sitting #sedentary #walking #health #fitness", "Ekelund et al., Lancet, 2016")

# ------------------------------------------------------------------ DIA 22
def reel_tre(handle):
    S = [
        hook(22, "twenty-two", "veintidós", "TEACHING YOU: EATING WINDOW", "Enseñándote: ventana de comida", ["DOES 16:8 FASTING", "BEAT NORMAL EATING?"],
             "time-restricted eating", "comer en una ventana horaria",
             ("Does eating in an eight-hour window help you lose more weight?", ["Does an 8-hour eating window", "help you lose more weight?"]),
             ("¿Comer en una ventana de ocho horas hace bajar más de peso?", ["¿Comer en una ventana de 8 horas", "hace bajar más de peso?"]), icon="clock"),
        {"type": "vs", "tail": 0.7, "head": "WEIGHT CHANGE IN 12 WEEKS", "sub": "116 adults · noon to 8 pm vs 3 meals",
         "rows": [{"title": "16:8 eating", "sub": "noon–8 pm", "es": "Ventana 16:8", "val": 0.94, "fmt": "-{:.2f} kg", "win": False},
                  {"title": "Normal meals", "sub": "3 structured meals", "es": "Comidas normales", "val": 0.68, "fmt": "-{:.2f} kg"}],
         "lines": [L("In a twelve-week trial, one hundred sixteen adults with overweight or obesity ate freely between noon and eight p.m., or kept three regular meals.",
                     "En un ensayo de 12 semanas, 116 adultos con sobrepeso u obesidad comieron libremente entre el mediodía y las 8 de la noche, o mantuvieron tres comidas regulares.",
                     ["12 weeks, 116 adults: free eating", "noon–8 pm, or 3 regular meals."], ["12 semanas, 116 adultos: comer libre", "12–20 h, o 3 comidas regulares."]),
                   L("The eating-window group lost 0.94 kilograms. The regular-meals group lost 0.68.",
                     "El grupo de ventana horaria bajó 0,94 kilos. El de comidas regulares bajó 0,68.",
                     ["Window group: -0.94 kg.", "Regular meals: -0.68 kg."], ["Ventana: -0,94 kg.", "Comidas regulares: -0,68 kg."]),
                   L("The difference between groups was not statistically significant.", "La diferencia entre grupos no fue estadísticamente significativa.",
                     ["The difference was not", "statistically significant."], ["La diferencia no fue", "estadísticamente significativa."])]},
        tips3("WHAT IT MEANS", ["clock", "flask", "check"],
              [("No extra weight loss on its own", "Sin pérdida extra por sí solo"),
               ("Lower lean mass index in a subgroup", "Menor índice de masa magra en un subgrupo"),
               ("12 weeks: not the long term", "12 semanas: no es largo plazo")],
              [L("On its own, the eating window was not more effective for weight loss.", "Por sí sola, la ventana horaria no fue más efectiva para bajar de peso.",
                 ["On its own, it was not more", "effective for weight loss."], ["Por sí sola, no fue más", "efectiva para bajar de peso."]),
               L("In a fifty-person subgroup, the appendicular lean mass index was lower in that group.", "En un subgrupo de 50 personas, el índice de masa magra apendicular fue menor en ese grupo.",
                 ["In a 50-person subgroup, lean mass", "index was lower in that group."], ["En un subgrupo de 50, el índice de masa", "magra fue menor en ese grupo."]),
               L("And twelve weeks says nothing about the long term.", "Y doce semanas no dicen nada sobre el largo plazo.",
                 ["And 12 weeks says nothing", "about the long term."], ["Y 12 semanas no dicen nada", "sobre el largo plazo."])]),
        cta(22, "twenty-three", "veintitrés", "DAY 23 TOMORROW: FOAM ROLLING", "Mañana, día 23: foam roller"),
    ]
    cap = caption(22, "the eating window", "la ventana de comida",
                  "Does eating in an 8-hour window (16:8) help you lose more weight? In a 12-week randomized trial, 116 adults with overweight or obesity either ate freely from 12 pm to 8 pm or kept three structured meals a day. Weight change: -0.94 kg vs -0.68 kg; the between-group difference (-0.26 kg) was not statistically significant. In a 50-person in-person subgroup, the appendicular lean mass index was lower in the eating-window group (-0.16 kg/m²). Conclusion: without other interventions, time-restricted eating was not more effective for weight loss than eating throughout the day. Only 12 weeks, so it says nothing about the long term.",
                  "¿Comer en una ventana de 8 horas (16:8) hace bajar más de peso? En un ensayo aleatorizado de 12 semanas, 116 adultos con sobrepeso u obesidad comieron libremente de 12 a 20 h o mantuvieron tres comidas estructuradas al día. Cambio de peso: -0,94 kg vs -0,68 kg; la diferencia entre grupos (-0,26 kg) no fue estadísticamente significativa. En un subgrupo presencial de 50 personas, el índice de masa magra apendicular fue menor en el grupo de ventana horaria (-0,16 kg/m²). Conclusión: sin otras intervenciones, comer en ventana horaria no fue más efectivo para bajar de peso que comer a lo largo del día. Solo 12 semanas: no dice nada del largo plazo.",
                  handle, "Lowe et al., JAMA Intern Med, 2020")
    return out(22, "eating-window", S, cap, "#intermittentfasting #weightloss #nutrition #fatloss #health", "Lowe et al., JAMA Intern Med, 2020")

# ------------------------------------------------------------------ DIA 23
def reel_foam(handle):
    S = [
        hook(23, "twenty-three", "veintitrés", "TEACHING YOU: FOAM ROLLING", "Enseñándote: foam roller", ["DOES FOAM ROLLING", "ACTUALLY WORK?"],
             "foam rolling", "el foam roller",
             ("Is foam rolling worth the time?", ["Is foam rolling", "worth the time?"]),
             ("¿Vale la pena usar el foam roller?", ["¿Vale la pena usar", "el foam roller?"]), icon="list"),
        stat("FOAM ROLLING · META-ANALYSIS", "21", 190, 0.5, "list", ["studies, 454 participants", "(rollers and massage bars)"],
             [L("A meta-analysis pooled twenty-one studies with four hundred fifty-four participants.", "Un metaanálisis reunió 21 estudios con 454 participantes.",
                ["21 studies,", "454 participants."], ["21 estudios,", "454 participantes."]),
              L("Rolling before exercise improved flexibility by about four percent.", "Rodar antes de entrenar mejoró la flexibilidad en cerca de un cuatro por ciento.",
                ["Rolling before exercise improved", "flexibility by about 4%."], ["Rodar antes de entrenar mejoró", "la flexibilidad en ~4 %."]),
              L("The effects on sprint and strength were minor.", "Los efectos sobre el sprint y la fuerza fueron pequeños.",
                ["Effects on sprint and", "strength were minor."], ["Efectos pequeños sobre", "sprint y fuerza."])],
             count=(21, "{:.0f}")),
        tips3("THE VERDICT", ["list", "check", "clock"],
              [("Best use: as a warm-up", "Mejor uso: en la entrada en calor"),
               ("Recovery effects: minor", "Efectos en recuperación: pequeños"),
               ("Jump height: no meaningful change", "Salto: sin cambio relevante")],
              [L("The evidence supports foam rolling more as a warm-up activity.", "La evidencia respalda más el foam roller como parte de la entrada en calor.",
                 ["Evidence supports it more", "as a warm-up activity."], ["La evidencia lo respalda más", "como parte de la entrada en calor."]),
               L("As a recovery tool, the effects were minor.", "Como herramienta de recuperación, los efectos fueron pequeños.",
                 ["As a recovery tool,", "the effects were minor."], ["Como herramienta de recuperación,", "los efectos fueron pequeños."]),
               L("And jump performance did not change in a meaningful way.", "Y el rendimiento en salto no cambió de forma relevante.",
                 ["And jump performance did not", "change in a meaningful way."], ["Y el salto no cambió", "de forma relevante."])]),
        cta(23, "twenty-four", "veinticuatro", "DAY 24 TOMORROW: MUSCLE AFTER 50", "Mañana, día 24: músculo después de los 50"),
    ]
    cap = caption(23, "foam rolling", "foam roller",
                  "Is foam rolling worth the time? A meta-analysis of 21 studies (454 participants) found that foam rolling before exercise improved flexibility by about 4% (Hedges' g 0.34), while the effects on sprint, strength and jump performance were minor or negligible. As a recovery tool, effects were minor. The authors conclude that the evidence seems to justify foam rolling as a warm-up activity rather than as a recovery tool.",
                  "¿Vale la pena usar el foam roller? Un metaanálisis de 21 estudios (454 participantes) halló que rodar antes de entrenar mejoró la flexibilidad en cerca de un 4 % (g de Hedges 0,34), mientras que los efectos sobre sprint, fuerza y salto fueron pequeños o despreciables. Como herramienta de recuperación, los efectos fueron pequeños. Los autores concluyen que la evidencia parece justificar el uso del foam roller como actividad de entrada en calor más que como herramienta de recuperación.",
                  handle, "Wiewelhove et al., Front Physiol, 2019")
    return out(23, "foam-rolling", S, cap, "#foamrolling #mobility #warmup #recovery #fitness", "Wiewelhove et al., Front Physiol, 2019")

# ------------------------------------------------------------------ DIA 24
def reel_older(handle):
    S = [
        hook(24, "twenty-four", "veinticuatro", "TEACHING YOU: MUSCLE AFTER 50", "Enseñándote: músculo después de los 50", ["CAN LIFTING BUILD", "MUSCLE AFTER 50?"],
             "muscle after fifty", "el músculo después de los 50",
             ("Is it too late to build muscle after fifty?", ["Is it too late to build", "muscle after 50?"]),
             ("¿Es tarde para ganar músculo después de los 50?", ["¿Es tarde para ganar músculo", "después de los 50?"]), icon="dumbbell"),
        stat("LEAN MASS GAIN · 49 STUDIES", "+1.1 kg", 130, 0.55, "dumbbell", ["average gain in lean body mass,", "adults averaging 50+"],
             [L("A meta-analysis of forty-nine studies looked at resistance training in adults averaging fifty or older.", "Un metaanálisis de 49 estudios analizó el entrenamiento de fuerza en adultos de 50 años o más en promedio.",
                ["49 studies of resistance training", "in adults averaging 50+."], ["49 estudios de entrenamiento de fuerza", "en adultos de 50+ en promedio."]),
              L("After about twenty weeks, lean body mass rose by about one point one kilograms on average.", "Tras unas veinte semanas, la masa corporal magra subió en promedio unos 1,1 kilos.",
                ["After ~20 weeks, lean mass rose", "~1.1 kg on average."], ["Tras ~20 semanas, la masa magra subió", "~1,1 kg en promedio."])],
             anim="squat"),
        tips3("KEEP IN MIND", ["dumbbell", "flask", "target"],
              [("Gradually progress volume and load", "Progresa volumen y carga de a poco"),
               ("Single easy sets may not be enough", "Una sola serie fácil puede no alcanzar"),
               ("Averages: your result will vary", "Son promedios: tu resultado variará")],
              [L("The authors recommend gradually progressing volume and load.", "Los autores recomiendan progresar el volumen y la carga de forma gradual.",
                 ["Authors recommend progressing", "volume and load gradually."], ["Los autores recomiendan progresar", "volumen y carga gradualmente."]),
               L("A single set or a fixed-volume program may no longer be enough.", "Una sola serie o un programa de volumen fijo puede dejar de ser suficiente.",
                 ["A single set or a fixed program", "may no longer be enough."], ["Una sola serie o un programa fijo", "puede dejar de alcanzar."]),
               L("These are averages, so start light and check with your doctor if you have a condition.", "Son promedios, así que empieza liviano y consulta a tu médico si tienes alguna condición.",
                 ["These are averages: start light, and", "ask your doctor if you have a condition."], ["Son promedios: empieza liviano y", "consulta a tu médico si tienes condición."])]),
        cta(24, "twenty-five", "veinticinco", "DAY 25 TOMORROW: COLD WATER", "Mañana, día 25: agua fría"),
    ]
    cap = caption(24, "muscle after 50", "músculo después de los 50",
                  "Is it too late to build muscle after 50? A meta-analysis of 49 studies of resistance training in adults averaging 50 years or older found an average gain of about 1.1 kg (2.4 lb) of lean body mass after roughly 20 weeks. The authors note that a single set and/or fixed-volume programs may no longer be sufficient for long-term gains, and recommend gradually progressing volume and load. These are averages: start light and, if you have a health condition, check with your doctor first.",
                  "¿Es tarde para ganar músculo después de los 50? Un metaanálisis de 49 estudios de entrenamiento de fuerza en adultos de 50 años o más en promedio halló una ganancia media de unos 1,1 kg de masa corporal magra tras unas 20 semanas. Los autores señalan que una sola serie y/o los programas de volumen fijo pueden dejar de ser suficientes para ganancias a largo plazo, y recomiendan progresar de forma gradual el volumen y la carga. Son promedios: empieza liviano y, si tienes una condición de salud, consulta antes a tu médico.",
                  handle, "Peterson et al., Med Sci Sports Exerc, 2011")
    return out(24, "older-adults", S, cap, "#strengthtraining #over50 #aging #muscle #fitness", "Peterson et al., Med Sci Sports Exerc, 2011")

# ------------------------------------------------------------------ DIA 25
def reel_cwi(handle):
    S = [
        hook(25, "twenty-five", "veinticinco", "TEACHING YOU: COLD WATER", "Enseñándote: agua fría", ["DO ICE BATHS HURT", "MUSCLE GROWTH?"],
             "cold water after lifting", "el agua fría después de entrenar",
             ("Do ice baths after lifting hurt your gains?", ["Do ice baths after lifting", "hurt your gains?"]),
             ("¿Los baños de hielo tras entrenar frenan tus ganancias?", ["¿Los baños de hielo tras entrenar", "frenan tus ganancias?"]), icon="flask"),
        stat("COLD WATER VS ACTIVE RECOVERY", "+17%", 150, 0.17, "flask", ["type II fibre size, active", "recovery group only"],
             [L("In a small trial, twenty-one active men did strength training twice a week for twelve weeks.", "En un ensayo pequeño, 21 hombres activos hicieron entrenamiento de fuerza dos veces por semana durante 12 semanas.",
                ["21 active men, strength training", "twice a week for 12 weeks."], ["21 hombres activos, fuerza", "dos veces por semana, 12 semanas."]),
              L("After each session, they spent ten minutes in cold water or in active recovery.", "Después de cada sesión, pasaron diez minutos en agua fría o en recuperación activa.",
                ["After each session: 10 minutes in", "cold water or active recovery."], ["Tras cada sesión: 10 minutos en", "agua fría o recuperación activa."]),
              L("Only the active recovery group increased type two muscle fibre size, by seventeen percent.", "Solo el grupo de recuperación activa aumentó el tamaño de las fibras musculares tipo dos, un diecisiete por ciento.",
                ["Only active recovery raised type II", "fibre size, by 17%."], ["Solo la recuperación activa subió", "las fibras tipo II, un 17 %."])]),
        tips3("WHAT THEY CONCLUDED", ["flask", "dumbbell", "target"],
              [("Active recovery: larger strength and muscle gains", "Recuperación activa: más fuerza y músculo"),
               ("Cold water blunted growth signals", "El agua fría atenuó las señales de crecimiento"),
               ("Small study: interpret with caution", "Estudio pequeño: interpretar con cautela")],
              [L("Gains in strength and muscle mass were larger with active recovery.", "Las ganancias de fuerza y masa muscular fueron mayores con recuperación activa.",
                 ["Strength and muscle gains were", "larger with active recovery."], ["Las ganancias de fuerza y músculo", "fueron mayores con recuperación activa."]),
               L("Cold water blunted the muscle's growth signals after a session.", "El agua fría atenuó las señales de crecimiento del músculo tras una sesión.",
                 ["Cold water blunted the muscle's", "growth signals after a session."], ["El agua fría atenuó las señales de", "crecimiento tras una sesión."]),
               L("But it was a small study, so interpret it with caution.", "Pero fue un estudio pequeño, así que interprétalo con cautela.",
                 ["But it was a small study,", "so interpret it with caution."], ["Pero fue un estudio pequeño:", "interprétalo con cautela."])]),
        {"type": "cta", "tail": 1.0, "next_en": "MORE LESSONS COMING", "next_es": "Vienen más lecciones",
         "lines": [L("Save this, and send it to a friend who loves ice baths.", "Guárdalo y envíaselo a un amigo que ama los baños de hielo.",
                     ["Save this, and send it to a", "friend who loves ice baths."], ["Guárdalo y envíaselo a un", "amigo que ama los baños de hielo."]),
                   L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
                     ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]},
    ]
    cap = (f"Day 25 teaching you: cold water after lifting 💪\n"
           f"Do ice baths after lifting hurt your gains? In a 12-week trial, 21 physically active men did strength training twice a week and spent 10 minutes in cold water immersion or in active recovery after each session. Gains in strength and muscle mass were larger with active recovery; type II fibre cross-sectional area rose 17% and myonuclei per fibre 26% in the active recovery group only. A second study (9 men) showed cold water blunted acute satellite-cell and kinase responses. The authors suggest reconsidering cold water as a regular post-exercise strategy, but note these were small samples.\n\n"
           f"Día 25 enseñándote: agua fría después de entrenar 💪\n"
           f"¿Los baños de hielo tras entrenar frenan tus ganancias? En un ensayo de 12 semanas, 21 hombres físicamente activos hicieron entrenamiento de fuerza dos veces por semana y pasaron 10 minutos en inmersión en agua fría o en recuperación activa tras cada sesión. Las ganancias de fuerza y masa muscular fueron mayores con recuperación activa; el área de las fibras tipo II subió un 17 % y los mionúcleos por fibra un 26 % solo en el grupo de recuperación activa. Un segundo estudio (9 hombres) mostró que el agua fría atenuó las respuestas agudas de células satélite y quinasas. Los autores sugieren reconsiderar el agua fría como estrategia regular posterior al ejercicio, pero señalan que son muestras pequeñas.\n\n"
           f"Save this 📌 and follow {handle}. / Guárdalo y sigue a {handle}.\n"
           f"Source / Fuente: Roberts et al., J Physiol, 2015.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return out(25, "cold-water", S, cap, "#icebath #coldplunge #recovery #musclegrowth #strengthtraining", "Roberts et al., J Physiol, 2015")

REELS_MORE3 = {19: reel_failure, 20: reel_mood, 21: reel_sitting, 22: reel_tre, 23: reel_foam, 24: reel_older, 25: reel_cwi}
