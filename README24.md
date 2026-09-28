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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35a57248-d922-3a74-b4d6-3051e0acd8f1 | -14.59951 | -45.59623 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7931241c-e9c5-3d06-9460-c8da5cde5716 | -19.47287 | -45.88636 | 2026-09-28 03:51:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dd5fc7e-3dae-3367-97df-2c80c249cf0a | -17.82857 | -44.38852 | 2026-09-28 03:51:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48d45864-ca16-39ea-841f-683fa2c53796 | -15.17088 | -46.16932 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f1fe080-148c-3fa4-a5cd-62359dbd1a59 | -14.79364 | -45.9512 | 2026-09-28 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0e24fa9-ca32-3b40-8aa3-e9a5ec38246d | -14.52578 | -48.3117 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cec52857-57af-3d83-adf2-84776c1148d7 | -15.25306 | -43.65607 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 298e994d-ad0a-3994-ba98-bf50dc47c90f | -17.25093 | -42.83024 | 2026-09-28 03:51:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0e2d4c4-9c41-3730-9e67-c047598c3cf0 | -14.73207 | -45.57856 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea6376e3-76ed-39ae-8d3a-c2b36a10717b | -19.1519 | -43.83466 | 2026-09-28 03:51:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edc3fc56-2e93-39ce-86a5-3c49015dfa3f | -15.15341 | -43.60638 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8382e20a-e658-3578-b26d-e452168257c9 | -15.17547 | -46.16286 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9aacc3c-2dec-38a7-9aaf-4ec3791256e0 | -16.35282 | -42.57962 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52113e1b-13fb-310c-8dcf-996c373b9db4 | -15.82388 | -42.53817 | 2026-09-28 03:51:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8b87289-350f-31c4-aee1-586015a00ef9 | -15.16782 | -46.14857 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f39e330-85f3-3109-9a08-c57416a5559e | -14.78862 | -45.95016 | 2026-09-28 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27168cdc-ef24-3564-b9d2-c34117c05870 | -15.1678 | -46.15806 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a0e3b0e-f873-39e3-9e60-59151b07a93f | -15.16842 | -46.15491 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5edd2d8-3dd5-3d79-ae9b-09beb6969da6 | -18.67906 | -41.46432 | 2026-09-28 03:51:00 | NOAA-20 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| b864bb0f-392f-3ebd-a4fc-18f2e51c3f3e | -15.05395 | -47.23158 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46a22e9f-88a0-37e9-bc11-ce73666d8ea8 | -15.17354 | -46.15564 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 191f4025-f7e6-3c3e-b5d8-6ac6863ff1e5 | -14.11479 | -46.30283 | 2026-09-28 03:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 649de5b7-c44e-3376-bf82-c40712a6ef07 | -15.14956 | -43.57958 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8bd7ae58-e772-3f76-a73e-623f1c1ff650 | -15.40924 | -47.91605 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d2056e3-86f6-319c-a71a-c10cc934431c | -14.51994 | -48.31033 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6befe29e-c5e3-3ecf-ba08-672f7e1eaac6 | -15.41224 | -47.90166 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e110e864-43b5-3161-b4d4-6ad7c3ba3690 | -16.3538 | -42.57423 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4f77c15-dba9-3041-ba50-85786073fc4b | -18.11888 | -44.38282 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4db9437c-7054-391a-a790-ba1db17efccc | -14.71615 | -45.58163 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9cd468f-8866-3fe4-84bd-bbdbfd7d2fac | -16.38802 | -42.5651 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05c11b3d-b04b-3259-8bec-f98f1ba36bee | -15.15104 | -43.61896 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb641501-a42f-3bfd-a82b-662787b82e92 | -18.10695 | -44.37551 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55b7feb1-fc5a-38f7-93a8-f1bec0e6e66e | -14.12062 | -46.30071 | 2026-09-28 03:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71367772-f985-3350-a235-72a3ad214364 | -18.12047 | -44.37439 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11e45207-e250-3927-ac97-b409369cac13 | -15.62195 | -43.52436 | 2026-09-28 03:51:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51b6524a-b0e0-3d36-9002-696dbb0a2fa9 | -15.15262 | -43.61056 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 332debf5-2805-3df0-a0f4-33bf52f4bcb7 | -15.17682 | -46.1562 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55cf9ae8-30f8-3638-bad4-97d8eba6d146 | -16.38317 | -42.56944 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e70c080-b4a1-3417-994a-c84b11623521 | -15.62118 | -43.52845 | 2026-09-28 03:51:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9ff7765-1511-3c48-95d4-5c13c5b2aba4 | -14.59462 | -45.595 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13348f4f-8b40-3cc8-bae6-23e10a5f1ed9 | -18.11969 | -44.37855 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fdf5f204-6f62-36f0-bb35-559fc6518380 | -18.11464 | -44.38181 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3cc463ad-5c3d-3675-8fe2-759a84c45ad6 | -16.3898 | -42.57179 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46b91df7-2598-3e2c-82d6-7e3add8090cd | -15.05321 | -47.23513 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 956d72f8-157e-3fbd-b5ca-2537e4686875 | -15.40348 | -47.91552 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ca3f12a2-a3a9-3268-9489-b21f4fa5cec9 | -16.39584 | -42.56694 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff1158bb-8cbb-37e5-89ff-238f57f2868e | -18.09767 | -44.37759 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e234a82-f19d-3eff-a581-319ea911aa39 | -15.16659 | -46.15466 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b819e7ca-d127-3eee-a84d-87e536390a2c | -16.39099 | -42.57129 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea8c3a19-0c90-3e4d-9f0c-7e2bffcc4aa1 | -15.16975 | -46.16508 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fa9b79c-c0a0-3962-a595-dfcdf5953f33 | -17.58153 | -44.29756 | 2026-09-28 03:51:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 786c739f-2bf9-36fe-ac1d-45772e22ca90 | -15.05939 | -47.2327 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06dd8e31-971f-3727-bc88-c89f9b6519a5 | -15.21573 | -46.3595 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06f8f04f-f765-3614-a400-686b2e1787a8 | -14.71727 | -45.57586 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7fdd92ca-16d6-3b30-bdc2-8ef81ab03e6b | -16.38708 | -42.57034 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd0e4a92-89a9-3f34-8885-a54a8546b8cb | -15.16582 | -46.16825 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 521369a0-60c6-305a-9d77-8cce4be78390 | -15.42506 | -39.09379 | 2026-09-28 03:51:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 212db277-1b8b-3c4b-9930-f5373842bd34 | -18.51768 | -42.42233 | 2026-09-28 03:51:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6057ceb0-dbae-39be-b686-8743960ce1e6 | -15.40652 | -47.9292 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d2c2754b-3f0b-3567-b925-4d6bfd207b34 | -21.05962 | -46.94458 | 2026-09-28 03:51:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ff9022e-445b-3035-9388-a4a67a138bea | -15.12879 | -43.619 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 29a568e8-b609-3d54-87f5-2468892d56e8 | -18.67549 | -41.46354 | 2026-09-28 03:51:00 | NOAA-20 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b10b0a7a-a57e-39af-b62e-fb46d737a6a1 | -15.41153 | -47.90507 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85a9d811-cfd6-3b23-b51c-e8abcde507fb | -14.51307 | -48.31384 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a4d0e51-cb3c-3098-b192-fa1b14c7046c | -16.21935 | -42.87436 | 2026-09-28 03:51:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f74adfe3-1be2-3293-8484-8bfc31574ab3 | -14.51895 | -48.31503 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 896384a1-35ea-3078-bc49-25caea22fc8c | -15.15612 | -43.61561 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 448ed579-26be-3f57-a5bc-be33574e9a2e | -21.22811 | -44.32909 | 2026-09-28 03:51:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f3cbe5b9-392b-3e1e-9c48-663e0a1d26a5 | -15.169 | -46.16879 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c1f6dce0-3255-3c81-baab-b31570194164 | -15.40262 | -47.91964 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d9ed8b42-5c68-3fa2-9dea-5cb0e4870343 | -15.16595 | -46.1578 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e1f4e62-6e30-3299-a80c-589cc12e19bb | -13.92292 | -47.85617 | 2026-09-28 03:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 725cd796-d089-3433-afc4-d9ec4294ea3b | -16.20319 | -42.87172 | 2026-09-28 03:51:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6f9c958-01cb-3286-bf10-01ca59dba1a4 | -21.52153 | -45.10964 | 2026-09-28 03:51:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ab328c88-87e8-3803-a0bf-c9a980ed4892 | -13.70438 | -48.82521 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2a18d20-83e1-3d03-85d0-f6e196b0d88f | -15.1792 | -49.39465 | 2026-09-28 03:51:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e292b037-2fdd-3211-a415-aab730513ee8 | -20.87363 | -44.11712 | 2026-09-28 03:51:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e993a559-dbf4-3425-8f3b-74acd7755ddc | -13.71879 | -48.81758 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f00b3bcb-a139-3b28-9162-f02817296717 | -18.54806 | -43.58844 | 2026-09-28 03:51:00 | NOAA-20 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bb80fa2d-ef7a-3934-8b65-84e4684bda04 | -15.17046 | -46.16156 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 949cc84c-3a06-3cbc-89f4-b3fb14cafebb | -18.75474 | -44.4077 | 2026-09-28 03:51:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3df8684e-f941-30e0-9ca1-9c6470274577 | -13.71057 | -48.82626 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e493cf10-505a-3dde-a855-466161b0329d | -15.0531 | -47.23206 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4f32605-723a-3156-bf6d-e9d391a9764a | -16.39078 | -42.56652 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfb42287-b83e-30cc-922d-9db76b152482 | -15.16721 | -46.1516 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b897e938-76ff-3ee9-9598-5bc10553f818 | -15.13308 | -43.61985 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2253a28b-71ae-31f5-b137-a9edeb202628 | -14.73697 | -45.57959 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7cfd87a-89a2-3f29-9757-a05b03ebf5a1 | -16.79455 | -39.40828 | 2026-09-28 03:51:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 22d9a2a9-929b-389c-af69-671cdc0c2eee | -13.92379 | -47.85189 | 2026-09-28 03:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac517f6d-0e34-3625-bca7-82441df7108e | -21.22335 | -44.33202 | 2026-09-28 03:51:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7fa287cf-503a-3252-a8ef-d2bdc00d7bcb | -15.05854 | -47.23318 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c262b5b4-032d-3862-b031-20a0b7acc61f | -15.68525 | -42.68036 | 2026-09-28 03:51:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8f714ccb-d026-3d5d-abc5-af318ff586fc | -15.94002 | -42.34103 | 2026-09-28 03:51:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a1a8bf8b-b501-3249-8bf2-9b965b262917 | -21.52488 | -45.11489 | 2026-09-28 03:51:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d45d850a-c60a-35a3-9640-20d97de536d3 | -17.70874 | -44.31804 | 2026-09-28 03:51:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ea904e7-74fa-33cb-8b19-7edba7af41fa | -14.89754 | -49.49846 | 2026-09-28 03:51:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b78327e-cff1-3593-b514-c93bfca73cf2 | -15.17175 | -46.15523 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cb48dde-ae6e-3539-ad6a-fb4b334fdcbe | -21.52571 | -45.11069 | 2026-09-28 03:51:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| cf61df06-6412-34b1-bd3b-70d5745c265d | -14.51207 | -48.31855 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 874e9cda-fd7b-3c1b-932a-cd7eacba0fc1 | -18.11119 | -44.37653 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README25.md)
