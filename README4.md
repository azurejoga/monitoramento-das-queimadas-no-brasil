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
| 52dced8c-ce1f-359b-bafe-073b0c597a2d | -10.123 | -52.074799 | 2026-07-02 00:50:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c63aad2a-826c-3547-a460-7df098852ced | -12.5025 | -48.254101 | 2026-07-02 00:50:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9eced92b-b248-396c-a77a-b411ceb6dc0b | -19.5014 | -52.7118 | 2026-07-02 00:50:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| df5b91e7-fe22-32f9-9a6e-c4cdb31a7c1a | -10.8213 | -58.0033 | 2026-07-02 00:50:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1071ed19-1912-3124-b482-9abe77ebb4b1 | -19.503599 | -52.720901 | 2026-07-02 00:50:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2d73f990-d287-3fb7-b3f3-f1967cd6e689 | -11.4141 | -56.0406 | 2026-07-02 00:50:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f2ce6b6-9907-34fe-99ca-3ddf60812fd5 | -13.6548 | -60.608799 | 2026-07-02 00:50:00 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2940a7-adb8-3103-96d3-01f452117a63 | -11.6337 | -59.010101 | 2026-07-02 00:50:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 39a7f2b4-891e-30cb-bfc9-f404ae1e0101 | -11.3626 | -55.421799 | 2026-07-02 00:50:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8173e08-3222-3d97-b62d-92c939bd838c | -11.8087 | -56.991798 | 2026-07-02 00:50:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4830d761-0a2d-359a-88a9-2baa6fd3c1b0 | -11.4293 | -56.061501 | 2026-07-02 00:50:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 037ea16b-911c-30de-bfd4-6a4777673e14 | -10.8229 | -58.0103 | 2026-07-02 00:50:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58c5b3eb-520b-3928-a705-2f63fa13fc2f | -3.5084 | -48.019001 | 2026-07-02 00:50:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac72fe2-84f7-35dc-a210-53ac1ebb5082 | -11.4195 | -56.063801 | 2026-07-02 00:50:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ec353cd-883b-39f8-9a31-42bd234f7a5f | -3.9905 | -48.037102 | 2026-07-02 00:50:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99f26fbf-32ce-36b9-9271-2e0306298f9c | -11.4275 | -56.053799 | 2026-07-02 00:50:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57cd503b-61ae-3d47-9b6b-eff713ae0380 | -8.7162 | -48.339401 | 2026-07-02 00:50:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06723aed-3eab-3ca5-b2b5-387311d6bcc3 | -8.6506 | -49.690102 | 2026-07-02 00:50:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 109ca42c-eb92-3512-b605-1bed1d790a70 | -21.7838 | -56.287498 | 2026-07-02 00:50:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9c3adab8-fc3b-3a85-bcd3-611f909587d8 | -9.1998 | -58.037102 | 2026-07-02 00:50:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dea4267d-3f39-3acc-a61e-dd36c82e8ba3 | -21.8016 | -52.709499 | 2026-07-02 00:50:00 | METOP-B | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 83eb30e5-20be-375c-bbf2-004da037f2b0 | -11.6321 | -59.003101 | 2026-07-02 00:50:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b7d74dd4-d5bc-340d-bf9d-3edbb1f574bd | -11.4239 | -56.0383 | 2026-07-02 00:50:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a64e6ecb-594a-3845-93e4-04556f6e50f3 | -21.7708 | -56.275101 | 2026-07-02 00:50:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 802fe945-eb71-3fc3-b7bf-f98454713053 | -11.8103 | -56.999001 | 2026-07-02 00:50:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86b37ebd-fd4f-35f8-9bbf-8494a8fcd18e | -8.7 | -48.316601 | 2026-07-02 00:50:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 561e3117-1c4f-347a-9f9b-6af9bc0c554a | -21.7724 | -56.282501 | 2026-07-02 00:50:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7c68c72a-af60-377f-8018-d2e5fbf07266 | -21.7617 | -56.301 | 2026-07-02 01:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 93490130-82b4-386c-b56b-945a9dfc1ae0 | -4.0046 | -48.0618 | 2026-07-02 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| aaf4a231-b9cb-3804-81fe-17d9b1ce5fc1 | -21.7827 | -56.2762 | 2026-07-02 01:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 106.1 |
| d45d05af-0d53-37f4-bd60-110f29c14f4b | -21.7622 | -56.2795 | 2026-07-02 01:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 21198dd9-7c64-3593-a668-5db1f02f0b2e | -21.7823 | -56.2976 | 2026-07-02 01:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 101.5 |
| cc3a127d-3a9c-3abc-bba4-2e220477eeb5 | -9.1933 | -45.3114 | 2026-07-02 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 5b596544-974b-3667-bd58-5654cc52f577 | -9.2123 | -45.3092 | 2026-07-02 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 4f60e098-65c5-31f5-bb42-376aa3878237 | -11.8007 | -57.0032 | 2026-07-02 01:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| fdcc0a74-05ba-3ecd-9f26-a66c8dfa39f5 | -3.5228 | -48.0383 | 2026-07-02 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| dc88a3dd-5146-3253-bb71-c11a3115e6a6 | -11.4147 | -56.0726 | 2026-07-02 01:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| accc83f4-f391-384f-9e10-8ba1876a3388 | -11.4149 | -56.0525 | 2026-07-02 01:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 6136cf2a-0fc1-3e15-9d6d-6e8159966905 | -8.7208 | -48.3441 | 2026-07-02 01:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 4ff3345c-ad8c-306a-810c-487c1d91c920 | -12.5135 | -48.2802 | 2026-07-02 01:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| f69cb138-e385-3aac-badd-42dc3b324970 | -10.9397 | -43.0593 | 2026-07-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 84144095-e2a8-3611-b8ff-fc5d55c014fe | -10.9593 | -43.0326 | 2026-07-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 04a31651-2da4-327f-bb3d-1191e25b92ce | -9.212 | -45.3321 | 2026-07-02 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| f47f1232-071b-3b5c-8b81-32d94fa31f1b | -10.9588 | -43.0565 | 2026-07-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| eede6eaa-8916-39a3-bade-f5aef980626a | -10.9401 | -43.0355 | 2026-07-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 6aef4ecb-8832-3807-b86d-98b25141e3b7 | -21.7823 | -56.2976 | 2026-07-02 01:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 668eed9d-1f0f-318a-8a98-cbe0f623b913 | -9.1933 | -45.3114 | 2026-07-02 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 78589d1e-763c-3d6b-b204-605e60ef57e1 | -11.4149 | -56.0525 | 2026-07-02 01:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 33bbb8e1-def6-3011-a900-7282d2203259 | -11.4147 | -56.0726 | 2026-07-02 01:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 176a9bfe-1e81-3d43-bd77-b9d29c617cc4 | -11.8007 | -57.0032 | 2026-07-02 01:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| aa4ea0d5-fa0f-3956-a208-1238e304a863 | -10.9397 | -43.0593 | 2026-07-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 38191bff-7f0a-3cad-9887-7437901dc807 | -12.5135 | -48.2802 | 2026-07-02 01:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| bc1cbfcf-8a42-34c6-89c2-0edf96bdb3fa | -21.7622 | -56.2795 | 2026-07-02 01:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 79.7 |
| acef06e8-0ff0-3b50-a7d8-3d78a529c935 | -10.9401 | -43.0355 | 2026-07-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 2dc294df-fc04-3da9-93c8-7323f8616254 | -4.0046 | -48.0618 | 2026-07-02 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9cebfb9b-8d57-31c1-a075-6c12dbd08f19 | -9.2123 | -45.3092 | 2026-07-02 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 1fa4f3f0-d3a9-3ed5-9270-08378f24e1e6 | -11.4338 | -56.0509 | 2026-07-02 01:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f02ec2bc-ad00-3277-9b57-6a5619ec90c7 | -9.212 | -45.3321 | 2026-07-02 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| dcdae42f-3c9d-3cc1-af04-c7975c464db8 | -3.5228 | -48.0383 | 2026-07-02 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a9cc8edc-9fe0-339d-8873-25e88dc42d16 | -21.7617 | -56.301 | 2026-07-02 01:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 666583ee-958e-39a9-b77e-816b2f962134 | -10.9588 | -43.0565 | 2026-07-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| e613ed87-b5f9-3bfb-b7bb-55ddb765baec | -21.7827 | -56.2762 | 2026-07-02 01:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 8b69eb7f-0c44-34ec-b9c9-934a4ac678bf | -10.9593 | -43.0326 | 2026-07-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| b7a6bbe5-a6cd-3d8c-88bc-cf931436d2cf | -8.7208 | -48.3441 | 2026-07-02 01:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 6e13eb82-a500-3d97-b5cf-3e9281551d1c | -11.42 | -56.060501 | 2026-07-02 01:17:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5cdf18f-daa4-3bee-8ad6-65cf651c2c63 | -12.5194 | -48.281601 | 2026-07-02 01:17:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cd48662-27f8-3382-82b6-80ea99a4b9b8 | -10.8219 | -58.018799 | 2026-07-02 01:17:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e0fe353-4621-374d-822b-07b92e5d241c | -11.8103 | -57.007599 | 2026-07-02 01:17:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c7653ec-d2a7-3c89-a1a6-72f61779d9d3 | -11.4184 | -56.053501 | 2026-07-02 01:17:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b876a639-8700-3ba9-ad8c-a065bab62401 | -11.6116 | -60.412201 | 2026-07-02 01:17:00 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e510e96-14da-3144-a468-59a1aaa1c937 | -11.7989 | -57.002899 | 2026-07-02 01:17:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7024399a-4440-3495-86e1-68d55a13964f | -12.8396 | -44.341202 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95fc5973-c7f6-373a-8973-2246c5f1e649 | -12.7506 | -44.501999 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4f272f5-0b60-3489-b5dc-3f7d46366e64 | -9.0294 | -59.535099 | 2026-07-02 01:17:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a97e8c73-2b4a-3f60-99e1-4699ebc5c2b2 | -3.5125 | -48.049301 | 2026-07-02 01:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e04f2c0-3621-35b7-a8cc-b0e5ca81c8fe | -21.771601 | -56.299702 | 2026-07-02 01:17:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 48e5a32c-0d20-351a-bc2c-d375b2a37319 | -12.8484 | -44.372601 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43b04e9f-f584-33f0-ace4-b7258d142bb0 | -21.779699 | -56.2897 | 2026-07-02 01:17:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd392be-47f2-38df-a2f9-36ce76ce5d62 | -19.509899 | -52.733002 | 2026-07-02 01:17:00 | METOP-C | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| db5441ad-d82d-3114-aef7-6d05759b2a1c | -12.742 | -44.4711 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f66de42b-2129-3f08-81e5-b05652ffac87 | -20.493401 | -50.528999 | 2026-07-02 01:17:00 | METOP-C | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 939fb1a9-89dd-38f5-a878-6fa186c880ba | -10.8203 | -58.011799 | 2026-07-02 01:17:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87dd4eb0-9512-3f22-8886-8303af4ae460 | -12.5149 | -48.264198 | 2026-07-02 01:17:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcda6c79-8f5c-3571-8a7f-9472b8c69e81 | -19.508101 | -52.725101 | 2026-07-02 01:17:00 | METOP-C | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4b534756-f26f-3c83-b7a0-72e6ba954f2d | -3.5159 | -48.0215 | 2026-07-02 01:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61130332-5c6e-3340-adc2-eb6828247e27 | -9.6055 | -56.919701 | 2026-07-02 01:17:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f164ece0-1f03-3c2e-b959-d878ee530d2a | -9.2009 | -58.044399 | 2026-07-02 01:17:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d75d201-f4a4-31d2-8700-c12e5842c579 | -9.2153 | -45.327999 | 2026-07-02 01:17:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8b8ed1fc-e65c-32fc-82d3-fe56026f7ba2 | -12.761 | -44.465599 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3929f25-0fc2-3697-879c-8f238592e678 | -12.8674 | -44.3671 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dc53670b-1d99-373b-bc07-ea7321678d50 | -9.2058 | -45.330601 | 2026-07-02 01:17:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 44944163-fe3f-3017-978e-236f01f7af1e | -12.7792 | -44.493801 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c260031-e000-3197-9452-d20202d29600 | -20.4911 | -50.519299 | 2026-07-02 01:17:00 | METOP-C | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2cd6b99e-bd71-30e6-a868-e100af509293 | -4.0057 | -48.063202 | 2026-07-02 01:17:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0078460b-d253-3cef-86ca-2ed5449bccf9 | -12.7601 | -44.499298 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79fe9a1e-f0ac-3fdd-909c-36d03a3e9971 | -11.433 | -56.072399 | 2026-07-02 01:17:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c870caf-ad94-3c8b-84a4-a5bf9df70736 | -12.7515 | -44.468399 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00b661d9-7ef1-384a-aa2f-aaee20a22ef9 | -21.778099 | -56.281898 | 2026-07-02 01:17:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d2d3c19f-9e1b-3a47-99d8-bda2dd48ec30 | -11.8005 | -57.009899 | 2026-07-02 01:17:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69698a42-36a0-3b9d-b0f8-d6ea143a389b | -12.8579 | -44.3699 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
