#
# Copyright (C) 2018  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import logging
log = logging.getLogger("composer-cli")

import json

def argify(args):
    """Take a list of human args and return a list with each item

    :param args: list of strings with possible commas and spaces
    :type args: list of str
    :returns: List of all the items
    :rtype: list of str

    Examples:

    ["one,two", "three", ",four", ",five,"] returns ["one", "two", "three", "four", "five"]
    """
    return filter(lambda i: i, [arg for entry in args for arg in entry.split(",")])

def toml_filename(recipe_name):
    """Convert a recipe name into a filename.toml

    :param recipe_name: The recipe's name
    :type recipe_name: str
    :returns: The recipe name with ' ' converted to - and .toml appended
    :rtype: str
    """
    return recipe_name.replace(" ", "-") + ".toml"

def frozen_toml_filename(recipe_name):
    """Convert a recipe name into a filename.toml

    :param recipe_name: The recipe's name
    :type recipe_name: str
    :returns: The recipe name with ' ' converted to - and .toml appended
    :rtype: str
    """
    return recipe_name.replace(" ", "-") + ".frozen.toml"

def handle_api_result(result, show_json=False):
    """Log any errors, return the correct value

    :param result: JSON result from the http query
    :type result: dict
    """
    if show_json:
        print(json.dumps(result, indent=4))
    elif result.get("error", False):
        log.error(result["error"]["msg"])

    if result["status"] == True:
        return 0
    else:
        return 1
