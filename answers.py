1. Такой формат ip-аддресса позволяет не выполнять инструкцию для каждого loopback'a по отдельности
2. 
3.
	1. LS Type: Router Links
	2. 3 на всех, т.к. в сети 3 роутера и каждый прислал свой LSA 
	3. Все роутеры. Тип, ID канала связи, ID-роутера распространителя,
		длину LSA, количество соединений роутера распространителя и их описание.
	   В пределах зоны. 
4. 
	1. LS Type: Router Links
	2. На всех 1, потому что общаются с 1 сетью
	3. Выделенный маршрутизатор, занимается рассылкой LSA в сети.
		Все маршрутизаторы шлют черз него.
	4. Designated router. Тип, адресс designated router'a, его ID,
		длину и список подсоединенных к сети. В пределах зоны.
6.	
	1. OSPF Inter Area
	2. Две - 192.168.1.0/24 и 192.168.2.0/24, две.
	3. Генерирует Area Border Router, конвертирует Router и Network LSA в  Summary.
		Содержит информацию о сетях и о стоимости пути к ним/ В соседние зоны.
7.	
	1. O - OSPF, E - External Type 2. 
		В типе 2 в качестве метрики рассчитывается только стоимость перехода из одной АС в другую.
	2. Информация о внешних сетях (использующих другие протоколы маршрутизации).
		Адрес, маски, ID роутера отправителя.
	3. Их генерирует пограничный маршрутизатор (R2AR0). 
		Он рассылает OSPF пакеты во все возможные области. 
		Они содержат описание внешних маршрутов, которые передаются в OSPF.
8.
	1. Зона, которая не знает путей за своими пределами (но свои наружу отправляет). 
		Если изнутри надо отправить что то вовне, то используется маршрут по умолчанию. 
		Снижает нагрузку на маршрутизаторы внутри области.
	2. У R1AR1 появился дефолтный маршрут (со звёздочкой) и пропала вся информация о внешних маршрутах.
	3. 
