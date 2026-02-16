# ============================================================================
# gui.rpy — GUI Customisation for Echoes of Spring
# ============================================================================

# ---- Resolution ----------------------------------------------------------
define gui.text_size          = 22
define gui.name_text_size     = 30
define gui.title_text_size    = 50
define gui.label_text_size    = 30
define gui.notify_text_size   = 16
define gui.interface_text_size = 22
define gui.button_text_size   = 22

# ---- Colours (soft pastel palette to match the spring theme) -------------
define gui.accent_color               = '#ff99cc'     # Cherry-blossom pink
define gui.idle_color                 = '#aaaaaa'
define gui.idle_small_color           = '#999999'
define gui.hover_color                = '#ffccdd'
define gui.selected_color             = '#ffffff'
define gui.insensitive_color          = '#55555580'
define gui.muted_color                = '#6b4e71'
define gui.hover_muted_color          = '#9b6ea5'

define gui.text_color                 = '#ffffff'
define gui.interface_text_color       = '#ffffff'
define gui.choice_button_text_idle_color    = '#cccccc'
define gui.choice_button_text_hover_color   = '#ffffff'

# ---- Dialogue window -----------------------------------------------------
define gui.textbox_height       = 185
define gui.textbox_yalign       = 1.0

define gui.name_xpos            = 240
define gui.name_ypos            = 0
define gui.name_xalign          = 0.0

define gui.dialogue_xpos        = 268
define gui.dialogue_ypos        = 50
define gui.dialogue_width       = 744
define gui.dialogue_text_xalign = 0.0

# ---- Buttons --------------------------------------------------------------
define gui.button_width     = None
define gui.button_height    = None
define gui.button_borders   = Borders(25, 5, 25, 5)
define gui.button_tile      = False

define gui.choice_button_width   = 740
define gui.choice_button_height  = None
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_tile    = False

# ---- Navigation buttons ---------------------------------------------------
define gui.navigation_xpos          = 40
define gui.navigation_ypos          = 0.4
define gui.navigation_spacing       = 4
define gui.navigation_button_width  = 225

# ---- Slots (save / load) -------------------------------------------------
define gui.slot_button_width   = 276
define gui.slot_button_height  = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_idle_color = gui.idle_small_color

define config.thumbnail_width  = 256
define config.thumbnail_height = 144

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

# ---- Scrollbars -----------------------------------------------------------
define gui.scrollbar_size      = 12
define gui.slider_size         = 30
define gui.slider_tile         = False

# ---- History screen -------------------------------------------------------
define config.history_length = 250
define gui.history_height    = 140
define gui.history_spacing   = 0
define gui.history_name_xpos  = 150
define gui.history_name_ypos  = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 1.0
define gui.history_text_xpos   = 170
define gui.history_text_ypos   = 2
define gui.history_text_width  = 740
define gui.history_text_xalign = 0.0

# ---- Skip indicator -------------------------------------------------------
define gui.skip_ypos = 10

# ---- Misc -----------------------------------------------------------------
define gui.unscrollable  = "hide"
define gui.nvl_borders   = Borders(0, 10, 0, 20)
define gui.nvl_height    = 115
define gui.nvl_spacing   = 10
