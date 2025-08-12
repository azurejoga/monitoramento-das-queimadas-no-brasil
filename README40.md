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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dea09c2f-9e8e-3eed-8ae8-0f9824661a02 | -10.865 | -45.2181 | 2025-08-12 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4ae73c07-044d-37e1-a73a-2c0edca196ad | -14.1212 | -44.8933 | 2025-08-12 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 327.9 |
| f491b32b-a489-3cb4-bc1d-bd0402bf3b99 | -17.5701 | -45.3346 | 2025-08-12 13:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 33c06233-fbee-376d-bd82-b958915c532f | -12.3565 | -59.8473 | 2025-08-12 13:20:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 11cd528f-2cd8-3b5b-92d4-5e144e516da0 | -14.1017 | -44.8968 | 2025-08-12 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 0fea8b10-2d02-3969-97e5-2f322c4718d4 | -9.2232 | -44.5283 | 2025-08-12 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| d12f303f-dff8-3722-965d-67f505c7fb19 | -14.1212 | -44.8933 | 2025-08-12 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 286.1 |
| d6ec9be6-4752-3b83-bf8b-787e40515473 | -14.1402 | -44.9133 | 2025-08-12 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| c141112a-8bac-3e1b-a7c2-d37dd0fe063b | -8.9401 | -60.7288 | 2025-08-12 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 03251958-889a-3076-a955-d1a49390f6e0 | -17.5701 | -45.3346 | 2025-08-12 13:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 253.1 |
| 72d993d9-ffde-3eaf-be41-c69507763faf | -17.5707 | -45.3108 | 2025-08-12 13:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 7def5893-b4de-37f6-af8d-0ad46b8e0350 | -14.1407 | -44.8899 | 2025-08-12 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 899708d8-71f8-3eb3-b6e1-676bbe6fd769 | -16.3157 | -52.8988 | 2025-08-12 13:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| df65e83a-af0a-353a-98a3-4005a5679346 | -12.3565 | -59.8473 | 2025-08-12 13:30:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f5ac2089-c5ea-3b84-88b5-fcd387970736 | -13.8743 | -45.5643 | 2025-08-12 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7ea7287c-9e49-35b3-9f1b-46ac9c4c6000 | -16.3153 | -52.9201 | 2025-08-12 13:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 1c070c5f-bc99-3b88-8109-e9ec23396680 | -9.2232 | -44.5283 | 2025-08-12 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 09e2fbbb-659c-353a-b5ce-da8705815120 | -17.5707 | -45.3108 | 2025-08-12 13:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 104.1 |
| bc1a8a03-3970-312e-a8d4-05ea6fbeab03 | -8.9401 | -60.7288 | 2025-08-12 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5c297bfd-6ce7-3375-a2c6-fb5b757bc8f0 | -14.1017 | -44.8968 | 2025-08-12 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| efabf987-e050-3e3d-9d97-daf998fe0be9 | -17.2637 | -44.88 | 2025-08-12 13:50:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 710d0946-8e81-3ca8-95aa-4a305972a197 | -12.3565 | -59.8473 | 2025-08-12 13:50:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 67cb70cf-462b-3b3f-a78d-4004b335fe8a | -7.1483 | -60.1174 | 2025-08-12 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3768354a-d85a-3a17-85e2-f80da67f0e8f | -17.5707 | -45.3108 | 2025-08-12 13:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3231f65a-c4ce-395f-b4e7-6395d8929cbe | -9.2232 | -44.5283 | 2025-08-12 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f56e0f32-3b0d-377e-996c-499664597d4d | -8.9873 | -46.5974 | 2025-08-12 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7e28f744-7d58-3060-98fd-f3c3867543a0 | -16.3153 | -52.9201 | 2025-08-12 13:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ac395e05-b4ea-3a3f-9b77-bfa3ab1971c8 | -14.1407 | -44.8899 | 2025-08-12 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| fd6f2aa7-1b32-32e0-b23f-412673e28bcc | -7.0799 | -59.1964 | 2025-08-12 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| bb9718bc-b9e9-3537-af53-1f8a784fd3b9 | -13.8743 | -45.5643 | 2025-08-12 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| af6a8b2d-8b7f-35f3-93c0-6bd418b1bbe8 | -7.1299 | -60.1182 | 2025-08-12 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e5d144d5-5ec8-395d-bb16-ea90cf9072a5 | -14.1212 | -44.8933 | 2025-08-12 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 312.8 |
| 2d0ce695-aa1d-3af9-9c59-0919539d7655 | -7.0614 | -59.1972 | 2025-08-12 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5b41b018-e83b-3e6e-817a-1e7e7f33a876 | -8.9684 | -46.5993 | 2025-08-12 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 8abb4b55-4e1e-3bdb-9fc7-5f3e1699f264 | -5.8418 | -59.9163 | 2025-08-12 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| bec55348-e306-395d-8f32-ff3823746fe4 | -17.5701 | -45.3346 | 2025-08-12 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 449.6 |
| 9974e85a-3cbf-3860-aa89-646330fb11bf | -17.5707 | -45.3108 | 2025-08-12 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 656ec33e-0a8a-3a90-b1ac-6724318f142f | -8.9401 | -60.7288 | 2025-08-12 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e3485ecf-4613-3ee3-bab4-17d2fca5aa86 | -14.1407 | -44.8899 | 2025-08-12 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 31918f57-505a-3342-9f6e-715601b8d09a | -7.1482 | -60.1366 | 2025-08-12 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 24e0e570-f1ac-385d-bb0f-d03c2b34f487 | -13.8743 | -45.5643 | 2025-08-12 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| b47929cd-0cac-30bd-9054-704a0fd37dcf | -7.1483 | -60.1174 | 2025-08-12 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 40f29efd-eaaa-32c4-813b-026ff23400b9 | -14.1017 | -44.8968 | 2025-08-12 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| b9515fe3-0314-34ce-9341-208b26ab3648 | -16.3153 | -52.9201 | 2025-08-12 14:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4b0d7360-8272-3779-a9f0-44b6c9b745d1 | -8.5788 | -54.7162 | 2025-08-12 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 1b0201b6-62a0-3874-b8d5-da29ae6facdc | -7.0614 | -59.1972 | 2025-08-12 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9314da84-eeba-3c8e-819e-2bb18efa689f | -14.1212 | -44.8933 | 2025-08-12 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 7e6732b9-fba5-3c84-bb11-87f376808260 | -14.1017 | -44.8968 | 2025-08-12 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 2d17e396-5edd-331c-9a14-9491de8ad783 | -7.1298 | -60.1374 | 2025-08-12 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a4c1a332-a45c-33ed-b565-a6655bfc28ef | -12.3565 | -59.8473 | 2025-08-12 14:10:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 2ec265e9-d403-3230-b653-4601069c09db | -17.5707 | -45.3108 | 2025-08-12 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 117.5 |
| c519a9ed-a7b1-33b7-b499-e77c533c44bf | -7.0614 | -59.1972 | 2025-08-12 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 1b1c8ad1-fea6-38de-9348-65eddad5f204 | -8.5788 | -54.7162 | 2025-08-12 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| a7b42bc1-0f38-3437-8693-68a29bf66db9 | -8.9401 | -60.7288 | 2025-08-12 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 737e3600-d234-38be-8fbb-80f0e0a98eef | -17.5695 | -45.3584 | 2025-08-12 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 29939533-8f73-301f-92fd-89105ef6cac5 | -13.8743 | -45.5643 | 2025-08-12 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 2038e23c-e964-3093-81ad-67e9bad00e00 | -17.5701 | -45.3346 | 2025-08-12 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 311.6 |
| c151599d-12cb-3c49-b7e8-1e0158c1a75d | -16.3153 | -52.9201 | 2025-08-12 14:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ad6926f4-baed-35e5-8afd-0b6ea54734dc | -14.1407 | -44.8899 | 2025-08-12 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 9c9ee1f6-4ea7-3889-8838-848e247e7e49 | -7.1482 | -60.1366 | 2025-08-12 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 7b414d0d-329b-39cd-a13d-ded1cc64486a | -7.0799 | -59.1964 | 2025-08-12 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 4ba093e4-ae36-3d95-99ea-8d6a92515418 | -7.1299 | -60.1182 | 2025-08-12 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 29c260fb-de5e-3ecc-8947-fdc5c2939ed1 | -14.1212 | -44.8933 | 2025-08-12 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 212227f3-a208-3991-8a35-bafe2f9b6da5 | -7.1483 | -60.1174 | 2025-08-12 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| c9b4c336-910e-3cc3-a0f6-c8a2b246348f | -11.8086 | -51.9012 | 2025-08-12 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1093e1b8-641d-3454-8a06-882023484d2d | -7.0614 | -59.1972 | 2025-08-12 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 1bb2b7e5-a319-3da1-87d2-41ed1531b848 | -7.1483 | -60.1174 | 2025-08-12 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 96f59846-eef4-3595-b53d-f857d03f5fc7 | -8.5788 | -54.7162 | 2025-08-12 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e51336d8-67c4-30c4-9f2d-e2aea55e2735 | -17.5701 | -45.3346 | 2025-08-12 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 250.7 |
| 74dba64f-a962-3dc5-a98f-2bb858e53e65 | -7.1299 | -60.1182 | 2025-08-12 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 95953bf3-13e1-34e9-9559-843b6bd6febe | -16.3153 | -52.9201 | 2025-08-12 14:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9dc884b7-7382-3db1-88c1-a75935c789a3 | -8.9401 | -60.7288 | 2025-08-12 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c1035156-a784-3df4-9e5c-62bb64e7312d | -14.1212 | -44.8933 | 2025-08-12 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 238.6 |
| 2650402d-77c0-3cf9-875c-04393682e10e | -8.5604 | -54.6973 | 2025-08-12 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d72e832d-3d0b-383c-81dc-ce55226013a2 | -5.832 | -52.1094 | 2025-08-12 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4ba39c1d-7208-3ba2-a1f7-7fd7f7b5c2c2 | -11.7896 | -51.9033 | 2025-08-12 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 201.6 |
| d178e188-5299-3bd8-aaeb-a5c06cc6762e | -13.8743 | -45.5643 | 2025-08-12 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 99f34735-35e4-381c-a4ff-d9580705d62e | -12.3565 | -59.8473 | 2025-08-12 14:20:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c1d557f9-1009-37c4-b4d8-1b43b0e8adb5 | -7.1482 | -60.1366 | 2025-08-12 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 8e48f919-ca1c-35a4-937b-e56fb1f81384 | -11.9493 | -43.4019 | 2025-08-12 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 207.5 |
| b36e34fd-fd3c-3e56-8c9d-086762d3a175 | -7.0799 | -59.1964 | 2025-08-12 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 5598d7ac-dc93-3156-9375-8ef45044e65b | -6.0992 | -59.9267 | 2025-08-12 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 4d3b3623-128d-3ee8-8bd4-28fbf8fe94d0 | -14.1027 | -44.8499 | 2025-08-12 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 8274effb-0c13-315c-9a18-1e07064ba87b | -7.1298 | -60.1374 | 2025-08-12 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 22941c3a-9868-33f5-82e0-bdc9fe51c646 | -14.1407 | -44.8899 | 2025-08-12 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| bd454410-a386-3202-ab23-c32fcaa49320 | -14.1017 | -44.8968 | 2025-08-12 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| f08d4c9e-0334-3b60-aed4-c76d5cf72bbc | -7.5671 | -49.3074 | 2025-08-12 14:30:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 120.8 |
| ba80c20f-5e3f-3e59-b570-8a695769b0c8 | -7.0614 | -59.1972 | 2025-08-12 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 6d6a3bbb-062c-3da4-9fa8-14b4ad036987 | -16.3153 | -52.9201 | 2025-08-12 14:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| a1bb1429-857d-3ec3-adb5-34c2f6f102bf | -11.7896 | -51.9033 | 2025-08-12 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 128.2 |
| c26803ad-de89-381a-9223-d07e91b1cb4b | -13.8743 | -45.5643 | 2025-08-12 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 579499c8-ad02-3b2c-8c4d-e51ea38e5ebb | -7.1483 | -60.1174 | 2025-08-12 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 142392da-8d6b-3da7-b9f8-a2897bb40729 | -7.0799 | -59.1964 | 2025-08-12 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 2ee52823-367b-3aae-ba05-5f5e337f6baa | -8.9873 | -46.5974 | 2025-08-12 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a647173a-b174-3422-b95a-2469a574fe3d | -8.5788 | -54.7162 | 2025-08-12 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| d0f1721a-5b4d-35c4-99cf-a7f5345c0a95 | -12.3565 | -59.8473 | 2025-08-12 14:30:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 84e0761b-5095-32bc-9f91-01361202a23f | -9.2079 | -59.6742 | 2025-08-12 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| eed7d681-4a74-30f4-802b-82cfdfe0cbed | -17.5701 | -45.3346 | 2025-08-12 14:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 7ef58959-cd53-37bc-b994-22a91edebe64 | -7.1299 | -60.1182 | 2025-08-12 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ccb5d4c3-cbeb-3e6d-b8f4-e43f1b62b7ac | -7.1482 | -60.1366 | 2025-08-12 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.0 |


[Clique aqui para ver as próximas entradas](README41.md)
