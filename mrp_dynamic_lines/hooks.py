# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def pre_init_hook(cr):
    cr.execute('ALTER TABLE IF EXISTS mrp_bom_line '
               'ADD COLUMN IF NOT EXISTS variant_id INT')
    cr.execute('ALTER TABLE IF EXISTS mrp_bom_line '
               'ADD COLUMN IF NOT EXISTS product_tmpl_id INT')
    cr.execute('UPDATE mrp_bom_line '
               'SET variant_id=product_id,'
               'product_tmpl_id=p.product_tmpl_id '
               'FROM product_product p WHERE p.id=product_id')
    return True


def uninstall_hook(cr, pool):
    cr.execute('UPDATE mrp_bom_line SET product_id=variant_id;')
    return True
