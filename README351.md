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

## Dados Diários - Página 351

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50b25d68-0e2f-3d66-bc87-7bf4e81b100b | -4.84314 | -40.39564 | 2026-10-08 16:39:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 6325964a-7356-3155-839e-3e22c34deca3 | -6.16159 | -52.6531 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 580e2da7-e153-3110-846b-bbf6009e4e56 | -3.82159 | -44.60296 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8bca5d79-59bd-395b-98b4-e196cf3de4f0 | -3.08899 | -57.66335 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 624b90c1-dce5-3d02-8495-c129402466aa | -3.99412 | -56.25531 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a7a625ac-40a9-32a5-92ce-793a8c76f0e1 | -2.22482 | -60.07961 | 2026-10-08 16:39:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b63280c5-6fdd-3b8d-ab4e-f891123b9bea | -3.09709 | -53.94171 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e20ee7da-718a-34db-a09b-c37c588fdf06 | -5.42134 | -45.86598 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 152fbfdd-af18-3456-a4dc-13341e8824da | -5.96218 | -45.69769 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 72d63714-2891-3f13-bc8a-4a4484248055 | -6.06819 | -44.64855 | 2026-10-08 16:39:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d32121cb-dd14-336d-bf40-4138d46fe065 | -2.56303 | -57.43272 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 71c9917a-6e1a-36c6-834e-dca83cafb4ed | -6.05168 | -53.48194 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| db907c0d-64fb-3a1a-b94c-7215d44c576f | -4.52275 | -44.01599 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0d2b5974-2249-3b21-b929-e5432ba48bbb | -3.18008 | -54.74157 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4187d9de-faa1-3ece-9c98-55c886d1093f | -2.4877 | -57.787 | 2026-10-08 16:39:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8528cd9b-a00f-354b-9fa2-53b447ac725b | -3.31299 | -54.70167 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d7bc2e55-17b2-3bf9-962f-3822a60b6f05 | -2.93905 | -57.92091 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 943f134a-d313-3da9-ab96-0452355998da | -6.83586 | -52.86388 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 655af218-a95e-37f8-aacb-c8d629983e98 | -3.0085 | -54.79426 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ac7d224b-20b6-35a2-86ed-bda816c00f36 | -1.96441 | -54.33372 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 62f49c79-b352-30d7-9fd7-92a02ef1ef71 | -3.81819 | -44.62622 | 2026-10-08 16:39:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b15ce7e6-5789-33f4-9aef-3f739bf1f018 | -2.08955 | -46.58464 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| cc53885e-2281-3162-975a-0a1266920632 | -3.22708 | -53.37987 | 2026-10-08 16:39:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3dcc14bf-de25-335d-9292-117e82753b2f | -6.51283 | -55.40248 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 57051d16-5266-300d-b9b0-1259ca665100 | -4.36592 | -40.41181 | 2026-10-08 16:39:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 14329241-f243-35b4-b4e0-abb1f85089d1 | -3.0233 | -53.94444 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 85e9da06-d46d-3a69-9534-bc06eb670aeb | -2.9967 | -54.06811 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6a45802e-18d3-316d-bba0-bcba1170e460 | -3.5721 | -54.48452 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 071cc1ca-d133-38b6-9eab-ef759b555be5 | -3.00583 | -54.09005 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| f000cfc0-a0fb-3852-a9e9-1f623dcc4d84 | -2.57437 | -56.17989 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f6c98153-3d1c-3f70-9513-29c6317501e5 | -7.22434 | -55.09629 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8f964584-7871-33b3-be2d-74b3117f169d | -2.73476 | -54.11228 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 206.6 |
| a1747515-12b0-3a01-a6aa-d19ba4215e6f | -6.73738 | -55.1444 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 08dd5b64-2120-3ba1-8a5b-3b3256baf074 | -6.14345 | -51.6628 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 353c4215-44ba-3f5d-8517-ba2ac713d07d | -2.48479 | -56.13661 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2093f3c3-d875-31d0-9125-91eea25d0cff | -3.02125 | -54.03889 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 2af14d17-3b18-3bb1-ae5e-4d1499847213 | -4.54963 | -54.97093 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b67f9223-31ad-3068-8b16-92234ed4cde4 | -2.83215 | -40.23148 | 2026-10-08 16:39:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 58a317df-f0f5-3986-93ab-fec20760691a | -5.30513 | -45.72838 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 13cc4e42-f329-341e-874b-b44617826fb0 | -5.27862 | -45.73242 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ef7d4bf-2712-3357-9cff-94f2c758c8e8 | -2.85177 | -57.46194 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2a9df2ac-36d3-3115-a941-bcace08c7f4c | -5.7111 | -53.45456 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b9f1c5b5-2fa2-3e45-8e85-3838e544e499 | -2.92689 | -54.11964 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| bb431431-f5b7-3f50-83c7-32889274557d | -4.92821 | -55.85586 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a930df7-83ad-3df5-80e6-a35aebbf36c7 | -2.75442 | -54.1146 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 377fd160-d158-3964-94d6-bb73cb1bba2d | -2.07536 | -56.87299 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 66ee42c0-ae8b-3507-a49c-1fe70ea034db | -5.9399 | -44.32363 | 2026-10-08 16:39:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4d958617-605d-3ebc-b167-a467e20f51cf | -3.11235 | -50.27658 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 272f3c8e-257c-398c-abdc-dd7f53492d0e | -7.08733 | -52.68757 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 2b2b8c88-f69c-37b3-9552-aa0f10d2ca0d | -2.07527 | -46.57975 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 3e3da735-28d2-3f3e-b39c-ee20aca45ccc | -1.21098 | -55.69553 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 37879211-f519-302a-880f-8a3f4479991c | -4.37186 | -41.8321 | 2026-10-08 16:39:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 6a87d771-be02-351a-a605-871fa3532f2f | -6.15071 | -52.64084 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f15c6bf5-37ad-3650-9fcd-8bf8694987e1 | -7.22997 | -55.17724 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b5fded20-100f-35fc-b2b4-3981a1656172 | -2.57926 | -56.17551 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 08de0e62-7fc7-3790-93c6-05c473d6c75f | -2.60755 | -57.58223 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dc0f5720-5c65-305f-a7cf-63823b74f7b3 | -0.77621 | -49.26621 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42d48299-000b-36b1-ae0b-9859982ecdaa | -3.00911 | -54.07921 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 03ec2af5-fbae-36e7-a4a4-410cd3db7f06 | -6.00026 | -55.67827 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13e61a78-4285-3289-b421-6fe0d6c5e83c | -3.51795 | -44.31964 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7f475e99-c5a7-3bd3-8ac0-13c838da5994 | -6.13781 | -53.50657 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c96f0df1-c013-3839-8079-bf9f08d6e38a | -3.19277 | -43.3744 | 2026-10-08 16:39:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4b74a9f4-88d7-310c-b3bb-42e1521ceb07 | -6.14996 | -47.92856 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1949075c-227c-3477-af2e-c45a0b4ddd90 | -3.51743 | -58.02383 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bc3ea85a-4a30-3253-8f1b-a9a3741061a1 | -3.36818 | -41.3661 | 2026-10-08 16:39:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 39.1 |
| b1fd0daa-a429-3c74-80a8-07b29aba18f9 | -3.45759 | -59.98497 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7de175d7-bb64-3382-b9dd-cebc5b977bc8 | -3.24982 | -57.85978 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 98f20747-2891-3c30-a6ec-2c1e1fce8f6d | -7.189 | -52.6135 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| b629b2bd-1ed9-3a01-9343-04e0b286fce5 | -2.09843 | -46.57626 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 84e99c17-af8c-3ca2-9bb8-91c59675304f | -2.38967 | -57.23055 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bcb23220-81df-35ae-8d14-8c9d784abf8d | -0.71623 | -57.43459 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5f573af4-6af6-3131-a9a7-e589589972b3 | -2.88716 | -54.18594 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 78f7c510-7d78-31b7-bdfe-f3cfa3cfac07 | -2.90359 | -54.02548 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a205a754-fde7-32e4-8927-d9c3474ee74b | -2.47354 | -58.07796 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3152a4a7-ca1d-33a0-bbe1-fc08327b8ffa | -3.52852 | -59.34747 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 7b98e49f-611c-318e-9e97-95aeb7bf8295 | -3.64656 | -59.16966 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e715b1e1-a407-376c-8ec4-56516c0d495d | -6.35723 | -49.7136 | 2026-10-08 16:39:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 26dd6612-4f79-3084-9fca-4968fd5a0a7e | -3.84426 | -55.83464 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1abe234c-f0b8-3b2b-9459-549f6a66b232 | -1.37845 | -48.04259 | 2026-10-08 16:39:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e799120-bcad-36ee-ad08-48c03560270d | -3.11997 | -54.1724 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 68779c8a-bec8-3516-81e4-cc93c8574f58 | -5.78479 | -45.38147 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| fb4129f1-05c1-3c9b-8683-0a3db6f71900 | -3.73032 | -39.53214 | 2026-10-08 16:39:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 527cae10-13b3-3888-bc09-e2f5e9217812 | -6.73784 | -55.1478 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| a61e9eca-49f8-3234-97b7-5ae5fb433862 | -3.25563 | -54.02846 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 1caacd40-51ef-3471-81ec-f9e463d72614 | -1.56603 | -48.22537 | 2026-10-08 16:39:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 716e3ab6-3e6c-3492-8baa-3c8fa8ee2f04 | -6.34503 | -52.57382 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| efd49ee1-82eb-36fa-866a-b481bff855d6 | -2.73301 | -58.09385 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2bf9ddd7-e4b2-3f21-a292-2f95dfd7e3cf | -7.21403 | -55.10152 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 26670c1e-90db-3e01-ab8f-01bb5ee703f0 | -3.46875 | -57.90337 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 218adf25-2511-3e4f-8606-a98d68095161 | -4.74688 | -55.6563 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7ef19201-33de-30a4-bd6a-2df4580ce699 | -2.4299 | -45.30289 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 892e648e-5341-3ddc-bba2-2c9044d7f1c7 | -3.40365 | -56.98415 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cc9039dc-0f4f-3135-975e-8d4bb5ecd320 | -6.86401 | -59.34629 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 16ca8f2e-cf87-3be0-b9c3-da4108641551 | -2.61452 | -56.48101 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 557c260e-7c8b-39dc-93a4-fb02c008f860 | -2.92619 | -54.12286 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e24c889f-462b-3a00-84ed-c6620f21598c | -6.20462 | -52.86225 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5d5a12ac-191d-34f6-b5ca-0eaee551667c | -7.19571 | -55.12896 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 56eff8a5-782c-3e06-ac6f-fba2cb95ef1c | -2.88502 | -59.2022 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c7ea721a-b3e9-31f2-8d68-92c3ec5c4763 | -7.24039 | -55.13252 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 1102df15-a57c-3460-92fe-232c21a766c8 | -1.50717 | -54.8102 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |


[Clique aqui para ver as próximas entradas](README352.md)
