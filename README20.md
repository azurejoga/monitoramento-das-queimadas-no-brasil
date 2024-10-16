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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 716e3da3-6639-3154-b6b7-8fe40f60a196 | -1.7738 | -56.001999 | 2024-10-16 01:37:54 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37c42760-49d8-3c0e-9411-081e069fc475 | 1.9434 | -60.8633 | 2024-10-16 01:39:13 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c8341820-20d0-33f4-ad69-8a7fe809e679 | 1.0016 | -52.2164 | 2024-10-16 01:45:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 6d4be646-8fea-362e-a1da-c2d916be53aa | -2.5444 | -47.2231 | 2024-10-16 01:45:20 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| bbfa15ef-4371-3f76-97af-ea78b34a0d50 | -3.1098 | -54.2464 | 2024-10-16 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 75b47016-7df8-3d13-ab9b-1c0bbd1b2023 | -3.1099 | -54.2263 | 2024-10-16 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 233.3 |
| 84d3b73c-92ea-33cc-8433-734b4a120a92 | -3.11 | -54.2063 | 2024-10-16 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| a3a91fff-40e1-3137-b034-e36b3a3f526e | -3.1282 | -54.2459 | 2024-10-16 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 5ca44a8d-d55c-35f0-a452-e092623cd25c | -3.1283 | -54.2259 | 2024-10-16 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 79569dad-88b0-3068-81e6-3cf40ebdfe36 | -3.2226 | -48.9092 | 2024-10-16 01:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 61237192-9891-37d0-9507-b2443572ccb9 | -3.4104 | -44.5599 | 2024-10-16 01:45:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 65.5 |
| af07827f-c37d-3b62-970a-f7f97fa8a7e9 | -9.9983 | -48.6295 | 2024-10-16 01:46:02 | GOES-16 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 2d8050b7-d690-3c10-a8af-ad63a15832db | -10.2439 | -47.3046 | 2024-10-16 01:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| b8697740-c194-3df9-ba0a-1b7139a4882f | -10.2442 | -47.2824 | 2024-10-16 01:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 1046058e-37c4-3a7b-8f4b-d403177c8b51 | -10.2628 | -47.3024 | 2024-10-16 01:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 91fed60a-e896-390a-82c6-5ee3a1b64929 | -10.2632 | -47.2802 | 2024-10-16 01:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| babd5b36-4608-33ca-ae8d-5b374554ddb0 | -10.822 | -49.256 | 2024-10-16 01:46:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d9e245ef-e019-34d2-9c66-fcea7fdc588e | -10.8224 | -49.2343 | 2024-10-16 01:46:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f3daf31c-e051-37c3-a7a9-0a0979b3c407 | -11.6915 | -65.2432 | 2024-10-16 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 0ef27676-0ad1-3ba0-bba0-a88d52ea6adf | -11.6917 | -65.2243 | 2024-10-16 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 2cbf32b2-ed34-3a08-911c-e7834ff411aa | -11.6918 | -65.2054 | 2024-10-16 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| c374720d-f02c-3dfc-b4d0-bff025566da8 | -11.7103 | -65.2424 | 2024-10-16 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 5127d3cc-fd0c-364e-88ab-a8bde9af32cd | -11.7104 | -65.2235 | 2024-10-16 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| b834e93e-dd07-3fee-9ad2-0f74d4d7d619 | -11.7106 | -65.2046 | 2024-10-16 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 38050cab-aa9a-3e77-8194-ca08e6d7e674 | -12.0427 | -46.7161 | 2024-10-16 01:46:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 672a9315-af99-3031-8a6f-4c5ac932f798 | -12.0431 | -46.6935 | 2024-10-16 01:46:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 84d73fe5-5de0-3e45-a15c-4db13117f9c5 | -12.0619 | -46.7134 | 2024-10-16 01:46:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 8a7b17bb-1d1e-3809-85cd-01964f7e522d | -12.0623 | -46.6908 | 2024-10-16 01:46:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c7e74440-8018-3ec3-9ecb-dd5f60a6edd6 | -12.4925 | -47.2818 | 2024-10-16 01:46:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 4aee63b7-78a0-339c-9f2a-a2af3a9b1ce9 | -12.3795 | -63.7103 | 2024-10-16 01:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 88.8 |
| e1c57d64-d11f-3465-a3f0-f860ef112277 | -12.3983 | -63.7093 | 2024-10-16 01:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 251a1178-3ad7-3f31-9ee1-62d4dcce3346 | -12.4602 | -63.0361 | 2024-10-16 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 91349f06-adf9-361c-a0d8-99f77005c365 | -12.4979 | -63.034 | 2024-10-16 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5690673a-9bfd-3daa-97e0-37dc7571a0af | -12.4981 | -63.0148 | 2024-10-16 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b7a9126f-083f-3a09-9824-241a657f0931 | -12.5168 | -63.0329 | 2024-10-16 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e892e428-0c5c-3c02-abfd-6262e4741c20 | -12.517 | -63.0137 | 2024-10-16 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 3542a43f-bd9a-3197-8902-d01ac219ed36 | -12.7633 | -62.942 | 2024-10-16 01:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c9faf164-8c7d-3606-9c64-277b899333db | -12.7822 | -62.9409 | 2024-10-16 01:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 13ba1444-dcf1-35e6-a49e-091ee88ca74b | -13.383 | -46.947 | 2024-10-16 01:46:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 76762645-a782-375a-a58b-ea8bb6df3aff | -17.2439 | -42.6575 | 2024-10-16 01:46:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 67ac8468-fcf8-39b9-940f-e8240e0dc013 | -17.2639 | -42.6527 | 2024-10-16 01:46:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e101e8c9-8e77-3d0d-8282-a9c0a57a9bcf | -17.0066 | -58.2934 | 2024-10-16 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 47a34f0d-b9e4-30f0-82c9-3679d4e036f0 | -17.1754 | -57.4995 | 2024-10-16 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 1bdcbcbc-508c-34ba-834a-4b9469ab4807 | -17.1951 | -57.4972 | 2024-10-16 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 14b23e82-9ea4-3491-b298-003ad6446d8c | -17.1954 | -57.4767 | 2024-10-16 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| d2151d62-0f7a-3c7b-86a2-8d374ef5d46b | -17.2081 | -56.6946 | 2024-10-16 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| bb078097-ffaf-3e18-944d-bfa4450f0c05 | -17.2177 | -57.3102 | 2024-10-16 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.9 |
| 2de6a863-e284-3b27-baf6-cfc38789a582 | -17.2373 | -57.3079 | 2024-10-16 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 7898b953-da87-3db4-891d-aa95d025bbc6 | -18.2742 | -56.5795 | 2024-10-16 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| c11da1b0-0aaa-3276-b0ba-28e4697a1b52 | -18.2746 | -56.5587 | 2024-10-16 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| b0b419be-2707-3450-9a4b-679a7fa5e090 | -18.2941 | -56.5769 | 2024-10-16 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 4c12082e-3874-3245-8a74-69f02a9b1740 | -20.8536 | -49.8742 | 2024-10-16 01:47:01 | GOES-16 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| 5cee25f3-8c52-3f5c-9b07-79fe9dcfc746 | 1.0016 | -52.2164 | 2024-10-16 01:55:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 41.7 |
| e3a765c6-2699-35d3-8390-39b3e7941e3c | -3.1098 | -54.2464 | 2024-10-16 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| a33a8fc9-fba1-320f-b931-9e037f6cf282 | -3.1099 | -54.2263 | 2024-10-16 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 164.7 |
| 35f68ce9-95a3-3a86-8cc1-d3c982f0b719 | -3.1282 | -54.2459 | 2024-10-16 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 894e0fad-7f1b-32b0-a2e4-a62bff8f54dd | -3.1283 | -54.2259 | 2024-10-16 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 215.1 |
| 89f3c960-d4e4-3d03-a358-1d3666b4b240 | -3.1284 | -54.2058 | 2024-10-16 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| f316ed8a-e701-38c7-8482-d3ff9a0c7207 | -3.2862 | -47.133 | 2024-10-16 01:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 6039d462-4678-3370-b1be-c38a103522c6 | -3.4104 | -44.5599 | 2024-10-16 01:55:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 04415f6d-5e6f-332f-a4b1-5d8469fd2453 | -3.958 | -46.4442 | 2024-10-16 01:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 117.4 |
| e097aa31-0993-3ad9-b1cb-263d2d1a9dc0 | -3.9581 | -46.422 | 2024-10-16 01:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 29e28f58-4475-321b-bd0d-0bba17e265fc | -10.2439 | -47.3046 | 2024-10-16 01:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 3ea86c26-8519-3d29-9536-798981e7ec92 | -10.2628 | -47.3024 | 2024-10-16 01:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 50e91fe5-8a52-3d6b-942d-45fd16da4dcc | -10.8413 | -49.2322 | 2024-10-16 01:56:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 018d1431-67f4-3511-ae77-267a9f463c80 | -11.6917 | -65.2243 | 2024-10-16 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e2697aab-efeb-37dd-87c4-0048cb7455f9 | -11.6918 | -65.2054 | 2024-10-16 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 96ad3222-a5ae-3f8e-92c1-2cce77016682 | -11.7103 | -65.2424 | 2024-10-16 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| ca70817f-ddcb-35f6-b57a-05e1de375f59 | -11.7104 | -65.2235 | 2024-10-16 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6054dc8d-d17c-350a-8654-59b9b97551bf | -11.7106 | -65.2046 | 2024-10-16 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 0859dc8f-591b-3b1f-ba8f-62ddbde8f0a3 | -12.0427 | -46.7161 | 2024-10-16 01:56:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 538f7f52-53ea-3850-92d3-1bca5fb627ca | -12.0431 | -46.6935 | 2024-10-16 01:56:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 3315cdcd-40c5-3377-9c11-d8fd892e5612 | -11.9381 | -64.8729 | 2024-10-16 01:56:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| bae5ca69-9743-37af-b2ed-339a19d576bc | -12.4925 | -47.2818 | 2024-10-16 01:56:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| cd96b3fb-c7d7-34bc-a521-315883ba64c8 | -12.5168 | -63.0329 | 2024-10-16 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7d3ad941-f2d0-3470-b467-d913c7465772 | -12.517 | -63.0137 | 2024-10-16 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 082283ff-33a0-3fbf-aaea-b9a72f4ec022 | -12.7633 | -62.942 | 2024-10-16 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f2295a1e-bf8a-37ea-8887-88f97ae9030b | -12.7821 | -62.9601 | 2024-10-16 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b533147a-0820-3fd2-86d3-67ee668e629a | -12.7822 | -62.9409 | 2024-10-16 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 9e1598e5-7626-3cb2-a258-c0db99e55059 | -12.7824 | -62.9217 | 2024-10-16 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 26aa31ba-f6eb-3557-9752-d3db67631f2d | -12.8012 | -62.9398 | 2024-10-16 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a815add9-31e6-3235-869d-6ef7b8bda148 | -13.383 | -46.947 | 2024-10-16 01:56:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 55e7d832-948a-3620-9260-09f41c6bd723 | -16.3226 | -57.0662 | 2024-10-16 01:56:38 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 602bfaf9-d61d-3bd6-bcc5-fc473be5eccc | -17.2439 | -42.6575 | 2024-10-16 01:56:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 2bfb3908-536d-303c-b010-b54f4acaa439 | -17.2639 | -42.6527 | 2024-10-16 01:56:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 53495855-a853-375c-979c-62a86b8a6c0f | -17.0262 | -58.2912 | 2024-10-16 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 081c9d45-1e90-3a53-ab5e-4b27e1829281 | -17.1754 | -57.4995 | 2024-10-16 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 0e23268e-bc62-3a20-8ab6-5d759a71f2db | -17.1758 | -57.479 | 2024-10-16 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 0120648b-75e8-3754-8cc2-1000bdae8cdb | -17.1951 | -57.4972 | 2024-10-16 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.7 |
| 5ccb4707-ceb8-3d77-90be-90bd98d55f97 | -17.1954 | -57.4767 | 2024-10-16 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| d359790e-2606-38dc-8821-18a674c1eccf | -17.2081 | -56.6946 | 2024-10-16 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| b6fbfb59-79c6-3380-98b6-9946f07be860 | -17.2157 | -57.4334 | 2024-10-16 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| b78ffd0b-8d64-3186-9803-5969c1be96d4 | -17.2177 | -57.3102 | 2024-10-16 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 55dad844-ed3e-36aa-8b4d-4500c6a76aa8 | -21.0877 | -51.067 | 2024-10-16 01:57:02 | GOES-16 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.2 |
| 24468270-f918-3480-a106-bdb60fd461b3 | -21.0882 | -51.0444 | 2024-10-16 01:57:02 | GOES-16 | LAVÍNIA | SÃO PAULO | Brasil | 3526506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.9 |
| 4cf46977-30c5-3168-a1af-bdff4b512769 | -18.25 | -56.58 | 2024-10-16 02:03:42 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f12503b2-52b1-3663-b9c5-b47820e143aa | -18.28 | -56.61 | 2024-10-16 02:03:42 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 43fb3743-0eaf-3514-8fda-def8a93c4235 | -17.84 | -57.46 | 2024-10-16 02:03:45 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0560e9ce-77f5-3e59-8715-26056da34916 | 1.0199 | -52.2162 | 2024-10-16 02:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 36.9 |
| abb31796-4053-37bc-a58a-97a04410dd3c | -3.1098 | -54.2464 | 2024-10-16 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |


[Clique aqui para ver as próximas entradas](README21.md)
