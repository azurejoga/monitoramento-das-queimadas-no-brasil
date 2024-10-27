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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db30d5c1-0986-3632-91e1-1adb5dd8f95a | 1.01059 | -52.21991 | 2024-10-27 04:21:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40992b29-6964-3e04-b219-d1c17fd18f62 | 0.93724 | -52.0019 | 2024-10-27 04:21:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1575d4cd-a312-371f-b167-979e5ebf25a6 | 0.41948 | -51.49217 | 2024-10-27 04:21:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e98b79bb-c466-3669-b8b6-076aca2804f4 | -0.11724 | -51.63241 | 2024-10-27 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 78788647-899a-3262-a7b2-0a1e0625e956 | -0.11344 | -51.6271 | 2024-10-27 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59bc02fe-0007-3b82-b003-d851853cd189 | -0.10964 | -51.62178 | 2024-10-27 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 505e6286-3b30-35f3-bd11-90911c431c5d | -0.10891 | -51.62631 | 2024-10-27 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8501a99-0292-3302-b6a5-b6c7d07e7658 | -0.10512 | -51.62099 | 2024-10-27 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bde58975-24d6-3bb0-ad73-1ccca89c3fe6 | -3.94356 | -40.97042 | 2024-10-27 04:23:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d8bbc823-7fee-36c7-acc6-db45e71207a6 | -4.50546 | -42.95476 | 2024-10-27 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 249d75aa-d553-3c72-b5a4-67b89f3c4f44 | -5.93763 | -38.1316 | 2024-10-27 04:23:00 | NOAA-20 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3001ecc0-d999-3300-be3e-5483913601bb | -5.69004 | -38.04244 | 2024-10-27 04:23:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 155c7b41-6a20-3e8f-9766-fe26fb08780a | -7.56232 | -38.75425 | 2024-10-27 04:23:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8e97989b-ddb5-3104-9f3c-e84f718948fe | -7.55748 | -38.75336 | 2024-10-27 04:23:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4b829879-8f22-35c6-97d4-3b38981cd8a3 | -7.55263 | -38.75257 | 2024-10-27 04:23:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| babe6821-7c9a-3800-a3e5-4d1d882ada6e | -7.29208 | -38.93875 | 2024-10-27 04:23:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 63106b48-3ee4-3442-adbd-2a13ef6437ee | -7.88515 | -39.16976 | 2024-10-27 04:23:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4132b288-1205-3288-828e-7a140ee3aa11 | -7.88446 | -39.17481 | 2024-10-27 04:23:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7bf50c7e-d6dc-308b-82d5-ff35bc9310f5 | -6.40432 | -39.69428 | 2024-10-27 04:23:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f58b16b5-19a7-3691-95f1-4093725469c7 | -6.0448 | -39.82559 | 2024-10-27 04:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0ea503ca-1f53-31f9-8efb-ff653c6c8acc | -6.04474 | -39.82443 | 2024-10-27 04:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c2c1aa00-374d-338f-b927-40c740bccfed | -6.04414 | -39.8287 | 2024-10-27 04:23:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 240943f5-edab-31f2-bac0-c37a5363f91e | -6.04102 | -39.8207 | 2024-10-27 04:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 63147763-69d0-3ba6-a6d9-c40b6ad1e4e6 | -6.04094 | -39.81951 | 2024-10-27 04:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 71.2 |
| de558987-347a-318d-8699-f9a1c87ac118 | -6.04039 | -39.82491 | 2024-10-27 04:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 1af0dfbf-fc88-39f1-b963-29131466c87f | -6.04033 | -39.82379 | 2024-10-27 04:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 71.2 |
| c16c9c8b-bfd3-3888-97ac-e3e005a471b0 | -6.03978 | -39.82905 | 2024-10-27 04:23:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 39.0 |
| da2e17e8-7e8c-3d6f-8bef-a518b363b4f7 | -6.03974 | -39.82794 | 2024-10-27 04:23:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 71.4 |
| cb6f2c53-c790-356a-b1c5-c20ce03f275d | -6.0366 | -39.8201 | 2024-10-27 04:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 38855805-8316-39eb-9c1b-86bc404076fd | -6.03651 | -39.8189 | 2024-10-27 04:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 04af9043-7d74-39cf-b06c-cb1f4c948ef3 | -6.03598 | -39.82427 | 2024-10-27 04:23:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 7f20b0b9-2024-3a76-b626-5939e8929214 | -6.03591 | -39.82316 | 2024-10-27 04:23:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 14ca6d63-c2d3-3f4b-8c5f-185ae2116e9e | -6.03538 | -39.82835 | 2024-10-27 04:23:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 39.0 |
| abc120e9-6ed3-3bc9-b09f-c5f7c1534989 | -6.03534 | -39.82725 | 2024-10-27 04:23:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 71.4 |
| fd9d8c34-e5a3-306c-899d-0163095c8814 | -6.03157 | -39.8236 | 2024-10-27 04:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2b451f84-c27c-31f8-bf16-50fae72a6f62 | -6.02716 | -39.82294 | 2024-10-27 04:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 817feffa-e584-3e34-83a9-1369b1e6c0aa | -5.87364 | -39.21225 | 2024-10-27 04:23:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1936358f-e532-300e-a34c-842b17ee19f8 | -5.86906 | -39.21152 | 2024-10-27 04:23:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69642e32-c8bd-38f6-b2f0-9d237e8b3181 | -6.96368 | -39.24991 | 2024-10-27 04:23:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3eb25a32-4755-358b-8bc1-27d699a241df | -6.72839 | -40.50826 | 2024-10-27 04:23:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1609c93-ad9b-3a48-8c6d-428addfb1779 | -8.16171 | -40.50286 | 2024-10-27 04:23:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 301dc479-a5e0-3dc2-ae6e-a958649c7807 | -4.29381 | -40.60023 | 2024-10-27 04:23:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1226de5-a045-381d-b91d-e1848b253e31 | -4.18555 | -40.68502 | 2024-10-27 04:23:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eef345cf-a6fa-34e0-b9fd-8e76249816d3 | -4.18499 | -40.68884 | 2024-10-27 04:23:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f26d00e6-f21e-36cf-90fd-575fb40c4dfe | -6.2928 | -41.91114 | 2024-10-27 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35fb1c02-d71e-3248-8917-d4c3f64b543e | -6.28895 | -41.91051 | 2024-10-27 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ac75ddb2-3f6e-3d21-b45b-b4568ecd6c75 | -6.5509 | -40.51313 | 2024-10-27 04:23:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 63887c9f-2b6b-3c93-acac-a97e0eded17a | -6.54668 | -40.51238 | 2024-10-27 04:23:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| f8fbd5c7-4d90-39d3-91b2-72990cf51529 | -5.72962 | -41.73017 | 2024-10-27 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 750ebc61-0b2e-3c2e-b4f2-b3992b463b86 | -5.69537 | -41.64044 | 2024-10-27 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b0d3cb50-b173-3563-a96f-f1888510316e | -5.69465 | -41.64536 | 2024-10-27 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6ec70bd6-18d6-3fd3-bf48-15aff3b7533b | -5.69393 | -41.65023 | 2024-10-27 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e349e57d-6839-3459-8004-2dc0c26e4d0a | -5.69076 | -41.64477 | 2024-10-27 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 53d94910-8897-3379-af43-0ddd149fbee0 | -5.69004 | -41.64964 | 2024-10-27 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e6e2b17b-5311-3fcb-9500-f754341d255d | -5.68687 | -41.6442 | 2024-10-27 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5df3897a-43c7-3bd8-8a10-e6eb31bdd16e | -5.65913 | -41.83265 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 12eea8e7-ba07-3cdf-ab74-016b13515b24 | -5.65075 | -41.83622 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 295a02af-4f12-3bb8-a217-4e300c2b2e93 | -5.60891 | -41.73473 | 2024-10-27 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 332519a6-70d2-36ef-9b0e-531bf34b024b | -5.59904 | -41.74791 | 2024-10-27 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c7123c0d-9996-364a-92fa-672440ca0cbe | -5.59589 | -41.74253 | 2024-10-27 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6b16877b-e4ed-30d7-a3de-4503e7770bce | -5.48778 | -40.78897 | 2024-10-27 04:23:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4045a256-8523-3950-885e-e60bbde57f8e | -7.26045 | -41.22575 | 2024-10-27 04:23:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 342eb51d-bd50-3b4a-9358-56eecd7e1766 | -7.25584 | -41.22881 | 2024-10-27 04:23:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1065a88d-8378-3a9a-a7bd-ef1a6a9641e2 | -7.25177 | -41.22809 | 2024-10-27 04:23:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ac3ac196-60ec-3928-aaf8-3bde3794204a | -7.25124 | -41.23177 | 2024-10-27 04:23:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5b3ab010-ec19-35a0-b1dc-619423915fcb | -7.24823 | -41.22363 | 2024-10-27 04:23:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 43f8c8e4-cfb9-3061-a7b8-e02a0330a424 | -7.2477 | -41.22734 | 2024-10-27 04:23:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7a523fc7-e4c8-31ab-99a9-6af650f7c31b | -7.00243 | -41.31447 | 2024-10-27 04:23:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 95508241-b979-354b-9605-2ed2e7fdb2e9 | -6.99838 | -41.31393 | 2024-10-27 04:23:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dd2e858d-a880-31c7-9140-f6590906d6b9 | -6.99785 | -41.31749 | 2024-10-27 04:23:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1072d0e0-5ea7-3838-bd3c-62c2d0474c87 | -6.96043 | -41.31897 | 2024-10-27 04:23:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3720e47a-4dee-39c6-a876-451e2dff53f8 | -6.95639 | -41.31839 | 2024-10-27 04:23:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 401452c6-67ec-32f2-acd2-1f330512fbc1 | -6.95374 | -41.33648 | 2024-10-27 04:23:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a185e714-e341-330b-95e0-fba679280840 | -6.95322 | -41.34008 | 2024-10-27 04:23:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3912a9c6-98bd-399b-addb-3787c5bcdf59 | -6.95182 | -41.32136 | 2024-10-27 04:23:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd754c54-4bdd-3ade-8fde-ceafaaf8fdfe | -6.95023 | -41.33226 | 2024-10-27 04:23:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2504e67b-8695-38eb-9533-1fbde06df34d | -6.9497 | -41.33594 | 2024-10-27 04:23:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bac35c2f-9e04-3cc3-9a49-7285c94adaad | -6.68986 | -40.89401 | 2024-10-27 04:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43ad8e42-878d-3605-8304-540fa4722d0e | -6.68157 | -40.89286 | 2024-10-27 04:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd03ca85-b8fb-3b58-bef9-88ff81e8919a | -6.68102 | -40.89667 | 2024-10-27 04:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0a211e78-42cf-3fcb-8583-ec6afe118ae9 | -6.68047 | -40.90048 | 2024-10-27 04:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9e63c103-ee9f-3462-aabe-2f490e907507 | -6.67992 | -40.90427 | 2024-10-27 04:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 33928aa3-2810-311f-9843-34586062430a | -6.67937 | -40.90804 | 2024-10-27 04:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2f7de2d6-b669-3578-9aad-ca659198b546 | -6.67632 | -40.8999 | 2024-10-27 04:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9b06beb8-e02b-3377-bedf-7ac1c4e8763d | -6.67577 | -40.90369 | 2024-10-27 04:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 25687a1a-cca4-3e64-b8f5-9498e50410d2 | -6.67523 | -40.90746 | 2024-10-27 04:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 20767f58-f47b-3277-a322-badc61be1e4f | -2.7932 | -42.47205 | 2024-10-27 04:23:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bdb46921-77d4-33de-aaf1-e87be442bd17 | -2.78962 | -42.47149 | 2024-10-27 04:23:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e83dbc7-7ac1-3cb6-bd6d-b247b16d00d5 | -4.92303 | -41.97356 | 2024-10-27 04:23:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5304625f-f6c8-3b24-b835-8ef290316f03 | -4.85179 | -42.4669 | 2024-10-27 04:23:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0fcbf05b-d9d0-34f4-b66f-8baade4b7d6a | -4.42077 | -42.52158 | 2024-10-27 04:23:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f9e7b5e1-b747-34ed-93ca-b528508a549f | -4.42012 | -42.5258 | 2024-10-27 04:23:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4effd433-27dc-3b2b-aed7-b96873cc5944 | -4.41648 | -42.52524 | 2024-10-27 04:23:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 78867ed3-03a0-331e-b629-9ea1b462df8e | -4.41583 | -42.52946 | 2024-10-27 04:23:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a603827-6991-346b-bbad-c13769d05a0d | -4.94683 | -42.90407 | 2024-10-27 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2839a3e3-bc53-30a9-8040-30f7fa13a90a | -4.94621 | -42.9082 | 2024-10-27 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 59171242-28fb-3c1d-8221-b87bdb461ef0 | -4.94559 | -42.91233 | 2024-10-27 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 77c7a910-cf97-3ac8-9239-3e660de1f6d9 | -4.94324 | -42.90354 | 2024-10-27 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8f25a17-fd1e-311e-a105-94682c8b1f46 | -4.94262 | -42.90768 | 2024-10-27 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 12d50b21-2c7e-308c-9c9c-53b62a647f72 | -4.942 | -42.91182 | 2024-10-27 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |


[Clique aqui para ver as próximas entradas](README40.md)
