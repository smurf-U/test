from odoo import api, fields, models, tools, _


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    menu_sequence_ids = fields.One2many('menu.sequence', 'menu_id',
                                        string="User Menu Sequence")

    # @api.model
    # @tools.ormcache_context('self._uid', 'debug', keys=('lang',))
    def load_menus(self, debug):
        menus = super(IrUiMenu, self).load_menus(debug)
        for menu in menus.get('children'):
            for user_menu in self.env.user.menu_sequence_ids:
                if not menu.get('parent_id') and user_menu.menu_id.id == \
                        menu.get('id'):
                    print("\n\n\n>>before>>>>>>>>", menu['name'],
                          menu['sequence'], user_menu.sequence)
                    menu['sequence'] = user_menu.sequence

                    print("\n\n........after", menu['sequence'])

        print(">>menusmenusmenus>>>>>...",menus)
        return menus


class MenuSequence(models.Model):
    _name = 'menu.sequence'

    user_id = fields.Many2one('res.users', string="User")
    menu_id = fields.Many2one('ir.ui.menu', string="Menu",
                              domain="[('parent_id', '=', False)]")
    sequence = fields.Integer('Sequence')

    _sql_constraints = [
        ('menu_user_uniq', 'unique (menu_id,user_id)', "Menu already "
                                                       "exists for user !"),
    ]


class ResUsers(models.Model):
    _inherit = 'res.users'

    def __init__(self, pool, cr):
        init_res = super(ResUsers, self).__init__(pool, cr)
        type(self).SELF_WRITEABLE_FIELDS = list(
            set(
                self.SELF_WRITEABLE_FIELDS +
                ['menu_sequence_ids']))
        return init_res

    menu_sequence_ids = fields.One2many('menu.sequence', 'user_id',
                                        string="Menu Sequence")
