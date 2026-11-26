# Python程序设计 第三次作业 第2题（25分）
# 函数直接更新传入的products，返回(是否成功, 本次操作产生的销售额)。


def process_operation(products, operation):
    # TODO: 读取操作类型和商品编号
    Optype = operation["type"]
    Opid = operation["id"]
    # TODO: 根据add/restock/reprice/sell处理新增、进货、调价、销售
    if Optype == "add":
        if Opid in products:
            return False, 0
        else:
            products[Opid]={
                "name": operation["name"],
                "price": operation["price"],
                "stock": operation["stock"]
            }
            return True, 0

        
    elif Optype == "restock":
        if Opid not in products:
            return False, 0
        else:
            products[Opid]["stock"] += operation["quantity"]
            return True, 0

        
    elif Optype == "reprice":
        if Opid not in products:
            return False, 0
        else:
            products[Opid]["price"] = operation["price"]
            return True, 0

        
    elif Optype == "sell":
        if Opid not in products:
            return False, 0
        if products[Opid]["stock"] < operation["quantity"]:
            return False, 0
        else:
            products[Opid]["stock"] -= operation["quantity"]
            profit = operation["quantity"] * products[Opid]["price"]
            return True, profit

    return False, 0
    # TODO: 失败时不修改products，返回(False, 0)
    # TODO: 成功销售返回(True, 本次销售额)，其他成功操作返回(True, 0)
    pass


# 以下为提供的测试与输出代码，请保留，不需要修改。
from copy import deepcopy

products = {
    "A01": {"name": "矿泉水", "price": 3, "stock": 10},
    "A02": {"name": "咖啡", "price": 8, "stock": 2},
}
# 每项：操作、预期返回值、预期的完整商品字典。
test_cases = [
    ({"type": "sell", "id": "A02", "quantity": 1}, (True, 8),
     {"A01": {"name": "矿泉水", "price": 3, "stock": 10}, "A02": {"name": "咖啡", "price": 8, "stock": 1}}),
    ({"type": "sell", "id": "A02", "quantity": 2}, (False, 0),
     {"A01": {"name": "矿泉水", "price": 3, "stock": 10}, "A02": {"name": "咖啡", "price": 8, "stock": 1}}),
    ({"type": "restock", "id": "A02", "quantity": 3}, (True, 0),
     {"A01": {"name": "矿泉水", "price": 3, "stock": 10}, "A02": {"name": "咖啡", "price": 8, "stock": 4}}),
    ({"type": "reprice", "id": "A02", "price": 9}, (True, 0),
     {"A01": {"name": "矿泉水", "price": 3, "stock": 10}, "A02": {"name": "咖啡", "price": 9, "stock": 4}}),
    ({"type": "sell", "id": "A02", "quantity": 4}, (True, 36),
     {"A01": {"name": "矿泉水", "price": 3, "stock": 10}, "A02": {"name": "咖啡", "price": 9, "stock": 0}}),
    ({"type": "add", "id": "A03", "name": "面包", "price": 6, "stock": 5}, (True, 0),
     {"A01": {"name": "矿泉水", "price": 3, "stock": 10}, "A02": {"name": "咖啡", "price": 9, "stock": 0}, "A03": {"name": "面包", "price": 6, "stock": 5}}),
    ({"type": "add", "id": "A03", "name": "新品", "price": 99, "stock": 9}, (False, 0),
     {"A01": {"name": "矿泉水", "price": 3, "stock": 10}, "A02": {"name": "咖啡", "price": 9, "stock": 0}, "A03": {"name": "面包", "price": 6, "stock": 5}}),
]
passed_count = 0
turnover = 0
for index, (operation, expected_result, expected_products) in enumerate(test_cases, 1):
    result = process_operation(products, operation)
    valid_return = (isinstance(result, tuple) and len(result) == 2
                    and type(result[0]) is bool and type(result[1]) is int)
    passed = valid_return and result == expected_result and products == expected_products
    print(f"操作{index}：{'通过' if passed else '未通过'}")
    if passed:
        passed_count += 1
    if valid_return:
        turnover += result[1]
    # 每项测试结束后恢复预期状态，避免一个错误干扰后续测试。
    products.clear()
    products.update(deepcopy(expected_products))

for kind in ["restock", "reprice", "sell"]:
    before = deepcopy(products)
    result = process_operation(products, {"type": kind, "id": "Z99", "quantity": 1, "price": 5})
    passed = (isinstance(result, tuple) and len(result) == 2
              and type(result[0]) is bool and type(result[1]) is int
              and result == (False, 0) and products == before)
    print(f"不存在商品的{kind}操作：{'通过' if passed else '未通过'}")
    if passed:
        passed_count += 1
    products.clear()
    products.update(before)

print(f"本次操作序列累计营业额：{turnover}元")
print(f"通过测试：{passed_count}/10")
