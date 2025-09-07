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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14529ac8-4fcc-3ea2-9329-3ca1992933c1 | -7.29139 | -39.21876 | 2025-09-07 03:30:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 71fbefda-0bfc-39c3-9401-4e2fd1b5d689 | -8.30725 | -44.97946 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee4eebc5-4103-3a5a-b7f7-13df7623458a | -8.3061 | -44.98558 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e04ae5c6-6fd7-339c-96e5-4b97126baee2 | -5.86181 | -42.42256 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 08570e20-675a-3362-8a37-249d5ab7369e | -6.53985 | -44.82327 | 2025-09-07 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 765f8fce-58aa-397f-b3fb-6b74f1ec3621 | -6.1359 | -44.25336 | 2025-09-07 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a9c4b168-13d9-3e3c-9d4e-7422e0d9cf38 | -7.29064 | -39.21609 | 2025-09-07 03:30:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c513948f-a1ee-32a3-9ede-d08cbfaf69d4 | -8.30798 | -44.97561 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c336afb2-0ff1-35d6-a934-6b5e11ac18b3 | -6.24464 | -43.51389 | 2025-09-07 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c5a1a99-14ad-3a74-a9f1-342431f9651d | -6.19396 | -42.63771 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 30693c60-7bcd-3437-b936-94965ae04e0d | -8.29558 | -45.39216 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b476ef0c-e5d7-35f3-a99d-8499b57b8e43 | -6.20125 | -42.63045 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b9e4f528-c0a4-303c-8804-adf8436a9529 | -5.86107 | -42.42664 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 69d3369b-ac20-321b-a1a1-0fdcb67d2269 | -6.1845 | -45.42786 | 2025-09-07 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| b18a4356-ff1a-396a-b7b6-8416a087d761 | -6.18411 | -45.42767 | 2025-09-07 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| d1896712-e77f-3a9c-867c-eac05fc8d297 | -9.39235 | -40.30437 | 2025-09-07 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5093ea82-4c4c-3a8d-9f57-96d03880cde9 | -7.24551 | -39.17983 | 2025-09-07 03:30:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3ecb393f-d89f-3c2d-a506-d147fba0e9c5 | -8.03338 | -44.03737 | 2025-09-07 03:30:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2a678df-18aa-3149-a724-ffe93e32a642 | -6.14962 | -44.25085 | 2025-09-07 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6224f6e1-9cf6-361e-9745-99467c97b525 | -8.01891 | -45.49952 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 81cecd24-9423-34e1-b74e-30aabac2d233 | -7.34659 | -44.31626 | 2025-09-07 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 35992798-44fe-3d02-8497-8e06bed5b566 | -7.80921 | -45.43956 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30ec1b99-bedb-3b58-ae93-31ac394f88c6 | -7.71249 | -44.72046 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 59237ba5-296a-37b0-9d91-8e95e0ea6247 | -6.24221 | -43.2794 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 141ffb26-6470-3ae0-b48a-3a7f0973b927 | -8.29672 | -45.38617 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb86efac-d165-366d-a0d7-405c3170efba | -7.60722 | -44.66944 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f5a0861d-f43d-349f-b98c-167f05be9c58 | -6.21798 | -42.63735 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7e37f16d-ae4f-38de-9cac-419250633285 | -6.19975 | -42.63886 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 20b5e5b3-98ef-3d5f-99a9-62a44ab9be45 | -7.01688 | -44.9547 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a41c41de-bf71-3a12-822a-1f9cd3bb3e7e | -8.15435 | -44.86574 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44f45170-ab48-3a59-86d0-3355c6fe6b6f | -6.20555 | -42.63988 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eba874dc-e4f3-3250-9979-30a0935b2d48 | -7.19428 | -44.72966 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19518a5b-d5d3-3e7f-8b6f-b209a679f76a | -7.71875 | -44.71932 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a6234d19-c268-3a03-9e95-8ea1f71cd258 | -7.84578 | -44.93711 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca67b37e-ea7e-344a-8526-30bd0dc4e516 | -7.33003 | -43.93833 | 2025-09-07 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6bfc487-8e7b-3a9d-b0a3-67f818cebe70 | -7.75413 | -44.00922 | 2025-09-07 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76709354-f3f5-3bb0-86e8-943406bfbffd | -6.22705 | -43.57558 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eed72378-af3b-362a-afd0-da16d84b1546 | -7.19979 | -44.73511 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f8753299-f012-33d1-be9d-498fcb6a6063 | -7.01582 | -44.9603 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f136ae2-7e60-3619-8c7f-66fbb06e1e53 | -6.13688 | -44.24794 | 2025-09-07 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 14ae3fd6-d818-39d0-852a-05aad8dab7bd | -8.02274 | -45.44392 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 17850087-1f7d-32a4-a306-c9620322bb71 | -6.23251 | -42.58919 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8fd3d1ad-00b8-3905-8f8b-d93645336eb3 | -7.71767 | -44.72519 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0b2f0173-052a-3ddf-b983-774cb77458bb | -6.22036 | -42.45741 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a9273de9-26c1-373b-954f-5e5eee32170d | -6.52493 | -42.42034 | 2025-09-07 03:30:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ed5e561c-678d-32c4-a9af-a8a3e5c0d0ce | -4.17196 | -42.02921 | 2025-09-07 03:30:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 45999636-cfcf-308e-bde3-9fe2db8f2909 | -7.75311 | -44.01091 | 2025-09-07 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b2ace1d1-6878-37f4-a9ee-b47c0d6e2eb6 | -8.68733 | -45.30359 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 346a919d-1309-3b8d-9312-03b07af1fe62 | -8.31355 | -44.98163 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 925effb6-7fc7-3d10-97db-d82471ffbcda | -7.81455 | -45.43284 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d47dfdc8-102f-365f-8d6d-a8a36cbee81b | -8.31426 | -44.97783 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5c188bd-f15c-3626-9372-e55a8a300381 | -8.6875 | -45.31102 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b5f3330-0175-378b-a290-5e6174cb9355 | -6.54434 | -44.83578 | 2025-09-07 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c1cd7ed5-ef90-3c7e-9c4f-f1259bb5c8f4 | -7.01823 | -44.95918 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ee0f53e3-590f-303f-ba3d-9924b0d2a895 | -7.34433 | -44.31413 | 2025-09-07 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90356517-adff-30a2-86aa-63e1a5152aa4 | -8.68093 | -45.30981 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2024f5aa-4725-3087-8b9f-85e5744e2f56 | -6.18298 | -45.43391 | 2025-09-07 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| ce27dda1-a73d-3d4e-aeed-5c10468d7537 | -8.02006 | -45.4936 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1af041ba-79b8-3529-9ec6-6a1f91d70afa | -8.4843 | -45.17897 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7a9fec76-e6da-38e4-a0de-4b7e31771067 | -7.71353 | -44.71507 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 935e211a-88c8-3d84-a52b-1ab0b3d971fe | -8.3083 | -44.97384 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38181ad9-2126-31b3-b5bc-e6d61fd6bf29 | -7.01717 | -44.96494 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c2f8c2f-308f-30b7-bb2b-7a6c17be142a | -6.43086 | -43.53291 | 2025-09-07 03:30:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 117bef14-63e5-3fbc-8b61-30e20912d81e | -8.68616 | -45.30958 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1e665334-489c-31d6-a17e-f55a6b704178 | -7.74785 | -44.00873 | 2025-09-07 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49d71863-b607-3cbe-8ba9-34581f557075 | -8.48297 | -45.1803 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a120e12-8fe0-31a8-a53f-92dfe02c3102 | -6.19702 | -42.62067 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 73ee2fbb-6820-3f4d-a71d-8f5a6d6f2032 | -7.74683 | -44.01042 | 2025-09-07 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d46f7dbe-1d7a-366f-9dbe-1bac29b6dcf4 | -6.20097 | -43.58319 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 51963ae6-8962-37c7-9d08-7388bcac0461 | -6.191 | -45.42883 | 2025-09-07 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 87bc10da-f289-3dda-8fbe-f6b5e00aa56a | -7.81045 | -45.43314 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 491fca6a-13d5-3a34-a2be-b08ccd7207be | -5.86075 | -42.4233 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e2fab690-b3eb-3c75-ba54-3a7cc5112be6 | -6.15451 | -43.17958 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 21fd48d7-8973-3b09-945f-6164e9e6fbb7 | -7.28684 | -39.21805 | 2025-09-07 03:30:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 86afeab0-1ea7-39ba-b501-2e1d97feb478 | -6.19984 | -43.58524 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f2f0042-b260-3256-bd64-4213ed641103 | -8.10938 | -45.31562 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e51593e-1422-3982-8408-573b1d62745f | -6.19806 | -43.59489 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c562f68-12c8-3813-979e-ac5b77e91cc9 | -8.30686 | -44.98136 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 20acc17c-0c9b-3313-9fc3-7d9f62a7161b | -6.52563 | -42.41632 | 2025-09-07 03:30:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ebfda79-34c5-3029-925d-3687992564d9 | -8.43774 | -45.03408 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6093928d-8ffb-3c82-b711-f29eca0a052b | -6.21097 | -44.39326 | 2025-09-07 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f48ce08a-bdf1-3e5f-876e-cbccb349cd70 | -7.32403 | -43.94187 | 2025-09-07 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 894fff69-0696-313f-9b26-99eaa903736d | -6.54191 | -44.81223 | 2025-09-07 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f166b0a2-4d3d-320e-828b-e95530229c7a | -6.13859 | -44.23856 | 2025-09-07 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9610db38-46a6-3c38-a6f8-388a017cec32 | -6.14513 | -44.23902 | 2025-09-07 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 398e9e7b-337f-316d-9776-8e7aee2fd74f | -5.55283 | -43.06429 | 2025-09-07 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71a29764-d041-38a4-8aef-1d945f07df78 | -8.08531 | -44.80508 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d4c8136-c4cd-3232-a944-2974956ea08c | -7.25465 | -41.88957 | 2025-09-07 03:30:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 793e6f2f-a2a0-3006-a618-bb99f02f865d | -8.45853 | -45.03075 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b5b06a3-af66-3820-8d93-a2aa3bad846b | -6.1857 | -45.4215 | 2025-09-07 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 918351cd-de5b-3866-af11-e3fd45600096 | -6.23612 | -43.27862 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 79b484a3-fb89-3be6-a965-cf6d8dca54f5 | -5.55472 | -43.06445 | 2025-09-07 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3599f5a0-762d-3c47-b26a-e0fc39391603 | -8.03951 | -44.0386 | 2025-09-07 03:30:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1794c743-7efa-39d0-bb33-5af5b0c900ac | -8.01952 | -45.44445 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aa92c423-0696-3d6b-ae99-56ae283487e1 | -6.16339 | -44.24794 | 2025-09-07 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92ab603c-fc8f-356e-9958-8bacd57fbde0 | -5.75898 | -43.1242 | 2025-09-07 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 12a1abed-877b-3b53-9fed-562874ace447 | -8.45753 | -45.03598 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3117cf4c-61fa-3f6e-b8b7-57f4dbdc0120 | -8.14879 | -44.85985 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc68176d-0607-37bf-a4b8-fcaf1e7fc112 | -6.53666 | -44.84036 | 2025-09-07 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f249bb1-de32-3657-a211-d065ff97c87a | -8.11348 | -45.31737 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README18.md)
