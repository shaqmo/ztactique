import random
random.seed(7)
ids = iter(range(10, 2000))
def nid(): return f"1:{next(ids)}"

cols, rows = 10, 7
gaps  = [0,20,17,14,11,9,7,5,4,3]
durs  = [24,22,20,18,16,14,12,10,8,6]
S = 1.6
t0 = 0; starts=[]; acc=t0
for g in gaps:
    acc += g; starts.append(round(acc*S))
durs = [round(d*S) for d in durs]
ends = [s+d for s,d in zip(starts,durs)]
last_end = max(ends)

# wider size variation: small flecks up to larger dots
sizes = [3, 4, 5, 6.5, 8, 10, 13, 16]
colors = ["FF4D5D67","FF76ABAE","FF8EAAAC"]
css_colors = {"FF4D5D67":"#4D5D67","FF76ABAE":"#76ABAE","FF8EAAAC":"#8EAAAC"}
col_nodes = []
xml_cols = []
svg_dots = []  # for the static HTML fallback, so it matches this layout exactly
for i in range(cols):
    cid = nid(); col_nodes.append(cid)
    col_x = 40 + i * 46
    dots = []
    for j in range(rows):
        x = random.randint(-8,8)
        y = 60 + j*62 + random.randint(-18,18)
        r = random.choice(sizes)
        c = random.choice(colors)
        dots.append(f'''                <Shape x="{x}" y="{y}" name="Dot"><Ellipse width="{r*2}" height="{r*2}" originX="0.5" originY="0.5" name="P"/><Fill name="F"><SolidColor colorValue="{c}" name="C"/></Fill></Shape>''')
        svg_dots.append(f'<circle cx="{col_x+x}" cy="{y}" r="{r}" fill="{css_colors[c]}"/>')
    xml_cols.append(f'''        <Node x="{col_x}" y="0" name="Column {i+1}" id="{cid}">
{chr(10).join(dots)}
        </Node>''')

# Write the same dot layout as a static SVG, so the page can paint it
# immediately (no WASM/asset load wait) before Rive takes over.
svg_markup = '\n    '.join(svg_dots)
open("dots.svg.txt", "w").write(svg_markup)

z_trim = nid()
dot_node = nid()
anim_id = nid(); sm_id = nid(); layer_id = nid(); state_id = nid()
z_start = last_end + 6
z_end = z_start + 60

# accent dot pops in once the Z has finished drawing
dot_start = z_end - 6
dot_mid = dot_start + 14
dot_end = dot_start + 24
duration = dot_end + 30

ease = '<CubicEaseInterpolator x1="0.42" y1="0" x2="0.58" y2="1"/>'
keyed = []
for cid, s, e in zip(col_nodes, starts, ends):
    keyed.append(f'''            <KeyedObject objectId="{cid}"><KeyedProperty propertyKey="18">
                <KeyFrameDouble value="1" frame="{s}" interpolationType="linear"/>
                <KeyFrameDouble value="0" frame="{e}" interpolationType="linear"/>
            </KeyedProperty></KeyedObject>''')

# original Z size
z_top, z_bottom, z_left, z_right = 170, 330, 160, 340

dot_r = 13
exclaim_x = z_right + 36
dot_y = z_bottom

scene = f'''<Rive version="1" kind="fragment">
    <Artboard width="500" height="500" name="Hero Z" defaultStateMachineId="{sm_id}" id="1:1">

        <!-- The letter Z, drawn on after the dots have gone -->
        <Shape x="0" y="0" name="Z" id="{nid()}">
            <PointsPath isClosed="false" name="Path">
                <StraightVertex x="{z_left}" y="{z_top}"/>
                <StraightVertex x="{z_right}" y="{z_top}"/>
                <StraightVertex x="{z_left}" y="{z_bottom}"/>
                <StraightVertex x="{z_right}" y="{z_bottom}"/>
            </PointsPath>
            <Stroke thickness="24" cap="round" join="round" name="Stroke">
                <SolidColor colorValue="FF76ABAE" name="Color"/>
                <TrimPath start="0" end="0" name="Trim" id="{z_trim}"/>
            </Stroke>
        </Shape>

        <!-- Accent dot: pops in on the Z's baseline once it has drawn -->
        <Node x="{exclaim_x}" y="{dot_y}" name="Accent" id="{dot_node}" scaleX="0" scaleY="0">
            <Shape x="0" y="0" name="Dot"><Ellipse width="{dot_r*2}" height="{dot_r*2}" originX="0.5" originY="0.5" name="P"/><Fill name="F"><SolidColor colorValue="FFFF5722" name="C"/></Fill></Shape>
        </Node>

{chr(10).join(xml_cols)}

        <StateMachine name="State Machine 1" id="{sm_id}">
            <StateMachineLayer name="Layer 1" id="{layer_id}">
                <AnyState x="80" y="-40"/>
                <ExitState x="240" y="-40"/>
                <EntryState><StateTransition stateToId="{state_id}"/></EntryState>
                <AnimationState x="80" y="40" animationId="{anim_id}" id="{state_id}"/>
            </StateMachineLayer>
        </StateMachine>

        <LinearAnimation loopValue="oneShot" duration="{duration}" name="Reveal" id="{anim_id}">
{chr(10).join(keyed)}
            <KeyedObject objectId="{z_trim}"><KeyedProperty propertyKey="115">
                <KeyFrameDouble value="0" frame="{z_start}" interpolationType="cubic">{ease}</KeyFrameDouble>
                <KeyFrameDouble value="1" frame="{z_end}" interpolationType="linear"/>
            </KeyedProperty></KeyedObject>
            <KeyedObject objectId="{dot_node}">
                <KeyedProperty propertyKey="16">
                    <KeyFrameDouble value="0" frame="{dot_start}" interpolationType="cubic">{ease}</KeyFrameDouble>
                    <KeyFrameDouble value="1.3" frame="{dot_mid}" interpolationType="cubic">{ease}</KeyFrameDouble>
                    <KeyFrameDouble value="1" frame="{dot_end}" interpolationType="linear"/>
                </KeyedProperty>
                <KeyedProperty propertyKey="17">
                    <KeyFrameDouble value="0" frame="{dot_start}" interpolationType="cubic">{ease}</KeyFrameDouble>
                    <KeyFrameDouble value="1.3" frame="{dot_mid}" interpolationType="cubic">{ease}</KeyFrameDouble>
                    <KeyFrameDouble value="1" frame="{dot_end}" interpolationType="linear"/>
                </KeyedProperty>
            </KeyedObject>
        </LinearAnimation>

    </Artboard>
</Rive>
'''
open("scene.rml","w").write(scene)
print("duration", duration, "dots gone at", last_end, "z", z_start, z_end, "dot", dot_start, dot_end)
