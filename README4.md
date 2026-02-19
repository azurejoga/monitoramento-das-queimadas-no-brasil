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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2505858-f405-326e-948c-23c7e47d2d52 | -22.78627 | -49.35658 | 2026-02-19 04:31:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a15e47e-2964-3884-ad10-4b5df9d59feb | -20.80743 | -49.84029 | 2026-02-19 04:31:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 18eb6fad-204c-3fa6-a7d8-b67621c0ee83 | -17.71987 | -42.20953 | 2026-02-19 04:31:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f44076e3-51c1-31ae-b947-6cd73cb9f4aa | -21.70293 | -48.43169 | 2026-02-19 04:31:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d96d9c9d-d96b-364d-b5d8-c7a17e22f596 | -17.71932 | -42.21409 | 2026-02-19 04:31:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d019d370-55d1-3279-ac23-9f584169f8f7 | -23.01144 | -49.90197 | 2026-02-19 04:31:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 94783c53-7060-3730-bfce-a112d8699124 | -22.78294 | -49.35598 | 2026-02-19 04:31:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe52505f-bf19-3a97-b15d-1d5edf005d72 | -30.73378 | -54.98166 | 2026-02-19 04:33:00 | NOAA-20 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 1a29dccb-6aee-36de-a2c7-259d495232dc | -27.68871 | -48.74912 | 2026-02-19 04:33:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 48277757-7693-372e-8886-5d84f279b9a7 | -27.6881 | -48.75352 | 2026-02-19 04:33:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2882d06e-c812-3029-95ff-1479ce521ceb | -27.26635 | -48.72864 | 2026-02-19 04:33:00 | NOAA-20 | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 327f68ee-f3ae-3f0e-900c-1fe4bf6c3398 | 4.43012 | -61.07715 | 2026-02-19 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c4d8779-5a7c-352e-bb90-b4ae2236726b | 2.43125 | -61.38879 | 2026-02-19 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70ea0cd2-3533-3f51-aa6a-9f89dd5b1a44 | 2.53172 | -60.72342 | 2026-02-19 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d5a0b17-4434-303b-b11f-3d7f0150ec6a | 2.68644 | -60.16757 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 53a7039c-4245-3ba5-9ec5-3f49c760465b | 4.48668 | -60.12764 | 2026-02-19 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42049dc2-8331-3d3f-896a-ac1ba3b68e3c | 2.53542 | -60.72285 | 2026-02-19 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 8dd7ebe6-3124-3218-b40f-fc87ad96528f | 3.75518 | -59.71463 | 2026-02-19 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 252a05da-c5ee-3d3c-83e4-cca784ae3a9c | 2.65921 | -60.13374 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8aa7fe84-46b0-366c-a06e-affeb57aea37 | 2.68094 | -60.15572 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ca819eb7-87ba-3859-b124-899efd84a093 | 2.69367 | -60.23865 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ef5bd595-438f-303a-86b9-a5d5e8c40674 | 2.69303 | -60.23447 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 33237c95-af22-31b9-9e51-8f944ef3f611 | 2.51713 | -60.98893 | 2026-02-19 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cd07bad-6dbb-3a1e-8475-37404a7ab15f | 2.76349 | -60.28356 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ba61ca9-1061-30a6-b58f-60090e834497 | 0.74776 | -52.03551 | 2026-02-19 05:16:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5704a7a3-b006-3964-8fa2-1967348265ad | 2.68812 | -60.15464 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fcb2e665-877c-3fa2-b31f-800b5067720c | 2.6628 | -60.13319 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f8f838e-f1ca-3ffe-8c62-4a60a0885118 | 2.76415 | -60.28773 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb6d8a00-2107-38e5-92af-6fa110fa7e0e | 2.6858 | -60.16344 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 27f265f1-4792-3f22-bb05-4f2a4abf7cd4 | 3.92117 | -60.57579 | 2026-02-19 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41e8557b-b384-3c50-9ef8-2d78529036a2 | 4.14795 | -60.71762 | 2026-02-19 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76619ad7-1420-36be-915d-75756a956225 | 1.36783 | -60.05695 | 2026-02-19 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 657586dc-b464-3bc9-9d49-5eef2f5fc497 | 1.75566 | -61.15674 | 2026-02-19 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a692b65c-8bf5-3f32-b4a7-4060a518b0d8 | 3.07342 | -60.92325 | 2026-02-19 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c251caf5-3432-35d0-afeb-619812eeeaf7 | 4.05763 | -60.28603 | 2026-02-19 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff0c92b0-a16c-3758-8056-4cc26bea70ae | 3.9249 | -60.57523 | 2026-02-19 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff139a70-500a-305a-9a97-5b4bfcfe564b | 2.69728 | -60.23809 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c6417de4-830d-3519-bb8f-c6634ddae21a | 2.6839 | -60.15106 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 036240f2-a734-3a49-bd03-4c2782ca2249 | 2.68453 | -60.15518 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 85e8fd7a-02b1-324c-8a69-aa176f567c53 | 1.9777 | -60.7024 | 2026-02-19 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46f85bd7-319e-3b44-b296-1fdb36537ed3 | 3.0666 | -60.92896 | 2026-02-19 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a378f399-dfe0-339b-bd4b-9c8b08960ece | 4.05697 | -60.28172 | 2026-02-19 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76e341cf-269b-38e9-9c92-b5a1b73c3e92 | 4.42626 | -61.0778 | 2026-02-19 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4eb03c1-a65a-3253-8430-27a6fef491cc | 2.69006 | -60.23919 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a70e3f1d-60a1-370f-93fb-2a67ce404953 | 2.69664 | -60.23394 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c4098931-f818-3e95-9273-d9d0c3ab8f9c | 2.682 | -60.21065 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e63702b3-189e-3717-80f8-1013e3f1f13d | 1.34669 | -60.06013 | 2026-02-19 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91b24234-4656-3ef4-b0f7-4b3273ecae0d | 2.52736 | -60.7196 | 2026-02-19 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fde35a6-96ec-38e3-9704-711d2121405a | 4.3388 | -60.21468 | 2026-02-19 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d4103f3-dbbe-3b3e-a07e-3481484f44aa | 3.96269 | -59.6968 | 2026-02-19 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03aa92b3-9e21-3808-9afd-e635206e88fb | 4.24581 | -59.79801 | 2026-02-19 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae864983-860b-321b-b041-254dc93c7025 | 2.68031 | -60.1516 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f48ba4f6-0d02-30ed-959c-8af626747652 | 2.53105 | -60.71904 | 2026-02-19 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61543f24-3588-306f-8a40-4a0f0932ef00 | 3.7558 | -59.71867 | 2026-02-19 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c1e1838-8a0a-37c9-91e7-97d04aa374b0 | 2.76493 | -60.28457 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05aa40e7-7d3a-3270-bc7e-ec89df60de12 | 1.36845 | -60.06091 | 2026-02-19 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44306905-9a60-3833-b41b-ced88982e5c1 | 4.28524 | -60.08342 | 2026-02-19 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ec23ea2-b4e3-3135-a347-c2ddfa9e7d34 | 2.65563 | -60.13428 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 627be866-f889-3cb5-8f88-3100e65ac484 | 3.28175 | -60.5312 | 2026-02-19 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02893c43-d111-38c0-a49b-3199fbcf698b | 1.35021 | -60.05962 | 2026-02-19 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e881570-cff7-348a-a148-d44303286bb5 | 2.696 | -60.22977 | 2026-02-19 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5118377-7429-39b9-9b4a-95cc799fd41d | 3.94288 | -60.56795 | 2026-02-19 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 644d1fb0-184d-3ea9-a924-6d9fed0499eb | 3.92558 | -60.57972 | 2026-02-19 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b9a53da-dd64-3594-b126-aac99a0daf2b | 3.94243 | -59.68346 | 2026-02-19 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b5927c2-28d8-309e-9604-36b7e296e2f0 | 4.20216 | -60.45458 | 2026-02-19 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9de57863-7aef-386d-8b0e-b7c838ae29cd | 4.20348 | -60.45323 | 2026-02-19 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2460aa61-25d4-3233-bf7d-2b47a25cfa65 | 4.29106 | -59.99905 | 2026-02-19 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72fdf205-8413-3a3a-b646-b47894c29dcf | 1.36492 | -60.06146 | 2026-02-19 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2454c2ee-1226-3316-adf5-1999ccdfb392 | 1.3496 | -60.05566 | 2026-02-19 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 493c0823-0b54-3f8e-ae98-bfe1259212a3 | 4.4868 | -60.12835 | 2026-02-19 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44eb30af-9d5b-395c-af02-e9d4bf40f176 | -10.67175 | -59.36719 | 2026-02-19 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a4352b-6e4f-33ad-b029-f0cbd9357747 | -12.30896 | -57.36842 | 2026-02-19 05:20:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c40b7fcb-b846-3ba1-84dc-dfc982f89153 | -11.83787 | -58.04864 | 2026-02-19 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94a95a68-5262-3e2b-aa60-32403af42b9a | -11.00339 | -54.01039 | 2026-02-19 05:20:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb358719-9c30-3ca3-9391-2c48feabe12f | -11.70534 | -55.45597 | 2026-02-19 05:20:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16b941ad-28fb-3705-ade1-f617ab5702cf | -12.31254 | -57.36895 | 2026-02-19 05:20:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2bdbb027-ed1f-3e00-ade3-38819d4a990c | -10.74153 | -59.22291 | 2026-02-19 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d54dbaf-4979-3325-a6ed-c88d6d6e9442 | -10.31528 | -58.50016 | 2026-02-19 05:20:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaa3ac42-28ae-3014-8392-e436d47d9217 | -11.00576 | -54.00843 | 2026-02-19 05:20:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2573bda5-6dec-3229-a233-6c3e662149c0 | -10.67067 | -59.37423 | 2026-02-19 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4aa7d928-624b-3d5d-8825-8c23c9ffa168 | -10.6679 | -59.37018 | 2026-02-19 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9314636-cdf4-3ba0-839f-ddb9401fa940 | -10.66844 | -59.36666 | 2026-02-19 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abb45573-74b3-3f38-a9eb-dfea0e56d9c7 | -12.31671 | -57.36534 | 2026-02-19 05:20:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e3df9911-52c8-3cb0-9e7e-020939d02191 | -13.5729 | -47.08804 | 2026-02-19 05:20:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4f91a78-aedf-3eba-ab7f-5b6d8bc712ed | -11.00087 | -54.01194 | 2026-02-19 05:20:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cef2bcf-2675-3418-acc3-16af359a421e | -12.31314 | -57.36481 | 2026-02-19 05:20:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1a21e47-8176-3f96-8231-0c4905ee8187 | -13.6621 | -60.63471 | 2026-02-19 05:20:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5d1e830-4b38-3662-a257-fcf2c88d0c12 | 2.76371 | -60.28671 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a94dae78-83d9-36e2-acd8-5ef874d84696 | 2.68261 | -60.15392 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cf72a4d2-ee96-3123-8b51-55d3bef29ba7 | 4.17019 | -60.36917 | 2026-02-19 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9dda8620-abd9-3595-9634-6c27d72b7c56 | 3.06894 | -60.92525 | 2026-02-19 05:46:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9ce61fd-3015-3794-a260-b2f9d6b199af | 2.68459 | -60.1664 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| baaa2c22-c9c5-30dd-b3f5-0233a5eceefc | 2.69283 | -60.24153 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bbaec33e-fb8b-3a04-83f6-6953e7c976cb | 4.05459 | -60.28118 | 2026-02-19 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34a91c61-afd7-3a2d-862e-9aaf4522e50e | 3.96307 | -59.69688 | 2026-02-19 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c018b289-689f-3ccd-8b9b-b4f500ec533c | 2.53071 | -60.7195 | 2026-02-19 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71ae5f01-6b12-3ddd-9cf7-0910455cd71f | 4.42811 | -61.07557 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed006440-b4a4-3f84-b8ff-a620dfab1b1f | 3.72442 | -61.13449 | 2026-02-19 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 153b57b1-b5b4-34d5-8d5e-f1dc487e2453 | 3.06832 | -60.92141 | 2026-02-19 05:46:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 415031b5-6778-3539-aade-5b9715f9a9f7 | 3.92164 | -60.57409 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README5.md)
