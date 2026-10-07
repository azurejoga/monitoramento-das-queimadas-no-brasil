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

## Dados Diários - Página 251

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c169e20-1000-3d28-b52c-8e95bf48c7f3 | -3.5684 | -54.4946 | 2026-10-07 18:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 1aad269e-9c2d-3a01-90d1-d0a2cf44986a | -7.1825 | -52.6283 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| ed33b7f4-3599-3b70-a9b5-5a6cb5aa6a6c | -4.3471 | -43.8021 | 2026-10-07 18:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 8c2a15c5-76b7-3f21-9d67-a5e346ede5c3 | -9.5176 | -67.1173 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 1e344a6b-d1c2-3163-9802-565629a8e397 | -3.7166 | -54.2096 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6a335345-5c23-3cfe-947d-d8d04ab73d92 | -8.8864 | -67.4678 | 2026-10-07 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| bd0dfd42-5031-3cd6-9fe9-e69e4dcee617 | -9.5177 | -67.0987 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 0eb1c7c1-1a81-3b3f-b424-7b9c5cb3583b | -11.6946 | -43.6787 | 2026-10-07 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d4136fdb-5f98-3fdb-a8db-a33c41d4c188 | -3.2357 | -50.1805 | 2026-10-07 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 3c50652f-4242-3f7a-b2a2-804e7e5e2ed0 | -9.1362 | -65.3022 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 34ff9bc0-9742-3a45-985b-3884bdbcee87 | -11.2333 | -44.8678 | 2026-10-07 18:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 6d55a914-c15e-3d9d-ad9e-9c11bf51b015 | -3.2956 | -49.1415 | 2026-10-07 18:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| dc09ef6b-7308-3e75-a698-c182e7c6acd9 | -6.6037 | -53.0321 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 165.4 |
| c78dcbdd-0b1c-3dc6-ac01-d9688b237770 | -11.7139 | -43.6757 | 2026-10-07 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| a2d8739f-8882-337f-93a3-5b4c56b17eeb | -9.9787 | -43.502 | 2026-10-07 18:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3a1d534a-1c6a-3be1-b9fd-b7f160d14a3a | -3.5494 | -54.6552 | 2026-10-07 18:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| b58168a4-7c1e-3cc9-bb6f-720f27f15cda | -5.7659 | -42.0389 | 2026-10-07 18:40:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 195.5 |
| 00ea63ff-5c3c-3f90-a0c8-b7d02ece61e3 | -3.1114 | -53.7839 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 307.2 |
| 3721fd10-a266-3a82-b416-06cb11106705 | -6.9925 | -45.1223 | 2026-10-07 18:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| bd1f8964-bf98-3f6a-9285-a4309140573b | -5.4835 | -44.2592 | 2026-10-07 18:40:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 259.9 |
| e1d3a44a-54d5-3ef8-9fc3-c06adf2d1247 | -3.3637 | -50.4701 | 2026-10-07 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 002bda7c-b3e3-3f43-be96-7d2b122b28e5 | -5.9644 | -40.9627 | 2026-10-07 18:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 187.4 |
| f0b39b20-cd29-3976-bac0-64007dcc0caf | -6.1937 | -42.4785 | 2026-10-07 18:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 130.0 |
| 3807f1e9-c898-3d1a-b6a6-02358b48e002 | -6.8292 | -39.5472 | 2026-10-07 18:40:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 81.6 |
| a049e10a-17c0-3ce0-b576-fc037c62bcbf | -3.5061 | -51.6924 | 2026-10-07 18:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a4fc6ce3-47d7-3fde-aa83-5d3cfebd0106 | -5.4958 | -42.8413 | 2026-10-07 18:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 240.0 |
| 17de07f3-eee2-315c-87be-070cdf07bb3f | -8.5367 | -67.032 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 7af82de9-e5cb-36e7-8927-db98bfce6bf8 | 1.8768 | -55.7227 | 2026-10-07 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 59733866-da85-3594-accd-a7c43d5108d3 | -3.5678 | -54.6547 | 2026-10-07 18:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 538b106d-f2d9-3ab8-8d1a-8d1058a50ea6 | -7.9178 | -70.9245 | 2026-10-07 18:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 89.6 |
| f625fc2b-7da8-3c56-94d9-c0d3d281fad4 | -6.5852 | -53.0331 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 167.9 |
| 8a5fc0b0-b714-3e84-b03d-25d9315f8a50 | -5.8204 | -53.8457 | 2026-10-07 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| bf3b4a8b-a4e1-3dfa-8d58-bdabdf60f5f5 | -3.4947 | -50.0877 | 2026-10-07 18:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 18d17dfa-db22-361f-9328-2e35ed7e09d0 | -8.5552 | -67.0315 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 0294c8c6-2304-3ed0-a6ac-4933a590fe48 | -13.8855 | -44.1127 | 2026-10-07 18:40:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d84dcdb1-8b47-3f53-aabf-ed585f8ecfb3 | -6.6599 | -52.9675 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 7b589cde-2aeb-3de9-b323-6b86491c2a4c | -4.1367 | -54.917 | 2026-10-07 18:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 4bfa49f3-2c81-3677-90fa-50d4f1a69df2 | -3.2137 | -42.953 | 2026-10-07 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 195.8 |
| 0e8f0b1b-7809-3bd5-ba13-ed4cd7e4adce | -3.3452 | -50.4707 | 2026-10-07 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 6714a26f-52c6-38f8-b1dc-c879d74ec989 | -3.6603 | -54.512 | 2026-10-07 18:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| a3d6c9bf-5291-39e1-8e9e-7a797e4b68df | -9.3381 | -65.7442 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 28d32b88-937c-38ca-af1a-9470dadfad8e | -3.5127 | -54.6562 | 2026-10-07 18:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| f075516e-e4c5-39b1-9633-c21d4cdf2213 | 1.7672 | -55.5463 | 2026-10-07 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1043595c-1368-3bd4-bd99-f41faa6d3d31 | -3.5866 | -54.5542 | 2026-10-07 18:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 18c5815d-7a47-3570-b5a5-5e11c899a491 | 1.7121 | -55.6261 | 2026-10-07 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 781bcb50-0f1d-3905-98d1-ccd108d7b175 | -8.6292 | -67.0111 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 08f6f5dc-def0-3947-96bc-897a5263224f | -5.2473 | -50.9149 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c2b317e5-83f1-38ec-aedb-fac94481d33a | -6.1747 | -53.4224 | 2026-10-07 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f25e143d-342d-33e8-8212-4bc6daa924da | -2.6859 | -49.0539 | 2026-10-07 18:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 9f63a8f6-e128-3c70-bea7-4ac033932919 | -5.9649 | -40.914 | 2026-10-07 18:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| 1f5c56ad-85d9-388a-952d-4d913f178aae | -2.9271 | -53.9295 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| cfeff898-bb8e-3b2f-95dc-f7b7372f5dd4 | 1.6937 | -55.6461 | 2026-10-07 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| fda1a75e-8dee-3764-9fe8-4c17b0a8de35 | -2.9327 | -58.3204 | 2026-10-07 18:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 278.2 |
| 1285579b-7dfe-3121-afdf-647e997a8c90 | -5.7191 | -45.132 | 2026-10-07 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| ab1c599b-71b3-30b2-b988-da62c1f51591 | -3.195 | -42.9772 | 2026-10-07 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| c0410954-97db-3c54-890d-77ff8418f3e8 | -5.7378 | -45.1307 | 2026-10-07 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 319.4 |
| f39ccb03-8c7e-3fec-b4fc-25944d8f32e0 | -5.9584 | -43.5072 | 2026-10-07 18:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| bb127e3e-be2d-3d06-b260-2910f893196e | -3.1972 | -50.5592 | 2026-10-07 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 563.5 |
| 770020b9-16cc-3639-8e93-fbd430329478 | -3.73 | -55.486 | 2026-10-07 18:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 388df53d-b6a1-3159-9d92-70d0a6edfaa2 | -13.3671 | -43.8742 | 2026-10-07 18:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 236.9 |
| 75244fc0-2d95-3fa7-b99b-8a7b4d15b4da | -1.8011 | -57.0967 | 2026-10-07 18:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 124.7 |
| a3cf1aed-71be-329e-917b-72c53975d81d | -3.1483 | -53.7426 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ee4e22c1-a433-380f-8931-0e1d47482d9a | -3.443 | -49.2641 | 2026-10-07 18:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 69f4c32d-2a2a-3cd8-b799-8387bbf3b469 | -5.7312 | -41.7309 | 2026-10-07 18:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 412.8 |
| 3661d079-0bb0-31ff-9080-f462c4f30b8c | 1.6937 | -55.6263 | 2026-10-07 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9ae12ec3-4a7b-374d-8517-34a4278ba940 | -4.2657 | -54.8729 | 2026-10-07 18:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a45ffbb9-9a84-3d70-9323-e4a75c3c6f0a | -11.7143 | -43.652 | 2026-10-07 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| fcce175f-f2dc-391d-b610-2fc8d49f989c | -5.2682 | -47.911 | 2026-10-07 18:40:00 | GOES-19 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 5aa10ba1-46b2-3ef8-97ef-b45507dafa0c | -11.6181 | -43.6669 | 2026-10-07 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f4013d27-ae83-364a-af7b-ccbd607caf15 | -9.9589 | -43.5516 | 2026-10-07 18:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| d2410fe8-6d4f-3c8f-b7eb-73ce82e1033a | -3.203 | -53.8823 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c9eaf004-dd8f-3976-8c70-e15dd7c4ad9a | -9.5468 | -64.8196 | 2026-10-07 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.1 |
| d3fb3bb0-1730-39dc-b644-d2e5efcdec3e | -4.3045 | -50.77 | 2026-10-07 18:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 72bd20c5-3607-3dae-b404-f52eccc56af0 | -3.1951 | -42.9538 | 2026-10-07 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 239.6 |
| ae55ea88-ba5f-34de-b6f5-9d013717d0ce | -9.3394 | -65.4638 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 693821cc-ca0f-3184-b934-a5f24a53f5da | -3.1971 | -50.5801 | 2026-10-07 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 9aff5698-a368-364c-9090-ddfe77ec3085 | -6.02 | -51.7272 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| a29e75a6-8ba6-32e4-b60b-af0d9b340df9 | -4.0947 | -52.0635 | 2026-10-07 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 3bcdb110-8276-324a-9fd6-c99120ca2ed0 | -6.6784 | -52.9664 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 3e6a4fbe-7ad1-3247-a713-0b9a2566c805 | -5.9647 | -40.9383 | 2026-10-07 18:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 265.7 |
| 7c6b35d8-31b0-3d06-ac9d-d458f78c2522 | -3.7296 | -51.2086 | 2026-10-07 18:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| caa14674-9224-3923-949c-6f2ddd965756 | -5.4958 | -42.8413 | 2026-10-07 18:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 202.2 |
| 64ba4ff7-d618-3b76-aa49-d416858d24a5 | -9.0591 | -65.9396 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 65e1fa52-7872-3e56-8621-0745604e592d | -3.4947 | -50.0877 | 2026-10-07 18:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 6d7cfea2-5793-36de-997c-c26ffbbc5799 | -6.1973 | -52.85 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 8a380ef0-8411-3c78-afec-aabbeff1104d | -6.8764 | -43.685 | 2026-10-07 18:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 6b09405d-3a51-3c71-82d0-6914ced43d39 | -1.4771 | -53.6134 | 2026-10-07 18:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c8d0e664-53fc-3e53-9940-8a440045c7c8 | 1.6937 | -55.6461 | 2026-10-07 18:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 30eb277d-d8d2-326d-a0f4-46e35571cad2 | -8.2184 | -46.3396 | 2026-10-07 18:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 78798d48-a679-3159-81f3-676db733a3b9 | -6.3163 | -43.3614 | 2026-10-07 18:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 7d8eefc2-3505-3a3d-8f57-674aac8d5ae7 | -8.6292 | -67.0111 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 0177a0ab-459c-3394-8f3f-31f82b06e31d | -3.2357 | -50.1805 | 2026-10-07 18:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2fa66da4-0e6a-3249-b903-dc8a74dcaaee | -3.2136 | -42.9764 | 2026-10-07 18:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| cd86f04f-7641-34f5-93c7-374c8a0eac8b | -3.6049 | -54.5736 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 6c253498-029a-3584-bc72-60dd52fb8a75 | -3.4762 | -50.0883 | 2026-10-07 18:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 205.9 |
| 7e66dbbb-d07d-3b85-940f-6b20dd77a12f | -3.1697 | -58.6437 | 2026-10-07 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 160.0 |
| a93a9400-10c8-3cfb-ab22-40e753abca68 | -9.3381 | -65.7442 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 81a042d9-59a8-3dd6-901a-8bf797f57b87 | -3.7166 | -54.2096 | 2026-10-07 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 2b555c85-843e-3fe8-a7cc-d16f6225700c | 1.3346 | -50.8503 | 2026-10-07 18:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 40cb8016-eb6c-3495-af83-1757691751c2 | -9.8245 | -65.0348 | 2026-10-07 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |


[Clique aqui para ver as próximas entradas](README252.md)
