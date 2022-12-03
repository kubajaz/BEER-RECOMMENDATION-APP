import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;

public class MyBeerForm {
    private JTextField searchField;
    private JButton searchButton;
    private JButton userButton;
    private JLabel userName;
    private JTextPane beerInfo;
    private JPanel mainPanel;
    private JLabel beerImage;
    private JScrollPane beerPane;
    private JScrollPane reviewPane;
    private JPanel reviewPanel;

    MyBeerForm() {
        ImageIcon searchIcon = new ImageIcon(getScaledImage(new ImageIcon("loupe.png").getImage(), 30, 30));
        searchButton.addActionListener(e->System.out.printf("Searching for %s!%n", searchField.getText()));
        searchButton.setIcon(searchIcon);

        ImageIcon userIcon = new ImageIcon(getScaledImage(new ImageIcon("user.png").getImage(), 30, 30));
        userButton.addActionListener(e->System.out.println("Getting user data"));
        userButton.setIcon(userIcon);

        ImageIcon beerIcon = new ImageIcon(getScaledImage(new ImageIcon("beer.png").getImage(), 200, 200));
        beerImage.setIcon(beerIcon);

        DefaultListModel beerListModel = new DefaultListModel();
        for(int i=1; i<=30; i++) {
            beerListModel.addElement(String.format("Some beer%d", i));
        }
        beerPane.getViewport().add(new JList(beerListModel));

        beerInfo.setContentType("text/html");
        beerInfo.setText("""
                <html>
                <body>

                <h1>Some beer info</h1>

                <p>Some paragraph about it</p>

                </body>
                </html>""");
        DefaultListModel reviewListModel = new DefaultListModel();
        for(int i=1; i<=30; i++) {
            reviewListModel.addElement(String.format("Some review%d", i));
        }
        reviewPanel.add(new JList(reviewListModel), BorderLayout.SOUTH);

        JFrame wndFrame = new JFrame();
        wndFrame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        wndFrame.setIconImage(new ImageIcon("beer.png").getImage());
        wndFrame.setVisible(true);
        wndFrame.setMinimumSize(new Dimension(600, 400));

        wndFrame.add(mainPanel);
    }

    private Image getScaledImage(Image srcImg, int w, int h){
        BufferedImage resizedImg = new BufferedImage(w, h, BufferedImage.TYPE_INT_ARGB);
        Graphics2D g2 = resizedImg.createGraphics();

        g2.setRenderingHint(RenderingHints.KEY_INTERPOLATION, RenderingHints.VALUE_INTERPOLATION_BILINEAR);
        g2.drawImage(srcImg, 0, 0, w, h, null);
        g2.dispose();

        return resizedImg;
    }
}
