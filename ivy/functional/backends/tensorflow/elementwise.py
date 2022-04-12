# global
import tensorflow as tf
from tensorflow.python.types.core import Tensor
from typing import Optional, Tuple, Union

# local
import ivy


def bitwise_left_shift(x1: Tensor,
                       x2: Tensor,
                       out: Optional[Tensor] = None)\
                       -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    ret = tf.bitwise.left_shift(x1, x2)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def add(x1: Tensor,
        x2: Tensor,
        out: Optional[Tensor] = None)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    ret = tf.add(x1, x2)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def bitwise_xor(x1: Tensor,
                x2: Tensor,
                out: Optional[Tensor] = None)\
        -> Tensor:
    if not isinstance(x2, Tensor):
        x2 = tf.constant(x2, dtype=x1.dtype)
    if ('int' not in str(x1.dtype)) & ('int' not in str(x2.dtype)):
        ret = tf.math.logical_xor(x1, x2)
    else:
        x1, x2 = _cast_for_binary_op(x1, x2)
        ret = tf.bitwise.bitwise_xor(x1, x2)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def exp(x: Tensor,
        out: Optional[Tensor] = None)\
        -> Tensor:
    ret = tf.math.exp(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def expm1(x: Tensor,
          out: Optional[Tensor] = None)\
        -> Tensor:
    ret = tf.math.expm1(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def bitwise_invert(x: Tensor,
                   out: Optional[Tensor] = None)\
        -> Tensor:
    if 'int' not in str(x.dtype):
        ret = tf.logical_not(x)
    else:
        ret = tf.bitwise.invert(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def bitwise_and(x1: Tensor,
                x2: Tensor,
                out: Optional[Tensor] = None)\
        -> Tensor:
    if not isinstance(x2, Tensor):
        x2 = tf.constant(x2, dtype=x1.dtype)
    if ('int' not in str(x1.dtype)) & ('int' not in str(x2.dtype)):
        ret = tf.math.logical_and(x1, x2)
    else:
        x1, x2 = _cast_for_binary_op(x1, x2)
        ret = tf.bitwise.bitwise_and(x1, x2)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def ceil(x: Tensor,
         out: Optional[Tensor] = None)\
        -> Tensor:
    if 'int' in str(x.dtype):
        ret = x
    else:
        ret = tf.math.ceil(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def floor(x: Tensor,
          out: Optional[Tensor] = None)\
        -> Tensor:
    if 'int' in str(x.dtype):
        ret = x
    else:
        ret = tf.math.floor(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def isfinite(x: Tensor) \
        -> Tensor:
    if ivy.is_int_dtype(x):
        return tf.ones_like(x, tf.bool)
    return tf.math.is_finite(x)


def asin(x: Tensor,
         out: Optional[Tensor] = None) \
        -> Tensor:
    ret = tf.asin(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def isinf(x: Tensor) \
        -> Tensor:
    if ivy.is_int_dtype(x):
        return tf.zeros_like(x, tf.bool)
    return tf.math.is_inf(x)


def _tf_cast(x: Tensor, dtype: tf.dtypes.DType) -> Tensor:
    try:
        return tf.cast(x, dtype)
    except ValueError:
        return x


def _cast_for_binary_op(x1: Tensor, x2: Tensor)\
        -> Tuple[Union[Tensor, int, float, bool], Union[Tensor, int, float, bool]]:
    x1_bits = ivy.functional.backends.tensorflow.dtype_bits(x1.dtype)
    if isinstance(x2, (int, float, bool)):
        return x1, x2
    x2_bits = ivy.functional.backends.tensorflow.dtype_bits(x2.dtype)
    if x1_bits > x2_bits:
        x2 = _tf_cast(x2, x1.dtype)
    elif x2_bits > x1_bits:
        x1 = _tf_cast(x1, x2.dtype)
    return x1, x2


def equal(x1: Tensor,
          x2: Tensor,
          out: Optional[Tensor] = None)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    ret = tf.math.equal(x1, x2)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def less_equal(x1: Tensor,
               x2: Tensor,
               out: Optional[Tensor] = None)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    ret = tf.math.less_equal(x1, x2)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def asinh(x: Tensor,
          out: Optional[Tensor] = None) \
        -> Tensor:
    ret = tf.asinh(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def sign(x: Tensor,
         out: Optional[Tensor] = None) \
        -> Tensor:
    if x.dtype in [tf.uint8, tf.uint16, tf.uint32, tf.uint64]:
        return tf.cast(tf.math.sign(tf.cast(x, tf.float32)), x.dtype)
    ret = tf.math.sign(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def sqrt(x: Tensor,
         out: Optional[Tensor] = None)\
        -> Tensor:
    if x.dtype == 'float32':
        x_64 = tf.cast(x, tf.float64)
        ret = tf.cast(tf.sqrt(x_64), x.dtype)
    else:
        ret = tf.math.sqrt(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def cosh(x: Tensor,
         out: Optional[Tensor] = None) \
        -> Tensor:
    ret = tf.cosh(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def log10(x: Tensor,
          out: Optional[Tensor] = None) \
        -> Tensor:
    ret = tf.experimental.numpy.log10(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def log(x: Tensor,
        out: Optional[Tensor] = None)\
        -> Tensor:
    ret = tf.math.log(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def log2(x: Tensor,
         out: Optional[Tensor] = None) \
        -> Tensor:
    ret = tf.experimental.numpy.log2(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def log1p(x: Tensor,
          out: Optional[Tensor] = None) \
        -> Tensor:
    ret = tf.experimental.numpy.log1p(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def isnan(x: Tensor)\
        -> Tensor:
    if ivy.is_int_dtype(x):
        return tf.zeros_like(x, tf.bool)
    return tf.math.is_nan(x)


def less(x1: Tensor,
         x2: Tensor,
         out: Optional[Tensor] = None)\
        -> Tensor:
    if hasattr(x1, 'dtype') and hasattr(x2, 'dtype'):
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    ret = tf.math.less(x1, x2)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def cos(x: Tensor,
        out: Optional[Tensor] = None)\
        -> Tensor:
    ret = tf.cos(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def logical_not(x: Tensor,
                out: Optional[Tensor] = None)\
        -> Tensor:
    ret = tf.logical_not(tf.cast(x, tf.bool))
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret

  
def divide(x1: Tensor,
           x2: Tensor,
           out: Optional[Tensor] = None)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    ret = tf.divide(x1, x2)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def greater(x1: Tensor,
            x2: Tensor,
            out: Optional[Tensor] = None)\
        -> Tensor:
    if hasattr(x1, 'dtype') and hasattr(x2, 'dtype'):
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    ret = tf.math.greater(x1, x2)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def greater_equal(x1: Tensor,
                  x2: Tensor,
                  out: Optional[Tensor] = None)\
        -> Tensor:
    if hasattr(x1, 'dtype') and hasattr(x2, 'dtype'):
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    ret = tf.math.greater_equal(x1, x2)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def acos(x: Tensor,
         out: Optional[Tensor] = None)\
        -> Tensor:
    ret = tf.acos(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def logical_xor(x1: Tensor,
                x2: Tensor,
                out: Optional[Tensor] = None) \
        -> Tensor:
    ret = tf.math.logical_xor(tf.cast(x1, tf.bool), tf.cast(x2, tf.bool))
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def logical_or(x1: Tensor,
               x2: Tensor,
               out: Optional[Tensor] = None)\
        -> Tensor:
    ret = tf.logical_or(tf.cast(x1, tf.bool), tf.cast(x2, tf.bool))
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def logical_and(x1: Tensor,
                x2: Tensor,
                out: Optional[Tensor] = None)\
        -> Tensor:
    ret = tf.logical_and(tf.cast(x1, tf.bool), tf.cast(x2, tf.bool))
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def acosh(x: Tensor,
          out: Optional[Tensor] = None) \
        -> Tensor:
    ret = tf.acosh(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def sin(x: Tensor,
        out: Optional[Tensor] = None)\
        -> Tensor:
    ret = tf.sin(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def multiply(x1: Tensor, x2: Tensor)\
        -> Tensor:
    if hasattr(x1, 'dtype') and hasattr(x2, 'dtype'):
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    return tf.math.multiply(x1, x2)


def negative(x: Tensor) -> Tensor:
    if x.dtype in [tf.uint8, tf.uint16, tf.uint32, tf.uint64]:
        return tf.cast(tf.negative(tf.cast(x, tf.float32)), x.dtype)
    return tf.negative(x)


def not_equal(x1: Tensor, x2: Tensor)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.math.not_equal(x1, x2)


def tanh(x: Tensor) \
        -> Tensor:
    return tf.tanh(x)


def floor_divide(x1: Tensor, x2: Tensor)\
                -> Tensor:
    if not isinstance(x2, Tensor):
        x2 = tf.constant(x2, dtype=x1.dtype)
    else:
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    return tf.math.floordiv(x1, x2)


def sinh(x: Tensor) \
        -> Tensor:
    return tf.sinh(x)


def bitwise_or(x1: Tensor, x2: Tensor) \
        -> Tensor:
    if not isinstance(x2, Tensor):
        x2 = tf.constant(x2, dtype=x1.dtype)
    if ('int' not in str(x1.dtype)) & ('int' not in str(x2.dtype)):
        return tf.math.logical_or(x1, x2)
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.bitwise.bitwise_or(x1, x2)


def positive(x: Tensor)\
        -> Tensor:
    return tf.experimental.numpy.positive(x)


def square(x: Tensor)\
        -> Tensor:
    return tf.math.square(x)


def pow(x1: Tensor, x2: Tensor)\
        -> Tensor:
    if not isinstance(x2, Tensor):
        x2 = tf.constant(x2, dtype=x1.dtype)
    promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
    x1 = tf.cast(x1, promoted_type)
    x2 = tf.cast(x2, promoted_type)
    if x1.dtype.is_unsigned:
        x1 = tf.cast(x1, tf.float64)
    if x2.dtype.is_unsigned:
        x2 = tf.cast(x2, tf.float64)
    return tf.cast(tf.experimental.numpy.power(x1, x2), promoted_type)


def remainder(x1: Tensor, x2: Tensor)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.experimental.numpy.remainder(x1, x2)


def round(x: Tensor)\
        -> Tensor:
    if 'int' in str(x.dtype):
        return x
    return tf.round(x)


def trunc(x: Tensor)\
        -> Tensor:
    if 'int' in str(x.dtype):
        return x
    res = tf.zeros(x.shape, dtype=x.dtype)
    res = tf.tensor_scatter_nd_update(res, tf.where(x > 0), tf.math.floor(x[x > 0]))
    res = tf.tensor_scatter_nd_update(res, tf.where(x < 0), tf.math.ceil(x[x < 0]))
    return res


def abs(x: Tensor,
        out: Optional[Tensor] = None)\
        -> Tensor:
    if 'uint' in ivy.dtype(x, as_str=True):
        ret = x
    else:
        ret = tf.abs(x)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def subtract(x1: Tensor, x2: Tensor)\
        -> Tensor:
    if hasattr(x1, 'dtype') and hasattr(x2, 'dtype'):
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    return tf.subtract(x1, x2)


def logaddexp(x1: Tensor, x2: Tensor) -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.experimental.numpy.logaddexp(x1, x2)


def bitwise_right_shift(x1: Tensor, x2: Tensor)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.bitwise.right_shift(x1, x2)


def bitwise_left_shift(x1: Tensor, x2: Tensor)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.bitwise.left_shift(x1, x2)


tan = tf.tan


def atan(x: Tensor) \
        -> Tensor:
    return tf.atan(x)



def atanh(x: Tensor) \
        -> Tensor:
    return tf.math.atanh(x)



def atan2(x1: Tensor, x2: Tensor) -> Tensor:
    if hasattr(x1, 'dtype') and hasattr(x2, 'dtype'):
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    return tf.math.atan2(x1, x2)



cosh = tf.math.cosh
log = tf.math.log
exp = tf.math.exp

# Extra #
# ------#

minimum = tf.minimum
maximum = tf.maximum
erf = tf.math.erf