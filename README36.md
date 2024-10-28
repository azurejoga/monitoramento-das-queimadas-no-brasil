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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c4f4384-8dcb-33c2-8a69-904dfc993ca9 | -6.60453 | -37.279 | 2024-10-28 04:06:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d214409-28fa-3f4c-8504-61ae2a2267e1 | -8.93196 | -36.55643 | 2024-10-28 04:06:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 01fbcfa4-3777-3720-800c-0f1d187d4af2 | -8.93011 | -36.55642 | 2024-10-28 04:06:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e00b0a35-5736-3a72-a52c-3b30797de05a | -11.39079 | -37.6729 | 2024-10-28 04:06:00 | NOAA-20 | UMBAÚBA | SERGIPE | Brasil | 2807600 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c71cae0f-8b0e-3767-8656-6d167e0d05b1 | -11.3903 | -37.67645 | 2024-10-28 04:06:00 | NOAA-20 | UMBAÚBA | SERGIPE | Brasil | 2807600 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e33bb21c-3c3d-35a3-9ef4-65b4edebc65c | -7.56518 | -38.75527 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a95acdab-41cc-312e-88af-e8af5400db82 | -7.56457 | -38.75937 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65c9d859-d637-3b30-8287-598448e0410e | -7.56395 | -38.76345 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ef6164cb-0a06-3ddc-993a-12438e183bf9 | -7.5616 | -38.75469 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0314292b-52d9-30e6-a1d3-463041eb8762 | -7.55742 | -38.75818 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3da84863-986d-342e-8e33-4eaa262f85a1 | -7.56753 | -38.76402 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 998ba3e3-f545-3c29-9550-d60ef1756150 | -7.55384 | -38.75759 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 203ae0d2-fc91-33ff-86e4-01ffc7ccbec0 | -7.56221 | -38.75061 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 72310e11-3329-33df-bac4-e9392f09fd00 | -7.56099 | -38.75878 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4497652f-19bf-303c-a1bd-d83f4eaa1f6f | -7.55803 | -38.75409 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 14521c76-8daf-3262-9433-239937962db6 | -7.56814 | -38.75994 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b63b125-996a-3cf7-a093-29c33542a34d | -7.56038 | -38.76287 | 2024-10-28 04:06:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 35f18e24-b20b-389f-ae58-927eb1400a3d | -7.9778 | -38.87093 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f030448d-44fb-38b8-89a8-4311476ce88a | -7.97657 | -38.87914 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d27a7fc1-9f72-34cc-bf2a-ae2a35bf58be | -6.38441 | -39.85149 | 2024-10-28 04:06:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 968a0177-be10-3af3-80bc-4d77658f7a0b | -7.21615 | -40.09285 | 2024-10-28 04:06:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a95f8303-6724-3d57-80f6-4a5d08f1c48c | -7.20362 | -40.0993 | 2024-10-28 04:06:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c3c73fc7-9476-37a8-a041-4e5fd06bd0df | -7.81419 | -39.77297 | 2024-10-28 04:06:00 | NOAA-20 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 858de9af-4445-330f-ba26-54b2379ded85 | -7.45415 | -39.72488 | 2024-10-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3684ed9c-003d-3631-9d4d-081e10eee02e | -8.91147 | -40.706 | 2024-10-28 04:06:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 788d2caa-0fc7-3c16-87cd-e4ed2e2e1b7a | -8.07454 | -39.92713 | 2024-10-28 04:06:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b58ed61e-5d50-3964-b966-c7fff362d153 | -8.07511 | -39.92339 | 2024-10-28 04:06:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| edc6c008-afed-3da8-aae0-fd5ecd2c3104 | -8.07169 | -39.92288 | 2024-10-28 04:06:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 81e76645-bb52-377a-9ab5-995da381e769 | -9.48335 | -40.53942 | 2024-10-28 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c88455b3-62c4-3685-8f9b-53c72b658381 | -6.57175 | -40.55854 | 2024-10-28 04:06:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d152eef0-494c-3e91-b82a-7494b7196190 | -6.3745 | -40.47352 | 2024-10-28 04:06:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2d9498b0-3a62-354a-b399-2c5aecfefdf9 | -6.37117 | -40.47301 | 2024-10-28 04:06:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c0c78b3a-e77e-3621-aac5-e0866cd732b1 | -6.3653 | -41.57526 | 2024-10-28 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d64631b-6773-385d-a663-b3a69a2062a5 | -6.30093 | -41.91899 | 2024-10-28 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8dda9326-1b72-3ee6-b151-3c29558d41ea | -6.29983 | -41.92591 | 2024-10-28 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24e38f46-21c6-331d-b7a6-09c63437563d | -6.29817 | -41.915 | 2024-10-28 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bcd34c72-d240-33e2-8876-7e97b08152fa | -6.29762 | -41.91846 | 2024-10-28 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb10f977-0314-3602-b3da-c42df276afe6 | -6.29653 | -41.92539 | 2024-10-28 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3403c45c-2423-31f9-b1dd-15b4e548b99f | -6.29322 | -41.92487 | 2024-10-28 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7a784de-ba58-32dd-b5af-f05856345b18 | -6.29101 | -41.91742 | 2024-10-28 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 93de1e39-c034-3d7f-8b09-1ccb1aff0028 | -6.29046 | -41.92088 | 2024-10-28 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e12f1b18-9ade-3c55-926c-d4b22b5fd691 | -6.28886 | -40.82634 | 2024-10-28 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ac3e8cb3-cf62-3a02-94b5-3d2a3ad9252c | -6.28716 | -41.92036 | 2024-10-28 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3ac74f5e-65fb-35bf-8bb6-8f3e366d7899 | -6.28549 | -41.90947 | 2024-10-28 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8c63e71f-c7bf-3e80-bbd6-b73426dcb517 | -6.23499 | -41.25752 | 2024-10-28 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6078b3db-4d22-35ba-886f-f3396d9a031f | -6.23006 | -41.26735 | 2024-10-28 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 57ee4f3e-8d98-329a-a1a3-f7d87bc37ba9 | -6.22676 | -41.26684 | 2024-10-28 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 14676ccb-eb9e-3c83-b88d-deba2834b067 | -6.22621 | -41.27029 | 2024-10-28 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f598ea51-1050-34d4-9eaa-580ae4f60c7a | -6.15808 | -41.78971 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3fd15e4b-9ebb-3b5f-a6d6-152dccb83359 | -6.15711 | -41.86041 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3320294e-4129-3235-99fa-0a1f12a48b2a | -6.15656 | -41.86385 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| a089a55d-24c9-3ec1-8c6f-04fe3863644e | -6.15478 | -41.78916 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ddeae48a-ca7b-3257-86df-a04623a11342 | -6.1538 | -41.85987 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 629ced4d-d760-3212-888f-a8b10f6c76a7 | -6.15326 | -41.86332 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 121ee8f6-e2c7-3943-bc5a-5ba061404293 | -6.09376 | -41.87528 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d8417750-086c-3c5d-a23b-171705132666 | -6.09267 | -41.88221 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c0f4f0c-a770-3d28-8249-1daa73e102da | -6.091 | -41.8713 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 765f83d0-e26f-3752-b914-446381cd57db | -6.09045 | -41.87476 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5de647b9-058f-3465-9302-985b268261fc | -6.08991 | -41.87822 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b78daf69-3cdb-39cc-ab87-25a1abb44a9d | -6.0866 | -41.8777 | 2024-10-28 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0ca180a3-2d24-33cb-8f9f-e88b4a3a961f | -5.61622 | -41.73597 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c1b10f35-e2ed-3366-a95d-6097fdf1abef | -5.61346 | -41.73199 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 426f1208-a52c-3f9d-8647-57bd7a7f0f82 | -5.61015 | -41.73147 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab67171a-d617-3fc7-a87b-bee6a1c2f4e8 | -5.60797 | -41.7453 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31dfcddb-3ea8-32d8-8c5d-ed3b45908fea | -5.60743 | -41.74876 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6f0976dc-2acb-326d-8c7a-0cc8f31b65ca | -5.60685 | -41.73095 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1680bb7d-ea81-3748-b248-6eb14329ec92 | -5.60467 | -41.74477 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6c1ffcaf-65fa-3ad3-b89f-13e0188d1ede | -5.60412 | -41.74823 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e114567-b6e7-30d9-9a51-970e97d924c5 | -5.60354 | -41.73042 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f4ac69da-b30b-3228-97d8-c3d94bb015b1 | -5.60027 | -41.75117 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 718db3d1-2300-3c4d-8ff7-a02e46b20c9b | -5.59969 | -41.73336 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a776d06-9ffa-3239-b13d-ca4c186fb021 | -5.59696 | -41.75066 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c800b4a0-643c-317b-bab1-5ace5258ca66 | -5.59642 | -41.75411 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 83565f45-3769-3bf4-9daa-ab1bcb7df605 | -5.59638 | -41.73285 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d71f8827-df4e-3b02-ad6c-ca9b00c3bc68 | -5.38549 | -41.47659 | 2024-10-28 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 99757a2b-cf3a-348e-811e-9644d205ca4d | -5.38165 | -41.47952 | 2024-10-28 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4feb9707-6799-3266-930c-a250d5b81747 | -5.29808 | -41.03638 | 2024-10-28 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ee18309a-42b1-3ce6-a6ca-aa73145f6ac1 | -5.26401 | -41.232 | 2024-10-28 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c7f5bb87-3bc5-362b-84eb-8e4606a946c9 | -5.26347 | -41.23544 | 2024-10-28 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7407dbb0-fb4b-3685-bbb6-e38682a7605e | -5.26071 | -41.23148 | 2024-10-28 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0dbef0f9-2374-321c-9aff-fe6be083ebac | -7.33632 | -41.8601 | 2024-10-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f231ed75-a85c-3317-b4f5-02a8862b9f40 | -7.00669 | -41.31908 | 2024-10-28 04:06:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b27a750f-5417-3de9-bc6a-e949ee6fca58 | -7.00664 | -41.29781 | 2024-10-28 04:06:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4af3e3e3-02dd-3728-bb14-7de4d951393c | -7.0061 | -41.30127 | 2024-10-28 04:06:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea43b5f5-90e5-3387-8578-97c093e359d7 | -7.00567 | -41.34727 | 2024-10-28 04:06:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bdb2985c-4884-304b-a399-c6164787c64e | -7.0029 | -41.3433 | 2024-10-28 04:06:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e43212aa-a92f-3e80-910b-0924ff3239fb | -7.00068 | -41.33587 | 2024-10-28 04:06:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b3ebbc38-9848-3b6f-b7f2-a28f486e2073 | -6.99791 | -41.33189 | 2024-10-28 04:06:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cd4b6698-f8ba-3693-8955-224f1c10c01b | -6.99737 | -41.33535 | 2024-10-28 04:06:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dbec7313-e9aa-30b8-8c11-89a269fa5ec1 | -6.99515 | -41.32792 | 2024-10-28 04:06:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b0021768-ee4d-3384-83ea-ff70cb766f57 | -6.99347 | -41.31702 | 2024-10-28 04:06:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4a7f1346-7097-3d9b-8d61-d65cb1edc373 | -6.99293 | -41.32048 | 2024-10-28 04:06:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a2467ba4-83d7-307e-9720-b11472ce7fc8 | -6.94725 | -41.33104 | 2024-10-28 04:06:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e8c842de-a178-3765-8272-5427e1451158 | -6.94671 | -41.33451 | 2024-10-28 04:06:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a606cd9-3eac-3ff4-9d67-d30e0b955e27 | -6.9434 | -41.33398 | 2024-10-28 04:06:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b134086f-d7c5-3527-af55-f294a328cb86 | -6.92579 | -41.33831 | 2024-10-28 04:06:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8cb3d48b-0ace-3d20-9ad3-5c05569ce2af | -7.33578 | -41.86356 | 2024-10-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c5435f63-e8df-3218-9ffb-f7a703dd3759 | -7.34293 | -41.86115 | 2024-10-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7d5ef165-4170-3bf4-bd61-1974e16ddfe7 | -7.33908 | -41.86408 | 2024-10-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2cec1189-b2d6-369e-9d39-381fc23a9ea4 | -7.34239 | -41.8646 | 2024-10-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README37.md)
