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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4172adff-281e-354e-8947-f8623f1893b7 | -6.1116 | -47.2457 | 2026-09-06 02:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 9a9a4efb-85b6-3248-bd20-fb7da84dc90e | -6.8813 | -55.619 | 2026-09-06 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 6db7b247-ecfb-30dc-8fd3-b4e01e3f66fe | -14.9246 | -44.6744 | 2026-09-06 02:20:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 0f6f04d9-33a0-33b5-8600-7d9bf95dfc5f | -13.8183 | -51.6634 | 2026-09-06 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| d3a6e6a9-05c2-31bd-bc52-fdbcc1a9c2ec | -6.8944 | -62.9748 | 2026-09-06 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 44e6f4fc-06b6-384c-bad7-8586d705f002 | -6.8944 | -62.956 | 2026-09-06 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| b7ab6086-5399-394e-b3df-05fb44b16528 | -5.1439 | -55.9543 | 2026-09-06 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 25ba2e11-5f99-34f1-99b2-db6997984fa9 | -11.2955 | -45.7087 | 2026-09-06 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 6b8d21fb-d747-3374-9c8c-1838bfe8929a | -11.3447 | -45.0597 | 2026-09-06 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 7296e9f4-f90d-318d-a596-6b4f069d678e | -5.1438 | -55.9741 | 2026-09-06 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| ee5cd31e-3697-3019-9fb9-fb12a8555327 | -13.7993 | -51.6445 | 2026-09-06 02:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| cd57906d-63b9-3e6e-9a78-68e2bcdbcaa1 | -13.8379 | -51.6396 | 2026-09-06 02:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d07b2d13-0a3f-3ea2-872e-2c6a8f1e996a | -10.7487 | -60.7676 | 2026-09-06 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 6d190828-aee9-3f3b-b49c-7cab59553fe2 | -14.9246 | -44.6744 | 2026-09-06 02:30:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 9f7edcbb-e682-3762-83bd-0f4c046a1358 | -6.6514 | -59.945 | 2026-09-06 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 24398c06-5670-3be7-b4a0-3324a6919fcd | -5.3645 | -56.0447 | 2026-09-06 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5ee19ef9-c8d0-317c-914d-199a8846b0b5 | -6.8813 | -55.619 | 2026-09-06 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| baee94a1-edae-3b17-8932-0b272679ac78 | -6.6515 | -59.9258 | 2026-09-06 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 40fd7183-6be5-3393-b9ab-93a49241a346 | -11.3255 | -45.0624 | 2026-09-06 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 06a8f3c9-a1f7-3e13-8983-39fdda8679e8 | -5.1439 | -55.9543 | 2026-09-06 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 9a44065a-fa11-34e1-a482-4502b5bf7002 | -9.1442 | -67.8317 | 2026-09-06 02:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| d9ec0cfb-e053-3c79-8b7e-f98bc9b47d18 | -11.2955 | -45.7087 | 2026-09-06 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| c9dd2659-1665-3c2a-99a7-6c65b66e1fb5 | -14.905 | -44.6782 | 2026-09-06 02:30:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e7f44bf6-facf-3562-a4f3-7a212d955739 | -6.6513 | -59.9642 | 2026-09-06 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 428d0067-c750-32c2-ae9c-e629d8463dc2 | -13.8183 | -51.6634 | 2026-09-06 02:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 6cb2194f-639c-3779-b9a0-578da259818f | -5.3462 | -56.0256 | 2026-09-06 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6291d803-ef29-3ad2-8ab1-24d61d58f597 | -6.8627 | -55.6199 | 2026-09-06 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 60c36260-e2f3-3370-ba5e-46620d6e466b | -6.6698 | -59.9443 | 2026-09-06 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4e5a19bc-5606-30ba-bdfd-9c54ce621e28 | -5.3646 | -56.0249 | 2026-09-06 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| f9327321-a6ec-3676-a555-39bd0c5729ae | -5.1423 | -56.2703 | 2026-09-06 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a618245b-18f3-3a8f-9f59-a4d4222d860e | -6.8944 | -62.956 | 2026-09-06 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 92d3f7b4-4bf3-36aa-b3e9-69b14bbee81e | -10.7492 | -60.7097 | 2026-09-06 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c1e4f8f9-e3b9-3fbd-8e34-2b52ec06f976 | -6.8944 | -62.9748 | 2026-09-06 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a8b4c3e7-c3db-32f4-91d8-eb8072eb9f3e | -13.8375 | -51.6609 | 2026-09-06 02:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| f3fb6159-d1ff-325d-9433-6b84b6146e0b | -5.6565 | -60.2475 | 2026-09-06 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 0bb6fcce-e464-3c5c-8842-9cada75c2f9b | -11.2959 | -45.6858 | 2026-09-06 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| e69255f0-7a8d-3f37-a186-309bad7f81ac | -11.2764 | -45.7113 | 2026-09-06 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| b706240e-0eb1-3928-820a-9dd7da5d4810 | -10.749 | -60.729 | 2026-09-06 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9ee3e2f8-c1c3-316d-a6fa-5510e94bb378 | -10.7299 | -60.7687 | 2026-09-06 02:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a8291d61-a945-3e45-a0cd-83f336517ca7 | -13.8375 | -51.6609 | 2026-09-06 02:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4777c6ad-52a7-324e-81f6-f52faa21e55a | -5.1439 | -55.9543 | 2026-09-06 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 0146e6f4-b001-3d94-b8e3-51ace41adbe8 | -5.1622 | -55.9734 | 2026-09-06 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8f7e1475-13f9-3d2a-a608-8c01bfbffb1c | -14.9246 | -44.6744 | 2026-09-06 02:40:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 3fface4c-6d7b-3e56-ad19-62b2d64f0ed1 | -6.6698 | -59.9443 | 2026-09-06 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ed356117-610c-31f6-aa6e-523e59c90a62 | -6.6514 | -59.945 | 2026-09-06 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| d3bd3d1b-8d28-3a1b-a405-c8dd1cbaa77d | -11.2955 | -45.7087 | 2026-09-06 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ff395e96-6191-36e9-9474-c89bdde18221 | -10.7487 | -60.7676 | 2026-09-06 02:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b12cb1c6-ee85-3add-b01d-6e6da1c414e3 | -6.8813 | -55.619 | 2026-09-06 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 384118d9-fbd3-3d6c-9801-fb34d1e72628 | -5.3645 | -56.0447 | 2026-09-06 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 1f3744b7-3f70-3256-95db-ae410c799cda | -5.3646 | -56.0249 | 2026-09-06 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 532d116d-6148-374c-9549-a51ecc5cfa5d | -5.1438 | -55.9741 | 2026-09-06 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 6975e121-e2ae-3db0-9d71-5127d95c9db9 | -5.3462 | -56.0256 | 2026-09-06 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 18422fe2-2ea7-3acc-bec3-1b52eec28ea7 | -6.6698 | -59.9443 | 2026-09-06 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 55f88840-c4ff-3c53-923d-546a94a3b76f | -6.6515 | -59.9258 | 2026-09-06 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 0d37fde2-fad9-3467-ac43-26039e61391a | -14.905 | -44.6782 | 2026-09-06 02:50:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 09bce64d-758b-3b9f-bb02-8de87f110b8b | -6.6514 | -59.945 | 2026-09-06 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| cf1060b4-2c93-3eba-a151-d3572a6b45ab | -13.8375 | -51.6609 | 2026-09-06 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f6cb4f88-ee09-363f-8b2a-3acec8081ca8 | -5.1423 | -56.2703 | 2026-09-06 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 4d56b524-5e97-3db3-99dd-b782d33074e5 | -5.3645 | -56.0447 | 2026-09-06 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 3fd32255-204c-3cab-9794-e74a3eb9d369 | -5.1438 | -55.9741 | 2026-09-06 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 3f87d1a7-b5c1-3207-b913-29fdb911d103 | -5.3646 | -56.0249 | 2026-09-06 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 1da7ee6e-8579-385e-bd1c-6d64c2f53672 | -10.7492 | -60.7097 | 2026-09-06 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| de21fb4b-2169-3a52-81e3-82a291800bd4 | -10.749 | -60.729 | 2026-09-06 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 8cc1f153-8146-3a5e-ab6c-4b873aa304e5 | -5.1439 | -55.9543 | 2026-09-06 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 140f610d-b724-30df-86ad-0292f5c03319 | -5.383 | -56.0242 | 2026-09-06 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 91819eb0-11ed-3a81-9d1f-65b34c3d8dac | -5.3646 | -56.0249 | 2026-09-06 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 92643984-bcd6-32cf-a620-90cef15e1e95 | -5.3645 | -56.0447 | 2026-09-06 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 7b8e1736-8349-32ee-a924-ece672d557f8 | -10.7492 | -60.7097 | 2026-09-06 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| f2c17003-713d-31dc-9c85-4b5e0ac82a58 | -5.1423 | -56.2703 | 2026-09-06 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 82656a9e-0234-31f7-94ed-e259c695d9dd | -14.9246 | -44.6744 | 2026-09-06 03:00:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b9725acd-0bb5-36e4-8555-998ed3a342e4 | -10.749 | -60.729 | 2026-09-06 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0f88f456-02bb-3b5a-8faf-4dc3327a9b3d | -5.1439 | -55.9543 | 2026-09-06 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| d43f9d1c-4e3b-3592-b942-dff1929334a9 | -5.3462 | -56.0256 | 2026-09-06 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ea831949-9faf-327b-9183-e1889c5ca031 | -5.1438 | -55.9741 | 2026-09-06 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| aef8a44c-e87b-31ad-aa05-757d76b1f5ca | -7.14173 | -38.28459 | 2026-09-06 03:06:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d8dafbf1-d4a7-35a2-a1ee-9c9798ca5fe9 | -7.14165 | -38.28313 | 2026-09-06 03:06:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| aae26cb2-0572-3510-860b-5b80cc4f00a1 | -18.38655 | -39.96008 | 2026-09-06 03:08:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 984200d7-36ef-33b6-8524-87ab572ce3c1 | -19.88247 | -42.64394 | 2026-09-06 03:08:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2c0a6ecb-d763-3414-8354-05d2f59394fd | -19.88394 | -42.63779 | 2026-09-06 03:08:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c17ff1cc-1eb8-3b6f-a2e9-ac18bec254ef | -17.43139 | -40.02321 | 2026-09-06 03:08:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cef9b725-87a9-39e8-8b56-75342965cce0 | -17.4254 | -40.02183 | 2026-09-06 03:08:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 21601864-c564-3cf1-9892-5a8cc4ac119f | -18.47034 | -39.74576 | 2026-09-06 03:08:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 66b34beb-4537-333b-aca3-4fc19e6307f2 | -10.7492 | -60.7097 | 2026-09-06 03:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| b9ff3848-0dd7-36ab-bf5c-3b49eaf121ed | -10.3833 | -46.8425 | 2026-09-06 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| dd2fd1cd-05a8-3471-8325-94e1d192f890 | -5.1438 | -55.9741 | 2026-09-06 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| ff89fa17-a2d0-36c8-92e0-81e548320efa | -5.3646 | -56.0249 | 2026-09-06 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 1b7dffdf-d1e2-3012-92bb-7340c6fe73f1 | -14.9246 | -44.6744 | 2026-09-06 03:10:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 74a17a39-bba4-3da8-bfbb-072eaf751175 | -5.1423 | -56.2703 | 2026-09-06 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8dcbb61c-2a9d-36f5-962b-443a0fc2e4b0 | -5.3462 | -56.0256 | 2026-09-06 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1d282c50-a265-38e7-9459-66a2ba83eb13 | -5.383 | -56.0242 | 2026-09-06 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7d33e1ac-7b86-39a5-8caa-0c39585c088c | -10.7492 | -60.7097 | 2026-09-06 03:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d0158613-20f9-3cc3-b7c7-947c3a582b1f | -5.1439 | -55.9543 | 2026-09-06 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 26203c4f-0b1e-301e-bd73-3f2a0c7e6c4b | -11.2959 | -45.6858 | 2026-09-06 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 3e6a2313-d1a2-33cf-a3cd-b1395c3b1f55 | -5.1438 | -55.9741 | 2026-09-06 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 4c3c96fb-6c26-3672-9210-e0a0507c060c | -14.9246 | -44.6744 | 2026-09-06 03:20:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3414f3d2-3d82-33dd-9e9f-f4414287055e | -5.3646 | -56.0249 | 2026-09-06 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 79da06e5-3632-3f49-8987-2444685081e6 | -5.3462 | -56.0256 | 2026-09-06 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| de8b6f4a-abf5-37f3-9ef1-13df9a601bbf | -11.2955 | -45.7087 | 2026-09-06 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 0d80d227-5265-3cd3-a047-54fb78c72a54 | -5.3645 | -56.0447 | 2026-09-06 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 517913ae-282c-32ae-96d5-9dccc2f75ca7 | -5.1423 | -56.2703 | 2026-09-06 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |


[Clique aqui para ver as próximas entradas](README11.md)
