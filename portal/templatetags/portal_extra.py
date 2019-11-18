from django import template

register = template.Library()


def str2(src):
        s = str(src)
        
        # need to remove leading zero 計件
        s2 = s.rstrip('0').rstrip('.') if '.' in s else s

@register.filter(is_safe=False)
def clean_decimal(value):
    if value == None:
        return ''
    """If value is None, use given default."""
    s = str(value)
        
        # need to remove leading zero 計件
    s2 = s.rstrip('0').rstrip('.') if '.' in s else s
    return s2
    
@register.filter(is_safe=False)
def default_rec5(value,arg):
    """If value is None, use given default."""
    s = str(value)
    if value < 10:
        return arg+"0000"+str(value)
    if value < 100:
        return arg+"000"+str(value)
    if value < 1000:
        return arg+"00"+str(value)
    if value < 10000:
        return arg+"0"+str(value)
     
@register.filter(is_safe=False)
def default_partempe_id(value):
    """If value is None, use given default."""
    arg ='S'
    s = str(value)
    if value < 10:
        return arg+"000"+str(value)
    if value < 100:
        return arg+"00"+str(value)
    if value < 1000:
        return arg+"0"+str(value)

@register.filter(is_safe=False)
def default_land_id(value):
    """If value is None, use given default."""
    arg ='L'
    s = str(value)
    if value < 10:
        return arg+"000"+str(value)
    if value < 100:
        return arg+"00"+str(value)
    if value < 1000:
        return arg+"0"+str(value)

@register.filter(is_safe=False)
def show_lock_status(value):
    if value :
        return "已鎖定"
    return "未鎖"
    
@register.filter(is_safe=False)
def default_if_dot(value, arg):
    """If value is None, use given default."""
    if value == '.' :
        return arg
    return value

@register.filter(is_safe=False)
def default_if_3dash(value, arg):
    """If value is None, use given default."""
    if value == '---' :
        return arg
    return value


@register.filter(is_safe=False)
def default_if_usage_status(value, arg):
    """If value is None, use given default."""
    if value == '使用情況' :
        return arg
    return value


# (0, '---'),
#     (1, '馒头'),
#     (2, '菜款'),
#     (3, '肉款'),
@register.filter(is_safe=False)
def display_food_cat(value):
    """If value is None, use given default."""
    if value == 0 :
        return '(未分類)'
    if value == 1 :
        return '馒头'
    if value == 2 :
        return '菜款'
    if value == 3 :
        return '肉款'
        
    return '(display_food_cat 要加信息)'


@register.filter(is_safe=False)
def default_if_img(value, arg):
    """If value is None, use given default."""
    # print(value)
    # if value:
    if value == 0:
        return ''

    return arg


@register.filter(is_safe=False)
def default_if_zero(value, arg):
    """If value is None, use given default."""
    # print(value)
    # if value:
    if value == 0:
        return arg

    return value

@register.filter(is_safe=False)
def default_if_none_zero(value, arg):
    """If value is None, use given default."""
    # print(value)
    # if value:
    if value == None:
        return arg
    if value == 0:
        return arg

    return value



@register.filter(is_safe=False)
def default_if_true(value, arg):
    """If value is None, use given default."""
    # print(value)
    # if value:
    if value  :
        return arg

    return '.'

@register.filter(is_safe=False)
def for_rowspan(value):
    """If value is None, use given default."""
    # print(value)
    # if value:
    if value == 0:
        return 1

    return value

def default_if_none(value, arg):
    """If value is None, use given default."""
    # print(value)
    # if value:
    if value == None or value == 'None':
        return arg

    return value

@register.filter(is_safe=False)
def default_if_true(value, arg):
    """If value is None, use given default."""
    # print(value)
    # if value:
    if value == True:
        return arg

    return ''



@register.filter(is_safe=False)
def min_to_hr(value):
    """If value is None, use given default."""
    # if len(value) == 0:
    #     return ''
    if value == None:
        return '.'
    if type(value) == str:
        return value

    if value == 0:
        return ''
# float("{0:.2f}".format(x))
    v= value/60
    v=int(v*10)
    v=v/10
    return v

@register.filter(is_safe=False)
def min_to_day(value):
    """If value is None, use given default."""
    # if len(value) == 0:
    #     return ''
    if value == None:
        return '.'
    if type(value) == str:
        return value

    if value == 0:
        return ''
# float("{0:.2f}".format(x))
    v= value/480 # 8*60=480 八小時算一天
    v=int(v*10)
    v=v/10
    return v

@register.filter(is_safe=False)
def tks_src(value):
    """If value is None, use given default."""
    # if len(value) == 0:
    #     return ''
    if value == None:
        return '?'
    if value == 'H':
        return '＊'
    return '　'# 全形空格

@register.filter(is_safe=False)
def leading_space_3(value):
    """If value is None, use given default."""
    # if len(value) == 0:
    #     return ''
    # print(type(value))
    if value == None:
        return '?'
    if value < 10:
        # return 'xx'+str(value)
        return '&nbsp;&nbsp;'+str(value)

    if value < 100:
        return '&nbsp;'+str(value)
    return value

    # return '　'# 全形空格


@register.filter(is_safe=False)
def min_to_int_hr(value):
    """If value is None, use given default."""
    # if len(value) == 0:
    #     return ''
    if type(value) == str:
        return value

    if value == 0:
        return ''
# float("{0:.2f}".format(x))
    v= int(value/60)
    # v=int(v*10)
    # v=v/10
    return v