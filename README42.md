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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f63325e8-0e35-3bf2-95ce-e8203e976e18 | -3.70055 | -47.13556 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 051e2e72-94ae-3f03-b8f0-7f2bb7b058fc | -2.57354 | -51.83555 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8c64378a-5798-3d15-93d4-68100fbef6cf | -2.92926 | -48.0116 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b597154d-196b-3236-b7b9-b5077e57d7be | -2.76279 | -47.90017 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7e8b0d7-51ab-30f7-84c7-9087be29be56 | -2.77373 | -45.48568 | 2024-11-30 04:40:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3482aa9-67b6-37a7-a6a9-40dc380376de | -3.38232 | -50.33386 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40b4d08b-4cbf-3bdd-930b-ef232909d820 | -3.25775 | -53.64461 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7fc5885c-3853-3bb7-9d6a-b4bb717af91c | -2.38032 | -53.6805 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17aba7c7-b39e-3e6b-b0ca-a30194e23420 | -3.84542 | -46.52679 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bd02d0d9-c1ac-3f36-a089-3991a546670c | -2.19314 | -48.41441 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebb1bace-6f3a-323e-a8dd-a5dfe9cfda81 | -3.46985 | -54.53941 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4c4d39d-1b53-34a4-b0be-c693208cf16a | -2.92593 | -48.01109 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1593a03-921e-3d3c-84ca-a205f28bc05b | -3.6753 | -50.24825 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b24f8e31-f77b-3beb-8a01-9c80e7af9382 | -2.75007 | -46.10728 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bb090fe-44f6-30d2-a6ac-ebf2a4331009 | -1.26994 | -47.87852 | 2024-11-30 04:40:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdadc57b-176e-3f0a-bb32-9d6a6d06fbcd | -4.6822 | -42.37073 | 2024-11-30 04:40:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 350ceada-0e70-354c-bacb-ee5f0c677501 | -2.83816 | -49.1207 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce6220c8-0620-3284-b567-b2e4a8373e8e | -2.6931 | -46.29191 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a565605-2fdf-31ec-8104-b847e68d34c5 | -2.86865 | -48.09495 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd9e5e71-5837-3c80-8ffe-847ea75a38d1 | -4.2402 | -45.76431 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34459b4b-216b-30c1-9bde-c7a6df702f6b | -3.29972 | -53.836 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a51d109-a383-33b2-806a-17717448931b | -3.21816 | -54.08592 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61ed499b-1e67-3056-a58d-eb0f2f6bbcda | -1.62777 | -52.37451 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46539fc5-153a-3525-835c-b6f49c02a2dc | -3.29693 | -50.22913 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5edd4070-8fb3-3132-9c99-50ff0f126d41 | -2.27553 | -46.43622 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66d1f489-60cb-312d-9c9a-9cdd4a324183 | -3.9919 | -41.51386 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 601e71c1-6520-39fb-bb6e-7f6a4590311e | -5.043 | -43.62119 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ba79982-2f19-3544-bea4-877c5e7af36b | -2.67232 | -46.54516 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4289f890-d1b4-345b-bd04-a4603e64c53d | -3.68915 | -47.14136 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57215f77-8fee-34f0-bb9b-01b6a1f24ee4 | -4.11277 | -50.77474 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b1fb554-d2b6-3bbc-b8dc-f965704267d7 | -3.50186 | -53.82829 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af71ff4a-8887-3eab-8030-55b596a600e5 | -2.75341 | -51.66481 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b271a12-7735-3249-99f8-c153d3b4fccd | -2.45108 | -46.52395 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c24f7a84-ded3-382c-b19d-6d7d45d21261 | -3.70624 | -47.14404 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddbe5bed-38ed-315b-8d82-3a0bbbbe180c | -1.7062 | -52.4672 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 10cf644d-ee77-36fb-9c11-80d22b2eb578 | -1.70447 | -52.4458 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c8501fa8-b5e5-3ec9-8964-601c550149ad | -3.35432 | -49.75667 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28b7470d-b880-363c-bd3e-19418debf006 | -1.71542 | -46.21987 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc17e43c-913f-352f-827b-9456fc977e58 | -4.10802 | -46.11124 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49ac9de9-6114-3c34-adbd-b9ad76b5ee68 | -3.43585 | -50.03815 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c36e6494-fccb-397e-9607-54f279a59d31 | -2.80498 | -45.93905 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca2c8e7e-0b96-39f8-b968-065603aafe1a | -3.26631 | -45.37067 | 2024-11-30 04:40:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edc13a86-35c8-3a9a-94f2-4fe621c70e4d | -2.57014 | -49.0962 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22e4d42c-bb02-30ad-aa63-3ae1c973c510 | -6.90814 | -43.53423 | 2024-11-30 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f9732949-0e20-38ed-aafe-933e7ed1b9ed | -3.70682 | -47.14034 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72f05add-e914-3ab3-a3e8-6d20a0e304cd | -3.61924 | -51.36792 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 605ac6ed-6c07-3bcc-b8d0-3d1fc61f2178 | -1.25868 | -51.74611 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03b82da1-801f-3d36-90d9-d4afc7503711 | -2.75249 | -47.90237 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4beccbe2-2eb2-3241-816f-6552630be2b5 | -2.902 | -54.15609 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b70f38e2-498b-312c-a262-d44551ddbb32 | -2.71615 | -46.21127 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e9addb6-50c4-3384-94b2-0f61b3a7aaa4 | -3.10751 | -53.27187 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ccc1e6a-870b-352c-8ed0-9eb07ee59ee0 | -3.87236 | -49.98812 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9440b32-7c3f-3c62-b6e9-8b4d4c8483f5 | -2.05372 | -48.48071 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa9f7e4-50db-3517-b2d8-effa00cc2f04 | -2.37459 | -50.40145 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2afa63dd-0ef0-399c-904a-1e9a7bdb7e96 | -4.87447 | -41.29537 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a1e9b2c3-cceb-38a1-b2a4-3eae15e35293 | -2.60008 | -54.08658 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 176652a7-7f4e-3afb-b42e-4406eeb7f2b8 | -3.96262 | -46.91453 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6747f37-9f89-384a-a286-8531ddcde077 | -3.04739 | -50.27797 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b295a470-4762-3c77-9543-a15884f9d7e1 | -2.44692 | -48.44353 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ea8ad96-5727-36e6-9bd9-30a7f51c9fbf | -3.26408 | -48.7653 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c1187d5-e734-3d7d-b130-5e948dc8fc9b | -2.23444 | -48.27981 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73fff31d-1523-3d59-8274-db38d1a77de1 | -3.0917 | -54.01777 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fda6619-c7ab-3c7b-ac6f-df9eef528150 | -3.80554 | -46.68476 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 534f4c8e-8ba0-3ecb-813b-2eff4b30e2f6 | -3.66023 | -50.23509 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d075611b-f162-3047-994c-88ea0770f020 | -2.81956 | -51.95642 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 147ad3b2-c971-3dc4-81f4-ba933fc76f73 | -3.272 | -50.56229 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c540b45e-d703-3812-adfb-8a62be77837b | -1.29911 | -55.74122 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 970b162e-566e-3df9-9169-5b7dd324fc0f | -3.14375 | -49.21106 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fef8a8b-1c14-39c2-8905-06e27cbda812 | -2.44514 | -50.37163 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ca3fca1-4837-37c2-a94a-baef32ca11ce | -3.71252 | -45.68848 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1102117-e9c8-3d90-bcdb-363f8f031982 | -1.34458 | -47.09584 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abc88140-f457-3149-bdfb-df0ed8274126 | -1.61216 | -52.29155 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6bc7d551-036a-395e-b56a-0d558db99c01 | -2.22755 | -46.40147 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c90b9d3d-00f6-3997-aecb-ae4c65fd3ff2 | -3.27703 | -50.59639 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f36e61c-4ebb-3796-921d-1e6600e40090 | -2.46547 | -46.5456 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8fbabb9-e242-3497-b06c-f54eefc96d74 | -3.89423 | -46.62985 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bbbd7cc-bd37-3498-9333-e3bbd3f9ee3f | -3.24344 | -53.93084 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 943c8311-925d-35e6-8be7-080fffa995e8 | -2.94001 | -49.44694 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2acf8cfa-a8d2-3f2e-ad3d-b8f8f9b9bafc | -1.12095 | -48.33132 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41bead7b-5e7b-32ff-a2e5-2240246ece35 | -2.58105 | -49.22116 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cac4bab8-1bd4-3450-b243-bb11aabf7d4a | -3.05655 | -53.22002 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad1bea21-677a-373d-ae95-a9d302e80d75 | -3.76938 | -51.61524 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3335c7ab-e1c3-382e-8de7-1791eb4cb255 | -3.05172 | -48.49224 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7118c510-c47a-386b-a484-af5e64c2c1ec | -2.02226 | -51.19335 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 032bef37-259d-3d9e-9864-56fd74c05b4c | -5.65648 | -45.20028 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72bbeccb-bc68-3b78-9539-e5bf4e04fbbe | -3.84365 | -46.56234 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 601ae5af-2fc1-3a21-a364-e43f2b0f6aab | -3.31596 | -50.50264 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eb49db3-cf34-39de-986c-18c35e0a1d2f | -2.31983 | -50.65512 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58bec986-d71f-34d9-9d96-764503e311cc | -3.29051 | -54.12988 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8904c77-d7bc-3215-90fa-3520fef0e6e6 | -3.07251 | -49.10078 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84b9745c-8cc3-346c-ae4f-868d7fa7ec91 | -3.58204 | -50.3391 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0dfde548-acc9-3793-936f-320436952e2c | -3.74117 | -50.79521 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31c38fc8-babc-34f7-9bf9-606ba02a84f9 | -2.33247 | -50.50686 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4762b035-6d3d-3220-bfe0-d97237e2a7aa | -1.37314 | -53.64085 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed0c3cad-ce10-393e-a97e-c556acdf788f | -2.7983 | -53.04066 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb3027e-7bae-30f8-8782-d349593147af | -2.95321 | -48.33919 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa39a22a-1421-3627-8c70-722d94393ee0 | -3.15649 | -50.62626 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce4d220d-ebd0-3c90-acb8-612e01e1a307 | -3.28099 | -50.5933 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9501fc21-ac6d-33ef-a9e5-9fd052ea9ea9 | -2.8376 | -46.8625 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d52aad7-02f0-3517-a454-2c1b317cc6f6 | -6.13648 | -43.94907 | 2024-11-30 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README43.md)
