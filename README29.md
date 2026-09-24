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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f05872b2-c22a-3342-89fb-098790421445 | -5.38405 | -46.56934 | 2026-09-24 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44c0e1c5-5122-3e12-9458-32ea46d9f417 | -4.99354 | -45.55505 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c34906bd-5247-3ca0-b60f-2c17d1555c58 | -8.12593 | -54.82655 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 888ad884-6226-31a5-ad65-654ccabcc7cc | -5.5717 | -42.73306 | 2026-09-24 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 89fe51fe-af8d-3b11-b7c1-890596132afa | -5.25948 | -49.22686 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f645d297-be06-3bdf-b1b5-62ab1c8b9ff5 | -9.22376 | -47.34412 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d16e717-73e9-317b-87f1-c5b40bfacb85 | -8.94167 | -45.9376 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 655a2c6e-44de-38f9-9382-eddf620396d1 | -6.89306 | -43.7485 | 2026-09-24 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2e76858-c588-37e2-8d55-0a869ec69b2e | -7.67909 | -45.49036 | 2026-09-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9b55841-a781-318a-b7da-4954e5b7f27f | -2.82672 | -46.7041 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a5e038f3-eda6-33f5-8d15-dbab76044132 | -7.19463 | -47.47149 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 158f9650-968a-3d84-9fcc-d073e87ec863 | -8.30552 | -48.22102 | 2026-09-24 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 792c834d-d4bf-36dd-8adf-e165a1deb35c | -7.44527 | -44.68594 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54bf4141-6fc5-3507-b276-895372f08cb7 | -4.12337 | -51.08032 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7c4a4f65-5d86-3982-b082-bc895a76b8c1 | -6.89025 | -43.74423 | 2026-09-24 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b046ca22-b6cb-368c-b196-720e792b9655 | -7.77626 | -44.77034 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a81896eb-a8cc-3bff-80e4-d0cabd7e296a | -7.41162 | -44.23927 | 2026-09-24 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b2fb526-afb9-3e30-8d7b-07382493835d | -4.11839 | -51.07573 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b9bd5751-2b77-3e34-8ca7-031359929f00 | -9.25631 | -47.34621 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8f81c55-bf5c-3dd1-8fda-b5c860cbfdec | -6.2084 | -47.4982 | 2026-09-24 04:08:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da7e4696-acc7-3358-8247-f0ce2a327549 | -9.2661 | -46.24948 | 2026-09-24 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c00fa966-13ca-3ed3-9870-dd8df434df62 | -6.61799 | -43.73191 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d853b8fa-cb11-38da-ac67-8628eda7f5cc | -6.88965 | -43.74796 | 2026-09-24 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd686b9a-0ecd-31ab-a8b7-97b402598034 | -6.60877 | -43.83413 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfd1d823-4546-3646-8d2c-1d74cd2fc8ea | -2.88753 | -54.08709 | 2026-09-24 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ac20961e-ea15-39ae-85b6-593de3c03423 | -8.00207 | -44.9446 | 2026-09-24 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51b3e31d-6bd0-3fe1-9239-3a34c934eb45 | -6.18243 | -43.25217 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7f05f1c0-0652-3f21-ac4a-2ec2e4e3a21f | -4.49478 | -42.54918 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3c6f41db-a2de-3bb2-bd27-5f44c15423c8 | -8.91835 | -50.8868 | 2026-09-24 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 670b59d2-7d14-3061-b049-42516e9906b3 | -5.78109 | -46.57184 | 2026-09-24 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd3e0d2c-0085-345a-a1e9-f1a061953fc8 | -7.42226 | -47.35901 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc47b171-b26f-3461-83f6-8a4d24292ef2 | -5.25373 | -49.23143 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05147734-5683-307c-b13f-6f9295ea56cc | -5.18691 | -42.96958 | 2026-09-24 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d9b7290-b95e-3631-b82c-6b8cd7933ec7 | -4.30277 | -49.12648 | 2026-09-24 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 803629e4-b2ac-368d-91f5-67612890fe53 | -6.72195 | -44.15525 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| c470c044-e08f-3e2d-9442-348462ac9f9f | -6.78373 | -48.68143 | 2026-09-24 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f96ec92e-4b97-3e22-9af6-d2643cf876ca | -9.22933 | -47.35957 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0555d4d3-eb84-3744-8caf-1906a3f830e8 | -6.12739 | -43.74644 | 2026-09-24 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6bd99fa-63cc-35ac-869e-d1998211652d | -6.7782 | -45.87893 | 2026-09-24 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 542be46f-9da8-32c9-8c7f-1e90dd86e7d6 | -6.88845 | -55.56732 | 2026-09-24 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08d85b23-8996-3fc7-ab9c-ff6278e7f569 | -8.06165 | -47.11612 | 2026-09-24 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94aece1c-ad66-3fa4-b7ee-06865d83e6be | -1.0237 | -53.73978 | 2026-09-24 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 291566e7-d8dc-380b-841b-94b6a9aecbdb | -7.42453 | -42.63505 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86e8426a-e0f8-3a92-a6cd-7539a1fc5bc4 | -6.91161 | -47.42924 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bbd8c36-4466-3017-be34-84dcd3c07c17 | -5.76418 | -43.71352 | 2026-09-24 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9cc333c-e038-3242-9373-4c1c48000729 | -7.67246 | -45.485 | 2026-09-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c180c57-43e6-3a59-b953-5eaf450b7c6d | -6.26452 | -43.70256 | 2026-09-24 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac853617-c641-35ec-bc04-2c8430a9e1dc | -9.26148 | -47.34 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5aff6261-a71e-3016-af22-9e4ae2a6e72b | -8.2625 | -54.78054 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 09d56e6d-8335-393a-b49f-ee6bda6212fc | -5.77708 | -46.57114 | 2026-09-24 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1cf50f9-af42-3162-ab97-6027d6d2ac45 | -8.72557 | -47.60984 | 2026-09-24 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc0797c3-9618-3d7e-b2d9-79f2ff6a6585 | -5.29967 | -49.27534 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05077cda-ff1d-3277-9360-a87a6015d69d | -6.31483 | -43.34419 | 2026-09-24 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7bb77cc7-d945-3ca8-b07e-7255e533324f | -7.26975 | -45.53736 | 2026-09-24 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f924369-b1ba-3bae-9086-0c934b9e2279 | -6.2765 | -43.2706 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52fef6f4-3fa9-3ebc-acda-1be419f8cbeb | -8.72655 | -47.61005 | 2026-09-24 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f9c60d8-30f1-367a-be26-2ca89de268af | -6.60714 | -43.73398 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82cbe0a8-7d10-3a3c-8d8c-99afbf9ba7f2 | -9.54396 | -45.36911 | 2026-09-24 04:08:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf20bd51-0bf6-3a69-ad1e-729011ffc20d | -3.44661 | -50.08615 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2255e58b-c9d5-3ad0-9e37-29452d07997a | -6.27312 | -43.27007 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a60aa5b-079c-3e3e-80f5-c5f8a7cec840 | -3.4477 | -50.07972 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e29b2795-e1af-3783-b886-6f60fa9ebf97 | -6.57927 | -44.14419 | 2026-09-24 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4435a1b-5e8a-33ef-b100-59f6c900bb51 | -4.99885 | -45.54637 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7b6fa123-8869-3ca3-85a7-2486a4d9d05f | -6.00333 | -44.10706 | 2026-09-24 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4241418-5a1b-310f-b066-334879a1b240 | -6.77995 | -48.67607 | 2026-09-24 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 33885ec0-5569-3212-8d6f-ffb11379dbff | -4.56411 | -44.07746 | 2026-09-24 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5dca843-cd56-34fb-bb1b-e81e6ad2e26b | -6.7845 | -48.67681 | 2026-09-24 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0182b020-618f-3f92-994a-4a536cedeafe | -5.95183 | -51.79112 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73a4d978-aff7-388a-b19e-a0ba632644ce | -8.74577 | -44.26403 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1e6cbeb-52a4-3074-8e23-b1785df2e5d7 | -7.42167 | -44.80992 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45ceb1f7-ec5b-31c4-bffe-5cb352eb1a99 | -4.53848 | -54.97033 | 2026-09-24 04:08:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 19cff727-7aa5-3fa1-bb6d-24f351e54818 | -6.4299 | -48.46517 | 2026-09-24 04:08:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e0311e3-eff5-3bf7-a7d3-e56a096d9e85 | -8.82267 | -45.92938 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b7b4b8a-369e-3bc2-b128-d89e94a10ae8 | -1.19835 | -54.14223 | 2026-09-24 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35d199ee-2193-34e3-ac20-ee1d14b42a83 | -5.77683 | -45.09543 | 2026-09-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| df79e64c-1951-35b1-a987-c13edfb7d10f | -6.18759 | -43.34981 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8d7a372-62b6-3bf2-9e23-5da2cf0ff4b3 | -6.28819 | -44.09959 | 2026-09-24 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 877c4b38-743f-36e9-b7fc-a9f257365c02 | -6.21969 | -45.30331 | 2026-09-24 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b837617b-8bdd-35c5-9f35-20eab6215a5d | -7.48593 | -46.15655 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05cdeca8-3848-3ece-83ef-a100cfdb72a1 | -3.18182 | -48.01918 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9bce3fa5-65a1-34f6-bbfa-c4c4176485bc | -9.26458 | -46.25867 | 2026-09-24 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 31fa6060-2521-3036-b61a-ea768cbbedc2 | -7.19372 | -47.45138 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20956f84-bd66-3217-afcc-bcb7750af278 | -7.19058 | -47.47015 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ae05d49-a659-3cab-8bfd-ce4944956a98 | -7.36106 | -42.06628 | 2026-09-24 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5e73d6c1-1727-381e-8139-2b806472cf4a | -7.28984 | -45.4152 | 2026-09-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88d6aaf5-1b52-3726-9b44-4e6dda6e8c20 | -7.48514 | -46.16128 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7db2de5d-145e-3a90-9eef-7297706d0697 | -8.91773 | -50.89016 | 2026-09-24 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36b1d8dc-5c2f-3ab4-a08d-2114c18941f4 | -7.09563 | -52.76023 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25d5f707-4e1e-3b72-9b28-b00367cdea57 | -5.57833 | -42.3021 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 515552a4-f68d-3dfc-8c26-9d2f9b1d70a9 | -8.39149 | -46.29881 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3bdda043-7963-35da-8ec8-cac12eee4552 | -5.38808 | -46.57001 | 2026-09-24 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc0f86ae-56ae-3eae-8313-ec0380e303d0 | -5.77315 | -45.09487 | 2026-09-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 011b73e6-47a6-36df-a2fb-590e49abcb8b | -8.39226 | -46.29414 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c5c0b260-5295-3f64-bca9-a5158d2fdcfd | -7.48132 | -44.57372 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e746201a-c74c-33fb-9bc7-2556a2f14fbd | -7.19526 | -47.46774 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6fefde48-87f2-3e68-aa0e-159d148c9e17 | -7.42912 | -40.23084 | 2026-09-24 04:08:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 73c7f6c9-9cf2-3c07-a135-d45e755a2e17 | -3.96453 | -48.12628 | 2026-09-24 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d5998a-9103-3e61-b159-111183cb855e | -7.37238 | -45.95236 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 244087a8-6963-395c-b46d-72df6eb22bc4 | -5.95727 | -49.97026 | 2026-09-24 04:08:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b641846-ff26-3b6c-a042-3ce6e9714acf | -8.45888 | -48.68971 | 2026-09-24 04:08:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README30.md)
