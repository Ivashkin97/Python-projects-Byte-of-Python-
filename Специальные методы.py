#__init__(self,...) этот метод вызывается прямо перед тем, как вновь созданный объект возвращается для использования
#__del__(self) вызывается перед уничтожением объекта
#__str__(self) вызывается при использовании функции print или str()
#__it__(self, other) вызывается, когда используется оператор "меньше" (<). Существуют и аналогичные методы для всех операторов (+, >, и т.д.)
#__getitem__(self, key) вызывается при использовании оператора индексирования x [индекс]
#__len__(self) вызывается при обращении к встроенной функции len() для объекта-последовательности
