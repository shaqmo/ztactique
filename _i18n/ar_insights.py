# -*- coding: utf-8 -*-
# Arabic translations: insights index and the three articles.
STR = {
    # ---- insights index ----
    "Insights: ZTactique": "رؤى: ZTactique",
    "Practical notes on IT strategy, cloud infrastructure, and software delivery from ZTactique, without gated whitepapers and without filler.":
        "ملاحظات عملية من ZTactique حول استراتيجية تقنية المعلومات والبنية السحابية وتسليم البرمجيات، دون أوراق بيضاء مقيّدة ودون حشو.",
    "Articles and case studies": "مقالات ودراسات حالة",
    "Have a Challenge That Isn't Covered Here?": "هل لديك تحدٍّ لم نتناوله هنا؟",
    "These are a few of the situations we see most. Yours is probably one we've handled before, too.":
        "هذه بعض الحالات التي نراها أكثر من غيرها. وغالبًا تعاملنا مع حالتك من قبل أيضًا.",
    "Fan data, member portals, and digital strategy for rights holders, federations, leagues, and clubs.":
        "بيانات المشجعين وبوابات الأعضاء والاستراتيجية الرقمية لأصحاب الحقوق والاتحادات والدوريات والأندية.",

    # ---- case study: football site ----
    "How We Built a Sports League Website 70x Faster: ZTactique": "كيف بنينا موقع دوري رياضي أسرع بـ 70 مرة: ZTactique",
    "A public, verifiable case study: how a lean two-service architecture and disciplined engineering practice beat a heavily-resourced official website on speed, reliability, and user experience.":
        "دراسة حالة علنية يمكن التحقق منها: كيف تفوّقت بنية رشيقة من خدمتين وممارسة هندسية منضبطة على موقع رسمي كثير الموارد في السرعة والموثوقية وتجربة المستخدم.",
    "Most case studies ask you to take our word for it. This one you can check yourself: the result is a live, public website, not a confidential engagement. <a href=\"https://fdl.saudiafootball.com\" rel=\"noopener\" target=\"_blank\">See it live →</a>":
        "تطلب منك معظم دراسات الحالة أن تصدّق كلامنا. أما هذه فيمكنك التحقق منها بنفسك: النتيجة موقع حيّ مفتوح للجميع، لا مشروعًا سريًّا. <a href=\"https://fdl.saudiafootball.com\" rel=\"noopener\" target=\"_blank\">شاهده مباشرة ←</a>",
    "The official website for the Saudi First Division (Yelo League) was slow, and it offered fans little beyond basic scores. There was no kickoff countdown, no useful player detail, and long waits for pages to load. We took it as an exercise: use the same publicly available data to build a faster, more complete alternative, and prove out an approach we use with clients, namely lean infrastructure, disciplined engineering, and every claim backed by evidence.":
        "كان الموقع الرسمي لدوري الدرجة الأولى السعودي (دوري يلو) بطيئًا، ولم يقدّم للجماهير سوى النتائج الأساسية. لا عدّاد تنازلي لانطلاق المباراة، ولا تفاصيل مفيدة عن اللاعبين، وانتظار طويل لتحميل الصفحات. اعتبرنا ذلك تمرينًا: نستخدم البيانات المتاحة للعموم نفسها لنبني بديلًا أسرع وأشمل، ونختبر النهج الذي نتبعه مع عملائنا، وهو بنية تحتية رشيقة وهندسة منضبطة وكل ادعاء مدعوم بالأدلة.",
    "The Problem Was Not a Lack of Infrastructure": "لم تكن المشكلة نقصًا في البنية التحتية",
    "A closer look at the official site explained why being \"in the cloud\" had not solved its speed problem. It was running through three separate content delivery networks stacked on top of each other, plus a bot-verification check and video widgets loading on pages that did not need them.":
        "أوضح فحص أدق للموقع الرسمي لماذا لم يحلّ وجوده «في السحابة» مشكلة بطئه. فقد كان يمرّ عبر ثلاث شبكات لتوصيل المحتوى مكدّسة فوق بعضها، إضافةً إلى فحص للتحقق من الروبوتات وعناصر فيديو تُحمَّل في صفحات لا تحتاج إليها.",
    "More infrastructure was not making it faster. It was slowing it down. This is a pattern we see often: teams add tools to fix a performance problem, and the tooling itself becomes the bottleneck.":
        "لم تكن زيادة البنية التحتية تجعله أسرع، بل كانت تبطّئه. وهذا نمط نراه كثيرًا: تضيف الفرق أدوات لحل مشكلة في الأداء، فتتحول الأدوات نفسها إلى عنق الزجاجة.",
    "Building Lean, on Purpose": "البناء بأقل قدر ممكن عن قصد",
    "Rather than layering on more infrastructure, we built the new site lean from the start: one small service to serve the pages, one to fetch and prepare the data, and a simple operating rule, which is to always show visitors something instantly and then quietly refresh it in the background. Standings, fixtures, and player data get a fast local copy that is always ready to serve, even if the original source is briefly unavailable.":
        "بدلًا من تكديس مزيد من البنية التحتية، بنينا الموقع الجديد رشيقًا منذ البداية: خدمة صغيرة واحدة لتقديم الصفحات، وأخرى لجلب البيانات وتجهيزها، وقاعدة تشغيل بسيطة هي أن نُظهر للزائر شيئًا فورًا ثم نحدّثه بهدوء في الخلفية. تحصل بيانات الترتيب والمباريات واللاعبين على نسخة محلية سريعة جاهزة دائمًا، حتى لو تعذّر المصدر الأصلي لوقت قصير.",
    "The result launched fully bilingual, in Arabic and English, from day one, something the official site still does not offer.":
        "وقد انطلقت النتيجة ثنائية اللغة بالكامل، بالعربية والإنجليزية، منذ اليوم الأول، وهو ما لا يزال الموقع الرسمي لا يقدّمه.",
    "What We Caught Before It Became a Problem": "ما اكتشفناه قبل أن يصبح مشكلة",
    "Building something reliable is not only about writing code that happens to work. It is about catching what breaks under real usage, and confirming every fix with evidence instead of assuming it worked. A few examples from this build:":
        "بناء شيء موثوق لا يقتصر على كتابة شيفرة تعمل بالصدفة، بل هو اكتشاف ما ينكسر تحت الاستخدام الحقيقي، وتأكيد كل إصلاح بالأدلة بدل افتراض أنه نجح. وهذه أمثلة من هذا المشروع:",
    "<strong>A 7-second load time, fixed.</strong> News articles were taking nearly 7 seconds to appear, diagnosed with real browser data rather than guesswork. Rebuilt so visitors see content immediately while a fresh copy loads behind the scenes, measured before and after at under a tenth of a second.":
        "<strong>إصلاح زمن تحميل بلغ 7 ثوانٍ.</strong> كانت المقالات الإخبارية تستغرق نحو 7 ثوانٍ لتظهر، وشخّصنا ذلك ببيانات متصفح حقيقية لا بالتخمين. أعدنا البناء ليرى الزوار المحتوى فورًا بينما تُحمَّل نسخة حديثة في الخلفية، وقسنا النتيجة قبل التغيير وبعده فإذا هي أقل من عُشر ثانية.",
    "<strong>A silent data-loss risk, closed.</strong> When an external data source briefly rate-limited requests as traffic grew, we found and fixed a related gap where a failed refresh could have overwritten good data with nothing. The fix was simple: never let an empty result replace a good one.":
        "<strong>سدّ خطر صامت لفقدان البيانات.</strong> حين قيّد مصدر بيانات خارجي الطلبات مؤقتًا مع تزايد الزيارات، اكتشفنا وأصلحنا ثغرة مرتبطة بذلك كان يمكن فيها لتحديث فاشل أن يستبدل بيانات سليمة بلا شيء. وكان الحل بسيطًا: ألّا نسمح أبدًا لنتيجة فارغة بأن تحلّ محل نتيجة سليمة.",
    "<strong>A launch-breaking bug, caught in review.</strong> A subtle error in the light and dark mode switch, of the kind that would have broken every single page view, was found through code review before launch, not by waiting for a visitor to report it.":
        "<strong>خطأ كان سيعطّل الإطلاق، اكتُشف في المراجعة.</strong> خطأ دقيق في مفتاح الوضع الفاتح والداكن، من النوع الذي كان سيعطّل كل زيارة للصفحة، اكتُشف عبر مراجعة الشيفرة قبل الإطلاق، لا بانتظار أن يبلّغ عنه زائر.",
    "<strong>A privacy gap, closed proactively.</strong> A routine check turned up a default web address quietly exposing a fragment of the account owner's email. It was disabled immediately, with everything depending on it safely re-pointed first.":
        "<strong>سدّ ثغرة خصوصية بشكل استباقي.</strong> كشف فحص روتيني عن عنوان ويب افتراضي يكشف بصمت جزءًا من بريد صاحب الحساب الإلكتروني. عطّلناه فورًا، بعد أن وجّهنا كل ما يعتمد عليه إلى مكان آمن.",
    "Do you recognize any of these patterns in your own systems?": "هل تلاحظ أيًّا من هذه الأنماط في أنظمتك؟",
    "Slow load times, infrastructure sprawl, and untested failure paths are usually fixable without a rebuild. Let us talk about what is actually happening under the hood.":
        "غالبًا ما يمكن إصلاح بطء التحميل وتضخّم البنية التحتية ومسارات الفشل غير المختبرة دون إعادة بناء. لنتحدث عمّا يجري فعلًا تحت الغطاء.",
    "The Results, Measured": "النتائج مقيسة",
    "The site is live, public, and tracked with real analytics, not only visit counts but what people actually do: switching languages, browsing photos, reading articles, and how long they stay.":
        "الموقع حيّ ومتاح للجميع ويُتابَع بتحليلات حقيقية، لا بأعداد الزيارات فقط بل بما يفعله الناس فعلًا: تبديل اللغة وتصفّح الصور وقراءة المقالات ومدة بقائهم.",
    "<strong>70x</strong> faster news loading than the pattern it replaced":
        "<strong>70×</strong> أسرع في تحميل الأخبار من النمط الذي حلّ محلّه",
    "<strong>Bilingual</strong> in Arabic and English from day one":
        "<strong>ثنائي اللغة</strong> بالعربية والإنجليزية منذ اليوم الأول",
    "The Takeaway": "الخلاصة",
    "<strong>More technology is not the same as better technology.</strong> The official site runs more infrastructure than this one and is still slower. The speed came from fewer, better decisions, not from spending more.":
        "<strong>مزيد من التقنية لا يعني تقنية أفضل.</strong> يعمل الموقع الرسمي على بنية تحتية أكبر من هذا الموقع ومع ذلك يظل أبطأ. جاءت السرعة من قرارات أقل وأفضل، لا من إنفاق أكثر.",
    "<strong>Never assume a fix worked. Confirm it.</strong> Every improvement here was measured with real evidence before being called done: real visitor data, real before-and-after timing. That is the same discipline we bring to client engagements.":
        "<strong>لا تفترض أبدًا أن الإصلاح نجح، بل تأكّد منه.</strong> قِيس كل تحسين هنا بأدلة حقيقية قبل اعتباره منجزًا: بيانات زوار حقيقية وأزمنة حقيقية قبل التغيير وبعده. وهذا هو الانضباط نفسه الذي نطبّقه في مشاريع عملائنا.",
    "<strong>Protect against the failure you did not expect.</strong> Good systems do not only handle the happy path. They fail safely when something goes wrong, instead of quietly making it worse.":
        "<strong>احمِ نفسك من الفشل الذي لم تتوقعه.</strong> الأنظمة الجيدة لا تتعامل مع المسار السعيد وحده، بل تفشل بأمان حين يحدث خطأ، بدل أن تزيد الأمر سوءًا بصمت.",
    "Want This Kind of Discipline Applied to Your Product?": "هل تريد هذا المستوى من الانضباط في منتجك؟",
    "Whether it is a slow site, a fragile system, or a build that has outgrown its own infrastructure, we approach it the same way: lean first, evidence always.":
        "سواء كان موقعًا بطيئًا أو نظامًا هشًّا أو منتجًا تجاوز بنيته التحتية، نتعامل معه بالأسلوب نفسه: البساطة أولًا والأدلة دائمًا.",

    # ---- article: migration vendor ----
    "The Real Cost When a Migration Vendor Disappears: ZTactique": "التكلفة الحقيقية عندما يختفي مورّد الترحيل: ZTactique",
    "What actually breaks when a migration partner disappears mid-project, and the three checkpoints that catch it early.":
        "ما الذي ينكسر فعلًا حين يختفي شريك الترحيل في منتصف المشروع، ونقاط التحقق الثلاث التي تكشف ذلك مبكرًا.",
    "The pattern is almost always the same. A migration begins with a confident timeline, a signed statement of work, and a vendor who answers emails within the hour. Six weeks in, the responses slow down. Then a project lead \"transitions to a new role.\" Then all communication stops entirely, usually right after the hardest and riskiest phase of the cutover has started but before it is finished.":
        "النمط يتكرر تقريبًا دائمًا. يبدأ الترحيل بجدول زمني واثق وبيان عمل موقّع ومورّد يردّ على الرسائل خلال ساعة. وبعد ستة أسابيع تتباطأ الردود. ثم «ينتقل قائد المشروع إلى دور جديد». ثم ينقطع التواصل تمامًا، وغالبًا بعد بدء أصعب مراحل التحويل وأكثرها خطورة وقبل انتهائها.",
    "What is left behind is not simply an unfinished project. It is a specific, predictable set of problems that grow worse the longer they go unaddressed.":
        "ما يتركه ذلك ليس مجرد مشروع غير مكتمل، بل مجموعة محددة يمكن توقّعها من المشكلات، تزداد سوءًا كلما طال إهمالها.",
    "What Actually Breaks": "ما الذي ينكسر فعلًا",
    "In the engagements where we have been brought in to clean up after a vendor disappeared, the damage almost never looks like \"nothing happened.\" It tends to look like this:":
        "في المشاريع التي استُدعينا فيها لإصلاح ما خلّفه مورّد اختفى، لا يبدو الضرر أبدًا تقريبًا كأن «لا شيء حدث». بل يبدو عادةً على هذا النحو:",
    "<strong>Half-migrated data.</strong> Some tables, buckets, or services have moved, others have not, and nobody has a clear list of which is which.":
        "<strong>بيانات رُحّل نصفها.</strong> انتقلت بعض الجداول أو الحاويات أو الخدمات ولم تنتقل أخرى، ولا يملك أحد قائمة واضحة بما نُقل وما لم يُنقل.",
    "<strong>Two production environments running at once</strong>, quietly drifting out of sync, each one treated as the source of truth by a different team.":
        "<strong>بيئتا إنتاج تعملان في وقت واحد</strong>، وتنحرفان عن التزامن بصمت، وكل فريق يعدّ إحداهما مصدر الحقيقة.",
    "<strong>No documentation of decisions made mid-project</strong>, so nobody can explain why a particular service was split a certain way or what workaround was applied and where.":
        "<strong>لا توثيق للقرارات المتخذة أثناء المشروع</strong>، فلا أحد يستطيع تفسير لماذا قُسّمت خدمة معينة بطريقة معينة أو أي حل التفافي طُبّق وأين.",
    "<strong>Eroded internal trust in the roadmap</strong>, which is often the most expensive cost and the hardest to repair. Once a leadership team has been let down once, every future technology recommendation is treated with suspicion.":
        "<strong>تآكل الثقة الداخلية بخارطة الطريق</strong>، وهو غالبًا أغلى الكلفة وأصعبها إصلاحًا. فما إن تخذل فريقَ القيادة مرة واحدة حتى تُقابَل كل توصية تقنية مستقبلية بالشك.",
    "Three Checkpoints That Would Have Caught It Early": "ثلاث نقاط تحقق كانت ستكشف المشكلة مبكرًا",
    "None of this requires exotic tooling to prevent. It requires a structure that most engagements skip because it feels like overhead at the start, when everyone is still optimistic.":
        "لا يتطلب منع أيٍّ من هذا أدوات غريبة. بل يتطلب هيكلًا تتخطاه معظم المشاريع لأنه يبدو عبئًا في البداية، حين يكون الجميع متفائلين.",
    "<strong>A written rollback plan for every phase</strong>, not only for the migration as a whole. If a vendor cannot explain how phase two gets safely undone, that is a signal worth noting before phase two even starts.":
        "<strong>خطة تراجع مكتوبة لكل مرحلة</strong>، لا للترحيل ككل فقط. فإن عجز المورّد عن شرح كيفية التراجع الآمن عن المرحلة الثانية، فهذه إشارة تستحق الانتباه قبل أن تبدأ المرحلة الثانية أصلًا.",
    "<strong>Weekly written status, not verbal.</strong> A short email summarizing what moved, what is blocked, and what comes next creates a paper trail and forces a clarity that a status call often allows to slip.":
        "<strong>تقرير حالة أسبوعي مكتوب لا شفهي.</strong> رسالة قصيرة تلخّص ما تحرّك وما تعطّل وما هو قادم تصنع أثرًا مكتوبًا وتفرض وضوحًا كثيرًا ما تفوّته مكالمة الحالة.",
    "<strong>A named technical owner on your side</strong> who understands the architecture well enough to take over without the original vendor, even if you never expect to need it. If nobody internally could pick up the project tomorrow, that is the real risk, not the vendor's intentions.":
        "<strong>مسؤول تقني معيَّن بالاسم من جانبك</strong> يفهم البنية جيدًا بما يكفي لتولّي المشروع من دون المورّد الأصلي، حتى لو لم تتوقع أن تحتاج إلى ذلك. فإذا لم يستطع أحد داخل المؤسسة تسلّم المشروع غدًا، فهذا هو الخطر الحقيقي، لا نوايا المورّد.",
    "If You Are Already Here": "إن كنت في هذا الموقف بالفعل",
    "If a migration has already stalled, the fastest path back is usually a short, scoped audit: what has actually moved, what remains on the old system, and what the safest sequence is to finish without introducing new risk. Resist the urge to simply \"push through\" without that audit. Finishing a half-documented migration blind is how a difficult situation becomes a production incident.":
        "إذا تعثّر الترحيل بالفعل، فأسرع طريق للعودة هو غالبًا تدقيق قصير محدد النطاق: ما الذي انتقل فعلًا، وما الذي بقي في النظام القديم، وما أأمن تسلسل للإنهاء دون إدخال مخاطر جديدة. قاوم الرغبة في «المضيّ قدمًا» دون هذا التدقيق. فإنهاء ترحيل شبه غير موثّق بشكل أعمى هو ما يحوّل موقفًا صعبًا إلى حادثة في بيئة الإنتاج.",
    "Mid-migration, and the vendor has gone quiet?": "في منتصف الترحيل وقد انقطع تواصل المورّد؟",
    "We can carry out a fast audit of where things actually stand before you decide on the next step.":
        "يمكننا إجراء تدقيق سريع لمعرفة أين تقف الأمور فعلًا قبل أن تقرّر الخطوة التالية.",

    # ---- article: fractional CTO ----
    "5 Signs You Need a Fractional CTO, Not Another Developer: ZTactique": "5 علامات تدلّ على حاجتك إلى مدير تقني بدوام جزئي: ZTactique",
    "When a technology problem appears, the reflex is usually the same: hire another developer. Sometimes that is the right call. Often it is not, because the bottleneck is rarely a lack of hands writing code. More often, the real issue is that nobody is making the decisions about what should be built, in what order, and why.":
        "حين تظهر مشكلة تقنية، يكون رد الفعل المعتاد واحدًا: توظيف مطوّر آخر. أحيانًا يكون هذا هو القرار الصحيح، وغالبًا لا يكون، لأن عنق الزجاجة نادرًا ما يكون نقصًا في من يكتبون الشيفرة. والأرجح أن المشكلة الحقيقية أن لا أحد يتخذ القرارات بشأن ما يجب بناؤه وبأي ترتيب ولماذا.",
    "Here are five signals that what is missing is decision-making leadership, not headcount.":
        "إليك خمس إشارات تدلّ على أن الناقص هو قيادة تتخذ القرار، لا عدد الموظفين.",
    "1. Every Technical Decision Is Made by Whoever Is in the Room": "1. كل قرار تقني يتخذه من يحضر الغرفة",
    "If your architecture, tooling, and vendor choices reflect whoever happened to argue most convincingly at the time, rather than a deliberate strategy, adding another engineer only adds one more voice to that same unstructured process.":
        "إذا كانت خيارات هندستك وأدواتك ومورّديك تعكس من كان أقنع في الجدال وقتها لا استراتيجية مدروسة، فإن إضافة مهندس آخر لا تضيف سوى صوت آخر إلى العملية غير المنظَّمة نفسها.",
    "2. Your Roadmap Changes Direction Every Quarter": "2. خارطة طريقك تغيّر اتجاهها كل ربع سنة",
    "Some course-correction is healthy. Constant re-platforming, tool-swapping, or \"let us redo this in a different framework\" usually means there was never a technical strategy tying decisions to business goals. What looks like agility is often just a series of reasonable-sounding ideas with no thread connecting them.":
        "بعض تصحيح المسار صحّي. أما إعادة بناء المنصة باستمرار أو تبديل الأدوات أو «لنعد بناء هذا بإطار عمل مختلف» فيعني عادةً أنه لم تكن هناك يومًا استراتيجية تقنية تربط القرارات بأهداف العمل. وما يبدو رشاقة هو غالبًا سلسلة أفكار تبدو معقولة دون خيط يربط بينها.",
    "3. Developers Are Building the Wrong Things Well": "3. المطوّرون يبنون الأشياء الخطأ بإتقان",
    "Good execution on the wrong priorities is one of the most expensive failure modes in software, because it looks like productivity from the outside. If your team ships consistently but the business impact does not follow, the gap is usually prioritization, not skill.":
        "التنفيذ الجيد للأولويات الخاطئة من أغلى أنماط الفشل في البرمجيات، لأنه يبدو من الخارج إنتاجية. فإذا كان فريقك يسلّم باستمرار دون أن يظهر الأثر في العمل، فالفجوة غالبًا في ترتيب الأولويات لا في المهارة.",
    "4. Nobody Can Explain the Stack to the Board": "4. لا أحد يستطيع شرح المنظومة التقنية لمجلس الإدارة",
    "If technology decisions cannot be translated into business terms, such as cost, risk, timeline, and competitive position, leadership ends up approving budgets on faith. That is a communication and strategy gap, not something a new hire's code will fix.":
        "إذا تعذّرت ترجمة القرارات التقنية إلى مصطلحات العمل، كالتكلفة والمخاطر والجدول الزمني والموقع التنافسي، فإن القيادة تعتمد الميزانيات بحسن الظن. وهذه فجوة في التواصل والاستراتيجية، لا شيء يصلحه ما يكتبه موظف جديد.",
    "5. Vendor and Tooling Decisions Keep Getting Revisited": "5. تُعاد باستمرار مراجعة قرارات الموردين والأدوات",
    "Repeatedly asking \"should we really be on this platform?\" months after adopting it is usually a sign that the original decision was not made against clear criteria. That is a leadership function, not an engineering one.":
        "طرح السؤال «هل يجب فعلًا أن نبقى على هذه المنصة؟» مرارًا بعد أشهر من اعتمادها علامة على أن القرار الأصلي لم يُتخذ وفق معايير واضحة. وهذه وظيفة قيادية لا هندسية.",
    "What a Fractional CTO Actually Changes": "ماذا يغيّر المدير التقني بدوام جزئي فعلًا",
    "A fractional CTO does not replace your development team. Their role is to give it direction: a defined roadmap, a consistent decision-making framework, and someone accountable for translating business goals into technical priorities, without the cost or timeline of a full-time executive hire.":
        "لا يحلّ المدير التقني بدوام جزئي محل فريق التطوير لديك. دوره أن يمنحه اتجاهًا: خارطة طريق محددة وإطارًا ثابتًا لاتخاذ القرار وشخصًا مسؤولًا عن ترجمة أهداف العمل إلى أولويات تقنية، دون تكلفة توظيف مدير تنفيذي بدوام كامل ولا مدة ذلك.",
    "Not sure if this is your gap?": "لست متأكدًا إن كانت هذه فجوتك؟",
    "A 30-minute call is usually enough to tell whether the issue is headcount or direction.":
        "تكفي غالبًا مكالمة مدتها 30 دقيقة لمعرفة إن كانت المشكلة في عدد الموظفين أم في الاتجاه.",

    # ---- cross-link sentence used on the cloud page ----
    "See how we approach infrastructure problems in <a href=\"/insights/fdl-performance-case-study.html\" style=\"color:#76ABAE;\">our sports-site performance case study</a>, then let's talk about yours.":
        "اطّلع على كيفية تعاملنا مع مشكلات البنية التحتية في <a href=\"/insights/fdl-performance-case-study.html\" style=\"color:#76ABAE;\">دراسة حالة أداء موقعنا الرياضي</a>، ثم لنتحدث عن حالتك.",
}
