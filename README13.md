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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7e7fa48-4a3e-35e9-b0ec-055eb7b57c37 | -5.79263 | -43.73961 | 2025-11-08 04:06:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f415d69b-3e7e-35f0-8b2e-d0b9da198dbe | -7.28925 | -39.77981 | 2025-11-08 04:06:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 853e2579-9df1-347e-aa3d-e670ea69340e | -7.38481 | -43.53594 | 2025-11-08 04:06:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46548737-33bd-316d-9a99-05fb97eaebae | -3.35159 | -53.22275 | 2025-11-08 04:06:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f504601-c8cf-35fd-8231-51084755c4ab | -2.98712 | -52.82536 | 2025-11-08 04:06:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bee74256-aca1-3dd2-a34f-67b0e66fb338 | -3.31707 | -50.11736 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2252d35d-c8c4-33f6-b360-a22ec82bd363 | -5.93602 | -38.17859 | 2025-11-08 04:06:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 24ae3852-0f9c-3a8a-b9ad-a8bb04ce2fea | -2.82628 | -49.82909 | 2025-11-08 04:06:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 239a3367-610e-34a0-9026-65728f9333fb | -5.75088 | -40.79848 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc693a98-bf79-3f09-b253-320cd9e7a3dc | -4.27213 | -48.33941 | 2025-11-08 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7be29916-6ae3-3e77-be55-da611be7001c | -6.47286 | -39.12995 | 2025-11-08 04:06:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b617f4fc-e7bb-3e38-9942-6e045435ec9e | -4.68796 | -46.39936 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3913d091-8ac5-3f59-9aa6-fff43867cf4f | -6.02866 | -44.32551 | 2025-11-08 04:06:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 124ba5ff-b572-3e2e-8670-6d53bc9de457 | -5.74812 | -40.79452 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bd143799-a2da-3abc-ad52-e5c2da13fda4 | -3.76375 | -43.04726 | 2025-11-08 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23eef23f-6603-3b19-83b3-4df912baec4d | -4.10558 | -47.26975 | 2025-11-08 04:06:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca294e89-af09-3cf8-92da-7c80308415eb | -6.32215 | -39.70366 | 2025-11-08 04:06:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 389e3497-e107-33bc-9cae-5268fe12c81e | -6.65179 | -44.4879 | 2025-11-08 04:06:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4fda3a84-b489-3af5-99f5-9fa11b791513 | -6.69043 | -38.32906 | 2025-11-08 04:06:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 191f78d0-79ea-3a27-8dcf-8f76ed69dc66 | -3.24913 | -48.76284 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01ed3eb6-61c2-39d3-b12a-001216cb47de | -5.74911 | -39.71276 | 2025-11-08 04:06:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0a823bf-1118-34c0-89fd-0e8ec757f71f | -4.23828 | -48.60279 | 2025-11-08 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ecf6fba-ab4d-3ea5-839b-5706e4061442 | -4.27686 | -48.34034 | 2025-11-08 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d891d713-e818-3999-b67d-c6ce7aaa9fce | -7.54826 | -41.6632 | 2025-11-08 04:06:00 | NOAA-21 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe3f5fa0-7566-361d-93a4-3b991a228ae5 | -3.97278 | -48.89983 | 2025-11-08 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f78fd98-6f0c-3a4f-8cee-6bd5e26b956a | -5.75416 | -40.80261 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e3ff59e9-c52c-340c-8746-ac3db5592704 | -3.35373 | -53.22172 | 2025-11-08 04:06:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ec05778-744d-39e9-b5a6-9949a6fff5f5 | -4.07718 | -44.57839 | 2025-11-08 04:06:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0503d02-7d37-3189-b386-91cd22c2b4c5 | -2.7115 | -49.54396 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 72a2e401-eff7-3bfd-bb19-459c25ee2e77 | -3.91508 | -50.04668 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b651ff4c-e212-389c-8ffa-60fe43fac5a2 | -4.34966 | -45.76266 | 2025-11-08 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd184bab-c8e8-34fd-ac2f-4f3a16341bd2 | -3.77144 | -49.68982 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1123655e-bea6-32a4-a750-19ab64cacb32 | -2.79041 | -50.31549 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05a2e847-315a-347c-b9e6-abee50aa4b47 | -3.32292 | -53.36208 | 2025-11-08 04:06:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4f1f6177-87f5-3a67-a0a8-2817926999df | -3.67458 | -50.4522 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28a66c6c-0286-3dd9-9bdb-ce4b88e77b09 | -3.65028 | -49.86248 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd8e0bd8-e819-3271-880d-8ca7a1aee2c8 | -2.70676 | -49.53985 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 35b2c915-a07b-31a8-8ce7-8cfc99f9e707 | -5.65337 | -46.39977 | 2025-11-08 04:06:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eca0c24-036e-3ad2-ba88-77bcff365b96 | -4.75793 | -42.60879 | 2025-11-08 04:06:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1e73137f-c4d2-3447-a58b-c8c087003037 | -3.33743 | -50.19728 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c237f7d8-1f79-3853-a4d9-a0892e42c514 | -4.64643 | -40.79039 | 2025-11-08 04:06:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 355ef107-26cb-362e-8849-85f92814726c | -4.74826 | -45.785 | 2025-11-08 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5327c678-08de-33f9-8632-7001befeccb2 | -5.16359 | -41.228 | 2025-11-08 04:06:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8f317f4b-82c1-307b-9503-4a9c2cab44a1 | -5.18573 | -44.75756 | 2025-11-08 04:06:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08b033c5-d3ee-3b6d-a242-181526d642bc | -3.06005 | -48.72334 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f76a8ff-7094-34dd-ac8b-e62dd252eacc | -3.83151 | -49.81573 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa75a44-3aba-3f3d-a107-7e31ebec6848 | -4.39166 | -45.36013 | 2025-11-08 04:06:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4447de69-cb25-30bb-a20a-5624cafd4fc0 | -5.05903 | -43.31759 | 2025-11-08 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cf66002-bb36-3863-929c-1fbeb4257a86 | -4.68275 | -45.84503 | 2025-11-08 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4cdf2df4-bea0-3b1a-98a8-15952ccb0dcf | -5.93467 | -38.17763 | 2025-11-08 04:06:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2dd736db-d97f-36cc-9de5-3bc6c3aa9f76 | -3.34766 | -50.17555 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95a93ad1-1d68-3a3a-b56c-49455a41cc03 | -3.73454 | -49.68456 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 188166f1-9a25-3a70-801d-83e65cbe9ba9 | -3.34222 | -50.20708 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2370bca9-bf04-39af-ae46-331dafd4df0c | -5.09326 | -44.79843 | 2025-11-08 04:06:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 509c3157-8cc0-3e84-98f2-6fad0de83ef2 | -5.72612 | -46.46399 | 2025-11-08 04:06:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 996d3f26-ec35-316e-8dfc-46ac7af296c9 | -6.10977 | -41.55106 | 2025-11-08 04:06:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 378fd342-1c3f-3282-adf2-d9cce32cc541 | -3.95227 | -49.02361 | 2025-11-08 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3f80224-1486-3b2f-a22f-7ce508ea5eac | -6.97216 | -39.07841 | 2025-11-08 04:06:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3d45caac-41cb-3d7e-98c1-0b0b3351791a | -4.10484 | -47.27422 | 2025-11-08 04:06:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 951d61ff-fbc4-3308-988f-8f3b5754ef80 | -4.28731 | -45.89122 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70aeb6a9-f2d6-3331-95fa-dfbd31cd34aa | -4.89973 | -45.62582 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c7b0e95-c9dc-3ce3-9cc4-05442a3bdbc0 | -3.06106 | -48.72218 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d800cdd-9ff2-3828-bbc6-817a6c288ae6 | -6.26887 | -43.68576 | 2025-11-08 04:06:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01f0f8b5-9224-3cc9-a999-4770e8793ae5 | -6.80204 | -38.52886 | 2025-11-08 04:06:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 66508272-2c70-3e64-abfa-6b5378c91e3a | -5.90412 | -37.82642 | 2025-11-08 04:06:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ad63f459-7fef-3f9f-bddd-cb5d5f276d95 | -4.59253 | -45.98489 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2ef97d7-8964-3794-a696-72328f12e67c | -4.0564 | -46.43436 | 2025-11-08 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74e08169-93e1-35b5-b151-df7d97648f4f | -4.47242 | -45.32808 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 64f24505-587d-30ff-b015-ff6e07f1a148 | -3.13123 | -49.10046 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e339d29a-b4f6-3ce2-8d2a-4dfc9a648766 | -3.44482 | -46.18966 | 2025-11-08 04:06:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 501309c2-af5f-3fbd-9d83-6d302749060e | -3.56133 | -50.80906 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69f321ef-cff9-304d-95e8-0edd8d89a70b | -3.35943 | -49.51057 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b18bb7a0-7218-379f-bf3b-c70a734612f5 | -3.36362 | -49.51376 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2323a203-4b7b-3e98-9e1e-378b25b688c7 | -5.83112 | -43.2795 | 2025-11-08 04:06:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 911e337e-ad7a-37e9-8ce6-dd9e9056f070 | -7.14992 | -39.86692 | 2025-11-08 04:06:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 468acfcc-27e2-3911-aad3-108f25794953 | -4.27798 | -46.40647 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4778d02a-d503-34e9-86b1-b30b37286334 | -3.3477 | -50.20797 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4ce032d2-acd6-33ed-850a-01832070f28d | -3.35214 | -50.21033 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c1910488-4022-3a3a-abd6-84f31c98686f | -4.28385 | -45.88717 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c1ba378-8356-3ac9-b470-e355b2d12239 | -4.63757 | -45.89551 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 639acfc1-b469-3d38-931a-808ed10d8977 | -4.46491 | -43.21397 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de6345cb-18af-3264-9439-4041ceb422bf | -3.68029 | -50.04385 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35c1644b-40ff-3e4d-a9f5-0de608b1aacf | -4.59346 | -43.45881 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a276c97a-d339-39a1-85c3-2b8e3a693523 | -4.69085 | -46.40758 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4424cf22-4f1b-3e42-86e7-571278ed82db | -4.11006 | -48.01059 | 2025-11-08 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 315c3f29-f8f8-38bc-9347-595db4526b0c | -4.52874 | -43.7686 | 2025-11-08 04:06:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1c5e616-c917-306b-8e61-187fe6380f81 | -3.03645 | -50.30371 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22f9d1ca-328c-36c0-9196-93af157c9a02 | -4.45087 | -46.44215 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d2bd544-253b-3b85-9c7f-c15d20e1f960 | -3.40168 | -50.45911 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 966d9077-8df8-3e85-97b3-5fbcd82657d2 | -4.67968 | -46.3981 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a69e7a21-d5c0-3845-9828-98b5d42bb007 | -6.65214 | -43.61304 | 2025-11-08 04:06:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da7eaa87-4b5a-3740-8f11-8c68fcb2c20c | -4.57719 | -45.77541 | 2025-11-08 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d517654e-fd3b-305c-9716-511d320f45b8 | -6.36827 | -41.74808 | 2025-11-08 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b7e13c42-540a-340b-977f-adbabf645f82 | -5.61933 | -41.07796 | 2025-11-08 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e37a2fcc-ec76-320d-885c-2127ab1c3069 | -4.84332 | -45.62507 | 2025-11-08 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 485276cc-e9a0-3d02-a5a2-d30006fdaad3 | -3.85261 | -47.40458 | 2025-11-08 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c4e85241-bd86-3e5a-adc1-2557670ffc26 | -2.9809 | -48.70763 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c420ba7-efcb-37c9-a7c2-243c6416a27d | -3.43648 | -51.5246 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3516cd45-9379-33d2-b29a-cdc1b8b3bc0e | -3.43052 | -50.11622 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c657e215-4e69-3e55-9e89-537c5c7ef2a0 | -3.40388 | -45.44087 | 2025-11-08 04:06:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |


[Clique aqui para ver as próximas entradas](README14.md)
