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

from splitting.factory.MultiRegressionSplittingRuleFactory import MultiRegressionSplittingRule

class MultiRegressionSplittingRuleFactory:
    def __init__(self, num_outcomes):
        self.num_outcomes = num_outcomes

    def create(self, max_num_unique_values, options):
        return MultiRegressionSplittingRule(
            max_num_unique_values,
            options.get_alpha(),
            options.get_imbalance_penalty(),
            self.num_outcomes
        )
