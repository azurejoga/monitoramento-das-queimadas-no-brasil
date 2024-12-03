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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2222086a-1666-30a3-8cf0-ff2e0b0788d6 | -2.23606 | -46.38959 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcff00bc-270e-31c5-a5e3-15a0836ebcc4 | -1.80329 | -46.65643 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0352dee9-c67e-3c05-a7b0-56618287f78e | -0.36795 | -48.476 | 2024-12-03 04:27:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b47c4260-5390-3b11-abaf-11c4a441ed3c | -1.23405 | -51.60868 | 2024-12-03 04:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ce9f789-2b0c-3e6b-8e50-5f6707ba91f0 | -1.99253 | -45.38926 | 2024-12-03 04:27:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 175a786d-e873-3b76-82ef-b71cfcd35e95 | -2.21225 | -45.73844 | 2024-12-03 04:27:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9f92a74f-a125-318f-a277-969c48fe8906 | -0.6047 | -51.68922 | 2024-12-03 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6fbf494-4ef8-3622-a482-d1158a12fd35 | -1.23461 | -51.60514 | 2024-12-03 04:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a37db4f-821a-33dd-8f3e-44c07e81d274 | -1.4775 | -47.53814 | 2024-12-03 04:27:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 078d79d4-8f86-356f-bef1-c58b1e5bbd5c | -1.03247 | -53.56229 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d38fb87d-4b7c-34b9-9ede-4b94602594b6 | -2.2128 | -45.73492 | 2024-12-03 04:27:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 09c6aeed-e6f8-3c38-a844-488aaee935f3 | -1.02859 | -53.55682 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0ad6627-f877-3b2d-9d9b-d816522343ac | -1.84558 | -46.23689 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9475b1a-ad81-3028-92d7-53649bad1c34 | -2.09105 | -46.31786 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5a1c7fc-141d-337c-b0be-b3b992f6a316 | -0.75348 | -47.8485 | 2024-12-03 04:27:00 | NOAA-20 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2f41842-2f10-3ffe-94f5-a050752eef45 | -1.84227 | -46.23637 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f16be48-4b1d-3528-b9e7-613b95d1c3c4 | -1.34907 | -51.38311 | 2024-12-03 04:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df736967-5730-3e22-a98e-54631996539d | -2.85353 | -41.75526 | 2024-12-03 04:27:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48fdbccd-6b04-3a0f-a22d-ad0f43feec2a | -1.7074 | -46.208 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f965af5d-f6f3-3491-83c9-822aba4b3488 | -2.22728 | -46.40234 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2664978-83a1-3f3e-844d-4a210b842193 | -1.07359 | -53.45003 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d11de97e-04ef-3967-8b35-5c814397230e | -1.70686 | -46.21145 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e22a4133-b669-30b6-bbb6-a5704bdc37c8 | -0.62809 | -51.70032 | 2024-12-03 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2400b540-0c17-31dc-b2e6-2dfdcb5644a9 | -2.24154 | -46.37632 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06affae7-5e6f-3453-9a56-5d9b2a893212 | -1.13698 | -53.23073 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca43f4b1-887d-3b25-807c-b44dcf4fe185 | -2.95667 | -39.96535 | 2024-12-03 04:27:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f159a413-a375-316b-a9aa-de48ede9bad6 | -0.35811 | -51.59138 | 2024-12-03 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bcf8405-6600-399a-b629-35699f63acf2 | -0.91325 | -53.1058 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8daa8ac9-ad90-36d2-911e-0ea6cdd6a9d3 | -1.61105 | -45.54472 | 2024-12-03 04:27:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e977e6e-aad2-34dc-b026-148eca50bc2b | -1.08199 | -53.45617 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 3c96b744-3264-30de-907e-f6a97dc5cd99 | -1.48831 | -47.27709 | 2024-12-03 04:27:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82a36ddc-42b1-3aef-ae45-9276cea770be | -1.97404 | -45.41925 | 2024-12-03 04:27:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 296749d9-1519-340c-affb-db3cd5f5ae79 | -2.10031 | -46.45333 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 085b2ce6-4abc-3a47-a351-41608ed93ebe | -0.59711 | -51.68427 | 2024-12-03 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e71d2e69-9162-394f-b952-bb11ae0fc8dc | -1.14484 | -47.70942 | 2024-12-03 04:27:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4aaa0c3a-eaee-3011-bdec-f30187c476ac | -1.59729 | -47.36127 | 2024-12-03 04:27:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0fb099f-8032-3786-bf9b-6c4e905ff75d | -0.85504 | -52.71006 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a720bd6e-6144-3bb8-ba8a-8fe67ad36c4c | -2.23883 | -46.39355 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c987a13c-797d-3254-a534-f3e6270d0a09 | -1.87908 | -45.48438 | 2024-12-03 04:27:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6eaaae42-8f0b-34dc-bb00-dfaf1c9a836e | -2.05119 | -46.29038 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ace52b4-2fa8-3612-b6d9-be3291346617 | -1.03678 | -53.55984 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6cab788-c8fd-39cd-ac33-243ac98b61a4 | -1.08124 | -53.4608 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 388723cb-1472-3511-b454-9f5d239e358b | -2.23052 | -46.38167 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c6f6e5a-c8ec-356a-b88d-3756fee22a1f | -1.08583 | -53.46143 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| afde4463-ff2a-32f1-9c16-70bc874cc307 | -1.03485 | -46.83492 | 2024-12-03 04:27:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4de3b7b-9baa-3d6b-ad06-2f330c465967 | -1.67856 | -47.55547 | 2024-12-03 04:27:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5de3240f-82bf-308a-b63f-46d8ba57c78f | -1.25506 | -51.63719 | 2024-12-03 04:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1df296d2-3718-3725-88a4-8dc418f004e3 | -1.3451 | -51.38249 | 2024-12-03 04:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 101a42a1-bd87-3f45-900c-d89736ceb7f6 | -2.23383 | -46.38219 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a89bf72-3469-3764-aff6-ac10c10a92de | -1.48556 | -45.84767 | 2024-12-03 04:27:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de8f9f4c-b117-3bf1-9e61-6180d6586417 | -1.2953 | -51.37273 | 2024-12-03 04:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3677f7c8-6c39-3f0f-a585-8af7f4b00ca9 | -0.61288 | -51.6905 | 2024-12-03 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0fc7e6b1-ee4c-30dd-9606-195fe635f264 | -0.84065 | -48.72045 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 904f346d-127e-33ab-91ea-3de8da903e7e | -1.93949 | -45.55192 | 2024-12-03 04:27:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ce74ef4-edc1-308d-9f65-c0d8efd32cb9 | -1.61278 | -46.16209 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72c42a6f-87fa-3ba8-a36a-e894c2002fa5 | -1.79669 | -46.65541 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2c2cd1e-35b9-3293-bb16-cd1ac779d206 | -1.72842 | -46.22538 | 2024-12-03 04:27:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fe37e11-1d97-3f2b-8bb9-622021475a42 | -1.36591 | -47.68637 | 2024-12-03 04:27:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ba380f9-8aa9-3e4f-9abf-4d789faf2c6c | -1.79999 | -46.65592 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8636b2e9-cacd-342b-8140-6bed30f20075 | -1.48416 | -47.53918 | 2024-12-03 04:27:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38391dbc-0adb-3e2d-be25-b2051f0049ef | -1.83896 | -46.23586 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 176d9fd2-9066-3ff9-a68c-047d2c82fb4b | -1.70355 | -46.21094 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a4991ac-7915-3f3c-9131-32ea4b38a206 | -1.5131 | -45.90886 | 2024-12-03 04:27:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85f02b23-7ca2-32ec-878f-03c9d75f2886 | -2.23329 | -46.38563 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeb1a4ac-2b9e-3676-9c09-4142d4088d50 | -2.11393 | -46.5822 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c51281e-848d-3aa5-98f5-1a2c6dee8b57 | -1.72186 | -46.24555 | 2024-12-03 04:27:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c7a1cdf-c248-3991-a0b2-584f7d0adcce | -1.96129 | -46.45279 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01bd36fb-167d-3305-959d-e7e6ef107581 | -0.76142 | -52.41754 | 2024-12-03 04:27:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56c0a837-9d63-3a5e-a144-26c2c4517eeb | -2.23937 | -46.3901 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 299fd588-96b0-34fa-9e27-eeb0a06de950 | -2.20946 | -45.73441 | 2024-12-03 04:27:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d347afd5-180a-3638-9831-45232baaabf7 | -1.74178 | -46.26981 | 2024-12-03 04:27:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e2b5d7b-536e-39a0-8170-1162df48bcc3 | -1.6897 | -46.19113 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b997bc5d-15f3-320c-8d97-8245e2ca1566 | -0.82098 | -51.90305 | 2024-12-03 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2d53301-ced9-3f82-9871-63198f19d015 | -0.37139 | -48.47654 | 2024-12-03 04:27:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f73391cc-ae77-340d-a1e1-ed97475d4bff | -1.65731 | -47.00306 | 2024-12-03 04:27:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bce9abfd-975a-37f1-8463-1bb262eeb2c2 | -1.67523 | -47.55495 | 2024-12-03 04:27:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 307fef65-0699-302f-98fa-a0ad22650b46 | -1.72131 | -46.249 | 2024-12-03 04:27:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77ec7516-956f-301e-bf09-447fa4a150b3 | -2.20891 | -45.73793 | 2024-12-03 04:27:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fea50dd4-fa78-3469-b82b-c99a3b666ee0 | -1.07233 | -53.45756 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc98b5f6-325b-3ae3-9295-1fc1a43aece1 | -1.32002 | -51.95786 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b4af47d-3faa-315a-9f70-12921c2a355f | -2.23059 | -46.40286 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7c6d451-c7c4-3042-baa9-010c77652813 | -1.36257 | -47.68585 | 2024-12-03 04:27:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b886db20-a93a-3203-b248-f583a0411e7a | -2.12554 | -45.34369 | 2024-12-03 04:27:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| aa6d361f-aa58-33a4-95cd-03b6e4ace32b | -1.07303 | -53.45307 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 89551a9e-b189-33f2-983d-e630508013f1 | -3.16412 | -40.17871 | 2024-12-03 04:27:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4b988ea3-473c-34d6-baae-ee53556c6b1a | -1.80761 | -46.62898 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 245e89f2-c787-34f7-8bc4-adcc1d246f1c | -2.11272 | -46.54683 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49467309-3e84-31cb-a097-a00d84006e57 | -2.23396 | -45.36787 | 2024-12-03 04:27:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2693df63-4383-315c-96f7-6c9bc46d7295 | -1.86229 | -48.00581 | 2024-12-03 04:27:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e516306b-b59b-340f-afe2-9ceadcf7a675 | -1.0332 | -53.55761 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b79cd79c-c92c-3d05-bd49-74a4d5a3d012 | -2.10071 | -46.58015 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7774321-6c69-3d48-b752-4426d524aee3 | -1.70254 | -45.7638 | 2024-12-03 04:27:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 438d1a60-03c0-3fce-84de-b9dbc2ad4bb9 | -1.07283 | -53.4547 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1be814d9-00a3-3fa2-91de-bc65b0fe0202 | -2.29238 | -45.76848 | 2024-12-03 04:27:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13dc7755-3983-3ee3-ac43-d52c361203f8 | -1.29354 | -51.37429 | 2024-12-03 04:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f060e546-8d15-3a07-b737-1ca8aa014cc8 | -1.79945 | -46.65936 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9aa391ea-985c-3f7c-8ed8-0c4628fe65a1 | -1.07816 | -53.45076 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 167d3e1e-1aec-3e8b-8a3a-62a9c961a29f | -1.08658 | -53.45683 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 3b8a9a66-a28e-3711-b6fe-022fed1e19a4 | -1.07667 | -53.45999 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4f567211-e3e5-3b9c-b3ec-38d5531359de | -0.60061 | -51.68857 | 2024-12-03 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
