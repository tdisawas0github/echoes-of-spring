# ============================================================================
# options.rpy — Game Configuration
# ============================================================================

# Basic game metadata
define config.name = _("Echoes of Spring")
define config.version = "1.0"

define gui.show_name = True

# The about screen text.
define gui.about = _p("""
{b}Echoes of Spring{/b}

A romance / slice-of-life visual novel set in the sleepy town of Hanamachi.

Meet Sakura — a spirited barista-painter — and Akira — a reflective bookshop owner.
Your choices shape the story across four chapters and seven possible endings.

Made with Ren'Py.
""")

# Build configuration
define build.name = "EchoesOfSpring"

init python:
    # Classify files for distribution builds
    build.classify('**~',          None)
    build.classify('**.bak',       None)
    build.classify('**/.**',       None)
    build.classify('**/#**',       None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.rpy',  None)

    build.documentation('*.html')
    build.documentation('*.txt')
