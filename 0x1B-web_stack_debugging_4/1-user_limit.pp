# Change the OS configuration to give permision to holberton to login without no errors msgs

exec {"update hard limit":
  command => "sed -i 's/^holberton hard nofile.*/holberton hard nofile 4096' /etc/security/limits.conf",
  provider => "shell"  
}

exec {"update soft limit":
  command => "sed -i 's/^holberton soft nofile.*/holberton soft nofile 4096' /etc/security/limits.conf",
  provider => "shell"
}
