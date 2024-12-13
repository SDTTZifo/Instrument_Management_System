<?php
$memcached = new Memcached();
$memcached->addServer('localhost', 11211); // Replace with your Valkey server address and port

// Test setting a value
$result = $memcached->set('test_key', 'test_value', 60); // key, value, expiration time in seconds
if ($result) {
    echo "Successfully set a value in the cache.\n";
} else {
    echo "Failed to set a value in the cache.\n";
}

// Test getting the value
$value = $memcached->get('test_key');
if ($value) {
    echo "Successfully retrieved the value from the cache: $value\n";
} else {
    echo "Failed to retrieve the value from the cache.\n";
}
?>
