from nicegui import app, ui

fonts = '<link rel="preconnect" href="https://fonts.googleapis.com"> \
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> \
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@100..800&display=swap" rel="stylesheet">'

app.add_static_files('/assets', './assets')

@ui.page('/')
def homepage():
    ui.page_title('patchbay consulting')
    ui.add_head_html(fonts)
    ui.add_css('''
        .sora-400 {
            font-family: "Sora", sans-serif;
            font-optical-sizing: auto;
            font-weight: 400;
            font-style: normal;
        }
    ''')
    ui.add_css('''
    :root {
        --nicegui-default-padding: 0rem;
        --nicegui-default-gap: 0rem;
        }
    ''')
    ui.colors(primary='black', dark_page='black', brand='#f0DB40')
    ui.query('body').classes('sora-400 p-0 m-0 gap-0 no-wrap')
    ui.button().default_classes('text-xs md:text-base p-1 self-center mt-3 md:mt-2')
    ui.separator.default_props('color=brand').default_classes('mt-3')
    with ui.header().classes('mt-1'):
        with ui.grid(columns=16).classes('w-full gap-0 h-14 place-items-stretch'):
            with ui.link():
                ui.image('/assets/PB_logo.svg').classes('col-span-2 md:col-span-1 h-14').props('fit=scale-down')
            with ui.row().classes('col-span-11 md:col-span-7 lg:col-span-6 place-items-stretch items-center'):
                with ui.link(target='#what').props('align=left'):
                    ui.button('what')
                ui.space()
                with ui.link(target='#who').props('align=center'):
                    ui.button('who')
                ui.space()
                with ui.link(target='#contact').props('align=right'):
                    ui.button('contact')
            ui.space()
    with ui.grid(columns=16).classes('w-full gap-0'):
        ui.column().classes('col-span-2 md:col-span-1 p-0 m-0')
        with ui.column().classes('col-span-11 md:col-span-7 lg:col-span-6 p-0'):
            ui.html('patch <br /> bay <br />').classes('text-brand text-8xl md:text-9xl p-0 -ml-1 -mt-4')
            ui.label('Taking the Big out of Tech').classes('text-brand text-lg md:text-3xl mt-8')
            ui.separator()
            ui.link_target('what')
            ui.label('What we do').classes('text-brand text-base md:text-xl mt-6')
            ui.link_target('what')
            ui.html('We’ve spent decades working in big tech – from the federal government to fintech, education to e-commerce, gaming to Google. Now we’re bringing that experience to you. We help local businesses improve their processes through custom software development. We meet you where you are, work with your existing workflows and tooling, and make things work seamlessly together.')
            ui.separator()
            ui.link_target('who')
            ui.label('Who we are').classes('text-brand text-base md:text-xl mt-6')
            ui.link_target('who')
            with ui.link(target='mailto:todd@patchbayconsulting.com').classes('text-brand'):
                ui.label('Todd').classes('text-brand')
            ui.html('Todd has been a product designer since 1999 - when they used to just call everyone a "web designer". Since then, he has worked for the likes of Capital One, Honda, Converse, and Unity Technologies doing things like building design systems, creating user flows for internal bank platforms and publishing mobile games. The job titles may have changed - ranging from Art Director to UX Designer to Product Lead, but to him its all been the same: he helped build user-friendly things on the internet, mostly by drawing a lot of rectangles.')
            with ui.link(target='mailto:micah@patchbayconsulting.com').classes('text-brand mt-3'):
                ui.label('Micah').classes('text-brand')
            ui.html('Micah got their start in tech by testing truly terrible video games. That experience has deeply shaped their approach to software development – if we’re not going to build something good, why build anything? They deeply believe that software should be built based on user need, that code is a tool to deliver user value and has no inherent value in and of itself, and that software engineering pedagogy went wrong when it forgot its roots in philosophy. Needless to say, this doesn’t make Micah popular in some circles. After years writing software and leading engineering teams in big tech and the federal government, Micah is excited to eject from all of that and build tools for you.')
            ui.separator()
            ui.link_target('contact')
            ui.link('Get in touch', 'mailto:contact@patchbayconsulting.com').classes('text-brand text-xl md:text-2xl mt-6')
            ui.link_target('contact')
            ui.space().classes('h-16')

ui.run(dark=True, port=10000, favicon='🎛️')