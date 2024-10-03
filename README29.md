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
| a8c55b48-519d-31a3-a2db-b7e7efead2b6 | -10.5428 | -50.956699 | 2024-10-03 01:04:55 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2ed8c960-b3bb-3eb7-bdfd-4606320d237a | -10.8746 | -52.413601 | 2024-10-03 01:04:55 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e69558c2-7d21-3821-aea2-233dec0c8a08 | -10.8762 | -52.420601 | 2024-10-03 01:04:55 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2671eb7-40cd-3e95-af71-e0aee7225cdd | -12.97 | -62.604698 | 2024-10-03 01:04:55 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ecd63ae-585c-3e55-b1b0-387a1d9a3542 | -12.9752 | -62.632599 | 2024-10-03 01:04:55 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b997bf65-55f9-39cd-9314-81caa935ee6a | -12.9656 | -62.634399 | 2024-10-03 01:04:55 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 81589915-c8f1-38d0-af59-e63dce9a994b | -10.5523 | -51.088001 | 2024-10-03 01:04:55 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 342713af-6113-37dd-9859-9fe8f86db20d | -10.5409 | -51.083302 | 2024-10-03 01:04:55 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d09e560-bd9c-3b94-b969-d5d2bff4c529 | -11.2355 | -54.1791 | 2024-10-03 01:04:55 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c07259bc-43d2-3d34-b4b0-3b8cd0864205 | -10.0077 | -48.847599 | 2024-10-03 01:04:56 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71e89376-998c-38f8-9c04-4c3e33177fbb | -10.4528 | -50.745998 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e085490c-3eda-321f-942f-377bea6ce5bf | -10.5295 | -51.078499 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21b72a85-6e8d-3b0e-9c40-9108f1e1e17b | -10.5311 | -51.085602 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7c006015-18c6-36f5-b722-857d0eb63c80 | -11.2257 | -54.181198 | 2024-10-03 01:04:56 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27a84b6a-05a4-3df2-9e78-2f7b9479a9e7 | -12.9008 | -62.4468 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 20a173e6-4996-3c4b-a7fb-2f562ceeb9bb | -10.4447 | -50.755402 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7cb62147-0288-3641-9abb-2d5a8db3bc9b | -10.4464 | -50.762501 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc88b42d-3c20-3f5b-a18c-1bbc3fad2ef7 | -10.448 | -50.7696 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb2ebc5e-baf4-3d19-87e5-5906f0937337 | -10.5197 | -51.080799 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1533dbf0-57ae-3556-9478-fdb63746c248 | -12.8911 | -62.448601 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ef1ba339-03e2-3110-8cb7-f821eea8a9c4 | -12.8961 | -62.4758 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 949cdb00-0d19-39aa-a649-a123de401030 | -10.5099 | -51.083 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| accc84e9-5243-375a-a5a7-1508ac8666b3 | -10.5115 | -51.090099 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07955813-a599-3ed7-a4d7-971a3c235f02 | -12.8814 | -62.450401 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eb69e783-c751-3eae-8a29-85735448de64 | -12.8865 | -62.4776 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7497b38-47f0-3e6f-8d80-09b7b197af75 | -12.8916 | -62.504902 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a27e6d6-2c9d-33ae-88f5-78d9ae049b57 | -10.435 | -50.802601 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be610278-643d-35e0-97ab-938a6c4c1a6d | -10.4366 | -50.8097 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b18a81f-f6c1-38a4-b09f-bdd95b2d401d | -10.505 | -51.1064 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4c498f8-5c7d-3460-a76c-e9691830976b | -10.5066 | -51.113499 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a8534da-27d2-3d71-bd2b-e51d00085919 | -12.8717 | -62.452202 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dfbda073-c192-3060-98d0-3fd76fb413c4 | -12.8768 | -62.479401 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9593c17-80ff-33d2-8b01-192b985476f6 | -12.8819 | -62.506802 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 49bab879-9b48-3e1a-9743-961782e5cac5 | -12.887 | -62.534199 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3711ee1b-250f-3ad2-b57b-542ee9e20026 | -12.918 | -62.7015 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2457b6bc-6fe4-386b-bf45-10aa9ba0fc82 | -10.4252 | -50.804901 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 187a1cf1-3312-33c5-ac05-698f7bc859c3 | -10.4969 | -51.1157 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d5ceb7c-a933-37d1-adb2-df2e069be832 | -10.4985 | -51.1227 | 2024-10-03 01:04:56 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8625ce57-1d27-323e-9152-8490b8544199 | -12.862 | -62.453999 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68880651-d1ca-3531-a9a4-db566dbd8428 | -12.8722 | -62.508598 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 75bfecac-a312-3894-97c9-221a5a3df12f | -12.8773 | -62.535999 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c7f56e5-7df0-371c-9677-fa065feaf87a | -12.9083 | -62.7033 | 2024-10-03 01:04:56 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e085f810-49a8-3477-ad24-278084cfdf18 | -12.8677 | -62.5378 | 2024-10-03 01:04:56 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5a27317-43ea-386f-bdc5-cac5d65153a8 | -12.7899 | -62.495602 | 2024-10-03 01:04:58 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4fbc77fb-7103-34f8-ade4-3b49796f66c7 | -11.1001 | -54.217098 | 2024-10-03 01:04:58 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aaf2ae1c-3082-3cd6-bf35-931c22082672 | -11.1018 | -54.224899 | 2024-10-03 01:04:58 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11bb9dc8-13ad-3812-ad76-a1c721962d06 | -10.3681 | -51.0047 | 2024-10-03 01:04:58 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8da48bd2-d8c6-3c38-8db2-b4eca9f344d0 | -10.3697 | -51.011799 | 2024-10-03 01:04:58 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff0157ff-e7a1-3ee9-ae8d-f08fc0b0f40f | -11.092 | -54.2271 | 2024-10-03 01:04:58 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7b47589-d489-383a-a383-c1b00f15c012 | -11.0298 | -53.990299 | 2024-10-03 01:04:58 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23599671-f466-3a62-bb4f-6657220aa633 | -11.0315 | -53.998001 | 2024-10-03 01:04:58 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 582c760e-c01f-3046-a7aa-5cacf4d457f2 | -11.4523 | -56.283798 | 2024-10-03 01:04:59 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4827c167-9b7f-3f36-8dca-14555608b806 | -11.4544 | -56.2938 | 2024-10-03 01:04:59 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6023f0da-1ac4-3e76-a564-b5737accbc6e | -8.9269 | -45.632801 | 2024-10-03 01:05:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7f7e2b61-a709-300e-8856-4fd166d5ad45 | -8.9302 | -45.646099 | 2024-10-03 01:05:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f9a8a2f1-51a7-38a4-9e6d-3d2414278918 | -10.9958 | -54.256302 | 2024-10-03 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b1d3a7c-b680-3870-ad70-50f62fd4d152 | -12.7417 | -62.881901 | 2024-10-03 01:05:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b0e3973b-3cc5-389e-9e54-f4cc5c236ab1 | -8.9172 | -45.635201 | 2024-10-03 01:05:01 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d4a93b8-dee3-3577-b163-4a8319afbe39 | -8.8545 | -45.507401 | 2024-10-03 01:05:01 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1059cedb-c761-3fd8-b41c-125d98646275 | -8.8579 | -45.521099 | 2024-10-03 01:05:01 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79a87c5b-243a-3358-8ce7-e848a5437cdf | -8.8414 | -45.496101 | 2024-10-03 01:05:01 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b9cf0923-77e5-3da2-94f8-1509655a3f84 | -8.8448 | -45.5098 | 2024-10-03 01:05:01 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0c4b83-8b78-314c-8cf0-316dd84aaaa8 | -8.8482 | -45.523499 | 2024-10-03 01:05:01 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 41bb8435-8ff4-3824-8489-bc46ced10584 | -12.6296 | -63.084599 | 2024-10-03 01:05:02 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 85c36a90-907d-336c-8a99-41a7f4a6b6ee | -12.6351 | -63.114399 | 2024-10-03 01:05:02 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5f44afc6-2285-338f-9f91-a663a540217c | -10.6548 | -53.687801 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d89913f2-fae3-341b-9b62-8c3c5d828f92 | -10.6564 | -53.695202 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b887a544-dc02-3160-99e7-106ff21df228 | -10.6581 | -53.702599 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59f39658-a029-32c5-9048-eb746d3ae7ad | -10.6597 | -53.709999 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecb6e784-acb8-3185-b695-170f6723f921 | -10.6434 | -53.682598 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0388db36-8baa-39da-be4a-64a7ffda92b1 | -10.645 | -53.689999 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10629364-da85-3df7-9c39-2b7f35fcc3aa | -10.6466 | -53.697399 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81a964f5-7197-3250-b636-de2e6434cf26 | -10.6483 | -53.7048 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 319307ed-ce9f-3648-a1fa-383fa6dc00ee | -10.6499 | -53.7122 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e6e75b9-984f-30cd-887a-a7da5d958751 | -10.6336 | -53.684799 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f003473-84cf-365e-8f37-bde044a35f09 | -10.6352 | -53.6922 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a76d1533-83ed-3835-8f2a-96188ba321fd | -10.6368 | -53.6996 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5e87a62-8624-3837-ae01-30cf0c20ba1f | -10.6385 | -53.707001 | 2024-10-03 01:05:03 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 677be7e9-5310-325f-93f8-9ee13aadca8b | -10.627 | -53.701801 | 2024-10-03 01:05:04 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11ff7363-ec1a-342f-a105-2a66aaaad348 | -9.7822 | -50.081001 | 2024-10-03 01:05:04 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a093c09-4401-3c02-ad39-fc94e459ce86 | -12.3997 | -62.9753 | 2024-10-03 01:05:06 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 41f0552e-cb8e-339f-a002-d4b91193a1ae | -12.39 | -62.9771 | 2024-10-03 01:05:06 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 36db7927-42fe-3e0c-a857-7de166a5c946 | -12.3954 | -63.006199 | 2024-10-03 01:05:06 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e11e987-fb61-35fb-9a6c-54bb00c7145b | -12.3803 | -62.978901 | 2024-10-03 01:05:06 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d0755c48-d62a-3ad1-a4a0-15d41a5c0770 | -8.1864 | -44.360298 | 2024-10-03 01:05:07 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e80e1f13-ed38-3cbe-8ee4-50cb65072d22 | -7.8519 | -43.0798 | 2024-10-03 01:05:07 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bdae83c2-8a94-39d5-827b-d42f8a31665e | -7.8572 | -43.100498 | 2024-10-03 01:05:07 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 621ddff5-e5b4-3bef-bdc9-656c1a11d8d8 | -8.1767 | -44.362801 | 2024-10-03 01:05:07 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0104e96-3438-3aa0-a6fa-07a808df7bd5 | -8.1809 | -44.379501 | 2024-10-03 01:05:07 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e50970e5-3405-3701-afbe-052814c4f3ee | -10.2186 | -52.701801 | 2024-10-03 01:05:07 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4831083d-c310-374f-bf8e-f6ce4d4580ef | -9.599 | -50.0924 | 2024-10-03 01:05:07 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c367ccb8-a4f6-36fa-92a8-5bbfb7ad2381 | -9.6008 | -50.099899 | 2024-10-03 01:05:07 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a3de930-66d2-375b-a7c9-15d0b1bc84fa | -9.7323 | -50.6646 | 2024-10-03 01:05:07 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9427e1be-f5f1-3243-8505-299f8ade5d17 | -9.5889 | -50.1814 | 2024-10-03 01:05:07 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 536c1a63-84b8-32d9-96be-b7007f942273 | -9.5907 | -50.188801 | 2024-10-03 01:05:07 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e641755a-193f-3a47-a2ad-1be0bf20b6db | -3.4 | -42.27 | 2024-10-03 01:05:07 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15345f50-0f59-3531-99ae-a4608ade10e0 | -10.5247 | -54.590801 | 2024-10-03 01:05:08 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6c51e21-e2b6-390d-a25a-d915d58c184d | -7.704 | -42.9837 | 2024-10-03 01:05:09 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7a74f372-c03f-35e9-bb6b-db2baa3e286f | -9.1672 | -48.743999 | 2024-10-03 01:05:09 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9848a737-41c7-3922-b90e-3b5a3491426c | -9.1692 | -48.752701 | 2024-10-03 01:05:09 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README30.md)
