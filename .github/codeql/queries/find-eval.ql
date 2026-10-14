
/**
 * @name Detect use of eval
 * @description Finds calls to JavaScript eval().
 * @kind problem
 * @problem.severity warning
 * @id custom/js/find-eval
 */

import javascript

from CallExpr call
where
  call.getCalleeName() = "eval"
select call, "Avoid using eval() because it can execute arbitrary code."