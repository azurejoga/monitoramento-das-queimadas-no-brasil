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
| 27d10c0e-7322-3e30-903a-408b937d167c | -12.13688 | -54.6559 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0b3db3e-fe37-3b51-9456-11af530875da | -11.38528 | -56.55881 | 2025-06-12 04:29:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b25706a-e967-37bd-bcb1-83ec8231c03d | -13.97545 | -54.4274 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f6f90f6-3e65-3191-8afb-41dcd3da0b98 | -14.17762 | -45.48526 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a53120ac-d19f-3e43-bf9f-388c71ad909b | -13.89774 | -48.74255 | 2025-06-12 04:29:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddcb2f0e-3de2-39e6-b10f-879b86ad6de3 | -10.88769 | -54.75625 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b44a67e0-7605-38ea-b1d3-f8adf56c55c0 | -14.03419 | -55.12893 | 2025-06-12 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eee8b2b1-0785-3600-8a8f-d80ecc4eb0f8 | -10.94572 | -55.32088 | 2025-06-12 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e648ba1-1fdd-36c6-8c1b-45c356cf6cdc | -13.57067 | -44.27227 | 2025-06-12 04:29:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e738e84-59bf-32d7-88c0-d2bc66975b3f | -12.20957 | -49.63268 | 2025-06-12 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84a86559-c513-3073-84e2-af4f7d963cd7 | -12.76901 | -44.39777 | 2025-06-12 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 541b7195-196f-30dd-bf30-fdbc24fdf6be | -11.98787 | -57.20539 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba617de9-4339-3a0f-b994-641f0c16f3f9 | -13.29295 | -57.07933 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1a95210c-1bc7-3eaf-9298-22062d636429 | -14.82576 | -54.66138 | 2025-06-12 04:29:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f078a9fd-22e0-350d-865b-99b11c50a3cb | -13.28708 | -57.07613 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75931a25-22c8-34fe-b67f-538339e01772 | -11.96644 | -46.94153 | 2025-06-12 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a33865c5-1af7-3c0c-adb1-316ff77b0ecd | -10.87827 | -54.75455 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 70b05662-1294-38bf-8366-3408a054e17b | -13.89556 | -48.7347 | 2025-06-12 04:29:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6bd905f-1169-344e-93c3-0b1064f821fb | -11.77959 | -47.40154 | 2025-06-12 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d5a7ee9-554f-3a3a-b300-ca6079a838bc | -12.05549 | -48.07588 | 2025-06-12 04:29:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2c864ce-f1b5-3609-8c3d-7358587ce281 | -14.02874 | -55.13271 | 2025-06-12 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f67dc693-df34-31fb-8b01-d4153b91b68a | -13.29099 | -57.08396 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 97fe2b61-382a-3982-a6c9-c119839a1e96 | -10.99506 | -50.75724 | 2025-06-12 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd8ebe9a-1681-3e1c-b9d7-d5e3a7602d1c | -11.38127 | -56.55124 | 2025-06-12 04:29:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa322679-251c-32d4-bcf1-eadd4888d6a0 | -10.88298 | -54.7554 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5f8470c7-4fc7-3fcb-bd5d-c5f6e7d7f95b | -11.571 | -51.30287 | 2025-06-12 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1680788e-3582-354c-b03a-db87def0363d | -10.94673 | -55.31545 | 2025-06-12 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8df4515e-7c73-3dc4-821e-c6e3b11380d0 | -11.84308 | -43.80037 | 2025-06-12 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 16977614-a66e-33eb-b2af-000e1161cea0 | -11.99805 | -57.21094 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e39f9911-7064-3933-930f-ddff490b5f6d | -12.76839 | -44.40211 | 2025-06-12 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c97089f-7089-3680-b43c-7057a06aaed0 | -15.38271 | -47.883 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1dfcde2-b03e-3ea4-b783-9bad5281f435 | -14.1723 | -45.4968 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e1f74fc-d6f3-3c2a-9502-0549f9ac09e1 | -13.5431 | -44.14402 | 2025-06-12 04:29:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e4623535-004a-30e9-8006-c51d64f0a7e7 | -13.90188 | -54.6534 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bcbc763b-1c54-39cb-ae1c-db53d37b6b08 | -12.37912 | -45.77161 | 2025-06-12 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bd11bdb-09da-3b50-a572-643db3ef6a8f | -11.76947 | -54.37429 | 2025-06-12 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53baa2a4-e5d8-3690-a77f-c9eb309a07bb | -12.4022 | -40.90995 | 2025-06-12 04:29:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a601dbf9-475d-30ca-a6eb-c48e02283ad5 | -12.82415 | -47.37764 | 2025-06-12 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bf0eea5-a4d8-367a-8215-a5f494425076 | -11.99261 | -57.20995 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a256d480-4f03-3400-aa22-390f867fb387 | -15.3766 | -47.87833 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 466d49cc-35ae-3dec-a771-59b088f5eda7 | -14.03507 | -55.12424 | 2025-06-12 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6ce5633-6d30-3d8d-9fad-86a6f63cf1af | -12.51435 | -57.24181 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dde2edb3-c95f-33f9-af04-0f5883d20667 | -10.99432 | -50.76153 | 2025-06-12 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e31557a5-b6fb-311a-82b9-29bc91e6106f | -10.86784 | -54.32147 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5d4ce75-68de-3f61-b85e-9353ed2b5570 | -13.89744 | -54.6526 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4c0a9402-5182-34ad-86ae-baefd504949e | -13.32447 | -47.24997 | 2025-06-12 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac1be77e-4a94-395a-a293-cdd6b107a291 | -14.82621 | -54.65985 | 2025-06-12 04:29:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53157e8d-9688-3838-bc56-b69576bcd527 | -11.00676 | -50.75484 | 2025-06-12 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46cb3e9c-cb13-3623-b47f-34680293dee4 | -14.17935 | -45.4979 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3709162b-affc-3238-8e3e-776d45aa2577 | -11.96255 | -46.94452 | 2025-06-12 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c05e9448-23b3-3533-a6fa-8ac6234ae8e2 | -14.42404 | -47.89552 | 2025-06-12 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 691f2f2d-6d56-3610-8c6e-8ad30b781b74 | -10.8792 | -54.74944 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 70382a12-4ef5-32d4-a447-79395576fde3 | -12.52043 | -57.23937 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d363cdb-7cf3-33fe-9d45-caa85220a5b9 | -11.7757 | -47.31772 | 2025-06-12 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 016e57ba-f150-3bb1-9ba9-09330a10c23c | -12.72839 | -54.97282 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e103b142-5aa3-31ce-8147-ce4f025bb7c4 | -15.37716 | -47.87473 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0897cbd-dfad-3857-b763-e193ce7f1eef | -14.18288 | -45.49845 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eb1f941-6ca0-3cf4-b9e7-f0a325303086 | -10.86411 | -54.31591 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33fedcb4-05bd-3c11-9ece-07727d479dfa | -13.29168 | -57.08599 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7022853b-6e52-3960-b407-4cd3bb7e469a | -10.88483 | -54.74518 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d5e395b-fbd9-3a39-b4c6-7ab6ae112ce9 | -11.13735 | -53.94369 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0471a74-7459-3b99-b346-1bdecc8f9a21 | -12.10967 | -48.87577 | 2025-06-12 04:29:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5f4bb0e-5e4f-3d24-b7a8-47851c7a5478 | -12.7258 | -54.97478 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00bbd7ab-04bd-3327-8f0b-14d33fa3ccc4 | -12.79563 | -48.73324 | 2025-06-12 04:29:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88030844-e756-3bc2-905a-cad959bd63b4 | -10.33418 | -57.49058 | 2025-06-12 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d68956da-81a9-3afe-a2fd-663682ce1a2f | -12.2102 | -49.62887 | 2025-06-12 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a3f049f-ed73-3a97-9833-2ee57795ca77 | -12.71074 | -58.02884 | 2025-06-12 04:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f52a2558-8697-3348-b1f0-407d4dc23e0c | -13.28839 | -57.06958 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d44528aa-5640-3933-b3d7-e8a55fb212b4 | -12.52181 | -57.23238 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5d20323-eec8-33a7-8de1-cd4a024bff6b | -13.89498 | -48.73835 | 2025-06-12 04:29:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bd35530-0d11-3330-9035-1b1ea71b9203 | -10.88012 | -54.74432 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cc51d72-01fd-3e98-a560-4210470068f8 | -11.86769 | -52.25457 | 2025-06-12 04:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 90bc6331-5f16-30c8-8a6a-36b74cfcbc4b | -13.29165 | -57.08064 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dc6b4182-1f3c-38cc-84a8-a854848252d6 | -14.42682 | -47.89962 | 2025-06-12 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc9e4c93-6289-3816-941e-b0b111858245 | -10.33986 | -57.49172 | 2025-06-12 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 283f0e73-3c67-3f50-a3a8-3ab697475d12 | -13.47096 | -56.85583 | 2025-06-12 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e87b50e4-c504-3148-a522-e873701911d3 | -15.28785 | -47.16104 | 2025-06-12 04:29:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c1d5d87-b504-3593-91c0-4f8afd392f46 | -11.37539 | -56.55349 | 2025-06-12 04:29:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72836019-549d-3f62-8831-f9565736daa4 | -12.20738 | -49.62446 | 2025-06-12 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cdc21a0-59fe-3306-98b5-ef9179c5c6fe | -10.36248 | -57.23921 | 2025-06-12 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 417e8c76-a071-3d1e-8a02-6a415f414e83 | -15.37327 | -47.87778 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2485f96a-3622-3848-bc4d-45f68b11acd4 | -12.70509 | -58.02776 | 2025-06-12 04:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ba77ce75-40a6-307a-a73f-9c59cfb5b56a | -10.36391 | -57.23151 | 2025-06-12 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be03ac1b-3d7f-3c0e-9d78-fe933b279896 | -12.10099 | -49.48622 | 2025-06-12 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c79e539-6c1a-3308-a2b3-d42f7cda2353 | -11.96588 | -46.94506 | 2025-06-12 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a67987f0-74c5-3369-ba75-6415e4d34447 | -13.65736 | -53.93921 | 2025-06-12 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d396359-9ca1-321e-9372-fe669b4e5c8d | -13.07761 | -46.74603 | 2025-06-12 04:29:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b2de8c1-01c0-3c61-9eba-cfc398e0d441 | -13.71147 | -58.67834 | 2025-06-12 04:29:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c21fbb6-3bb8-393d-a86b-ac9609801e3d | -12.50048 | -54.43468 | 2025-06-12 04:29:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 746b0822-ad5a-3943-bd56-c3b9789d32cd | -11.56186 | -47.45286 | 2025-06-12 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f39491d1-cc06-3e60-a9fa-2083a8d66d71 | -17.00865 | -49.78012 | 2025-06-12 04:29:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9fc3278-bc2b-3536-82de-eb0fe6a10e83 | -10.30095 | -57.13597 | 2025-06-12 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c01218e-f23f-3546-a5b4-165bebf0e920 | -11.78857 | -54.77835 | 2025-06-12 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 248174f0-8752-3a2a-a9d5-3bd5ed58667f | -13.49421 | -53.49503 | 2025-06-12 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bb0574f-00c0-3975-9ee1-44ce8bd09c48 | -15.36638 | -48.07547 | 2025-06-12 04:29:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01c9b59b-9f1f-3975-83d0-7b40c461c5a6 | -11.99331 | -57.20637 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8b78caed-e3ad-342b-abc3-f525a23536c5 | -11.84556 | -43.8031 | 2025-06-12 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8280b09e-4ef1-3398-99db-94c068d431f6 | -11.56519 | -47.4534 | 2025-06-12 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38a5622d-f112-3086-a433-043852979353 | -12.70998 | -58.03265 | 2025-06-12 04:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e208e8f-8935-3fad-90a7-9aff38f74585 | -11.77117 | -54.3651 | 2025-06-12 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
