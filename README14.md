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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 887f014e-58e8-3f1a-9947-435d3c544ea7 | -2.8726 | -46.77063 | 2024-11-08 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b9947517-2f1f-36fb-ba01-a4edfff82e33 | -1.38372 | -47.50889 | 2024-11-08 03:57:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fac2f83f-ebd8-3d57-999e-3620b4e20468 | -4.51893 | -45.69444 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| fb2965e5-82a5-311d-b448-20ad96d733e5 | -3.80604 | -44.46582 | 2024-11-08 03:57:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9fff1d4-9c90-317b-acaf-b0858812c6f4 | -3.9728 | -48.1772 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0c4e3382-ac4a-3736-8502-539faf6cfba5 | -4.21742 | -45.74211 | 2024-11-08 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1bf1506-0a5f-34dc-b954-a1865ebb8ec3 | -3.07179 | -45.74537 | 2024-11-08 03:57:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 777881d6-6c57-3117-ab1f-a7887b3bcdd2 | -3.90828 | -46.444 | 2024-11-08 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a5e1a8c-9f5c-3316-9637-e4b5016166a9 | -3.71818 | -40.69764 | 2024-11-08 03:57:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b863c8a6-98f3-391c-ab11-2e439fb82a03 | -4.31718 | -45.13849 | 2024-11-08 03:57:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b3c1e26-49dc-3673-982c-99af033691fc | -4.28327 | -45.69642 | 2024-11-08 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5406fd70-0267-37c5-9bcc-a3ed3d7d61be | -5.03427 | -40.97372 | 2024-11-08 03:57:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9f2d9f10-93ba-35aa-a7d3-930606910c08 | -3.59884 | -44.91787 | 2024-11-08 03:57:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49f027a8-c600-311d-a7a7-d2cd88a3658f | -3.80546 | -44.46941 | 2024-11-08 03:57:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 533fb4d4-37cc-3ba8-902a-bafb901ec44e | -3.7436 | -52.10022 | 2024-11-08 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 472efc57-2641-37c6-8f0a-a67cfedfdcc1 | -4.69527 | -46.37512 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e7d75c78-50cb-3a1a-9a63-09812360498f | -3.79341 | -44.02079 | 2024-11-08 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 86a55235-f0e1-35ff-9aa7-f4c3fe7b158d | -4.24433 | -48.53978 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 232e6e6c-763b-3e95-9d6d-87cda3841852 | -3.72131 | -41.69168 | 2024-11-08 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b028076d-1c15-3d74-9e67-09a2756c1775 | -4.52535 | -45.6828 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c3626f44-00cb-32da-a306-51a3e514249d | -1.65839 | -47.91329 | 2024-11-08 03:57:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f880d95-10f1-3773-acf1-dae042e3b1fd | -4.19994 | -44.26781 | 2024-11-08 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c28d96d9-f430-3cb0-9264-71b310ee072a | -4.68461 | -46.41156 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fac660b9-e2b8-3b19-991d-60a6ed483115 | -2.17042 | -46.44133 | 2024-11-08 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2982eefd-e0e2-3da1-973d-573d7328a683 | -2.01473 | -46.58355 | 2024-11-08 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fc014d43-be7c-3cb2-a5f4-f380950a8718 | -4.17146 | -47.46606 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b806fdbb-2a76-36b2-a6db-37931d028cc3 | -1.695 | -45.80524 | 2024-11-08 03:57:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d6f58aa-fb0a-357b-89c7-8acb0b272cfc | -4.91906 | -44.0452 | 2024-11-08 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf327e9e-4cb9-3537-b114-ee088d320880 | -3.96269 | -48.16792 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ed7cf1a-729a-3aca-9ac8-6185fe9dbafd | -4.79124 | -37.76384 | 2024-11-08 03:57:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6eed3456-d180-3b7a-805c-c76790e5de40 | -3.95748 | -48.1671 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47a8761d-3bcf-3e76-bfc4-b4f9b4fd52e0 | -4.74044 | -44.10309 | 2024-11-08 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58665408-0df2-3be0-97e1-ea1a7db907af | -3.52791 | -40.91872 | 2024-11-08 03:57:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0489f005-6988-30e9-9814-7c507502ad3a | -2.26799 | -47.99947 | 2024-11-08 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a4cd019-c9e7-35d8-9703-dd610c55c8e3 | -3.40712 | -47.58361 | 2024-11-08 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbb3a8de-0d80-3cf9-b4a6-ae19362f1d56 | -5.52104 | -37.62184 | 2024-11-08 03:57:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cce98c7e-d0c0-3878-924f-2b336d267f8b | -4.21748 | -45.05898 | 2024-11-08 03:57:00 | NOAA-20 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08b1877b-d3cf-361b-b769-671c6e3907b4 | -4.08076 | -43.36047 | 2024-11-08 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6bbac03-d555-39fb-9d31-acdf38e3791f | -4.31174 | -45.6908 | 2024-11-08 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c16b3cb-c622-38f2-a440-50f3b73a87e2 | -4.51238 | -45.68035 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 43fa5953-4c8f-30ee-9e45-f82778af9668 | -5.54359 | -41.67598 | 2024-11-08 03:57:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 94b52726-f210-3e99-8ee5-3c08de849417 | -3.78868 | -44.02513 | 2024-11-08 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e86828c-3b93-307b-bc43-150eb90612b4 | -3.53748 | -47.38474 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f93f785-e2f6-3454-981b-e1cfc40c2041 | -3.24181 | -45.69313 | 2024-11-08 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0084690b-d1c6-3daa-9874-fab957cc5854 | -4.36278 | -47.22515 | 2024-11-08 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8589b48a-5f9d-34fc-91d0-2beb85152326 | -4.61514 | -45.71428 | 2024-11-08 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d802b71f-dd7f-3745-9b74-5b5faf93ba1d | -4.21541 | -48.55875 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd9c8c22-e692-3749-909f-b69bbd5aeec6 | -3.88567 | -43.15217 | 2024-11-08 03:57:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cccdefb6-4c81-3fc6-92e6-fa8a668b3c78 | -4.91517 | -44.04466 | 2024-11-08 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e539f006-8567-3d77-824a-696c0336ca4d | -3.59178 | -45.20238 | 2024-11-08 03:57:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b6eaf46-197f-306f-93e5-8d47b264a164 | -4.61305 | -49.58002 | 2024-11-08 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5af8f637-4f4f-3751-8c2b-55b2df765e93 | -3.71927 | -40.71244 | 2024-11-08 03:57:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a5950568-9f9d-3740-8075-c84fc6ef30f5 | -3.9719 | -48.4024 | 2024-11-08 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a45721bb-16e5-3149-9e08-9dc3647e9cd3 | -3.58486 | -42.85694 | 2024-11-08 03:57:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 378f2dd6-1d4a-3046-ba9e-42d50916badb | -4.32063 | -44.84381 | 2024-11-08 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07050623-1314-3e28-93a6-fa1e5c23998b | -4.23805 | -47.8698 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce891bf0-1d52-362a-bcd5-1d841b5bdd42 | -4.51963 | -45.69028 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 900736d6-24e2-3e2f-b9ba-324cea1c99ec | -4.50714 | -45.67798 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 40419253-f970-3844-b952-fea4144ae934 | -0.92377 | -47.13386 | 2024-11-08 03:57:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d903c425-1588-312d-9f12-64ecb4719dd9 | -4.52033 | -45.68612 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| fb212836-9de8-3881-b1cc-778d769b1256 | -3.55242 | -47.3869 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 6f4a4dd3-3cec-3593-b59b-856176a3757f | -3.71089 | -41.69001 | 2024-11-08 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a3c7a3d9-1f7e-3da2-ae8f-d8452390b749 | -3.69168 | -43.72952 | 2024-11-08 03:57:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fd68007-b01f-324a-bf80-e4d58f2beec4 | -4.51082 | -45.6828 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a0e96d25-d30e-38ce-b098-5dff5fbbe61c | -3.96322 | -48.16471 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7582a027-6c91-3caa-a260-2dcde6421a8d | -5.42675 | -42.44785 | 2024-11-08 03:57:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f99c1e0e-96bf-3813-98dc-669713d60d5e | -3.38036 | -46.10868 | 2024-11-08 03:57:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 895777c4-88c9-39ff-9d69-07d5573d665d | -3.13417 | -44.49494 | 2024-11-08 03:57:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c2dfb3a-d0e6-3bdb-a1b1-b9f86457f5ac | -5.62121 | -37.78997 | 2024-11-08 03:57:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 48468ffc-71c3-38e1-b83c-02190daf9717 | -4.48426 | -48.11315 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f0fc5ef-c5db-38bf-8d9a-5e29589faaee | -3.46666 | -39.14864 | 2024-11-08 03:57:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| adcff001-8f33-38ad-8792-028826d089fe | -4.36362 | -47.22847 | 2024-11-08 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7814267a-fb9a-35be-a6bd-ad79b82ac07b | -4.52967 | -45.68364 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9f4825c1-14cb-38cc-93ef-bd95357d5d56 | -1.14524 | -52.00285 | 2024-11-08 03:57:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b299c617-d272-3cb2-a585-2d5cdf59c8aa | -1.47433 | -47.22108 | 2024-11-08 03:57:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ed3a9d1-7998-3f43-9102-bfdfe10391bf | -4.46673 | -46.30769 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdb33f82-0711-305c-b49a-763eb32dc29b | -6.52622 | -35.26543 | 2024-11-08 03:57:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6ce49d65-3b05-31b5-9fd7-b6039559bfaa | -2.17125 | -46.43623 | 2024-11-08 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e9dedc7-1e49-39b8-bd33-fc864dbd2443 | -3.53842 | -47.37904 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9cb2b49-bb19-398c-8161-7a9f33268b3e | -4.32337 | -44.8443 | 2024-11-08 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0613931-e387-3ffd-8a7c-9f4a3ca291e0 | -4.32123 | -44.84007 | 2024-11-08 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18e8a784-9194-33a6-b813-0f26c1ced511 | -4.9774 | -45.49551 | 2024-11-08 03:57:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f0687eb-be70-378f-b4cc-dc2693c6976c | -4.60888 | -49.58736 | 2024-11-08 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d54fabd-6e50-35fd-9b36-4daf2dd4bea1 | -5.2053 | -42.40561 | 2024-11-08 03:57:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 769c81dc-80c3-39b2-8a6f-71eb17b3492b | -5.54399 | -44.32788 | 2024-11-08 03:57:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05186b66-5c6d-3c39-9b35-8884659e24c2 | -4.50884 | -45.70128 | 2024-11-08 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5d3b891-6d00-39e5-ad7c-13529dfae40b | -4.00829 | -44.83204 | 2024-11-08 03:57:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5593caef-d1bc-3438-a923-8c7736cc8f43 | -5.73644 | -42.00605 | 2024-11-08 03:57:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b1d9d70e-17bc-31e1-aa43-eb3f1e093acf | -3.97157 | -48.17883 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1c652f81-3176-3d00-90bd-ccc2c7cc9277 | -3.96216 | -48.17109 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2ee58983-96de-3c64-9744-a5b1b3f3d4a8 | -3.59605 | -45.20308 | 2024-11-08 03:57:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d6f36d3-1f7b-3c8a-8337-a3b71f24e2ae | -3.5432 | -44.96808 | 2024-11-08 03:57:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11e5f907-c1e6-3d86-9783-15585cfb8317 | -3.74638 | -52.10313 | 2024-11-08 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 335a4f97-6ec6-3743-be9c-05de9d3d4102 | -5.48226 | -42.08027 | 2024-11-08 03:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43e1b43a-9fea-38de-bbe6-b05cf848cadb | -1.64543 | -47.82411 | 2024-11-08 03:57:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 444ecae1-e9c3-3f06-a788-c96f1ea069aa | 0.03362 | -49.43882 | 2024-11-08 03:57:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 820c20e3-2070-3ec4-8a07-bc054646b922 | -3.95335 | -48.15981 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 850fdc98-391a-36ce-bc7d-16c103192d7d | -5.17412 | -44.23008 | 2024-11-08 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4ce1d49-fbfa-3024-b2bc-e4c6764f1746 | -4.51531 | -45.68941 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 66e9a2d5-c9e5-3788-8f41-70abea43a9b2 | -4.61234 | -49.58402 | 2024-11-08 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README15.md)
