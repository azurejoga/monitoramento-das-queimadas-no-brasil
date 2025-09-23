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
| 220d1087-5fc2-3ab0-9d46-7fcdfcea1de1 | -7.29005 | -44.1534 | 2025-09-23 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 658f2f01-5aa6-3026-ba8a-72d11d02d633 | -6.61081 | -44.60823 | 2025-09-23 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1311319-f007-3da2-a72d-71b4544e7a6c | -11.45019 | -43.53165 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43a368ce-328b-32ce-8553-666a791b2b8e | -7.36092 | -44.54611 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d244da8b-4d60-3db2-9493-f9e5635b130d | -11.41128 | -44.93454 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 862ffaf1-190b-326d-971c-e31d12930d64 | -7.07112 | -46.19693 | 2025-09-23 04:19:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e08028b-2d21-3c29-bc91-c5b1f9a84350 | -6.42643 | -44.16092 | 2025-09-23 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 226a99f4-ca0e-345c-88a5-cd1f902f752f | -11.48944 | -43.54451 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdde954a-bc52-3862-b78d-91f4194435a5 | -10.96475 | -45.70721 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4df9dbf3-eda3-3f59-9f01-b0949c8ac208 | -7.03835 | -41.99507 | 2025-09-23 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a5a86464-c0f9-3834-ab52-b41534b2773a | -7.76814 | -44.72073 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be716a69-036c-3664-a3dc-b946cad350c2 | -6.25018 | -46.76343 | 2025-09-23 04:19:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 299708d6-9ae3-3966-aa4a-6de375a92b97 | -6.71834 | -47.20683 | 2025-09-23 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b624acb4-2a69-398d-b603-42a4ed44dd13 | -11.41794 | -44.93561 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7eb50d44-451e-3425-8953-4a032647346c | -6.25811 | -45.33429 | 2025-09-23 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e2eb9f2b-e91f-3a98-8e6f-0e70ee98c462 | -7.79547 | -46.19925 | 2025-09-23 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd335513-10fe-3029-b8b8-c39dda3cc8a9 | -11.41406 | -44.93861 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a681f51f-bdda-3625-83b9-cca28dee3c6b | -8.79799 | -43.02468 | 2025-09-23 04:19:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05b54522-1119-33f6-8a8e-e71f574031ad | -9.59125 | -46.44088 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a522e121-e70b-3e9a-a93e-c141cc1e8a3e | -11.4063 | -44.94465 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ab6452f-5cdc-3e37-aa36-2573f4c65297 | -7.03864 | -41.99622 | 2025-09-23 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 935581bb-212a-3f3c-b2ad-bf1ea7e7e6fe | -5.64448 | -51.46576 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 113947bd-6a53-3627-bbe7-5618ccd144f8 | -10.30541 | -45.23519 | 2025-09-23 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4e6ce05-03a0-3bd7-ac4d-4ce5e43811c6 | -8.13766 | -44.46523 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d2512e48-17b2-3229-a33e-5ccf6f897751 | -7.59761 | -44.44427 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf26537a-f704-3cc4-8228-3cadec99080e | -7.04157 | -42.00077 | 2025-09-23 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9078f522-772a-3589-a557-beda83b81814 | -9.15035 | -46.66044 | 2025-09-23 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3438dcc0-5254-3e46-9215-3a7ee0e567e7 | -1.48198 | -48.92883 | 2025-09-23 04:19:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8158f7b3-69ce-3939-a3da-c91f24a70d6d | -9.31324 | -43.36316 | 2025-09-23 04:19:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c1452e28-645c-398c-a3b7-a6fcdffb3396 | -11.44501 | -43.51902 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15663e2f-6ccf-302a-831d-581cfe7a3e42 | -8.54477 | -44.92215 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0f232cd-e9ee-3d58-8df3-3e4cf62a883b | -11.40297 | -44.94413 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1407cc4-004d-3101-94fb-37b211868971 | -7.89128 | -44.02075 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2380a09-8fbc-33da-92f0-169bbdb80cc6 | -11.41908 | -44.95024 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c39c080-3b9e-3bd5-84d8-2c3b664ae13d | -7.89073 | -44.02428 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e5bd8c3-a547-39d2-b707-b11cdcd9312e | -14.00873 | -42.47267 | 2025-09-23 04:19:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ac550b9-1637-30a4-a5a6-0f860f137b7f | -7.05986 | -45.05535 | 2025-09-23 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 349340c2-97b4-3073-9141-a039ab53a1cc | -12.4479 | -45.09801 | 2025-09-23 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b22b9ed-0012-3bff-a6df-50963bdc1cb7 | -8.92501 | -44.46714 | 2025-09-23 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a077da26-7341-312b-9a44-00cd1b85f99e | -11.02644 | -45.89656 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bc9d9fa-48df-3645-9f99-9cd89ee78bdf | -11.91816 | -43.43127 | 2025-09-23 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06702ecc-8bce-3d48-92a0-973a5825da1d | -10.82964 | -44.81363 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 027ce633-5120-3126-b9b6-3da1be7ad5ff | -11.60552 | -41.62182 | 2025-09-23 04:19:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4dea40b7-88f4-3056-9596-08dd7b3cf01f | -11.02424 | -45.88902 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| abaa22ab-2862-3a1c-890f-86b835a42a23 | -7.88127 | -44.01919 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37520607-f664-3bde-9964-7f5157e1ac1f | -12.96854 | -43.52665 | 2025-09-23 04:19:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 09e4ab12-e67b-31a1-86cf-66125bae166b | -7.89018 | -44.02782 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc29ce67-9683-3ce8-b2c2-eef2983c20e6 | -7.88017 | -44.02626 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f533e260-a294-387d-a5d1-d0834fea9f5b | -10.00313 | -46.28532 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc3adc26-cffd-34d8-b71f-59ce20d36192 | -11.45078 | -43.52779 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 619d86f1-32d0-3bb9-8563-386e04abb5fd | -7.04218 | -41.9968 | 2025-09-23 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 81e9337c-aa42-3a15-96a2-e0c2d3c69465 | -8.95573 | -44.48666 | 2025-09-23 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb884b67-448b-3f87-ba6d-6c2da2cdd269 | -6.33765 | -56.1963 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d148674c-4f9a-3659-b914-8005ef818879 | -8.0884 | -49.91772 | 2025-09-23 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 195bac03-b2bc-3261-acd4-14bdd77d3cb7 | -11.89192 | -41.2697 | 2025-09-23 04:19:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 027b3e65-71bd-325c-81fb-7cc6733ede8d | -7.88406 | -44.02324 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bbf7f272-0bf1-3a00-8cd0-51b6b315ea90 | -11.53154 | -43.61787 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7736450f-2068-33cf-860b-6da3a5f850cc | -8.52375 | -44.96923 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| abcd82a6-d73d-3329-b001-1cc1ede00935 | -6.26143 | -45.33481 | 2025-09-23 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c81b0318-99e4-380f-8959-c7c83bfc224d | -7.16216 | -48.29672 | 2025-09-23 04:19:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d72e4310-ccf8-3630-8789-d79df42ffdd0 | -7.70228 | -44.90215 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6525e176-736f-3281-8028-c57f64fb5799 | -7.79384 | -46.18785 | 2025-09-23 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2390f018-96f3-3f01-8a3f-142c4671d838 | -7.78934 | -46.19454 | 2025-09-23 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cb2d1ce-950f-3ae7-89a6-0da0221f2208 | -7.26986 | -42.99157 | 2025-09-23 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 921832a4-eba0-3b66-9b6c-69dbf23c3c20 | -11.4074 | -44.93756 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b315843-b8ed-3034-96b4-b908fdd83db3 | -11.45424 | -43.52831 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caea1968-db28-3347-900a-71a8f1256277 | -8.52317 | -44.95133 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bcb0279d-7106-372f-b77f-1417ec9288de | -6.71897 | -47.20291 | 2025-09-23 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9660c983-1c7c-322b-9555-29be3218e19c | -6.58917 | -43.59404 | 2025-09-23 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 763ad2c1-ef29-327f-b6f3-34888eedba7e | -8.00157 | -45.71299 | 2025-09-23 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d7640b3-4016-38a3-84a9-d4e6a49b7beb | -6.33144 | -56.19516 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee8a169d-0307-3c5d-8f8a-26bcb676c956 | -9.16307 | -44.61599 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d811ab7e-be5c-3ac8-b6c7-8f072e09dd93 | -6.25755 | -45.33778 | 2025-09-23 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e773719e-0ee4-3569-a807-258ff69ac580 | -9.01457 | -48.03563 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83cd21b0-d1ae-3cef-a28a-b5ac093348a2 | -7.16749 | -44.437 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 522260be-a61f-33f6-ac2d-e56cad66df05 | -6.25478 | -45.33377 | 2025-09-23 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77712265-afc2-30e2-8724-f3a4d8547810 | -11.45888 | -43.52108 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d033773e-0c29-3b1c-ae97-bcfa335c63d0 | -6.33855 | -56.19136 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9f4b884-47f6-3501-984f-eead615e63a2 | -6.58972 | -43.59051 | 2025-09-23 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fedc37d-150b-3e72-9aa6-78d58b60199b | -10.33778 | -46.06144 | 2025-09-23 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a151d094-7213-3945-8d53-6227e8052ec8 | -11.51941 | -43.24474 | 2025-09-23 04:19:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5ed77e5e-3fa9-371f-86a6-a696ec2ba37a | -7.08042 | -46.35438 | 2025-09-23 04:19:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec440c8b-66e6-30de-8beb-8b812843e770 | -6.53465 | -49.49715 | 2025-09-23 04:19:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7453f40f-7130-3ce6-b6ad-89a57875d52d | -9.00948 | -48.02223 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bf191d2-bf1d-3322-816e-f25bbe1dd3b0 | -7.36146 | -44.54265 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4636cdb0-2914-36c6-bd22-266f3cba9d2e | -8.37922 | -44.7001 | 2025-09-23 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7c87c13-0fc1-3ce1-b2bf-a02b62627d3d | -11.4479 | -43.5234 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82f273c6-606b-3b11-9437-62a3073b1c95 | -7.04189 | -41.99566 | 2025-09-23 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| eb02feae-9a90-3c73-9298-144fe1141d75 | -11.11085 | -43.19843 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b81689e-e74c-368c-8aeb-e4a7258bd9c1 | -11.46118 | -43.52934 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69874845-0a1f-3301-8236-c26ec5de84dc | -7.89462 | -44.02127 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bf21102-32a4-3baa-a75b-06d00f6b20c4 | -10.31876 | -47.86187 | 2025-09-23 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e40c0672-4285-3ce5-9035-69d62cfba616 | -7.05733 | -44.53337 | 2025-09-23 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 907dd37d-0f0d-3a00-a472-e83343541456 | -7.88351 | -44.02678 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd275279-8bc0-3d32-bc12-94b3119c1482 | -11.02257 | -45.89953 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7963bc14-cd93-3dcc-bfb7-3a3faa8121f4 | -8.66825 | -47.07705 | 2025-09-23 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9cadedc8-06b1-3b39-ba45-86adf2d64832 | -7.62791 | -46.547 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb6a71c0-7a19-32db-8b10-5a51929869c7 | -7.11464 | -44.49268 | 2025-09-23 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 920315d5-c39f-3b59-8edc-53447bf3fc37 | -9.30506 | -35.69708 | 2025-09-23 04:19:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b85c6f74-d84d-3b2d-a14c-745a49208734 | -13.56129 | -42.22187 | 2025-09-23 04:19:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README15.md)
