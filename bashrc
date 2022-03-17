alias g='grep -i'
alias h=head
alias t=tail
alias p='ps aux'
alias ll='ls -alF --block-size="'\''1"'
alias cls='printf "\\ec"'
alias copy='xsel -ib'
alias past='xsel -ob'
alias od='od -tx1z'

export PS1='\[\e[1;33m\]$(df -h $PWD | tail -1 | awk '"'"'{print $1,$2,$5}'"'"')첸샹송\[\e[0m\]'\\w\ 

shopt -s globstar
