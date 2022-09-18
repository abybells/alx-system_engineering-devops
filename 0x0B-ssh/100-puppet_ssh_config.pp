# set up your client SSH configuration file using Puppet

file_line { 'Declare identity file':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'IdentityFile ~/.ssh/school',
  multiple => true,
}
file_line { 'Turn off passed auth':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'PasswordAuthentication no',
  multiple => true,
}
