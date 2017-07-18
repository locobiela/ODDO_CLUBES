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
from datetime import datetime, date, time, timedelta
current_date=datetime.now().strftime("%m/%Y")

class res_partner(osv.osv):
    _inherit = 'res.partner'
    _columns = {
       			"socio": fields.boolean("Socio"),
       			"tipo": fields.selection([("0","D.N.I."),("1","C.I."),("2","L.E."),("3","L.C."),],"Tipo de Documento"),
    			"dni": fields.char("Documento Nro."),
    			"num": fields.integer("Numero de Socio"),
    			"call": fields.char("Señal Distintiva",size=6,help="Señal distintiva o numero de operador"),
				"cat": fields.selection([("0","Radioescucha"),("1","Inicial"),("2","Novicio"),("3","Intermedia"),("4","General"),("5","Superior"),("6","Especial"),],"Categoria"),
				"cond": fields.selection([("0","Cadete"),("1","Activo"),("2","Fundador"),("3","Vitalicio"),("4","Honorario"),("5","Benefactor"),("6","Extraordinario"),],"Condicion"),
				"vence": fields.many2one("account.period","date_start"),
				"down_date": fields.datetime("Fecha de Baja"),
				"motivo": fields.selection([("0","Voluntario"),("1","Exonerado"),("2","Fallecimiento"),("3","Mora"),],"Motivo"),
				"acta": fields.char("Acta Numero"),
				"estado": fields.selection([("0","Baja"),("1","Alta"),("2","Suspendido")],"Estado"),
				"birthdate": fields.datetime("Fecha de Nacimiento"),
				}
res_partner()
