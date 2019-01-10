# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    Autor: Brayhan Andres Jaramillo Castaño
#    Correo: brayhanjaramillo@hotmail.com
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from odoo import api, fields, models, _
import time
from datetime import datetime, timedelta, date
import logging
_logger = logging.getLogger(__name__)


class ResourceNodo(models.Model):

	_name = "resource.nodo"

	name = fields.Char(string='Name Nodo', required=True)
	number_nodo = fields.Char('Number Nodo', readonly=True)
	serial_number = fields.Integer(string='Serial Number')
	employee_id = fields.Many2one('hr.employee', string='Installed to')
	instalation_date = fields.Date('Instalation Date')
	description= fields.Text(string='Description')
	antenna_ids = fields.Many2many('resource.antenna', 'resource_antenna_nodo_rel', 'nodo_id', 'antenna_id', string='Antennas')
    
	@api.model
	def create(self, vals):
		sequence_id= self.env['ir.sequence'].next_by_code('resource.nodo')
		_logger.info(sequence_id)
		vals['number_nodo'] = sequence_id
		res = super(ResourceNodo, self).create(vals)
		return res
		
ResourceNodo()