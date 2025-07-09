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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81d991c8-b33a-3f41-add5-9ec5bb971fc7 | -10.6324 | -49.445599 | 2025-07-09 00:35:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e6024d6-bee2-3e87-924b-86a63626cc86 | -6.6768 | -46.2994 | 2025-07-09 00:35:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24756fc4-9a92-3d2d-8ce6-912400690128 | -11.3324 | -55.206402 | 2025-07-09 00:35:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16fb968a-5417-37a4-b20f-419f1ff26ece | -8.5071 | -43.267399 | 2025-07-09 00:35:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3a969086-fd45-3096-814c-861219c2c555 | -10.1893 | -51.1465 | 2025-07-09 00:35:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f73d6d09-ce57-39da-afdc-fdde62bc4962 | -11.4489 | -45.091702 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 138dff1f-5800-3b82-acb1-b9d8120662c9 | -10.5661 | -49.118301 | 2025-07-09 00:35:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d541dea2-1e83-31de-ab93-01a698c00a5c | -5.5882 | -52.082901 | 2025-07-09 00:35:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18017537-8560-3e6e-bdf2-20112ad29410 | -10.6363 | -49.462399 | 2025-07-09 00:35:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b715ac8d-c3b9-3b95-8bf0-fd5af2db4180 | -10.1795 | -51.148701 | 2025-07-09 00:35:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c1be4b1-1050-370f-ba74-535d9e4d7157 | -6.1535 | -48.029999 | 2025-07-09 00:35:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 133ec99d-72dd-38f0-a7a4-db7c002a2b23 | -22.622299 | -47.915699 | 2025-07-09 00:35:00 | METOP-B | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a05dd74c-f01e-3cdb-ae48-cf16ca15b77d | -5.2254 | -45.221901 | 2025-07-09 00:35:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa7250e4-bba8-36c2-9fb0-314a6195be98 | -17.3311 | -47.4865 | 2025-07-09 00:35:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8cdf344d-6b5a-34c2-ac97-7209dbd29f6a | -6.173 | -48.025398 | 2025-07-09 00:35:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 550c11d5-63fc-36b2-b7b5-a94a7d7fc630 | -15.3777 | -47.3214 | 2025-07-09 00:35:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 085d0b79-a468-3abc-95a9-33a96afa8065 | -7.09 | -49.1642 | 2025-07-09 00:35:00 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8b16364e-b6d4-3465-9e05-85e6440bc66d | -6.6732 | -46.284599 | 2025-07-09 00:35:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67c043ec-447d-35bd-abe3-c21a7dae1837 | -9.2233 | -48.588001 | 2025-07-09 00:35:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abca6858-84c2-38c1-92c9-ce34e2f2842f | -5.221 | -45.2034 | 2025-07-09 00:35:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a51d5ac-02c0-37bf-a11c-5ca4a5529b10 | -7.6624 | -44.362701 | 2025-07-09 00:35:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7a6cced-a1e8-3eaf-aa97-d27c919c782e | -10.5563 | -49.120701 | 2025-07-09 00:35:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d54a2c46-23d9-377a-95ac-98e7694aa291 | -5.2307 | -45.201099 | 2025-07-09 00:35:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f4f6c7f-b205-3c84-ba7f-18711134377f | -4.5499 | -47.993099 | 2025-07-09 00:35:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2aa641a-5723-3073-bc61-dcef78eb31cf | -8.4918 | -43.247601 | 2025-07-09 00:35:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 66c3d62f-1b02-3974-89be-42bedb6294ce | -14.8546 | -45.110401 | 2025-07-09 00:35:00 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 57494730-4ef2-3475-aa6e-82d29e28d77a | -11.4429 | -45.1092 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd4fa453-9a8c-3c43-9227-babe793812fb | -17.3332 | -47.495499 | 2025-07-09 00:35:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25e98d20-700e-30bf-8b3e-2bf00f06d7ae | -10.3514 | -56.474201 | 2025-07-09 00:35:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24ce0ba5-3724-309f-aa45-cbb4c36ca11c | -11.4392 | -45.0942 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29c76fc2-f228-3fe9-a43c-c7e88ad0311a | -8.5211 | -43.3063 | 2025-07-09 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 198.6 |
| ccec9a35-8506-303a-975e-887df592d0c0 | -10.5779 | -49.1098 | 2025-07-09 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 92eae905-f881-3e22-8dc0-059456cd91e8 | -18.6467 | -55.7351 | 2025-07-09 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 45de57ef-bc6b-3424-8ee5-6444101d13be | -11.6737 | -43.7762 | 2025-07-09 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 810fc0e2-bcff-3d57-873b-29cc27f61656 | -18.0208 | -50.4769 | 2025-07-09 00:40:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 4ed7b49f-248c-39d7-aaea-973e1a0e0f4e | -11.4205 | -45.095 | 2025-07-09 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 41566465-17c1-393c-acc4-e4814aa89979 | -8.5214 | -43.2828 | 2025-07-09 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 354.8 |
| 46161394-f4d2-3c2e-8a2e-b8bf80dc6713 | -10.5776 | -49.1316 | 2025-07-09 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 7cd71c7b-ef00-3ad2-87b6-6129217514f9 | -8.5022 | -43.3085 | 2025-07-09 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 297cb648-5238-3e22-ae83-63ed14ab8ba6 | -6.1794 | -48.0277 | 2025-07-09 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 31daf2bc-90ba-36a5-b8d4-fda56ce47b71 | -11.4584 | -45.1126 | 2025-07-09 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 25b62e40-8783-31a2-b7c2-140d5cd6d3f1 | -11.4393 | -45.1154 | 2025-07-09 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 227.0 |
| 8d918632-9d02-3b9d-893f-b2b26925b811 | -5.2328 | -45.2102 | 2025-07-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 26c393f4-8d39-32a7-85a9-e467519e7a89 | -11.4201 | -45.1181 | 2025-07-09 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| ca497e3d-c018-3c5d-a3bf-2ee137ea5f18 | -6.1792 | -48.0494 | 2025-07-09 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 844f052b-bef8-3b40-b868-dd507985985f | -6.1606 | -48.0507 | 2025-07-09 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| b0ffb6a4-9159-38ec-8a2a-90f15b6c7c51 | -8.5217 | -43.2593 | 2025-07-09 00:40:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 50f51531-0960-3e49-b942-c943076b7326 | -11.4397 | -45.0923 | 2025-07-09 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 62a9ca1f-de39-3c99-b290-92ff0bdc208b | -8.5025 | -43.285 | 2025-07-09 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 173.3 |
| 3058c757-7e91-3e50-8861-7d4dea398fe9 | -8.5028 | -43.2614 | 2025-07-09 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| d626c608-3e60-3db1-891d-cd2d4b8aafe8 | -11.4588 | -45.0895 | 2025-07-09 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| cf39455d-7ed1-346e-bf50-6260a7dd19cb | -7.2597 | -43.0645 | 2025-07-09 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 6fefc9fb-74d4-36d9-97bf-e878be637af8 | -8.5028 | -43.2614 | 2025-07-09 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 670260bc-fdff-3a9f-9aa4-75313a4ce7ab | -11.4397 | -45.0923 | 2025-07-09 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 6a066c46-9065-3456-8836-f74f9ec106b8 | -6.1792 | -48.0494 | 2025-07-09 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| a68c2f1a-c6d5-3fa5-aa73-2c371c3d0309 | -11.4393 | -45.1154 | 2025-07-09 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 998da10d-2679-3113-a185-7bda52a01a1c | -11.6737 | -43.7762 | 2025-07-09 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| dd736499-1e41-3cd7-80cf-ff5259f41064 | -11.4201 | -45.1181 | 2025-07-09 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 69014013-b054-33aa-b6d5-ce202194ccc1 | -8.5022 | -43.3085 | 2025-07-09 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| f769fa5f-e023-3ab6-9a74-6bd0b8309699 | -18.0009 | -50.4805 | 2025-07-09 00:50:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4c81a095-19cd-34fc-b6f2-bc81f7d78d76 | -8.5211 | -43.3063 | 2025-07-09 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 1d9767b0-9a5e-3b68-a024-fe7f3b8126b5 | -8.5025 | -43.285 | 2025-07-09 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 205.6 |
| 6c71aadd-851f-341e-8d30-c1019228f8b2 | -5.2328 | -45.2102 | 2025-07-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 904c98c7-1c4f-3298-8658-4a8e553b4cef | -7.2405 | -43.0899 | 2025-07-09 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 2083b2a9-2949-3bbd-baad-264635ed1828 | -11.4588 | -45.0895 | 2025-07-09 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 1ed1da2a-f8ae-346f-8aeb-8044f9ba7e66 | -10.5776 | -49.1316 | 2025-07-09 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| fbee3c22-fb8e-37cb-b953-ba10dfc7c000 | -8.5214 | -43.2828 | 2025-07-09 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 276.5 |
| 477c28d3-55cf-31dd-974c-1fad7a5e8059 | -18.6467 | -55.7351 | 2025-07-09 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| d9e5ecc9-e3c8-34d2-8e5f-d7e36d82af07 | -18.0004 | -50.5027 | 2025-07-09 00:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| e547b2e9-6762-3361-9da5-4d3362248877 | -11.4205 | -45.095 | 2025-07-09 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 0fbcb35b-7b38-3f56-8a6b-96042d730fc6 | -18.0203 | -50.4991 | 2025-07-09 00:50:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 3770245b-9c2a-3f36-ab98-d46313eb86a5 | -7.2408 | -43.0664 | 2025-07-09 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 162.5 |
| 8f0798a4-9f3c-3770-8885-711669049825 | -10.5779 | -49.1098 | 2025-07-09 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5f9f1afe-324e-3d25-b33e-e53858cf6673 | -18.0208 | -50.4769 | 2025-07-09 00:50:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 60dd48d6-78f2-3120-bd99-cfa7ad7c6fa3 | -8.5217 | -43.2593 | 2025-07-09 00:50:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| d9558e91-ed83-39e2-87a9-834b0068bbcb | -11.4584 | -45.1126 | 2025-07-09 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 8d06e5b6-6e00-3886-a210-fbf9e943b9d6 | -7.2597 | -43.0645 | 2025-07-09 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| a6cfbd95-9450-3ff8-9a93-cbe36451f5cf | -18.0203 | -50.4991 | 2025-07-09 01:00:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 284.5 |
| 1880de94-4fd0-37da-8ac6-a96c955cc427 | -8.5211 | -43.3063 | 2025-07-09 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 765903d6-a8f1-3d36-b53a-d50bc8f1a821 | -8.5025 | -43.285 | 2025-07-09 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 299.7 |
| aa29b79c-f9fd-3994-a3ee-ce704c745a48 | -17.7589 | -40.0761 | 2025-07-09 01:00:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 104.8 |
| af77f72a-c177-3506-bb0c-d9cd4a3eff38 | -10.5776 | -49.1316 | 2025-07-09 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 97044d29-1f1d-3f3e-9116-120e662b6ae1 | -7.2408 | -43.0664 | 2025-07-09 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 185.6 |
| 8e0e5101-6a66-3fba-91e7-27572b5f8a73 | -17.3367 | -47.5011 | 2025-07-09 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 0097c7a0-1ab8-31b5-8cda-a25d5a2b6ab6 | -18.0009 | -50.4805 | 2025-07-09 01:00:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 163.8 |
| a4295774-167b-391c-841e-b2ef48f2e30a | -7.2405 | -43.0899 | 2025-07-09 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| ddc3e609-72ce-3f3a-a7d3-3ee7fb27d3b9 | -5.2328 | -45.2102 | 2025-07-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c6bcf4ca-d264-37af-8934-b7e0a9405db2 | -7.2219 | -43.0682 | 2025-07-09 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 963c9501-66e3-386b-8692-7d93f44a6564 | -8.5028 | -43.2614 | 2025-07-09 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| dd0954eb-1ce2-3531-836a-e1e3c6fdda77 | -17.7783 | -40.0966 | 2025-07-09 01:00:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| da1b91aa-5286-3861-9bfc-295d6627d8bc | -8.5022 | -43.3085 | 2025-07-09 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.7 |
| 07b066b7-c256-33e4-b2e1-4a51544799b4 | -17.7581 | -40.1021 | 2025-07-09 01:00:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 145.1 |
| 10b86745-1acd-37d9-b703-c2ea70095267 | -8.5214 | -43.2828 | 2025-07-09 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 283.4 |
| 3b5a636c-f21d-3424-ae2f-1fdf356d6c82 | -10.5779 | -49.1098 | 2025-07-09 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b64e7e37-75a5-3a8a-912d-2dd681dc6e29 | -18.0208 | -50.4769 | 2025-07-09 01:00:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 197.0 |
| f3c89db0-e81c-352d-9727-4e47815f3f2e | -18.0004 | -50.5027 | 2025-07-09 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 90316554-8420-3fa5-baeb-56069bb2b586 | -10.5776 | -49.1316 | 2025-07-09 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 1ee5fe1a-ad8a-3680-95ec-62b02fd2f2e8 | -8.5025 | -43.285 | 2025-07-09 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 237.3 |
| 5d1c0026-9f92-39d6-b94a-11d4377e9ed9 | -8.5217 | -43.2593 | 2025-07-09 01:10:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 1bb45e08-e2c3-374e-b4d1-450210f6925a | -8.5022 | -43.3085 | 2025-07-09 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |


[Clique aqui para ver as próximas entradas](README4.md)
