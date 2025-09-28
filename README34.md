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
| 375c9158-48e3-3f70-838f-f381b7146802 | -8.2927 | -45.45229 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d995c3f-2735-35ba-802a-52536f62ad90 | -6.26178 | -44.07373 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a827ea79-5277-3cba-9a53-3cfb1171abd3 | -8.16872 | -46.40461 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d9481ebf-04d3-3ee1-b76e-13d1a3c387f6 | -6.18284 | -42.94612 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 75340404-1f70-35a8-9227-94c7d1e4895b | -5.81941 | -44.44238 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6a100db2-953e-3d67-8ef5-5216dbffbb61 | -6.16341 | -42.80843 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3c4f4234-59ee-31e9-9385-692d7cc951ef | -5.41752 | -42.26822 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4f707ca1-c59b-3030-8bf0-118d5d5c7a1a | -5.09497 | -46.02601 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e675fc6-015b-363b-86cf-80fa02fc6bf9 | -5.83149 | -45.59359 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dfab9a2a-3485-3c24-a6ff-110b839982b1 | -5.76578 | -42.827 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 92986376-f4e7-33ae-a6a4-61149b145f8d | -6.31142 | -43.46136 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ee08ecfa-3fde-39db-934b-80eab450ebdc | -5.05199 | -45.31775 | 2025-09-28 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f18e4ac-4b06-3713-8100-0d51c6f45822 | -8.50114 | -47.01025 | 2025-09-28 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef8ee9ff-f9de-3f25-8a28-b6618c126494 | -5.70992 | -42.66382 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 342a813b-efd1-3b36-a838-9f2c647ecc88 | -5.80962 | -42.83008 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 70806936-62fd-34c4-a6b6-c014925f8cf9 | -7.8658 | -44.57201 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f2b2849-863d-332f-b1a5-1abf229a0144 | -5.33867 | -45.64462 | 2025-09-28 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6540b91f-cdd3-3966-8614-60ba5fb71a34 | -5.71642 | -42.669 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0bf336ea-4b3f-3761-acbe-248efb9b824d | -6.9001 | -44.75881 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 76ea8dc6-e98b-33a1-8a20-898db9b158ed | -3.83246 | -40.34188 | 2025-09-28 04:04:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 89e8508d-6a76-3bd9-8dc6-fb06f6283012 | -5.93736 | -43.8599 | 2025-09-28 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b54401f9-af0e-3bed-98fb-8fdbb4e5786a | -6.24611 | -44.48428 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c759e65-a157-32d0-a1e0-09bba69198ce | -6.71229 | -42.76043 | 2025-09-28 04:04:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 078cee84-ba10-3b8c-8378-c1ab9c00a17e | -6.56846 | -45.10246 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c708ac1e-b659-3087-8312-96d9141cd840 | -7.58095 | -42.32838 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2669b3e9-2794-3549-a652-c5d1a0b2cc1e | -6.83061 | -44.09045 | 2025-09-28 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 700fadaf-af72-360d-8bd7-8d09daba483e | -5.0925 | -38.83588 | 2025-09-28 04:04:00 | NPP-375D | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c589ec7a-26a9-323b-a9a9-05c2f8da135b | -9.28215 | -48.96449 | 2025-09-28 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98669736-695f-388b-b890-29971bb0f604 | -7.78625 | -47.02488 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5b7f05e4-3a2f-376a-858d-3fac84bb39df | -5.91465 | -42.93911 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b73bdab3-ac74-367c-957e-826005ed34ca | -6.25161 | -42.46482 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4c2d6b0f-2a1f-3a88-8a9c-765ed276698f | -6.11547 | -41.80875 | 2025-09-28 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c311206-d39d-3aa6-b332-a4bed8f95df6 | -4.82703 | -45.82542 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 581635a7-fe57-3574-944f-20bd9bacaa0b | -5.94115 | -43.86052 | 2025-09-28 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb825027-68fe-303a-afcf-67dddbdb01fd | -10.13444 | -45.32366 | 2025-09-28 04:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5da8f4ce-f6e7-30d5-bd90-8d408b59a062 | -6.00111 | -43.8041 | 2025-09-28 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d80ef281-e697-3dfb-98ad-4d4828e48462 | -7.74939 | -46.99275 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b36909ad-404f-3ab3-a610-913f40247831 | -3.64411 | -48.32165 | 2025-09-28 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb116f08-6631-337c-bd14-eddffec7542c | -8.2862 | -45.46593 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b12f89e-eed4-3456-b275-4077625c128e | -7.43776 | -43.19149 | 2025-09-28 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 24c8e8e7-8b8c-3ad3-ae2b-37b21fa36ed3 | -5.20367 | -42.76888 | 2025-09-28 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc413868-cb64-3ecc-aae9-9705379cf87b | -7.76013 | -45.73733 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38f6d483-6706-3b7a-a5ee-4c5ac7398dc8 | -5.46368 | -41.08281 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| b1f54325-ca69-3aa4-9f74-ddc5c0426337 | -8.83379 | -46.20305 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c41564da-ad20-3d2f-b628-439b8048fff8 | -8.68439 | -47.06583 | 2025-09-28 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be65cb82-3993-3c7c-a0f4-8c96022f0a20 | -5.62884 | -43.3643 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0f7fbfe-ed9d-377a-8622-a3c5f2332549 | -5.6207 | -43.36745 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1c30964-393a-3958-9c18-2d950c4e599d | -6.40547 | -44.29445 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbc2ecc8-d226-3047-80c3-09257e7cdbf3 | -5.90286 | -43.28933 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4fffbc03-5f08-3f12-8039-176e55dea4bd | -10.53828 | -43.63237 | 2025-09-28 04:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3377c96e-ff84-3711-9754-9e031ef64b5c | -5.86788 | -45.75784 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3dfc9da1-79fa-3f90-bb43-1c4992d4a19a | -3.81734 | -40.37204 | 2025-09-28 04:04:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2afec4c-9d31-3917-96f8-7ea9c3332a22 | -9.28924 | -45.70543 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9860a28-01bd-3a90-9ac7-2e07f51d7d20 | -5.90355 | -43.28498 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6930afc2-b705-38a2-8690-5d766399b11e | -6.92733 | -44.64459 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b03a1cf-fe2c-37c0-be7e-922ed42ee02f | -8.477 | -47.80538 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6046b08-b8b4-3c4c-a644-fa4e80838ae0 | -6.78357 | -44.04448 | 2025-09-28 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e92d6358-0848-3282-87f2-7935113daa19 | -5.76433 | -42.82792 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4bbb4a77-84d5-3824-8ec7-45706d25c200 | -7.74252 | -47.00568 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 381bffd8-6949-3bf4-9c2f-0839fe0526d5 | -8.17092 | -46.4178 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6391415f-aac6-3536-abb5-e55798940e96 | -5.76402 | -42.79306 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2ef8c765-1597-3cf8-ab4a-975681acd6ee | -4.53638 | -48.65158 | 2025-09-28 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9c547bc-43b4-3122-911f-0a112d78214c | -8.16729 | -46.41301 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 67a82238-3429-3895-88fa-84b59537be20 | -5.7977 | -42.79018 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a11b9b5d-a6a7-356a-b87a-fea85ac203e8 | -4.62096 | -43.10056 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2709a821-d823-3e0c-a80b-8d5079fbcc22 | -5.81098 | -42.82177 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4dedeb88-da44-3570-b4ee-f195684d97fd | -6.25159 | -42.46508 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 36f77ae7-5eb3-356e-a645-ae1c791e7872 | -9.45185 | -47.61418 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e0ec733-e387-34da-9be9-ac9d88f001be | -5.91045 | -43.67487 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c884cc0-5b86-3418-b81f-92937504a393 | -9.06729 | -45.54515 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa7210a1-b0cf-324c-b131-5ecc48ae6c91 | -5.90672 | -42.94218 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 05268b47-dd7b-3fb3-9cd6-59392b5e2994 | -5.41623 | -42.27606 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 738a80a0-ec45-31f5-9587-f932ba762390 | -8.28805 | -45.45513 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8c0f469-2fc8-32eb-997f-827d85aa07b7 | -9.77877 | -47.75917 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bab83e72-b297-3211-a561-e2af22755f12 | -8.71881 | -50.05169 | 2025-09-28 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1d8fdcb-d4d3-34ae-8ad9-6190c3c13e62 | -9.43615 | -43.70077 | 2025-09-28 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f95a154-a9b4-32af-9210-e3608112f4ab | -7.79484 | -47.00254 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c6ffb16-bf66-346d-be6a-1883838b7501 | -6.39861 | -43.53009 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1910805e-b45b-31b0-bb6e-bc3e11182b9f | -4.04316 | -40.50868 | 2025-09-28 04:04:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e6b79c8a-6722-3a8d-b0b2-376846ad9d1c | -4.17979 | -38.11765 | 2025-09-28 04:04:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 19d2f3d5-a300-3e48-8881-df20b77d1989 | -5.73204 | -42.6632 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 896806b1-1eb1-3aae-a344-ba7cab3342b9 | -8.27 | -45.46316 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56cbd898-0d1c-3642-874d-ca70d59f9e37 | -6.57649 | -45.09967 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 226460c9-bc1b-3d4a-8032-3a577195a8da | -5.7539 | -42.55138 | 2025-09-28 04:04:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c8536d5c-c6ba-39d2-84e5-1bd37e1eafa0 | -6.78801 | -44.08799 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1ee80ee5-ffdf-32e7-9aff-f5cb46679896 | -5.59996 | -43.37769 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| fb8c6118-0c9c-356b-94c3-d1e6e86a39dc | -5.74416 | -42.88451 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a14c161a-0d4e-3775-9aff-73b481523727 | -8.48647 | -47.80688 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 176969a1-0e6c-32d3-9306-ca085b776cc7 | -5.65106 | -43.06739 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 93b67c80-a996-3c23-a814-c4cb1d884a5f | -6.47798 | -44.50448 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6654934e-9307-31e4-bdf9-bbfaa1cc5132 | -5.05264 | -45.3139 | 2025-09-28 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6a9812e-d809-339b-b893-fdd91c42f3e1 | -8.5006 | -44.72758 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| efec4d7b-b77c-3ca3-b040-8df21ee5c8a1 | -5.28912 | -43.15755 | 2025-09-28 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 209f5e04-f980-3d3d-b554-f4ebc60f6989 | -5.46425 | -41.07921 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 03e972de-8e37-3251-88a5-59485e63ea92 | -8.62813 | -44.84702 | 2025-09-28 04:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8287c199-fae9-3b46-aab2-f5cd9adc9829 | -10.54316 | -43.62496 | 2025-09-28 04:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69dd5fcc-d44d-32ab-9c03-1277205b1de0 | -9.28861 | -45.70904 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bb1f35e-b30a-3b83-9c8a-0115471657b3 | -10.53962 | -43.62436 | 2025-09-28 04:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 242ef833-c3b9-39e8-b7ce-3b4233c258d8 | -8.82387 | -46.01149 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b177ce67-751b-3f9d-9c82-29d2669f288c | -3.32909 | -50.24863 | 2025-09-28 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README35.md)
