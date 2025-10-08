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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea6047ee-6513-3990-9235-e449395b052d | -14.7179 | -46.0867 | 2025-10-08 12:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| a844bcdc-0f2d-3d86-9069-cec3bf32b32d | -11.1644 | -54.8804 | 2025-10-08 12:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 179.3 |
| 7bddb886-2c3f-36ef-b729-d8dcc382b6a4 | -11.1455 | -54.882 | 2025-10-08 12:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 7882c915-5b51-3949-848c-777b50d17183 | -13.2855 | -48.0381 | 2025-10-08 12:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 09d0b695-87bd-3420-a05a-eeec737a8755 | -11.1642 | -54.9007 | 2025-10-08 12:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 7b8110a1-b91a-3b1a-8bcf-f751a81ee0da | -13.0009 | -46.7795 | 2025-10-08 12:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a973d5df-87a1-35ce-8bc4-5350fb8b900c | -10.4245 | -45.3907 | 2025-10-08 12:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b667892e-1878-3605-b575-47c08c8fa730 | -15.2811 | -45.3337 | 2025-10-08 12:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 91c21661-a991-371c-a764-15afd5d319d9 | -10.9106 | -47.1353 | 2025-10-08 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c15179e9-45ff-329c-a4e2-736b369356cf | -14.7184 | -46.0636 | 2025-10-08 12:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 22de8637-7049-33aa-a997-27ca43191def | -13.7923 | -45.7859 | 2025-10-08 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 7ee8c863-ae6c-3d86-b2d5-7ebc622ba33a | -13.8117 | -45.7826 | 2025-10-08 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 29cdb27d-ff0d-337d-9272-12f2b2052398 | -13.2662 | -48.0409 | 2025-10-08 12:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4465dda6-2c39-37e3-b04e-f88808b56f79 | -11.183 | -54.8991 | 2025-10-08 12:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 6b70fa3b-3447-36cd-9913-89d4ad7fea81 | -13.8112 | -45.8057 | 2025-10-08 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 15c92eeb-a28a-3246-8175-880bebbd38b6 | -13.8343 | -51.8529 | 2025-10-08 12:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 201.3 |
| b2b72dbd-2ef2-36d3-981a-e31ef1e278a6 | -13.7364 | -45.68 | 2025-10-08 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 10f81eae-78dd-3952-b58f-f0466f031b18 | -12.5107 | -54.7345 | 2025-10-08 12:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 2000153c-fa85-309c-8def-3c6efd9191c5 | -9.0016 | -45.5148 | 2025-10-08 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| f85c17c9-73b1-30ff-a5b4-0396e7e21044 | -13.3513 | -47.6042 | 2025-10-08 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a3834b58-8366-3778-9bbc-6105147aa0ab | -11.1642 | -54.9007 | 2025-10-08 12:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 225.2 |
| 88f3c704-9408-36b4-b475-16215b76d16e | -12.5109 | -54.714 | 2025-10-08 12:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 1d32c300-122b-3cb0-888f-fe19bc8d2f5c | -14.7179 | -46.0867 | 2025-10-08 12:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 8ca1ba4b-45ae-37f8-be79-2e3a3789696f | -13.7364 | -45.68 | 2025-10-08 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 42d54d72-82e4-37f1-a5b8-644680cc8623 | -12.5107 | -54.7345 | 2025-10-08 12:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 963162be-6924-339f-90bf-336a14ca6f48 | -13.0939 | -47.9992 | 2025-10-08 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| d9aa487e-ef59-392c-938a-3d4404ef8caf | -10.4245 | -45.3907 | 2025-10-08 12:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6f600f47-a1f2-3b7b-88da-295d5aaa89f9 | -10.9296 | -47.1329 | 2025-10-08 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| cf7017be-d6b3-3570-aa3c-2710622c5170 | -14.7184 | -46.0636 | 2025-10-08 12:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 117.4 |
| c751d2d8-33dd-3a78-8574-66fccda14685 | -11.1644 | -54.8804 | 2025-10-08 12:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 267.0 |
| ab2ca77c-ef58-31bf-a848-9513fcf2e877 | -17.5828 | -47.1762 | 2025-10-08 12:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 103.4 |
| f91e7902-99c1-35bf-98fb-b6129a55dcb9 | -11.183 | -54.8991 | 2025-10-08 12:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 173.5 |
| e0d406bb-dace-35b0-b874-1dd00878b01f | -13.0743 | -48.0243 | 2025-10-08 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 8664404d-7969-362a-9ac5-4cf914d8fef3 | -14.211 | -43.4573 | 2025-10-08 12:10:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7c5dc241-9fc7-3b7b-a2ae-e8fce20b0658 | -13.2662 | -48.0409 | 2025-10-08 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 6bbd950d-7444-329e-9f18-2abfad8b7c0b | -13.7368 | -45.6569 | 2025-10-08 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f49bcba9-f651-36e3-9ce7-000090fd5d48 | -15.321 | -46.1622 | 2025-10-08 12:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b490d509-ffe4-3ffc-b412-f7fe082ad268 | -14.3884 | -46.0294 | 2025-10-08 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 8e074cf6-07bc-30e6-a83e-296fb6915dab | -10.8732 | -47.0953 | 2025-10-08 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| b5c5ea16-1eed-3c0b-8818-5ca4b4006513 | -9.3343 | -48.9364 | 2025-10-08 12:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| e16c5db0-cb9d-3dfb-b502-edb58c14ffd2 | -11.1833 | -54.8787 | 2025-10-08 12:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 1d108c90-2f7c-3ebb-aef8-08fe74b25e49 | -13.2855 | -48.0381 | 2025-10-08 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f8b452fa-2b78-37a4-a46e-c248980a5413 | -11.1646 | -54.86 | 2025-10-08 12:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 4bf6483b-15af-32c1-969c-a0d968be2507 | -13.8117 | -45.7826 | 2025-10-08 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 54d25f9e-3e3e-373f-bdfc-b044b9bac345 | -12.5297 | -54.7326 | 2025-10-08 12:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 22637f70-7b27-39b1-b98f-a2e9690a3deb | -13.0935 | -48.0215 | 2025-10-08 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| d729ed4f-7610-338b-a638-2b72b6f41fa4 | -11.1455 | -54.882 | 2025-10-08 12:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| d2d66a41-14e9-3838-8fea-130e7e527824 | -13.8536 | -51.8504 | 2025-10-08 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 6a1cbd35-b6f0-32af-8b29-52c9638df608 | -15.748 | -49.0083 | 2025-10-08 12:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 4706c6ff-b343-301f-97e1-1c0982197e80 | -10.8732 | -47.0953 | 2025-10-08 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b340ebb2-379b-3641-a566-eec98d404fbc | -13.2855 | -48.0381 | 2025-10-08 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 0a3f6b59-8011-39b2-9d39-020f7a421548 | -11.1833 | -54.8787 | 2025-10-08 12:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 190.9 |
| 0fcfda61-0a1c-31d4-9c8a-285120c28522 | -11.1646 | -54.86 | 2025-10-08 12:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 3da157e6-c9fd-3953-b30e-41765cb12d3b | -14.7179 | -46.0867 | 2025-10-08 12:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 3e49a3f7-5a54-3385-92dd-761a4656867a | -9.3343 | -48.9364 | 2025-10-08 12:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 5beabd6d-e4c2-305e-beaf-08cf6602cd7a | -11.1644 | -54.8804 | 2025-10-08 12:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 396.1 |
| be34dcb4-f340-31ee-84f7-e055a7f6c99c | -8.5395 | -46.2406 | 2025-10-08 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 80e861dc-932a-3b49-9d55-b26fff21d623 | -17.5828 | -47.1762 | 2025-10-08 12:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 7eaaa9de-c23e-3acd-9267-0609ebc61ae5 | -11.1455 | -54.882 | 2025-10-08 12:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 8373027e-de95-304b-bc47-b9ce5b00a7c0 | -8.5207 | -46.2425 | 2025-10-08 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 19b755bd-20cc-3baf-845e-4a735c50343c | -11.1642 | -54.9007 | 2025-10-08 12:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 477.3 |
| a3625690-304b-3ade-a7cc-9fae2a0385a8 | -14.7184 | -46.0636 | 2025-10-08 12:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 143.8 |
| cc9e4bf8-361d-3331-9a5a-f989bfbbeb81 | -13.7918 | -45.809 | 2025-10-08 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 69ef198d-9a85-35e0-b929-ebaa1fd2c0dd | -11.183 | -54.8991 | 2025-10-08 12:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 228.3 |
| fb5ca923-e15b-32c2-aade-9d475103e2c2 | -12.5107 | -54.7345 | 2025-10-08 12:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| d3453b6c-66f8-3b1d-b0bb-96783340f3e9 | -12.2525 | -47.8728 | 2025-10-08 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 78cde30f-372b-3e14-881a-99b8ab79ca7a | -17.954 | -44.4124 | 2025-10-08 12:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9c7c43b5-764d-3c3e-9c87-3639330fcc6c | -13.8112 | -45.8057 | 2025-10-08 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| dfa2e3ce-f343-3a08-9ecb-b89601dc4650 | -13.2662 | -48.0409 | 2025-10-08 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 634303b1-5941-3c63-990b-f24ade88696a | -10.4245 | -45.3907 | 2025-10-08 12:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| cbe3e3c8-4c41-3327-886c-a3fc8dba6a56 | -13.7364 | -45.68 | 2025-10-08 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 330b68d4-b59c-3523-b0d7-e7a1e6640965 | -8.9309 | -46.5809 | 2025-10-08 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c5fa4e05-506d-3d95-90d5-d2b1b294cc46 | -8.5398 | -46.2181 | 2025-10-08 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 41d37f6e-ac97-3090-b16b-cb425dd7e859 | -12.4267 | -45.6136 | 2025-10-08 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 749e8902-af66-3746-804a-f622f9c3f77f | -8.6295 | -45.1 | 2025-10-08 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7eac8445-cad0-34f8-9b08-9adc0ec15303 | -13.8117 | -45.7826 | 2025-10-08 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 16d549f6-b398-3942-bafa-9aaa7c5640ed | -14.6983 | -46.0902 | 2025-10-08 12:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 34f5f6cb-f95a-35ed-a82f-5b1592897e12 | -11.1642 | -54.9007 | 2025-10-08 12:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 601.1 |
| b5cdbca6-1b50-36eb-9142-c1b1acdfe07c | -17.954 | -44.4124 | 2025-10-08 12:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 040f8427-c880-3bfe-b453-0526574301ad | -15.6198 | -52.5715 | 2025-10-08 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| eac5970c-fe06-32d2-91d4-db6b15afd9f1 | -13.8117 | -45.7826 | 2025-10-08 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 434fc9fa-50d2-3fcd-83df-eead094669f6 | -10.9106 | -47.1353 | 2025-10-08 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cf0cd84d-abca-34d6-a8e2-3503b5f0acb7 | -14.7184 | -46.0636 | 2025-10-08 12:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 706f6103-c212-3df8-9024-7e5510d3cfe3 | -13.2855 | -48.0381 | 2025-10-08 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6ca58f7a-c075-3409-b1b7-f2a63d617f62 | -8.9309 | -46.5809 | 2025-10-08 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 80c7f0f3-8707-3321-86a7-67fc5ba8ea87 | -8.9121 | -46.5829 | 2025-10-08 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 76189db1-4ce4-3cfe-8ac2-e91b8be38736 | -9.3343 | -48.9364 | 2025-10-08 12:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 61595d55-9b27-37a6-bbc1-74a12e3d120b | -11.1833 | -54.8787 | 2025-10-08 12:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 343.7 |
| 29ed36ba-47e9-323a-88b5-09f2f87a18e3 | -8.6295 | -45.1 | 2025-10-08 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| fb977b55-cab2-38a4-aded-826d9cda1076 | -11.1455 | -54.882 | 2025-10-08 12:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 1dfc51a2-6360-3400-92b8-de13a4f70cb7 | -9.2096 | -46.9084 | 2025-10-08 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| d341c7d0-69f0-315a-8076-d15dcdaaccb7 | -8.4827 | -46.2688 | 2025-10-08 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 16d304c0-4958-3c2e-8e0f-1547c3a3560f | -14.7179 | -46.0867 | 2025-10-08 12:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 295.8 |
| 34062832-7f36-3df1-b55a-7fff60008bf8 | -13.8112 | -45.8057 | 2025-10-08 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 500dc3a7-f836-375b-87af-f1256689406b | -13.7359 | -45.7031 | 2025-10-08 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 5a9ee774-fa7d-3cbd-a235-150349487ac8 | -13.8343 | -51.8529 | 2025-10-08 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 5027d2c8-047e-3a62-9f5a-38c11e5c8e7b | -8.4824 | -46.2912 | 2025-10-08 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 72cf3e37-41cc-3d79-b510-724aeea77b46 | -10.4245 | -45.3907 | 2025-10-08 12:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 17758a46-2c81-37df-bafe-378444379652 | -14.3889 | -46.0063 | 2025-10-08 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 2dd3a797-b5d3-34e5-8d21-7b34a5dcbc73 | -13.7364 | -45.68 | 2025-10-08 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |


[Clique aqui para ver as próximas entradas](README101.md)
