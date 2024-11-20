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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 649d9a2d-ca6b-3cdc-ad21-f07ec50ee261 | -3.0602 | -54.40266 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b45d9913-fa43-329d-9cf7-a91e4834e9d1 | -4.06638 | -46.87177 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2117bc06-b609-3573-817e-e91f2825d803 | -5.25315 | -43.83154 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ab3322c-bfa7-3666-9743-39d3b15a5777 | -3.48558 | -48.23968 | 2024-11-20 04:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c5d337d-b975-305e-bb79-870d15bf0052 | -5.25894 | -43.84027 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60e1f1f0-5b7d-3856-9507-38e029bc8271 | -2.95096 | -48.32543 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47dce912-b4e3-37a7-bb75-5c973d672b4e | -2.92955 | -53.07898 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48f4e0c7-730f-3870-982b-c85698af7324 | -10.46139 | -45.07321 | 2024-11-20 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2c0b3e0-f7c7-3643-8913-7b67d1af5f9b | -2.7083 | -53.17613 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 732bfc39-011c-3b45-8c3f-73914930d17a | -3.90651 | -45.08461 | 2024-11-20 04:27:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba4e5ae-fc61-3b02-8dce-c4e1d5de2252 | -9.25268 | -45.00293 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da133971-d04f-3081-a902-15df888f7b0d | -7.155 | -48.32026 | 2024-11-20 04:27:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a62cd66d-ba93-334e-b487-e71f42dd43b3 | -4.38895 | -47.76192 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e8f67e8-c68a-3d56-87af-e1888321509e | -3.98363 | -46.70535 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 828a8fb0-930d-3376-bb55-de7fc6a53d68 | -4.32327 | -46.01335 | 2024-11-20 04:27:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9e457fe-dc9c-396c-9c8d-75f4dd34d8c7 | -4.51499 | -50.57867 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f6b8349-40ca-33bd-b203-5fd0b24b1bc3 | -2.80102 | -51.79483 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb185419-603d-3d71-82eb-8332f30395e1 | -4.38018 | -50.42022 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 564e088b-db86-3824-a4a8-487045fc60b2 | -5.06947 | -44.2264 | 2024-11-20 04:27:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf95d9ca-994e-3001-8d0b-828fe3c024fc | -9.21442 | -44.16478 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aae8be96-7f37-3cfe-960d-a1a966de8271 | -2.91936 | -53.08215 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ea2633a-cc2c-3517-a362-5fba0a7fc8fb | -5.96389 | -48.0612 | 2024-11-20 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| ecda0065-e5a1-31b3-898a-fe1743f6bf06 | -5.38024 | -44.96513 | 2024-11-20 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b62822ca-d6b7-3618-a835-4917667a237c | -9.93251 | -44.49271 | 2024-11-20 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59b6d816-6296-3d3c-9be8-0dcfd02138c4 | -4.19789 | -46.81414 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b612e2f-4541-3c57-959d-52c3e9159c1e | -5.2473 | -42.64359 | 2024-11-20 04:27:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d103ed94-6c33-3540-a088-d4fb3fee61ff | -4.44464 | -46.58604 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e3e56786-bdd8-3e42-a4bb-dcfb31784839 | -3.22078 | -53.84294 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b573507b-6bd6-3b09-b80d-47ff5e2dd94e | -4.07679 | -50.03966 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12ed5d85-8d29-3082-af4e-70e671deec05 | -5.64001 | -46.36153 | 2024-11-20 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9411fd01-7300-3ffc-88d9-eb7a77388cb8 | -5.59741 | -46.17493 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17fff4ad-cf29-3b34-b97e-402f8aa21da1 | -4.93925 | -50.64951 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5065ff55-77b6-3c52-a1f7-5ca9ab3c1fe7 | -6.24909 | -47.2705 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9204c811-7f1b-308e-b021-a2658faef43a | -3.73133 | -47.37437 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8456d6c-142d-37a2-b03d-8dd4694d9192 | -3.19779 | -54.31917 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e61b7ded-a211-30de-bcc8-6703aa3a5575 | -10.76636 | -44.82328 | 2024-11-20 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06767e98-605b-375d-9e7a-e04808b13c5c | -3.8328 | -46.56053 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73573a9f-8f24-31a3-93ac-20384928bc6e | -7.17611 | -45.03889 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15ed27c6-2de1-36ce-8da0-b6e307e065db | -2.91358 | -53.06811 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| de760e5a-afa7-3550-a832-f9da495541b9 | -4.12399 | -46.85211 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecef198d-7fda-3825-9ecb-f4e2e791101b | -5.4201 | -44.70649 | 2024-11-20 04:27:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 990ae168-4882-36fa-8a57-3da17f6aa09b | -2.9225 | -53.06245 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c9741349-7cf6-3299-855b-36470fab4f0f | -2.45643 | -53.69964 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2ca1ff67-405f-35df-823d-555e8e8029cd | -5.69527 | -45.85069 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1be44f96-7a0e-39d8-95fb-7c61af55ecb5 | -3.91706 | -46.41484 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67260ade-cafa-3ca6-a8c0-bb3e156ea1e8 | -8.73696 | -44.0885 | 2024-11-20 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71c2d0cf-bfc7-3d31-adb3-086335703248 | -2.92801 | -48.33391 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e305161c-0d18-3ee8-8405-a2480d37656d | -3.18652 | -54.32375 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3ecc032-5267-3239-9a1c-58ff5e983f01 | -6.37871 | -44.74711 | 2024-11-20 04:27:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af922671-e08c-3afd-a0df-2b97051cd950 | -2.93104 | -49.43502 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95abc84c-8994-3306-b85c-4f6a250a40cc | -2.95972 | -51.41011 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1223e5f3-ba57-34f3-bcd5-91c8a8fc0dfa | -9.21502 | -44.16077 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12d075dd-e603-3c75-8877-67fa7d859f0b | -3.89077 | -43.15032 | 2024-11-20 04:27:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57e8a8e3-8a02-3fe9-a16c-7da302b1a42e | -6.01423 | -38.66108 | 2024-11-20 04:27:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7bdab4af-faf8-3708-a171-191401d23ad9 | -4.1024 | -44.85248 | 2024-11-20 04:27:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62baf24a-fb2d-3e8f-868f-d4a2f98d7436 | -2.74599 | -51.82132 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 617c7f25-7a6e-34a9-af56-6db2214ad860 | -3.19629 | -54.32826 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a4d66454-3776-30b9-8efb-d7fd093999cd | -2.78914 | -51.71827 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6db51fe4-5905-3609-8b62-638574b83f7b | -2.95159 | -48.32151 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2eed750-7f51-3767-8dde-620a3e7146a8 | -3.88953 | -46.65513 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60ab30e7-fc2a-364d-a83c-d828baf93cbd | -9.93313 | -44.48862 | 2024-11-20 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1039ef6a-c4ab-366a-aa9c-85ba93a5f5eb | -3.04835 | -54.41019 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4384730d-dda2-3259-9f5d-39c87b7e7f14 | -2.93152 | -48.33446 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8d2284bf-c1a9-312a-9e81-85510a730888 | -7.2579 | -48.42311 | 2024-11-20 04:27:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16c36363-3bb6-36a5-8583-fb5e822ecc16 | -4.78859 | -50.48547 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3aa6c8a-3762-3f8d-952a-4a212f7a2af3 | -3.87735 | -46.05903 | 2024-11-20 04:27:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eaed4ed1-138d-3263-8ce2-a34047db0740 | -4.69966 | -44.46403 | 2024-11-20 04:27:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33820ca0-1b10-33b6-aaa1-8fb9e611e7d3 | -5.96728 | -48.06173 | 2024-11-20 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 96e2c8f6-d319-3fe8-94c0-ceef8ccebd29 | -3.46518 | -48.25605 | 2024-11-20 04:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4062db4-7c5f-3556-8d3a-43d0b36a5255 | -2.61348 | -51.80572 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da19d60f-5465-3420-a9aa-f7f301b1cc34 | -3.88622 | -46.65461 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af613cae-f79d-34c3-a7e4-51834a93ee30 | -3.28814 | -46.19581 | 2024-11-20 04:27:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b31a849-e92e-341f-b556-5a0981126687 | -2.92602 | -53.0806 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39609e30-6e31-3c57-ab35-2b6bee4f9356 | -4.33866 | -50.42114 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13ee403c-ac7d-34c1-97ca-7f2a660e5c73 | -5.46933 | -43.94503 | 2024-11-20 04:27:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7b00488-2a9c-39ca-9e4a-4b4899df6e20 | -2.90763 | -53.06469 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7db5b69e-1b66-36e2-aa05-38a3e60bf5f9 | -3.20243 | -54.3229 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2efab264-50d5-3b55-8b78-f6f2a3821d8f | -7.56332 | -46.45623 | 2024-11-20 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf7f6c38-e617-3523-a4ac-dcc610047b4a | -3.81926 | -51.35403 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 31c21209-993b-36fe-872b-9b2a9a2d87cd | -4.14077 | -47.73436 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 379dabb3-1acf-3b4e-a28e-b12508f98d94 | -3.36726 | -54.10481 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f2d98ea-a603-3d29-bf59-df891b0443be | -5.06223 | -44.77748 | 2024-11-20 04:27:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66eb6335-e6bb-396e-9ca3-7e6590fa9138 | -4.23907 | -46.11581 | 2024-11-20 04:27:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8d22b7b-71cd-3975-ad67-8f84293b38ea | -5.7205 | -44.80766 | 2024-11-20 04:27:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4911f77d-7a81-3524-bbe4-0b9df4c012a3 | -10.45314 | -44.88778 | 2024-11-20 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29684af9-9572-3378-940c-e49d5cc922f8 | -5.2199 | -47.08613 | 2024-11-20 04:27:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7659246-ac18-3596-b94c-f0f394709351 | -3.94515 | -46.40858 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f9ddc58-0226-30ff-ab1d-3375f87e0cd5 | -3.84879 | -50.69129 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6189db8-b456-3166-bcf2-8bed4c4f0d2c | -2.28668 | -53.63448 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 513192a0-b454-3c7a-9f40-afa99560addb | -2.92406 | -53.08305 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ecb549c-4eab-346f-89e5-4c0941f1b37b | -2.61416 | -51.80157 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c68c9580-b48a-3cfd-9fe9-37ea81b88564 | -8.92299 | -45.77154 | 2024-11-20 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf1a4c37-4d6c-3ad9-8c8b-edba46941270 | -10.94959 | -44.4062 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1ace761-99c9-371c-b8b8-1bb6b187f317 | -5.45211 | -49.68468 | 2024-11-20 04:27:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3383b21c-cca5-322d-afc7-52feda3a5ae5 | -5.38685 | -45.45022 | 2024-11-20 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce782d33-caca-3530-9a21-4ad546999b6d | -7.34619 | -47.88609 | 2024-11-20 04:27:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 766a968f-b506-3dba-b6d5-6007de0c9aa4 | -2.92484 | -53.07813 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2eaf07e4-209c-3de3-ac53-871eee1b3101 | -4.24237 | -46.11631 | 2024-11-20 04:27:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dfe8616-6ddb-3809-a66f-e0a126eadb88 | -5.1964 | -44.22235 | 2024-11-20 04:27:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d6ec5e4-06d7-3744-bc80-4224ab424b23 | -4.44741 | -46.59001 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README39.md)
