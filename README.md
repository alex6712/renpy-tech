# Ren'Py Tech

<p align="center">
    <em>Репозиторий технического мода для Бесконечного лета, в котором собрано множество интересных решений</em>
</p>

## О модификации

Основной идеей, заложенной в эту модификацию, я вижу создание общего сборника инструментов для удобной разработки модов.

### Актуальность проблемы

С самого открытия мастерской **Бесконечного лета** моды делал кто только мог и кто только хотел. Благодаря простому синтаксису Python
и очень небольшому необходимому набору знаний программирования для минимального старта, практически каждый человек может создать что-то
своё.

И это замечательно!

Однако из этого вытекает и проблема _"разношёрстности"_ модов. Как в плане интересных идей, так и в плане качества сценариев, 
визуального оформления, и что интересно в данном контексте, **местной кодовой базы**. Кто-то более опытный пишет код, ориентируясь
на принципы форматирования, изложенные в PEP 8, а кто-то даже и не слышал о том, что код может быть _отформатирован_. Кто-то
использует объектно-ориентированное программирование для решения его программистских задач, а кто-то буквально вчера понял, как
работают функции.

Несомненно, с каждым годом _среднее_ качество исполнения модов растёт. Однако всё ещё остаётся на весьма низком уровне.
В один момент кто-то из сообщества каходит решение определённой проблемы. Например, как заменить экран ``say`` в своём моде.
И после успешного применения этого метода, его начинают использовать и в других модах. Не разбираясь, однако, как он работает.
И хотя массово _заставить_ людей начать изучать программирование более глубоко невозможно, можно хотя бы немного посбособствовать
повышению качества кодовой базы модификаций, путём создания платформы, объединяющей определённые решения и встраиваемой
в другие модификации в качестве фрагмента.

### Список возможностей

* множество мелких _features_, не включённых в стандартную библиотеку **Ren'Py** по типу _декомпилятора_,
описанных другими разработчиками _CDD_ и _CDS_, _ATL_, игр;
* механизм внедрения зависимостей и набор декораторов для более тонкой настройки модификаций;
* способ разграничения **пространств имён** различных модификаций благодаря именнованным хранилищам
(ориг. англ. _named storages_).

## Загрузка

Мод загружается как и все в мастерской Бесконечного лета: подпиской в Steam.
Данный репозиторий служит для предоставления доступа к кодовой базе мода.

Не рекомендуется устанавливать мод с данного репозитория.

## Интеграция

Если Вы, как разработчик, хотите использовать _"платформу"_ в своей модификации, Вы можете сделать следующее:

1. подпишитесь на модификацию **Ren'Py Tech** в Steam (это действие можно будет отменить позднее);
2. перейдите на страницу вашего продукта в Steam;
3. в блоке **"Управление"** выберите пункт _Изменить список необходимых продуктов_;
4. перейдите во вкладку **"Подписки на предметы"**;
5. среди списка выберите **Ren'Py Tech**;
6. нажмите на кнопку _Сохранить и продолжить_.

После выполнения данных действий модификация **Ren'Py Tech** будет устанавливаться вместе с Вашим модом, если
она ещё не была установлена у пользователя. Таким образом, Вы можете быть спокойны относительно того, присутствует
ли данная модификация на устройстве пользователя.

***

### Автор

_**alex6712**_ - _Ванюков Алексей Игоревич_, **Python & Java Junior Backend**.

### Контакты

* Адрес электронной почты: alexeivanyukov@yandex.ru
* [Telegram](https://t.me/Eclipse6712)
* [VKontakte](https://vk.com/zerolevelmath)
