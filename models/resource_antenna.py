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


class ResourceAntenna(models.Model):

	_name = "resource.antenna"

	name = fields.Char(string='Name Antenna', required=True)
	number_antenna = fields.Char('Number Antenna', readonly=True)
	serial_number = fields.Integer(string='Serial Number')
	nodo_ids = fields.Many2one('resource.nodo', 'Nodo')
	sale_date = fields.Date('Sale Date')
	instalation_date = fields.Date(string='Instalation Date')
	state= fields.Selection([('in_service','In Service'), 
							('out_service','Out of Service'), 
							('in_maintenance','In Maintenance')], 
		string="State", default='out_service')
	amortization = fields.Integer(string='Amortization')
	days_of_use = fields.Integer(string='Days of Use')
	partner_id = fields.Many2one('res.partner', 'Assigned to')
	description= fields.Text(string='Description')

	@api.model
	def create(self, vals):
		sequence_id= self.env['ir.sequence'].next_by_code('resource.antenna')
		vals['number_antenna'] = sequence_id
		res = super(ResourceAntenna, self).create(vals)
		return res

	@api.model
	def update_data_antena(self):

		format="%Y-%m-%d"
		date_end= fields.Datetime.context_timestamp(self, fields.Datetime.from_string(fields.Datetime.now()))

		antenas_ids= self.search(['|',('days_of_use', '=', 0), ('amortization', '=', 0)])
		_logger.info(antenas_ids)

		if  antenas_ids:

			for x in antenas_ids:
				days_of_use=0
				days_amortization=0

				if x.instalation_date:
					date_begin= x.instalation_date

					if x.days_of_use == 0:
						_logger.info('no esta actualizado')
						_logger.info(str(date_begin))
						_logger.info(str(date_end)[0:10])

						date_begin_parse= datetime.strptime(str(date_begin), format)
						date_end_parse= datetime.strptime(str(date_end)[0:10], format)

						_logger.info(date_begin_parse)
						_logger.info(date_begin_parse)

						days_of_use= date_end_parse - date_begin_parse

						_logger.info(days_of_use.days)

						days_of_use=days_of_use.days

				if x.sale_date:

					date_sale= x.sale_date

					if x.amortization == 0:
						_logger.info('no esta actualizado')
						_logger.info(str(date_sale))
						_logger.info(str(date_end)[0:10])

						date_begin_parse= datetime.strptime(str(date_sale), format)
						date_end_parse= datetime.strptime(str(date_end)[0:10], format)

						_logger.info(date_begin_parse)
						_logger.info(date_begin_parse)

						days_amortization= date_end_parse - date_begin_parse

						_logger.info(days_amortization.days)

						days_amortization=days_amortization.days

				x.write({'days_of_use': days_of_use or 0, 'amortization': days_amortization or 0})


ResourceAntenna()