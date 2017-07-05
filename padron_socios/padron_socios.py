# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    Copyright (c) 2017 Leandro Masutti
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv
from datetime import time, datetime
from openerp.tools.translate import _

class res_partner(osv.osv):
    _inherit = 'res.partner'
    _columns = {
    			"socio": fields.boolean("Socio"),
    			"dni": fields.char("Documento"),
    			"num": fields.integer("Numero de Socio"),
    			"call": fields.char("Señal Distintiva",size=6,help="Señal distintiva o numero de operador",translate=True),
				"cat": fields.selection([("0","Radioescucha"),("1","Inicial"),("2","Novicio"),("3","Intermedia"),("4","General"),("5","Superior"),("6","Especial"),],"Categoria"),
				"cond": fields.selection([("0","Cadete"),("1","Activo"),("2","Baja"),("3","Vitalicio"),("4","Honorario"),],"Condicion"),
				"pago": fields.date("Pago Hasta"),
    			}
    _defaults = {
				}
res_partner()