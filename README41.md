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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47da43e0-b4cd-32e5-b127-0813e7d453fb | -8.5822 | -63.130299 | 2024-09-27 02:15:26 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1953f711-fc4b-3ba5-ab35-a54faaf260ef | -8.5726 | -63.132801 | 2024-09-27 02:15:27 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 617e19d3-14a4-3a45-9996-92fd674ee43b | -7.8693 | -61.279499 | 2024-09-27 02:15:30 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49ad013b-3695-3c9f-be29-734cbc0496b5 | -7.8873 | -61.308998 | 2024-09-27 02:15:30 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff82722f-e8cf-3117-a927-008a639e0f1b | -7.8789 | -61.277 | 2024-09-27 02:15:30 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c03e652-fe07-31e8-8980-6d7ec4d09b16 | -7.7295 | -61.212898 | 2024-09-27 02:15:32 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9736f36c-4129-300a-ab31-17efdde6f15e | -7.721 | -61.180199 | 2024-09-27 02:15:32 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d277fba-c7db-3648-aa46-5d1ed6984483 | -7.739 | -61.2104 | 2024-09-27 02:15:32 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 295ed433-342f-313d-96b3-8069606e70f3 | -7.7305 | -61.1777 | 2024-09-27 02:15:32 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23650014-3bd9-3ab3-abe8-e5096fed091f | -7.74 | -61.175098 | 2024-09-27 02:15:32 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41a22941-e1bb-321c-aa2d-2112a6c16ccb | -5.397 | -43.4332 | 2024-09-27 02:15:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 311419c8-5f88-3676-8ccd-e0a1c0d05fac | -9.0809 | -67.886299 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a13cf366-b398-34ce-8458-267b8ee52043 | -8.9598 | -67.383499 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28afa2e6-aae5-3b93-b008-c69d43e85083 | -8.9569 | -67.371597 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 477cba16-a1da-35c4-a890-335b3acd70b8 | -8.954 | -67.359703 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3a0a12e-ffa2-34f8-bd4b-f3d4c1823635 | -8.9695 | -67.381104 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7901fa54-d85f-3bd9-8382-e25a9d835b0c | -8.9666 | -67.369202 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 699cd036-ad07-38ac-ac8c-453c8860eb12 | -8.9638 | -67.3573 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 115e3af5-aa2d-39bf-98f3-36b02857e0cc | -8.9609 | -67.345299 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1aef12c-11e7-370a-8112-2a9ff4b9e5a1 | -8.9793 | -67.3787 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4464252f-eeae-368b-8bf5-434d6fd8b027 | -8.9764 | -67.366898 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17376cbc-8a37-34ea-b9a6-825573887b7b | -8.9735 | -67.354897 | 2024-09-27 02:15:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cddcc0d-badf-3b9d-927e-4a6985322be9 | -8.7851 | -67.685303 | 2024-09-27 02:15:41 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4580b1-2cf5-3ea5-88dd-c135ffda155f | -8.7824 | -67.673897 | 2024-09-27 02:15:41 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 750ffb5f-7525-3467-821a-d3b417ff0375 | -8.7781 | -67.699097 | 2024-09-27 02:15:42 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d115e9f0-2047-379a-bc87-bec09d55d1cc | -8.7753 | -67.687698 | 2024-09-27 02:15:42 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 272c2794-d8b0-3c37-bb1e-d1e19589205d | -8.7726 | -67.6763 | 2024-09-27 02:15:42 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69d071a1-baf5-3295-8e5b-9ecaf12a6ec7 | -6.8927 | -59.6475 | 2024-09-27 02:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 28232ca4-b98f-37ad-a140-520f3184ed04 | -7.309 | -61.0862 | 2024-09-27 02:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 7fcdd5a6-5653-322f-8787-43980351e0de | -7.5289 | -61.3825 | 2024-09-27 02:15:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 4bafad26-2966-36d0-b611-8cebfea37cf6 | -7.5888 | -60.5785 | 2024-09-27 02:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 4d211335-aded-3b96-ac85-da6dc7bc681e | -7.5887 | -60.5976 | 2024-09-27 02:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 7d649b50-1160-3a1c-9117-0bfea992ade5 | -7.5703 | -60.5984 | 2024-09-27 02:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1bf680e7-0b2b-34da-8472-a82e9f167d24 | -7.7886 | -61.1817 | 2024-09-27 02:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.1 |
| fe9d9247-acbe-3429-bd27-ab9d7b93438d | -7.7885 | -61.2008 | 2024-09-27 02:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| eb364c16-99c0-3e49-9bd0-ba1fc374031d | -7.8156 | -54.7252 | 2024-09-27 02:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 4a08977f-88d1-3aea-a121-5399b0245ece | -7.7701 | -61.1825 | 2024-09-27 02:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 188.5 |
| 4ef7bba1-cfc7-3468-80ff-0ff89d52abac | -7.77 | -61.2015 | 2024-09-27 02:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 50b207c3-b1b9-33d2-afca-c6a40d7a509b | -7.936 | -61.271 | 2024-09-27 02:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 03ed1b1b-1833-35cf-afeb-5e7ed5156cf9 | -7.9175 | -61.2718 | 2024-09-27 02:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| bc6b9154-2c4f-36d1-9310-bbeb82715052 | -7.9174 | -61.2909 | 2024-09-27 02:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7d08bfb3-594f-33e9-8394-a16139b7d99a | -8.1579 | -61.2809 | 2024-09-27 02:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b46317b8-ac9a-3c4b-aa21-805e3d44d411 | -8.1395 | -61.2626 | 2024-09-27 02:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 817c0d2c-a9f8-3d79-872c-b1903694e512 | -8.1394 | -61.2817 | 2024-09-27 02:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 63f9509c-c40f-30db-9efc-4182d51361b9 | -8.1393 | -61.3007 | 2024-09-27 02:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 957b00fa-8a01-3915-b3e9-48a5ea825bdf | -8.1209 | -61.2824 | 2024-09-27 02:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9d6f2c74-4a5a-3ec5-8ddb-d55f038370be | -8.556 | -49.6112 | 2024-09-27 02:15:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a32f6904-8eed-3dbd-a91a-b996d0fbf911 | -8.8117 | -67.6732 | 2024-09-27 02:15:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| c93eb480-ddaf-31f9-85e2-2354f90805b1 | -8.8116 | -67.6917 | 2024-09-27 02:15:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| c373c8b4-ff33-3aff-a00f-cef6ac6c5dbf | -9.107 | -67.8881 | 2024-09-27 02:15:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 366dcdaf-3e4c-38fa-b4df-159c5a342daf | -9.417 | -51.4426 | 2024-09-27 02:16:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9d55239b-69be-30d2-a65b-a5aa8b8a2fe7 | -9.6206 | -50.1334 | 2024-09-27 02:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 812dd656-9fcd-3820-a446-4c30193411e4 | -9.602 | -50.1139 | 2024-09-27 02:16:01 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 09738038-dd29-3c88-b117-12643057b5d2 | -9.6018 | -50.1352 | 2024-09-27 02:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 236.0 |
| 395af5c9-8402-3012-a4b4-c4b997a6532f | -9.6015 | -50.1566 | 2024-09-27 02:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| be0b6266-3619-3663-8a45-1cd5d9f2f5db | -9.5829 | -50.137 | 2024-09-27 02:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 47491524-7067-3d16-b93f-34b430c93268 | -10.3672 | -53.7858 | 2024-09-27 02:16:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 606e63c7-7f99-3d1d-bcdd-f433dd610007 | -10.6643 | -45.861 | 2024-09-27 02:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d2e7f2e6-7b03-3517-8381-bdd0eca0a8b8 | -10.6639 | -45.8838 | 2024-09-27 02:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| dc2ed5a1-e3a0-3315-81ee-ffcb3d8f8da4 | -10.74 | -51.0849 | 2024-09-27 02:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| f43f273e-3668-3f84-8479-7bb33e28bc1a | -10.7214 | -51.0657 | 2024-09-27 02:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 7d3edab1-c254-3feb-891a-5bb52aa2a1db | -10.7211 | -51.0869 | 2024-09-27 02:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 010faf63-813d-3851-81d3-fee93d5d664b | -10.9456 | -54.2471 | 2024-09-27 02:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 2ebd8264-74e4-3513-a656-87952dedfb6c | -10.9453 | -54.2676 | 2024-09-27 02:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 4e74f4c9-890d-3739-b1c1-daefc2fa8895 | -10.9267 | -54.2488 | 2024-09-27 02:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 242.8 |
| 40c46eac-16bb-3298-94d1-34891daff3dd | -10.9264 | -54.2692 | 2024-09-27 02:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 196.8 |
| ff7669f4-14d7-3554-89d0-3e618e2e8563 | -11.2223 | -54.7735 | 2024-09-27 02:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| a0bcbe0b-07fb-3898-b681-43ab42fb91ed | -11.2036 | -54.7548 | 2024-09-27 02:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 2b03b980-354a-3dc9-b554-7a4c21aa8a3d | -11.2034 | -54.7752 | 2024-09-27 02:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 070544bd-9f2c-3c20-af21-12561a6105b7 | -11.6061 | -63.9397 | 2024-09-27 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 4db7b88e-ac7c-355e-84cd-599c73a7074d | -11.606 | -63.9587 | 2024-09-27 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 155.2 |
| c65fda77-086a-3348-8556-1126b7c8139e | -11.6059 | -63.9777 | 2024-09-27 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 27bf5b82-6575-3540-9020-94528467f0f0 | -11.5874 | -63.9406 | 2024-09-27 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| ece2dc45-002c-31a9-88c6-8a79d0c88bd1 | -11.5872 | -63.9596 | 2024-09-27 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 133.2 |
| fed2ef4c-1db1-37d2-a565-f48ca7998f16 | -11.5871 | -63.9786 | 2024-09-27 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e0367387-a906-3828-b04a-ea5c014630f5 | -12.6826 | -54.6763 | 2024-09-27 02:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 540a0255-fcf9-3407-bf2b-063009202953 | -12.6824 | -54.6968 | 2024-09-27 02:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 42a5d5e3-9965-3e39-ad0e-726b6c5fcef2 | -12.6639 | -54.6577 | 2024-09-27 02:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 81e9b77f-9231-3e22-8e74-9fc260b46ff4 | -12.6636 | -54.6782 | 2024-09-27 02:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e5dc3b90-db7c-3525-afeb-2f151615033c | -12.6633 | -54.6988 | 2024-09-27 02:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d930cd20-81e4-3e72-8303-8961352659cd | -12.8628 | -54.0402 | 2024-09-27 02:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 14e2ba53-9537-385f-a1d6-b5777f4acd28 | -12.8631 | -54.0195 | 2024-09-27 02:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 3d042c1f-400e-331e-be14-a32f1304f1ce | -16.8933 | -58.0213 | 2024-09-27 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 3d5277af-053b-369d-93be-5f5f09eeec29 | -16.8737 | -58.0235 | 2024-09-27 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 3c1701ea-ebbf-380f-b99f-683ec603f130 | -19.6342 | -42.8103 | 2024-09-27 02:16:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.2 |
| 5321f9c3-989e-3481-bcf8-c5f8cb6ff23d | -19.6136 | -42.8159 | 2024-09-27 02:16:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.9 |
| 65237648-4e0e-3c63-9819-00ee1e404057 | -21.0665 | -48.8196 | 2024-09-27 02:17:02 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 4dd7b621-bb48-3ff6-b97e-a5fa8cc12483 | -21.0658 | -48.8428 | 2024-09-27 02:17:02 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.6 |
| c6f23e13-70d9-30b5-a89e-07bd748364c6 | -21.0865 | -48.8381 | 2024-09-27 02:17:03 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.4 |
| 73febadb-0264-3854-aff6-72c4f874cf8b | -22.7442 | -44.7785 | 2024-09-27 02:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.7 |
| ceb9762a-a644-389c-a764-f1b8043e81d2 | -22.7433 | -44.8035 | 2024-09-27 02:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.9 |
| 78efca72-5b23-3112-abaa-bf602ce2ce9a | -23.5816 | -47.3408 | 2024-09-27 02:17:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.9 |
| e57d1bed-55e4-32e5-93b1-1d2131b538b1 | -2.358 | -47.5989 | 2024-09-27 02:25:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| d40a6984-fb03-33d6-98f0-43b5fb04f2f3 | -2.3579 | -47.6206 | 2024-09-27 02:25:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ccd7cdf8-0349-3f98-95d2-8a298e74ffac | -2.9339 | -57.8562 | 2024-09-27 02:25:23 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| ecf2a627-8f91-3a99-83fa-026c92ab2789 | -2.8795 | -51.6695 | 2024-09-27 02:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b94e3ff4-60fa-39f5-ba07-789ec475bee1 | -3.2136 | -46.7843 | 2024-09-27 02:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| eea58f2a-d64a-348f-b83a-0794a8fa5cb2 | -5.397 | -43.4332 | 2024-09-27 02:25:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 281a535c-6bfd-37a1-b39e-93305cf3febf | -6.8927 | -59.6475 | 2024-09-27 02:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e78ba0ba-1a64-3c45-acb0-bb1a72d30f52 | -7.309 | -61.0862 | 2024-09-27 02:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |


[Clique aqui para ver as próximas entradas](README42.md)
