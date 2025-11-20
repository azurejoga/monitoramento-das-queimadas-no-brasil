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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cb6fefe-985c-37ab-952c-f0819e8aebce | -22.70017 | -43.36105 | 2025-11-20 04:16:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| df447313-deb2-32a0-b1f2-a7a1c96cc86e | -23.38437 | -46.41502 | 2025-11-20 04:16:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b8029fa3-cb15-30ab-8586-96789158546c | -21.26402 | -43.37157 | 2025-11-20 04:16:00 | NPP-375D | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1e4ce4cd-679b-32f9-a928-d9fdd61a73c8 | -22.42858 | -47.63262 | 2025-11-20 04:16:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 46e719c1-84da-3075-aab6-2e19b210e973 | -21.04319 | -48.55587 | 2025-11-20 04:16:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 1ec1f95a-b259-3d71-a03d-d8c6bccc185b | -21.044 | -48.55131 | 2025-11-20 04:16:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 0dd801b2-bdaa-31ed-adb3-8c2ce6fe1749 | -20.88746 | -52.35162 | 2025-11-20 04:16:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fc684aa-ce18-3064-830f-c72b29757f55 | -21.24719 | -49.17188 | 2025-11-20 04:16:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 4ae722e6-531d-3c83-b55c-7b7edb101fea | -19.4799 | -53.95153 | 2025-11-20 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7dc0811-4292-36d7-b0db-365ef90027bb | -21.16243 | -48.63781 | 2025-11-20 04:16:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a2845db6-4bc3-34d7-9f29-81f6032a5ba2 | -22.97824 | -48.6719 | 2025-11-20 04:16:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48102b99-2007-3746-9d43-7b4f2107aae3 | -32.09133 | -52.15628 | 2025-11-20 04:18:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 2367f92b-0b8c-36c2-bb08-7b92ebdd59ce | -2.93169 | -45.05314 | 2025-11-20 04:31:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b73e07a6-219c-32c3-8db3-f189b57df8f1 | -2.92577 | -52.41029 | 2025-11-20 04:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d32ab05-3ef9-33b8-997a-416bb6feee85 | -2.08074 | -45.65218 | 2025-11-20 04:31:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9395b287-c218-33d9-9575-2280dac790cc | -3.67427 | -50.15963 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 267dbef4-b379-3d7b-b80a-29fab1549e1d | -5.1331 | -55.94458 | 2025-11-20 04:31:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af328d25-c49b-3cc1-a5d1-dcb817380730 | -1.70105 | -47.13446 | 2025-11-20 04:31:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1aedb28b-110b-3334-b340-4fb73f934b27 | -3.68163 | -50.49244 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ff4a7d2-9141-37ea-97cd-8dd490dd06d8 | -1.35659 | -52.94727 | 2025-11-20 04:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7af65990-2493-32f1-90b4-49bf209dd639 | -3.94307 | -49.00226 | 2025-11-20 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cd8f44c-bd30-3c7f-b8b6-ae9945677b74 | -4.10304 | -50.06057 | 2025-11-20 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 01658a1e-b644-3381-9372-7d3f59017e79 | -3.93968 | -49.00172 | 2025-11-20 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b5234a3-78a7-3623-bde9-01a742d1abf8 | -6.5311 | -47.0126 | 2025-11-20 04:31:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3849136-2bdd-3d4e-977e-432a1948c2d8 | -6.17792 | -49.87368 | 2025-11-20 04:31:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5e9974c-576d-30ab-8e80-2d0ea242b2ea | -3.92025 | -50.02535 | 2025-11-20 04:31:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69d629b8-b8be-31d9-bc61-84f024c2030e | -2.23328 | -46.53975 | 2025-11-20 04:31:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e83d480d-ff5b-35fa-bc2e-9a57157c2041 | -3.68074 | -50.16483 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4455380c-2230-3947-9719-cf6e0d4401d8 | -6.22982 | -48.06629 | 2025-11-20 04:31:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d671285-866d-3f48-acaa-9c233dcb5dd9 | -1.91972 | -48.80111 | 2025-11-20 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfeb5ac0-4ecf-370f-b4c3-4c2b40a9d92f | -7.22148 | -47.98291 | 2025-11-20 04:31:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9833aa54-b210-36a1-8949-7c9be7b0027d | -4.0488 | -49.08593 | 2025-11-20 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe267bd3-2acc-309a-89d5-7c251bd6879b | -2.51097 | -47.81424 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e683c6a-6d39-3ef6-9870-16dee394d590 | -6.97828 | -47.08565 | 2025-11-20 04:31:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f6101ed-ddab-39a8-baf4-f36a3ba7bf88 | -2.48106 | -49.3286 | 2025-11-20 04:31:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c74a8838-0aef-3359-9f2e-193cf9754403 | -3.01293 | -44.46144 | 2025-11-20 04:31:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ef34bcd-e74c-35af-b801-0d97c4c2283a | -2.29777 | -46.30233 | 2025-11-20 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b548195-9ed3-31c1-b297-54e5881cd7ee | -6.16385 | -46.10305 | 2025-11-20 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4dbcbb47-ef3e-338d-bd5f-85d9b1f4eba5 | -3.23313 | -44.85459 | 2025-11-20 04:31:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5777653-fd26-37db-b960-e70e82b5f6c0 | -5.69552 | -50.1212 | 2025-11-20 04:31:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7645e559-1dc2-312a-a311-e4d0ce21c6b0 | -1.88524 | -46.37528 | 2025-11-20 04:31:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2efdd99-0b1a-3236-a139-ef694d18c883 | -6.92981 | -45.99779 | 2025-11-20 04:31:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7f0c48ba-4fa5-32bd-abe4-fdb465a62e3d | -2.39527 | -49.38708 | 2025-11-20 04:31:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9da8f1b4-6787-3f3f-af0d-6d4b9c733045 | -2.03207 | -52.40291 | 2025-11-20 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf7b6772-ccf9-3b39-94c0-bc403c43ed6d | -6.83429 | -46.30134 | 2025-11-20 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e890851-5184-3787-85a5-d3e5a1f5d6c0 | -6.93264 | -46.00216 | 2025-11-20 04:31:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 479f1b83-3f37-3505-b819-2c3119a79ff8 | -6.23806 | -48.05698 | 2025-11-20 04:31:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9667a2d-f278-3fb1-8440-4d06a130a609 | -5.72814 | -49.0981 | 2025-11-20 04:31:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43b3a3be-8070-331f-aa77-9808fb18034d | -6.72645 | -47.17547 | 2025-11-20 04:31:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b839509c-c28b-319f-8400-44177c351d02 | -2.95924 | -41.55434 | 2025-11-20 04:31:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5aaf2fc-cbb5-3d98-b18f-35d012a628aa | -5.13345 | -55.94737 | 2025-11-20 04:31:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb04fa21-15c1-3645-a948-03ee6de4f833 | -2.51429 | -47.81477 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32af2e1e-5147-3c98-a814-08320978f98a | -6.95829 | -47.08256 | 2025-11-20 04:31:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09de0acd-ff7c-309f-a977-0c345a45178a | -2.95865 | -41.55812 | 2025-11-20 04:31:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff4edd35-10c5-3d32-9168-6c85e0810b08 | -4.50226 | -48.7326 | 2025-11-20 04:31:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5206c0d-cef1-3919-9978-15bbef856d58 | -1.70159 | -47.13103 | 2025-11-20 04:31:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 946ccc2d-55b7-3a3e-a288-eabf0ddba190 | -7.55347 | -47.57717 | 2025-11-20 04:31:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f624c2d5-ffb8-3cc1-bb12-846e6d8c5c4e | -2.51152 | -47.81077 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 87cf54c2-8b9a-345c-9699-5c8676f6a98c | -3.59981 | -49.8554 | 2025-11-20 04:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a41aa674-357b-33d7-83f9-c0b7d8dc4c2d | -6.15988 | -46.10619 | 2025-11-20 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fdb7d81-0f00-3e15-8ad4-60d489f5f980 | -0.94095 | -46.86728 | 2025-11-20 04:31:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17b5bb78-ba66-3183-869a-77068ab61683 | -6.48458 | -47.50489 | 2025-11-20 04:31:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a608b45-2fa5-3476-9d2d-67d6b6f36ddc | -3.67782 | -50.16024 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e795304-f678-307c-a031-4a9777f62f98 | -3.57412 | -39.78508 | 2025-11-20 04:31:00 | NOAA-20 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5414198a-0348-3e53-b5b6-51e2d6f15421 | -6.84989 | -35.17789 | 2025-11-20 04:31:00 | NOAA-20 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d9a901ce-03c6-32d8-ac54-1be4d4957e78 | -3.81456 | -50.34262 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ab0d250-f723-381f-a1aa-86ae0a1c021c | -6.17853 | -49.86993 | 2025-11-20 04:31:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2537188-bf06-3d3c-9992-ee678984d2e5 | -6.23752 | -48.06044 | 2025-11-20 04:31:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80b888bf-7c4d-3002-b785-26534b6d55e2 | -5.49249 | -42.16631 | 2025-11-20 04:31:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d0fc52c-a54b-3f66-8cbc-632f59d9df01 | -7.33494 | -35.07923 | 2025-11-20 04:31:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 96ec9ee2-c9da-37a0-a45e-f45b05670734 | -5.84906 | -57.54552 | 2025-11-20 04:31:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d1600af-c0ca-3b48-806c-60dc9170f749 | -2.51319 | -47.82172 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb4ebf1d-0cc0-3e77-949b-cdc5e75ea5c3 | -6.93322 | -45.9984 | 2025-11-20 04:31:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3a4ca6e4-0388-392b-86ad-48eea62d7cba | -3.6801 | -50.16883 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 969d2c74-17db-3260-942a-446bd42221ef | -3.67363 | -50.16367 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ad3efd1-512f-3b23-b173-a9609b22f4cb | -4.22179 | -49.14632 | 2025-11-20 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21d1a530-af39-3195-a125-c8f314f05413 | -1.87686 | -47.05332 | 2025-11-20 04:31:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92a919d8-c330-3261-8126-710f8ccba7f2 | -5.13392 | -55.9445 | 2025-11-20 04:31:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e66b96de-3b4a-35aa-b50a-bee7a969ab2b | -3.9515 | -49.01478 | 2025-11-20 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a4f7035-62ea-3abc-a963-a5e8593ca5da | -5.72872 | -49.09452 | 2025-11-20 04:31:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0457c5d4-001a-3cc4-9233-65d1c54d0e34 | -1.1234 | -47.73646 | 2025-11-20 04:31:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cec1d5c-485e-3e0b-bf4d-daaace14def1 | -2.12851 | -46.19047 | 2025-11-20 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fa93daa-78b5-3195-a917-0e82b86b6a8b | -6.77402 | -46.12318 | 2025-11-20 04:31:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be016e4b-9e61-3e7f-9d30-2898aab774f5 | -4.38779 | -44.08442 | 2025-11-20 04:31:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e239e8ba-0ac4-39d6-9dac-3d76ce042a73 | -6.14671 | -53.01851 | 2025-11-20 04:31:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e16e1ca8-a2ac-3a54-8cd3-0e0b91b3a588 | -5.1326 | -55.94743 | 2025-11-20 04:31:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8181601-810c-334c-a2e4-3828a8ac9178 | -2.26131 | -47.43783 | 2025-11-20 04:31:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81a1264b-f75a-3fb6-82fc-3874233383ca | -7.95605 | -46.88754 | 2025-11-20 04:31:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6895623-44fd-32f7-80c1-a474e6531c34 | -3.67718 | -50.16426 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62d45177-4b30-3f7d-b65e-fb7a69c8dac0 | -5.8484 | -57.54919 | 2025-11-20 04:31:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afc51574-262f-388e-b8ab-bf9d22de3422 | -6.16328 | -46.10671 | 2025-11-20 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aeea72bd-774b-3fdf-a4fc-c7a5e41094ed | -2.93227 | -45.0494 | 2025-11-20 04:31:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 099df967-d8d7-36dd-ad95-1eec1ad3418e | -3.784 | -49.31654 | 2025-11-20 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72aaa4f6-bd2f-33aa-b4ad-1b4076fe7b54 | -4.02543 | -48.88522 | 2025-11-20 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45cce895-e8f1-33de-a3b9-6c02283af912 | -4.39694 | -48.17929 | 2025-11-20 04:31:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26662980-2d0a-3f17-8514-97195f65ec1b | -2.51594 | -47.80433 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86ae53d6-2f06-384b-9621-ce7d232780e7 | -2.30109 | -46.30285 | 2025-11-20 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea0651b9-e720-379e-9798-22171d001b24 | -2.14999 | -47.36768 | 2025-11-20 04:31:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7628770a-3a22-3219-84af-c02e52e94f1a | -2.50875 | -47.80677 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 72a179ad-d64e-3a4e-a71f-dd95649aa3da | -6.23421 | -48.05991 | 2025-11-20 04:31:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README10.md)
