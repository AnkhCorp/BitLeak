require 'watir'

RED    = "\e[31m"
GREEN  = "\e[32m"
YELLOW = "\e[33m"
RESET  = "\e[0m"

ascii_art = <<-'EOF'
          O
         _|_           BitLeak 1.0
   ,_.-_' _ '_-._,     by: AnkhCorp
    \ (')(.)(') /
 _,  `\_-===-_/`  ,_
>  |----"""""----|  <
`""`--/   _-@-\--`""`
     |===L_I===|
      \       /
      _\__|__/_
     `""""`""""`
EOF

puts "#{GREEN}#{ascii_art}#{RESET}"

def main
  print "Digite o endereço IP: "
  torrent = gets.chomp
  url = "https://iknowwhatyoudownload.com/en/peer/?ip=#{torrent}"

  # Inicia o navegador
  browser = Watir::Browser.new(:chrome, headless: true)

  # Acessa a URL
  browser.goto(url)

  # Aguarda até que a tabela esteja presente (máximo de 10 segundos)
  begin
    Watir::Wait.until(timeout: 1000) { browser.table(class: /table-condensed/).exists? }

    # Localiza a tabela e imprime o texto
    table = browser.table(class: /table-condensed/)
    puts table.exists? ? table.text : "Tabela não encontrada."
  rescue Watir::Wait::TimeoutError
    puts "Tempo esgotado. A tabela não foi encontrada."
  rescue => e
    puts "Erro: #{e.message}"
  ensure
    browser.close
  end
end

main if __FILE__ == $0
