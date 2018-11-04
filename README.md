# Appetito aracnide (adattato da Selezione Territoriale OII 2018)

Ape Maya è rimasta intrappolata in un nodo della tela di Tecla, un ragno molto temuto tra le api dell'alveare. Tecla si affretta ad afferrarla ma, quando giunge su quel nodo, si accorge di non avere appetito, e dice `BLEAH`. Va detto che l'appetito dei ragni è molto particolare: ogni volta che percorrono un filamento della loro rete, essi invertono lo stato del loro stomaco tra `SLURP` e `BLEAH`. Tecla deve quindi farsi un giretto nella rete sperando di tornare da Maya in stato `SLURP`.

La tela di Tecla è composta da `N` nodi (numerati da `0` a `N-1`) connessi tra loro da `M` filamenti.
Tecla e Ape Maya all'inizio si trovano entrambe nel nodo `0`,
e ogni filamento può essere attraversato da Tecla in entrambe le direzioni.
Aiuta Tecla ad individuare una passeggiata funzionale al buon appetito!

<description for="solve">

La procedura <method>solve</method> viene chiamata una sola volta all'inizio, e riceve in input i seguenti parametri:

- parametro <param>N</param>: numero di `nodi`,
- parametro <param>M</param>: numero di archi,
- parametro <param>U</param>, <param>V</param>: per `0 <= i <= M`, l'i-esimo arco è `(U[i], V[i])`.

La funzione <method>solve</method> deve calcolare e salvare il cammino di Tecla (in variabili globali).

</description>

<description for="length">

La funzione <method>length</method> viene chiamata una sola volta senza parametri, dopo <method>solve</method>,
e deve restituire la lunghezza del cammino fatto da Tecla.

</description>

Sia `L` la lunghezza del cammino restituita da <method>length</method>.
Deve valere `L <= {{longest_allowed_walk}}`, altrimenti il programma viene terminato.

<description for="get_node">

La funzione <method>get_node</method> viene chiamata `L` volte, con `i = 0, ..., L`, e deve restituire l'i-esimo nodo del cammino di Tecla.

</description>
