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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa5c1704-5a04-3e1c-bb4c-9d0d0a23d0a9 | -6.74786 | -59.17493 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5f4e4e2f-b036-3a63-b9d6-50391c93a991 | -6.75019 | -59.1571 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f73fd9fb-5bbb-33d8-bebb-6a23a274918d | -6.7763 | -59.76136 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba8639a8-1efe-3cff-99a2-ae521e6ab2eb | -6.7494 | -59.16316 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 919b3a3f-a584-3099-8454-a75b972565fa | -6.74486 | -59.17421 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3b6a7bc8-4269-3767-a121-e21810dc243a | -6.70819 | -58.93604 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 876a18eb-fd81-3331-887c-c5f9522f0acc | -6.84792 | -58.99226 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 072e5f74-1027-374c-abe5-e525aae46cfe | -6.11226 | -57.73354 | 2026-08-18 06:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b191bd66-8062-3423-988f-48f9e32abd72 | -6.7473 | -59.15649 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e80f75c1-9ad2-38bf-9b4f-2624455fa61d | -6.71503 | -58.93673 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dc18bca-0725-3d77-adb6-a9ce8b446c32 | -6.70047 | -58.9419 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e8e546a-5f49-352b-b234-6ad885ceba09 | -6.75147 | -59.1759 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 13154ec8-d033-35ad-9bd2-02bdde6784b0 | -6.7569 | -59.15821 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 54f18f62-a92c-32f8-9c8b-4865c300d422 | -6.79204 | -59.45346 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5d1319f-8ee4-3223-a55d-6d0b20d7802c | -3.55586 | -62.07978 | 2026-08-18 06:18:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59ccab13-9380-310f-9de9-307690c4a698 | -6.74405 | -59.18012 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cc7e1a51-7392-345f-83ad-43606513bbf5 | -6.75311 | -59.16403 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7687ad76-b67a-3c5f-82da-59739be1649a | -3.55051 | -62.07902 | 2026-08-18 06:18:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fff10dc3-083a-3540-87ec-0e23c705d3cf | -6.75524 | -59.17079 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4286219b-52a2-3880-8ae3-baa6f5c99bb3 | -6.75987 | -59.16474 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dc64e00-28c8-3181-be9a-23f7a657eb74 | -6.77064 | -59.46228 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d7b12af-cb46-362b-bcd4-3f69e846c618 | -6.11004 | -57.73523 | 2026-08-18 06:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86a52172-44ac-37f4-8dc1-4bddae8cb63b | -6.8462 | -59.00497 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 09c7218d-d978-31a1-b4f1-9ddf8fd33039 | -6.8539 | -58.9992 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 169c9367-5366-3eae-8d11-eb434dfea600 | -6.74709 | -59.18076 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6aff3771-b037-363b-8c3f-26369fa9a09d | -6.84536 | -59.01119 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4422b42d-c8ad-3de5-82a7-227c42b97d09 | -6.78622 | -59.44675 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a9d1494-581f-3dcb-86f1-b2ef71c28755 | -6.70736 | -58.94228 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a2317ac-68ab-30be-8f79-70485e702760 | -6.74197 | -59.16762 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 91302737-5017-31de-955f-95d9b0d6b1cb | -6.79282 | -59.44781 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a6ae0ea-5cd7-3b9f-ba36-931b08e74847 | -6.78282 | -59.76203 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e8c426d-b026-3ba7-b5e8-c99e410fc39d | -6.85474 | -58.99305 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a67ca152-4324-349f-8e0c-1f5a73b6bf98 | -6.85219 | -59.01182 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 00a99998-8269-30e2-8b41-3d81f2aba416 | -6.77141 | -59.45661 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91179c7f-66ab-3db3-96c4-56dff9e9e245 | -6.84457 | -59.01699 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ac50889a-fb1d-357f-a1d3-616037d6a54c | -6.76484 | -59.45543 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a93e28de-e505-3f2b-bdcd-b92132a50ae3 | -6.69966 | -58.94805 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3df49ae-060b-3837-8575-9ce465716974 | -6.76408 | -59.46106 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcf63e0b-5680-3814-aaf7-f80007b4b275 | -6.75447 | -59.17665 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ff70f20-3811-3d6b-9754-51033dd0d220 | -6.75227 | -59.17014 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 41f100f9-16f1-3f0a-9036-b2fd8c00a9de | -6.75396 | -59.15793 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 98de4a22-6170-3c5a-b7ca-649179864fa1 | -6.85138 | -59.01777 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 79f547dc-0bf6-3fdf-9d5e-cdfd45f65fbf | -6.10405 | -57.73981 | 2026-08-18 06:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea904494-9c99-3169-baf8-2a7e80b98aed | -6.75372 | -59.18237 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf38bff9-7e68-3df6-9ac3-5da5946929d4 | -6.74862 | -59.16909 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9b55e4df-d148-379d-8234-b6882721acec | -6.76073 | -59.15851 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29eafd4e-22e0-3bd2-bfed-a0ba66900f26 | -6.74647 | -59.16253 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b8345125-0548-343e-9df0-e8c6e742d8ce | -6.74567 | -59.16836 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9f82c075-a21e-3da7-be9a-1280c7dbf847 | -6.83944 | -59.00378 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc068b82-00f1-3d04-85d8-bd9bf4d33412 | -6.7412 | -59.17352 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 82f04dd2-bbfb-36cd-864f-5cb91f52f29a | -6.75897 | -59.17121 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aeadaa4b-453b-3eb7-833c-96ac9587ffc2 | -6.75068 | -59.18161 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1b14cf87-6846-32dc-8f93-de4c243ed502 | -6.10501 | -57.73249 | 2026-08-18 06:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e2dc908-04f9-3973-8526-e0bf7b8c1b0a | -6.74042 | -59.17949 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e17535f3-12a9-3e7d-bcf0-bf981606f39a | -14.1821 | -52.93 | 2026-08-18 06:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 90242087-3bd2-3c66-8915-039ade974060 | -14.1631 | -52.9113 | 2026-08-18 06:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 57eec714-42c0-36e6-bd98-778132c0a87a | -6.7478 | -59.1716 | 2026-08-18 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 37ae473a-a9f5-331c-9610-26c00579cc9b | -14.8033 | -46.6453 | 2026-08-18 06:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 099abc30-3f37-3b37-916d-1a1bb1777f6b | -14.2017 | -52.9065 | 2026-08-18 06:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| ab7b4be5-3069-33f7-af34-020c4d506473 | -14.8233 | -46.619 | 2026-08-18 06:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3569855f-3b60-3f62-9245-9a24f208ca5b | -14.8228 | -46.6419 | 2026-08-18 06:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 56728075-1935-31a7-a023-f67ddafdc924 | -14.1824 | -52.9089 | 2026-08-18 06:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 154.7 |
| a46a69d2-9647-3eb4-a2c3-56ff2560fadc | -6.96125 | -59.03148 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f57685b-9152-3308-94e2-082aee9ca97e | -6.91552 | -62.90591 | 2026-08-18 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d408db9c-09fb-3996-8117-5a408312980d | -9.42574 | -60.41353 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f9813da-3b83-3886-87fc-1a83a27358ed | -7.60564 | -60.82505 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85763dd6-1dfb-3f1a-ba0d-c0c9a3eafadc | -8.09092 | -61.34087 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2222772d-04b9-3bd9-b604-79259ef42c7f | -9.42878 | -60.44073 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8884c95-3290-36b3-b89a-c18beb22ffaa | -9.53021 | -63.66304 | 2026-08-18 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e6fa501-7c1a-38a8-8d68-a5dbed3778dd | -7.61398 | -60.94986 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dabbd912-bd3e-3e53-bbf4-c8c80f15a129 | -9.17342 | -59.70365 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b690b235-4726-313f-a086-6a873475278e | -6.83966 | -59.00911 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f6b1a70b-03c8-382a-a297-154abd17d206 | -9.42642 | -60.40855 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 060a14f8-be69-371c-9cec-0760c2bc07cd | -8.90289 | -60.59399 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2dc9bdd-4653-324f-b14c-8cf936084ba4 | -6.95704 | -59.02456 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 69d84737-0f7c-3742-aa09-48599ae34d9c | -6.85325 | -59.01099 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a323ba40-7425-35f7-b1b3-08cd696d07d9 | -8.96426 | -60.52953 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73cc3c12-d777-3fec-9616-1f64b14777eb | -10.58328 | -63.54862 | 2026-08-18 06:20:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5771b57d-4af5-3fe4-8804-c7a2862dc6f8 | -9.42899 | -60.44112 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89e86be9-e148-352e-a5b7-9e681ba50bf8 | -8.4421 | -70.70653 | 2026-08-18 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a73f3db8-05a2-3d9e-8cf2-4bc81acdcec6 | -8.95146 | -60.51714 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b80ba4e2-aa49-34d8-8bd0-206479f629b8 | -6.85487 | -58.9984 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05787751-4e51-3df0-9388-8665df0c468d | -6.84805 | -58.99761 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 27ef0b56-2f73-3d97-a338-0d012b32f24f | -9.42234 | -60.43985 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2898b950-d95a-3004-9b31-3fe4f4c77680 | -9.06125 | -71.25632 | 2026-08-18 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd4df242-f663-361c-a440-4971800bb31a | -6.84044 | -59.00299 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d606c64c-38ef-3943-9c72-cef0a6bace83 | -8.9508 | -60.52227 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f526699-d0cb-3b45-820d-77b3672f5ff3 | -8.51589 | -70.27068 | 2026-08-18 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d663cd48-1485-35d5-8818-5e6ee2b61cf9 | -8.89943 | -60.55036 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a213d34-8f8f-3345-9cb5-e6381ee9023f | -8.9451 | -60.51622 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3978fbd6-acd3-3dbd-bf49-502fe213408c | -7.88465 | -63.75982 | 2026-08-18 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 857a8ab1-7f2f-3d4e-8852-6b8e9e0d377b | -9.42437 | -60.42411 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2839a77b-b514-3c67-a6bd-681b95c0f6fe | -9.42741 | -60.45131 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 915b830c-1db0-387d-afdf-aee66328297a | -7.61179 | -60.82589 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f573214f-f7da-3c96-a338-38cdbedf0e55 | -7.91386 | -61.74266 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cb7c71c-b885-399f-a9d8-44cc5ae07194 | -7.90858 | -61.73782 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 770d0595-51c0-3828-9a66-da22bb2f8901 | -9.42098 | -60.45041 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e0341c4-3c0e-3483-a89f-e697b24228ea | -6.85407 | -59.00467 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 202f607f-8526-3375-8bd2-484f0507885b | -9.83675 | -65.06379 | 2026-08-18 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27d8a5b6-4e7b-33bf-9ef7-4cd3a9b50413 | -8.94575 | -60.51109 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README60.md)
