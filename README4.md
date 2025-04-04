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
| cc160fbb-fe55-3f1c-ad2a-0091b61dc87a | -30.15022 | -52.02731 | 2025-04-04 04:25:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 50758377-4f16-339b-bb03-c0a1ac4a521e | -30.62351 | -51.86186 | 2025-04-04 04:25:00 | NPP-375D | CAMAQUÃ | RIO GRANDE DO SUL | Brasil | 4303509 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 7332cdb8-b622-3563-945b-486f0c9aaba9 | -6.24037 | -47.00877 | 2025-04-04 04:42:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27dff42f-0099-3b6f-88ce-1417ed9cb419 | -5.02311 | -43.60327 | 2025-04-04 04:42:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 241090bc-170f-3d5c-a7c0-a2a2f6a7636e | -7.22977 | -44.77196 | 2025-04-04 04:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5537eecf-67d9-32d0-85f5-f0d9e33ee0c5 | -5.94446 | -45.39606 | 2025-04-04 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9662dbc3-c1a0-3c3d-b1e7-3477aa8f26eb | -6.53809 | -43.09462 | 2025-04-04 04:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ed9f4858-c13b-3909-ab4f-df38bbf64bdd | -10.58129 | -48.51367 | 2025-04-04 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e42bf3aa-a031-3b4c-a58f-6e6b11ca3e7c | -11.26679 | -52.46635 | 2025-04-04 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ff0eb3d-9462-350c-bbfd-05a420f86785 | -12.27681 | -43.52846 | 2025-04-04 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2dd29c17-f92d-34b7-8e06-0094d95bfcbc | -11.26735 | -52.46283 | 2025-04-04 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dee3384-0784-3701-a7d2-b926a91088d3 | -10.34926 | -38.46891 | 2025-04-04 04:44:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aa811251-a72f-3e96-8a7d-b35f7af3e8a6 | -11.02955 | -48.81131 | 2025-04-04 04:44:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22fa2f2e-7b0a-30c8-b332-7db5a5b19ebd | -13.02393 | -45.09376 | 2025-04-04 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c701106e-8696-39f6-9647-50734fad82bb | -11.27229 | -52.47449 | 2025-04-04 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72de9859-0a2d-3687-b4af-81790cd2a736 | -11.26566 | -52.4734 | 2025-04-04 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03a81ad6-c030-3774-bf25-46f6c861685f | -14.12462 | -47.65516 | 2025-04-04 04:44:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90522348-3bd8-3ab9-a296-4900ff77789f | -8.93278 | -44.23432 | 2025-04-04 04:44:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63b09a62-8ae6-34ec-94c1-0b44e39bcc42 | -10.3482 | -38.47387 | 2025-04-04 04:44:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bbbc93db-ea7e-3e76-811c-d8d27ed0bf13 | -15.07731 | -48.94241 | 2025-04-04 04:44:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8781db6-e896-3115-b07c-26459aaa58c0 | -10.34854 | -38.47528 | 2025-04-04 04:44:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1ddf4d7e-2eb7-3956-98f8-6a3d64332a47 | -13.02923 | -45.08946 | 2025-04-04 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c5f2de1-df73-33cc-8381-4566d7128a10 | -11.50351 | -51.95777 | 2025-04-04 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7ef68e3-89e7-303a-a696-c0a82eb0c121 | -13.03518 | -45.08017 | 2025-04-04 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93e4094a-edfd-39e0-b48a-e04682f1e05e | -14.12786 | -47.66098 | 2025-04-04 04:44:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a6170dd-58d7-3146-a14d-7bac972b8f9f | -13.04428 | -53.71092 | 2025-04-04 04:44:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3223dd0b-f926-3cde-86cd-1a116276b5e7 | -12.28154 | -43.53218 | 2025-04-04 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b68be276-0c90-3466-9359-de3ab5feefd9 | -13.04705 | -53.71515 | 2025-04-04 04:44:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43bc1e8b-389f-39d2-a7ac-ea5d62f02362 | -13.03389 | -45.09009 | 2025-04-04 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca729335-54bd-3c74-85d4-61069be2910c | -12.55838 | -45.33461 | 2025-04-04 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59dcec61-4b15-3da5-9b0e-054864a89a31 | -13.03453 | -45.08513 | 2025-04-04 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc2dc8e4-378b-3160-a19d-290377fbe49d | -13.02458 | -45.08883 | 2025-04-04 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7a3ac247-46a6-3723-baab-2b7ffacfe4f5 | -11.26898 | -52.47394 | 2025-04-04 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69f5e38d-1d68-316a-adcb-f3711fd6aec9 | -13.02988 | -45.08451 | 2025-04-04 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b69cc274-1d81-3257-a8ac-f91290b2b299 | -13.04764 | -53.7115 | 2025-04-04 04:44:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 925e61b0-715e-3daa-9179-5eccbd25b5a4 | -12.2772 | -43.52538 | 2025-04-04 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 109a7082-9a67-3b91-b396-7cc72bdfbd17 | -12.5037 | -45.50594 | 2025-04-04 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a22f6e40-d552-3a06-a79c-9fb7716978b0 | -11.03252 | -48.816 | 2025-04-04 04:44:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66d4580e-79c3-353d-86ae-e068124995a8 | -14.12666 | -47.65753 | 2025-04-04 04:44:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9549e262-c7dc-30d7-bb17-a33ebcc15bcc | -14.12861 | -47.65563 | 2025-04-04 04:44:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27c37549-19e3-3650-92cc-ecee2cc449ee | -11.02862 | -44.43663 | 2025-04-04 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc5a93f7-4560-37c8-acd6-247591d2fb4f | -11.26347 | -52.46581 | 2025-04-04 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a8f6814-d664-3fbd-b774-880d6bb1707a | -19.43843 | -54.78122 | 2025-04-04 04:46:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df4a2c72-86f3-30ad-aff7-b574149586a0 | -20.58021 | -56.03332 | 2025-04-04 04:46:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85217517-aea6-3d53-a807-b7472dbd950f | -19.73158 | -49.75024 | 2025-04-04 04:46:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50edcc8f-5243-3735-816f-63b9663c5c5f | -20.56831 | -55.08595 | 2025-04-04 04:46:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7006de44-a35f-39b4-b32f-a78e707fa723 | -19.44509 | -54.78244 | 2025-04-04 04:46:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d496538a-b6a1-3568-a0be-5dc6014d94ac | -19.73224 | -49.74534 | 2025-04-04 04:46:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5495c7a6-d3fe-3484-8533-53a31890557b | -20.57955 | -56.03722 | 2025-04-04 04:46:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e5f9dbb-4e04-3829-95da-e0bf489e2760 | -16.4589 | -47.55668 | 2025-04-04 04:46:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8604b1a7-357f-3fd8-ade0-ba28e9804725 | -20.47669 | -53.67473 | 2025-04-04 04:46:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4ff89cb-7d2e-3aee-9619-1e45506b2515 | -16.45839 | -47.5606 | 2025-04-04 04:46:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34ae1a49-9d82-37b9-b17f-ea2333624307 | -17.15655 | -44.795 | 2025-04-04 04:46:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e8da0d0-be0d-3e5e-a2ce-22a8e275b969 | -17.82932 | -42.62596 | 2025-04-04 04:46:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 544a3c1b-e399-32b9-8a67-062af701efb1 | -22.67567 | -42.85562 | 2025-04-04 04:46:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3e608fc0-7f64-304e-80ba-b18b3904181c | -17.16193 | -44.79265 | 2025-04-04 04:46:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 190a3a52-acac-3796-9fa4-5be3fb580596 | -19.44176 | -54.78183 | 2025-04-04 04:46:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0a45aa4f-2ff8-301c-baf4-64654868e5a4 | -19.43783 | -54.78494 | 2025-04-04 04:46:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aefd171-c592-3075-8fcc-aca800e03ade | -17.1562 | -44.79797 | 2025-04-04 04:46:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 351cfe72-0d69-3792-b88b-6bf289e5e921 | -17.83605 | -42.62475 | 2025-04-04 04:46:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e27151d2-2101-3dd4-8faa-6096e5667e0c | -17.83562 | -42.62886 | 2025-04-04 04:46:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c31f919-c868-3cc1-8b39-db4d573f96e5 | -22.67607 | -42.85074 | 2025-04-04 04:46:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0a96a42b-4212-3cf1-bc2b-a7b75699ee63 | -17.83513 | -42.62687 | 2025-04-04 04:46:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 39ad2878-a78a-353d-9850-52ce4f13b41b | -16.45477 | -47.55605 | 2025-04-04 04:46:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e93aa4fc-d813-3077-bc00-730850322362 | -20.61788 | -56.08094 | 2025-04-04 04:46:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c020eae9-43e1-3ea6-aa35-210a87725ba5 | -13.72204 | -58.67652 | 2025-04-04 04:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 324ac0cf-af4a-36f5-ac34-6c804c9741db | -19.44449 | -54.78616 | 2025-04-04 04:46:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3f56d0c6-4717-3a61-9d5f-1c32eb595599 | -17.82981 | -42.62795 | 2025-04-04 04:46:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a7ad4305-30be-3f1e-b628-edfd02da9604 | -20.57681 | -56.03267 | 2025-04-04 04:46:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02e89fbd-ba8b-30b6-8d50-f9ac24784977 | -19.44116 | -54.78555 | 2025-04-04 04:46:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1da28450-ff83-3c86-9f99-fecb48ee1d27 | -17.15691 | -44.79203 | 2025-04-04 04:46:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 859bf71f-8754-37e5-a4de-7769dd692592 | -30.62687 | -51.85964 | 2025-04-04 04:51:00 | NOAA-20 | CAMAQUÃ | RIO GRANDE DO SUL | Brasil | 4303509 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 9ed7bd9e-e92e-31d8-aeff-14f39e336226 | -8.1034 | -43.11552 | 2025-04-04 04:59:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 1b0da3a8-49a2-3903-a61f-b2a0b5245419 | -10.34639 | -38.47205 | 2025-04-04 04:59:00 | AQUA_M-M | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f1e97d30-6b6a-38bb-829d-83d38447c2c2 | -8.1156 | -43.11734 | 2025-04-04 04:59:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 697e964b-3320-3e03-9370-37559647cbd9 | -13.02997 | -45.0791 | 2025-04-04 05:01:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| dd3f5686-11d7-388c-833f-a90316baf6d8 | -11.26893 | -52.47347 | 2025-04-04 05:36:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b81d7c24-0477-322b-b0d4-543984965ad0 | -20.57863 | -56.03795 | 2025-04-04 05:40:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a0281e1-546d-30a2-8f1d-5101f3acc763 | -19.44398 | -54.78318 | 2025-04-04 05:40:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 17.0 |
| dcae0f23-ab65-3740-a9ad-534d4f2d6a21 | -20.57903 | -56.03358 | 2025-04-04 05:40:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed9db7a7-daf1-382b-944b-b487bbb408bb | -19.43776 | -54.7827 | 2025-04-04 05:40:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41096d44-ab40-3866-8474-942d410a8993 | -13.0533 | -45.0529 | 2025-04-04 11:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| ed6e96e2-780d-3207-9281-7a8c2d5d8bdc | -13.0533 | -45.0529 | 2025-04-04 11:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 4bd10de9-a3b3-3b4c-85de-f9b9b32dcd55 | -13.0533 | -45.0529 | 2025-04-04 12:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 7a12149b-bec3-3b70-8159-0b499b644137 | -13.0533 | -45.0529 | 2025-04-04 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1326cc28-0eab-3d77-9545-639bb325d054 | -13.0533 | -45.0529 | 2025-04-04 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 1bf88afa-7a54-3f60-9e70-adfac76c0f79 | -13.0533 | -45.0529 | 2025-04-04 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| efbb4fba-f78d-3f4a-8856-82e7bea14772 | -8.1078 | -43.1175 | 2025-04-04 13:10:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 49ab2cbe-073a-303c-8903-24871a95d9aa | -13.0533 | -45.0529 | 2025-04-04 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6ece80ac-904a-39da-938f-059b1e39764c | -13.0533 | -45.0529 | 2025-04-04 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8f536e8f-1cdb-371f-b823-aa9d87f25784 | -13.0533 | -45.0529 | 2025-04-04 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| db943766-c037-3162-ac1f-564443beb506 | -8.1078 | -43.1175 | 2025-04-04 13:50:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |


