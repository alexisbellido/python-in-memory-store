A very basic Python in-memory store using tuples in a dictionary
=====================================================================================

Store is a Python class that uses a dictionary to work as a simple key-value in-memory store.

The basic usage is like this.

.. code-block:: bash

  from store import Store
  Store.set('name', 'John')
  key = Store.get('name)

Unit tests for all the class methods are in test-store.py.

The use-store.py script uses the class to measure times and memory when storing and retrieving 10 million keys.

Methods
------------------------------------------------------------------------
You can use the following methods:

**Store.set(key, value, expires)**

  Assigns value to key and sets the expiration to expires seconds (the default is 3600).

**Store.get(key)**

  Retrieves the value stored in key.

**Store.delete(key)**

  Deletes one key.

**Store.clean()**

  Deletes all the keys that have expired.

**Store.purge()**

  Deletes all the keys by emptying the dictionary.

Some time and memory values after storing and retrieving 10 million keys
-------------------------------------------------------------------------------------

A couple of runs as a single thread.

.. code-block:: bash

  $ python use-store.py
  Storing 10,000,000 keys...
  Keys stored: 10,000,000
  Milliseconds per key: 0.001250524640083313
  Bytes used by store: 335,544,424
  Bytes used per key: 33.5544424
  Retrieving 10,000,000 keys...
  Milliseconds elapsed to retrieve each key: 0.0007979944467544556

.. code-block:: bash

  $ python use-store.py
  Storing 10,000,000 keys...
  Keys stored: 10,000,000
  Milliseconds per key: 0.0013451412439346314
  Bytes used by store: 335,544,424
  Bytes used per key: 33.5544424
  Retrieving 10,000,000 keys...
  Milliseconds elapsed to retrieve each key: 0.0008334815740585328

And here the results from running use-store-multi.py, which separates the 10 million keys in different blocks of keys to run in multiple threads (the current version is hardcoded to five threads for demonstration purposes).

.. code-block:: bash

  # Retrieving 10,000,000 keys in multiple threads...
  # Milliseconds elapsed to retrieve each key in 5 threads: 0.0008087094783782959

  # Retrieving 10,000,000 keys in multiple threads...
  # Milliseconds elapsed to retrieve each key in 500 threads: 0.0008524939060211181

  # Retrieving 10,000,000 keys in multiple threads...
  # Milliseconds elapsed to retrieve each key in 5000 threads: 0.0008140542030334473


Performance and memory usage
-------------------------------------------------------------------

As I'm using a hash table, that's what a Python dictionary is, the amortized worst case is O(n) and the average case is O(1).

The Store class is not considering the times when a key is accessed but it could be improved to do that and take advantage of a least-recently-used (LRU) algorithm.

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
