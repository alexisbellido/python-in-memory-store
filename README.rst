A very basic Python in-memory store using tuples in a dictionary
=====================================================================================

Store is a Python class that uses a dictionary to work as simple key-value in-memory store.

The basic usage is like this.

.. code-block:: bash

  from store import Store
  Store.set('name', 'John')
  key = Store.get('name)

Unit tests for all the class methods are in test-store.py.

You can use the following methods:

*Store.set('key', 'value')*
Assigns `value` to `key`.

*Store.get('key')*
Retrieves the stored in `key`.

Some time and memory values after storing and retrieving 10 million keys.

.. code-block:: bash

  $ python use-store.py 
  Storing 10,000,000 keys...
  Keys stored: 10,000,000
  Milliseconds per key: 0.001250524640083313
  Bytes used by store: 335,544,424
  Bytes used per key: 33.5544424
  Retrieving 10,000,000 keys...
  Milliseconds elapsed to retrieve each key: 0.0007979944467544556


Performance and memory usage
-------------------------------------------------------------------


A design document on any of the individual components and how they interact is optional.

Please address as part of your final work any trade-offs you made amongst the requirements.


Requirements
-----------------------------------------------------------------------------


At its heart, our library stores key/value pairs with an optional time based expiration of keys.

The caller of the library should be able to:

Put a key/value pair

Put a key/value pair that has an optional expiration value

Retrieve a key/value pairc

Delete a key/value pair

Be used within a process that includes multiple threads


Performance targets:


Retrieve a key with a 95p time of less than 1 millisecond

Retrieve a key with a 99p time of less than 5 milliseconds

Handle up to 10 million key/value pairs


For performance targets, it is acceptable to discuss the various strategies you might attempt in order to hit those targets and what the tradeoffs might be with each approach.
