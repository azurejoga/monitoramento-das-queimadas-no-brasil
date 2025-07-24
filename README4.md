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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1558ed44-99da-301e-806b-22999376f15d | -4.0569 | -42.5118 | 2025-07-24 01:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 81fe12d1-decb-39ce-a4fd-8e78e75325b4 | -7.2405 | -43.0899 | 2025-07-24 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 65a87eab-d0b1-3983-b121-034325427909 | -7.2597 | -43.0645 | 2025-07-24 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 354.6 |
| 0442ccdd-5d4b-315d-b27c-8c48d12d830a | -7.2408 | -43.0664 | 2025-07-24 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| d6462e5d-31e3-3c1f-b5a3-57b7f86979b6 | -7.4541 | -49.4018 | 2025-07-24 01:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f4b42339-a604-3a19-b1d1-77a858c89692 | -13.6975 | -45.6865 | 2025-07-24 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 420cb9b6-58a0-35f7-a8b5-bcf810b2f48a | -3.1832 | -49.4642 | 2025-07-24 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 410ce3ef-47f9-380e-bbaa-6971c6153cc2 | -3.1649 | -49.4435 | 2025-07-24 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 0bea7dcb-c61d-352a-932d-5371a4293439 | -13.698 | -45.6634 | 2025-07-24 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| d69e64bf-f765-3b67-8d45-9155b0347e4b | -7.2594 | -43.0881 | 2025-07-24 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 234.0 |
| 47878bb1-17e3-3394-adea-0494c8a7926a | -3.1833 | -49.4429 | 2025-07-24 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 204.2 |
| fb30041f-8dd0-319b-b3e3-21956607c36f | -3.1648 | -49.4648 | 2025-07-24 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 63d47dfb-a967-3c73-92b4-a088974c5d7c | -3.1648 | -49.4648 | 2025-07-24 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 15c00c6e-0458-366f-b0e2-bd8024ea275a | -4.0569 | -42.5118 | 2025-07-24 01:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| a64a1e9f-42e2-3abb-959b-a271cbe36966 | -7.2408 | -43.0664 | 2025-07-24 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| 4e89e9ea-887d-312c-a205-b1296813f89e | -3.1649 | -49.4435 | 2025-07-24 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| dc3ac108-5fee-33ff-b048-e4bb510a581d | -7.2785 | -43.0627 | 2025-07-24 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| b5e31676-c509-38c2-9c2e-1adbd107b486 | -7.2594 | -43.0881 | 2025-07-24 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 182.7 |
| 0f1a71f7-84a8-3cc2-a0dc-b8ff9ad71684 | -7.2405 | -43.0899 | 2025-07-24 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 848fdcda-fca2-336d-bfac-acaad3eae2a5 | -3.1833 | -49.4429 | 2025-07-24 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 200.6 |
| cf3ab98e-42e3-3b5a-adaf-d00d74ce5e28 | -3.1832 | -49.4642 | 2025-07-24 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 4320bde1-5114-3235-9c43-839c3e9b5d7b | -7.2597 | -43.0645 | 2025-07-24 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 304.0 |
| 673c7742-2cb6-36de-8b84-40e74cc2df80 | -21.47966 | -57.11294 | 2025-07-24 01:41:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a3c06929-8861-3273-bbf9-89ec16d98ff5 | -21.48039 | -57.10221 | 2025-07-24 01:41:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1b070baf-1764-3539-a365-9560cdb2c7a4 | -10.04018 | -59.09897 | 2025-07-24 01:43:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| f9f21852-4b90-3288-92c4-753e20368fd6 | -11.94451 | -58.76394 | 2025-07-24 01:43:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 6922d004-5d88-3537-a845-7482d31f6bf5 | -12.43477 | -63.69925 | 2025-07-24 01:43:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5e988a25-7862-3f7c-a22a-3dada6506fa3 | -11.94736 | -58.7816 | 2025-07-24 01:43:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 30c9bd59-ebec-345a-9f2a-a5b6ae1d5ff8 | -8.49215 | -64.0284 | 2025-07-24 01:45:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18dbb501-d5b3-3cdd-a78a-91e6868c72c8 | -9.62883 | -67.25496 | 2025-07-24 01:45:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d0d65674-fab1-3464-bca2-db4a4017e5ef | -9.75715 | -65.09641 | 2025-07-24 01:45:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b0044428-4abc-3704-b56f-4f1e87e14015 | -9.33154 | -63.52107 | 2025-07-24 01:45:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ef1a93f6-7bfe-3d59-be5b-291c004fd064 | -9.38048 | -66.58009 | 2025-07-24 01:45:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 73024224-d0f8-3bf8-aa9e-bce818bf5441 | -7.2408 | -43.0664 | 2025-07-24 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 936978ac-868c-3716-9298-33f52231845c | -7.2597 | -43.0645 | 2025-07-24 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 274.1 |
| aa30227d-5a19-3f8b-bbe3-47f8ec0f867d | -3.1649 | -49.4435 | 2025-07-24 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 8c1f08ae-da14-36f4-9329-94a955c30d5c | -7.2785 | -43.0627 | 2025-07-24 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 801b18db-1f8e-3f0a-bd78-abe151cf0452 | -7.2405 | -43.0899 | 2025-07-24 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| dd958a65-b48c-37ca-b02d-3ab2e07b0c85 | -4.0569 | -42.5118 | 2025-07-24 01:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| fc3ea255-d216-3353-9650-70ebc068977c | -3.1648 | -49.4648 | 2025-07-24 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 9675d09a-c9e4-30f7-908b-7f968a3df3f6 | -3.1832 | -49.4642 | 2025-07-24 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 484cff66-e571-39a0-8fe4-90a3a3af824f | -3.1833 | -49.4429 | 2025-07-24 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 182.7 |
| 1c1dfbb3-0b32-30ea-93af-257dba79ae40 | -7.2594 | -43.0881 | 2025-07-24 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.2 |
| 10435e8e-4f49-3320-8a98-503e66da1d3b | -3.1649 | -49.4435 | 2025-07-24 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 69756794-963b-3afc-822c-5fd0f08e0cff | -3.1832 | -49.4642 | 2025-07-24 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 199.6 |
| e7232371-d152-3611-a1ab-184362d2b8bc | -3.1833 | -49.4429 | 2025-07-24 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 45b6097e-fbdb-3593-a2b7-b9808828d101 | -4.0569 | -42.5118 | 2025-07-24 02:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| c3763603-bda1-3a5b-8b8b-a518136e964a | -7.2597 | -43.0645 | 2025-07-24 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 235.8 |
| d7e73339-10e4-33e5-a5fe-99401af6ea39 | -7.2405 | -43.0899 | 2025-07-24 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| ab227857-ea67-3d58-9af1-452408ad06a9 | -7.2785 | -43.0627 | 2025-07-24 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 5e52d4b5-c9d6-3988-9e54-20fcda1e4a97 | -3.1648 | -49.4648 | 2025-07-24 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| f0c02067-abfe-3997-b6db-ec480f4d568f | -7.2408 | -43.0664 | 2025-07-24 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 40dd4f93-96dc-3a8e-9fce-6337cd179b60 | -7.2594 | -43.0881 | 2025-07-24 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 188.2 |
| 0fc835b7-f843-3d4e-9fe8-d3357d84c5d0 | -3.1649 | -49.4435 | 2025-07-24 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 61a13665-06e3-36df-ad54-48be182b8fd8 | -3.1833 | -49.4429 | 2025-07-24 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 3b479381-ab45-35cd-bd5e-a827f452b3e9 | -7.2408 | -43.0664 | 2025-07-24 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 694abcde-d55a-35a0-8de5-36e064b09e83 | -7.2594 | -43.0881 | 2025-07-24 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 175.9 |
| 49b281cf-f447-3a53-b44f-a3de6a3f5e15 | -3.1832 | -49.4642 | 2025-07-24 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 26cd5454-d0e5-3220-8c4a-d0f2c2669fa2 | -3.1648 | -49.4648 | 2025-07-24 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| ac8350d9-ed3f-37a0-b6f4-0a63cd2139b6 | -4.0569 | -42.5118 | 2025-07-24 02:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 4239315c-a4de-3b35-b0b9-053444f57ba3 | -7.2597 | -43.0645 | 2025-07-24 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 290.5 |
| 067cb6a7-1e94-3c11-90a7-ccfc2ce9fce4 | -7.2405 | -43.0899 | 2025-07-24 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 56168683-3de1-3bcc-8b2d-db4330974b03 | -7.2405 | -43.0899 | 2025-07-24 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| e9f7dccd-e348-393f-bd27-6b5d8a36025b | -3.1649 | -49.4435 | 2025-07-24 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| f11068d9-8d36-3d37-a141-fa9848cc2748 | -3.1833 | -49.4429 | 2025-07-24 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| c57fb2f8-68d6-3463-92ed-a2ffb134f61c | -7.2594 | -43.0881 | 2025-07-24 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 174.6 |
| 3e0b73fa-d05b-37ad-96a2-f9e6c80b311a | -4.0569 | -42.5118 | 2025-07-24 02:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| f461fe5a-cea2-3fa0-add0-f814bba84e9b | -3.1832 | -49.4642 | 2025-07-24 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| bb2dfb7c-23a7-356e-93f8-559d295368b9 | -7.2597 | -43.0645 | 2025-07-24 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 238.9 |
| 79eefe17-e1d3-30ab-af00-4b27e5bbea36 | -7.2408 | -43.0664 | 2025-07-24 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 9ab62334-983b-3028-a914-58d6d71b0235 | -3.1648 | -49.4648 | 2025-07-24 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 279795ff-8784-3af0-9a7c-c3d0c9747069 | -8.5876 | -63.8772 | 2025-07-24 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| d8f146a1-84fa-3e76-814b-78b076666828 | -7.2405 | -43.0899 | 2025-07-24 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| f8c802d9-c3f9-3206-879a-310f401915c9 | -4.0569 | -42.5118 | 2025-07-24 02:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 65179cf8-4e02-3eec-887f-553235105f7c | -7.2408 | -43.0664 | 2025-07-24 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 138cd8ac-dc29-3640-841b-69329d4dd1cd | -3.1833 | -49.4429 | 2025-07-24 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 90426548-7718-3d75-b8b2-a2db24b3ee78 | -7.2597 | -43.0645 | 2025-07-24 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 211.8 |
| 067cc83d-cf1c-310d-9b1c-7803daba74e8 | -3.1832 | -49.4642 | 2025-07-24 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 145.7 |
| d928c8a9-07be-399a-a19d-42ab39e7b578 | -7.2594 | -43.0881 | 2025-07-24 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| bdf035aa-1d57-33ce-ab18-4ba4d782ff7f | -3.1649 | -49.4435 | 2025-07-24 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 3f5171a2-44a9-364e-ae81-1e0e8c07a599 | -3.1648 | -49.4648 | 2025-07-24 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 0da53879-33d0-335b-ac73-303002b534d0 | -7.2594 | -43.0881 | 2025-07-24 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 852dc3b3-fe52-3ef6-a383-8ea35b309c9f | -3.1648 | -49.4648 | 2025-07-24 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 0591d3dd-cbdc-3087-8a8a-035cdfc9aa92 | -3.1833 | -49.4429 | 2025-07-24 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 97f77c88-9034-3c9b-8eb7-2479368f0839 | -4.0569 | -42.5118 | 2025-07-24 02:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 2eb6c3e5-04ef-30ec-aad7-5d995f3de7f8 | -3.1649 | -49.4435 | 2025-07-24 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 29c290e9-c571-3bbc-899f-cb0fb0cae19d | -7.2405 | -43.0899 | 2025-07-24 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 81edc3cb-7d5b-33fe-b52a-1f392fd3a5bd | -3.1832 | -49.4642 | 2025-07-24 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 2ff0ca39-15fe-3be9-876f-ee6f13cf2d5b | -7.2597 | -43.0645 | 2025-07-24 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 201.4 |
| 38c86c95-3be8-3be6-9cd0-97d7bdfddafc | -7.2408 | -43.0664 | 2025-07-24 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| ca8d1358-5ff2-3337-b0af-e0706049bf74 | -7.2408 | -43.0664 | 2025-07-24 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 3ccc0e89-3a29-3411-9e2e-08e7d47afec1 | -3.1832 | -49.4642 | 2025-07-24 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 4b21678f-1133-302f-b540-aef826f645f2 | -7.2405 | -43.0899 | 2025-07-24 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| d233bb08-8e2c-3a39-9cde-5d76f48bd30c | -7.2597 | -43.0645 | 2025-07-24 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 218.7 |
| 79d3596f-013f-35ba-96a2-7d42ba020768 | -7.2594 | -43.0881 | 2025-07-24 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.0 |
| 6ca4e7b7-bd45-37de-b2b2-759372d78605 | -4.0569 | -42.5118 | 2025-07-24 02:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 8137ec54-b4f4-3216-83e2-dddab4b5cfd6 | -3.1649 | -49.4435 | 2025-07-24 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 75863895-cbd6-3ec6-923d-66b16e6f2672 | -3.1648 | -49.4648 | 2025-07-24 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| f31e36cc-58d7-38d7-96b6-d51601e6088c | -3.1833 | -49.4429 | 2025-07-24 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 4289bce9-f9e8-3928-b2b5-f207dbda9ed4 | -3.1649 | -49.4435 | 2025-07-24 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |


[Clique aqui para ver as próximas entradas](README5.md)
