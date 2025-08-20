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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc770f89-dd6c-3b64-b4d0-2f7d4dff7543 | -8.7945 | -45.4693 | 2025-08-20 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 9200efdc-bb1a-36fa-92b6-ab4fc7bb82bf | -12.9778 | -56.8614 | 2025-08-20 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| cec7b086-90f2-35ad-8236-c19556185c0c | -5.9711 | -44.1542 | 2025-08-20 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 165.6 |
| d3659037-7d5e-3e23-9213-7c482852aa1f | -6.9607 | -42.858 | 2025-08-20 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.6 |
| 9e9b559c-f162-3a5b-8570-a14c555c3e60 | -11.3087 | -44.9264 | 2025-08-20 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 6f075779-c855-32d5-a8f0-99f093f9511c | -13.3537 | -54.4213 | 2025-08-20 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| e3e1af10-ee2a-31c4-b023-772b03d4c0fe | -12.9736 | -45.1819 | 2025-08-20 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ee5663fa-0472-3c00-ac13-6a1594dc24f8 | -13.1364 | -54.9376 | 2025-08-20 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| b8d8b0d0-cbc1-3bc0-a424-488e31a22f4c | -8.8294 | -52.035 | 2025-08-20 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3e8be244-3b6d-3ba4-8464-feae63adfe0f | -5.9713 | -44.1312 | 2025-08-20 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7d5083bf-5d5b-3df4-a2cb-863cbd39a079 | -8.8291 | -52.0558 | 2025-08-20 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 707029bc-fe8e-39a8-ae34-4ff7bde8e196 | -7.2602 | -50.1613 | 2025-08-20 14:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9bf25bdf-ea78-3ec8-b43e-5b0541242bed | -12.9925 | -45.202 | 2025-08-20 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 330.1 |
| 83ecd009-6584-3b46-8a7b-f3177d24c2fa | -6.4639 | -45.5057 | 2025-08-20 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 60801361-c8c2-39e6-9555-b8dc22440e74 | -10.9916 | -45.6359 | 2025-08-20 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 25ad5caf-ef87-36e3-8282-bbeec69554a4 | -12.9921 | -45.2252 | 2025-08-20 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3f8883b1-828b-3130-b834-566efa6a2e46 | -12.9732 | -45.2051 | 2025-08-20 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 4c352622-d838-32e5-bdd6-c03fda8182ae | -11.011 | -45.6105 | 2025-08-20 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 94b3ff5b-cb4a-3a10-bf8e-c544a6798c48 | -11.6739 | -60.1869 | 2025-08-20 14:10:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ec812122-d1a2-37be-b118-f3e076c893a7 | -13.1558 | -54.9151 | 2025-08-20 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 140.4 |
| f10a1c04-f433-348c-8c4d-22deef53671a | -7.1289 | -44.6541 | 2025-08-20 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 63a008d6-0a72-39ab-9a52-09b5aa304180 | -6.4451 | -45.5072 | 2025-08-20 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 27948f96-6da2-3d95-9299-ea48e2f4574a | -12.9736 | -45.1819 | 2025-08-20 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 2612ed6e-dee5-3b5f-a92e-7f1db1b3673e | -7.2903 | -43.6696 | 2025-08-20 14:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 7ab773d9-a87d-37fb-b1ff-bdcad62798ac | -13.1555 | -54.9357 | 2025-08-20 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 7b097066-9050-355f-b9b5-6cd8daafeb11 | -12.9925 | -45.202 | 2025-08-20 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 265.4 |
| 48ce07a9-f339-363d-8734-52e238daa6eb | -10.9916 | -45.6359 | 2025-08-20 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c6b9cd3e-4ab9-316d-ad71-661489822c9d | -7.2901 | -43.6929 | 2025-08-20 14:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 166.9 |
| d7071622-ef60-379c-923e-27c7ac1e89dc | -12.6698 | -44.9525 | 2025-08-20 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| c4d31b84-6379-3b9c-8f93-252ebbf8c05f | -9.152 | -59.6772 | 2025-08-20 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2ebe3a18-ce92-3e46-a515-804e388684a1 | -8.8294 | -52.035 | 2025-08-20 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4d2b5a01-0ec6-3101-9545-6459d3d588b9 | -7.26 | -50.1825 | 2025-08-20 14:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| faffb425-151f-3ad8-83b3-b3177d6e1247 | -12.0976 | -44.717 | 2025-08-20 14:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 98d496a5-bddd-37fc-93bc-73575bce43d2 | -5.9711 | -44.1542 | 2025-08-20 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 30a6870d-8dfd-3b7e-ae19-1f38cb56c1f8 | -8.6343 | -62.1367 | 2025-08-20 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 006e4490-89af-3ba2-aae4-9dbb671c334f | -8.7945 | -45.4693 | 2025-08-20 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 569fb8be-5ca6-3607-b4b2-ab79a6c94463 | -6.9419 | -42.8598 | 2025-08-20 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| d9e71b4b-1028-3c69-b2eb-2b8fb263fb67 | -6.4529 | -53.3669 | 2025-08-20 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 4cfdee65-5fde-3791-8ade-b490f00573c6 | -12.9778 | -56.8614 | 2025-08-20 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 49958b75-ef85-3788-b79d-9f114f1c5565 | -8.2234 | -44.4092 | 2025-08-20 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 14713d9b-668a-3da0-b435-cc7f309381a9 | -15.0196 | -54.8112 | 2025-08-20 14:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| de78ace4-10c4-3a3e-8077-c4260f515292 | -13.0387 | -46.819 | 2025-08-20 14:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 67ed67ee-e0f4-359e-a3a6-2e703b8a9a5f | -13.1558 | -54.9151 | 2025-08-20 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| e1b78390-0d6f-3746-b9ce-5decdab0828e | -8.8291 | -52.0558 | 2025-08-20 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 14da8076-20e6-36ec-bbaf-26203385b369 | -10.1974 | -46.596 | 2025-08-20 14:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 22535ba5-45e1-3cc1-af41-ff1dabb37f42 | -13.1364 | -54.9376 | 2025-08-20 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 39563123-3b95-300f-856e-539df77afad9 | -11.3087 | -44.9264 | 2025-08-20 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| aa313e75-d7ca-30c4-a803-7a5dafffe7ae | -12.4474 | -47.668 | 2025-08-20 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 47357f3e-2894-31db-99b3-f888ce6202ea | -6.4528 | -53.3872 | 2025-08-20 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d4b804d3-41fc-345a-a06d-e1fb0419fd49 | -8.8137 | -45.4445 | 2025-08-20 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| d67bfd03-7b54-3ba4-ad9f-b70473367046 | -12.8984 | -46.0906 | 2025-08-20 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a8d0d5bb-3109-3fa4-a00d-03f5d4f388f4 | -13.1367 | -54.9171 | 2025-08-20 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| b33ac54d-b9f8-307b-b9bb-729053c22fcc | -15.0002 | -54.8135 | 2025-08-20 14:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 56bcf5f3-019b-3873-b4f4-cefb3e3087e4 | -3.982 | -42.516 | 2025-08-20 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 9e69efc0-baac-3226-b5cf-0128f4ddcc4d | -5.9713 | -44.1312 | 2025-08-20 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 5277598c-49f0-35d5-8548-bd8abd0d2a9f | -8.7948 | -45.4465 | 2025-08-20 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9c6fca3a-7bc1-3deb-a333-0c06ac64cac0 | -12.9732 | -45.2051 | 2025-08-20 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 8c96df80-d6b0-3862-952f-8cec8ca5bbd1 | -8.2231 | -44.4323 | 2025-08-20 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 27bef414-bc75-362a-ae9f-ea6ee360db41 | -9.152 | -59.6772 | 2025-08-20 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d410af4c-0329-31ea-80be-3aaf2c93be69 | -5.6411 | -43.3687 | 2025-08-20 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| dbec1580-fb38-3f77-815d-0ce8ca06b881 | -13.0387 | -46.819 | 2025-08-20 14:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 26acd337-4d0c-3f02-9181-d027278123a4 | -7.6293 | -45.2691 | 2025-08-20 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 27a4e10a-3e2a-3b70-aa01-8c193c5b0a43 | -12.9732 | -45.2051 | 2025-08-20 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| dc8557fc-ae98-345f-ade8-b65732f2139e | -13.1364 | -54.9376 | 2025-08-20 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| dedd2ba2-037d-341f-9108-38bfcb34dc88 | -14.313 | -53.166 | 2025-08-20 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| c03a7340-d848-336b-8541-c0d3a45b0e43 | -12.8984 | -46.0906 | 2025-08-20 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 89bfd72a-4f7e-3bcb-b1ae-6faaeb2c5f0e | -10.9916 | -45.6359 | 2025-08-20 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e1d1f5cb-d443-3102-9cc0-d3e00d4d66cc | -12.9968 | -56.8597 | 2025-08-20 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 5b2d828a-a583-3f3d-a220-f868ec019c6a | -12.9778 | -56.8614 | 2025-08-20 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| cbf116e6-a99b-39dd-9bbc-1da567f78383 | -9.9329 | -49.2869 | 2025-08-20 14:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| cc7ff441-41f1-3138-913b-3ca6523e3f0c | -14.6326 | -54.8773 | 2025-08-20 14:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 6ae4de0c-a5d2-3821-891c-fb7aeaacec5a | -8.7945 | -45.4693 | 2025-08-20 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 61bdff54-4098-3af5-9ee6-9be8e6969b33 | -13.1558 | -54.9151 | 2025-08-20 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 3cd6074d-a5b9-3734-9732-24495507e4f4 | -7.0169 | -44.5954 | 2025-08-20 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| a957d805-3d5b-3bd3-9593-24322e97c92b | -3.982 | -42.516 | 2025-08-20 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| 04272ad0-ba26-3517-b4a7-4a840ce170d7 | -8.8291 | -52.0558 | 2025-08-20 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ea4df8b0-2644-36cc-a729-bb3258c40d13 | -8.6343 | -62.1367 | 2025-08-20 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5642dac9-4fd1-3df2-b196-c1f3a3483f36 | -6.4451 | -45.5072 | 2025-08-20 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| b7f848f1-d1ab-3c62-9699-d02baf59dc41 | -5.9713 | -44.1312 | 2025-08-20 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 75014ead-e0f7-37c8-acb9-79f4a78c66a3 | -7.2602 | -50.1613 | 2025-08-20 14:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 452711ca-7980-32ed-a28f-aa7743e33f31 | -8.7948 | -45.4465 | 2025-08-20 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 9790419f-319c-3443-a10b-91a97b86b667 | -8.5556 | -66.9389 | 2025-08-20 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f519cc4d-3812-34b8-a21d-9b1a0546998c | -7.26 | -50.1825 | 2025-08-20 14:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 13c2bb3b-3799-3fe8-a6dd-34d18a337a86 | -11.011 | -45.6105 | 2025-08-20 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 9352b6a5-df12-357e-9f7f-ee8d4ca89805 | -15.0002 | -54.8135 | 2025-08-20 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 4cbf122e-a88f-3a48-a51f-2097d930d8b1 | -9.1711 | -59.618 | 2025-08-20 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b992ab3a-1fda-38c4-ab92-6bd9173ce3a6 | -13.1367 | -54.9171 | 2025-08-20 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 983c0d56-fad1-3fac-a9cb-39f29fbc0678 | -9.1712 | -59.5987 | 2025-08-20 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 582fceb6-0b9c-3203-b60d-2204caa1ab5f | -15.0196 | -54.8112 | 2025-08-20 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| bbaefbb8-da66-39c0-a2cd-d87aa4c1fd8e | -6.4454 | -45.4846 | 2025-08-20 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 459e7178-af20-3599-9c06-487ace5edd0a | -12.9736 | -45.1819 | 2025-08-20 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 8841cf10-8979-3e92-a931-769b4e23bafb | -5.9711 | -44.1542 | 2025-08-20 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| c17af1a4-fad7-34f8-a939-675f9173107d | -13.1555 | -54.9357 | 2025-08-20 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| c8a7b945-0969-3c9e-9e32-f6c51619de2b | -6.4528 | -53.3872 | 2025-08-20 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a0213194-269e-3725-8d95-dbaf162292db | -8.8737 | -62.3925 | 2025-08-20 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 88eae1f9-2304-3b53-a724-823051f9947d | -12.9971 | -56.8395 | 2025-08-20 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 96370fed-453e-3774-b775-0578f8a5ccc5 | -14.6323 | -54.898 | 2025-08-20 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ce302bf0-9f9b-3c4c-bc42-ef0cb39765d1 | -9.1711 | -59.618 | 2025-08-20 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4be723ee-5280-321d-bf53-6f2d5f71c478 | -14.313 | -53.166 | 2025-08-20 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 64d2afb4-d5cd-35f4-a3f0-c173438172e5 | -12.9968 | -56.8597 | 2025-08-20 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |


[Clique aqui para ver as próximas entradas](README66.md)
