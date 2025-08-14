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
| b4737ade-434e-370e-b267-10c88a909421 | -22.18056 | -44.36259 | 2025-08-14 11:38:00 | TERRA_M-M | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| bb835f91-948e-3756-ae96-82197716fb0f | -21.33474 | -42.01486 | 2025-08-14 11:38:00 | TERRA_M-M | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e7a76e53-848f-3a50-b415-2e6a62ed4a35 | -22.17749 | -44.37997 | 2025-08-14 11:38:00 | TERRA_M-M | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 45b2e2b3-6e06-3e34-9620-bab9365c312e | -22.175 | -44.36859 | 2025-08-14 11:38:00 | TERRA_M-M | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| ffcb5d3d-d87d-31eb-b238-49f433bf838f | -21.50405 | -42.66013 | 2025-08-14 11:38:00 | TERRA_M-M | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 52452987-1327-39f6-97ed-418991180852 | -12.6891 | -44.9494 | 2025-08-14 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| dfeaa026-00dd-3144-ac68-b133fa5dd199 | -8.7382 | -44.0289 | 2025-08-14 12:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 83fbc3cf-f43c-398f-85c7-a51751966a76 | -9.1522 | -59.6578 | 2025-08-14 12:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| f761e5ba-f36c-334d-b7ff-9a1b40e81bf6 | -9.1522 | -59.6578 | 2025-08-14 12:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 8648cd89-0d67-3618-9c0d-ecd4bc7ac876 | -12.6891 | -44.9494 | 2025-08-14 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| a4d036f6-ef4e-3421-849b-a057b8fbcc71 | -8.7382 | -44.0289 | 2025-08-14 12:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e6f08b5b-8c3f-30fd-8072-4ef37dbf37cd | -9.152 | -59.6772 | 2025-08-14 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b5d35f69-04a6-34ba-afc6-c3d725184353 | -9.1522 | -59.6578 | 2025-08-14 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| e74103d6-4790-30a9-9991-1bbd47632e69 | -9.1522 | -59.6578 | 2025-08-14 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 94b37597-6ac8-3afb-8756-53efce4e082f | -9.152 | -59.6772 | 2025-08-14 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ab495916-f4ee-3fc3-ad68-42cabb871439 | -8.7382 | -44.0289 | 2025-08-14 12:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 0533fd58-ceda-3a42-adea-289342a4ee7e | -12.6435 | -45.3269 | 2025-08-14 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| ae0c7b3c-f9a1-34ef-92d1-51dd63948921 | -12.6891 | -44.9494 | 2025-08-14 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 9a35b240-1a30-34c6-b1cd-353865e48aca | -9.1522 | -59.6578 | 2025-08-14 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 629b1cc7-89d6-3e2f-bb95-dce7db974810 | -6.8956 | -59.1462 | 2025-08-14 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ed62120a-f2aa-3742-97c2-e0830a3e7e90 | -12.6891 | -44.9494 | 2025-08-14 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 4acbc436-85ad-32b8-bbbe-4c3dddc9d129 | -9.152 | -59.6772 | 2025-08-14 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 0b48699e-4691-364a-a0dc-97ab3f385dbb | -12.6435 | -45.3269 | 2025-08-14 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 2627bca9-1fdb-3e2d-8405-d2b1002f541f | -9.1708 | -59.6568 | 2025-08-14 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c3ace56f-6000-3ee6-b42d-c75d79ae7cfe | -9.1708 | -59.6568 | 2025-08-14 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 91276fe0-0fa7-3b5d-bd3f-bae2d5f86d1c | -9.1522 | -59.6578 | 2025-08-14 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 189.6 |
| b9e9cd59-ec97-33a1-b6e7-10962f8e120d | -9.1523 | -59.6384 | 2025-08-14 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 1c096ac5-d9d3-3721-9942-0d3ffc7677fc | -12.6435 | -45.3269 | 2025-08-14 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 458c8a47-1df4-3e09-ad52-1b96626396a0 | -9.1336 | -59.6588 | 2025-08-14 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| d2792b2e-d970-3ca1-9478-16ce05513a62 | -12.6891 | -44.9494 | 2025-08-14 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 5768413b-46b2-31bc-824b-ad7597ba12be | -9.152 | -59.6772 | 2025-08-14 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 70f3ec9a-9f2a-3b2f-af74-20fb0b819afb | -6.914 | -59.1455 | 2025-08-14 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0c4f2766-ae3e-36ee-ba44-b39d74a564b1 | -6.8956 | -59.1462 | 2025-08-14 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 868709f6-e728-3f46-8d79-e8d7a7c94f21 | -9.1522 | -59.6578 | 2025-08-14 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 2ef89c2f-c45b-377c-a60d-5259a7bf6404 | -8.7382 | -44.0289 | 2025-08-14 13:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b320bde2-916d-3105-b2b3-504ebb65c82e | -6.0991 | -59.9459 | 2025-08-14 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f6d8d712-5679-30e7-9a75-a3e8e8743eb2 | -6.0807 | -59.9465 | 2025-08-14 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| fde1f616-d27a-39e8-b9a2-a29dbdbf03f1 | -8.7385 | -44.0056 | 2025-08-14 13:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e2876544-7604-3736-a5d2-b6ec323cb806 | -12.6435 | -45.3269 | 2025-08-14 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 8b0681bd-b7d3-36ef-9419-26088fecfd90 | -9.152 | -59.6772 | 2025-08-14 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 2a7df1ac-5b6c-3587-8405-87273e9ec9c7 | -6.914 | -59.1455 | 2025-08-14 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 12b3c115-eaa1-3480-8e79-372d916f1f1a | -12.6891 | -44.9494 | 2025-08-14 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 176.7 |
| b77993c9-6ae1-3742-8a9f-262af2e1a324 | -9.152 | -59.6772 | 2025-08-14 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.3 |
| b35e3542-1b5d-3e44-874c-53a97611bb12 | -8.7385 | -44.0056 | 2025-08-14 13:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| b566a3cb-5ca2-3269-a430-8e2a95960b9b | -13.8937 | -45.561 | 2025-08-14 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 218.9 |
| b419f14c-780a-3c0c-8042-d49249fdf6a0 | -6.2959 | -41.6824 | 2025-08-14 13:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| c9f5b7ee-5e83-323f-aaf8-ccede0016cdf | -6.8956 | -59.1462 | 2025-08-14 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 9bf00c0b-8045-32b3-9111-c2fcf37efea2 | -9.1334 | -59.6781 | 2025-08-14 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 89dcc1be-1495-3df2-886d-bd06c48b367c | -12.6435 | -45.3269 | 2025-08-14 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| b2e540fb-386d-31b3-b218-c3aa3783e1af | -9.1708 | -59.6568 | 2025-08-14 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 48cc8908-05f8-3b8c-8da3-e6657882542d | -8.7382 | -44.0289 | 2025-08-14 13:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| dead5ab8-1cee-32e1-b3fe-6611fae1a978 | -6.8771 | -59.147 | 2025-08-14 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 82da687b-c414-3989-87e3-d06cc926a951 | -9.1522 | -59.6578 | 2025-08-14 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 164.4 |
| ab4a1b1c-e353-3f71-8ae9-ac07209ed81f | -6.914 | -59.1455 | 2025-08-14 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 14cf1877-183d-3953-9455-3f8ebaf0aa20 | -13.8743 | -45.5643 | 2025-08-14 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| c23357a1-401a-3838-a443-2682f81971a6 | -6.8771 | -59.147 | 2025-08-14 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8dc3ec25-f0d0-3d42-a0e7-8258fee63478 | -6.2959 | -41.6824 | 2025-08-14 13:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 155.7 |
| ef497160-7a77-3c2f-b441-be5e234e8232 | -12.6891 | -44.9494 | 2025-08-14 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 217.6 |
| fbd71e80-504e-38d3-8cc3-61b450858ba3 | -9.1336 | -59.6588 | 2025-08-14 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 205.1 |
| 03da4faa-8efe-3637-a37e-656d9f71498f | -6.8956 | -59.1462 | 2025-08-14 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 8fcb739c-5632-341d-aa16-ffb35b643d96 | -8.7572 | -44.0267 | 2025-08-14 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 1d9058a6-c3f7-3ec1-8ab3-e3df37f1fe79 | -12.6435 | -45.3269 | 2025-08-14 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| b9390604-9f53-3787-8353-17b2f07de1e3 | -6.0807 | -59.9465 | 2025-08-14 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a8890920-307b-3829-9c94-0a12471b34c0 | -9.152 | -59.6772 | 2025-08-14 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 177.7 |
| e3ddf7e5-4dd1-3542-99e6-449392423a37 | -9.1522 | -59.6578 | 2025-08-14 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 191.1 |
| eceb421d-f433-3407-a3d5-18128c4ed001 | -6.914 | -59.1455 | 2025-08-14 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| c3dd827f-61ae-3bc8-bf57-dd211e8a059f | -9.1334 | -59.6781 | 2025-08-14 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 307.9 |
| 403b6a50-88cc-3f0b-ab39-b04be47ca01f | -8.7385 | -44.0056 | 2025-08-14 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 789bfbfa-630f-38c8-a05d-916a2c723382 | -9.1706 | -59.6762 | 2025-08-14 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 13616b46-f915-37f0-86e2-d0c494935e5e | -6.0991 | -59.9459 | 2025-08-14 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 6455ec72-ab1d-379e-9341-6ce91f1de2da | -6.0992 | -59.9267 | 2025-08-14 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f1d70b2e-6bdc-3825-a0eb-d337091e9f51 | -8.7382 | -44.0289 | 2025-08-14 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 537714e6-8111-3faa-aa50-12e214253325 | -12.0462 | -43.3626 | 2025-08-14 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| a2621489-1c3d-34d9-92b3-7c9f5c87712c | -9.1708 | -59.6568 | 2025-08-14 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| cc5d3259-b99b-3c55-9307-b419501adcfe | -7.33 | -60.6273 | 2025-08-14 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 26044085-7194-3914-b6f5-b956b973c8f5 | -6.0991 | -59.9459 | 2025-08-14 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| fee7a7ac-bc09-3029-a254-634ef8bef908 | -6.914 | -59.1455 | 2025-08-14 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| dd530d03-c3d2-3239-9b06-1401d2d5e051 | -7.33 | -60.6273 | 2025-08-14 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| f1e68f78-6b7e-3f81-9c6c-3bbcef0b7679 | -8.7382 | -44.0289 | 2025-08-14 13:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 7b32da2e-c1cd-3b97-b256-86f46e7e15b3 | -6.0807 | -59.9465 | 2025-08-14 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 7d9b7671-bcd5-32af-bc50-a566f1594490 | -12.6435 | -45.3269 | 2025-08-14 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 72044bf4-a856-3382-b322-175c6adae439 | -8.7572 | -44.0267 | 2025-08-14 13:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 42a40967-37dd-382c-8065-0c40480656c1 | -6.2959 | -41.6824 | 2025-08-14 13:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 142.5 |
| 4e017bd2-5391-33de-a0dc-8d9f390769cb | -6.8956 | -59.1462 | 2025-08-14 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| d0ec3e9a-07c5-3d96-9abd-734c38929e9c | -12.6896 | -44.9261 | 2025-08-14 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| a828e27f-29e8-3f6d-b0ae-5054478adb3c | -6.0992 | -59.9267 | 2025-08-14 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 4532c2ba-d43f-399f-9711-3328f88ff6d1 | -12.6891 | -44.9494 | 2025-08-14 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.2 |
| d0154f9b-95bd-3271-906e-2bec1d04d2f9 | -7.3116 | -60.628 | 2025-08-14 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b1818156-1ce2-3340-9846-67150af96af6 | -8.7385 | -44.0056 | 2025-08-14 13:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 3f9ac3b0-1ec0-3cad-a171-58b02d2493f8 | -13.8743 | -45.5643 | 2025-08-14 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 5748d0f0-82ae-3ded-bbf6-e9a5a1e34eb2 | -6.8771 | -59.147 | 2025-08-14 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3e48bd1b-7821-377b-acfe-5cf2576ebe10 | -6.8957 | -59.1269 | 2025-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 67c2af26-7439-38cd-88d1-ea6b97748d07 | -6.0807 | -59.9465 | 2025-08-14 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| e311efda-38f5-3cec-ab49-a22b4da9acc5 | -8.7382 | -44.0289 | 2025-08-14 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| b854fc11-21b2-3ae9-8634-087af9f4197e | -8.7572 | -44.0267 | 2025-08-14 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| d2d103ed-b3ed-37e5-8941-044c2e199ce3 | -6.8956 | -59.1462 | 2025-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 32b1cb67-e290-3c34-ad00-c93905cf6fdd | -6.9141 | -59.1261 | 2025-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ce6d8787-f3c5-38bd-9524-243c4b163132 | -7.3117 | -60.6089 | 2025-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c07b68ec-5c46-3079-b094-0b38cafbb238 | -6.914 | -59.1455 | 2025-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| c1eb4c6b-1d91-3fac-a48a-18cfcf60a0be | -6.0808 | -59.9274 | 2025-08-14 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |


[Clique aqui para ver as próximas entradas](README41.md)
