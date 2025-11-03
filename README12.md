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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4ec76d9-b2ee-3bb0-9a3b-ae1c0439d47b | -1.27282 | -53.85546 | 2025-11-03 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d046d9ce-a6cc-3cf6-81b6-cf1ab88ff690 | -1.27466 | -53.85892 | 2025-11-03 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f984c06-37b7-37a7-aef8-ba8ce956c8e7 | -1.27523 | -53.85509 | 2025-11-03 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fc38dbf-baf3-3d67-a5a0-34c98da4e95a | -1.26401 | -53.837 | 2025-11-03 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b0b6738-f2af-3741-9450-0c469aa48b80 | -5.18131 | -60.30815 | 2025-11-03 05:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de342c5f-1557-3a7a-a390-660b8116f880 | -1.40056 | -53.08914 | 2025-11-03 05:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2261b8e0-7820-3e9c-b587-3374a823cbb6 | -1.96468 | -52.10833 | 2025-11-03 05:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fae1dfc6-1205-390b-80ea-9f6ddeb090b1 | -5.18689 | -60.30132 | 2025-11-03 05:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60946201-df0b-3b4a-8973-d7d8b0b951ea | -9.71432 | -61.30115 | 2025-11-03 05:42:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1ea692c-f71f-3c32-bff8-9e5b6fb503ed | -6.6226 | -55.02129 | 2025-11-03 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a08b79ba-a392-39f7-8049-eaf2109a9dd6 | -10.84688 | -56.95836 | 2025-11-03 05:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 936a2d7e-2a42-3d96-a78b-bce2a9305f6f | -10.8526 | -56.95584 | 2025-11-03 05:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34dcda03-ca9a-388a-9237-8ec6a3e5f091 | -9.15283 | -62.40586 | 2025-11-03 05:42:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 331471e1-aa71-3729-8ab4-4066a090a19a | -9.35649 | -60.85553 | 2025-11-03 05:42:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1284491b-3717-3d44-9dd2-c3069802d3f5 | -9.15458 | -62.41919 | 2025-11-03 05:42:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02c81758-6fea-3a4a-adcd-a88824541d0a | -9.18618 | -63.73455 | 2025-11-03 05:42:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0b8c8c33-0776-320a-a6ba-7250f861e1ad | -10.10446 | -62.92239 | 2025-11-03 05:42:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3ac76a1-bc97-3ab7-ad0d-1c9a9b27ab06 | -10.84728 | -56.9551 | 2025-11-03 05:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f331836d-845c-30a6-bb45-0ae0d63927ee | -10.05453 | -64.99176 | 2025-11-03 05:42:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71217671-0a57-3f7b-87e2-b1cef6d46f37 | -10.10335 | -62.92125 | 2025-11-03 05:42:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89391d33-5826-372c-be16-40dd04175350 | -8.96386 | -63.62797 | 2025-11-03 05:42:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6a6fc63f-fef6-3382-a9d0-c06713ac6c0e | -13.49095 | -61.4544 | 2025-11-03 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea162b93-e7f8-38d9-a7de-8ae18b58aebe | -12.43272 | -63.14405 | 2025-11-03 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1687404b-1f60-36f0-be1d-30612b3b992a | -12.57977 | -62.95519 | 2025-11-03 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 447cc7f0-1ade-33d5-91e7-2530930d5d82 | -13.49144 | -61.45071 | 2025-11-03 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6bb5027-3903-3541-9892-bcc53b5445cd | -12.58408 | -62.95133 | 2025-11-03 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f64a29cd-1ea3-3d7a-b59e-df53a63af8fa | -12.43635 | -63.14459 | 2025-11-03 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9fc6f68-67a8-3527-a87a-dfbc0fbb8321 | -13.49651 | -61.4439 | 2025-11-03 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b45e8ed-a58c-3720-9df8-3b58937604b2 | -12.96105 | -60.86311 | 2025-11-03 05:44:00 | NOAA-21 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d43aeb3f-d0aa-34ae-bc1c-0b61877f4687 | -13.50059 | -61.44448 | 2025-11-03 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30771ce1-3963-3a11-984b-a6d20fb60eba | -12.43999 | -63.14515 | 2025-11-03 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 792e6f55-cc3a-383f-a5d1-36c705d6cf13 | -6.5631 | -51.1126 | 2025-11-03 05:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8fa06fba-d09c-3930-9b83-dddfdb8d2362 | 3.2278 | -60.75452 | 2025-11-03 06:07:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54c5c737-b78b-3a6f-96ad-e0ed7992dc67 | -5.18299 | -60.3069 | 2025-11-03 06:09:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d1f85e7-d151-34d3-b259-80afeb0cd88f | -5.17689 | -60.30598 | 2025-11-03 06:09:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a763f24-bc36-3b71-ab0a-5c9108d63396 | -5.18467 | -60.29957 | 2025-11-03 06:48:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0221f5fc-d82d-39f4-84e3-23cdc3cec868 | -1.96615 | -52.10395 | 2025-11-03 06:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2654ebfd-724c-3325-84f3-c5d81e166067 | -1.39512 | -53.08641 | 2025-11-03 06:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b6879003-e296-32c7-b81d-465d37d27cdd | -0.89722 | -52.03196 | 2025-11-03 06:48:00 | AQUA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d6a48882-1958-3265-b9ee-f2cf58c2c3b2 | -10.84589 | -56.951 | 2025-11-03 06:52:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 46be2725-9917-332e-a3f2-9d50aac77f5d | -6.8971 | -38.6312 | 2025-11-03 13:00:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 99.1 |
| fd367146-c463-3b58-9c37-8a08a72458d4 | -2.9008 | -42.071 | 2025-11-03 13:10:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 42341bc9-370a-357e-a52a-ba6add0a80e7 | -2.9009 | -42.0472 | 2025-11-03 13:10:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d92ec0f8-34ed-3842-9474-82a7b8532a63 | 0.9844 | -51.2279 | 2025-11-03 13:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4d3cfab0-cdc9-3186-bfa7-9cf3abfb6655 | 1.0028 | -51.207 | 2025-11-03 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.4 |
| df9be77d-813d-3b8d-b0f1-3c7d65845906 | -3.29 | -42.6448 | 2025-11-03 13:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8071571b-fd19-3088-b08e-12c276a624ce | -3.2901 | -42.6213 | 2025-11-03 13:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 6f3d9983-f430-3c73-b6ac-582c608f2a66 | -4.903 | -42.0085 | 2025-11-03 13:40:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| a4df51f0-0a34-3c74-82d5-54a2c08f3cb7 | -4.903 | -42.0085 | 2025-11-03 13:50:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 7ee74418-a022-3053-80c3-6266ca963d4a | 1.0028 | -51.207 | 2025-11-03 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 07401797-37d3-3d1c-a689-4cec3a13ecd5 | 0.9844 | -51.2279 | 2025-11-03 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 2f658ac5-c750-3197-9ad4-311627186738 | 1.0028 | -51.207 | 2025-11-03 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0d230ad6-48cc-340d-925d-0e67539eaba0 | -4.903 | -42.0085 | 2025-11-03 14:00:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 7afa6e70-7ea9-3fa1-ac53-42a4babbb3f3 | -3.2901 | -42.6213 | 2025-11-03 14:00:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 381d057d-4643-3b65-902c-b3ffddf0b733 | 0.9844 | -51.2279 | 2025-11-03 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 188.9 |
| 351853e6-5d20-31d6-a985-9c33b1608c97 | -10.285 | -44.581 | 2025-11-03 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 0e231548-d0de-38de-8995-7c21e515df31 | -10.4219 | -44.3542 | 2025-11-03 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 268.8 |
| 99728408-3fda-3c99-9081-daec89be65b8 | -10.2854 | -44.5578 | 2025-11-03 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 136.5 |
| eb20f804-d4ef-3052-bcfe-bdd7b81d173d | -10.4032 | -44.3335 | 2025-11-03 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 0887b226-fb35-3fc7-8d88-11863b021bb1 | -9.4123 | -44.552 | 2025-11-03 14:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 14f6fe12-e360-3094-915b-25c21aedc8f9 | -9.8546 | -44.1496 | 2025-11-03 14:10:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |
| d8af4f38-e42a-3867-8a3b-81333020b6b8 | -9.8627 | -44.8656 | 2025-11-03 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 8d41d668-cf0e-3453-8f38-5c02772ebc48 | 0.9844 | -51.2279 | 2025-11-03 14:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 239.0 |
| 192e67e5-5e8d-38cf-a5f4-de3ba4ccc1a6 | 1.0028 | -51.207 | 2025-11-03 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7c5f7d2c-0759-3199-8c80-b0d5ce7f45c6 | -4.4464 | -45.6845 | 2025-11-03 14:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1ca6f6e4-f906-3d63-a4bb-f7cba225c36f | -10.4795 | -44.3232 | 2025-11-03 14:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 131.5 |
| c30a6245-bbf1-33d9-b3fd-2eb528cd54c0 | -10.4032 | -44.3335 | 2025-11-03 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 95aaaf41-32b4-398c-9fc2-9f1bdffc76fd | -9.9011 | -44.8378 | 2025-11-03 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 9d721d58-33e6-3cd9-a3bf-20e321b9f7aa | -10.3041 | -44.5785 | 2025-11-03 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 16bbf510-6ee6-3765-ae95-6214628566ba | 0.9844 | -51.2279 | 2025-11-03 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 278.2 |
| 2bbdbb44-93d3-3717-b75d-1a65c0e62e87 | -4.903 | -42.0085 | 2025-11-03 14:20:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 71a31650-c740-3a26-a13f-200a940af29c | -10.4028 | -44.3568 | 2025-11-03 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 272.6 |
| 6ed7c929-ab00-36cc-92b2-330b2b9ec5b3 | -10.4222 | -44.331 | 2025-11-03 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 2c8b386a-a4d8-35c7-b7e3-a0709d67e0f8 | -9.9201 | -44.8354 | 2025-11-03 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| d3b4e0f5-dcce-370b-bd10-17724f4fb50c | -5.5304 | -41.0964 | 2025-11-03 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| 553b3bc4-c339-3e75-a7bc-98bc0329b717 | -10.4417 | -44.3051 | 2025-11-03 14:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| d613d5c8-dfa5-30a7-b170-3e2234fae77d | -10.2473 | -44.5628 | 2025-11-03 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 793483bc-8f68-3747-ac14-f136f37e27fe | -10.2854 | -44.5578 | 2025-11-03 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| edd5b48f-e3c4-3841-975f-3e1acecf78a1 | -10.4222 | -44.331 | 2025-11-03 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 89eeb561-4377-3f7f-b4a1-ca13caae3415 | -9.8546 | -44.1496 | 2025-11-03 14:30:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 6c33bf3b-870b-3f5e-870d-40af1742c545 | -4.4464 | -45.6845 | 2025-11-03 14:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 2feaa34d-920e-30dd-ae45-41d96332516d | -10.4417 | -44.3051 | 2025-11-03 14:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 4e74f795-229d-37de-9a74-ee12f7d097a4 | -9.9201 | -44.8354 | 2025-11-03 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 82a092a1-37a9-3e5d-8c60-9f73b94ba238 | -11.0374 | -44.0355 | 2025-11-03 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 0eb88999-fab1-31a4-bfbe-e3493973a16f | -10.2473 | -44.5628 | 2025-11-03 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 141.8 |
| d95b5fc7-e60a-3766-ae7d-3ff34fbaf581 | -10.4032 | -44.3335 | 2025-11-03 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 5ab77ea9-5208-3115-ad73-d936b9af6947 | -11.0566 | -44.0327 | 2025-11-03 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |


