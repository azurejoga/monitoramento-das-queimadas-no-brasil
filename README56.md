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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f94b6d36-ee1b-368d-81bf-10bb5b40ad6e | -16.58844 | -43.51655 | 2025-10-30 04:27:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 852ef5a9-f8d4-3251-9ae5-e913501ceb25 | -13.95422 | -48.46071 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1954bb5-7b21-3ab1-88a9-16414b47c5a3 | -19.63408 | -47.66612 | 2025-10-30 04:27:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9da16edf-a16a-36c4-8d2d-605b58e26b35 | -12.23755 | -46.48223 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 317fe2fc-9c78-3051-b6a3-03a5a58a31eb | -14.78329 | -44.98634 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5190cc45-000b-3f27-adce-8798bc8687c5 | -13.32971 | -47.68644 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49be39dd-56bf-3b14-8d10-3f14571c4f4c | -12.01055 | -49.83525 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16dffb59-1660-3f99-bed9-1e60c3dfabae | -15.05018 | -43.47084 | 2025-10-30 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9cd27996-5ef9-3b52-a116-f563b80e69b6 | -12.29517 | -50.32665 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1529da34-54d0-342c-a402-18dac4c2912f | -13.3319 | -47.69405 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f698425b-70d1-3845-bf50-048bec37bba6 | -12.26821 | -46.76459 | 2025-10-30 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f158b8d-1ed0-39c5-b473-098922507729 | -11.65357 | -49.80429 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f37181b-57e6-3d47-af22-5e2373cec3d9 | -15.02715 | -46.30864 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 581aebb7-443d-3a3c-9c06-dd18bd6538d1 | -17.95327 | -43.00242 | 2025-10-30 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de4fee5a-0855-344d-bfad-e7e02ef76f5c | -12.68665 | -46.29776 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d45d3d9-3e91-317d-9534-e36527da6991 | -13.29886 | -47.68859 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d957397f-7e3e-3347-9af9-0e4fd5f28ee8 | -12.85438 | -48.62179 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ce6f868-ed47-3421-aec7-514fba43c3b5 | -13.65295 | -48.43281 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a160298a-58df-3043-8025-79cf0741764d | -19.88875 | -42.63675 | 2025-10-30 04:27:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2eecaab9-904f-356c-82ef-ab240f80e46a | -16.37851 | -45.25569 | 2025-10-30 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 742b3df6-9923-3323-9cd8-8eef2072c98d | -13.68841 | -47.69402 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 15404a85-5805-3b5b-8d3a-f580b9edb759 | -14.33323 | -46.52689 | 2025-10-30 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff5e21e5-a799-3141-883e-57b7af93b103 | -13.67814 | -47.17243 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73f7e000-8304-36e6-be33-dec7ae1accaa | -13.32662 | -47.44691 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd27365d-ec13-34fe-b2de-cf7ba2358ad1 | -13.16897 | -48.46186 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5368ef49-2b59-3c0f-aae4-48ddd4432ba2 | -12.85098 | -43.76723 | 2025-10-30 04:27:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23381aa2-affc-3789-9e26-59f3bc2e9efb | -13.51757 | -47.33262 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b90d2301-5e90-305f-b127-e47faca2e15c | -12.68899 | -46.32739 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 36dc8fc2-fb96-309c-aeaf-36096713d3fc | -12.47934 | -50.56702 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 27241b8c-7e31-38b1-b620-df126e3a11cd | -12.47417 | -46.88133 | 2025-10-30 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da7afb94-aae9-3049-b9d7-bee996e988af | -13.5137 | -47.33562 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5d28dc8-6ea1-3fd1-b50d-af43d0fa7500 | -13.95488 | -48.43528 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b6c28a83-14ed-3020-8fbb-b60f8279072b | -12.28674 | -50.31388 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc15608c-f9fe-3531-a6c4-42c799c9fd3d | -13.67959 | -47.68535 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a419cecc-afd4-38af-be73-e97be8ed1c82 | -12.51677 | -46.78254 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 853e7bbb-5d52-308f-9fcd-d9736c2ce1ae | -14.28414 | -42.33523 | 2025-10-30 04:27:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a5b8bc31-b2e0-376b-8b13-bcb201da1e6e | -13.1635 | -48.4535 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03c97f82-5a43-35bb-98ae-f67f6a18ea5f | -11.96412 | -49.70746 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2268c28c-6b70-32d9-bb29-c95d6af3dca4 | -12.8339 | -43.45399 | 2025-10-30 04:27:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 307e4b6e-12d4-3004-9286-62326c3b2d42 | -13.98467 | -44.02253 | 2025-10-30 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97c0162c-e9b7-33f5-8ec3-922b0f714578 | -13.35991 | -43.09212 | 2025-10-30 04:27:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| bf2c41f6-305f-346c-bae2-f4a171bb4dcd | -12.31146 | -48.06523 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46181553-4d42-3932-8a28-cb1c0c6d669a | -13.3288 | -47.47631 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 530eea93-2b22-399c-b3ee-16ccd830079d | -16.20241 | -45.05041 | 2025-10-30 04:27:00 | NOAA-20 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 905fe00a-f840-336f-bea2-06b1dba74c94 | -15.74915 | -45.11759 | 2025-10-30 04:27:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a975297-a56b-3621-afbb-6a3ad1bf8785 | -16.67979 | -41.36876 | 2025-10-30 04:27:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 737e0c9f-7c61-30f5-a9fb-581825269c33 | -12.3644 | -50.15243 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ac610579-5b6e-3300-a0a7-0795ddc9d9e3 | -13.94097 | -48.45842 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b894ae37-7a2d-30f9-8774-39bea17002d6 | -14.71381 | -45.09691 | 2025-10-30 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58497fec-3c86-3ae5-b686-3997a19a8055 | -13.02029 | -48.7718 | 2025-10-30 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca38f4d5-0ff8-373c-b564-64962c7b836a | -12.31421 | -48.06936 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50b136df-69e9-3e67-a2c1-5ae2c8474c89 | -13.92858 | -42.3731 | 2025-10-30 04:27:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c5266215-937e-31e0-b376-e7fa4508c37c | -12.88044 | -48.62995 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1abeb621-fd4e-329a-9ad3-7c99604c924b | -13.61025 | -47.60875 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60856152-3f0e-3edf-8663-3f23247db4f4 | -12.28874 | -47.0041 | 2025-10-30 04:27:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae78bb02-4ac7-37d0-9447-4b110447660d | -14.75457 | -44.95604 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82e0d3be-7f77-3483-a2ac-df31372e26c1 | -12.31202 | -48.06169 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9aa1a0ce-474a-3cbb-a041-15f6a01c86a0 | -13.29399 | -47.0671 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ae31e21-fdf4-3297-babc-d4a059b70bd2 | -12.53392 | -47.54159 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 794ef6b2-e1f4-3b2f-a516-d672d6e12224 | -12.11879 | -47.1356 | 2025-10-30 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deda792a-9755-3436-926a-86c70883282e | -13.27673 | -47.74287 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bceccb1-75c6-369c-a0b6-a50df515b983 | -13.39624 | -48.52857 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7fd936c-b0fb-3986-bab5-40d792fa513e | -14.28885 | -47.30766 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bddbb5df-a4e7-30ae-985e-83f3716650bf | -13.24568 | -47.72307 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bd395a7-0350-3c94-9f5d-a754726e8d91 | -13.31887 | -47.47476 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eae7e5c3-bc50-34f8-8c53-79ee1c90ffe9 | -12.30814 | -47.27098 | 2025-10-30 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d1e9188-5261-39cd-a300-80e0efde5394 | -13.94428 | -48.45899 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa3426cb-8531-36d6-a7ab-ed45868f9377 | -13.70381 | -48.39001 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccf84068-9159-3c88-9708-0a7485b29f89 | -13.92669 | -42.37202 | 2025-10-30 04:27:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f2114ef7-e304-3cd0-ac9b-528f69d7a09f | -13.52308 | -47.3408 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f3b1849-1582-3e49-9bf9-df2916fcc503 | -14.12959 | -44.06713 | 2025-10-30 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6fe42d4-b5ff-3064-8746-ee177b4aa414 | -13.16234 | -48.46068 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d2df65d-f493-3510-9d14-4302ebe0f0d9 | -18.04264 | -43.14767 | 2025-10-30 04:27:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c3750875-87f7-3cba-9750-d6f1a281189c | -13.3935 | -48.52442 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99a3722a-5777-3d93-a20b-b29240ff1482 | -13.28613 | -47.7263 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac6eda94-25f7-3f2a-afa8-95ebe14293fc | -12.5228 | -50.57041 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eab898f7-2220-373f-adc5-cc138b53ca32 | -16.88755 | -42.00107 | 2025-10-30 04:27:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d2944383-9a4d-3516-a8f7-80e0b60a03aa | -13.40825 | -47.38056 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9db893fc-6466-33a7-9ed4-b5c0e92851b7 | -15.02145 | -46.32349 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 08e3283c-b90f-3f3b-abac-288971a83c98 | -13.18017 | -48.43463 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1abc152a-4aa8-3d91-b64b-101463f59482 | -15.31252 | -42.63469 | 2025-10-30 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c0fdb507-8590-38ad-92da-4b852c7ded8c | -13.49435 | -47.99912 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dcbb476-61f3-36cb-b857-567b25c6e102 | -12.78564 | -47.86105 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae423408-0afc-3b5d-8976-9ef5a3286bdd | -13.04776 | -48.6656 | 2025-10-30 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccfbf625-e522-3b36-a059-66594aa19506 | -12.20196 | -46.49125 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35a59645-e165-328a-87ae-3b4bbe505a71 | -13.75018 | -48.39783 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14d4ced3-0cea-3f2d-b7eb-23a29d01f09e | -12.37499 | -46.48928 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba8b1b77-3f62-36f3-af57-e9e97491661c | -13.94873 | -48.45246 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cebf8489-f98a-3e10-947f-4c0ae76761d8 | -13.28227 | -47.72929 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a0ea90a-7017-3933-9fa2-69d88b0079f7 | -12.24724 | -47.93526 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c6ab3f9-5c95-31af-9b8c-f8af5012a237 | -13.56073 | -47.31736 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be918e65-42b6-3524-8751-025cb15a9f80 | -13.21909 | -47.04773 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15511bc6-71bb-3107-8cce-3e4f62c28963 | -13.72335 | -51.45833 | 2025-10-30 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e5d1ba4-5498-33f2-90eb-a6089b64de7e | -14.40706 | -42.65895 | 2025-10-30 04:27:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 00affea5-a0cd-317e-a428-56e4da67b736 | -13.16292 | -48.45707 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f56fed94-fb05-3375-8d2b-5f6fa912964d | -19.3366 | -43.06892 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d8b481b7-c37f-3706-86a4-a9dc9584e720 | -12.66332 | -45.80753 | 2025-10-30 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f36e105-294a-3a69-b206-3c7ef82a493f | -13.94759 | -48.45957 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9f71ed4-f077-3aa1-a0a7-3366cced02c7 | -13.34627 | -47.66744 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 322f5ed1-8a8c-3a61-9de3-df3c38e1c607 | -13.42094 | -47.36425 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README57.md)
