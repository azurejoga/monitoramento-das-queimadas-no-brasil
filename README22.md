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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04ec99fb-0de5-30b3-aa6b-42e00e185ffb | -2.63509 | -54.57895 | 2025-11-04 04:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3eb55690-e82f-3d6d-b8b8-44ac2f2026f2 | -2.83554 | -49.40848 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e643de1-1180-33ae-8f10-c179c8f6787d | -5.32398 | -48.18023 | 2025-11-04 04:31:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1086372f-c789-3847-8782-d138b6855187 | -4.41327 | -49.78336 | 2025-11-04 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 565cbfae-3520-3dff-aaf8-29b1b3d0f63e | -2.31144 | -48.59989 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eabb032d-31ff-3409-bacf-b89c2b6b5c7d | -3.0062 | -49.47726 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a391600b-ef05-34ca-8d2f-f5f548fac217 | -2.31432 | -48.58168 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e8eac6d-a2f7-344e-aab0-235227a4ae17 | -5.35515 | -46.71175 | 2025-11-04 04:31:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9bbbd8f9-b126-3c15-9fed-002682e73998 | -3.49891 | -45.63459 | 2025-11-04 04:31:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 768dca78-28a2-34ed-9abb-5ec999fc643b | -7.42899 | -40.72086 | 2025-11-04 04:31:00 | NOAA-20 | MARCOLÂNDIA | PIAUÍ | Brasil | 2205953 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac1b7019-b9a6-3f22-bd1a-c69095f82717 | -3.9136 | -47.68727 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c835704c-fb65-312c-837d-cef8edd45782 | -2.32617 | -48.59475 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 944db6d0-c1b8-37d4-9ff1-898e5656acf7 | -4.02984 | -45.46592 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 306b0db3-e6b2-3b57-809a-420bacaa6fd3 | -4.0222 | -51.0148 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9f6cacd-fe75-3e50-bf6e-86c139ff8367 | -5.08355 | -46.07914 | 2025-11-04 04:31:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5595aa5-76de-3573-8cd8-8c88bab4a2b0 | -3.49815 | -50.47184 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eeeaa39-facb-361f-88c8-13a8399be5fe | -3.04152 | -50.28102 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74952d11-4963-36a3-b8bc-358b7bcba46d | -4.59627 | -45.58598 | 2025-11-04 04:31:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 597af636-8818-3161-b34b-bc7dd0cae7b6 | -5.19088 | -45.27341 | 2025-11-04 04:31:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52b064eb-218e-3dff-b565-bb600989a890 | -6.4144 | -43.07143 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 95c098c5-13cd-3082-a0fa-1a8ac2f48cf5 | -4.02308 | -45.46151 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d43d300-16a1-3118-a15b-d5acf0438108 | -2.72102 | -48.34573 | 2025-11-04 04:31:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1ab808e7-ac87-3b26-b30a-6bf68a883f8e | -3.36202 | -45.54043 | 2025-11-04 04:31:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e364f135-5ec9-3d21-9d75-e19a4a896f62 | -4.93502 | -43.41955 | 2025-11-04 04:31:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a5c99d3-e5a1-36e3-93c9-edd1ba46298f | -3.01068 | -51.39704 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17ddb855-6796-3d37-9a1e-8865df7cd00e | -7.55367 | -45.84707 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a23106a-c3a5-39e7-a556-23fd6db0433a | -6.39867 | -47.55032 | 2025-11-04 04:31:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c75cabc6-3c1a-3c43-9205-c783fa9907e5 | -5.42943 | -44.6631 | 2025-11-04 04:31:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99c1b249-9f1c-30bf-bcc9-4cf12fd7f10f | -3.34334 | -44.85655 | 2025-11-04 04:31:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90eb38df-ba69-3c8f-a5b6-82fad6c7b6f5 | -5.23051 | -44.20726 | 2025-11-04 04:31:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 176fe63f-5ea2-34a0-9fa5-71d58f32ee43 | -6.43095 | -43.06883 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05aab4ae-5d01-3283-87a2-e50ea2ffb275 | -2.73898 | -47.14195 | 2025-11-04 04:31:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce3cc9d5-c235-3fb9-8c32-11bd5494a469 | -4.8704 | -47.54539 | 2025-11-04 04:31:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03875586-4034-3309-b4a1-9f5516de20c7 | -4.9509 | -44.90333 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19ccc19b-33e8-33d3-99d6-f18e4b83540a | -4.61817 | -46.40663 | 2025-11-04 04:31:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c45fec52-f3e5-353e-805d-daf82b9d9017 | -6.24523 | -42.08621 | 2025-11-04 04:31:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7798a56b-f25c-3890-95bf-3b85efd4264f | -4.47594 | -43.23374 | 2025-11-04 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48b61c73-eb32-34d6-81dc-b3ec376ec9f2 | -7.52994 | -47.29046 | 2025-11-04 04:31:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e9c8c0f-2d77-3a1f-8065-369973a03cab | -3.99801 | -47.73235 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7a25781-3d04-375c-8989-d4d4156038f3 | -3.91802 | -47.70212 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 92fecf07-1cbf-3ec1-a1cf-40e44413d65a | -6.09977 | -44.44012 | 2025-11-04 04:31:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 386ebb6c-e205-3431-a3de-cba9a59782f3 | -3.4959 | -50.46267 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e78f2c62-1b43-328f-bc5c-5d6b6d8f9c1b | -4.29466 | -46.25988 | 2025-11-04 04:31:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86eb0599-6189-3035-b6ad-e78e947165ff | -4.96684 | -44.34628 | 2025-11-04 04:31:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33759fd5-89cc-32b7-b863-06db372b8c48 | -2.81909 | -48.2482 | 2025-11-04 04:31:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 343bb298-6f91-35c3-b4a0-55b2371c7024 | -6.41911 | -43.06695 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fd3903ba-fa78-3fa4-b376-b74a68013afb | -5.83978 | -43.45088 | 2025-11-04 04:31:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75139355-a77b-3839-b71a-22fee29b576a | -5.58213 | -43.7934 | 2025-11-04 04:31:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c171725-7e28-342d-9915-e22d4545062a | -6.1327 | -41.54497 | 2025-11-04 04:31:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e9b028c-bbc3-3740-ac8d-12820c82b7f6 | -5.062 | -45.90614 | 2025-11-04 04:31:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 80f3d24e-daef-36aa-991b-16b93179baaa | -2.89869 | -51.46655 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e668814-ae7a-3895-abd7-2a299753d65a | -2.90724 | -51.46297 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0ae62f5-9069-38be-a783-6b03cf3d13e3 | -3.3462 | -44.86087 | 2025-11-04 04:31:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d573bbc-4749-32ac-8eea-10ca211c80f5 | -2.31541 | -48.59678 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ce86daa-d820-307b-9755-446347bca2a3 | -3.14911 | -49.6231 | 2025-11-04 04:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 13d31e85-657f-3f5c-b7d7-affa0351bcc3 | -3.43552 | -42.54197 | 2025-11-04 04:31:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8494b3aa-8b74-303a-8927-74ea83b536f9 | -6.61035 | -43.6186 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc87deeb-749b-31b1-bec2-fa5bad072bab | -3.45567 | -50.22234 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a81ec1c-cc52-3780-9fa3-c1db111923cc | -9.24322 | -47.54076 | 2025-11-04 04:31:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11a95b28-5fc5-3e47-9b14-e3f739f2cefc | -7.61533 | -46.47595 | 2025-11-04 04:31:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 638f45ee-c730-36a7-8657-3e2477ea1c8c | -7.61871 | -46.47647 | 2025-11-04 04:31:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d45c889e-7187-3652-88e6-0c72ebfd41da | -3.49521 | -50.46695 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9f6a764-9f17-3aa8-9e2a-f32a8b64c943 | -6.41196 | -43.0607 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f04a36ce-765a-3bab-b407-b9106bee8856 | -3.91857 | -47.69867 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cbf0b764-5026-3a45-b269-24c0d073bf9e | -3.50178 | -50.47246 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 702b42ec-9bc3-3750-99af-29dba072848b | -5.53789 | -44.51957 | 2025-11-04 04:31:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad4fad14-82a1-3817-8f07-1d468e1da289 | -3.5223 | -55.43131 | 2025-11-04 04:31:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5146bd97-8fd9-318d-9f4b-f281140240b8 | -2.83021 | -49.41952 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f43098d5-d837-3897-af93-556e3f6ff111 | -3.5367 | -49.44828 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d03d7a0-8955-3a97-8381-9a309ef9719e | -6.35923 | -46.14789 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 334eaf52-eb9c-3d46-8a2a-6d9daf323a62 | -3.27873 | -50.76732 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d61bda12-a1a5-3e67-900b-fb649da87add | -3.85062 | -51.40522 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea433c09-bbc9-376f-9ef0-ffac5dfc3bfa | -5.85697 | -43.99712 | 2025-11-04 04:31:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62f7fd97-dcad-3aa5-9dfc-4216c3ccd233 | -3.45207 | -50.22176 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c76f33a-9ed7-39a8-a5ea-8a779ae4426d | -3.46503 | -50.32587 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7a55279-fc64-36a5-a3e4-dd59bc2448c0 | -3.75227 | -49.17718 | 2025-11-04 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96d6fbac-c284-3a91-8692-7e284004a0f0 | -4.87339 | -49.007 | 2025-11-04 04:31:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 434504e2-f653-34dc-aae9-9bff8499467e | -6.16491 | -47.2444 | 2025-11-04 04:31:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6427419-5eec-3075-8b38-72843398da8a | -4.87094 | -47.54195 | 2025-11-04 04:31:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0c6de49-af2e-342b-b327-d6faa8464477 | -2.88047 | -52.61374 | 2025-11-04 04:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b854afca-179d-3a05-9cd8-b5ba9468298d | -3.57211 | -50.64023 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 98dcb652-f8b5-36de-a600-6247603a4f39 | -4.1081 | -45.5005 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23dae1e0-5ad2-3a14-a2c6-2480c34753d0 | -4.34919 | -50.79304 | 2025-11-04 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b281f006-bd05-3f36-aea7-d5d7f24f3603 | -5.5805 | -46.48713 | 2025-11-04 04:31:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9835b2a8-990f-3544-9726-c4f1d3375c6d | -6.84817 | -46.29703 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38e6eb59-a616-3f51-91e9-20204b0b6081 | -3.72887 | -50.05531 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea08d854-3c5e-3056-ad65-4e0042fce439 | -4.96324 | -44.34573 | 2025-11-04 04:31:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18436672-8378-3207-b586-7a1d948c6752 | -5.75978 | -45.89998 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 946d2243-7c49-3103-bb47-16d934c46a11 | -2.94296 | -51.41398 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58767dea-5f3f-3aee-8d22-4a53e82d65fa | -6.24101 | -42.08567 | 2025-11-04 04:31:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d90b9f68-3bab-30fe-be32-7a3542ec8dc1 | -3.82432 | -52.39081 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35456523-ef01-373d-acda-5638cbafb883 | -6.10358 | -41.70382 | 2025-11-04 04:31:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74eb7d6a-e92c-34bf-8817-6425d7b38ec8 | -4.02989 | -45.46255 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ec82a379-e491-36a9-b1dc-edefd5dcf3b8 | -9.04365 | -47.00637 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca66d358-de6f-3a85-89a1-2111b107657f | -4.8897 | -45.86185 | 2025-11-04 04:31:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2ebaaf6-54ec-39bc-8168-57b802465372 | -3.01919 | -51.39344 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e1e0caf-ec11-3126-b624-0d5e160b11d9 | -7.54997 | -45.85455 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52485e37-00fd-3f56-98de-b354e369149d | -3.91966 | -47.69176 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 318d52e2-e8f9-3f20-9d31-695e61d86648 | -2.98308 | -48.70367 | 2025-11-04 04:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fce39b03-da25-3c21-b55f-75242524780d | -2.37087 | -47.72816 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
