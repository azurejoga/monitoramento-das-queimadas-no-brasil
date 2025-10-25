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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f83ddc8b-6280-3b41-96c9-3f216da78286 | -7.1659 | -45.84515 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9875559-dcd5-3a71-bf0d-c1d916f6231d | -6.84796 | -45.0601 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40035c07-33a9-3709-84d5-6f4da69b5492 | -6.59553 | -44.32813 | 2025-10-25 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 231a0755-a6aa-35a6-99ab-01cfd398ab46 | -6.91892 | -45.16927 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c96ad0a-49d4-3e4d-8a55-c1bf6c003fea | -3.12401 | -49.10525 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d9b923c1-a945-3f84-8e12-f5cfe07d6798 | -5.69729 | -49.32011 | 2025-10-25 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6642662b-1168-3248-bffd-42a66d36f22a | -1.30309 | -49.34579 | 2025-10-25 03:57:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2e7db45-f27f-396f-844e-4996a2334f6b | -9.62253 | -40.3414 | 2025-10-25 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 14409242-ec3b-3a81-a9fa-60b6b94e5e72 | -5.03557 | -41.19978 | 2025-10-25 03:57:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0cc3d0cd-a278-38ed-a111-ecc6227e0300 | -4.9991 | -47.76144 | 2025-10-25 03:57:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69845b3e-a123-3eba-9309-f0f14dc42a54 | -9.61784 | -40.34091 | 2025-10-25 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92368f85-5141-3aa5-ba34-d42290cd249b | -7.41965 | -46.65612 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f500e5a2-1dee-38c0-9bdc-4b1e74c75480 | -2.81086 | -49.14551 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5f8e468c-5875-38f3-8e26-ab7dfa7a54e2 | -5.65024 | -45.97189 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c48002ce-8764-3487-b7d9-665484caba40 | -8.13533 | -47.04298 | 2025-10-25 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bf44e8b-8bbd-3064-8558-6fa22bc8dcd5 | -5.54935 | -41.3414 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c5fde3c2-dba7-3f8d-bb88-95b5351021b6 | -2.26758 | -47.8576 | 2025-10-25 03:57:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 960b9a21-e423-3eb6-8f1e-a3c2187c3758 | -6.5962 | -44.3242 | 2025-10-25 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7b2e1fb-87b5-3071-90e1-1ae1145a8f89 | -4.55349 | -46.6889 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b7079c66-d6e6-309f-82a1-373aa16bf18c | -7.45772 | -41.90676 | 2025-10-25 03:57:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 811365af-ff26-3134-8969-6b64bf53eccd | -5.55298 | -41.34197 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1cade39-1e06-3b22-9ee8-95d8eba8d456 | -2.72773 | -49.1593 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5e08a1e-e2e5-3b43-b518-fcb85f54103c | -5.62819 | -42.59309 | 2025-10-25 03:57:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 939ae913-16e3-3bde-8287-4ecd041a12c1 | -6.31404 | -41.84884 | 2025-10-25 03:57:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4ec97684-1fe9-3ad9-911b-bf69f664cf3a | -6.90466 | -45.17126 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54537ffd-94d5-3e71-8f81-80afbc31b435 | -4.27597 | -40.6853 | 2025-10-25 03:57:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bc89d2e8-fa97-37a6-b806-91dbc6fc09de | -3.08724 | -49.47396 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7197020c-38bc-3f59-ae16-a71361504474 | -5.80621 | -35.54225 | 2025-10-25 03:57:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 09efd0ce-4bf3-38c9-970a-7a4dc2b1f68f | -4.45468 | -38.44444 | 2025-10-25 03:57:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc1fee95-d374-3756-b179-3fd87252c5a8 | -5.7064 | -49.30968 | 2025-10-25 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a49fff8-dd2c-3a51-b678-bc37061d075f | -14.8706 | -48.0822 | 2025-10-25 04:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d4ebe124-901d-30b6-a731-5b373c9c2ee4 | 1.6386 | -55.7455 | 2025-10-25 04:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| a1184bbd-96a1-3e3f-bb8f-1ef966758e83 | -9.6295 | -40.3392 | 2025-10-25 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 8e50bfa7-d094-31a9-b175-f8166d4fb0ca | -2.8149 | -49.1354 | 2025-10-25 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 643847bf-7bb2-35de-b1ff-6b62295f0aa0 | -16.5857 | -43.4946 | 2025-10-25 04:00:00 | GOES-19 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| fdf127f8-0cdf-39a3-8413-339c4acf0635 | -14.8701 | -48.1047 | 2025-10-25 04:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 8754b8be-a1a2-3301-9a5c-ee3063ae9a74 | -2.7964 | -49.136 | 2025-10-25 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 3c73b949-62e8-3fac-80f8-262f023eb391 | -9.6104 | -40.342 | 2025-10-25 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 3e335fc5-821d-32cb-ad34-2588e4afd985 | -18.1714 | -51.7466 | 2025-10-25 04:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 45.1 |
| f14eed45-4012-3ea6-a132-8e9f1e7e654c | -10.87713 | -45.07951 | 2025-10-25 04:00:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a10330f-1ce9-39d6-bfa5-dd0b30d8e06c | -13.35156 | -47.41149 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bc8cb96-c636-3c93-bfaa-f1757afd132b | -14.45882 | -47.93147 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9c44495-3888-3025-95f0-ac7896231e4c | -9.751 | -47.83357 | 2025-10-25 04:00:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7cd52aa-b5ed-3ac8-b8f5-c2e83004d621 | -12.46876 | -44.53922 | 2025-10-25 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a27ac72-c963-3009-8439-f152954dab99 | -10.8868 | -48.03744 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 598ec7e0-4a2a-34b7-a3a0-881e755f24ac | -8.87004 | -48.29285 | 2025-10-25 04:00:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c82b0c94-fe9d-3bd2-8b41-af17d74d0897 | -14.51971 | -47.94609 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2071793-4747-3d1b-8b87-0d267a0e69d6 | -14.71798 | -46.84848 | 2025-10-25 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8275ca5f-bcf7-3a87-a8bf-1d272173012f | -14.53952 | -47.94544 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27f5e4dd-18fd-3e19-95c5-17747e8d8d86 | -10.62462 | -42.31391 | 2025-10-25 04:00:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7320f5df-67e2-3dac-8bee-33d9ba517c74 | -12.25017 | -47.44213 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42b7f061-fcf7-3412-8c33-edf18eb9bc5f | -12.04868 | -46.40954 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cf6bcdb4-e9da-312a-8453-f09283ef5d54 | -14.74212 | -46.59896 | 2025-10-25 04:00:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d33633fb-52e4-36f9-8aff-6eff659ad462 | -12.94714 | -48.49977 | 2025-10-25 04:00:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e2be95d-061a-39a8-8909-87d4d20e1a72 | -9.32041 | -45.20316 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec6c1fe2-cb2e-3ec9-84e7-39c10584738f | -12.12604 | -46.71038 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3ae07b32-b299-37c5-a900-91603645b3f1 | -14.4736 | -47.90511 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4e6bfdb-aeaa-304e-b946-af5895ad1274 | -14.20331 | -47.3065 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a4c549f-3f58-3b26-b65b-c9d4759ec57e | -10.87452 | -48.04681 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 465a266e-5742-32d4-8c68-1b7dce3925c9 | -15.18874 | -44.07786 | 2025-10-25 04:00:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efca9690-487a-3630-8378-c8800129feee | -12.06258 | -46.44481 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ff4ab4f-dcf0-30cc-98c1-cc2f1933b44b | -12.07833 | -46.40974 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d798008-125a-333d-a99a-d0262c996c74 | -12.08919 | -46.4263 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 873cd90a-a186-36c5-b0a8-eea4bc9ad561 | -12.94974 | -48.50213 | 2025-10-25 04:00:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85ba5e77-36b0-32ee-9bb2-41e7466de01e | -10.87658 | -48.03558 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1b73650-8fbb-3bc8-a40a-eb5968918d4a | -13.87036 | -43.31527 | 2025-10-25 04:00:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5ff0e3b-601b-3dd0-b72f-fb5bb5f811a9 | -13.8736 | -48.38797 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfba6207-7518-3bf1-b6f8-8e14a37e7956 | -9.32281 | -46.97516 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15eee57c-edd8-3368-b982-8cfa079ee32d | -13.34771 | -47.40613 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c057ab85-f398-3205-8d46-ba5ee18eca03 | -14.8802 | -48.09601 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 538d1958-a7f2-33e7-806b-7e221d61c334 | -10.64005 | -45.24149 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9c2c68a0-60db-3f70-ba99-27a5ab873b31 | -9.32671 | -46.98155 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b707d184-bd5e-3c3f-b398-9eb50dced7da | -14.4791 | -47.90143 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b8f044e-c248-3ade-8c68-6e7d290e9409 | -12.8302 | -48.6681 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 331900da-98e4-390a-be0d-23dc8921df66 | -10.87157 | -48.04691 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7e2aa65-fb2a-394a-8e88-4ac83650b3da | -13.06816 | -43.84408 | 2025-10-25 04:00:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f052a942-379b-32bd-a7a6-0c5ff41eb66a | -9.09531 | -47.82244 | 2025-10-25 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad952835-a158-37ac-ab9b-6e2272c437b1 | -12.05513 | -46.40988 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e4c64f7-4b4c-31bf-a00c-a9315f16cffa | -12.17972 | -43.60981 | 2025-10-25 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4e0e0bb-fee6-3c52-a74d-2f73991dbd1f | -11.06588 | -49.62547 | 2025-10-25 04:00:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d223f52-0720-34a3-905f-32d01fad472a | -12.0856 | -46.42063 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ae71737-8edc-3267-9fc0-b9cd1cf2f106 | -14.88904 | -47.8671 | 2025-10-25 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53099ec5-e744-3a18-bc0d-bb09572dd43e | -14.15546 | -44.31806 | 2025-10-25 04:00:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8145e439-43c9-38c1-867e-386ae435d6f1 | -11.97779 | -44.96897 | 2025-10-25 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82ea193d-c164-3ca3-9658-f0f302c9136f | -15.57632 | -43.22364 | 2025-10-25 04:00:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9bb03e2f-70be-3deb-80bc-dc64af550665 | -13.909 | -48.41755 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2484aee0-1783-3c33-ba7c-e6e7f4358327 | -15.57985 | -43.22428 | 2025-10-25 04:00:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ee276ba6-1d01-3ff2-8138-392370cd8326 | -12.21354 | -46.51457 | 2025-10-25 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77fe52a8-b21f-39de-802a-37abe2b1c5b6 | -12.70109 | -46.3331 | 2025-10-25 04:00:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e14ea87-b3f2-3633-b3e1-1f079ade73b1 | -15.58055 | -43.22019 | 2025-10-25 04:00:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a1938f3-1238-35d8-b702-aa78df2dc581 | -9.65267 | -47.75528 | 2025-10-25 04:00:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d077964-6c09-391f-96a9-38cac168c9bc | -13.4069 | -47.95008 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27f5a78e-de32-3004-875e-fe58c8f232ca | -10.0013 | -47.59365 | 2025-10-25 04:00:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f618fe9e-6f89-34d0-a5ce-ed94a6e3f346 | -9.30978 | -46.25439 | 2025-10-25 04:00:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 960c422a-1021-3a28-8900-4537b5cd8ec0 | -12.21975 | -46.50599 | 2025-10-25 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e138b4c-680a-3de4-bcf5-be3068d4616c | -14.87366 | -48.07527 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 083481a1-8977-36fa-aa39-5a673e55c732 | -13.88423 | -49.05008 | 2025-10-25 04:00:00 | NPP-375D | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25ff1bc6-6b9c-346b-aba7-6fdc7bf46d9e | -13.28294 | -47.49185 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc287d8d-049a-3272-a38e-65828a1d8c05 | -11.97372 | -44.96814 | 2025-10-25 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fb3d604-4ec0-3f94-a036-5cb0d63744d9 | -14.57478 | -47.45647 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README19.md)
