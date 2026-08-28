# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d5ae9d7-f870-3271-a1e4-888ed70f3df0 | -26.1028 | -53.13659 | 2026-08-28 17:22:00 | NPP-375 | FRANCISCO BELTRÃO | PARANÁ | Brasil | 4108403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0c7b028b-d9fc-3428-9e65-cb329a5fe686 | -27.82322 | -51.83522 | 2026-08-28 17:22:00 | NPP-375 | SÃO JOÃO DA URTIGA | RIO GRANDE DO SUL | Brasil | 4318424 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 14367d78-1e06-37d5-aee5-945ddadd779e | -27.39866 | -52.00026 | 2026-08-28 17:22:00 | NPP-375 | ALTO BELA VISTA | SANTA CATARINA | Brasil | 4200754 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 71a440e5-3805-3d4a-ab9b-815188b26a56 | -26.68914 | -51.45459 | 2026-08-28 17:22:00 | NPP-375 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c82e5422-5526-3e3e-86c9-85c39e2f2ffb | -26.73211 | -51.56659 | 2026-08-28 17:22:00 | NPP-375 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d8ed0b07-b318-3943-9d0e-af577e38a7b3 | -26.91603 | -51.67595 | 2026-08-28 17:22:00 | NPP-375 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 148.4 |
| 7d6efe72-171d-3087-86f5-92e2086208eb | -28.10821 | -49.01356 | 2026-08-28 17:22:00 | NPP-375 | SÃO MARTINHO | SANTA CATARINA | Brasil | 4217105 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 24442c02-38fe-3fc3-931b-016c09c84265 | -27.2778 | -50.6559 | 2026-08-28 17:22:00 | NPP-375 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9d087133-cf51-3064-bb2d-421743a9d6e2 | -26.05228 | -51.59729 | 2026-08-28 17:22:00 | NPP-375 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| a867e330-ba52-3c81-9bf4-3cf1034ec698 | -26.84089 | -51.02505 | 2026-08-28 17:22:00 | NPP-375 | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 974c493c-6b1f-3555-9a6e-647e93855a3e | -25.07291 | -48.58057 | 2026-08-28 17:22:00 | NPP-375 | CAMPINA GRANDE DO SUL | PARANÁ | Brasil | 4104006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5d602e57-06a6-3753-9be9-8d1ef7aa7c94 | -25.22201 | -52.47429 | 2026-08-28 17:22:00 | NPP-375 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 80aec39c-65ae-3f9d-9b12-dd4eb10e1d20 | -25.18222 | -49.17118 | 2026-08-28 17:22:00 | NPP-375 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 68f835cc-2d89-350f-b741-350aa9ce1061 | -24.67043 | -49.58048 | 2026-08-28 17:22:00 | NPP-375 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| d0903004-cf96-3890-8640-748a48dc355d | -27.18678 | -52.86639 | 2026-08-28 17:22:00 | NPP-375 | RIO DOS ÍNDIOS | RIO GRANDE DO SUL | Brasil | 4315552 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6fca65dd-f031-33c8-abe1-0802cd0151b5 | -25.68276 | -51.57603 | 2026-08-28 17:22:00 | NPP-375 | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b3c4d9b0-6640-3855-9b63-3384a845775e | -26.05168 | -51.59343 | 2026-08-28 17:22:00 | NPP-375 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 7f6df204-c8e5-3f48-bdcc-d5407c49527a | -25.09144 | -51.06936 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 5fd0ee2f-c155-3259-be9b-3b324d8a67e2 | -27.45519 | -53.59846 | 2026-08-28 17:22:00 | NPP-375 | ERVAL SECO | RIO GRANDE DO SUL | Brasil | 4307302 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 751b751d-09b4-37ae-8716-4120cfb73181 | -26.47436 | -51.39193 | 2026-08-28 17:22:00 | NPP-375 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b0656d0f-1bf4-3a56-8b80-85d22d00ee4e | -24.39234 | -49.04761 | 2026-08-28 17:22:00 | NPP-375 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 92e76640-b0bf-38f5-90cf-2925fa8e3b3c | -27.82656 | -51.83458 | 2026-08-28 17:22:00 | NPP-375 | SÃO JOÃO DA URTIGA | RIO GRANDE DO SUL | Brasil | 4318424 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 9f5b18f9-246a-35e5-aaca-020bdc727078 | -26.92875 | -51.58119 | 2026-08-28 17:22:00 | NPP-375 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b180077f-44a0-3f31-8ed0-5510d0cd5ab9 | -26.50019 | -51.51132 | 2026-08-28 17:22:00 | NPP-375 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 957e1e8a-cde6-32d1-bbd2-755ad9621b3f | -26.46485 | -51.71043 | 2026-08-28 17:22:00 | NPP-375 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0e700cb4-823b-3bf9-82fa-8b4a596a1df9 | -25.49753 | -50.48174 | 2026-08-28 17:22:00 | NPP-375 | FERNANDES PINHEIRO | PARANÁ | Brasil | 4107736 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| a4b11955-22df-32ff-8fff-f87991cd161c | -27.32322 | -52.89439 | 2026-08-28 17:22:00 | NPP-375 | NONOAI | RIO GRANDE DO SUL | Brasil | 4312708 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| f623d431-fdc1-34d1-b294-e7329b93923c | -26.58564 | -52.79721 | 2026-08-28 17:22:00 | NPP-375 | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7d845fdd-b105-3ea7-b0db-a725a6eb48a3 | -25.03295 | -51.20241 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 3a4accd9-3035-3c17-b942-9c8e220748c2 | -27.27715 | -50.65191 | 2026-08-28 17:22:00 | NPP-375 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| aedc60f8-472c-32cb-b457-a3105a7f5d1a | -24.78855 | -49.5706 | 2026-08-28 17:22:00 | NPP-375 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 37263b20-0457-332c-a583-391d52ee7c65 | -24.90281 | -51.26339 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8cdeb507-fe53-3a0a-9026-cfbe2f43d08a | -25.91486 | -50.63738 | 2026-08-28 17:22:00 | NPP-375 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 2fe8ee59-ad03-36e1-b36c-af2aad4833ac | -25.65951 | -50.78243 | 2026-08-28 17:22:00 | NPP-375 | RIO AZUL | PARANÁ | Brasil | 4122008 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0f3a7d46-2b5c-3e27-a301-d91e7e418666 | -26.97649 | -51.05933 | 2026-08-28 17:22:00 | NPP-375 | RIO DAS ANTAS | SANTA CATARINA | Brasil | 4214409 | 42 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 62281881-cafc-3337-8cc3-da3c1ad29ac9 | -25.03235 | -51.20232 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| e6451c6d-673f-3ed9-9345-424275d8b1a2 | -26.58229 | -52.79782 | 2026-08-28 17:22:00 | NPP-375 | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| fa546066-8c20-3abe-a7a0-a9ae949c6bc2 | -27.88072 | -50.94985 | 2026-08-28 17:22:00 | NPP-375 | CERRO NEGRO | SANTA CATARINA | Brasil | 4204178 | 42 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 4bb86dd3-a4aa-3fc3-8481-e0c29cdd625f | -26.73545 | -51.56594 | 2026-08-28 17:22:00 | NPP-375 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d8adb70d-5dae-3fb0-9bb8-00a08b994834 | -25.83311 | -51.6669 | 2026-08-28 17:22:00 | NPP-375 | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 89964715-805a-39dc-af07-f38b987b720d | -27.47122 | -49.18007 | 2026-08-28 17:22:00 | NPP-375 | MAJOR GERCINO | SANTA CATARINA | Brasil | 4210209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| f708da4c-b3a9-33ff-b5fb-edbf0aa41b65 | -25.32115 | -49.45066 | 2026-08-28 17:22:00 | NPP-375 | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6a3a9bd3-5d7b-3e6e-88f9-765b682db86a | -25.9154 | -50.637 | 2026-08-28 17:22:00 | NPP-375 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| e97e2649-76e3-3d1f-886d-1b45b49b900b | -25.7704 | -51.35881 | 2026-08-28 17:22:00 | NPP-375 | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| b9da8f8f-159e-346e-b341-08d2aaf54926 | -26.10616 | -53.13597 | 2026-08-28 17:22:00 | NPP-375 | FRANCISCO BELTRÃO | PARANÁ | Brasil | 4108403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b681522e-8443-3614-867f-c02e61f29a0f | -24.90398 | -51.05666 | 2026-08-28 17:22:00 | NPP-375 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 59ee1191-273b-3b91-9863-25ddc370348e | -26.47771 | -51.39128 | 2026-08-28 17:22:00 | NPP-375 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| f79be237-0024-3cf2-9597-05206b2a6b6b | -27.81079 | -50.40783 | 2026-08-28 17:22:00 | NPP-375 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2aec4e30-9d74-3a46-af39-4a9fc76c7320 | -26.38169 | -53.67311 | 2026-08-28 17:22:00 | NPP-375 | DIONÍSIO CERQUEIRA | SANTA CATARINA | Brasil | 4205001 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 93a0ebb0-e6b0-391d-a749-c9a7e38c3805 | -28.14506 | -49.18582 | 2026-08-28 17:22:00 | NPP-375 | RIO FORTUNA | SANTA CATARINA | Brasil | 4214904 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 90920dd6-6e7e-3697-9ba2-9ba0f964a112 | -27.26668 | -51.26123 | 2026-08-28 17:22:00 | NPP-375 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 60122d70-333e-34bd-81e6-f08367c82c84 | -27.32717 | -52.89775 | 2026-08-28 17:22:00 | NPP-375 | NONOAI | RIO GRANDE DO SUL | Brasil | 4312708 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| cb467f59-173b-32ae-8298-693ee846e81f | -27.79714 | -52.27634 | 2026-08-28 17:22:00 | NPP-375 | EREBANGO | RIO GRANDE DO SUL | Brasil | 4306973 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6648d665-cf52-3e7c-81cb-6de3840e7113 | -25.46007 | -51.29838 | 2026-08-28 17:22:00 | NPP-375 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 3d33164b-9d22-3d05-8bed-37be3c38b082 | -25.28581 | -50.8469 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fec29317-b753-372a-a2ee-6f7ef2781177 | -24.87624 | -51.29262 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 2d831b54-c3ab-32ed-9012-9b329c73a1a3 | -26.33482 | -52.33567 | 2026-08-28 17:22:00 | NPP-375 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 84f08e7a-5a7c-3c93-a95d-2260f50781a1 | -27.83102 | -51.3658 | 2026-08-28 17:22:00 | NPP-375 | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 21b10e6a-f2d3-3f97-a064-902e520113dd | -27.26334 | -51.26189 | 2026-08-28 17:22:00 | NPP-375 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 4d0cc634-9260-3b22-9726-049e4e99844b | -25.90333 | -51.44988 | 2026-08-28 17:22:00 | NPP-375 | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b82c940b-8690-3141-ad4c-5a2c829b3f0f | -26.632 | -51.02545 | 2026-08-28 17:22:00 | NPP-375 | CALMON | SANTA CATARINA | Brasil | 4203154 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 38cdc8f6-e9d5-369d-a5cb-b9846367d809 | -24.87575 | -51.20379 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c816829c-42fb-3f7d-af16-cd9cd3d87d84 | -27.81014 | -50.40382 | 2026-08-28 17:22:00 | NPP-375 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 6724c24c-223f-3dcb-a676-4b60d204261f | -25.6402 | -50.49543 | 2026-08-28 17:22:00 | NPP-375 | FERNANDES PINHEIRO | PARANÁ | Brasil | 4107736 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0be79ba8-448b-3011-9379-88c22657f050 | -26.21798 | -51.42922 | 2026-08-28 17:22:00 | NPP-375 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 735a5bb8-b90b-3db9-a5ad-0dcd0c3f624e | -25.18476 | -51.1284 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| d62c1e19-312e-337c-a45a-56d942df206a | -27.79201 | -50.84922 | 2026-08-28 17:22:00 | NPP-375 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b6852412-032c-3263-9943-74f715c28da4 | -26.33087 | -53.07961 | 2026-08-28 17:22:00 | NPP-375 | MARMELEIRO | PARANÁ | Brasil | 4115408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| f3a77509-e721-3f33-ae65-34f725f75431 | -27.05241 | -49.47946 | 2026-08-28 17:22:00 | NPP-375 | IBIRAMA | SANTA CATARINA | Brasil | 4206900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 03fd4011-ca41-3732-9ddf-b3fdf02b0c87 | -25.86701 | -50.68399 | 2026-08-28 17:22:00 | NPP-375 | RIO AZUL | PARANÁ | Brasil | 4122008 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5ec7bbb2-4e23-371f-a1b0-c5ab37feb94b | -27.25386 | -51.15856 | 2026-08-28 17:22:00 | NPP-375 | IBIAM | SANTA CATARINA | Brasil | 4206751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d07c8014-6596-347f-8052-1589a77a1257 | -26.3821 | -53.67262 | 2026-08-28 17:22:00 | NPP-375 | DIONÍSIO CERQUEIRA | SANTA CATARINA | Brasil | 4205001 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a02e3649-8df2-3d1b-8943-3b4953c5cee2 | -25.49411 | -50.48243 | 2026-08-28 17:22:00 | NPP-375 | FERNANDES PINHEIRO | PARANÁ | Brasil | 4107736 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| b0e2d407-3390-335a-923f-7141ba1463c1 | -27.71658 | -50.99068 | 2026-08-28 17:22:00 | NPP-375 | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 70582c43-4143-3a94-86f9-80244b0bb8c5 | -24.96565 | -52.61545 | 2026-08-28 17:22:00 | NPP-375 | DIAMANTE DO SUL | PARANÁ | Brasil | 4107124 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f066b20e-9791-3aea-8926-916e53f0796a | -25.66076 | -50.47043 | 2026-08-28 17:22:00 | NPP-375 | REBOUÇAS | PARANÁ | Brasil | 4121505 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2679dff1-8c0c-3b05-a8dc-0c4417b95043 | -25.3176 | -49.45139 | 2026-08-28 17:22:00 | NPP-375 | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 0058ce3c-5025-3c79-a546-81a5a2c78abd | -25.8694 | -50.30303 | 2026-08-28 17:22:00 | NPP-375 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 33c45439-c7d1-3d1e-b058-9d7c0917b462 | -25.91474 | -50.63298 | 2026-08-28 17:22:00 | NPP-375 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9377429b-d82e-3db3-a9d0-14853b0301ae | -27.47198 | -49.18444 | 2026-08-28 17:22:00 | NPP-375 | MAJOR GERCINO | SANTA CATARINA | Brasil | 4210209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 38d425bc-ed93-3583-ae9d-d0c5b1112ac3 | -27.04254 | -52.75882 | 2026-08-28 17:22:00 | NPP-375 | GUATAMBÚ | SANTA CATARINA | Brasil | 4206652 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| de3cdebb-3c1b-3204-89df-887164b1120d | -25.69639 | -49.07255 | 2026-08-28 17:22:00 | NPP-375 | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f9e2d8bd-ad64-3b50-8184-5d452e2d3c1f | -27.12468 | -50.46687 | 2026-08-28 17:22:00 | NPP-375 | PONTE ALTA DO NORTE | SANTA CATARINA | Brasil | 4213351 | 42 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 372dd39d-6c7e-337d-9f44-9d36aaa4cf88 | -25.07661 | -48.5798 | 2026-08-28 17:22:00 | NPP-375 | CAMPINA GRANDE DO SUL | PARANÁ | Brasil | 4104006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ca253f90-4d9c-301b-addf-0e87c88a700c | -24.81219 | -51.13497 | 2026-08-28 17:22:00 | NPP-375 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| f1f05363-da7c-359a-bb18-3213c93affe6 | -26.7529 | -52.0862 | 2026-08-28 17:22:00 | NPP-375 | VARGEÃO | SANTA CATARINA | Brasil | 4219101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 8c6cb64e-72d8-3d3c-a3b3-9ac7e9ccbbcb | -24.67121 | -49.58487 | 2026-08-28 17:22:00 | NPP-375 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 4975a090-8a31-39a3-977d-28f59f5cae29 | -26.64886 | -51.08698 | 2026-08-28 17:22:00 | NPP-375 | CALMON | SANTA CATARINA | Brasil | 4203154 | 42 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| d7c8a226-67e8-3a95-87bf-c8cc77bbb90b | -25.02769 | -50.09771 | 2026-08-28 17:22:00 | NPP-375 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a7bda2e8-e54f-30df-bef0-ba1d1ef613b3 | -24.91397 | -51.28942 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8cb8c6d3-4e20-3c0f-814b-5cce7c4a8e8f | -24.96903 | -51.80723 | 2026-08-28 17:22:00 | NPP-375 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| df77b888-5a9a-35ee-b65b-12c6799fc27e | -27.83435 | -51.36514 | 2026-08-28 17:22:00 | NPP-375 | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| db1709d6-10f8-3c1e-beba-ca1b7523bb84 | -27.79079 | -50.84923 | 2026-08-28 17:22:00 | NPP-375 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c5462470-116b-3145-af4f-7f20663308a8 | -28.08861 | -50.0786 | 2026-08-28 17:22:00 | NPP-375 | PAINEL | SANTA CATARINA | Brasil | 4211892 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| fdf6c800-05b8-3e01-8dc3-2e895ee286cc | -27.03037 | -51.85004 | 2026-08-28 17:22:00 | NPP-375 | IRANI | SANTA CATARINA | Brasil | 4207809 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| ca174200-5011-32b4-9a25-1e658bc5ae9b | -25.91419 | -50.63336 | 2026-08-28 17:22:00 | NPP-375 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 8a4d711a-80ef-3781-a37f-580977323be7 | -27.34519 | -53.02096 | 2026-08-28 17:22:00 | NPP-375 | PLANALTO | RIO GRANDE DO SUL | Brasil | 4314704 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| bb055018-b695-3991-98f6-ddcfce46f636 | -26.47708 | -51.38737 | 2026-08-28 17:22:00 | NPP-375 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| 4c8e30b3-5e0d-3855-bd02-1c9ec824fc99 | -25.14555 | -51.38306 | 2026-08-28 17:22:00 | NPP-375 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 982cdc19-d64d-32dd-9b1a-581ec23f6ec9 | -25.92709 | -51.70906 | 2026-08-28 17:22:00 | NPP-375 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |


[Clique aqui para ver as próximas entradas](README104.md)
