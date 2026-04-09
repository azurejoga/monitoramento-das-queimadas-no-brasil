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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39455ec8-230c-33c2-b0a3-1f74478157eb | -23.40835 | -46.42403 | 2026-04-09 03:53:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 01c4c90b-d095-35d0-af64-ea9e8bf3b567 | -23.36372 | -46.16867 | 2026-04-09 03:53:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5689e5e5-78a3-3ddc-a80c-8a8b8ad38ae2 | -29.71205 | -50.68311 | 2026-04-09 03:55:00 | NPP-375D | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4b5a2372-648a-308b-9247-59cdbed40b9d | -29.71125 | -50.68644 | 2026-04-09 03:55:00 | NPP-375D | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5d23d53a-d411-3aac-bbd2-82a84c19b607 | -11.86475 | -43.86145 | 2026-04-09 04:10:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ab06788-e3e3-3597-813d-862644bcda72 | -9.45816 | -47.81166 | 2026-04-09 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b1f18d6-e1cb-3f02-b8e2-bdd2649c7db9 | -11.87142 | -43.86256 | 2026-04-09 04:10:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 99286eea-5175-340c-95bb-90b018edabea | -12.43442 | -40.91991 | 2026-04-09 04:10:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 419cdecf-36db-38ba-b6c9-7f29be501cff | -11.95651 | -43.37349 | 2026-04-09 04:10:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5817d0e1-fb92-3219-8a45-a338b30e599b | -10.58186 | -37.62226 | 2026-04-09 04:10:00 | NOAA-20 | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 06a6472b-62d1-3c78-9f8d-a1948fcb4361 | -11.95925 | -43.37759 | 2026-04-09 04:10:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3828c682-6f74-3ba6-a96b-53cfdcd8a7c8 | -11.70358 | -37.67033 | 2026-04-09 04:10:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7bb33b0e-1df8-3c25-b97d-1d9a66b9d2be | -9.4588 | -47.80792 | 2026-04-09 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a21c013-d6c0-3000-aa7d-35bff3d0ed98 | -9.1838 | -47.79612 | 2026-04-09 04:10:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b109b6c5-a801-336e-aac1-656bc052a9c4 | -11.82283 | -38.26276 | 2026-04-09 04:10:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 529119d6-2cde-372d-995a-4eb70c60f386 | -9.45466 | -47.80719 | 2026-04-09 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56361423-91db-3fa2-b065-b16717c934ab | -9.45207 | -47.82231 | 2026-04-09 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f478548-087d-347f-be78-e008e649f73c | -11.86809 | -43.86201 | 2026-04-09 04:10:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 59ab3b3b-05c9-3c25-91e2-574ac2d40035 | -10.58584 | -37.62289 | 2026-04-09 04:10:00 | NOAA-20 | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1b895e21-ba91-3004-a1d4-b28755404a4f | -10.4972 | -38.48489 | 2026-04-09 04:10:00 | NOAA-20 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e6f921c0-83db-3582-8b8f-e6cb41766d55 | -9.45944 | -47.80417 | 2026-04-09 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 665bab3a-8e86-3a73-971e-4900cc84cb52 | -11.95868 | -43.38112 | 2026-04-09 04:10:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2883fbd-9948-3c6b-ac27-9814dffbc481 | -9.45141 | -47.82616 | 2026-04-09 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16d25008-6f6b-3308-93ad-b2adec2bb102 | -11.69954 | -37.6698 | 2026-04-09 04:10:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 917e27e2-2bab-3041-a8e4-1971bd6de29e | -11.26055 | -41.04516 | 2026-04-09 04:10:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8717714c-9dca-3f56-8153-4dc94ad6cd13 | -12.01232 | -45.23328 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04048a32-0077-34e2-a9f8-0caac77bda39 | -12.83442 | -45.95168 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60565b77-aa19-3d24-90f5-efb4d80f872f | -14.43182 | -45.62966 | 2026-04-09 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a15e5618-96ff-3cf1-8960-2b9bd65c54e5 | -12.02685 | -45.23178 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bb9f0cd-b89b-3dee-820f-fe2f0f9f8759 | -12.02338 | -45.23118 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38291ac5-4283-31b1-a0d6-a234081e6f9c | -14.1164 | -41.84977 | 2026-04-09 04:12:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99d2dd78-a21b-3f20-8404-e4e080aaef57 | -12.0262 | -45.23568 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f4878a0-6c17-3d86-b07b-2845acdf7640 | -12.02273 | -45.23508 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24f5dfd5-5bcd-37f1-b378-0432412cb48f | -12.67167 | -46.65586 | 2026-04-09 04:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35d2b38b-bcc8-3037-89ee-fa520e054d83 | -12.67243 | -46.65141 | 2026-04-09 04:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e7937e5-9099-3bdf-bc79-a41946c2fa4c | -12.83512 | -45.94758 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38b6418f-3cbc-30dc-991b-61126acd0a1c | -15.02688 | -45.11193 | 2026-04-09 04:12:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 662b8e77-ea3a-3df5-ab3f-31552ee589ef | -16.92422 | -43.59769 | 2026-04-09 04:12:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b09724e0-1b49-311f-901a-20172fc7cad8 | -12.01167 | -45.23718 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e522d664-8d25-33a2-a40f-ec723a3c0c78 | -14.12417 | -43.41605 | 2026-04-09 04:12:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 02d5394b-da73-39b5-91d3-fbed6d7ae58d | -12.01579 | -45.23388 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a40c4d91-0f47-3a09-b33d-af538fd27bea | -12.0275 | -45.22788 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9340da4f-9faa-3ef1-b1d1-9e3d21fb8847 | -12.83372 | -45.95577 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1299eac-cc5f-336c-8ff0-4bb3b969f2f6 | -13.18534 | -43.55108 | 2026-04-09 04:12:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1967c254-59df-3e4f-840c-7b2806170a66 | -12.8341 | -45.95748 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02020005-2cea-3847-90e5-7ce4e11a9b56 | -15.02351 | -45.11134 | 2026-04-09 04:12:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b6d186e-43ad-3fd2-94a8-4af64ec47ae2 | -15.03302 | -45.11684 | 2026-04-09 04:12:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9c7112f-36ad-3756-9812-6072ef74ed74 | -16.72097 | -43.83353 | 2026-04-09 04:12:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00a5a0cf-7fdf-394f-884d-bb3af608df39 | -12.83547 | -45.94927 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6456dfba-52c8-3fb1-922b-99614e1f18f8 | -14.12748 | -43.4166 | 2026-04-09 04:12:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34f7f035-eb18-3357-b749-78ed047559cf | -12.83727 | -45.9564 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 876d8855-6e65-373c-91a5-115d6f497c45 | -12.83615 | -45.94517 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51b78020-101a-3a04-82cb-cc1767775a4d | -15.02749 | -45.10822 | 2026-04-09 04:12:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24b0b076-3f6b-3215-91fc-b9316f629659 | -12.0677 | -45.33907 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6ee49dc-9454-3dc9-bff1-95b14edd51ca | -13.21406 | -43.69008 | 2026-04-09 04:12:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1e72bea-57ec-3b03-af12-db8b39767b4f | -12.01514 | -45.23779 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d028b546-07c8-3284-9605-6bc1f5794b4e | -16.92366 | -43.60129 | 2026-04-09 04:12:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a69be73c-a62c-38ed-a119-04a46af35354 | -14.23707 | -43.64572 | 2026-04-09 04:12:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ad37750-6240-31f1-9caa-e207d9943560 | -12.01861 | -45.23838 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 801b53da-f329-3e5c-bd8c-7498d476e6b2 | -14.89841 | -41.98296 | 2026-04-09 04:12:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c550c67-91ad-32dc-8264-17bbde1e11c0 | -12.00819 | -45.23658 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a8801da-3966-30d0-8ace-52ba6243b22c | -12.00885 | -45.23268 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc2822c9-77db-35bf-9e99-cb3b91b2a4f0 | -12.02967 | -45.23628 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1eddfe0d-9686-34cf-a860-0abc5189e418 | -12.03032 | -45.23238 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9400f270-439d-368b-9217-98eac715f1bd | -12.84151 | -45.95292 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3f0b142-dfdf-3e07-a4d8-b69ad79482ef | -12.83937 | -45.94411 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10612d9b-bdb2-33d0-80ff-f13e6a2925d9 | -12.01926 | -45.23448 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 040e4ffb-fac9-32a3-b06a-339c2a0bb979 | -15.03025 | -45.11253 | 2026-04-09 04:12:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b0afc5d-6683-322f-8b62-d1130b5c52ea | -12.84081 | -45.95703 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25ffc1da-7c86-346f-9cbb-eb0bd154b639 | -15.38193 | -43.05962 | 2026-04-09 04:12:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 228dbda3-0a15-35fd-b77b-3ba2f9aa4593 | -12.06623 | -45.33943 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cb36d59-3b6a-35e6-b342-f0e01c9a9e4a | -15.02412 | -45.10762 | 2026-04-09 04:12:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de7d9d8d-8475-35e9-927d-ae8ae807863a | -15.02627 | -45.11565 | 2026-04-09 04:12:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cc1a82c-c544-395a-b108-612527c9b8d3 | -12.84011 | -45.96113 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5b52c3e-7c3b-37db-a0c3-e9d37444921f | -13.26717 | -43.54979 | 2026-04-09 04:12:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47d9e4d7-ef1d-3d46-a0cb-362be2e0701a | -13.21074 | -43.68953 | 2026-04-09 04:12:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce64d1a-1b62-3940-ac5e-6dbf45281be4 | -12.83797 | -45.9523 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f581ce35-69ab-3a57-91cb-9f2171cbf710 | -12.03097 | -45.22848 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0c5c249-f0de-3c6f-aed2-190d5a459475 | -12.01991 | -45.23058 | 2026-04-09 04:12:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26fc0b23-c070-3a88-9f25-9962dba139d0 | -12.83478 | -45.95337 | 2026-04-09 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 150381f8-39d4-3898-904c-8ee601bb764b | -18.49429 | -55.49736 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 855aa33f-a926-3c44-88ae-80a41903d928 | -18.5014 | -55.51754 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f33ebacb-fa21-3648-93d0-08de42742e5e | -19.59004 | -40.07874 | 2026-04-09 04:14:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 695ecc92-cd82-3644-9783-bee9760ce2c9 | -18.49336 | -55.50166 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1386d502-1c3a-39ac-a507-ff1376a09c94 | -18.50811 | -55.51466 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6934ab6b-f293-334d-aca8-96776652125c | -18.50782 | -55.51887 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7e1fe963-c503-353a-a4f3-f5214b35d7f9 | -18.50114 | -55.52172 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 60e561af-c36f-3a7f-aca1-1167a012fe73 | -19.00887 | -42.15084 | 2026-04-09 04:14:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d4ca04b0-4732-3182-b4e9-46db6ff4a52e | -18.49911 | -55.50311 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9e45ddc8-b277-31d2-a8db-e7e2899ea174 | -18.49374 | -55.49752 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a2866141-8bcf-3ab3-ae75-2cd787e54be2 | -20.5454 | -41.59047 | 2026-04-09 04:14:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3f9de43d-8924-3f3c-8e7f-48a675ee65dc | -18.50207 | -55.51743 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 344092c0-2c7e-3c5d-97dc-b7703968e6cc | -18.49853 | -55.50324 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 229231a8-81d3-3023-b2b2-1cdcbb1c86a5 | -20.83804 | -47.27843 | 2026-04-09 04:14:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26ff1c53-7223-35f5-bb33-23ab15c3c0a7 | -18.49947 | -55.52616 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d88475fe-33ed-3d39-abc1-9ffbc41f824a | -18.49949 | -55.49895 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c4f5384d-9cfd-3802-a7a2-f3568d085900 | -18.49724 | -55.51169 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a8d99552-8a16-3eba-9cb3-d885137f0522 | -18.50715 | -55.51896 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f583b0c1-f7f0-38eb-a827-e962fec37212 | -18.50236 | -55.51325 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6cbe9781-ee6f-3053-a281-3ce9b971ba5f | -18.49278 | -55.50181 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README3.md)
