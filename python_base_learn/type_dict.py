from typing import TypedDict
class User(TypedDict):
   name: str
   age: int
   email: str
   is_active: bool
# 正确示例
user1: User = {
   "name": "Alice",
   "age": 30,
   "email": "alice@example.com",
   "is_active": True
}
# 类型检查会报错（age 类型错误）
bad_user: User = {
   "name": "Bob",
   "age": "thirty", # ❌ 应为 int
   "email": "bob@example.com"
}

from typing import NotRequired, List
class Address(TypedDict):
   street: str
   city: str
   zipcode: str
class UserProfile(TypedDict):
   id: int
   name: str
   email: str
   address: Address
   tags: NotRequired[List[str]] # 可选字段