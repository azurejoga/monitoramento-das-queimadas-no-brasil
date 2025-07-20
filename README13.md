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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdd0d083-89f7-354b-afcd-e961da8a556b | -8.06993 | -50.09865 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 547c3c67-a666-3236-aab3-d65fa57731fb | -3.93842 | -48.09275 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d1fcd8-8e7f-3e30-a756-e90484b5aa7a | -7.23406 | -44.12706 | 2025-07-20 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6dfac6c-d10a-3d83-ac11-6ba9b2346524 | -7.70613 | -47.29279 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2b1b48b9-269e-324f-9eba-2346ac3d8d70 | -8.36007 | -46.64462 | 2025-07-20 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ab23c9d-307d-3066-bb0d-a2f034a32f54 | -3.3163 | -49.04519 | 2025-07-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4ecc8f5a-b97b-3927-837d-a99fdecb4033 | -7.54717 | -45.37061 | 2025-07-20 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08f7ac82-434f-36e1-8e50-67bae282be88 | -3.12294 | -47.01259 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58767e57-92a8-3202-8c66-1b8792f29962 | -3.51268 | -47.21026 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3168fa3f-065c-381e-bb2b-4916910d325d | -7.71023 | -47.28939 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09f900cf-5e1a-3105-bbc3-3ad863bb0697 | -4.58587 | -43.31031 | 2025-07-20 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50015c88-973c-373e-bb95-f68bcd278a50 | -7.48521 | -44.70752 | 2025-07-20 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5d3918d-5eeb-33c4-bede-bf0ed8909597 | -4.07894 | -48.0387 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96ad358e-349a-3488-a3a2-18e94efb6b60 | -2.93925 | -48.05084 | 2025-07-20 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e70920e-34f3-3e4a-bc9d-de9d2a58a5c8 | -4.12571 | -47.6578 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54d83ad1-65e1-3b97-9a5f-0de19c1cbfc9 | -9.54401 | -40.33086 | 2025-07-20 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 19e8bfd5-901b-3cbb-8910-41174c17b4c1 | -7.70321 | -47.28835 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d52047c7-37c5-32c5-9579-65dcd07d55aa | -4.86603 | -45.04834 | 2025-07-20 04:38:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5d32535-e29a-372d-a986-96574eb1f85c | -7.26712 | -60.12124 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da6b32f2-cbe7-35b7-8fe7-9689d8da7c86 | -7.26373 | -60.11407 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4d9f987-62f0-3440-9e63-dd278ecfbce6 | -7.26224 | -60.12212 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac4b9b87-1d6d-35ef-8ab5-7bd16839e828 | -6.71571 | -47.79719 | 2025-07-20 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b54301c-cbe6-37df-9be0-deda5d19cf8f | -5.34779 | -45.26854 | 2025-07-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f13d4d3c-5f9a-343c-933d-418ed6444bf8 | -3.11613 | -47.01154 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21575d76-f0f9-308c-a3c3-ff70136aebea | -8.63803 | -49.42303 | 2025-07-20 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39f4193a-55e0-36b2-9197-f641e36d8d7d | -3.10989 | -47.00683 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88e4b5a7-b91d-3ecd-a469-81ae170668b8 | -5.64988 | -44.3555 | 2025-07-20 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd92641b-8068-3e1d-942a-d7ca09a57b3b | -8.00492 | -43.68348 | 2025-07-20 04:38:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00d5771c-20c1-340a-be54-de5ebdf50de8 | -3.58947 | -47.52465 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e06c1ce6-4774-302b-8dc9-0dfb9f2937ff | -4.07785 | -48.0457 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed754536-8f75-3c82-a8e3-2173acce18cf | -4.5938 | -43.31562 | 2025-07-20 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6f4978b7-cd78-3f6d-a30e-f5c0ead19045 | -3.5155 | -47.21442 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03d03fbc-620b-3ea0-94af-dab77043982d | -6.92505 | -44.8373 | 2025-07-20 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 026fc157-9f97-3782-911d-f08bae2925d5 | -5.87043 | -45.21462 | 2025-07-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6aa12266-e464-31f2-8924-60e1431ecb01 | -2.90878 | -48.24467 | 2025-07-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c41c6050-b278-321d-b249-61e70718774b | -4.58528 | -43.3143 | 2025-07-20 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 842affd1-1acb-3c9a-a5a5-eb59aa8bcf92 | -6.032 | -51.66105 | 2025-07-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0012d5bf-bf74-3ca8-ab53-90cf29030d62 | -3.13316 | -47.01416 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a383b93f-3bd1-345a-a62b-5108ec159217 | -3.10931 | -47.0105 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c510144-6cb9-3df2-a0bc-68b926d97e80 | -8.07654 | -50.09969 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c6c4343-22ee-3612-abaf-2d9b4f9d8582 | -7.05943 | -44.86795 | 2025-07-20 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 139c49f4-7b62-30e3-8c05-8b42689feecb | -3.65095 | -48.32209 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc8d2e44-990e-39db-a152-3e64d9af5cf3 | -7.2335 | -44.13085 | 2025-07-20 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 748580e6-bb61-3e67-a854-a2cd99bd9459 | -2.90823 | -48.24812 | 2025-07-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3f5561c-5743-326f-baee-3706f8a4f1a9 | -6.83884 | -47.86114 | 2025-07-20 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a0d28e2-d19d-3113-a2b2-c99804096e4c | -4.12704 | -47.66177 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52b0672e-ecfd-30af-a2c0-7ca355a4c0c6 | -5.62597 | -42.30597 | 2025-07-20 04:38:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4092ebd5-3041-3b46-b2ef-d1b479a02799 | -7.26869 | -60.11925 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75927018-281b-39d6-94aa-89d12346e05b | -6.92456 | -44.84063 | 2025-07-20 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58005dff-d2a2-3896-b99f-ac946584334b | -7.48818 | -44.71539 | 2025-07-20 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a8552a5-6c87-3f69-8acb-91e9c4bc051b | -8.74605 | -47.7302 | 2025-07-20 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c2b33fb-99ef-3cb6-a493-894f2fa59233 | -3.79263 | -41.00095 | 2025-07-20 04:38:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c207e905-caf5-3473-ad56-9038747a8124 | -7.42317 | -44.28106 | 2025-07-20 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 595b9d50-000e-355a-9602-b0c8db968543 | -3.83008 | -47.74035 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8daa335e-7c12-3436-97cb-5d4a523de329 | -7.6291 | -44.29141 | 2025-07-20 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b22b42bd-5fd0-3306-b3c0-0fe7c171818e | -7.25572 | -60.12532 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82a68173-80c3-3532-bb4a-4bae8bead78b | -4.96516 | -43.23019 | 2025-07-20 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e02b47ef-4dd6-38a5-9a8c-a4edfe15c06a | -7.47182 | -49.45323 | 2025-07-20 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3f8a463e-e2ba-33b1-86fe-330c5eecd4e2 | -3.13033 | -47.00996 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 244bbbb9-3ede-3270-8950-f741f2a1ec7d | -7.4226 | -44.28495 | 2025-07-20 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6377d31d-5a44-3f7d-a7b2-ba0360178d1c | -7.15367 | -48.20386 | 2025-07-20 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12aa40d2-af63-3df3-aa81-390b1643e9be | -9.53888 | -40.32629 | 2025-07-20 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3b27137a-999e-311b-996d-9a816af1672d | -3.11953 | -47.01207 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5803d025-76b1-36f4-8a4b-bc665651199c | -7.70203 | -47.29617 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f196d70b-8915-3869-bba9-f99dc0fa7b2a | -4.12515 | -47.66137 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48e873ef-3be4-3182-b8c0-ea79485a49aa | -7.25569 | -60.11893 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 233eeb28-8564-3413-bd97-b78a777d8914 | -9.63206 | -40.60409 | 2025-07-20 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 17bf6cf4-8545-3988-b569-ae55128fd265 | -4.12475 | -46.32693 | 2025-07-20 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3d9840c-0de5-37ee-a486-33a1d24c6df3 | -6.64778 | -42.88023 | 2025-07-20 04:38:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e7015afb-7922-3032-acb9-d37801a8540b | -9.27281 | -48.22407 | 2025-07-20 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdb24a07-b3c4-33d2-b386-03f1de472556 | -8.0782 | -50.11061 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73f93775-eda9-32e3-a160-82df740fddd0 | -3.10591 | -47.00998 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cf17b75-5ae0-3313-ada1-dda84c2242f7 | -7.25652 | -60.12103 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15caea76-2d44-349b-ae6e-5a918ce39b7d | -3.5861 | -47.52414 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 06a902b8-edaf-3e2b-a1f9-7ebf56f1ac27 | -3.12975 | -47.01364 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ed58e34-54e9-3032-87b2-6a7c8a77f6bb | -8.35279 | -46.64346 | 2025-07-20 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bfe1dee-1c60-3c39-8644-88886e557fb8 | -7.26066 | -60.12431 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba0cc83d-1aa5-3045-9163-6c789a110b24 | -3.13373 | -47.01049 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f545789e-a3f5-3e8d-b5e8-0fc89ade049e | -2.90932 | -48.24121 | 2025-07-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e364d128-bafc-30a7-8d71-391ed33c6978 | -7.26684 | -43.10104 | 2025-07-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4c1c249c-dc02-3c49-91f1-795c4a75f0ad | -3.03662 | -47.8629 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 2aa65e83-0514-3fa4-b026-82c971822346 | -5.32538 | -55.94401 | 2025-07-20 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaab1fed-5f43-3a6c-a287-4b90336e3c68 | -2.91594 | -48.24224 | 2025-07-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75a0cdfa-ebeb-38ce-9701-e428f9bd9e4a | -3.90966 | -42.41045 | 2025-07-20 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| dda2be4b-b25f-3bbb-aafd-84ed6ee95e01 | -3.13656 | -47.01469 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12acb4f1-209a-3378-b6b7-1797fbbd7657 | -7.26213 | -60.11599 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9055cf9-70e9-39dd-b10e-94597f94a054 | -8.35943 | -46.64892 | 2025-07-20 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 939401e2-2a98-3414-a510-35b6455b6ba7 | -7.26144 | -60.12643 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8d4a346-d62a-3db5-a2a9-7f7104c1d7cc | -6.14712 | -42.91828 | 2025-07-20 04:38:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 150d4b68-8a00-3883-85a8-58997a9a3d3b | -5.3485 | -45.26389 | 2025-07-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8996c5b-800f-35da-84e6-390c376fdf9c | -4.12814 | -47.65461 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11b19593-04ac-3d4c-bb2b-48fb5518475f | -3.11272 | -47.01102 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 687cba12-9f9c-3593-81cd-7e0bfeef385b | -6.34383 | -44.04472 | 2025-07-20 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b0b0237-13c8-357c-b123-9fcae08c6df9 | -3.54334 | -47.37771 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 505cca35-7044-30c9-8737-0e7711d27108 | -8.08536 | -50.1082 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 187ad6c3-480a-365a-b39e-6b6d82206036 | -5.08879 | -48.4245 | 2025-07-20 04:38:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| aa2ecb80-ab8b-39af-8527-8b416adf47ef | -3.32015 | -49.04226 | 2025-07-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d098b49-d7aa-3de9-836d-710f0852e60a | -3.03275 | -47.86586 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9eadfea3-9e1d-3f05-a75e-57816e6d3b4b | -7.62965 | -44.28765 | 2025-07-20 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03382928-942c-3cb5-928f-77e09ce97d8e | -3.91863 | -42.4118 | 2025-07-20 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README14.md)
