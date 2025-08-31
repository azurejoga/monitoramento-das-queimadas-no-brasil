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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 244bc03f-080c-3c10-9254-c12f56eb410a | -7.90823 | -63.00749 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9920d1bf-187c-32b7-bd2a-f712a8180d82 | -8.8538 | -70.62161 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e559810-0aef-308c-805b-479467328095 | -8.67512 | -62.42694 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22e76d32-342f-343d-926c-40983aa2eb00 | -8.67671 | -62.42451 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 173fa8ba-b6bd-35c0-847d-327fa7f6e8d7 | -7.90778 | -63.01073 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0be7596a-8806-30bf-aa37-feee30ac053b | -9.45406 | -60.57406 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5b14c2e-42a4-3fc5-8aaa-a02da5bfbfd3 | -8.74341 | -62.38041 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88cbf2d4-f678-35b1-83d6-10cc9eaf565c | -11.31808 | -63.26657 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5e751d1a-9cf8-32c6-9ac4-f27bb218a1d8 | -7.91921 | -63.00575 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cff4785-bdb2-3b5c-b301-512bba5ad5bc | -8.09719 | -71.24767 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d14ace77-6620-32f3-9eff-66df675fcdbd | -11.42038 | -63.24483 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7b9c165c-e169-3d99-b2b5-6466a3db8cb7 | -8.51604 | -70.00531 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b1faf8e-8792-36dc-b28f-8cf94189ad8e | -8.88873 | -62.38809 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1119066-75e9-3739-856f-638fd7300047 | -9.44453 | -62.35731 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 611758db-1e60-3a52-be24-55df1c013b0b | -9.45624 | -62.35521 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f0ef2c59-2690-3c62-bfe8-a0a0c9d4203e | -9.43891 | -62.35646 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 356806cd-68d2-3165-b16a-f15a2e087192 | -7.91305 | -63.01151 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7908c076-661b-3cd2-98c1-e15192a7b361 | -8.56828 | -63.01304 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9fd73e00-6ca2-39b4-9767-aa35e074af11 | -8.64968 | -62.83241 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cbcf1c3-b3ef-30be-8a94-64330fe4996a | -9.43227 | -62.33757 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf5276c7-2bd2-3b8b-9031-fe1650f4e607 | -8.90449 | -62.1018 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 730103b2-7f5e-30b5-a2c2-2b00fd63144f | -8.65563 | -68.68816 | 2025-08-31 06:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eefcf434-7c63-3ec0-83a7-5613aa8235de | -8.74242 | -62.38784 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d25ac19-09b7-31c7-b5c0-59c22e9fa11c | -9.44966 | -62.36193 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22c179e9-69bb-3584-b27a-a5751226aaaf | -8.76055 | -71.06821 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7991b5f-2a82-3d31-bb74-92de602c69e4 | -7.71142 | -72.70153 | 2025-08-31 06:10:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 28dce7c3-250a-3ecd-beba-4aa89a855882 | -7.9126 | -63.01474 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd7e1d5a-e2ec-396f-b1b7-216c0d015dfa | -9.44078 | -60.57757 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3c88750-a380-344d-b2d5-4b15adc3ed04 | -9.27313 | -67.64554 | 2025-08-31 06:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 56ae80ee-2102-3389-b2ee-9b8ff670eeb3 | -8.67606 | -62.41968 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2521026-3648-3f7c-a964-0efb9e53e9d5 | -9.76363 | -67.53835 | 2025-08-31 06:10:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cf1ad2c-7fa7-3cf8-aeab-60f14fa1a810 | -9.44501 | -62.35354 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03fa64c7-4fce-3d1c-8d32-5c29fe1c3ed7 | -9.4418 | -62.33386 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24a45162-677b-3431-a78a-8d853fae96c1 | -7.97992 | -71.3942 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e879d3f-a869-3306-b123-dcc46ba369eb | -8.73638 | -62.39071 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0db2823e-2eba-3b3a-a32b-124c70eb5d74 | -8.64475 | -62.82825 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b059bba8-1773-3f99-bbcf-e07e391785a2 | -8.22884 | -70.46692 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45d0f43e-42c6-35dd-90e7-ceba47c23bb2 | -7.92403 | -63.00973 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 68930e95-662f-3015-a487-b640fe89b8fc | -9.45724 | -62.34751 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aa186c89-9835-31ad-96b9-b6cce2a73ad4 | -6.91583 | -71.74713 | 2025-08-31 06:10:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 756b4f8d-4760-3429-b61c-d3c66ac56f92 | -9.26921 | -67.64495 | 2025-08-31 06:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0973f04c-51db-3ee9-a16a-030da40ca1eb | -8.04125 | -70.09937 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 827286bb-1fa0-32fb-bc41-c95a613c71a6 | -8.6777 | -62.41727 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 683fbe8a-ea43-3ac5-a744-41f57719757d | -8.68207 | -62.41682 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b77af92d-f820-37ef-b0ff-28dfe210aa25 | -8.55629 | -63.02146 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b480151a-3198-3ac5-8ebf-7e5a1e071a97 | -6.91638 | -71.74365 | 2025-08-31 06:10:00 | NPP-375D | ATALAIA DO NORTE | AMAZONAS | Brasil | 1300201 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2caccff7-9536-3f7f-bf68-d5b6beed8ae2 | -9.43771 | -60.57796 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a141dd2e-dc33-3a23-8f0b-fb00dcff8b5c | -8.65598 | -62.82637 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97dd4b99-a404-39c1-a256-3b3e2e52b068 | -6.9186 | -71.75113 | 2025-08-31 06:10:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a66f6d00-9966-3cca-81db-31e567aff356 | -8.6443 | -62.83165 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a1d5d71-f39a-3eed-9e92-ad5462e609e2 | -11.41628 | -63.24348 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 2129ed61-f0df-3e49-8085-d263cc56c373 | -8.82249 | -72.31498 | 2025-08-31 06:10:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f433385d-44df-3d71-a58e-a13ba80efba4 | -11.32308 | -63.27079 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6908fcfe-f22b-3d70-b800-0559ebfebead | -10.70601 | -69.05952 | 2025-08-31 06:10:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b1f35fa-82f1-3b71-b5a5-3acddf395f02 | -11.31663 | -63.27121 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 919acc9e-be38-377b-b36c-d8b43ad02593 | -7.56579 | -63.41348 | 2025-08-31 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27e35723-2b00-3050-b653-c1a57fb4677e | -8.59843 | -61.96223 | 2025-08-31 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35d6b99b-8beb-31a1-b28e-3cfbcd92e58c | -11.41539 | -63.24052 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8202d76e-097d-3129-ace4-86752dadb73f | -9.28171 | -67.64174 | 2025-08-31 06:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60d86267-c1ba-3f38-ba87-59fe203fc519 | -9.43279 | -62.33371 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0edcc734-5076-3ddb-9a20-1dd84639e6b8 | -11.32252 | -63.26841 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1a9603a4-4a58-3498-bf50-69058886e9ae | -9.44402 | -60.57869 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71e6dfdb-86ed-3d3c-802a-e095ea3ee7fb | -8.88726 | -62.38472 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14d5d4ee-d7c3-31c8-90c0-4cac1d5ecd65 | -7.46481 | -70.12998 | 2025-08-31 06:10:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1dad934-09e2-3547-b916-27a5295ddf1e | -8.65013 | -62.82903 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1cee1e8-1151-3cf6-976d-1c91f597422e | -9.43901 | -60.54168 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d734be2-095f-3ad3-bd07-3a0fa458af91 | -8.68761 | -62.41762 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68ab7108-8bfc-3048-b5ca-b9d279aeca4a | -8.88366 | -62.38362 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7c9fcd9-b104-3517-b1c6-00f32e71c589 | -8.67465 | -62.43056 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0b028e6-c0d5-3ee6-8aa8-f5e147b532d0 | -9.43474 | -62.34431 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49ee4418-6968-3aad-b415-3933c14bc5b3 | -8.84781 | -64.15352 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 909afbe0-cb20-37c2-981c-a72d931ea2b8 | -8.97832 | -70.74432 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba7864ef-d4b9-3f7f-bfd2-8c39567279de | -8.01962 | -69.882 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21b45cad-4def-3b7e-a05b-7c4186a49645 | -7.46537 | -70.1263 | 2025-08-31 06:10:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a25398e2-35c7-3a95-bc65-87ab17173b0e | -8.23168 | -70.47109 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61b0e146-fdc3-3b19-b8a3-9e15ed5768c8 | -8.90563 | -62.1061 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4efad0ce-98f1-39be-be09-33777b518b67 | -8.84843 | -64.15432 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d100ac7-1bce-3b98-8256-114988f637f9 | -8.56647 | -63.02623 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca4d2dde-5575-3943-b85b-5520fad6b532 | -8.3891 | -70.7615 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f76a2a8-192f-39a9-99cb-10cd382e8089 | -8.56115 | -63.02549 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 688b908d-3237-3278-8186-3a85451c2361 | -9.43005 | -62.33612 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce454fd5-2e45-36f6-9206-9a039912446c | -7.56801 | -63.41309 | 2025-08-31 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3fb51d8-723c-3074-bfbb-0ff3d4bd600c | -8.9224 | -62.41955 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2e8cb8f-fbe2-313f-bfc4-1def6e5e57ae | -11.41584 | -63.23699 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3a208461-e161-3abd-a8a2-ebb0eeee9b70 | -8.65522 | -62.45012 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ce553e3d-6a54-3195-a29b-e47be2bf97da | -9.57285 | -66.6909 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a33f6d86-b2e6-3a80-ac74-6741072c14dc | -9.46385 | -62.34067 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33a70bf7-239f-35f6-a90f-104438e0c985 | -8.67653 | -62.41607 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65156bca-9883-310c-abb9-d1782b9c9c8b | -11.41494 | -63.24406 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f3c252ba-4505-382d-b76e-6cc5f9c092dc | -8.55188 | -63.01412 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 041b8a06-1ff1-34f8-b2ba-1edfcf0639cf | -11.28216 | -63.23831 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62d4ae1f-dc52-31b6-b9c4-973adafb544a | -8.392 | -70.8318 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24fc3a1c-75b1-386f-9242-f8ba10e7e907 | -7.56843 | -63.41008 | 2025-08-31 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d44b22c-c47f-3a31-a7d4-af53a8b8132c | -8.66346 | -70.03883 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcd95fb5-c049-3ef8-b927-048a3f57aa22 | -8.65553 | -62.82978 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fbfd7b5-2e84-3297-88c3-8888a1e3ebe2 | -7.92358 | -63.01297 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c5b92d07-4298-3162-bef0-598c58547ac1 | -9.44693 | -62.33858 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b72998bf-4b18-3aba-8c5b-5cf59e39adbd | -9.44917 | -62.36568 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dca5889-4029-300c-b96c-bcb0416d251c | -9.46434 | -62.33688 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00b9bee8-ad9a-3a0c-9adb-e23ca0768116 | -8.74193 | -62.39152 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README80.md)
