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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5db16d83-abcf-3e0d-863f-bdf3c1c89718 | -10.85388 | -45.33485 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 37b7d5f8-3bad-3891-b341-14f777e10fb4 | -8.7612 | -46.46208 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ad22c87c-cedf-3918-8de4-477348519578 | -7.92824 | -45.00264 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| af4722b9-0ae3-3015-897b-4fa1cd33bd97 | -11.19795 | -46.10952 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 1c79ee9d-e9ab-3430-9555-cc97f9f3d010 | -6.59006 | -35.20794 | 2026-08-31 16:50:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e1b66f02-62c4-35b9-8d4f-3a32c8f3c534 | -8.73375 | -46.46216 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 68e664c6-3886-3135-9b8c-521d5045a18f | -9.48046 | -57.02132 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 8b8926fd-6cad-37c2-a3e1-01192ba7b310 | -11.19887 | -46.11616 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 901afda1-f875-35dc-8f10-cf22c6e55e7d | -11.71851 | -47.64663 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| cd5ab7fc-06f5-3b5b-a63b-840dbc5b7bd5 | -8.71209 | -52.36583 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 68f0ccb0-3686-3ad9-b2a5-06b1f4eced1e | -11.2498 | -45.09865 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 99cb67bb-f109-34b0-b445-db536806080b | -7.96891 | -44.31936 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 48b58c63-9ad3-3cd4-a9d1-f47f3c70f936 | -11.67562 | -47.61026 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ab63c5f2-f787-396c-88fa-c56b69a9fc76 | -11.24923 | -45.11109 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8c7e3318-dde8-3810-b6eb-8c55f10fc259 | -11.24605 | -45.13668 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c6ef4449-aeb5-3618-af62-4173e6df13e9 | -7.58312 | -61.34879 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 6c592c0e-7dea-3e68-84f1-9198c5053744 | -11.93537 | -45.10038 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9dd05fb2-0ca8-3791-9e34-9d0f42cc205b | -10.74944 | -61.57487 | 2026-08-31 16:50:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a98eb3a1-e4f4-37d9-a47e-474e1a6f8339 | -11.05612 | -47.11758 | 2026-08-31 16:50:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| dbc7d269-e0bc-3ade-8785-ddf686322b32 | -8.91808 | -44.1745 | 2026-08-31 16:50:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| eca6a6fb-75f4-35a4-a052-b5f44cbdfeda | -10.01797 | -46.16566 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d924d6a1-2dd0-34fd-8469-fa36284e850a | -9.416 | -51.68261 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7164f06b-a031-3bcb-b213-4ba35d9f562b | -7.63379 | -44.83732 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ee0445c5-0702-3b23-b449-3be36a7ed87a | -5.57646 | -45.74277 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1a0bf669-834a-3f45-b511-dcfc2177e42b | -6.65851 | -43.87488 | 2026-08-31 16:50:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c301fda1-d662-3090-9451-8c5a35df11bd | -11.93117 | -45.09691 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| af03a3e9-15cc-326e-9982-bf0b4129b50a | -5.58325 | -42.33255 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 4ea40ff1-a4b4-3480-af5c-a3132aaee77c | -8.92036 | -44.16414 | 2026-08-31 16:50:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ac21ed84-a06a-3a0a-b860-aa96cbda4109 | -8.13414 | -45.58231 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e5842383-eb0d-3074-922d-c2441a853370 | -9.42264 | -51.67747 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 43d0fd98-f11f-3881-83b6-e9e6621caeee | -10.08389 | -46.61997 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| eac23b7f-acce-31bf-85e1-f91345c492cb | -11.64663 | -46.7482 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7ce57487-dd61-3a04-aa1f-721d83e94ed0 | -11.03284 | -49.67126 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7e9307d6-bd2f-3637-9699-50631069c0c8 | -8.4414 | -46.89766 | 2026-08-31 16:50:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25396208-57df-387e-869b-f463d0f4a45d | -7.54174 | -57.80629 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14bd420b-69bc-3cd2-b67c-20a4c0ce0d76 | -6.35446 | -44.88877 | 2026-08-31 16:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23e7e4a3-297f-3317-872b-5000518d70db | -7.93121 | -61.34741 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 6b469f28-4261-349f-a831-97ef94ca7369 | -10.30673 | -49.98896 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2aa1dbc4-bc3c-3502-a0e7-6219336b8f95 | -7.31276 | -43.00578 | 2026-08-31 16:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 492453ba-23cf-3062-975c-5318f8f4a7df | -8.12987 | -45.57871 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e04de3b8-ae1e-3d39-8241-72d0da7ece2f | -9.16925 | -59.37452 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 5d1bbfa2-70ac-35cf-89a6-82dd0e3a9779 | -8.75835 | -46.46635 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 96fe8047-af8c-3874-81ab-37125842697b | -7.0634 | -42.20848 | 2026-08-31 16:50:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| e1b70031-f56e-34dc-86e0-39c290cbaa12 | -7.53146 | -55.58325 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e720d5dc-aa8f-39e9-ae99-6a2aec6df725 | -9.93491 | -48.3414 | 2026-08-31 16:50:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6e1cb6a7-56f9-33b3-a6a0-9337db23e74b | -9.87568 | -46.12572 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02efae2a-22ed-3bc5-bfd3-46bf2af3e421 | -13.98341 | -54.40987 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f76f358f-3d2a-3bd4-a591-4cba71c72a68 | -12.10394 | -47.15261 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| b5298287-68e9-3835-855e-abd9d9e856af | -13.36212 | -51.6786 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| dad29dc9-84ec-360d-bfd6-7465176d2133 | -7.67909 | -44.73406 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bf238b62-4039-32c5-b820-70960ec844ed | -5.76624 | -44.13199 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4b695ced-632e-3d82-b251-64ea320e034f | -12.904 | -45.83751 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1a257217-f5d6-38e8-a9ac-04596dbdb0d0 | -10.0833 | -46.61629 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 962ac545-d68b-397c-843a-26584a78fd5b | -13.95932 | -54.40314 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f0b138b9-9bd0-3e18-9883-730ce37f9615 | -9.42013 | -45.6757 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 35bee332-2e9d-3cc2-868d-1f2beef45838 | -9.66481 | -50.86179 | 2026-08-31 16:50:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 7cd4805b-f636-38f6-acf2-4a502610727f | -7.16973 | -44.68342 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3b20a5b0-5017-332d-9302-95bba8b1e059 | -13.4712 | -57.03289 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 09c131a6-1f03-35c0-8194-bc789900f7a6 | -11.22563 | -46.10807 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 56298cde-cabb-3573-ac71-1dcd93924eac | -13.53444 | -59.75791 | 2026-08-31 16:50:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| df671de4-3b80-3794-bb99-12be8d109195 | -13.42977 | -51.69574 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e452f0c2-ba4a-32b2-8e85-0d5dc0001202 | -10.1128 | -50.313 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5a41baea-0fbb-3952-b18a-a92e6731d814 | -7.68569 | -55.33753 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 15562884-8c41-31fe-8618-5c9dc546dbb3 | -7.35984 | -45.08274 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f0ba60ae-2ffe-3919-b869-551b122e6125 | -6.93348 | -55.62923 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ce4803ca-5124-31ce-86e6-9eb50f838afc | -8.64549 | -47.30914 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 70a7bd48-bcec-3436-9ceb-0e40f44afc0c | -9.40246 | -60.58536 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 84ac64ad-9ca7-3c51-963d-c182872d7785 | -7.00155 | -55.8802 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e818f585-81ee-3a01-a42b-4dbb6081f9a0 | -8.93353 | -45.03504 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a032e77b-d3af-3a36-954c-7e568e9ed39b | -7.91929 | -44.2354 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 8d850688-6518-3bbe-8a0a-4837456d5b43 | -10.09569 | -46.60671 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5a5e867-7061-3004-bf6a-ed87a78fd086 | -11.25186 | -45.11105 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| b4869802-a3b6-3212-a894-e4892cbf635f | -6.76883 | -52.90402 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 805febe2-4409-38d8-b7ed-f9d47bc4414c | -6.63035 | -53.17475 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7d01359-9581-39b2-a74d-ebe191e66d46 | -10.06137 | -59.40918 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 68828dae-804e-3047-abb4-a7a7963648f7 | -7.62639 | -55.295 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 35c1678f-fae1-31c1-8420-fc39c0b017b9 | -8.00547 | -44.34101 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 40072de4-5846-39d1-8d21-9401c81e9eed | -9.15604 | -60.93837 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f91c1590-cfe6-389a-b2d2-b57def6bcd5c | -11.25474 | -45.10635 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| adad5a00-8b71-3d6f-8670-16dbf4b540db | -11.21816 | -45.34555 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 5a2db369-50ca-315b-9cc1-75bf1bc88267 | -10.15567 | -45.76933 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f57ce851-8715-353a-b80d-2317081e859e | -12.95878 | -45.93976 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| a7c4552b-42fe-31ce-848b-8215384199c2 | -8.79466 | -39.85152 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 58121012-8ecd-31b0-b70b-67ef5ee898b0 | -11.20317 | -45.09753 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 3f9a7c09-dda2-3d38-aacd-8e0094e188b0 | -7.41483 | -44.24583 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 58b1b9e6-aa95-3bff-8e7f-35dfe588da83 | -10.33299 | -49.95473 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| cae4736a-c884-36fe-b887-f538ff1e2f0d | -11.6773 | -47.59919 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d17e8260-6046-3fb6-8756-2b43c4000caa | -8.15298 | -45.46806 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 5ba08cc5-63aa-37d3-8c98-613f7142de13 | -12.10268 | -47.25448 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5ae90627-0ffd-3eae-8b1e-d11a72500ba5 | -11.6706 | -47.62181 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| fa5948e9-1f49-3585-9dd6-3e02d471e5b1 | -7.62179 | -44.93185 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| d5fec02e-764b-368a-ba54-1c9686005941 | -5.58314 | -45.7372 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1b79ffac-8c86-3d5d-b37a-a6b276fd77a8 | -11.68327 | -54.549 | 2026-08-31 16:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a68e0c33-e9e5-32f2-a280-ab63cfb1ec65 | -11.32785 | -45.17398 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 560b083e-a3a0-369f-852a-fb0c1c3ea796 | -12.07786 | -47.20401 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 91c65c1f-b948-35a5-acc2-a6af0e80f6e2 | -7.17355 | -44.68272 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57dbdaae-3915-3ad9-bf84-8183ec7b4209 | -12.09719 | -45.06957 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 52812173-88e3-390a-ad6c-e9d450ef14b2 | -13.3871 | -51.77657 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f726dc58-7fea-3b36-a8de-639576f5b55d | -7.04642 | -45.40681 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0ab61b48-2e94-35bc-908f-a15cf2ae0c94 | -7.05656 | -45.42297 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README149.md)
