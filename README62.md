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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a917c36c-eabc-3120-89e2-2c46ed12d020 | -1.6343 | -52.61972 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a2ab630-2634-328b-87f7-5f25e9279714 | -0.94802 | -51.72013 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dd926bf-ee7a-36ac-bff1-9c1862da732b | -1.27346 | -52.97925 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da44ddde-0dd8-3993-b4cb-7250d2bf3dc6 | -2.50471 | -49.00285 | 2024-11-22 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f06947da-a5af-3a4b-bfee-7a23b7a7da37 | -1.186 | -51.94716 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 718f702f-067a-3a69-aa3a-0923c352a2bc | -1.77273 | -53.60617 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 97f5492d-92f3-36ca-9850-0b1dd5d2a44b | -1.23808 | -51.74638 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65262229-9d33-329a-b4c9-afdde1f68670 | -1.13685 | -53.40308 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e9bea4d4-944d-3a2e-a1cd-2abe93ff25ff | -1.19019 | -51.93826 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48a881b5-03c6-37e1-9f8d-39a03e6fb5ef | -1.1848 | -51.93745 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89e00be5-e00c-341c-a6e6-d083245f8bcd | -13.2469 | -50.88367 | 2024-11-22 05:31:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5ecff42-3ac4-31fe-95e1-757069d0b1b7 | -1.30189 | -52.21884 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7cee0317-fdcc-3016-b8e3-1dbb2418ec0b | -1.44355 | -53.38138 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43e9198a-1143-3e3f-b5c3-9faf701db5bd | -1.44566 | -53.56363 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73568aba-5817-3655-8c82-a5eca8dc67f9 | -1.74751 | -56.17818 | 2024-11-22 05:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ba4926c-dfc9-3abd-a368-1da298787cce | -1.20504 | -54.0342 | 2024-11-22 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5cf9b8ab-c237-3614-b2d1-633386624a45 | -1.20899 | -51.74644 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 248e0e89-ec4e-3a92-a30c-2132b5654234 | -1.61145 | -52.58485 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7ca6f2fc-f4c1-3d1b-83f8-f25b93f00c30 | -1.19935 | -51.9501 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8deef0aa-d89c-3711-88d6-a456e1e4e45e | -1.23188 | -51.74288 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b9d93c94-654e-31c1-8890-da9b13baf505 | -1.12715 | -53.40143 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 852d4e26-7734-3874-8749-cb8c73f77ed7 | -1.2001 | -51.96332 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6758e0b7-cc0e-351a-bab8-2c4bd5f956f5 | -0.26995 | -51.57609 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 405db7a6-4e63-3d95-9144-4c87cd40c2a7 | -1.71743 | -52.49138 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efec61cd-e15b-306f-8a7f-37d452efd29b | -13.25365 | -50.88452 | 2024-11-22 05:31:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f844dfde-d90c-3824-ac8f-99f3faaeafe2 | -1.13603 | -53.40842 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2faf996e-9181-3371-8544-2378185a5588 | -0.86699 | -51.89066 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8366295a-cb0f-33cb-9484-882409c7562e | -1.63993 | -52.61744 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18d495ae-2c66-3ee4-b151-034332f2edbe | -2.00793 | -54.524 | 2024-11-22 05:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee5881ca-8737-3014-9402-e6341170761b | -1.19882 | -51.95349 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8c9b085c-a6d4-3032-b32f-77bb6a6de577 | -1.27849 | -52.97993 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05a9747e-51e6-35c4-93ee-e664ccef40ca | -1.57797 | -52.92998 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8669e729-5af5-382d-b869-792e86d2b7b1 | -2.07956 | -50.31619 | 2024-11-22 05:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38f60b9d-21f7-32d2-a6d3-35161d4825ad | -0.94259 | -51.71927 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d5298a5-788a-3d34-b3cf-428c40c10a7a | -1.20614 | -53.68589 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 84413b01-9a35-36ab-9e17-2c224e4b8576 | -0.91737 | -52.69275 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68e381ad-2597-3c92-a33a-3b81b93e3468 | -1.61871 | -53.27047 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf384081-8584-36a4-b3cc-bca2f322a6e8 | -0.26919 | -51.5346 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8f53327-e530-387f-9943-2ed30d63588f | -1.94041 | -49.52544 | 2024-11-22 05:31:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 050ef9d9-0b87-3815-90aa-a4f164db2a58 | -11.99407 | -57.20304 | 2024-11-22 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8d800f3-3451-313e-93f3-3faba79496e1 | -1.21518 | -51.97267 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c62376d2-fe94-348f-a623-4124d680815f | -1.61615 | -52.58878 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e7e5159-8e71-364a-97c9-376bc6e8d937 | -1.52614 | -55.37828 | 2024-11-22 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a081db87-58e3-3a53-a82c-62d0ac0c1236 | -1.19676 | -51.94883 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f9474d8-9bb1-364d-9db4-8f7b98ff7817 | -1.12147 | -53.40602 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 52dbc824-ab81-3cb3-ba05-7382901cc38c | -2.07714 | -50.32407 | 2024-11-22 05:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c28157cf-d0b5-31d1-8390-d59ddf1e4bd0 | -1.23316 | -51.74199 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef76c9b1-15a6-3372-b836-e5793f6ffa79 | -1.29083 | -52.46713 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0939f53e-90b3-368d-831a-62ef52246dfd | -1.19138 | -51.94798 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b31b9f1-6dc3-331a-ac0a-7ac065c4e551 | -0.92364 | -51.7341 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16e3886d-b119-354c-b6a8-60afe8e5e85f | -1.63901 | -52.62365 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 796d8091-7967-369e-a53e-af030ddfe63f | -1.65789 | -52.67413 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f973a81-2b38-3216-a4b1-2453852e104a | -1.73344 | -52.71108 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bc0ad76b-5a53-350b-9864-37a2c4787573 | -2.07783 | -50.31952 | 2024-11-22 05:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ce71a90-c95f-330d-ba88-ed4e7f183bdb | -1.19451 | -51.94586 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a286b60a-6d43-3846-98c7-96c87e944d7b | -1.26653 | -52.06709 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a9d48c6-c551-3a07-8b53-fe6849c119b3 | -1.26084 | -53.36225 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 266ade98-bfb4-37e5-ab8a-c92ccc82bd43 | -1.51154 | -53.1339 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f04825c5-488d-3613-af0c-9f73aa28f4f7 | 0.97236 | -60.40485 | 2024-11-22 05:31:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d854683-7a4a-3fde-b034-91725cc1f5fb | -1.22225 | -51.74024 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 455335cb-de2d-3947-b66a-945cf61430e9 | -1.12633 | -53.4068 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a140f484-1287-3c7c-9d74-af6867162a18 | -1.74407 | -52.38726 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d40cdf92-a350-36e7-bbd0-5d00662d8f68 | -1.19087 | -51.9514 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02d99bc3-2c71-32de-97fa-9d1ef28985af | -1.30139 | -52.22211 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 975e3edb-6b7c-39fc-b881-dbef788613e8 | -1.22841 | -55.81432 | 2024-11-22 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98e2dc02-20d8-379d-9ae1-806f58791b5a | -1.5784 | -52.92704 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a5dbb35-d6fd-32de-be34-0bb8dee9d9d4 | -1.7267 | -52.70695 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7a62b52e-500d-3e57-a427-c5f5aee4a9f4 | -1.04614 | -51.74357 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0564f304-7a82-30bf-838b-873b795f7626 | -0.18762 | -51.55721 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d26bdcd-c406-3847-94a8-ccbacf6b9a63 | -1.44681 | -53.3929 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 72891d99-9e61-3ad0-aa2b-569268992bff | -13.25113 | -50.8856 | 2024-11-22 05:31:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc660380-c24c-375d-86c1-4709d6ac3981 | -0.954 | -51.7175 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fc72b8b1-c70b-31d4-a8f1-5bc826bbf35f | -1.59396 | -53.81286 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5c8ff091-320a-3136-86b2-99d7645e8b12 | -1.11742 | -53.3999 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 1489786c-3f6a-3bc4-bcd3-e2f6eef8f139 | -11.98967 | -57.20234 | 2024-11-22 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 117b4cef-334f-32f8-a2c2-0963cb57d3c1 | -1.2583 | -51.76038 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62348a69-4b64-34c0-a2f0-f37257259da7 | -3.8719 | -52.3589 | 2024-11-22 05:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6c7c7da0-3fbf-3a70-bf88-87ca956d246c | -3.8535 | -52.3596 | 2024-11-22 05:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 59811870-0da7-3aa2-9a7a-b41fbacfce46 | -3.2569 | -54.2426 | 2024-11-22 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| aadefe17-38b8-3539-96a3-3861129ed2b3 | -3.2385 | -54.2431 | 2024-11-22 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 862a90f6-4bf8-3135-87d3-06c8c3828fd3 | -3.2384 | -54.2632 | 2024-11-22 05:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| e09426f2-a049-3512-935c-969640dcc717 | -3.5159 | -53.8132 | 2024-11-22 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b2571b1e-7cef-34b6-a5cb-8e3413c5aecb | -3.22 | -54.2636 | 2024-11-22 05:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f163c071-f997-310b-9eeb-c7f97387737a | -3.2768 | -53.8199 | 2024-11-22 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d74f61ed-f040-3ae9-be81-4c6b59ce5c88 | -3.2201 | -54.2436 | 2024-11-22 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| f3e4afcb-99f2-331e-97b5-e414b503ea17 | -1.1287 | -53.3951 | 2024-11-22 05:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 07a0278a-aa78-3d77-b4b7-9c273bd53c55 | -3.516 | -53.793 | 2024-11-22 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 39da7047-c6af-3f1f-900b-6cf021593206 | -3.2386 | -54.223 | 2024-11-22 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3b001529-2598-39b7-90c5-a5c2353bc7e3 | -1.1287 | -53.3951 | 2024-11-22 05:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 81c8518c-2732-39d5-895b-6ce53c39a32f | -3.2569 | -54.2426 | 2024-11-22 05:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a92c6536-a64f-34ba-9dbc-86ced97ed6a5 | -3.2201 | -54.2436 | 2024-11-22 05:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| f112b381-4fc1-3724-9b5a-95f0237d1b14 | -3.2768 | -53.8199 | 2024-11-22 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9d97f6bd-f038-3cd7-9c44-87994018421e | -3.8535 | -52.3596 | 2024-11-22 05:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 8438c13d-eea4-3541-8f78-d4ec5bf66ef3 | -3.2386 | -54.223 | 2024-11-22 05:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| e1fcf180-9028-310c-8e79-ed01abb0c6e6 | -3.2384 | -54.2632 | 2024-11-22 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| fa3951ae-9cb0-3f94-8c21-5d0296d926e8 | -3.8719 | -52.3589 | 2024-11-22 05:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b42bae0e-f040-37b0-83a9-86cc18d812c0 | -3.2385 | -54.2431 | 2024-11-22 05:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 28351aeb-df4f-3d39-aa63-cce51788af4c | 3.56754 | -60.08883 | 2024-11-22 05:50:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1854f578-708a-3cc0-96db-8bb1ceff78d8 | -3.27886 | -53.84315 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9dee8a3-b96d-37f3-aa80-40000ff80055 | -3.28094 | -53.8287 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README63.md)
