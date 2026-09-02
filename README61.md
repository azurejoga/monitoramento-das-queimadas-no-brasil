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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a01d49c5-746e-39ee-acdf-e125706aef6d | -3.09397 | -61.21547 | 2026-09-02 05:59:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 233bdc3e-e62a-3e43-9997-34b9e09caf36 | -8.4856 | -54.7225 | 2026-09-02 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| cc359a57-8354-3ad5-8f57-621ee2280f8a | -10.92 | -45.3483 | 2026-09-02 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| e7bf71b6-74bd-3121-8c2a-49617b7238fc | -10.4804 | -64.3313 | 2026-09-02 06:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0e14fa93-9bc4-3c94-b120-a8bf7ef3c6f4 | -10.9013 | -45.3279 | 2026-09-02 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 8b37596e-4547-35eb-b2a1-84a813015ddd | -10.9009 | -45.3509 | 2026-09-02 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e4cd957f-4395-3013-9a8d-eae7acc678e2 | -10.9204 | -45.3253 | 2026-09-02 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.0 |
| d47a29f7-a90a-305b-91b2-7e79d8d0a9a4 | -8.4669 | -54.7237 | 2026-09-02 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 8b1fe6b6-5bb9-31f0-8568-f6e7bb5538dd | -6.6948 | -58.7678 | 2026-09-02 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f96dc73c-4256-3d7c-a8d8-1e228527fcfb | -9.52154 | -67.16791 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5713a4b6-d4b8-33f2-9f15-1f8a132e4946 | -5.58591 | -60.20211 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4e2fd8a-871e-3bd1-9aa3-11b56964d018 | -9.93079 | -67.84409 | 2026-09-02 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e4f3db9-b1e3-35cf-bd11-05f440e2dbd5 | -6.15708 | -57.77552 | 2026-09-02 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a902ada5-50c4-3b96-a0af-50675b4e427a | -6.6884 | -59.94345 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0d1c0726-4147-3090-b21c-601abbbfb9f6 | -7.3455 | -60.58194 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9382c5a-c3ca-35db-a1e2-28f67244a459 | -6.87819 | -59.4046 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b9ed8d32-cf29-348f-b8eb-60f6fc9dcac8 | -7.1993 | -60.66621 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd555232-e960-3ab7-8689-958e72f362f2 | -10.12792 | -68.52174 | 2026-09-02 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 527cbaa5-8aa0-350f-917f-f0e9de9eb3dd | -7.6994 | -67.12645 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9973d7f6-dd98-34c4-9b8b-a4212e7182bd | -9.44286 | -67.44814 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fc44aea0-f705-39fa-8d93-aa455cc2fe2f | -7.19859 | -60.67534 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c4077aa-c8b0-3549-b8d3-1c16f5f3a67f | -9.8696 | -64.97816 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78e33221-854d-36b1-aed3-8aaa9167fd71 | -6.68182 | -58.76084 | 2026-09-02 06:01:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 057c5a6b-d7b9-30c9-a262-2cb54acd6e21 | -9.00438 | -65.4525 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bba96ce0-e5e6-341e-b789-e724955a6ce9 | -8.5683 | -63.18832 | 2026-09-02 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a47b08b-0ddf-3e4a-bfc0-1348d428184c | -9.87444 | -64.97469 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd664b33-a606-3a94-a592-dc5716f5372f | -9.19721 | -65.91562 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4b2ed2-f4da-3d2b-8c7e-1d9a6e822b60 | -5.57697 | -60.19476 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 650b79e4-67d3-3282-99f5-0c86696d2733 | -9.12573 | -68.90375 | 2026-09-02 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bc54f3c-c567-3de0-82e6-84ebd6f50585 | -8.87232 | -66.82073 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61c24cac-fa2a-3a6e-a1d4-ab29a1fb7ae7 | -7.20244 | -60.68543 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7065265-a52a-395f-9531-b443b6801c7a | -6.15633 | -57.78113 | 2026-09-02 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73b7b731-34e7-334b-b5a7-0dd787c62d68 | -7.21489 | -60.67646 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec7fc3c1-51eb-3390-ae92-80f54296dea4 | -9.87015 | -64.97404 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4780669d-daaa-3cf4-b522-1ed38da3fa53 | -5.33517 | -60.14962 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4512610-b84c-3896-99c0-6314558b6bcb | -8.90632 | -62.36498 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c1555261-e46c-3c54-9599-fb3f475d2a9d | -9.88247 | -64.98003 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23324b18-0954-3ea1-9774-20108bed4bf8 | -9.204 | -67.77399 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fea4df3-f0b8-3cbb-a5e4-e19828b77b56 | -7.35328 | -60.60915 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 803d1fbd-4d2f-32e4-bfe6-f3fd4ed45764 | -8.92068 | -62.36405 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85749b6e-3ba9-36ab-a4b5-146736d49688 | -7.20387 | -60.67439 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 244a3cbb-e5df-3a7b-8654-82d801b33880 | -7.72659 | -60.97684 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9377e0d-bc2f-3a88-86e6-3ec430f9f0be | -8.65913 | -70.68269 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3b169ba-07af-390b-8807-c006e08b11b5 | -9.02427 | -65.4543 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50c0a0dc-e899-3305-8296-deb076efef3d | -6.94047 | -56.4564 | 2026-09-02 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1ddb533-f9e5-32f8-83a9-586f63a9982d | -7.69881 | -67.12766 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b0c7d4b-8dcf-3c9c-b6d3-4e5443e9442c | -7.20984 | -60.67191 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 693dfb4c-bf42-3458-a177-4b9cbe1ec2ed | -9.87707 | -64.98759 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b063eccc-325e-3f5f-ac86-33a16fd1c507 | -8.55807 | -63.1921 | 2026-09-02 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 525d6858-1c40-3e1e-8365-c76467d229b4 | -6.68806 | -58.76152 | 2026-09-02 06:01:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8b99348a-8167-36bb-bda3-d204faa22343 | -8.65528 | -70.68564 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 183dc07c-69e4-3910-b4a1-08030d2986a5 | -8.91547 | -72.81236 | 2026-09-02 06:01:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d1e370f-10f5-35f0-8a64-bdbe1760debb | -7.20962 | -60.67723 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3266459-9f9e-352d-8ad6-5579a65445d8 | -6.69432 | -58.76213 | 2026-09-02 06:01:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4aa85053-be7e-3c3d-bd57-698c412e3ec5 | -7.21012 | -60.67357 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f418e0f-e725-3b1b-875e-01295d04b059 | -8.75886 | -62.58331 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f01c5e3-8231-346f-8df6-ce8e2856bb15 | -8.98532 | -70.68471 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e476dc46-c83d-3d46-ae1b-208f414f6382 | -8.93586 | -62.36629 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55bfa60f-c67e-311f-bdb6-d27243d74231 | -7.54062 | -60.72272 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db369d74-0eaa-3a31-aa03-64b9186d1f8e | -7.84668 | -71.74083 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55303f90-4e19-393a-bde6-19b46d20a4d9 | -7.45479 | -61.37484 | 2026-09-02 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 621d8dbd-aa98-3384-8097-188ccee6ace9 | -4.23674 | -62.23828 | 2026-09-02 06:01:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14039975-923c-3aaa-ad70-52ae45d48342 | -6.94135 | -59.64117 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| feba71da-8f71-31ea-87b2-f009fed751c8 | -9.03194 | -65.42894 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 205dceee-c225-3044-8b21-ec492b1c03b0 | -9.92671 | -60.48817 | 2026-09-02 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2e66473-3aa9-365a-906e-206c8b649f0b | -8.91638 | -63.29145 | 2026-09-02 06:01:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 67193b9b-0193-3aac-b60b-47429a47bfce | -9.88303 | -64.97594 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61bb24e3-bb73-30b0-8613-ccd5f01d4192 | -9.01616 | -65.45799 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 287e1c75-d74f-3941-8023-3abfc18ffb7e | -7.20889 | -60.67921 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d246ef5-f08c-387e-a98d-0bd9fb106b12 | -6.93098 | -59.6422 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca5099ba-3ee1-302e-acda-23a06379d8ed | -10.4842 | -64.32504 | 2026-09-02 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 8ae09765-0477-327b-9b85-4b181824cb09 | -9.08864 | -65.38391 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2f0e7468-906a-3c55-afd0-608728eb8005 | -8.36869 | -70.60439 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d1c4c60-f7b8-394a-ac3d-c994816412b0 | -6.68787 | -59.94742 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b57970b0-b330-3bc5-86b1-a89ea5472f6f | -7.76373 | -61.19563 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b5a9e3b-fecb-3658-a080-14afce221052 | -8.93547 | -62.36929 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4c4d9dc-82a4-394f-8316-590e3c243fb1 | -8.33266 | -70.72669 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7c9e16f-c3bd-34c4-b053-68774d060eff | -10.09692 | -68.73235 | 2026-09-02 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afb6495a-b772-32ca-8ad1-9c07430b3105 | -6.81182 | -59.09953 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35394ab6-63c0-3277-b97d-2e9bbc0ce60d | -8.90511 | -62.36482 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 72b87873-8e17-35fa-a923-8565c42acf8a | -7.76327 | -61.19906 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4ba58ca-107d-3f26-a12f-c22ecd485176 | -8.21694 | -61.47945 | 2026-09-02 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ced97c2-8abe-3da7-8d1c-c2fc5568c273 | -6.81119 | -59.10435 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa903826-2e32-30f1-83c4-2c3ab4864199 | -8.90287 | -62.35246 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bdbf3f6-2bb8-382b-9950-3136788ddb09 | -6.9167 | -59.64581 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 098178f6-4383-3c6d-b774-5c8ee0765f4b | -8.76398 | -62.59 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 65479009-be47-3f72-bc60-510a230bb903 | -9.86586 | -64.97341 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb919659-ebc3-3b27-8188-114ddd26bed1 | -9.02377 | -65.45801 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f6ef15c-28e4-3ccd-b7da-3070d4faa578 | -6.76105 | -59.43882 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2eb45212-8d1c-3b60-b9de-d2d034c52e49 | -9.44297 | -67.42169 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cea475ee-0602-33e8-b412-93a5bfd985b8 | -8.76474 | -62.5841 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eda7576a-fc2e-3b20-be92-2f962fa3d37d | -9.8302 | -59.48016 | 2026-09-02 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32e8858f-57f0-3dd9-a664-1deff514baff | -8.75977 | -62.58338 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ce7d4d70-0a7e-3ef5-8ccc-109fd09a0107 | -9.0299 | -65.44381 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d42fb955-f679-3c64-90d9-76c9eb35a6ca | -7.20843 | -60.68276 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c48368e6-f21f-3da9-9e2e-ec911704cf91 | -9.44664 | -67.42225 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 485a58f1-a119-3b33-929d-f44d5b28d5ed | -5.34075 | -60.15044 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd416b73-69c3-3010-8c44-13c73e756fde | -7.25917 | -61.11209 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e946134-b966-3fae-9e96-1bf89b2da4ac | -8.04681 | -70.57465 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96db6e43-7785-332d-a3b3-d1fc559c1553 | -9.84295 | -64.9926 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README62.md)
