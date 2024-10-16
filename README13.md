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
| 5092c81f-4600-38dd-906d-c7e40eb3e1d9 | -1.56608 | -48.01983 | 2024-10-16 01:02:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 85e7fa8a-d8f0-3267-8aa2-e40828c1c0cd | -1.70976 | -52.52794 | 2024-10-16 01:02:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1060da95-68d4-38f7-852c-812f842c302a | -5.2772 | -46.3549 | 2024-10-16 01:02:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 001a1516-90f5-386c-af8f-4ba1096fb39c | -5.25819 | -46.8687 | 2024-10-16 01:02:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7dd620a4-363d-38bd-9a61-d387de96e491 | -5.23712 | -49.8538 | 2024-10-16 01:02:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 44de4cc1-ac98-370c-8cea-47288f707c73 | -5.23056 | -50.87865 | 2024-10-16 01:02:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 840548ae-8f12-35e7-a97e-31571ae18e8b | -5.21943 | -47.96332 | 2024-10-16 01:02:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 137ba912-5523-35cc-9400-35e8f3e6ca84 | -5.11235 | -46.84057 | 2024-10-16 01:02:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ada4a0f-57f3-3951-a7c8-31343e6b1d58 | -5.10259 | -46.842 | 2024-10-16 01:02:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e5be085b-07d9-3462-8d76-349bb19f9d91 | -5.09887 | -45.82816 | 2024-10-16 01:02:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| eae27feb-72d0-3da1-8fce-1865def7b55c | -5.05417 | -46.08302 | 2024-10-16 01:02:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 22d5eefd-0910-3cdb-ad0a-0ba935cc3aa5 | -4.99154 | -50.88361 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 427948ac-d4a0-3dfc-bd95-9793933bcf00 | -4.96373 | -50.4769 | 2024-10-16 01:02:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 53ff2a6f-0f2c-3dc5-9d82-0dac3e864ec1 | -4.82764 | -46.98986 | 2024-10-16 01:02:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 55ad2fe8-9f06-30ce-9b45-e00b52867d95 | -4.8257 | -46.99593 | 2024-10-16 01:02:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ea0676d1-94b5-30d1-a2d1-f91589218d0e | -4.82416 | -46.98506 | 2024-10-16 01:02:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b89bd462-2241-314a-af2c-0b940eea3fcc | -4.82336 | -49.14429 | 2024-10-16 01:02:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6c2c1c43-e259-35bb-9c18-a7e7415009c4 | -4.81609 | -45.22383 | 2024-10-16 01:02:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| de3cbf03-8807-31b4-b9b1-10a53ff8e193 | -4.81449 | -49.14554 | 2024-10-16 01:02:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a6952af-2d2a-37f0-98e5-3a0c732c61b8 | -4.81267 | -49.39013 | 2024-10-16 01:02:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f756ea94-d029-32fe-8f9d-9ffe34ce51a4 | -4.73271 | -46.55462 | 2024-10-16 01:02:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 75465e51-eb6a-3f7c-af45-eb9d5b2a4f7c | -4.73103 | -46.54289 | 2024-10-16 01:02:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| b6da4057-ffae-3128-b41e-1d227e785014 | -4.57324 | -48.02179 | 2024-10-16 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ba109756-f6dd-3a42-aae2-131766d9ff42 | -4.47559 | -47.73632 | 2024-10-16 01:02:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 677f877d-9bee-367f-9992-047e657d352f | -4.47016 | -47.74331 | 2024-10-16 01:02:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 07b298e8-2267-33ba-85e4-3c16d7e1556b | -4.46878 | -47.73346 | 2024-10-16 01:02:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 57d584a2-9fa3-3e6f-8c6a-b264a5d14f47 | -4.44955 | -44.84266 | 2024-10-16 01:02:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 982af83a-649f-3d0b-9187-32f74b43f28b | -4.44781 | -49.03094 | 2024-10-16 01:02:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9eb9b112-9dc9-3901-86ba-ff8f78ae7c30 | -4.44727 | -44.82735 | 2024-10-16 01:02:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 49712b9b-ba7c-3dae-b5e7-176a958cf1fc | -4.43482 | -49.72604 | 2024-10-16 01:02:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d347b75-c5ad-3ba5-9442-0978ab8fe01c | -4.41273 | -50.69727 | 2024-10-16 01:02:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 09d89cac-c55c-38fa-8725-f078bf99c3c0 | -4.41148 | -50.6883 | 2024-10-16 01:02:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9aafb06a-9baf-36e9-bfa5-5fc04d64b533 | -4.38967 | -49.66061 | 2024-10-16 01:02:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 136c71c7-7b14-30f9-bdad-628640e5b736 | -4.38589 | -47.48752 | 2024-10-16 01:02:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f9b5852a-064e-3f35-8d78-e47017afc569 | -4.36333 | -48.49439 | 2024-10-16 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7bbb2c76-0166-3fff-ab0a-e79ff32fa9b5 | -4.36099 | -48.22038 | 2024-10-16 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 47577e81-63f7-362b-9ace-3370456180de | -4.3595 | -50.97782 | 2024-10-16 01:02:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 0a3830eb-9a60-300e-874d-01be1712b1c5 | -4.35824 | -50.96876 | 2024-10-16 01:02:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 77601b10-36c8-381c-af36-32acc34a0f58 | -4.35429 | -48.49573 | 2024-10-16 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 55886b56-d835-30c4-ac3e-4324e9495da3 | -4.35053 | -50.97908 | 2024-10-16 01:02:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 75b9c4e0-62f8-3729-b135-87c0727e72f7 | -4.22504 | -47.85161 | 2024-10-16 01:02:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ed39d9fb-400e-3599-aa32-4e3cf19eda5e | -4.18515 | -51.24804 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 36d91ed1-17e6-3c7b-b599-e39dc25f59ed | -4.18401 | -47.9437 | 2024-10-16 01:02:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a289b47f-a0cc-3611-b99a-966842307c21 | -4.13666 | -45.36691 | 2024-10-16 01:02:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 41994515-ede5-3acb-a75a-aedbf9256786 | -4.11864 | -51.09805 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e85561bd-be02-389f-807d-2e39c118c034 | -4.10869 | -51.09599 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d3ee2a14-0c94-30dd-9a4d-ac769d174f36 | -3.98351 | -50.71813 | 2024-10-16 01:02:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 53d1fa52-e3ca-3c99-b559-2a5fd0429227 | -3.98228 | -50.70919 | 2024-10-16 01:02:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 4320a150-e1ea-3e5a-a9b9-89baa68dfee2 | -3.97452 | -45.58877 | 2024-10-16 01:02:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f806e56b-8cae-3268-923d-82decbb87519 | -3.97217 | -45.59556 | 2024-10-16 01:02:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 64b35170-c471-35f2-98d0-22fda9ca7093 | -3.96409 | -44.05655 | 2024-10-16 01:02:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 123bc3fd-ca12-3cee-a8d1-8c2c9867bf3d | -3.9637 | -47.95749 | 2024-10-16 01:02:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7f7dcacd-a6af-31fe-9753-c216ecf5bcd5 | -3.95881 | -46.44167 | 2024-10-16 01:02:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 52a85b83-ff45-3d7e-92e2-df131a9ef701 | -3.9571 | -46.42987 | 2024-10-16 01:02:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 116.1 |
| b932b94c-463c-3cc4-a68b-f53c0e66b275 | -3.93791 | -49.40414 | 2024-10-16 01:02:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 48481a48-1e9e-3a07-b55f-e3c4f6c74f57 | -3.93232 | -49.95948 | 2024-10-16 01:02:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8debe81e-14af-31dd-94ca-395bc38fa995 | -3.9237 | -50.22077 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 374c8f6c-9775-3a79-8a5d-dcfceb59ede5 | -3.91487 | -50.22203 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 710a7db2-42e0-3e39-aa40-38d070944b0a | -3.86885 | -45.97092 | 2024-10-16 01:02:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c1b17fb1-0e7e-3506-8718-81c23efe84bf | -3.86694 | -45.95795 | 2024-10-16 01:02:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a200e43a-f14e-3b4f-9c9c-fb5b239ad1a3 | -3.842 | -47.55089 | 2024-10-16 01:02:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a0b111c2-1b03-3f75-8ccd-db8729385c9e | -3.84052 | -47.54055 | 2024-10-16 01:02:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 62510406-0427-3a09-aa38-7230004dba5c | -3.81153 | -51.27767 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f99ec14b-db85-3b9d-9102-e3baca28bcbc | -3.80466 | -47.80059 | 2024-10-16 01:02:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1c065732-dd68-3435-99af-28223f1ad496 | -3.80324 | -47.79056 | 2024-10-16 01:02:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0b48e177-dbff-3c1c-8cab-1ab9658eb864 | -3.77608 | -51.35428 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 1ab15d07-5263-3c06-8cc5-865168695af0 | -3.77479 | -51.34504 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7cb224e9-b0a8-3e78-b9fc-a826f8cad499 | -3.74599 | -51.93438 | 2024-10-16 01:02:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8a6681a5-8d93-3e68-a91c-289d518797ff | -3.6991 | -53.44784 | 2024-10-16 01:02:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3159828b-b9ca-3335-a789-f86281df29c1 | -3.66863 | -52.0405 | 2024-10-16 01:02:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e0336c92-0317-36d5-ab38-1aa0d63eaaff | -3.62071 | -54.68084 | 2024-10-16 01:02:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 92c19f56-6434-32e3-961a-cc5c998d3d8c | -3.61878 | -54.66647 | 2024-10-16 01:02:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| bbca92cf-d052-3d09-9168-374e4c1338d5 | -3.61421 | -51.38328 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e71fbe9c-5959-3a31-b5c4-2f3f3d8556c6 | -3.61404 | -51.44949 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b7071e9b-6320-398b-8cc5-97d3067729d8 | -3.58967 | -51.00548 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| b8aca723-abb2-3c41-a6f8-ae3e99ec11ba | -3.58691 | -50.58068 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 65052580-e541-3230-b244-e43a8a3aad50 | -3.58663 | -51.44976 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9321a5c2-2f2e-383a-b69e-46feb782a1dc | -3.58569 | -50.57183 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 96940d8b-cdaf-3b9b-a34d-3725d9fa9d36 | -3.58074 | -51.00673 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b8a7847c-bac6-3abd-9b5a-4ba206dcf3bd | -3.57582 | -50.57962 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc34b6f4-d285-34d6-af71-8e03061a339b | -3.57458 | -50.57076 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1e3a2972-381e-3442-915f-fd580b2d03d7 | -3.57335 | -50.56191 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 93d53b9d-8729-36be-9ba2-8be460cc9775 | -3.55016 | -51.58807 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9dfd839b-2062-3ead-8920-bb3adf7b773b | -3.54148 | -51.38999 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5d80e084-7a7e-3eab-b022-083ccc8fa111 | -3.5312 | -54.86921 | 2024-10-16 01:02:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7b1a3b7c-6862-3157-b520-ed310169b94e | -3.53045 | -54.86362 | 2024-10-16 01:02:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c6ffac1b-42b2-3ef0-b69a-1818b5b26e03 | -3.51122 | -52.16497 | 2024-10-16 01:02:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 396d50f1-3c76-3f91-803b-150da0424890 | -3.50984 | -52.15509 | 2024-10-16 01:02:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 943c0a6b-42f2-3b8c-ab99-e57720bd57fc | -3.50479 | -51.59111 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 364f2337-b219-3610-8a03-0a76ac6a67d6 | -3.50188 | -52.16624 | 2024-10-16 01:02:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 2f2908b3-fab9-37f5-ac1f-d3ba53959cef | -3.5005 | -52.15633 | 2024-10-16 01:02:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 43562fff-8d97-3423-a658-6d49d8722144 | -3.49697 | -51.66895 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 71234173-bd0e-3216-9071-49c6fb45ff45 | -3.48516 | -55.45426 | 2024-10-16 01:02:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e9531343-b9fa-38bf-a5f2-70f2380cafb6 | -3.47148 | -47.46964 | 2024-10-16 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c2620f86-c3bc-3ff6-b71a-bfe00b8435bd | -3.40989 | -44.57351 | 2024-10-16 01:02:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1d2c3f41-f1d9-3a9e-8a0c-022aee4826f7 | -3.40742 | -44.55675 | 2024-10-16 01:02:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 333.9 |
| 76e169d6-4777-366b-b270-c2b480663575 | -3.34443 | -53.54503 | 2024-10-16 01:02:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 778be403-e8d2-3dda-8629-05cd0598f782 | -3.34047 | -49.15223 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5e5f024c-30ea-3b64-affb-d2bcc5b3c0c2 | -3.33617 | -53.55186 | 2024-10-16 01:02:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 98879da4-71ce-3200-8d4a-bb4e065f46c5 | -3.33452 | -53.54005 | 2024-10-16 01:02:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |


[Clique aqui para ver as próximas entradas](README14.md)
