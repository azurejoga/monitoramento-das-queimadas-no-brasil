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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 229e51dc-93c2-3e52-b138-9a1fa17037ec | -3.25102 | -53.06548 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7e5fa6d-1a4b-30ea-8f8c-f00d922ff256 | -3.25058 | -53.06842 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13cee793-c4dc-3574-9d67-593ed6bfc19a | -3.25014 | -53.07134 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b22c8297-9917-36d1-91bf-639c14842476 | -3.24971 | -53.07422 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b87642c9-014c-3094-92fb-60d9b7614781 | -3.24927 | -53.0771 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03f64dcd-0350-3915-8c4d-981be66be1a3 | -3.21371 | -53.00298 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4139b479-5936-3701-aff4-c812cb611ac5 | -3.21327 | -53.00594 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0f4ca3a2-4c1a-3396-b550-10f626460b5a | -3.20864 | -53.00212 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67a5632e-5908-3489-9c69-d6f602dacb49 | -3.20821 | -53.0051 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff132d0b-0420-3816-8b72-e72718fed18f | -3.06261 | -53.16006 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 554999ea-c858-3426-9495-afa1938df6dd | -3.05843 | -53.15886 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c9d18800-9470-3fa0-b933-9892473d8b60 | -3.0576 | -53.15931 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 75fb26da-0d2e-3f3e-bd28-bc8f2dd83c4c | -3.05756 | -53.16449 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d71ee96-c710-333a-820b-57a3b67bc814 | -3.05678 | -53.16494 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 814f5d55-5f5d-3927-bc57-fbcb2f468537 | -3.05255 | -53.16376 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0c869f0-39aa-3854-8b2f-236e47bdaf3e | -3.05177 | -53.1642 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a52e8628-a2ee-3dec-ade1-2ffe361a862c | -2.99624 | -52.3719 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e975eb54-d4b3-3e10-8366-e4d98cb3422a | -2.99146 | -52.91695 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd136954-17a1-3394-9cd8-76772d4c90cf | -2.99095 | -52.37114 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b2a8059-6d67-3f2b-8908-0d99d9350e61 | -2.98895 | -52.91167 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ea5f86d-d5e2-3037-8711-903590183a45 | -2.9885 | -52.9146 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c2cb048-d4c3-3d4a-99e2-7da364c99c00 | -2.98805 | -52.91751 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c30af66a-7060-340b-8397-bb1a0e5a3734 | -2.98721 | -52.91042 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f882416-71e1-3e4e-bacf-62a7d24384d3 | -2.98678 | -52.91338 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee941e10-0366-3671-bb4e-02d92018b942 | -2.98635 | -52.91631 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97fb2585-6cce-3996-a33b-67c991283882 | -2.98339 | -52.91395 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e89ab9bd-47a5-3c0b-92cf-94d69c7487aa | -2.90959 | -52.59564 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61cb7a58-67b1-3f1d-8e7c-1407866f4aed | -2.87996 | -52.89207 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45e4d6aa-249c-32c8-a270-d640e99ee231 | -2.87949 | -52.89514 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 109131c1-e4d8-3372-b778-054870f9bce3 | -2.87783 | -52.88888 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 208b9184-096a-3b94-bc80-83b1c84dfab4 | -2.87739 | -52.89194 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 405a4783-4920-3153-a548-d218613bd687 | -2.87694 | -52.895 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38750ddc-85a3-3c24-8756-7327870cd4bb | -2.87488 | -52.89127 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b94cdc45-1d1c-3abe-9cf2-99cf8133ce9a | -2.87442 | -52.89428 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20c5cf68-0a27-39c5-acc5-baf229115cbb | -8.03316 | -71.32493 | 2024-11-02 05:29:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9bf98650-aa46-3573-93f5-33738277b7db | -1.2014 | -53.9184 | 2024-11-02 05:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| e7834eac-b401-31bb-b6f9-8f89e0676572 | -1.6002 | -47.2234 | 2024-11-02 05:35:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| af4fdbc1-e1d2-3bcf-a3bd-ec6f9c02cf6c | -2.2663 | -53.7422 | 2024-11-02 05:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 6924fa66-7863-3773-b3f4-75c8b0f8b495 | -3.0726 | -45.1405 | 2024-11-02 05:35:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 106.6 |
| b610a134-7686-3afd-87b7-482f34ae6ad4 | -3.0727 | -45.1179 | 2024-11-02 05:35:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ebd57a28-e95b-354a-a7f4-2b02b245ad62 | -3.1281 | -54.266 | 2024-11-02 05:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| bf5e4f57-850f-31d0-bd45-016844ee6e81 | -3.2047 | -53.4179 | 2024-11-02 05:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| afef0d36-530d-3a25-835a-317d2293bda4 | -3.2231 | -53.3972 | 2024-11-02 05:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| b31138d1-dccb-3db9-b72f-7f1019cb858e | -3.2415 | -53.4169 | 2024-11-02 05:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 071a1541-0d64-31af-9d03-24c947bc9e73 | -3.2599 | -53.4164 | 2024-11-02 05:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| cf91a52b-05f1-31de-92c4-d9f22b68f50c | -3.2415 | -53.3967 | 2024-11-02 05:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| aa09c16d-3fe1-3805-824e-c7b135a93433 | -3.9473 | -48.3666 | 2024-11-02 05:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2b788283-a02b-35a5-9028-384a024ab729 | -3.9474 | -48.3451 | 2024-11-02 05:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| fb6d78aa-7c46-3333-81d8-cf0c61fa7a3c | -4.3537 | -48.6068 | 2024-11-02 05:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7d057eba-c04a-34c0-96a3-76893719f1cb | -4.5577 | -43.0928 | 2024-11-02 05:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e9fe384b-1e6c-3e76-ae96-8cc215ad0073 | -1.2014 | -53.9184 | 2024-11-02 05:45:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 043858ca-b2ba-3107-8caa-8ecfed46ec6f | -1.6002 | -47.2234 | 2024-11-02 05:45:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b1289e4d-4d22-3a5f-8d4b-3c39aa336be5 | -2.2663 | -53.7422 | 2024-11-02 05:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| cb22a571-a183-390f-82d2-733cf8051033 | -3.0727 | -45.1179 | 2024-11-02 05:45:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| df5dd5bc-f7dc-3d7c-af98-a70abe4debfd | -3.0726 | -45.1405 | 2024-11-02 05:45:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| eb2f955d-f8e9-3e28-a64c-c85e2db48b75 | -3.2047 | -53.4179 | 2024-11-02 05:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| dafa13b3-73d0-3db1-acb8-476eca20e518 | -3.1281 | -54.266 | 2024-11-02 05:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 0c0984ef-7907-3e12-992e-5523850d7917 | -3.2415 | -53.4169 | 2024-11-02 05:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5577ce18-9a4a-31aa-8d3e-64c036d2d6c6 | -3.2415 | -53.3967 | 2024-11-02 05:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 87d47880-1227-399b-a008-61778a2c1854 | -3.2599 | -53.4164 | 2024-11-02 05:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| bf6ec4f0-5c2f-304e-88e3-e889712ee9d6 | -3.2599 | -53.3962 | 2024-11-02 05:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ce739f69-4a1c-3aef-bdf8-d530c2937c15 | -3.3878 | -45.3307 | 2024-11-02 05:45:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 02ac0ca9-07ef-3cf3-b61d-739906c0766d | -3.2231 | -53.3972 | 2024-11-02 05:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 37231ed7-dc3d-3d09-bb8f-cd7dcd252d6a | -3.7701 | -43.5554 | 2024-11-02 05:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| ee54829e-c51a-3f3a-8797-8ccb1bab15ea | -3.9473 | -48.3666 | 2024-11-02 05:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| fdbc47d7-afcb-39be-a4c4-666f1d0711ed | -3.9474 | -48.3451 | 2024-11-02 05:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 11208b85-5f6c-3612-8d68-80194c5c3c1c | -4.3537 | -48.6068 | 2024-11-02 05:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 83574a56-930c-3281-be55-63564407bcbb | -4.5577 | -43.0928 | 2024-11-02 05:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 4144326c-372a-3b8c-bc69-2318acc8e5bc | 0.08285 | -49.86111 | 2024-11-02 05:46:00 | AQUA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| de431294-592f-32fc-a961-c5a1b7e43686 | -1.21885 | -53.37411 | 2024-11-02 05:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0a69c0c3-17e6-3fdb-8cf1-401fb6785a10 | -1.20299 | -53.90826 | 2024-11-02 05:48:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a3e4acb9-084a-3182-a4d9-86fa9527c35e | -2.76716 | -51.66935 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bec8672e-0a41-3ced-8dd1-4d9bdf56a6bd | -4.55808 | -43.07867 | 2024-11-02 05:48:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 3aaa9966-4de5-3ca5-be59-b6d8d2972482 | -3.77647 | -43.54974 | 2024-11-02 05:48:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| c77405b0-925e-34f1-8952-74bffc5c934d | -3.76628 | -43.54378 | 2024-11-02 05:48:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| a2eec540-d9e4-3f29-ab67-096834eb6b90 | -5.72922 | -47.17733 | 2024-11-02 05:48:00 | AQUA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d104f38d-1c20-3687-8ace-15e6a3c3315e | -5.50947 | -47.17097 | 2024-11-02 05:48:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 52c51047-80ef-3b31-ba54-fae9c5fca3b4 | -5.50494 | -47.16513 | 2024-11-02 05:48:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6186cc05-3a58-3972-92b4-79d2e351e06e | -5.22068 | -47.44432 | 2024-11-02 05:48:00 | AQUA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 8ada304d-894e-3c54-8639-734db1ddf55a | -5.16724 | -48.24092 | 2024-11-02 05:48:00 | AQUA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6fd3f154-d46b-3559-891f-619d12b16b1e | -5.15175 | -47.70671 | 2024-11-02 05:48:00 | AQUA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0d3788fd-d2d2-31d7-9fe7-9f61db3b4e7c | -5.14764 | -47.71332 | 2024-11-02 05:48:00 | AQUA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1a420e3b-61aa-3bd2-9eb1-d8ac6b02cf87 | -4.99982 | -46.03093 | 2024-11-02 05:48:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| cf9e5916-314e-3ffb-9c1f-5ff695e0789d | -4.93788 | -49.14724 | 2024-11-02 05:48:00 | AQUA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e279fc30-6371-341c-9862-425cfeee72cd | -4.92996 | -49.15184 | 2024-11-02 05:48:00 | AQUA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 56aff11b-5961-3836-9567-1254d0ff83e2 | -4.91844 | -48.63087 | 2024-11-02 05:48:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0eb6c142-479a-324e-82cd-fd85920104d9 | -4.84484 | -48.57466 | 2024-11-02 05:48:00 | AQUA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 3f39ac74-9e03-3ab9-9cf5-ec5fb13b9aa1 | -4.84225 | -48.56728 | 2024-11-02 05:48:00 | AQUA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 74992670-bf4a-37e2-a721-b2ee73b3306b | -4.84025 | -48.58085 | 2024-11-02 05:48:00 | AQUA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5b5d81e1-fa58-35c1-b71c-e4cf5ad357bc | -4.79954 | -49.47996 | 2024-11-02 05:48:00 | AQUA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b659cc5b-eee9-3300-a614-5102967e6092 | -4.79896 | -49.4854 | 2024-11-02 05:48:00 | AQUA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6d157357-95e4-3e00-aa86-87061040ee28 | -4.71116 | -49.59616 | 2024-11-02 05:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 49d75e6a-d34e-3aad-9509-93e7105a7f2c | -4.70953 | -49.60754 | 2024-11-02 05:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| b0c43c19-b93f-3d10-88e1-e0804f6fae79 | -4.65657 | -46.59864 | 2024-11-02 05:48:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e3487f30-4a2a-395e-8928-db921f9eea79 | -4.42013 | -55.39291 | 2024-11-02 05:48:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4a4dd9ce-37ae-329a-afc8-9e1662457539 | -4.41048 | -55.39138 | 2024-11-02 05:48:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5d0fbf87-d92d-3867-97e1-9a2e97521e34 | -4.3545 | -48.60333 | 2024-11-02 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| cf983244-5bf1-39d9-98e5-cc8acc474870 | -4.35257 | -48.61651 | 2024-11-02 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d4e29511-91cc-33c8-b9e2-b2b65d717bf7 | -4.3509 | -48.15356 | 2024-11-02 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6cebc0ed-dd7e-39c3-811d-00fab8c6c6f6 | -4.34384 | -48.60192 | 2024-11-02 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README97.md)
