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
from openerp.osv import fields, osv,
from datetime import time, datetime
from openerp.tools.translate import _

class res_partner(osv.osv):
    _inherit = 'res.partner'
    _columns = {
    	"socio": fields.boolean("Socio"),
    }
    _defaults = {
			}
res_socios()

class padron_socios(osv.osv):
	_name = "padron.socios"
	_description = "Formulario de Socios"
	_columns = {
	"name": fields.char("Nombre del socio",size=30,required=True,help="Nombre del socio completo con las mayusculas en las primeras letras",translate=True,),
	"dni": fields.char("Documento",size=9,required=True,help="Numero de documento sin puntos decimales",translate=True),
	"call": fields.char("Señal Distintiva",size=6,help="Señal distintiva o numero de operador",translate=True),
	"cat": fields.selection([("0","Radioescucha"),("1","Inicial"),("2","Novicio"),("3","Intermedia"),("4","General"),("5","Superior"),("6","Especial"),],"Categoria"),
	"cond": fields.selection([("0","Cadete"),("1","Activo"),("2","Baja"),("3","Vitalicio"),("4","Honorario"),],"Condicion"),
	"fechan": fields.date("Fecha de Nacimiento"),
	"pago": fields.date("Pago Hasta"),
	}
	_defaults = {
			}
padron_socios()