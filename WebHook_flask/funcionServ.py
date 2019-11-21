import numpy as np
def multiplica(A=None, B=None):
    matA = A["Array"]
    rowA = A["row"]
    colA = A["col"]
    matB = B["Array"]
    rowB = B["row"]
    colB = B["col"]
    if not(A and B):
        result = np.matmul(np.random.randint(1, 40, size=(4,5)), np.eye(5))
        codigoE = 0
        msg = ""
    else:
        matA = np.asarray(matA).reshape((rowA, colA))
        matB = np.asarray(matB).reshape((rowB, colB))
        try:
            assert colA == rowB, "no son compatibles"
            result = np.matmul(matA, matB)
            codigoE = 0
            msg = ""
        except Exception as error:
            msg = error.__str__()
            result = None
            codigoE = 1
    result = [result.ravel().tolist(), result.shape[0], result.shape[1]]
    return {"result": result, "EC": codigoE, "MSG": msg}

