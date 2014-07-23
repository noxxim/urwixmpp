#!/usr/bin/python

import sys
import urwid

def handle_input(input):
    if input == "esc":
        sys.exit(0)

    pass

# Just some Content for testing
t0 = urwid.Divider()
t1 = urwid.AttrWrap(urwid.Text("Hello World"), "p1")
t2 = urwid.Divider("+")
t3 = urwid.AttrWrap(urwid.Text('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas porta porta nunc eget dignissim. Morbi ante nibh, varius vitae rhoncus id, fermentum in nisl. Curabitur metus diam, pharetra vel varius non, vulputate eget lectus. Sed et nisl sed nisi sollicitudin egestas. Curabitur in ligula elit. Duis tristique porttitor porttitor. Cras rutrum lectus quis sem rutrum vulputate suscipit orci bibendum. Nam consectetur turpis purus, at suscipit tellus. Aenean diam lorem, tristique vel consequat in, rhoncus ac felis. Nam scelerisque justo nunc.

Suspendisse ut dolor vehicula felis gravida egestas. Nullam porttitor pulvinar mauris id tempor. Ut eu risus eu tellus laoreet pulvinar vitae ac nisl. Fusce bibendum consequat mauris, a lacinia turpis hendrerit eu. Nunc a arcu eget ante cursus dignissim vestibulum in magna. Nunc tempor accumsan augue eget cursus. Nullam interdum arcu eget metus placerat tempus. Morbi id lacus et diam tempus auctor. Morbi vehicula mi id mauris faucibus vitae pharetra purus rhoncus. Aliquam erat volutpat. Vestibulum nisi dolor, tincidunt quis interdum vitae, mattis quis nunc. Maecenas velit tortor, luctus non aliquet vel, euismod non arcu. Nunc ante lorem, bibendum eget pretium id, accumsan id odio. Aliquam odio lectus, porttitor dignissim egestas eget, vestibulum ut sapien. Pellentesque neque dolor, ultrices vel eleifend in, tincidunt vel libero.

Aliquam pulvinar est sit amet ligula viverra eleifend. Nullam porttitor sem sit amet massa egestas at ultricies lorem vestibulum. Donec eu libero dui. Sed in fringilla arcu. Nunc porta tincidunt lorem, eu dignissim lorem tempus ut. Integer faucibus magna non libero varius elementum blandit dolor lobortis. Maecenas a pharetra neque. Sed massa augue, placerat a varius eget, lobortis in nunc. Praesent non leo neque, non imperdiet felis. Aenean sed orci quis justo rutrum ornare vel nec erat. Vestibulum posuere elementum justo, in cursus neque varius a. In vel blandit nunc. Mauris blandit ligula eget felis lacinia at faucibus sem adipiscing. Sed malesuada lorem eget neque ornare eget condimentum nunc scelerisque.'''), "p1")
t4 = urwid.Divider("-")
t5 = urwid.AttrWrap(urwid.Text("Hello Arch!"), "p1")
t6 = urwid.Divider("8")

header = urwid.AttrWrap(urwid.Text("Dies ist der Header!"), "p2")
footer = urwid.AttrWrap(urwid.Text("Und hier ist der Footer!"), "p2")

content = [t0, t1, t2, t3, t4, t5, t6]

content = urwid.ListBox(urwid.SimpleListWalker(content))

palette = [('p1', 'light green', 'black'),
           ('p2', 'white', 'dark red')]


main_frame = urwid.Frame(content)

main_frame.set_header(header)
main_frame.set_footer(footer)

loop = urwid.MainLoop(main_frame, palette, unhandled_input=handle_input)
loop.run()


