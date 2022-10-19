import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Interface {

    JFrame janelaPrincipal;

    public void iniciaPrograma(){
    //Criando a janela Principal
    JFrame janelaPrincipal = new JFrame();//Criado Objeto da Janela
    this.janelaPrincipal = janelaPrincipal;
    janelaPrincipal.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Definido como ira fechar
    janelaPrincipal.setSize(500, 100); // Tamanho da Janela

    botoesTela();
    janelaPrincipal.setVisible(true);
    }

    public void fechaPrograma(){
    janelaPrincipal.setVisible(false);
    }

    public void botoesTela() {
        JButton botaoSelecionar_arquivo = new JButton("Escolher o Arquivo");
        janelaPrincipal.add(botaoSelecionar_arquivo);
        JFileChooser fcEscolhe_arquivo = new JFileChooser();
        botaoSelecionar_arquivo.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent listaRamais_clicado)
            {
                fcEscolhe_arquivo.showSaveDialog(null);
            }
        });
    }


}