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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17fb63e0-fa6e-344c-aa54-f0274a42384e | -8.6124 | -50.40287 | 2025-10-01 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d41ed45-6d7c-3d54-a3f4-2c8e7657a946 | -13.29876 | -48.70505 | 2025-10-01 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c0bd317-4944-3153-aeb6-1f50497050e8 | -15.44607 | -51.56141 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7cce34e-2135-30d9-98d7-ac901e6905f0 | -10.44693 | -48.08558 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40bc29f3-fde9-399d-97cd-d464c97def59 | -15.54944 | -48.1859 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d71ca7e2-f096-3aac-ad44-63a22e1f32be | -13.06583 | -47.0878 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20cfb45d-92c1-3c82-be15-c3bb6df32695 | -15.26891 | -47.84203 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05122cd7-d28d-355c-a47f-dc3795f5059f | -13.79232 | -47.98332 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b515930d-e255-3a2a-84b7-35af5a144ff6 | -14.7957 | -48.32115 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b144911-6325-3870-be18-621a3fe06f15 | -14.18743 | -46.12639 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c7518234-a936-3551-acfc-33a307e1c104 | -14.78447 | -46.96659 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e2d5bbc-8164-34b9-944d-a958aaa6db0c | -13.94192 | -48.10438 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e1024e4-e9b3-32b6-a68e-62c6521aa54b | -9.56311 | -50.97835 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9734abb-1d0c-3166-965c-5b6a7057f3a2 | -14.01775 | -44.97934 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f786f5e-77f2-374e-bb10-3dd98421dc17 | -11.81914 | -44.98294 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0155dad9-c8ab-3efd-8a36-8747d3059324 | -15.23401 | -48.74605 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 347bd83f-209f-3f44-affd-8d0bf84db47c | -16.08391 | -51.03123 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15ca9000-5cdb-3a9a-8c24-44384bff11c8 | -15.41916 | -47.05853 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ab22a091-ef62-33bf-bf59-22de0402f1db | -11.47866 | -45.10117 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3cfaaef-cd10-3d83-9faf-631701fcba63 | -9.50864 | -54.6583 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91c950c2-cf8c-33cd-a69d-3eef8adafd96 | -14.36628 | -47.14484 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8e6e9fe-efc9-3c0e-8856-2e496cb99f75 | -13.92153 | -48.08861 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69fee1a1-05be-3d7d-82f8-9d1e5eba77a9 | -16.01032 | -50.87087 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b53be802-d64e-3051-b7c7-786eb21f2d5c | -15.45856 | -45.88871 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 558a56ff-4210-397a-b017-45c57a3d41b6 | -13.66432 | -48.04643 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c99b795d-d0ec-319e-b59a-56abfc9581f0 | -14.68427 | -48.23473 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 635c32b6-8d61-3df4-81ff-5a0a51d12cb9 | -9.45087 | -47.92273 | 2025-10-01 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c306420-134f-393b-939d-88b2d6716b07 | -9.21309 | -50.69054 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5119d80f-a96d-36e3-977f-349be495bdd3 | -15.31526 | -46.40393 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02d56ae6-34b9-33ce-97f6-6d8e0a5c5ad2 | -14.39539 | -46.21573 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcd4f95a-1b99-3ad1-8447-ee8c824d1c7d | -13.37721 | -48.10724 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc55698f-a646-362f-b428-a009eaab0926 | -16.05403 | -51.01179 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b64d583-d638-3eb0-a498-31b303a27e58 | -12.94041 | -48.41296 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8b17de5-7ddb-3da4-8a95-9cdcd4c6f368 | -11.56894 | -50.17745 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49e211ac-7909-324b-a0e9-738f3d16f658 | -11.60358 | -45.03368 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2db28176-b7f8-361d-a293-755a0b427f8f | -13.07467 | -47.0853 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7b14d24-855e-39c7-b968-87fc88550d45 | -11.811 | -44.97183 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b798b3d3-675b-3990-a1be-c79d06effb4d | -14.72784 | -46.82711 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac9e4010-97c3-3bf3-890d-a478febe1d47 | -13.67332 | -48.06851 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c1573aca-7b00-3c8e-a6fe-0c871f5d02c9 | -13.28335 | -47.22049 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24c422c5-2d92-3cd0-9f5c-660742d9f12c | -12.24339 | -47.79243 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79b54ffc-a113-38fc-b0d5-fc2709f47769 | -14.10095 | -49.74999 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eb3c43a-7e8a-376b-af56-104fb08acd62 | -15.94581 | -48.11944 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 002c429b-9610-3591-ac19-355a5118a037 | -11.76449 | -46.84889 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5f8b4f70-b43c-3a69-9c89-07e0bbdc270f | -11.82167 | -44.92708 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75f02fd3-27c5-3150-a83c-4282f7336568 | -13.32443 | -47.33709 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b3199848-c996-3fe1-9bd4-981f929c52c8 | -10.57466 | -51.47118 | 2025-10-01 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a593de48-ad28-3275-81f2-bff34187a1d5 | -15.30912 | -46.40133 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc229013-a471-324b-8fb1-20c4bcdec52a | -16.06099 | -51.01292 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b451bd14-2202-335a-83aa-c530cb0100c4 | -12.74494 | -44.77129 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6cd3b93-eb5c-3387-aa05-8ac738eaf840 | -14.7255 | -48.14009 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07ff7fee-dec8-3d5a-8759-eb81255e07b3 | -14.52695 | -48.369 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b491791-4ed7-32cd-8e64-89d4168f1511 | -13.21224 | -47.34011 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 595dcb82-ec89-3e0a-96e2-82b8378325e4 | -10.41797 | -51.64852 | 2025-10-01 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8f5306d-dcfb-39b5-873c-1c4159083dee | -14.36215 | -47.14451 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a623e8c-dd35-32c0-95b6-7e5683f0e318 | -14.79005 | -45.77348 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8d34a17b-6c12-348d-8a36-fc280f36325e | -12.43419 | -50.17067 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b112c1c6-62ee-3a48-83d2-1071c68caa9a | -14.5478 | -48.22131 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daad3d3a-ade1-3469-8575-4687005a8975 | -9.55941 | -50.78077 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8b422cb-2913-3fcb-b423-e162dc2b7099 | -14.98707 | -46.95442 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96c90b40-6f61-33f5-a7e1-ace6eb7765dc | -11.84143 | -48.06399 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 998b5118-f59d-3537-8fd1-5d372f8a523f | -11.85077 | -44.99755 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b27bc8b4-4413-372c-b16e-5ed99889924a | -11.46488 | -44.98911 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1c1a6fc-702e-3f63-80e0-140ade4be2c7 | -10.06182 | -48.19289 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 558f2fd0-1cff-31cd-9432-34e469217ef4 | -14.6825 | -46.9625 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57d3ea78-639d-3abe-9020-effd8b2462f6 | -13.98726 | -44.90793 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 06479e72-1010-3ff0-a0c4-2440fd3ba827 | -15.92663 | -48.13908 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c322dd49-bc95-35a5-8676-c7332adefb36 | -12.66328 | -46.8648 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 680baed3-252f-30d7-a974-cb7f525ea9da | -9.80667 | -45.93397 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e7bb8f5-89f7-3188-86cd-45f251574459 | -11.05816 | -47.83657 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1c44e7c-28f9-3898-81c9-f6e563196d3b | -13.33143 | -47.85854 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ecb454b6-980f-3ee6-979c-a554166643a5 | -13.93996 | -48.1187 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b17aabd0-2081-3d71-ba6e-e37a54881cb3 | -15.52549 | -44.34117 | 2025-10-01 04:51:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a85ec37c-d40e-3978-bae7-899e0a1a7f0c | -9.81844 | -47.85817 | 2025-10-01 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abfc6eaa-08cc-3576-ae44-4fe787dd0472 | -9.42183 | -54.70781 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d56525af-f30a-3b9a-a470-b25eb4c6e3b5 | -13.30013 | -47.23708 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f8f3e84-3bcd-32d5-8f61-4bf628615bd5 | -11.45035 | -44.97405 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84eb3a9d-5b29-30c6-b488-cf1eba443b97 | -10.63688 | -48.52808 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 137c1f67-b430-3a3f-aea6-0b3845a7de81 | -11.13798 | -43.37903 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 21b537bf-896b-39f0-9bab-5fd275733ffd | -12.78474 | -46.85781 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 82302895-3f9b-3cf1-9459-6654c699d9b5 | -12.39647 | -44.76402 | 2025-10-01 04:51:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7bea6102-6a83-339a-8624-41306029fe5c | -9.4202 | -63.21269 | 2025-10-01 04:51:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c686d26a-8c38-36a9-a067-b4d5ff70c042 | -10.91024 | -46.57354 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b396653a-a5fd-34c5-a24c-0a036ff76655 | -12.77197 | -46.88817 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35268e1e-9095-3661-a6ba-e65c741a4b75 | -13.22465 | -48.44978 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b1cb95d-ec75-3430-a10a-fc66b75dfdb0 | -12.94671 | -48.42366 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52346097-1b5c-3919-bdf4-9860569fee43 | -14.89176 | -48.12411 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc589f07-6029-3da5-aedf-e89cdce87fc2 | -14.00048 | -44.84286 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 735d225b-c3b3-3132-85b5-6173bb525567 | -10.08445 | -50.19812 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eb8986c4-0596-3418-b3cb-72a2133aed8d | -13.80947 | -47.49689 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47a27f73-cbc2-3fa1-9b99-d88cb9a2bcd2 | -9.82385 | -48.26939 | 2025-10-01 04:51:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c594db1d-d693-3622-8a23-52d481a14f09 | -13.66617 | -48.06205 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7305deaa-2a77-391c-b3a4-ae9358d68d38 | -13.40966 | -48.16005 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf86f82c-3f63-365c-b04e-ae90ca5e6da3 | -12.24917 | -47.80014 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 531d239a-7655-315d-b33b-b3d8c7c67e13 | -13.02988 | -48.67667 | 2025-10-01 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbd19877-4166-3caa-8438-5b00beb08052 | -11.16941 | -54.11995 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d110d023-bdce-3937-9f9e-6d84fcac68d4 | -11.11818 | -49.78332 | 2025-10-01 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78fc87f5-7a89-31c4-b143-b46f4b4fe578 | -13.77632 | -48.01111 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3126b55e-a7e4-3c02-ba05-32b9ed0ecb16 | -13.32885 | -47.84776 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5e27ce17-4cfe-3332-85f3-155033c7c527 | -10.91038 | -46.50856 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README109.md)
