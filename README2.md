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
| 7e9c6e5a-400c-3730-811d-94c8fd0c5fe2 | -10.70715 | -37.59913 | 2026-01-28 04:21:00 | NPP-375D | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 046f60f2-3ea4-3630-b97d-498efce80679 | -9.30896 | -37.99076 | 2026-01-28 04:21:00 | NPP-375D | PARICONHA | ALAGOAS | Brasil | 2706422 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 70006cee-8c99-3079-8ec9-d02aea9c382d | -10.71221 | -37.59564 | 2026-01-28 04:21:00 | NPP-375D | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e6483bf4-1c4d-366a-84db-a7533ca557ad | -8.46317 | -45.13409 | 2026-01-28 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d40da5e2-529f-3705-a549-242dfe45e155 | -10.70801 | -37.07105 | 2026-01-28 04:21:00 | NPP-375D | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 487fc06c-d518-3c11-ba7b-c613bdd70229 | -16.08973 | -45.17363 | 2026-01-28 04:23:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f1b1b6f-5153-3da0-a5a8-dad601158fdf | -16.09029 | -45.17002 | 2026-01-28 04:23:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 740181db-e784-3901-afa4-5ccb7beaede4 | -15.8531 | -43.50986 | 2026-01-28 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e22ea52e-4c6e-32d1-9da7-005a5d3de343 | -12.89665 | -49.21759 | 2026-01-28 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c2f4e576-bbfd-3fda-b328-965ef5c1c508 | -15.9768 | -43.66185 | 2026-01-28 04:23:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5606e672-4660-3ff8-92d8-f37e2c61e198 | -15.85367 | -43.50602 | 2026-01-28 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f7af760-3993-30c4-9720-897797101468 | -15.84966 | -43.50931 | 2026-01-28 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62e49ac3-aace-39fc-abdb-bbb1dc674a41 | -14.46855 | -46.99421 | 2026-01-28 04:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b23b1ade-8a1e-39ef-b6af-4bdb6381c3d0 | -15.85023 | -43.50547 | 2026-01-28 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1df5a62e-ac0b-3136-8a25-40ddacb65870 | -12.50161 | -46.6763 | 2026-01-28 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66709355-3e17-3ed4-a670-72e60ca2fc6f | -12.87486 | -45.28716 | 2026-01-28 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7c2ef41-b499-3085-9d58-a72c670bd9b4 | -12.50506 | -46.67691 | 2026-01-28 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1ad99cd-3371-3b4d-a6e7-a5224ee2c332 | -14.46512 | -46.9936 | 2026-01-28 04:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee9d1096-c792-3919-bde1-a63e49b8a89c | -16.62431 | -45.61792 | 2026-01-28 04:23:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adb025c0-be2f-3aec-bedb-bd72ee32bd54 | -22.80606 | -49.33168 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0b6c4244-5e43-3fd5-acbe-9a9ff2b7ed66 | -22.73487 | -49.34414 | 2026-01-28 04:23:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87ff881a-0119-307f-9248-f303f7487e49 | -23.43476 | -47.26389 | 2026-01-28 04:23:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f753e6b2-ed1d-3dc7-92eb-54396b9ba6e3 | -22.80332 | -49.3269 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b83210af-58f0-3519-8841-ec41f1a20113 | -23.00846 | -52.38676 | 2026-01-28 04:23:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1841ed28-e3a6-3313-8caa-62fea02ee29d | -22.79436 | -49.33076 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a15ddd7b-854b-32f0-a4be-20e3317c6c1b | -23.59612 | -48.34404 | 2026-01-28 04:23:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1065f8f9-0703-3e62-b64e-fe912aa1114f | -22.79916 | -49.33027 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b28c128-b0a8-3785-a45a-b4217479b9aa | -22.79781 | -49.33146 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18d623f2-b399-3ec8-ab9a-0bed33c677f4 | -22.79986 | -49.32621 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c1c52b2-bd01-345d-8add-e4da5f669fcb | -22.85739 | -43.49838 | 2026-01-28 04:23:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ecbdbf78-b0a7-3cdf-9d65-0bcd173c324a | -23.00655 | -52.38968 | 2026-01-28 04:23:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a54fed4a-9785-3736-aaa1-5033eca1641f | -22.7957 | -49.32958 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7881ea3-423a-38d4-b032-fc815f738735 | -22.7985 | -49.32739 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f818a500-b1b1-36a0-b07f-65e4b20ac84d | -22.7916 | -49.32599 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcacbd25-4c6f-3d97-b394-c100f2c0c70b | -22.32521 | -47.1338 | 2026-01-28 04:23:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8df11f63-7396-341d-898c-a5596559929e | -22.79505 | -49.32669 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54fe546c-f9f1-33b8-a55f-81c045278750 | -22.80535 | -49.33577 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5c787a78-7a7d-38fe-9b02-9724bbeb9a5e | -22.8019 | -49.33504 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f3e099b-883a-3036-b0b5-7e61ce6d2b5a | -22.79641 | -49.32551 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e99e3f25-cf41-301c-a44b-b4ddb31be8de | -22.80261 | -49.33097 | 2026-01-28 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 19c3ecc1-b1ea-3243-bcfe-2641288227c1 | -19.95088 | -44.70457 | 2026-01-28 04:25:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0515c72e-2e26-3ee8-bba0-e682dd3f6cda | -19.23795 | -48.60612 | 2026-01-28 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c621b482-aec6-3569-b572-03152e9c4d77 | -25.10071 | -52.91288 | 2026-01-28 04:25:00 | NPP-375D | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d0007a15-c218-35c5-b5fe-4aa12560382e | -27.09662 | -50.52856 | 2026-01-28 04:25:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a52e1658-8abf-310b-b7c1-ea4289a02da4 | -27.56617 | -48.66102 | 2026-01-28 04:25:00 | NPP-375D | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2db3ac44-e607-34a3-9ffb-45004e29368c | -27.21412 | -48.68144 | 2026-01-28 04:25:00 | NPP-375D | TIJUCAS | SANTA CATARINA | Brasil | 4218004 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6be4a146-b6c8-3ffb-973e-9f861a0334bd | -27.65766 | -48.70276 | 2026-01-28 04:25:00 | NPP-375D | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c2acf6f5-dfd3-3b5d-8f19-460f9904a240 | -27.68554 | -48.7517 | 2026-01-28 04:25:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bb8f871e-d5a4-3eec-a8d2-96eab0c1c50d | -27.68888 | -48.75237 | 2026-01-28 04:25:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d5fb97c3-37c9-39fa-9c13-a3dae6ca13bc | -26.7 | -50.5795 | 2026-01-28 04:25:00 | NPP-375D | TIMBÓ GRANDE | SANTA CATARINA | Brasil | 4218251 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 138467ce-8c47-3c0e-ac9d-ea81acd050ee | -27.56284 | -48.66034 | 2026-01-28 04:25:00 | NPP-375D | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 387d3133-3e1b-373f-90b0-8b3f1ef92b96 | -1.31042 | -53.20175 | 2026-01-28 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| d4bcb313-d4ef-3b12-a8bc-8584fa379238 | -1.30961 | -53.20686 | 2026-01-28 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 42b7f283-a141-314b-a015-be0620feb930 | -8.45901 | -45.13371 | 2026-01-28 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f45c30af-b3a2-3c3b-91f0-93939ac18821 | -8.46301 | -45.13427 | 2026-01-28 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36853c8f-94e0-3e89-8670-26440f242ae0 | -14.46903 | -46.99144 | 2026-01-28 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a9f3880-3259-304c-b45e-2c060e0d0d2f | -12.89674 | -49.21506 | 2026-01-28 04:42:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ac3a303-aa93-3cbe-b16f-c59bc46e6f63 | -15.85086 | -43.50467 | 2026-01-28 04:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98ae4aff-498e-3402-82a7-ab4062f2d728 | -14.46833 | -46.99635 | 2026-01-28 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 632af78f-8ad9-3fe8-bd73-fd3164a48e26 | -13.50587 | -46.7065 | 2026-01-28 04:42:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df87263d-3ba5-38fa-bad0-c418e7b7d8c9 | -13.49283 | -46.71482 | 2026-01-28 04:42:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f637e791-c6a7-3635-9504-ed5cdd50e0b1 | -15.85017 | -43.51041 | 2026-01-28 04:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4af78122-f306-352c-ba38-f58d9996790f | -14.46447 | -46.9958 | 2026-01-28 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 007bbf94-3e49-36ba-af85-a29a8cdf7a20 | -11.14477 | -43.32117 | 2026-01-28 04:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4a6ec53c-6da1-3b16-a794-231602709ce4 | -12.503 | -46.67583 | 2026-01-28 04:42:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35aa5871-7ff9-3aeb-8c02-9ffc89afbc59 | -11.16601 | -44.50486 | 2026-01-28 04:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a699603-9134-39d2-aa6e-555b4800059d | -16.09215 | -45.17284 | 2026-01-28 04:42:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef4bec0b-76c0-3d75-a314-aeb4754326b9 | -13.50517 | -46.71146 | 2026-01-28 04:42:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58b491a7-bd4d-3e45-ae34-2b972441e100 | -11.07364 | -45.37434 | 2026-01-28 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c229d15b-a05a-38b1-8031-10c264590eea | -12.89618 | -49.21881 | 2026-01-28 04:42:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bc4796a-3982-3140-b75c-af4fff0719d7 | -12.89276 | -49.21827 | 2026-01-28 04:42:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4158284a-1766-36f1-99b4-11433fbd27f3 | -13.2498 | -50.13197 | 2026-01-28 04:42:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24dd1cc9-6a80-340a-8537-692c457cc8fe | -13.49352 | -46.70985 | 2026-01-28 04:42:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3bdc0ee8-c975-32f5-9708-3f13be963cd2 | -11.16416 | -44.50559 | 2026-01-28 04:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f641e1ca-bba5-31eb-a341-145bc545ff37 | -13.57051 | -52.49532 | 2026-01-28 04:42:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b11ef16e-74bb-35ef-b33a-e5c6c16c8e27 | -22.7963 | -49.33193 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a48e4ea1-66a9-3afc-8c7e-ec109dc00ea9 | -20.2121 | -58.02619 | 2026-01-28 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c73917af-441c-3c36-8202-31f9ce718112 | -22.7998 | -49.33001 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 804e3936-50bd-3660-a8ad-97d3ed85c73f | -22.80668 | -49.33593 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5362c4e-3306-308d-b9f5-24af715f1675 | -22.79692 | -49.32706 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0eb0d6a5-f98d-331e-a88c-0cf9e5f18d30 | -22.84289 | -48.64361 | 2026-01-28 04:44:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2ea0d965-bc68-3a7b-93b5-087f17c325eb | -22.80444 | -49.32821 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0af59aa6-df2e-3f96-a2b2-7021d2a24df7 | -22.79229 | -49.32885 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a7e95c6-fba1-3f28-94a1-8762ce23aadc | -23.00798 | -52.38776 | 2026-01-28 04:44:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fa04ae8c-536e-3e7d-97e9-5101817f3326 | -22.80006 | -49.33251 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deaa3963-9e98-3717-8bec-c3bfe3481087 | -15.76544 | -52.5869 | 2026-01-28 04:44:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19286150-dfd5-39a4-8789-e1816adc04b0 | -17.3112 | -44.92961 | 2026-01-28 04:44:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05ee4778-65f0-3055-8372-bbd75c8f5025 | -22.80068 | -49.32764 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7b23a5d-898d-306f-aca0-fce2ec389839 | -22.80733 | -49.33109 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f914bbda-65ce-30e5-be63-a57ee3edb3b9 | -20.21062 | -58.02642 | 2026-01-28 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 55db7f17-cccb-327f-9f44-517925b25a87 | -22.79294 | -49.32403 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de75ec3a-b251-31ab-affb-561ce1f993e1 | -23.59677 | -48.34172 | 2026-01-28 04:44:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b71f957-2527-3ff5-b429-ebf6cbef55a9 | -22.7967 | -49.32459 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c26dfe2b-e9b0-3507-8892-8d1c71fb8b64 | -22.79605 | -49.32943 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f191ddf9-63d6-32a5-822a-d385aca23f2a | -22.80291 | -49.33541 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d86594b-b571-33f9-833a-a96d58878796 | -22.80046 | -49.32514 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2b44e69-21e2-31c5-bda4-c23c7b2f962e | -22.80356 | -49.33059 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eb4970ad-7f29-398b-b29f-8abbc0171932 | -22.80382 | -49.33306 | 2026-01-28 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 36557a20-43bd-3000-8cc6-70d5addd5da4 | -22.73277 | -49.34447 | 2026-01-28 04:44:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b00940fb-35d5-3133-bfaf-19b7732673c5 | -27.68749 | -48.75106 | 2026-01-28 04:46:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
