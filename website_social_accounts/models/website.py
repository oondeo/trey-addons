###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class Website(models.Model):
    _inherit = "website"

    social_twitter_username = fields.Char(
        compute="_compute_social_twitter_username",
    )
    social_instagram_username = fields.Char(
        compute="_compute_social_instagram_username",
    )
    social_flickr = fields.Char(
        related="company_id.social_flickr",
    )
    social_pinterest = fields.Char(
        related="company_id.social_pinterest",
    )
    social_reddit = fields.Char(
        related="company_id.social_reddit",
    )
    social_skype = fields.Char(
        related="company_id.social_skype",
    )
    social_tumblr = fields.Char(
        related="company_id.social_tumblr",
    )
    social_twitch = fields.Char(
        related="company_id.social_twitch",
    )
    social_vimeo = fields.Char(
        related="company_id.social_vimeo",
    )
    social_whatsapp = fields.Char(
        related="company_id.social_whatsapp",
    )

    @api.model
    def _get_username_from_url(self, url):
        return url and [p for p in url.split("/") if p][-1] or ""

    @api.depends("company_id.social_twitter")
    def _compute_social_twitter_username(self):
        self.social_twitter_username = self._get_username_from_url(
            self.company_id.social_twitter
        )

    @api.depends("company_id.social_instagram")
    def _compute_social_instagram_username(self):
        self.social_instagram_username = self._get_username_from_url(
            self.company_id.social_instagram
        )
