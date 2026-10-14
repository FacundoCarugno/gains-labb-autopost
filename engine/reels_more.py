"""reels_more.py -- Dias 6 a 12 de la serie Gains Lab (contenido verificado + nivel de calidad q = dia - 5)."""


def L(en, es, sub_en, sub_es):
    assert len(sub_en) == len(sub_es), (en, sub_en, sub_es)
    return {"en": en, "es": es, "sub_en": sub_en, "sub_es": sub_es}


def hook(day, day_en, day_es, teach_en, teach_es, title, topic_en, topic_es, q_en, q_es, icon=None):
    return {"type": "hook", "tail": 0.55, "day": day, "teach_en": teach_en, "teach_es": teach_es, "title": title, "icon": icon,
            "lines": [L(f"Day {day_en}, teaching you about {topic_en}.", f"Día {day_es}, enseñándote sobre {topic_es}.",
                        [f"Day {day}, teaching you", f"about {topic_en}."], [f"Día {day}, enseñándote", f"sobre {topic_es}."]),
                      q_en_es(q_en, q_es)]}


def q_en_es(q_en, q_es):
    # q_en / q_es: (texto, [chunks])
    return L(q_en[0], q_es[0], q_en[1], q_es[1])


def cta(day, next_day_en, next_day_es, next_en, next_es, closing=None):
    lines = [L(f"Save this, and come back tomorrow for day {next_day_en}.", f"Guárdalo y vuelve mañana para el día {next_day_es}.",
               ["Save this, and come back", f"tomorrow for Day {day + 1}."], ["Guárdalo y vuelve mañana", f"para el Día {day + 1}."]),
             L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
               ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]
    return {"type": "cta", "tail": 1.0, "next_en": next_en, "next_es": next_es, "lines": lines}


def caption(day, title_en, title_es, body_en, body_es, handle, source_full):
    return (f"Day {day} teaching you: {title_en} 💪\n{body_en}\n\n"
            f"Día {day} enseñándote: {title_es} 💪\n{body_es}\n\n"
            f"Save this 📌 and follow {handle} — Day {day + 1} tomorrow. / Guárdalo y sigue a {handle}: mañana, Día {day + 1}.\n"
            f"Source / Fuente: {source_full}.\n"
            f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")


# ----------------------------------------------------------------------------- DIA 6
def reel_calories(handle):
    S = [
        hook(6, "six", "seis", "TEACHING YOU: CALORIE DEFICIT", "Enseñándote: déficit calórico", ["HOW DOES A", "CALORIE DEFICIT WORK?"],
             "the calorie deficit", "el déficit calórico",
             ("Why does weight loss slow down over time?", ["Why does weight loss", "slow down over time?"]),
             ("¿Por qué la pérdida de peso se frena con el tiempo?", ["¿Por qué la pérdida de peso", "se frena con el tiempo?"])),
        {"type": "stat", "tail": 0.7, "head": "ENERGY INTAKE CHANGE", "value": "24", "ring": 0.3,
         "label": ["kcal per day ≈ 1 kg", "of eventual weight change"],
         "lines": [L("A deficit means eating less energy than your body uses.", "Un déficit es comer menos energía de la que tu cuerpo usa.",
                     ["A deficit means eating less", "energy than your body uses."], ["Un déficit es comer menos", "energía de la que tu cuerpo usa."]),
                   L("A well-known Lancet model estimated that every twenty-four calories a day of change leads to about one kilo of eventual weight change.",
                     "Un modelo conocido de The Lancet estimó que cada 24 calorías diarias de cambio llevan a cerca de un kilo de cambio de peso final.",
                     ["A Lancet model estimated: every", "24 calories a day of change means", "about 1 kg of eventual change."],
                     ["Un modelo de The Lancet estimó: cada", "24 calorías diarias de cambio son", "cerca de 1 kg de cambio final."]),
                   L("That model was built for the average overweight adult.", "Ese modelo se hizo para el adulto promedio con sobrepeso.",
                     ["That model was built for", "the average overweight adult."], ["Ese modelo se hizo para", "el adulto promedio con sobrepeso."])]},
        {"type": "tips", "tail": 0.6, "head": "WHAT TO EXPECT",
         "items": [("Weight loss slows as you get lighter", "La pérdida de peso se frena a medida que bajas"),
                   ("Half of the change takes about a year", "La mitad del cambio tarda cerca de un año"),
                   ("Think in months, not days", "Piensa en meses, no en días")],
         "lines": [L("Weight loss tends to slow down as you get lighter.", "La pérdida de peso tiende a frenarse a medida que bajas de peso.",
                     ["Weight loss tends to slow", "as you get lighter."], ["La pérdida de peso tiende a frenarse", "a medida que bajas."]),
                   L("In that model, half of the eventual change took about a year.", "En ese modelo, la mitad del cambio final tardó cerca de un año.",
                     ["In that model, half of the", "eventual change took about a year."], ["En ese modelo, la mitad del", "cambio final tardó cerca de un año."]),
                   L("So think in months, not days.", "Así que piensa en meses, no en días.",
                     ["So think in months,", "not days."], ["Así que piensa en meses,", "no en días."])]},
        cta(6, "seven", "siete", "DAY 7 TOMORROW: GYM MYTHS", "Mañana, día 7: mitos del gimnasio"),
    ]
    cap = caption(6, "calorie deficit", "déficit calórico",
                  "Why does weight loss slow down? A Lancet modelling study (Hall et al.) estimated that, for an average overweight adult, every ~24 kcal/day change in intake leads to about 1 kg of eventual weight change, with half of it taking about a year. So the 'constant loss forever' idea doesn't hold: think in months, not days.",
                  "¿Por qué la pérdida de peso se frena? Un estudio de modelado en The Lancet (Hall et al.) estimó que, en un adulto promedio con sobrepeso, cada cambio de ~24 kcal/día en la ingesta lleva a cerca de 1 kg de cambio final de peso, y la mitad tarda cerca de un año. Piensa en meses, no en días.",
                  handle, "Hall et al., The Lancet, 2011")
    return {"id": 6, "day": 6, "q": 1, "topic": "calories", "scenes": S, "caption": cap,
            "hashtags": "#caloriedeficit #weightloss #nutrition #fitness #health", "source": "Source: Hall et al., The Lancet, 2011"}


# ----------------------------------------------------------------------------- DIA 7
def reel_myths(handle):
    S = [
        hook(7, "seven", "siete", "TEACHING YOU: GYM MYTHS", "Enseñándote: mitos del gimnasio", ["3 GYM MYTHS", "WORTH DROPPING"],
             "gym myths", "los mitos del gimnasio",
             ("Three common beliefs that research does not support.", ["Three common beliefs that", "research does not support."]),
             ("Tres creencias comunes que la investigación no respalda.", ["Tres creencias comunes que", "la investigación no respalda."])),
        {"type": "stat", "tail": 0.7, "head": "MYTH 1: SPOT REDUCTION", "value": "6", "ring": 0.5,
         "label": ["weeks of ab exercises", "did not cut belly fat"],
         "lines": [L("Myth one: crunches burn belly fat.", "Mito uno: los abdominales queman la grasa del vientre.",
                     ["Myth 1: crunches", "burn belly fat."], ["Mito 1: los abdominales", "queman la grasa del vientre."]),
                   L("In one trial, twenty-four adults did six weeks of ab exercises, with no significant drop in abdominal fat.",
                     "En un ensayo, 24 adultos hicieron seis semanas de abdominales, sin una baja significativa de grasa abdominal.",
                     ["In one trial, 24 adults did 6 weeks", "of ab exercises, with no significant", "drop in abdominal fat."],
                     ["En un ensayo, 24 adultos hicieron 6", "semanas de abdominales, sin una baja", "significativa de grasa abdominal."])]},
        {"type": "stat", "tail": 0.7, "head": "MYTH 2: THE ANABOLIC WINDOW", "value": "23", "ring": 0.5,
         "label": ["studies analyzed", "no significant timing effect"],
         "lines": [L("Myth two: you must eat protein right after training.", "Mito dos: debes comer proteína justo después de entrenar.",
                     ["Myth 2: you must eat protein", "right after training."], ["Mito 2: debes comer proteína", "justo después de entrenar."]),
                   L("A meta-analysis of twenty-three studies found no significant effect of protein timing once other factors were controlled.",
                     "Un metaanálisis de 23 estudios no halló un efecto significativo del momento de la proteína al controlar otros factores.",
                     ["A meta-analysis of 23 studies found", "no significant timing effect once", "other factors were controlled."],
                     ["Un metaanálisis de 23 estudios no halló", "un efecto significativo del momento al", "controlar otros factores."]),
                   L("Total daily protein was the strongest predictor of growth.", "La proteína total diaria fue el mejor predictor de crecimiento.",
                     ["Total daily protein was the", "strongest predictor of growth."], ["La proteína total diaria fue el", "mejor predictor de crecimiento."])]},
        {"type": "tips", "tail": 0.6, "head": "MYTH 3: SORE = GROWTH",
         "items": [("Soreness is a weak signal of damage", "El dolor es una señal débil de daño"),
                   ("Not a reliable predictor of growth", "No es un predictor fiable de crecimiento"),
                   ("Don't judge a workout by soreness", "No juzgues un entreno por el dolor")],
         "lines": [L("Myth three says soreness means growth. But soreness is a weak signal of muscle damage.",
                     "El mito tres dice que el dolor significa crecimiento. Pero el dolor es una señal débil de daño muscular.",
                     ["Myth 3 says soreness means growth.", "But it is a weak signal of damage."], ["El mito 3 dice que dolor es crecimiento.", "Pero es una señal débil de daño."]),
                   L("Researchers conclude it is not a reliable predictor of muscle growth.", "Los investigadores concluyen que no es un predictor fiable de crecimiento muscular.",
                     ["Researchers conclude it is not a", "reliable predictor of growth."], ["Concluyen que no es un predictor", "fiable de crecimiento muscular."]),
                   L("So don't judge a workout by how sore you feel.", "Así que no juzgues un entreno por cuánto dolor sientes.",
                     ["So don't judge a workout", "by how sore you feel."], ["Así que no juzgues un entreno", "por cuánto dolor sientes."])]},
        cta(7, "eight", "ocho", "DAY 8 TOMORROW: FREQUENCY", "Mañana, día 8: frecuencia de entrenamiento"),
    ]
    cap = caption(7, "3 gym myths", "3 mitos del gimnasio",
                  "1) Spot reduction: in a 6-week trial of 24 adults, ab exercises alone did not significantly reduce abdominal fat. 2) The 'anabolic window': a meta-analysis of 23 studies found no significant effect of protein timing once other factors were controlled; total daily protein was the strongest predictor. 3) Soreness is a weak, unreliable indicator of muscle growth.",
                  "1) Reducción localizada: en un ensayo de 6 semanas con 24 adultos, los abdominales solos no redujeron significativamente la grasa abdominal. 2) La 'ventana anabólica': un metaanálisis de 23 estudios no halló un efecto significativo del momento de la proteína al controlar otros factores; la proteína total diaria fue el mejor predictor. 3) El dolor muscular es un indicador débil y poco fiable de crecimiento.",
                  handle, "Vispute et al., J Strength Cond Res, 2011; Schoenfeld et al., J Int Soc Sports Nutr, 2013; Schoenfeld & Contreras, Strength Cond J, 2013")
    return {"id": 7, "day": 7, "q": 2, "topic": "myths", "scenes": S, "caption": cap,
            "hashtags": "#gymmyths #fitnessfacts #musclegrowth #bellyfat #gym",
            "source": "Source: Vispute 2011; Schoenfeld 2013; Schoenfeld & Contreras 2013"}


# ----------------------------------------------------------------------------- DIA 8
def reel_frequency(handle):
    S = [
        hook(8, "eight", "ocho", "TEACHING YOU: FREQUENCY", "Enseñándote: frecuencia de entrenamiento", ["HOW OFTEN SHOULD", "YOU TRAIN A MUSCLE?"],
             "training frequency", "la frecuencia de entrenamiento",
             ("How many times a week should you train each muscle?", ["How many times a week should", "you train each muscle?"]),
             ("¿Cuántas veces por semana debes entrenar cada músculo?", ["¿Cuántas veces por semana debes", "entrenar cada músculo?"]), icon="calendar"),
        {"type": "stat", "tail": 0.7, "head": "WHEN WEEKLY SETS ARE EQUAL", "value": "SAME", "vsize": 118, "ring": 0.5, "icon": "calendar",
         "label": ["frequency did not appear", "to change muscle growth"],
         "lines": [L("A meta-analysis compared how many times per week people trained each muscle.",
                     "Un metaanálisis comparó cuántas veces por semana se entrenaba cada músculo.",
                     ["A meta-analysis compared how many", "times per week people trained a muscle."], ["Un metaanálisis comparó cuántas veces", "por semana se entrenaba cada músculo."]),
                   L("When total weekly sets were equal, frequency did not appear to influence muscle growth.",
                     "Cuando las series semanales totales eran iguales, la frecuencia no pareció influir en el crecimiento muscular.",
                     ["When total weekly sets were equal,", "frequency did not appear to", "influence muscle growth."],
                     ["Con las mismas series semanales totales,", "la frecuencia no pareció influir", "en el crecimiento muscular."]),
                   L("When sets were not equal, more sessions went with a bit more growth, but the difference was modest.",
                     "Cuando las series no eran iguales, más sesiones fueron con un poco más de crecimiento, pero la diferencia fue modesta.",
                     ["When sets were not equal, more", "sessions went with a bit more growth,", "but the difference was modest."],
                     ["Con series distintas, más sesiones iban", "con un poco más de crecimiento,", "pero la diferencia fue modesta."])]},
        {"type": "tips", "tail": 0.6, "head": "WHAT THIS MEANS", "icons": ["target", "calendar", "check"],
         "items": [("Weekly total sets matter most", "Lo que más importa: series semanales totales"),
                   ("Pick a schedule you can repeat", "Elige un horario que puedas repetir"),
                   ("Missed a day? Move the sets", "¿Faltaste un día? Mueve las series")],
         "lines": [L("What matters most is hitting your total weekly sets.", "Lo que más importa es completar tus series semanales totales.",
                     ["What matters most is hitting", "your total weekly sets."], ["Lo que más importa es completar", "tus series semanales totales."]),
                   L("So pick a schedule you can actually repeat.", "Así que elige un horario que realmente puedas repetir.",
                     ["So pick a schedule you", "can actually repeat."], ["Así que elige un horario que", "realmente puedas repetir."]),
                   L("Missed a day? Move the sets to another day.", "¿Faltaste un día? Mueve las series a otro día.",
                     ["Missed a day? Move the", "sets to another day."], ["¿Faltaste un día? Mueve las", "series a otro día."])]},
        cta(8, "nine", "nueve", "DAY 9 TOMORROW: REP RANGES", "Mañana, día 9: repeticiones"),
    ]
    cap = caption(8, "training frequency", "frecuencia de entrenamiento",
                  "How many times a week should you train a muscle? A meta-analysis (Schoenfeld, Grgic & Krieger) found that when total weekly sets were equal, training frequency did not appear to influence muscle growth. When sets were not equal, higher frequencies went with a modest advantage. Total weekly volume is what to hit; pick a schedule you can repeat.",
                  "¿Cuántas veces por semana entrenar un músculo? Un metaanálisis (Schoenfeld, Grgic y Krieger) halló que, con las mismas series semanales totales, la frecuencia no pareció influir en el crecimiento muscular. Con series distintas, las frecuencias mayores iban con una ventaja modesta. Lo importante es el volumen semanal; elige un horario que puedas repetir.",
                  handle, "Schoenfeld, Grgic & Krieger, J Sports Sci, 2019")
    return {"id": 8, "day": 8, "q": 3, "topic": "frequency", "scenes": S, "caption": cap,
            "hashtags": "#traininfrequency #hypertrophy #musclegrowth #gym #fitness".replace("traininfrequency", "trainingfrequency"),
            "source": "Source: Schoenfeld, Grgic & Krieger, J Sports Sci, 2019"}


# ----------------------------------------------------------------------------- DIA 9
def reel_reps(handle):
    S = [
        hook(9, "nine", "nueve", "TEACHING YOU: REP RANGES", "Enseñándote: repeticiones", ["IS THERE A", "BEST REP RANGE?"],
             "rep ranges", "las repeticiones",
             ("Do you need heavy weights to grow muscle?", ["Do you need heavy weights", "to grow muscle?"]),
             ("¿Necesitas pesos altos para crecer?", ["¿Necesitas pesos altos", "para crecer?"]), icon="dumbbell"),
        {"type": "vs", "tail": 0.7, "head": "MUSCLE SIZE GAIN", "sub": "21 studies, 630 people, sets near failure",
         "rows": [{"title": "Heavy loads", "sub": "above 60% of 1RM", "es": "Cargas pesadas", "val": 8.3, "fmt": "{:.1f}%"},
                  {"title": "Light loads", "sub": "60% of 1RM or less", "es": "Cargas livianas", "val": 7.0, "fmt": "{:.1f}%"}],
         "lines": [L("A meta-analysis of twenty-one studies compared heavy and light loads, both trained close to failure.",
                     "Un metaanálisis de 21 estudios comparó cargas pesadas y livianas, ambas entrenadas cerca del fallo.",
                     ["A meta-analysis of 21 studies compared", "heavy and light loads, both", "trained close to failure."],
                     ["Un metaanálisis de 21 estudios comparó", "cargas pesadas y livianas, ambas", "entrenadas cerca del fallo."]),
                   L("For muscle size, heavy loads gave about eight point three percent.", "Para el tamaño muscular, las cargas pesadas dieron cerca de 8,3 %.",
                     ["For muscle size, heavy", "loads gave about 8.3%."], ["En tamaño muscular, las cargas", "pesadas dieron cerca de 8,3 %."]),
                   L("Light loads, about seven percent. Not a significant difference.", "Las livianas, cerca de 7 %. No fue una diferencia significativa.",
                     ["Light loads, about 7%.", "Not a significant difference."], ["Las livianas, cerca de 7 %.", "Diferencia no significativa."])]},
        {"type": "vs", "tail": 0.7, "head": "STRENGTH GAIN (1RM)", "sub": "heavy loads gave significantly more",
         "rows": [{"title": "Heavy loads", "sub": "above 60% of 1RM", "es": "Cargas pesadas", "val": 35.4, "fmt": "{:.1f}%", "win": True},
                  {"title": "Light loads", "sub": "60% of 1RM or less", "es": "Cargas livianas", "val": 28.0, "fmt": "{:.1f}%"}],
         "lines": [L("Strength told a different story.", "La fuerza contó otra historia.", ["Strength told", "a different story."], ["La fuerza contó", "otra historia."]),
                   L("Heavy loads: about thirty-five percent stronger.", "Cargas pesadas: cerca de 35 % más de fuerza.",
                     ["Heavy loads: about", "35% stronger."], ["Cargas pesadas: cerca de", "35 % más de fuerza."]),
                   L("Light loads: about twenty-eight percent.", "Cargas livianas: cerca de 28 %.", ["Light loads:", "about 28%."], ["Cargas livianas:", "cerca de 28 %."])]},
        {"type": "tips", "tail": 0.6, "head": "TAKEAWAYS", "icons": ["dumbbell", "flame", "target"],
         "items": [("Muscle size: both can work", "Tamaño muscular: ambas pueden funcionar"),
                   ("Strength: heavier loads win", "Fuerza: ganan las cargas más pesadas"),
                   ("Train hard, close to failure", "Entrena duro, cerca del fallo")],
         "lines": [L("For muscle size, both heavy and light loads can work.", "Para el tamaño muscular, pueden funcionar tanto las cargas pesadas como las livianas.",
                     ["For muscle size, both heavy", "and light loads can work."], ["Para el tamaño muscular, sirven", "cargas pesadas y livianas."]),
                   L("For strength, heavier loads came out ahead.", "Para la fuerza, las cargas más pesadas salieron adelante.",
                     ["For strength, heavier", "loads came out ahead."], ["Para la fuerza, las cargas", "más pesadas salieron adelante."]),
                   L("And in these studies, sets were taken close to failure.", "Y en estos estudios, las series se llevaron cerca del fallo.",
                     ["And in these studies, sets were", "taken close to failure."], ["Y en estos estudios, las series", "se llevaron cerca del fallo."])]},
        cta(9, "ten", "diez", "DAY 10 TOMORROW: WHO GUIDE", "Mañana, día 10: guía de la OMS"),
    ]
    cap = caption(9, "rep ranges", "repeticiones",
                  "Do you need heavy weights to grow muscle? A meta-analysis of 21 studies (630 people, mostly untrained) compared heavy (>60% 1RM) and light (≤60% 1RM) loads, all taken close to failure. Muscle size gains: ~8.3% vs ~7.0% (not a significant difference). Strength gains: ~35.4% vs ~28.0% (heavy loads significantly more).",
                  "¿Necesitas pesos altos para crecer? Un metaanálisis de 21 estudios (630 personas, la mayoría sin entrenamiento previo) comparó cargas pesadas (>60 % 1RM) y livianas (≤60 % 1RM), todas llevadas cerca del fallo. Ganancia de tamaño muscular: ~8,3 % vs ~7,0 % (diferencia no significativa). Ganancia de fuerza: ~35,4 % vs ~28,0 % (significativamente más con cargas pesadas).",
                  handle, "Schoenfeld et al., J Strength Cond Res, 2017")
    return {"id": 9, "day": 9, "q": 4, "topic": "reps", "scenes": S, "caption": cap,
            "hashtags": "#hypertrophy #strengthtraining #muscle #gym #workout",
            "source": "Source: Schoenfeld et al., J Strength Cond Res, 2017"}


# ----------------------------------------------------------------------------- DIA 10
def reel_who(handle):
    S = [
        hook(10, "ten", "diez", "TEACHING YOU: WHO GUIDE", "Enseñándote: guía de la OMS", ["HOW MUCH MOVEMENT", "DO ADULTS NEED?"],
             "the World Health Organization guide", "la guía de la OMS",
             ("How much physical activity does a healthy adult need?", ["How much physical activity", "does an adult need?"]),
             ("¿Cuánta actividad física necesita un adulto?", ["¿Cuánta actividad física", "necesita un adulto?"]), icon="walk"),
        {"type": "stat", "tail": 0.7, "head": "WHO GUIDELINES · ADULTS", "value": "150–300", "vsize": 86, "ring": 0.5, "icon": "walk",
         "label": ["minutes of moderate", "activity per week"],
         "lines": [L("The World Health Organization updated its guidelines in twenty twenty.", "La Organización Mundial de la Salud actualizó sus guías en 2020.",
                     ["The World Health Organization", "updated its guidelines in 2020."], ["La Organización Mundial de la Salud", "actualizó sus guías en 2020."]),
                   L("For adults, it recommends one hundred fifty to three hundred minutes of moderate activity per week.",
                     "Para adultos, recomienda de 150 a 300 minutos de actividad moderada por semana.",
                     ["For adults: 150 to 300 minutes", "of moderate activity per week."], ["Para adultos: de 150 a 300 minutos", "de actividad moderada por semana."]),
                   L("Or seventy-five to a hundred fifty minutes of vigorous activity, or an equivalent mix.",
                     "O de 75 a 150 minutos de actividad intensa, o una combinación equivalente.",
                     ["Or 75 to 150 minutes of vigorous", "activity, or an equivalent mix."], ["O de 75 a 150 minutos de actividad", "intensa, o una mezcla equivalente."])]},
        {"type": "stat", "tail": 0.7, "head": "MUSCLE STRENGTHENING", "value": "2+", "ring": 0.29, "icon": "dumbbell",
         "label": ["days per week, all", "major muscle groups"],
         "lines": [L("It also recommends muscle-strengthening activities on at least two days per week.",
                     "También recomienda actividades de fortalecimiento muscular al menos dos días por semana.",
                     ["It also recommends muscle-strengthening", "activities on 2 or more days a week."], ["También recomienda fortalecimiento", "muscular 2 o más días por semana."]),
                   L("Involving all major muscle groups, at moderate or greater intensity.",
                     "Con todos los grandes grupos musculares, a intensidad moderada o mayor.",
                     ["Involving all major muscle groups,", "at moderate or greater intensity."], ["Con todos los grandes grupos musculares,", "a intensidad moderada o mayor."])]},
        {"type": "tips", "tail": 0.6, "head": "TAKEAWAYS", "icons": ["walk", "dumbbell", "heart"],
         "items": [("Brisk walking counts as moderate", "Caminar rápido cuenta como moderado"),
                   ("Add strength work on 2+ days", "Suma fuerza 2 o más días"),
                   ("Health condition? Ask your doctor", "¿Condición médica? Consulta a tu médico")],
         "lines": [L("Brisk walking counts as moderate activity.", "Caminar rápido cuenta como actividad moderada.",
                     ["Brisk walking counts", "as moderate activity."], ["Caminar rápido cuenta", "como actividad moderada."]),
                   L("Then add strength work on two or more days.", "Luego suma trabajo de fuerza dos o más días.",
                     ["Then add strength work", "on 2 or more days."], ["Luego suma trabajo de fuerza", "2 o más días."]),
                   L("If you have a health condition, ask your doctor first.", "Si tienes una condición médica, consulta antes a tu médico.",
                     ["If you have a health condition,", "ask your doctor first."], ["Si tienes una condición médica,", "consulta antes a tu médico."])]},
        cta(10, "eleven", "once", "DAY 11 TOMORROW: WARM-UP", "Mañana, día 11: entrada en calor"),
    ]
    cap = caption(10, "the WHO guidelines", "la guía de la OMS",
                  "How much physical activity does an adult need? The WHO 2020 guidelines recommend 150–300 minutes of moderate-intensity activity per week (or 75–150 minutes of vigorous activity, or an equivalent mix), plus muscle-strengthening activities involving all major muscle groups on at least 2 days per week. If you have a health condition, ask your doctor first.",
                  "¿Cuánta actividad física necesita un adulto? Las guías de la OMS 2020 recomiendan 150–300 minutos semanales de actividad moderada (o 75–150 minutos de actividad intensa, o una mezcla equivalente), más actividades de fortalecimiento muscular de todos los grandes grupos musculares al menos 2 días por semana. Si tienes una condición médica, consulta antes a tu médico.",
                  handle, "WHO guidelines on physical activity and sedentary behaviour, 2020")
    return {"id": 10, "day": 10, "q": 5, "topic": "who", "scenes": S, "caption": cap,
            "hashtags": "#physicalactivity #health #WHO #exercise #fitness",
            "source": "Source: WHO guidelines on physical activity, 2020"}


# ----------------------------------------------------------------------------- DIA 11
def reel_warmup(handle):
    S = [
        hook(11, "eleven", "once", "TEACHING YOU: WARM-UP", "Enseñándote: entrada en calor", ["DOES WARMING UP", "REALLY HELP?"],
             "warming up", "la entrada en calor",
             ("Is warming up worth your time?", ["Is warming up", "worth your time?"]),
             ("¿Vale la pena entrar en calor?", ["¿Vale la pena", "entrar en calor?"]), icon="bolt"),
        {"type": "stat", "tail": 0.7, "head": "WARM-UP EFFECT", "value": "79%", "vsize": 118, "count": (79, "{:.0f}%"), "ring": 0.79, "icon": "bolt", "anim": "jack",
         "label": ["of performance outcomes", "improved after warming up"],
         "lines": [L("A review of thirty-two studies looked at warming up before exercise.", "Una revisión de 32 estudios analizó la entrada en calor antes del ejercicio.",
                     ["A review of 32 studies looked", "at warming up before exercise."], ["Una revisión de 32 estudios analizó", "la entrada en calor antes de entrenar."]),
                   L("Warming up improved performance in seventy-nine percent of the outcomes measured.",
                     "Entrar en calor mejoró el rendimiento en el 79 % de los resultados medidos.",
                     ["Warming up improved performance", "in 79% of the outcomes measured."], ["Entrar en calor mejoró el rendimiento", "en el 79 % de los resultados medidos."]),
                   L("The authors also found little evidence that it harms athletes, but noted that few high-quality trials exist.",
                     "Los autores también hallaron poca evidencia de que perjudique, pero notaron que hay pocos ensayos de alta calidad.",
                     ["Little evidence it harms athletes,", "but few high-quality trials exist."], ["Poca evidencia de que perjudique,", "pero hay pocos ensayos de calidad."])]},
        {"type": "tips", "tail": 0.6, "head": "A PRACTICAL EXAMPLE", "icons": ["walk", "dumbbell", "flame"], "anim": "circles",
         "items": [("Start with easy, light movement", "Empieza con movimiento suave y ligero"),
                   ("Do a few light sets first", "Haz unas series livianas antes"),
                   ("Then go to your working sets", "Luego pasa a tus series de trabajo")],
         "lines": [L("Here is a practical example, not from the study. Start with easy, light movement.",
                     "Un ejemplo práctico, que no es del estudio. Empieza con movimiento suave y ligero.",
                     ["A practical example, not from the", "study: start with easy, light movement."], ["Un ejemplo práctico, que no es del", "estudio: empieza con movimiento suave."]),
                   L("Do a few light sets of your first exercise.", "Haz unas series livianas de tu primer ejercicio.",
                     ["Do a few light sets of", "your first exercise."], ["Haz unas series livianas de", "tu primer ejercicio."]),
                   L("Then move on to your working sets.", "Luego pasa a tus series de trabajo.",
                     ["Then move on to", "your working sets."], ["Luego pasa a", "tus series de trabajo."])]},
        cta(11, "twelve", "doce", "DAY 12 TOMORROW: ROUTINE", "Mañana, día 12: rutina para principiantes"),
    ]
    cap = caption(11, "warming up", "entrada en calor",
                  "Does warming up really help? A systematic review of 32 studies found that warming up improved performance in 79% of the outcomes measured, with little evidence that it harms athletes. The authors noted few high-quality trials exist. (The 3-step example in the video is a practical suggestion, not a finding of the study.)",
                  "¿La entrada en calor realmente ayuda? Una revisión sistemática de 32 estudios halló que entrar en calor mejoró el rendimiento en el 79 % de los resultados medidos, con poca evidencia de que perjudique. Los autores notaron que hay pocos ensayos de alta calidad. (El ejemplo de 3 pasos del video es una sugerencia práctica, no un hallazgo del estudio.)",
                  handle, "Fradkin, Zazryn & Smoliga, J Strength Cond Res, 2010")
    return {"id": 11, "day": 11, "q": 6, "topic": "warmup", "scenes": S, "caption": cap,
            "hashtags": "#warmup #gym #workout #fitness #training",
            "source": "Source: Fradkin et al., J Strength Cond Res, 2010"}


# ----------------------------------------------------------------------------- DIA 12
def reel_routine(handle):
    names = ["PROTEIN", "VOLUME", "CREATINE", "OVERLOAD", "SLEEP", "CALORIES", "MYTHS", "FREQUENCY", "REPS", "ACTIVITY", "WARM-UP", "ROUTINE"]
    S = [
        hook(12, "twelve", "doce", "TEACHING YOU: ROUTINE", "Enseñándote: rutina para principiantes", ["A SIMPLE ROUTINE", "FOR BEGINNERS"],
             "your first routine", "tu primera rutina",
             ("Let's put it all together.", ["Let's put", "it all together."]),
             ("Vamos a juntarlo todo.", ["Vamos a", "juntarlo todo."]), icon="list"),
        {"type": "stat", "tail": 0.7, "head": "DAYS PER WEEK · BEGINNERS", "value": "2–3", "vsize": 170, "ring": 0.36, "icon": "list", "anim": "jack",
         "label": ["ACSM recommendation", "for novice lifters"],
         "lines": [L("For beginners, the American College of Sports Medicine recommends training two to three days per week.",
                     "Para principiantes, el Colegio Americano de Medicina del Deporte recomienda entrenar de dos a tres días por semana.",
                     ["For beginners, the ACSM recommends", "training 2 to 3 days per week."], ["Para principiantes, el ACSM recomienda", "entrenar de 2 a 3 días por semana."]),
                   L("With loads around eight to twelve repetitions maximum.", "Con cargas de unas ocho a doce repeticiones máximas.",
                     ["With loads around 8 to 12", "repetitions maximum."], ["Con cargas de unas 8 a 12", "repeticiones máximas."])]},
        {"type": "tips", "tail": 0.6, "head": "ONE EXAMPLE SESSION", "icons": ["dumbbell", "list", "target"], "anim": "squat",
         "items": [("Big multi-joint lifts first", "Primero los ejercicios grandes y multiarticulares"),
                   ("Example: squat, press, row, 8–12 reps", "Ej.: sentadilla, press y remo, 8–12 reps"),
                   ("Small isolation work last", "Los ejercicios pequeños al final")],
         "lines": [L("The guideline orders big, multi-joint exercises before small, single-joint ones.", "La guía ordena los ejercicios grandes y multiarticulares antes de los pequeños.",
                     ["The guideline puts big multi-joint", "exercises before small ones."], ["La guía pone los ejercicios grandes", "multiarticulares antes de los pequeños."]),
                   L("For example, a squat, a press and a row, for eight to twelve reps.", "Por ejemplo, una sentadilla, un press y un remo, de ocho a doce repeticiones.",
                     ["For example: a squat, a press", "and a row, for 8 to 12 reps."], ["Por ejemplo: una sentadilla, un press", "y un remo, de 8 a 12 repeticiones."]),
                   L("Finish with small isolation work.", "Termina con ejercicios de aislamiento pequeños.",
                     ["Finish with small", "isolation work."], ["Termina con ejercicios", "de aislamiento pequeños."])]},
        {"type": "recap", "tail": 0.8, "head": "12 DAYS · 12 LESSONS", "items": [(i + 1, names[i]) for i in range(12)],
         "lines": [L("That's twelve days, twelve lessons.", "Son doce días, doce lecciones.", ["That's 12 days,", "12 lessons."], ["Son 12 días,", "12 lecciones."]),
                   L("Protein, volume, creatine, overload, sleep, calories, myths, frequency, reps, activity, warm-ups, and a routine.",
                     "Proteína, volumen, creatina, sobrecarga, sueño, calorías, mitos, frecuencia, repeticiones, actividad, entrada en calor y una rutina.",
                     ["Protein, volume, creatine, overload,", "sleep, calories, myths, frequency, reps,", "activity, warm-ups, and a routine."],
                     ["Proteína, volumen, creatina, sobrecarga,", "sueño, calorías, mitos, frecuencia,", "repeticiones, actividad, calentamiento y rutina."])]},
        {"type": "cta", "tail": 1.0, "next_en": "MORE LESSONS COMING", "next_es": "Vienen más lecciones",
         "lines": [L("Save the series, and share it with a friend who is starting out.", "Guarda la serie y compártela con un amigo que está empezando.",
                     ["Save the series, and share it", "with a friend who is starting out."], ["Guarda la serie y compártela con", "un amigo que está empezando."]),
                   L("Follow for more lessons.", "Sígueme para más lecciones.", ["Follow for", "more lessons."], ["Sígueme para", "más lecciones."])]},
    ]
    cap = (f"Day 12 teaching you: your first routine 💪\n"
           f"For beginners, the ACSM recommends training 2–3 days per week with loads around 8–12 RM, ordering large-muscle, multi-joint exercises before small, single-joint ones. The squat/press/row session in the video is an example, not a prescription. That's 12 days, 12 lessons: protein, volume, creatine, overload, sleep, calories, myths, frequency, reps, activity, warm-ups and a routine.\n\n"
           f"Día 12 enseñándote: tu primera rutina 💪\n"
           f"Para principiantes, el ACSM recomienda entrenar 2–3 días por semana con cargas de unas 8–12 RM, ordenando los ejercicios grandes y multiarticulares antes de los pequeños y de una sola articulación. La sesión de sentadilla/press/remo del video es un ejemplo, no una prescripción. Son 12 días, 12 lecciones: proteína, volumen, creatina, sobrecarga, sueño, calorías, mitos, frecuencia, repeticiones, actividad, entrada en calor y una rutina.\n\n"
           f"Save the series 📌 and follow {handle}. / Guarda la serie y sigue a {handle}.\n"
           f"Source / Fuente: ACSM position stand, Med Sci Sports Exerc, 2009.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return {"id": 12, "day": 12, "q": 7, "topic": "routine", "scenes": S, "caption": cap,
            "hashtags": "#beginnerworkout #gymbeginner #fullbodyworkout #fitness #strengthtraining",
            "source": "Source: ACSM position stand, Med Sci Sports Exerc, 2009"}


REELS_MORE = {6: reel_calories, 7: reel_myths, 8: reel_frequency, 9: reel_reps, 10: reel_who, 11: reel_warmup, 12: reel_routine}
