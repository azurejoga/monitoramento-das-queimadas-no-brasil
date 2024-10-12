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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8041b23f-89c2-3b1b-88a1-cbf31658364c | -8.74831 | -60.48397 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 127d6d30-ffaa-32e0-94b4-3694055292f0 | -8.74498 | -60.48345 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b0ac1f4-0fc8-380e-b500-dfd74fd6bad5 | -8.74443 | -60.48695 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d1a6af9-870f-3d73-8e68-a98827aa9105 | -8.6436 | -60.74324 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ea62ade-80f7-3245-a0f5-1bcaff058953 | -8.64305 | -60.74673 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9d332ad-7a1c-35b4-9cdc-a06b32e4fa71 | -8.80029 | -60.15003 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fc4d2f0-c490-39d6-bcfe-05b83131aed1 | -8.79975 | -60.15354 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc215173-4b64-3699-a928-fb3d7c74ca1c | -8.79749 | -60.14602 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6aeb81e6-6d57-3404-9efd-b7a897ba807e | -8.79695 | -60.14954 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7b12a9f-6116-30ef-82a6-14442b84b664 | -8.7964 | -60.15304 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a038e2f-cc66-34ac-9820-48a10eae09d9 | -8.79586 | -60.15655 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81884397-0671-3fa4-9bad-2c34b0f82406 | -8.79415 | -60.1455 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09099f03-1b04-3f1e-9443-05c2c6c9488a | -8.79306 | -60.15252 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7e4eae4d-c462-3aff-9a1f-d70837ff9937 | -8.79252 | -60.15603 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 802f7dfb-79d0-328f-91b7-6821b62cf7b8 | -8.79197 | -60.15955 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 856677d2-1f14-3f34-83c9-13801f5dd4a4 | -8.78802 | -60.14087 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f31bda5a-ab9c-39a0-836e-48683ef8f3d3 | -8.78468 | -60.14033 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc5cbdf1-df11-3c8c-8253-64c98cfe538b | -8.78134 | -60.13978 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 511f44d1-23d1-3df6-986a-7a5bb520e63a | -9.38684 | -60.91822 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a1b64f2-843a-3496-a313-4f058d3061fa | -9.46588 | -60.54287 | 2024-10-12 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f135177a-eb62-3f37-9ca5-8aee46f68130 | -9.39568 | -60.90529 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5a9b2bd-3509-3a21-8ec2-867df660461c | -9.39513 | -60.90879 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48a862a4-9233-3ee2-aa43-2d7d6bb307bc | -9.3929 | -60.90126 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3cfd172-c15e-39fd-bd50-c792b5f95f29 | -9.39235 | -60.90476 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5d2dc4a-8c94-3d03-bdb8-73c6bb3021a5 | -9.39071 | -60.91525 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9db5629-dc16-3174-a6ce-8492a19ed45f | -9.39016 | -60.91875 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f82303b-365a-3f31-b65e-a695f2cce965 | -9.38958 | -60.90073 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b2d8974-4123-3843-9afe-1c356ce01b21 | -9.38903 | -60.90424 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0d20e6c-f467-358b-b0e1-69a79a4ba141 | -9.38848 | -60.90773 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7062c794-3286-3ea3-a6a0-5e61e2554025 | -9.38793 | -60.91123 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79b0afcc-06a8-3e82-a940-8361e3c07548 | -9.38738 | -60.91473 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 649023c8-346b-3e4c-b517-22373d064790 | -9.38715 | -60.90067 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ef33770-ea50-3762-9dde-d0c909c3792c | -9.38702 | -61.04725 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c50a183d-25b5-37a6-9f52-619cbccf74ee | -9.3866 | -60.90416 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 225a0592-8958-3292-aa5c-3144fc824987 | -9.38605 | -60.90766 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 380bc14f-8f76-34f0-9195-b5ddd3963c76 | -9.47767 | -60.37865 | 2024-10-12 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bcac128-c908-3ea1-b35c-8a7fe6a581ac | -9.41763 | -60.28988 | 2024-10-12 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5da46e1-25b0-3991-9a27-ec8775fc91d8 | -9.78734 | -59.81545 | 2024-10-12 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b5c5737-77c1-3de0-a37f-2da21842e930 | -9.78451 | -59.81128 | 2024-10-12 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 652e219c-1cfc-3ed8-b289-1b27749e9f34 | -12.14879 | -60.74621 | 2024-10-12 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ffa6d9fb-e110-3549-a85e-bdb0a534bbe4 | -12.14544 | -60.74569 | 2024-10-12 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b9615bf-a405-3af0-af9b-d06499722af2 | -12.14209 | -60.74517 | 2024-10-12 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4188df0-90dd-356a-a33c-849d8c184b6a | -13.73561 | -60.60418 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54a0cc42-fca4-31b8-9a94-c72095237119 | -13.73504 | -60.60788 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6fa4316-514d-39db-b02a-af0cf74793be | -13.72771 | -60.63325 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3bc48388-1b08-3dae-ac25-311728277d47 | -13.35311 | -60.57542 | 2024-10-12 05:23:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5ed816f-6d1a-3f8a-98ba-38d55ee6eead | -13.35256 | -60.57903 | 2024-10-12 05:23:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56224c0e-412f-3830-9bba-346ce0762cd1 | -13.35201 | -60.58266 | 2024-10-12 05:23:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d58d2b77-e48d-3382-be18-58ef8f7cc350 | -13.34972 | -60.57491 | 2024-10-12 05:23:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9ef2c65-2592-3346-9206-745439687d79 | -13.34917 | -60.57851 | 2024-10-12 05:23:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec411772-f9f3-3b25-a588-b6a039642e67 | -13.34862 | -60.58214 | 2024-10-12 05:23:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea00e9b0-5b21-39d7-920e-79b840a13e7c | -13.34687 | -60.57079 | 2024-10-12 05:23:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b895726f-7111-3734-a1c5-3b5c28d2f424 | -13.34633 | -60.57439 | 2024-10-12 05:23:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ca39bf6-d648-3ee9-9720-1a5faa3202ef | -13.34578 | -60.57799 | 2024-10-12 05:23:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a6ee9d8-613d-358d-9455-5497d7218a90 | -12.83543 | -60.83529 | 2024-10-12 05:23:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15bf0e29-523c-3620-820f-b4982aa36fdc | -12.83263 | -60.83113 | 2024-10-12 05:23:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e4fb6b6-d853-3a9d-8c73-a22e7bd1b364 | -12.83207 | -60.83475 | 2024-10-12 05:23:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b0c9ecaf-af31-33a1-b083-758419273fd2 | -12.68723 | -60.84893 | 2024-10-12 05:23:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7814e1f-4173-3ee6-b817-6b675d4c430d | -13.08427 | -60.48586 | 2024-10-12 05:23:00 | NPP-375D | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8e11edf-6287-376c-8334-927bbe103449 | -12.8676 | -60.51255 | 2024-10-12 05:23:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3ef4eeb-7f39-3f7e-b8df-b587dc83c537 | -13.73956 | -60.60102 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3bf66da6-1f41-3adb-bfbe-ba0b9859c757 | -13.739 | -60.60471 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fea587c-a0d7-3999-a4eb-262e316697c9 | -13.73617 | -60.60048 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d7836ba1-d123-3315-9cea-a889e9cb546f | -13.73448 | -60.61158 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 274117ca-3063-378d-97ea-2b769e69667e | -13.73278 | -60.59995 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88b6bc2d-9cdf-3d22-9531-65520b07f71c | -13.73221 | -60.60364 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5a9ae6f2-4c96-3030-a3ff-b178ecb7cc01 | -13.73165 | -60.60734 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ec1405a0-26ba-345a-b66f-7843e700fca8 | -13.72998 | -60.64118 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5ff42d9-2d8d-37aa-8446-5eca3d1f0f09 | -13.72715 | -60.63694 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 854aacd6-cc85-3da6-80d6-fc27edaaaf6a | -3.45685 | -60.59546 | 2024-10-12 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c8b7771-1c68-34a8-98e7-0a01c49c1309 | -3.4563 | -60.59897 | 2024-10-12 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15a914a1-4c0b-3e14-9b94-8bbab8102308 | -3.44793 | -60.58688 | 2024-10-12 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b1724c1-0295-31ef-afbf-1b330691eb4e | -3.37715 | -60.64407 | 2024-10-12 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19fb2d79-88b4-3287-95b5-7716b6b5f417 | -3.24616 | -60.7105 | 2024-10-12 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7ed792f-f51e-3885-8e4a-367afa89b718 | -3.24561 | -60.71402 | 2024-10-12 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6089e806-e27e-32e8-ab5c-c143e22c6e6f | -3.20236 | -60.38045 | 2024-10-12 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43f8e7a5-8f77-3e28-b9c6-b558bb770dd0 | -3.11517 | -61.10225 | 2024-10-12 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6b1225b-4878-3bce-9031-061829ca597f | -3.08581 | -61.0427 | 2024-10-12 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fe121c5-5b23-3210-935a-358bfcbfd4b5 | -3.56408 | -60.10659 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e78c38f-e8dd-368b-a557-e6e7e4162b28 | -3.52001 | -59.97873 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7390dd2a-ddc4-3c44-b9e6-0141e7b5deef | -3.51947 | -59.98218 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d121c4d7-fe5f-329a-bd7c-d2ab7f86fd2a | -3.08473 | -60.29439 | 2024-10-12 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43f3adf1-06f7-399c-8fc9-70ad4eb36083 | -2.91461 | -60.08235 | 2024-10-12 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a97eb074-6bbb-30e0-a2af-9dee3a19becc | -2.91137 | -60.08538 | 2024-10-12 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bca6cd83-7748-33c2-ae95-6a209293b504 | -3.78922 | -60.11677 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d1d9cbb-f73f-3ffa-b76b-7fac844efdd0 | -3.78038 | -60.12957 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e378721-e9e0-3ce6-91a0-e9328359cf7c | -3.77706 | -60.12905 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 930096ea-9dbf-3e6c-887e-44145fb129ec | -3.77374 | -60.12853 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbecabee-bc30-3e8f-ba85-4076863a2e15 | -4.00855 | -60.37888 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d19eb4fa-d6c8-3bcb-ab79-40f116f449ce | -4.00523 | -60.37836 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b17632de-55dc-3f76-b8fe-06ce4528686f | -4.00413 | -60.38531 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef40a736-092d-3635-a22b-acebdaa4964e | -4.00025 | -60.38826 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66c437b0-e513-3d1f-afcd-ca77e05037f5 | -3.9997 | -60.39173 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eadb373c-b639-32dd-83dc-e4c33dda46df | -3.99802 | -60.38078 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6acde527-412b-3d4f-a340-f4c101d1ae81 | -3.99747 | -60.38426 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2625bb0-fa8f-3a94-ac6a-f426d0319597 | -3.78867 | -60.12023 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad64257d-ce2d-3f8c-afe8-22066d1e5649 | -4.77241 | -60.74457 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3cffc67-dbaf-3b5b-a99b-207841c96642 | -4.76907 | -60.74404 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36daadc8-274b-392c-a12e-2aaab7131416 | -4.73332 | -60.78153 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34440073-5730-30b5-99e8-8e67b94c9a13 | -4.73166 | -60.79203 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README112.md)
