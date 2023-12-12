'''-------------------------------------------------------------------------------
  This file is part of generalized random forest (grf).

  grf is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  grf is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with grf. If not, see <http://www.gnu.org/licenses/>.
 '''-------------------------------------------------------------------------------*/

from splitting.factory.ProbabilitySplittingRuleFactory import ProbabilitySplittingRule

class ProbabilitySplittingRuleFactory:
    def __init__(self, num_classes):
        self.num_classes = num_classes

    def create(self, max_num_unique_values, options):
        return ProbabilitySplittingRule(
            max_num_unique_values,
            self.num_classes,
            options.get_alpha(),
            options.get_imbalance_penalty()
        )