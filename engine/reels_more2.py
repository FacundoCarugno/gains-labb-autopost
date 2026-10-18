"""Dias 13-18: tanda 2. Datos verificados contra la fuente (resumenes/abstracts) el 18/10/2026."""
from reels_more import L, hook, cta, caption

def tips3(head, icons, items, lines, anim=None):
    d = {"type": "tips", "tail": 0.6, "head": head, "icons": icons, "items": items, "lines": lines}
    if anim: d["anim"] = anim
    return d

# ----------------------------------------------------------------------------- DIA 13
def reel_rest(handle):
    S = [
        hook(13, "thirteen", "trece", "TEACHING YOU: REST TIME", "Enseñándote: descanso entre series", ["HOW LONG TO REST", "BETWEEN SETS?"],
             "rest between sets", "el descanso entre series",
             ("Is resting longer between sets a waste of time?", ["Is resting longer between", "sets a waste of time?"]),
             ("¿Descansar más entre series es perder tiempo?", ["¿Descansar más entre series", "es perder tiempo?"]), icon="clock"),
        {"type": "vs", "tail": 0.7, "head": "REST BETWEEN SETS", "sub": "8 weeks · 21 trained men · same program",
         "rows": [{"title": "Long rest", "sub": "3 minutes", "es": "Descanso largo", "val": 3, "fmt": "{:.0f} min", "win": True},
                  {"title": "Short rest", "sub": "1 minute", "es": "Descanso corto", "val": 1, "fmt": "{:.0f} min"}],
         "lines": [L("In a study, twenty-one trained men followed the same program for eight weeks. One group rested one minute between sets, the other three.",
                     "En un estudio, 21 hombres entrenados siguieron el mismo programa durante 8 semanas. Un grupo descansó un minuto entre series y el otro tres.",
                     ["21 trained men, same program,", "8 weeks: rest of 1 or 3 minutes", "between sets."], ["21 hombres entrenados, mismo programa,", "8 semanas: descanso de 1 o 3 minutos", "entre series."]),
                   L("The three-minute group gained more strength in the squat and the bench press.",
                     "El grupo de tres minutos ganó más fuerza en la sentadilla y el press de banca.",
                     ["The 3-minute group gained more", "strength in squat and bench press."], ["El grupo de 3 minutos ganó más", "fuerza en sentadilla y press de banca."]),
                   L("It also grew more thigh muscle thickness.", "También creció más el grosor muscular del muslo.",
                     ["It also gained more", "thigh muscle thickness."], ["También ganó más grosor", "muscular en el muslo."])]},
        tips3("TAKEAWAYS", ["clock", "dumbbell", "flask"],
              [("Longer rest gave more strength", "Más descanso dio más fuerza"),
               ("Thigh growth was also greater", "El muslo también creció más"),
               ("Small study: one data point", "Estudio pequeño: un solo dato")],
              [L("In this study, resting longer gave more strength.", "En este estudio, descansar más dio más fuerza.",
                 ["In this study, resting longer", "gave more strength."], ["En este estudio, descansar más", "dio más fuerza."]),
               L("And more growth in the thigh.", "Y más crecimiento en el muslo.", ["And more growth", "in the thigh."], ["Y más crecimiento", "en el muslo."]),
               L("But it was a small study, so treat it as one piece of evidence.", "Pero fue un estudio pequeño, así que tómalo como una pieza de evidencia.",
                 ["But it was a small study, so treat", "it as one piece of evidence."], ["Pero fue un estudio pequeño: tómalo", "como una pieza de evidencia."])]),
        cta(13, "fourteen", "catorce", "DAY 14 TOMORROW: DAILY STEPS", "Mañana, día 14: pasos diarios"),
    ]
    cap = caption(13, "rest between sets", "descanso entre series",
                  "Is resting longer between sets a waste of time? In an 8-week trial, 21 young resistance-trained men followed the same program resting either 1 or 3 minutes between sets. The 3-minute group gained more maximal strength (squat and bench press) and more anterior-thigh muscle thickness, with a trend toward more triceps growth. It was a small study: one data point, not the final word.",
                  "¿Descansar más entre series es perder tiempo? En un ensayo de 8 semanas, 21 hombres jóvenes entrenados siguieron el mismo programa descansando 1 o 3 minutos entre series. El grupo de 3 minutos ganó más fuerza máxima (sentadilla y press de banca) y más grosor muscular en el muslo, con una tendencia a más crecimiento del tríceps. Fue un estudio pequeño: un dato, no la última palabra.",
                  handle, "Schoenfeld et al., J Strength Cond Res, 2016")
    return {"id": 13, "day": 13, "q": 7, "topic": "rest", "scenes": S, "caption": cap,
            "hashtags": "#restbetweensets #hypertrophy #strengthtraining #gym #workout",
            "source": "Source: Schoenfeld et al., J Strength Cond Res, 2016"}

# ----------------------------------------------------------------------------- DIA 14
def reel_steps(handle):
    S = [
        hook(14, "fourteen", "catorce", "TEACHING YOU: DAILY STEPS", "Enseñándote: pasos diarios", ["HOW MANY STEPS", "DO YOU NEED?"],
             "daily steps", "los pasos diarios",
             ("Do you really need ten thousand steps a day?", ["Do you really need", "10,000 steps a day?"]),
             ("¿De verdad necesitas diez mil pasos al día?", ["¿De verdad necesitas", "10.000 pasos al día?"]), icon="walk"),
        {"type": "stat", "tail": 0.7, "head": "RISK OF DEATH · MOST VS LEAST ACTIVE", "value": "0.47", "vsize": 150, "count": (0.47, "{:.2f}"), "ring": 0.47, "icon": "walk",
         "label": ["hazard ratio: about half", "the risk (observational)"],
         "lines": [L("A meta-analysis pooled fifteen studies and about forty-seven thousand adults.", "Un metaanálisis reunió 15 estudios y unos 47.000 adultos.",
                     ["A meta-analysis pooled 15 studies", "and ~47,000 adults."], ["Un metaanálisis reunió 15 estudios", "y unos 47.000 adultos."]),
                   L("The most active quarter had about half the risk of dying, compared with the least active quarter.",
                     "El cuarto más activo tuvo cerca de la mitad del riesgo de morir, comparado con el cuarto menos activo.",
                     ["The most active quarter had about", "half the risk of dying vs the least."], ["El cuarto más activo tuvo cerca de", "la mitad del riesgo vs el menos activo."]),
                   L("This is an association, not proof of cause.", "Es una asociación, no una prueba de causa.",
                     ["An association,", "not proof of cause."], ["Una asociación,", "no prueba de causa."])]},
        {"type": "stat", "tail": 0.7, "head": "WHERE BENEFITS LEVELLED OFF", "value": "6–10k", "vsize": 120, "ring": 0.6, "icon": "walk",
         "label": ["steps per day, depending", "on age (see below)"],
         "lines": [L("The benefit levelled off at about six to eight thousand steps a day for adults sixty and older.",
                     "El beneficio se estabilizó en unos 6.000 a 8.000 pasos al día en adultos de 60 años o más.",
                     ["It levelled off at ~6,000–8,000", "steps a day for ages 60+."], ["Se estabilizó en ~6.000–8.000", "pasos al día en mayores de 60."]),
                   L("And at about eight to ten thousand steps for adults under sixty.",
                     "Y en unos 8.000 a 10.000 pasos en adultos menores de 60.",
                     ["And ~8,000–10,000 steps", "for adults under 60."], ["Y ~8.000–10.000 pasos", "en menores de 60."])]},
        tips3("TAKEAWAYS", ["walk", "heart", "target"],
              [("More steps, lower risk, up to a point", "Más pasos, menos riesgo, hasta un punto"),
               ("Over 60: ~6,000–8,000. Under 60: ~8,000–10,000", "60+: ~6.000–8.000. Menos de 60: ~8.000–10.000"),
               ("Association, not proof of cause", "Asociación, no prueba de causa")],
              [L("More steps went with lower risk, up to a point.", "Más pasos fue con menor riesgo, hasta cierto punto.",
                 ["More steps went with lower", "risk, up to a point."], ["Más pasos fue con menor", "riesgo, hasta cierto punto."]),
               L("That point depends on age.", "Ese punto depende de la edad.", ["That point", "depends on age."], ["Ese punto", "depende de la edad."]),
               L("And remember, these were observational studies.", "Y recuerda que fueron estudios observacionales.",
                 ["And remember, these were", "observational studies."], ["Y recuerda que fueron", "estudios observacionales."])], anim="circles"),
        cta(14, "fifteen", "quince", "DAY 15 TOMORROW: CAFFEINE", "Mañana, día 15: cafeína"),
    ]
    cap = caption(14, "daily steps", "pasos diarios",
                  "Do you really need 10,000 steps a day? A meta-analysis of 15 international cohorts (47,471 adults, 3,013 deaths) found that more daily steps went with a lower risk of death from any cause: the most active quartile had an adjusted hazard ratio of 0.47 vs the least active. The benefit levelled off at roughly 6,000–8,000 steps/day for adults 60+ and 8,000–10,000 for adults under 60. These are observational data: association, not proof of cause.",
                  "¿De verdad necesitas 10.000 pasos al día? Un metaanálisis de 15 cohortes internacionales (47.471 adultos, 3.013 muertes) halló que más pasos diarios iban con menor riesgo de muerte por cualquier causa: el cuarto más activo tuvo un cociente de riesgo ajustado de 0,47 frente al menos activo. El beneficio se estabilizó en ~6.000–8.000 pasos/día en adultos de 60 años o más y ~8.000–10.000 en menores de 60. Son datos observacionales: asociación, no prueba de causa.",
                  handle, "Paluch et al., Lancet Public Health, 2022")
    return {"id": 14, "day": 14, "q": 7, "topic": "steps", "scenes": S, "caption": cap,
            "hashtags": "#dailysteps #walking #health #longevity #fitness",
            "source": "Source: Paluch et al., Lancet Public Health, 2022"}

# ----------------------------------------------------------------------------- DIA 15
def reel_caffeine(handle):
    S = [
        hook(15, "fifteen", "quince", "TEACHING YOU: CAFFEINE", "Enseñándote: cafeína", ["DOES CAFFEINE", "BOOST TRAINING?"],
             "caffeine", "la cafeína",
             ("How much caffeine helps your workout?", ["How much caffeine", "helps your workout?"]),
             ("¿Cuánta cafeína ayuda en tu entrenamiento?", ["¿Cuánta cafeína ayuda", "en tu entrenamiento?"]), icon="bolt"),
        {"type": "stat", "tail": 0.7, "head": "ISSN POSITION STAND · 2021", "value": "3–6", "vsize": 170, "ring": 0.5, "icon": "bolt",
         "label": ["mg of caffeine per kg", "of body weight"],
         "lines": [L("The International Society of Sports Nutrition says caffeine reliably improves performance at three to six milligrams per kilogram of body weight.",
                     "La Sociedad Internacional de Nutrición Deportiva dice que la cafeína mejora de forma fiable el rendimiento con 3 a 6 miligramos por kilo de peso.",
                     ["The ISSN says caffeine reliably", "improves performance at 3–6 mg", "per kg of body weight."], ["La ISSN dice que la cafeína mejora", "el rendimiento con 3–6 mg", "por kilo de peso."]),
                   L("The most common practice is taking it about sixty minutes before exercise.",
                     "La práctica más común es tomarla unos sesenta minutos antes de entrenar.",
                     ["Most common: take it about", "60 minutes before exercise."], ["Lo más común: tomarla unos", "60 minutos antes de entrenar."]),
                   L("For example, for a seventy-kilo person, that is two hundred ten to four hundred twenty milligrams.",
                     "Por ejemplo, para una persona de 70 kilos son de 210 a 420 miligramos.",
                     ["Example: for a 70 kg person,", "that is 210 to 420 mg."], ["Ejemplo: para 70 kg,", "son 210 a 420 mg."])]},
        tips3("GOOD TO KNOW", ["bolt", "flask", "moon"],
              [("Effective dose may be as low as 2 mg/kg", "La dosis eficaz puede ser de hasta 2 mg/kg"),
               ("Very high doses add side effects", "Dosis muy altas suman efectos adversos"),
               ("May affect sleep or anxiety", "Puede afectar el sueño o la ansiedad")],
              [L("The minimal effective dose may be as low as two milligrams per kilogram.",
                 "La dosis mínima eficaz puede ser de apenas 2 miligramos por kilo.",
                 ["The minimal effective dose may", "be as low as 2 mg/kg."], ["La dosis mínima eficaz puede", "ser de solo 2 mg/kg."]),
               L("Very high doses, like nine milligrams per kilogram, cause more side effects.",
                 "Las dosis muy altas, como 9 miligramos por kilo, causan más efectos adversos.",
                 ["Very high doses, like 9 mg/kg,", "cause more side effects."], ["Dosis muy altas, como 9 mg/kg,", "causan más efectos adversos."]),
               L("And responses vary. It may affect sleep or anxiety in some people.",
                 "Y las respuestas varían. Puede afectar el sueño o la ansiedad en algunas personas.",
                 ["Responses vary. It may affect", "sleep or anxiety in some people."], ["Las respuestas varían. Puede afectar", "el sueño o la ansiedad."])]),
        cta(15, "sixteen", "dieciséis", "DAY 16 TOMORROW: REP SPEED", "Mañana, día 16: velocidad de repetición"),
    ]
    cap = caption(15, "caffeine", "cafeína",
                  "How much caffeine helps your workout? The ISSN position stand (2021) says caffeine reliably improves exercise performance at 3–6 mg/kg of body weight, most commonly taken about 60 minutes before exercise (for a 70 kg person: 210–420 mg). The minimal effective dose may be as low as 2 mg/kg; very high doses (~9 mg/kg) cause more side effects. Responses vary, and caffeine may affect sleep or anxiety in some people. If you have a health condition, ask your doctor.",
                  "¿Cuánta cafeína ayuda en tu entrenamiento? La declaración de posición de la ISSN (2021) dice que la cafeína mejora de forma fiable el rendimiento con 3–6 mg/kg de peso, tomada con más frecuencia unos 60 minutos antes de entrenar (para 70 kg: 210–420 mg). La dosis mínima eficaz puede ser de apenas 2 mg/kg; las dosis muy altas (~9 mg/kg) causan más efectos adversos. Las respuestas varían y la cafeína puede afectar el sueño o la ansiedad en algunas personas. Si tienes una condición médica, consulta a tu médico.",
                  handle, "Guest et al., ISSN position stand, J Int Soc Sports Nutr, 2021")
    return {"id": 15, "day": 15, "q": 7, "topic": "caffeine", "scenes": S, "caption": cap,
            "hashtags": "#caffeine #preworkout #sportsnutrition #gym #fitness",
            "source": "Source: Guest et al., ISSN position stand, 2021"}

# ----------------------------------------------------------------------------- DIA 16
def reel_tempo(handle):
    S = [
        hook(16, "sixteen", "dieciséis", "TEACHING YOU: REP SPEED", "Enseñándote: velocidad de repetición", ["DO SLOW REPS", "BUILD MORE MUSCLE?"],
             "rep speed", "la velocidad de repetición",
             ("Does lifting slower build more muscle?", ["Does lifting slower", "build more muscle?"]),
             ("¿Levantar más lento construye más músculo?", ["¿Levantar más lento", "construye más músculo?"]), icon="clock"),
        {"type": "stat", "tail": 0.7, "head": "REP DURATION · 8 STUDIES", "value": "0.5–8 s", "vsize": 104, "ring": 0.55, "icon": "clock",
         "label": ["per rep: similar muscle", "growth in the studies"],
         "lines": [L("A review of eight studies compared how long each repetition lasts. All sets were taken to muscle failure for at least six weeks.",
                     "Una revisión de 8 estudios comparó cuánto dura cada repetición. Todas las series llegaron al fallo muscular durante al menos seis semanas.",
                     ["A review of 8 studies compared", "rep duration. Sets to failure,", "6 weeks or more."], ["Una revisión de 8 estudios comparó", "la duración de cada repetición.", "Al fallo, 6 semanas o más."]),
                   L("Muscle growth was similar for repetitions lasting from half a second to eight seconds.",
                     "El crecimiento muscular fue similar con repeticiones de medio segundo a ocho segundos.",
                     ["Growth was similar for reps", "lasting 0.5 to 8 seconds."], ["El crecimiento fue similar con", "repeticiones de 0,5 a 8 segundos."])]},
        tips3("TAKEAWAYS", ["clock", "dumbbell", "target"],
              [("0.5–8 s per rep: similar growth", "0,5–8 s por rep: crecimiento similar"),
               ("Very slow (10 s+) may be worse", "Muy lento (10 s+) podría ser peor"),
               ("Pick a speed you can control", "Elige una velocidad que controles")],
              [L("So you don't need to obsess over tempo within that range.", "Así que no hace falta obsesionarse con el tempo dentro de ese rango.",
                 ["So don't obsess over tempo", "within that range."], ["Así que no te obsesiones con", "el tempo en ese rango."]),
               L("Very slow reps, over ten seconds, may be less effective, but few studies exist.",
                 "Las repeticiones muy lentas, de más de diez segundos, podrían ser menos efectivas, pero hay pocos estudios.",
                 ["Very slow reps, over 10 seconds,", "may be less effective. Few studies."], ["Repeticiones muy lentas, de más de 10 s,", "podrían ser menos efectivas. Pocos estudios."]),
               L("A practical suggestion: choose a speed you can control.", "Una sugerencia práctica: elige una velocidad que puedas controlar.",
                 ["A practical suggestion: choose", "a speed you can control."], ["Una sugerencia práctica: elige", "una velocidad que controles."])]),
        cta(16, "seventeen", "diecisiete", "DAY 17 TOMORROW: LIFTING & LONGEVITY", "Mañana, día 17: pesas y longevidad"),
    ]
    cap = caption(16, "rep speed", "velocidad de repetición",
                  "Does lifting slower build more muscle? A systematic review and meta-analysis of 8 studies (training to failure for at least 6 weeks) found similar hypertrophy with repetition durations from 0.5 to 8 seconds. Very slow repetitions (over ~10 s) may be less effective, but few controlled studies exist, so conclusions are tentative. (\"Choose a speed you can control\" is a practical suggestion, not a finding.)",
                  "¿Levantar más lento construye más músculo? Una revisión sistemática y metaanálisis de 8 estudios (entrenando al fallo durante al menos 6 semanas) halló una hipertrofia similar con repeticiones de 0,5 a 8 segundos. Las repeticiones muy lentas (más de ~10 s) podrían ser menos efectivas, pero hay pocos estudios controlados, así que las conclusiones son provisorias. («Elige una velocidad que controles» es una sugerencia práctica, no un hallazgo.)",
                  handle, "Schoenfeld, Ogborn & Krieger, Sports Med, 2015")
    return {"id": 16, "day": 16, "q": 7, "topic": "tempo", "scenes": S, "caption": cap,
            "hashtags": "#repspeed #tempo #hypertrophy #gym #musclebuilding",
            "source": "Source: Schoenfeld, Ogborn & Krieger, Sports Med, 2015"}

# ----------------------------------------------------------------------------- DIA 17
def reel_longevity(handle):
    S = [
        hook(17, "seventeen", "diecisiete", "TEACHING YOU: LIFTING & LONGEVITY", "Enseñándote: pesas y longevidad", ["DOES LIFTING", "HELP YOU LIVE LONGER?"],
             "lifting and health", "las pesas y la salud",
             ("Is strength training good for more than muscle?", ["Is strength training good", "for more than muscle?"]),
             ("¿El entrenamiento de fuerza sirve para más que el músculo?", ["¿La fuerza sirve para", "más que el músculo?"]), icon="heart"),
        {"type": "stat", "tail": 0.7, "head": "MUSCLE-STRENGTHENING · 16 STUDIES", "value": "10–17%", "vsize": 112, "ring": 0.4, "icon": "heart",
         "label": ["lower risk of death, heart", "disease, cancer, diabetes"],
         "lines": [L("A review of sixteen studies looked at muscle-strengthening activity and health.",
                     "Una revisión de 16 estudios analizó la actividad de fortalecimiento muscular y la salud.",
                     ["A review of 16 studies looked at", "muscle-strengthening and health."], ["Una revisión de 16 estudios analizó", "el fortalecimiento muscular y la salud."]),
                   L("It was linked to ten to seventeen percent lower risk of death from any cause, heart disease, total cancer, diabetes and lung cancer.",
                     "Se asoció con un 10 a 17 % menos de riesgo de muerte por cualquier causa, enfermedad cardíaca, cáncer total, diabetes y cáncer de pulmón.",
                     ["Linked to 10–17% lower risk of death,", "heart disease, cancer, diabetes", "and lung cancer."], ["Asociado a 10–17 % menos riesgo de muerte,", "enfermedad cardíaca, cáncer, diabetes", "y cáncer de pulmón."]),
                   L("These were observational studies, so it is an association.", "Fueron estudios observacionales, así que es una asociación.",
                     ["Observational studies:", "an association."], ["Estudios observacionales:", "una asociación."])]},
        {"type": "stat", "tail": 0.7, "head": "BIGGEST BENEFIT AT", "value": "30–60", "vsize": 150, "ring": 0.5, "icon": "clock",
         "label": ["minutes per week (about", "10–20% lower risk)"],
         "lines": [L("The biggest risk reduction, about ten to twenty percent, appeared at thirty to sixty minutes per week.",
                     "La mayor reducción del riesgo, de un 10 a 20 %, apareció con 30 a 60 minutos por semana.",
                     ["The biggest risk reduction, ~10–20%,", "was at 30–60 minutes per week."], ["La mayor reducción del riesgo, ~10–20 %,", "fue con 30–60 minutos por semana."]),
                   L("Doing it along with aerobic activity was linked to even lower risk of death.",
                     "Hacerlo junto con actividad aeróbica se asoció con un riesgo de muerte aún menor.",
                     ["Combined with aerobic activity,", "even lower risk of death."], ["Combinado con actividad aeróbica,", "un riesgo de muerte aún menor."])]},
        tips3("TAKEAWAYS", ["dumbbell", "heart", "flask"],
              [("30–60 min/week of lifting: biggest benefit", "30–60 min/semana: el mayor beneficio"),
               ("Add it to aerobic activity", "Súmalo a la actividad aeróbica"),
               ("Observational: association only", "Observacional: solo asociación")],
              [L("Thirty to sixty minutes a week showed the biggest benefit.", "De 30 a 60 minutos por semana mostraron el mayor beneficio.",
                 ["30 to 60 minutes a week", "showed the biggest benefit."], ["30 a 60 minutos por semana", "mostraron el mayor beneficio."]),
               L("And combining it with aerobic activity looked even better.", "Y combinarlo con actividad aeróbica se vio aún mejor.",
                 ["And combining it with aerobic", "activity looked even better."], ["Y combinarlo con actividad", "aeróbica se vio aún mejor."]),
               L("Remember, it is an association, not proof.", "Recuerda que es una asociación, no una prueba.",
                 ["Remember, it is an", "association, not proof."], ["Recuerda: es una asociación,", "no una prueba."])]),
        cta(17, "eighteen", "dieciocho", "DAY 18 TOMORROW: CARDIO + WEIGHTS", "Mañana, día 18: cardio y pesas"),
    ]
    cap = caption(17, "lifting and longevity", "pesas y longevidad",
                  "Is strength training good for more than muscle? A systematic review and meta-analysis of 16 cohort studies found that muscle-strengthening activity was associated with 10–17% lower risk of all-cause mortality, cardiovascular disease, total cancer, diabetes and lung cancer. The biggest risk reduction (~10–20%) appeared at about 30–60 minutes per week, and combining it with aerobic activity was linked to lower mortality. These are observational studies: association, not proof of cause.",
                  "¿El entrenamiento de fuerza sirve para más que el músculo? Una revisión sistemática y metaanálisis de 16 estudios de cohorte halló que la actividad de fortalecimiento muscular se asoció con un 10–17 % menos de riesgo de mortalidad por todas las causas, enfermedad cardiovascular, cáncer total, diabetes y cáncer de pulmón. La mayor reducción del riesgo (~10–20 %) apareció con unos 30–60 minutos por semana, y combinarlo con actividad aeróbica se asoció con menor mortalidad. Son estudios observacionales: asociación, no prueba de causa.",
                  handle, "Momma et al., Br J Sports Med, 2022")
    return {"id": 17, "day": 17, "q": 7, "topic": "longevity", "scenes": S, "caption": cap,
            "hashtags": "#strengthtraining #longevity #health #weightlifting #fitness",
            "source": "Source: Momma et al., Br J Sports Med, 2022"}

# ----------------------------------------------------------------------------- DIA 18
def reel_concurrent(handle):
    S = [
        hook(18, "eighteen", "dieciocho", "TEACHING YOU: CARDIO + WEIGHTS", "Enseñándote: cardio y pesas", ["DOES CARDIO KILL", "YOUR MUSCLE GAINS?"],
             "cardio and weights", "cardio y pesas",
             ("Will cardio ruin your muscle gains?", ["Will cardio ruin", "your muscle gains?"]),
             ("¿El cardio arruina tus ganancias de músculo?", ["¿El cardio arruina", "tus ganancias de músculo?"]), icon="flame"),
        {"type": "stat", "tail": 0.7, "head": "ADDING CARDIO TO STRENGTH TRAINING", "value": "43", "vsize": 190, "count": (43, "{:.0f}"), "ring": 0.5, "icon": "flame", "anim": "jack",
         "label": ["studies reviewed in this", "meta-analysis"],
         "lines": [L("A meta-analysis of forty-three studies asked: does adding aerobic training hurt your strength training results?",
                     "Un metaanálisis de 43 estudios preguntó: ¿sumar entrenamiento aeróbico perjudica los resultados de tu entrenamiento de fuerza?",
                     ["A meta-analysis of 43 studies: does", "adding aerobic training hurt your", "strength training results?"], ["Metaanálisis de 43 estudios: ¿sumar", "entrenamiento aeróbico perjudica", "tus resultados de fuerza?"]),
                   L("Adding cardio did not meaningfully affect muscle size or maximal strength.",
                     "Sumar cardio no afectó de forma relevante el tamaño muscular ni la fuerza máxima.",
                     ["Adding cardio did not meaningfully", "affect muscle size or max strength."], ["Sumar cardio no afectó de forma relevante", "el tamaño muscular ni la fuerza máxima."])]},
        tips3("WHAT WAS AFFECTED", ["flame", "dumbbell", "bolt"],
              [("Muscle size: not meaningfully affected", "Tamaño muscular: sin efecto relevante"),
               ("Max strength: not meaningfully affected", "Fuerza máxima: sin efecto relevante"),
               ("Explosive strength: reduced", "Fuerza explosiva: reducida")],
              [L("Muscle size was not meaningfully affected.", "El tamaño muscular no se vio afectado de forma relevante.",
                 ["Muscle size was not", "meaningfully affected."], ["El tamaño muscular no se vio", "afectado de forma relevante."]),
               L("Neither was maximal strength.", "Tampoco la fuerza máxima.", ["Neither was", "maximal strength."], ["Tampoco la", "fuerza máxima."]),
               L("But explosive strength gains were reduced, more so when both were done in the same session.",
                 "Pero las ganancias de fuerza explosiva se redujeron, más cuando se hacían en la misma sesión.",
                 ["But explosive strength gains were", "reduced, more in the same session."], ["Pero la fuerza explosiva se redujo,", "más en la misma sesión."])], anim="squat"),
        {"type": "cta", "tail": 1.0, "next_en": "MORE LESSONS COMING", "next_es": "Vienen más lecciones",
         "lines": [L("Save this, and send it to a friend who skips cardio.", "Guárdalo y envíaselo a un amigo que se salta el cardio.",
                     ["Save this, and send it to a", "friend who skips cardio."], ["Guárdalo y envíaselo a un", "amigo que se salta el cardio."]),
                   L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
                     ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]},
    ]
    cap = (f"Day 18 teaching you: cardio and weights 💪\n"
           f"Will cardio ruin your muscle gains? An updated systematic review and meta-analysis of 43 studies found that adding aerobic training to strength training did not meaningfully affect muscle hypertrophy or maximal strength. Explosive strength gains were reduced, and more so when both were done in the same session. No significant influence of aerobic modality, frequency, training status or age was found.\n\n"
           f"Día 18 enseñándote: cardio y pesas 💪\n"
           f"¿El cardio arruina tus ganancias de músculo? Una revisión sistemática y metaanálisis actualizado de 43 estudios halló que sumar entrenamiento aeróbico al de fuerza no afectó de forma relevante la hipertrofia muscular ni la fuerza máxima. Las ganancias de fuerza explosiva se redujeron, y más cuando ambos se hacían en la misma sesión. No se halló influencia significativa de la modalidad aeróbica, la frecuencia, el nivel de entrenamiento ni la edad.\n\n"
           f"Save this 📌 and follow {handle}. / Guárdalo y sigue a {handle}.\n"
           f"Source / Fuente: Schumann et al., Sports Med, 2022.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return {"id": 18, "day": 18, "q": 7, "topic": "concurrent", "scenes": S, "caption": cap,
            "hashtags": "#cardio #strengthtraining #hypertrophy #gym #fitness",
            "source": "Source: Schumann et al., Sports Med, 2022"}

REELS_MORE2 = {13: reel_rest, 14: reel_steps, 15: reel_caffeine, 16: reel_tempo, 17: reel_longevity, 18: reel_concurrent}
