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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3867f65a-0aa3-3532-a218-b48bc3a97c7d | -3.2416 | -53.3764 | 2024-11-01 04:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 2107ceb4-7f85-37e9-bc28-f76dc6a47706 | -3.5631 | -47.3847 | 2024-11-01 04:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1096c86c-52ee-312d-b7c1-930d4191b80a | -4.3867 | -43.4757 | 2024-11-01 04:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 93a49020-07c7-3f89-bbb4-ef75abeeb71e | -4.4054 | -43.4746 | 2024-11-01 04:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| a5f5d7bd-1fe4-3546-a1ef-7b6060f714d4 | -6.1041 | -43.9593 | 2024-11-01 04:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ccdbeef4-cb6c-3570-b63d-a90acc8363a6 | -6.1229 | -43.9578 | 2024-11-01 04:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 73c75c83-22c2-3b37-a4fb-9f50e1a0735b | -9.9186 | -64.8246 | 2024-11-01 04:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 5d09c407-369e-3bb9-8631-4e84a45f9f65 | -9.9187 | -64.8058 | 2024-11-01 04:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b5207e61-16a6-3341-af8d-f58e45999c81 | -19.4878 | -56.6227 | 2024-11-01 04:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.1 |
| e741f788-0944-373b-a845-43f4d80bfc3b | -19.4882 | -56.6017 | 2024-11-01 04:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 1fdc0937-c471-3373-b01c-6378245e342e | -19.5079 | -56.6199 | 2024-11-01 04:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 4a317d5c-c5cb-3d34-82d1-11e33ad4d396 | -19.5083 | -56.5989 | 2024-11-01 04:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| dc61b3f4-242d-3d01-a613-a7419e500123 | -19.5087 | -56.5779 | 2024-11-01 04:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.3 |
| e5f842ed-e70d-3ed0-862f-66766075cb87 | -3.0353 | -49.4901 | 2024-11-01 05:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5d51be9c-b9b5-3e44-8ba0-86580a25622a | -3.0354 | -49.4688 | 2024-11-01 05:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c7730a05-50c2-3f1b-9ab0-f2bdf0909b27 | -3.0538 | -49.4895 | 2024-11-01 05:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1904647d-cad2-31f3-a0b7-b445cdce1e81 | -3.0539 | -49.4683 | 2024-11-01 05:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| fef116a0-59a8-3535-9f7c-dba3da0a499a | -3.5631 | -47.3847 | 2024-11-01 05:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 861ce5ff-7516-385f-a457-ec33376e2abe | -4.4054 | -43.4746 | 2024-11-01 05:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| fd48a24b-cb1c-35c7-a3a5-5a47f8bffd1b | -9.9186 | -64.8246 | 2024-11-01 05:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 33fece7f-7361-3051-a39e-8c391f11cba0 | -9.9187 | -64.8058 | 2024-11-01 05:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a7d407f5-c19f-3604-bb38-4551ab0a4aad | -3.1924 | -44.31219 | 2024-11-01 05:08:00 | AQUA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 01b05d63-dfeb-3d9c-836e-08b8d9f338ca | -3.19094 | -44.3219 | 2024-11-01 05:08:00 | AQUA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2e91fbc8-4e82-3e98-ba93-289dd0dd1a4d | -3.14564 | -45.38036 | 2024-11-01 05:08:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6f78588f-bc1f-3ab3-913a-0d1870db7b13 | -3.05296 | -49.47075 | 2024-11-01 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d3fbb891-3805-3e94-89c5-5e633a24cec0 | -3.04954 | -49.49302 | 2024-11-01 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 18a28455-cf98-30de-b5c7-68f10af81622 | -3.04807 | -49.47509 | 2024-11-01 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e0274841-f5ef-39b3-9dfc-73ecc256943b | -3.03942 | -49.46864 | 2024-11-01 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 5b38a967-9390-3d2b-b677-b284855b3814 | -3.03596 | -49.49093 | 2024-11-01 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| c6d6b865-e839-3433-9e96-a2b888a40e54 | -2.91118 | -48.60443 | 2024-11-01 05:08:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 557a5cbb-b75d-3c75-b353-bea8924f03f9 | -2.91028 | -48.61153 | 2024-11-01 05:08:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 09807a44-ff04-32ed-a7f5-8e3d76f46cc0 | -2.8122 | -49.75135 | 2024-11-01 05:08:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 296d49c8-840e-34c3-af93-517025477785 | -2.80496 | -49.21083 | 2024-11-01 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| eec465c1-2125-3594-a2d1-f33c2978db81 | -2.77421 | -48.63756 | 2024-11-01 05:08:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9665582d-15c9-3598-85a0-be60f5ea8e1d | -2.3236 | -48.82862 | 2024-11-01 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 09c99fb5-85a6-3625-806d-d2e317ec2e10 | -2.17189 | -48.7101 | 2024-11-01 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 4409908c-6047-3676-b322-68d56a43857e | -2.17176 | -48.72342 | 2024-11-01 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1b9cd80b-1eec-3fc6-b17b-90e034465943 | -2.16871 | -48.73017 | 2024-11-01 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| f680b8b5-faa9-3c13-9ed6-2af4b63e45c7 | -6.53269 | -43.9586 | 2024-11-01 05:08:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 07c797c7-28a7-3982-ab3c-ec22e9f52e66 | -6.3127 | -42.03139 | 2024-11-01 05:08:00 | AQUA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 05b05d7f-2b8a-39dd-95bb-aa458fc0393c | -4.68729 | -37.79795 | 2024-11-01 05:08:00 | AQUA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 48717ec8-fb61-317d-a41c-a0615b06a315 | -4.40013 | -43.46626 | 2024-11-01 05:08:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 82e86e65-ee83-382f-882c-5c2bdc2a16a4 | -4.39878 | -43.47523 | 2024-11-01 05:08:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1283d5c4-54f3-3339-9c22-0af80b3f3aa8 | -4.39122 | -43.46496 | 2024-11-01 05:08:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 34050374-a07d-333b-8800-06a88099a937 | -4.38986 | -43.47391 | 2024-11-01 05:08:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| a2d738db-aed7-3450-94ae-b5baba0c6bb5 | -3.94506 | -41.50892 | 2024-11-01 05:08:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 39cb14f4-19ae-385d-9df2-a001e530b57e | -3.76158 | -43.53156 | 2024-11-01 05:08:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3419b37c-c04e-397b-80e8-878b0d389b7d | -3.55585 | -42.70054 | 2024-11-01 05:08:00 | AQUA_M-M | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 46765b9b-ac90-3c1b-a25b-5ae6de6be0ce | -3.42844 | -43.97046 | 2024-11-01 05:08:00 | AQUA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2fdc54cf-05e1-3d9c-bb4e-273e8e5faaee | -3.42703 | -43.97981 | 2024-11-01 05:08:00 | AQUA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 5cb86ffe-57f4-3675-b664-a1dde01a8416 | -3.41934 | -43.9691 | 2024-11-01 05:08:00 | AQUA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| eb70737e-2823-3396-9fe9-ca1688b4f9be | -3.41793 | -43.97844 | 2024-11-01 05:08:00 | AQUA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 6da9b003-7c31-3745-be56-08473118f755 | -3.39009 | -41.64041 | 2024-11-01 05:08:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ed80979b-6844-3d3d-a01f-11c6296ba7bc | -6.5387 | -44.46047 | 2024-11-01 05:08:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 67162203-b703-36d3-87e5-b01d57b5daa5 | -6.53729 | -44.46971 | 2024-11-01 05:08:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19074204-6a09-3a49-a079-54a0637490a8 | -6.52967 | -44.45907 | 2024-11-01 05:08:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2a8a3956-7b8c-3715-9528-dd3e8c1f21be | -6.05562 | -45.79542 | 2024-11-01 05:08:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6ad21d79-d615-37f3-bff2-16c772e11225 | -5.5944 | -45.1988 | 2024-11-01 05:08:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f368c169-85d7-30bf-980e-75e5783cce4a | -5.59283 | -45.2089 | 2024-11-01 05:08:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1a581851-5de1-33c6-b062-5476ef60ada4 | -5.33039 | -45.11002 | 2024-11-01 05:08:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd3c6658-d3ee-3159-becb-79ce9e036284 | -5.06954 | -44.23012 | 2024-11-01 05:08:00 | AQUA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0249d163-3a1a-3454-bfc0-a4478212d13a | -4.97344 | -44.49491 | 2024-11-01 05:08:00 | AQUA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4704cbad-a001-33bd-a0ac-85c2e98b3038 | -4.91541 | -47.03489 | 2024-11-01 05:08:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 65f259e9-782f-3197-8883-5491197b492e | -4.91325 | -47.04836 | 2024-11-01 05:08:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| db03f5bc-dc76-3fa7-88d2-f692ab058725 | -4.91137 | -47.02869 | 2024-11-01 05:08:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 70795d30-28f9-3773-ae32-35c0e7b1e7c9 | -4.90932 | -47.0421 | 2024-11-01 05:08:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| cdbd221b-89d8-3cfa-a336-0f4d9c98c6f6 | -4.72792 | -45.74628 | 2024-11-01 05:08:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5402535d-8df9-36a8-966c-2cd571df4c90 | -4.6518 | -46.31369 | 2024-11-01 05:08:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ba53e027-898e-36b4-a66f-aca15ff6e01c | -4.53953 | -45.70535 | 2024-11-01 05:08:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 26ea6b16-1620-3804-aea2-e32ca7e0ec92 | -4.53784 | -45.71643 | 2024-11-01 05:08:00 | AQUA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0b600100-d735-3020-9555-6db91b7c08a5 | -4.37061 | -46.00948 | 2024-11-01 05:08:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 64ce5c5d-fb14-3a3e-84fc-990fa34912b6 | -4.04455 | -46.0673 | 2024-11-01 05:08:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 512d5f30-750a-38dd-8e4f-6ca4c02b5e94 | -4.04272 | -46.0794 | 2024-11-01 05:08:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 29e52e00-f449-3987-9ead-c9af32584c28 | -3.93627 | -48.34416 | 2024-11-01 05:08:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 751f915d-6159-31bf-bbf7-73940613f41f | -3.9335 | -48.36195 | 2024-11-01 05:08:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6eb0acf7-f7ff-33af-ad37-1fa19e4c538a | -3.55821 | -47.37161 | 2024-11-01 05:08:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 0003a76b-8186-318b-bea5-4f666974f23c | -3.55594 | -47.38653 | 2024-11-01 05:08:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| b88c8ef0-590b-3fc8-b370-9a2494b52b2a | -9.63819 | -40.5732 | 2024-11-01 05:10:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 5c85e8c5-8079-30bb-9370-06b9250230aa | -9.63657 | -40.5847 | 2024-11-01 05:10:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 165d5b9f-0bfb-39cb-ac81-bcab60d89254 | -7.20472 | -42.17573 | 2024-11-01 05:10:00 | AQUA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| b5f8178c-a5bd-3a7f-807d-36f6153ebc4f | -7.55705 | -45.52086 | 2024-11-01 05:10:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c286e797-d88a-3078-9926-f3fac09f823c | -7.55135 | -45.51417 | 2024-11-01 05:10:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9fa8638a-6e5d-3dbe-828f-3858ba0adb8a | -19.50854 | -56.67941 | 2024-11-01 05:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 77fa8381-4956-329e-896a-0dd2ad473d5f | -19.50007 | -56.71891 | 2024-11-01 05:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 210e966d-84fd-3ad2-a543-f8bff73eeb1d | -19.49883 | -56.71095 | 2024-11-01 05:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.3 |
| 83d02bba-250e-33fe-8d27-5a06bc5d6bd4 | -19.48329 | -56.71495 | 2024-11-01 05:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 179.4 |
| b9bb5e15-e2a7-398b-bc7c-751a7d15b6ba | -19.48206 | -56.70694 | 2024-11-01 05:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.0 |
| d9f5f7d3-cbde-3b31-a627-e28fffc470ce | -17.59944 | -53.73846 | 2024-11-01 05:14:00 | AQUA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9876474f-4711-3644-9b45-c62a972cbeff | -17.59542 | -53.73248 | 2024-11-01 05:14:00 | AQUA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 29011f85-4885-3be7-982e-ffc126fa96f9 | -3.0538 | -49.4895 | 2024-11-01 05:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 0541ea49-50c9-3faa-88de-cee5cf520f3a | -3.0539 | -49.4683 | 2024-11-01 05:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9ee3558e-9d7b-340b-9900-5a51238193be | -3.0353 | -49.4901 | 2024-11-01 05:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a0bdec70-7976-39e6-b243-a9eaf586dd01 | -3.0354 | -49.4688 | 2024-11-01 05:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 62eee4a0-8eea-3389-b56b-261f6179f2a3 | -3.4321 | -43.9868 | 2024-11-01 05:15:25 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1bc19fe9-502d-3ea5-8a0b-2e39d104d943 | -6.3898 | -49.5839 | 2024-11-01 05:15:42 | GOES-16 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4b3c9402-27ca-3afe-aa5a-0b3f8dc48fd7 | -6.3899 | -49.5626 | 2024-11-01 05:15:42 | GOES-16 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 567df4ec-5717-344f-a161-7967413943cc | -9.9187 | -64.8058 | 2024-11-01 05:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 8523e835-f9ea-3ca0-be54-353e48665c21 | 3.42516 | -51.24905 | 2024-11-01 05:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 513a082e-0fc1-39d0-a950-203b1df15019 | 4.06119 | -59.88386 | 2024-11-01 05:23:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa7bb877-bc75-36c3-b248-07220006393f | 4.05782 | -59.88445 | 2024-11-01 05:23:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README44.md)
