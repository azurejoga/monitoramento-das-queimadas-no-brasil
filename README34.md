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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be771a4a-62d5-35ca-8102-19fd7429882e | -5.17071 | -45.4752 | 2025-10-09 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a490f2a5-ffd3-3361-8445-4f4526dc50e0 | -7.04838 | -37.69178 | 2025-10-09 04:17:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4e848780-6b38-3b50-8172-0a062829a1bd | -6.728 | -42.84013 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d5ee4fb0-f587-300e-b5dd-8170f8a4ebb9 | -6.68245 | -46.3059 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f356cf9-5a44-320e-b325-7e8ca5b4f39a | -7.52685 | -42.00275 | 2025-10-09 04:17:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c5a161b5-cd95-37d9-b7f3-109f90661086 | -5.12081 | -49.95229 | 2025-10-09 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89c50e2a-2b45-350d-840a-10e6275e6606 | -7.02188 | -42.86239 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b37c8dae-bd32-3290-aa35-228335e11280 | -5.4006 | -40.98225 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ba1d0cb1-dde0-3a2d-a4e6-2d68f285b450 | -4.46622 | -41.97012 | 2025-10-09 04:17:00 | NOAA-20 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3652678d-74c2-3286-9cd4-99634e09f108 | -5.41545 | -41.34361 | 2025-10-09 04:17:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e6b8ac20-8d5f-38c7-a714-76341c940a8f | -5.79169 | -44.66766 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b41f1c9c-a4aa-3c41-b7a8-22ad6fcd1aff | -5.25981 | -46.47599 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53cf9e4e-f1ad-3acf-ae08-64f03d61ce8c | -4.69054 | -45.84629 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51002532-a244-359d-ab55-8fe95599a88f | -7.50516 | -42.72492 | 2025-10-09 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| cd421cdf-0c63-3f4b-84b1-c7e1090a4225 | -6.69265 | -46.30753 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f3f41779-24d0-34f3-8e6b-22475f3a4e5e | -5.80659 | -44.68064 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b5655f6-cdab-3b99-b13c-137b025bf3bb | -6.72747 | -42.86639 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 32905b30-38f9-3615-b268-e96f702ed067 | -5.13358 | -37.55721 | 2025-10-09 04:17:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ffcd86d2-2e54-3b4e-a131-8f199e8574b9 | -3.38858 | -49.0433 | 2025-10-09 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd6e3925-25ea-3b52-8c72-6d6e7e2a742c | -5.2459 | -42.99577 | 2025-10-09 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c07f7de6-763c-3929-b9fa-19ef057eb861 | -5.48546 | -42.89717 | 2025-10-09 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0e27dae-8cde-3aed-8572-7376302e40b7 | -5.38969 | -40.98061 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d42e89c1-2b13-3a14-b41e-05ef42d4913f | -3.47179 | -50.02288 | 2025-10-09 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5192ed9b-fc23-3f9e-a1e9-bb655ecada70 | -6.65671 | -35.09809 | 2025-10-09 04:17:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e360cecd-7f2c-39e5-b5ca-28ee9a8a9a60 | -6.32697 | -43.74818 | 2025-10-09 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cc8facc-930f-3efe-a5cc-01553959e54c | -4.2191 | -48.36526 | 2025-10-09 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6abecded-cdb7-3778-9d54-5c0813eecce8 | -5.71511 | -42.7732 | 2025-10-09 04:17:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 2e4d48ab-a897-33f9-a5fd-0f9816deb2e7 | -6.68703 | -46.29912 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9c0df0b6-4d3a-3440-ac3f-3c47b4ed24be | -5.39633 | -40.98588 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 699b45d8-3fe5-314c-92ba-df7654a66e5c | -6.48878 | -46.11436 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9bbf911-7061-37ac-aaf1-4906a24ddfe7 | -5.80713 | -44.67719 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34495997-839b-336e-87d9-e11e7e94be69 | -3.83659 | -49.26514 | 2025-10-09 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f391205f-8860-3127-9cde-46e956c8d6c8 | -5.48321 | -42.88948 | 2025-10-09 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17a33e97-84b5-3545-9fcd-3f5df0ee0dc2 | -4.68715 | -45.84573 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68740356-5a99-3af8-8f96-b3d7f8bf5d84 | -5.13629 | -46.2594 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7129ada-b4d3-3c5a-af4b-580d3450d4a6 | -5.14015 | -44.96202 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 076b74a4-0ffe-3506-9fef-bcb91ed771eb | -7.50632 | -42.74046 | 2025-10-09 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d4458be1-b9f0-3015-a725-95f84f8a3cf5 | -5.61142 | -41.16864 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0926b8c5-0045-3264-b63b-6d743637180e | -5.52817 | -45.32145 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 155117c8-1abb-3cad-9d59-9201855bfa1a | -6.68925 | -46.30698 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 386ca8ba-e3b0-3741-b435-50cd91f7aa70 | -5.7994 | -44.6618 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cc25ace-8981-3bca-b3d4-3953980124c3 | -4.03432 | -49.49974 | 2025-10-09 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60bfea02-8cf1-3a67-b5a3-d71f240c4b25 | -5.23653 | -45.80851 | 2025-10-09 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56d12e6c-cf70-35c4-aa09-d0596f9adbb7 | 0.90655 | -51.13011 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 519011b9-6cfc-30b5-8e47-32369d559876 | -4.45308 | -43.22371 | 2025-10-09 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d623fed5-2dde-346e-9c41-629c76619c33 | 0.90152 | -51.13095 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a131360d-29bc-3d2e-ab3f-bc40e304770d | -6.72635 | -42.87369 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c165a5a9-631a-31c3-a86f-6ef2a1b11d68 | -2.18783 | -54.48021 | 2025-10-09 04:17:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d01d4df7-0106-34ec-bad3-108412fe7e99 | -5.25274 | -43.14933 | 2025-10-09 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38a91227-ea75-3ba0-b43f-1fc3f02d1f9a | -5.30243 | -43.08837 | 2025-10-09 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3908428f-e495-378f-8b37-969c8ebab24a | -4.30297 | -48.06987 | 2025-10-09 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a6a5dc2-d6aa-3951-a24c-94113dedb6a1 | -7.51718 | -42.71523 | 2025-10-09 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3cd44def-05ab-306c-a861-03afc643a9e1 | -4.69112 | -45.84262 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 652d2dce-f568-3e12-8b08-4c96ad7efa7f | -3.10616 | -47.79969 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06eef24e-2ed5-3a9d-8f47-1962ad12d650 | -5.64482 | -50.31696 | 2025-10-09 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf2905c1-5b6b-3a17-aee8-e4428135cb3b | -5.13683 | -44.9615 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ba811c4-4edb-3fa5-b43c-c634757d1861 | -7.48389 | -43.11611 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a84d6bbe-b74a-3208-bd35-b936e5318749 | -5.73919 | -44.33402 | 2025-10-09 04:17:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da3674c2-14b7-3bbf-9b75-7635ad449187 | -4.87355 | -42.23707 | 2025-10-09 04:17:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 753220ae-4c04-33bd-b6c0-0648bbc39e44 | -4.36311 | -45.57146 | 2025-10-09 04:17:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a6964db-7523-3f62-816c-ac48df4812d6 | 0.89368 | -51.14721 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d80bab34-7491-3c1c-b7ea-a25fdcd75fed | -7.52862 | -42.98389 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 41df8ce1-8042-3a13-ae53-ddf4b84a8858 | 0.89737 | -51.13757 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7d52409-712e-3620-9f74-57de3686cefc | -5.15577 | -46.09497 | 2025-10-09 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 621ace97-3443-3b46-b549-a12c5be2e7a6 | -3.44287 | -45.59943 | 2025-10-09 04:17:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70374224-5f15-3d32-b610-ac4807994fe0 | -3.8947 | -44.90853 | 2025-10-09 04:17:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2467e13-feb2-35aa-a058-c5d54d69897f | -4.6889 | -45.83471 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bcb8c2c-eae5-3cfa-bdaf-4326dde72ed0 | -6.58623 | -47.0372 | 2025-10-09 04:17:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5af3be9-c873-33bf-9817-fc3e495b7de2 | -4.21525 | -48.36462 | 2025-10-09 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3f5b3c5-e608-3558-9a94-8ece9a498c5b | -5.67073 | -43.94776 | 2025-10-09 04:17:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb2d2460-2670-3356-9084-2ad2f3653a5a | -5.48798 | -45.40171 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e785fcc-dd16-381e-95b9-2adcc1228c14 | -5.87444 | -49.22346 | 2025-10-09 04:17:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 001bcd00-c3ea-3cb2-b9eb-d71f1a65bbc9 | -4.7464 | -44.93919 | 2025-10-09 04:17:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 275e65e3-8a3e-3978-b77f-7e7ee3a78099 | -3.11081 | -47.79332 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb04b364-1f0c-3c4e-8630-8af0a3df5880 | -7.42302 | -42.98663 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c5b5d73-4df0-38c8-814c-303478750674 | -5.13487 | -37.55975 | 2025-10-09 04:17:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2cd9d08f-d925-3c63-951e-8ea25ecddc83 | -3.38475 | -50.14273 | 2025-10-09 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 633f6031-65bb-3332-a0be-b3e0f80c3359 | 0.88964 | -51.1487 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ce9a0ad-05e1-3c3e-b795-9baed45cabe1 | -5.40123 | -40.97808 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 35c26bef-7b32-3a16-a4c3-056a2acc828e | -4.37126 | -46.75641 | 2025-10-09 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 384ab47a-b54b-3746-9627-6a025f2e7e90 | -5.49911 | -36.85524 | 2025-10-09 04:17:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 25c4de45-3825-35eb-8ddb-56abeef771e2 | -7.41735 | -42.9782 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b71971ef-6c19-3249-b7fd-00ae1dc54e1d | -7.01449 | -42.86502 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e2818684-08fb-3a35-a69b-3569695a0c7e | -5.58584 | -43.96992 | 2025-10-09 04:17:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92a1f896-f821-3030-acc5-852b401def9f | -3.58907 | -49.35167 | 2025-10-09 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 54592952-77b6-34b0-9418-2081d6b429e5 | -5.44399 | -44.82508 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f9b29e1-934f-375c-abe3-6abd405c99c0 | -6.72551 | -44.79805 | 2025-10-09 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbac0eb0-8d70-3af8-868d-05dca531b9d4 | -7.50289 | -42.73992 | 2025-10-09 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40f20e93-a5db-3f20-89fc-5ca5bcd308d5 | -5.44731 | -44.8256 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e339fa6e-bc95-39c1-89cc-d6b3422fdd29 | -3.38844 | -50.14761 | 2025-10-09 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d329c020-1b74-3226-a71d-24671998aecc | -7.02198 | -42.74878 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6e3640c7-49ca-3d7e-ab54-11085ae4a2fb | -5.15176 | -46.09815 | 2025-10-09 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6945f3c-a58b-3f88-adf9-62701f6f4085 | -7.02651 | -42.78738 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2529c710-267e-34bf-8398-430cfccfe859 | -5.28777 | -45.75738 | 2025-10-09 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d2ff39f-ea7e-3bce-b923-08309cae867b | -3.38417 | -50.17319 | 2025-10-09 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4692ff9-1032-3595-9cb6-41292783aa65 | 0.33662 | -50.95436 | 2025-10-09 04:17:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| da5f3819-254a-336f-92d8-52ddfaeac96c | -7.48841 | -43.10933 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 95cbf1a8-06e7-322e-89d6-6d812cd912f5 | -4.61066 | -43.14741 | 2025-10-09 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaa6df52-2f3e-3cd7-ac2d-33a0a91d6059 | -6.69323 | -46.30387 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| e90fde46-5a02-3314-a9c7-fc476483afa8 | -5.40655 | -45.90981 | 2025-10-09 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README35.md)
