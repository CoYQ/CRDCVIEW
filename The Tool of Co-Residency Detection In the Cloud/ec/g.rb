#!/usr/bin/ruby

dom_id=nil
(1..65535).each do |i|
	if system("xenstore-ls /local/domain/#{i} > /dev/null 2>&1")
		dom_id=i
		break
	end
end

$stdout.puts("#{dom_id}")
