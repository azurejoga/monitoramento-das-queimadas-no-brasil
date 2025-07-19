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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 213a247c-f073-332a-abeb-77335eae8115 | -3.1384 | -47.0068 | 2025-07-19 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 319d92d2-eb21-34bc-86d6-803606e6cb44 | -5.6379 | -43.7175 | 2025-07-19 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 93d33032-22df-3a35-9a64-e99b2ce3b2a2 | -11.7317 | -48.1849 | 2025-07-19 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 257.6 |
| 67b8db2d-d1d4-337c-8079-8ba2174b02d4 | -10.6438 | -44.7645 | 2025-07-19 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 35b5c52e-c671-3ed6-9d38-60ef1f146e8f | -11.7126 | -48.1874 | 2025-07-19 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 7622860f-02a3-39ac-bcff-473e38d1b456 | -9.6104 | -40.342 | 2025-07-19 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 06bbc77f-262d-33f9-b292-334e92494bf4 | -2.9109 | -48.2325 | 2025-07-19 01:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 9a168217-0335-3d06-a60e-d7b26121b858 | -14.1798 | -58.4354 | 2025-07-19 01:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 46eafa9b-ec9d-3e62-973d-544270a79e5b | -5.6567 | -43.7161 | 2025-07-19 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 266.2 |
| 026bd934-84a2-3904-9b24-06fd720bee9b | -7.4735 | -47.493 | 2025-07-19 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 456f94de-c10b-3dff-a400-47ad1fd8c5a4 | -6.1606 | -48.0507 | 2025-07-19 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 3e621ad2-2230-322d-94a8-efc868cc8dea | -22.842501 | -46.834599 | 2025-07-19 01:18:00 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ef81ade-3cad-3741-8aaa-4af4c6b63db4 | -23.5462 | -51.6189 | 2025-07-19 01:18:00 | METOP-C | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a156a13-1144-3432-866e-2fc5874b9ccc | -21.036699 | -49.870602 | 2025-07-19 01:18:00 | METOP-C | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4436edef-a1ed-3696-89d4-bab2a3a39c25 | -2.9136 | -48.230099 | 2025-07-19 01:18:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 932e305e-cff4-378e-bc3a-b7a05743f18a | -22.832899 | -46.837601 | 2025-07-19 01:18:00 | METOP-C | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| baa5c7cf-3e4b-3e78-87a8-588a3cc990f2 | -3.1224 | -47.0037 | 2025-07-19 01:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b97aea31-377e-3b34-955a-ceaa4925f084 | -22.7024 | -47.247398 | 2025-07-19 01:18:00 | METOP-C | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 09f878e4-f3c1-335b-bd2c-13dfa2bd6fbb | -3.1319 | -47.0014 | 2025-07-19 01:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b9a85fc-19ae-327e-afd4-be88265a787a | -2.9101 | -48.257702 | 2025-07-19 01:18:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f87b7283-d5c6-3f31-ad0c-6aa0883fda48 | -2.904 | -48.232399 | 2025-07-19 01:18:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32e2f733-3e6f-3ae2-abc8-5dd050c53b55 | -23.5481 | -51.627102 | 2025-07-19 01:18:00 | METOP-C | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c3444e5-0ace-320f-8a84-bf9147cbb020 | -21.042801 | -55.9818 | 2025-07-19 01:18:00 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7c88a4db-adaf-3539-8f51-1dce1ff4eceb | -2.9198 | -48.255402 | 2025-07-19 01:18:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e74ac7c7-22d4-3e0d-9fed-5227aff4ed5e | -3.1415 | -46.9991 | 2025-07-19 01:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6f96caa-a829-3f96-8030-4d0cdd6fd4d8 | -9.6104 | -40.342 | 2025-07-19 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 166.4 |
| 3283429c-eab8-3daf-919f-40d3f45f33b9 | -3.1384 | -47.0068 | 2025-07-19 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3f18a887-c252-321e-bf41-527457d320fa | -7.4923 | -47.4914 | 2025-07-19 01:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 92492d0c-3f13-305c-a362-7066f0ab4906 | -5.6379 | -43.7175 | 2025-07-19 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 25f9f5e3-3bc4-3a65-ab7f-9038a6ee4779 | -2.9109 | -48.2325 | 2025-07-19 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a08b02d6-1435-3b84-97f8-02e39680e7e1 | -10.6247 | -44.767 | 2025-07-19 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| b4afba57-0ae7-3556-bf4f-298e3a637655 | -11.7317 | -48.1849 | 2025-07-19 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 217.9 |
| a09c9f6b-3b9f-3a2f-8dbd-86cd56c0ea88 | -9.6108 | -40.3171 | 2025-07-19 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 1bcfd574-d691-3b0b-b978-8cd88397ad40 | -5.6567 | -43.7161 | 2025-07-19 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 7bedc29f-0fbe-3474-ae26-56a6c8866e32 | -9.8104 | -48.5622 | 2025-07-19 01:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 0e668180-2497-3665-b56a-a0996a93fb02 | -5.6565 | -43.7393 | 2025-07-19 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 97c9a313-db95-3246-bd60-b8d116c1b884 | -22.7046 | -47.2429 | 2025-07-19 01:20:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 49.9 |
| c19d91ac-8c00-31a1-a379-79c9f303c7e2 | -7.492 | -47.5134 | 2025-07-19 01:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 5cfd6ce9-35ce-3a3b-812a-1a00eb963045 | -11.7126 | -48.1874 | 2025-07-19 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| d532499c-723a-38b9-8b8d-8802e7c1b024 | -11.4786 | -47.3306 | 2025-07-19 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| b82982a1-289e-340e-b7d4-649befe09b72 | -11.7313 | -48.207 | 2025-07-19 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 38a20d2c-4e85-3a21-8e34-0a8bc2a3778a | -10.6438 | -44.7645 | 2025-07-19 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6d769bbf-2bd7-3491-801e-4ea8ae720155 | -6.1606 | -48.0507 | 2025-07-19 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 9ef63c79-55c3-3438-a5f8-13d6dfefd409 | -11.7508 | -48.1825 | 2025-07-19 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 7cf1b278-1605-3190-ad76-a88d4d03ed34 | -2.9108 | -48.254 | 2025-07-19 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 6a2029c5-84b0-3fa4-8b26-b0f91f02c943 | -3.1198 | -47.0075 | 2025-07-19 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 07060f79-18f1-3811-af4f-5ab2b69016cb | -6.1792 | -48.0494 | 2025-07-19 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ec4eedd5-8f38-39e5-800a-1b96a6f728b5 | -11.7317 | -48.1849 | 2025-07-19 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 222.4 |
| 6db595c0-8422-3f7d-a7cb-981881e74755 | -11.4786 | -47.3306 | 2025-07-19 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 79f4ed87-9b4c-3c8e-808a-f5671096ba8c | -10.6438 | -44.7645 | 2025-07-19 01:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 59329977-579a-3154-9d58-174f0e30818d | -2.9108 | -48.254 | 2025-07-19 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 49e2d027-4811-3bae-b9de-a5b2a30e7fa4 | -6.1606 | -48.0507 | 2025-07-19 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 09c16471-4687-38b7-9529-c8fc0d00aded | -11.7126 | -48.1874 | 2025-07-19 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 39c2bcd2-d96f-370a-aae6-86b74967527e | -22.7046 | -47.2429 | 2025-07-19 01:30:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 82.4 |
| d3cfd154-b132-3305-b157-4757f8c3b2d2 | -11.7313 | -48.207 | 2025-07-19 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 965eb9bd-898b-3d17-aeaa-28d7beebb412 | -3.1198 | -47.0075 | 2025-07-19 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e7720811-4dab-3fb9-8fa2-c5fbb72bb76b | -6.1792 | -48.0494 | 2025-07-19 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ee337325-cb84-3800-a1ef-cb5e87958a73 | -5.6567 | -43.7161 | 2025-07-19 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 1c67f2d7-413b-39f1-9a52-7a75d1d17a0a | -9.6104 | -40.342 | 2025-07-19 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 4e951a21-0561-3a1f-8bab-49f686e26750 | -11.7508 | -48.1825 | 2025-07-19 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8c9eff2d-ff54-31a9-9c78-9777389ed7ef | -10.6247 | -44.767 | 2025-07-19 01:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| daf02af1-fa71-36b8-ae2f-8cc57d06bda8 | -3.1384 | -47.0068 | 2025-07-19 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 2d3d5805-873d-3dd5-991d-ec32462f85c8 | -22.7038 | -47.267 | 2025-07-19 01:30:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a39dda05-073b-348c-b20c-0409c1535ace | -9.8104 | -48.5622 | 2025-07-19 01:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 0643f511-1328-36d4-9f1f-d6a0dbb27eda | -7.492 | -47.5134 | 2025-07-19 01:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 13f25f56-d9be-313f-9571-976b2f40d64a | -7.4923 | -47.4914 | 2025-07-19 01:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| e769f019-6174-3510-bc0d-be990e81345b | -2.9109 | -48.2325 | 2025-07-19 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| c91dd69b-7dec-3dea-b999-980b7a004257 | -5.6379 | -43.7175 | 2025-07-19 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 22020048-f58c-343a-b625-25b65ba49eaf | -6.1606 | -48.0507 | 2025-07-19 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 6f6f1d7b-0dab-34f5-81d8-eca48f73c591 | -22.6835 | -47.2485 | 2025-07-19 01:40:00 | GOES-19 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 56.2 |
| c6e68ef7-10cf-3886-bc7e-5312b7fee2d1 | -10.6438 | -44.7645 | 2025-07-19 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 4660e713-0bed-36f0-9c48-83c0f739e029 | -11.4786 | -47.3306 | 2025-07-19 01:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 32563a40-2495-3d76-9db0-64de61fee371 | -3.1384 | -47.0068 | 2025-07-19 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d032f07a-8a50-3f5f-a299-0718c1af5993 | -3.1198 | -47.0075 | 2025-07-19 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 40ecf897-a1b6-3114-a127-3e3029ae3ebc | -10.6247 | -44.767 | 2025-07-19 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 9a2b1849-df9c-3088-bbc5-8fd93a4a14bd | -11.7508 | -48.1825 | 2025-07-19 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 64bf68d0-6b29-3eb7-9b5e-238d8ec65617 | -7.4923 | -47.4914 | 2025-07-19 01:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 4bf38e2d-37dc-3920-aff7-dfb003eee4dd | -2.9108 | -48.254 | 2025-07-19 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| a628456f-2941-32ee-8a85-ea7263a208d2 | -22.6828 | -47.2726 | 2025-07-19 01:40:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 7be73a57-65b8-3c87-958c-bf244e302acc | -5.6567 | -43.7161 | 2025-07-19 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 228.9 |
| e123397d-b155-3e22-bf8a-937382121cda | -22.7046 | -47.2429 | 2025-07-19 01:40:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 90.9 |
| ac7804a8-68b0-317b-bb8d-38e64c44e873 | -9.8104 | -48.5622 | 2025-07-19 01:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 0d23b1df-c173-3905-8ad4-09e029f0ec8d | -5.6379 | -43.7175 | 2025-07-19 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| bfac1c0e-4357-3e25-8257-681b67c09624 | -6.1792 | -48.0494 | 2025-07-19 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 05aaaffb-6722-334f-adcd-0253706c207a | -2.9109 | -48.2325 | 2025-07-19 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 50e67ec3-fd94-3d6f-88c4-60b49e433802 | -11.7313 | -48.207 | 2025-07-19 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1fdb437d-cb23-3e97-85ff-9b617178ff3c | -7.492 | -47.5134 | 2025-07-19 01:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ced39b92-3a48-3a74-b1f6-f182e5818c2f | -22.7038 | -47.267 | 2025-07-19 01:40:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 101.1 |
| b84a2783-c9f5-342d-913b-9554cd44d0dd | -11.7317 | -48.1849 | 2025-07-19 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 237.9 |
| 49fb82ba-4ac0-3432-99a5-e562aceaa9ac | -14.19663 | -58.44458 | 2025-07-19 01:41:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| fba5c6db-61e8-3ac4-afcd-5c445b7ffad2 | -14.18164 | -58.20078 | 2025-07-19 01:41:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 895082f3-313e-336a-895c-d0fe04ea8d7c | -14.17458 | -58.19558 | 2025-07-19 01:41:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ee9bc23b-c926-3da5-86b9-a1aa402d8e88 | -14.17755 | -58.21312 | 2025-07-19 01:41:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9e2d0e95-380d-32c6-a63e-0d10eaa099df | -14.16966 | -58.2029 | 2025-07-19 01:41:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ad45e7db-7cd3-32ca-9984-f876b0da7c40 | -10.29956 | -60.5489 | 2025-07-19 01:43:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5a1b3b18-aa1d-301b-b728-7afe10c380f6 | -11.84406 | -63.22562 | 2025-07-19 01:43:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| fba3cacd-d4b6-3ffd-bbd1-420798f24f22 | -9.01704 | -59.76997 | 2025-07-19 01:43:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 140b4585-522f-305a-904a-f6659034bb96 | -8.96945 | -61.51214 | 2025-07-19 01:43:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 5fd05b2d-2299-367d-a37c-b522d2b739b7 | -7.48712 | -63.82135 | 2025-07-19 01:45:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6111002a-99c6-3f74-b24a-803d59c083ba | -6.1606 | -48.0507 | 2025-07-19 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |


[Clique aqui para ver as próximas entradas](README7.md)
