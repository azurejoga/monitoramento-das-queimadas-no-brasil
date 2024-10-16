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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 532772ee-b54e-3846-b51d-b92b2da6d1e5 | -1.1345 | -49.1911 | 2024-10-16 13:15:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| fc71d928-2993-3bdc-937c-11215b984780 | -18.2379 | -56.3972 | 2024-10-16 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 188.8 |
| bdecd5e0-47c2-3df8-919f-d71c47f66da9 | -18.1978 | -56.4233 | 2024-10-16 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.6 |
| 92ecaebe-2821-3c28-b757-172a87022214 | -18.2177 | -56.4207 | 2024-10-16 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.7 |
| f39019cd-4ab2-3865-9ebd-932f72ab56ac | -18.218 | -56.3998 | 2024-10-16 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.0 |
| 63e00965-1b4d-339b-8362-d66813c827cb | -1.1345 | -49.1911 | 2024-10-16 13:25:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 560b52d5-976d-3fe9-92b5-5d3d658185c6 | -1.1346 | -49.1698 | 2024-10-16 13:25:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 487ee1e5-e275-3aec-b76f-446bc4ec842b | -0.8583 | -48.7248 | 2024-10-16 13:35:11 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c1d3f14b-c2dc-3d8d-869b-ea47b8548be3 | -1.1345 | -49.1911 | 2024-10-16 13:35:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f9ac3082-d753-3bc7-9cb0-0d09c91c4d6d | -1.0796 | -48.8721 | 2024-10-16 13:35:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| febcd9d2-88d6-3d88-87e9-655a9f710e71 | -1.1346 | -49.1698 | 2024-10-16 13:35:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 0cb4067a-75e8-3958-8875-8f70a0c24aab | -1.153 | -49.1696 | 2024-10-16 13:35:13 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b37e0031-02a4-3ac9-811e-4d7582352140 | -0.766 | -48.7042 | 2024-10-16 13:45:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 78bbcec6-55de-34b2-a7fe-44f8991e5dd6 | -0.9829 | -52.4415 | 2024-10-16 13:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 7c36a644-842e-3c62-ade0-47f03a65aef1 | -1.0796 | -48.8721 | 2024-10-16 13:45:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e462f63c-2a7a-372a-b8f7-520039c17168 | -0.766 | -48.7042 | 2024-10-16 13:55:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4229801b-7bac-3229-8ff3-030ed17ed22f | -1.0796 | -48.8721 | 2024-10-16 13:55:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 3b9aa26e-560c-3fe1-a02f-a3dabcf861ea | -0.9829 | -52.4415 | 2024-10-16 13:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 8d5c9fe2-647a-3875-b615-ace766f5ff74 | -2.6119 | -49.0772 | 2024-10-16 13:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| d7fb25c1-dc1d-31ae-9bd9-b879bde46dd0 | -2.6118 | -49.0985 | 2024-10-16 13:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 6e4e52c3-55d1-367f-90a4-9f4c07ebb7ba | -3.08 | -50.36 | 2024-10-16 14:05:09 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51d467be-75b1-390f-93c8-abf3c3d07a52 | -3.06 | -50.36 | 2024-10-16 14:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df9c901b-fab1-385d-a396-78c09e680dac | -0.4889 | -49.1327 | 2024-10-16 14:15:09 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| dbb6f894-008c-3dac-b03b-6c6fa8e52c79 | -0.766 | -48.7042 | 2024-10-16 14:15:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| adb891a8-b507-3387-9ffd-532ff9bcbfea | -0.9829 | -52.4415 | 2024-10-16 14:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| e7e85fca-7304-3584-bf09-a676d2c2190d | -1.0796 | -48.8721 | 2024-10-16 14:15:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f4a15455-f9c7-3075-b055-de67664ca9f3 | -2.5175 | -49.6741 | 2024-10-16 14:15:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 95b41629-ddad-301b-8457-276d9dd98dba | -2.395 | -53.7196 | 2024-10-16 14:15:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 24ec7b55-3948-33d1-8b6e-7de4776e331a | -3.0688 | -50.3536 | 2024-10-16 14:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 276.8 |
| 0dfd94df-5846-3eab-afd6-e9b03f0ab55e | -3.0687 | -50.3746 | 2024-10-16 14:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 466.2 |
| 1205267d-84a3-3078-959e-8b46104224c7 | -0.8583 | -48.7248 | 2024-10-16 14:25:11 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 01a0c204-686a-357d-afb7-2490e4daa806 | -0.9829 | -52.4415 | 2024-10-16 14:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 12957985-3ccf-3c8d-a508-07c92ccd02ad | -2.5175 | -49.6741 | 2024-10-16 14:25:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f19d19ad-aa1b-310b-90e9-29500ab3e136 | -2.6119 | -49.0772 | 2024-10-16 14:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 1e57666e-3fd5-3d2f-8da7-b462c2d9ab7d | -2.6118 | -49.0985 | 2024-10-16 14:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 9696a559-49d5-3ece-97b9-d83a160bc37e | -3.0688 | -50.3536 | 2024-10-16 14:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 246.4 |
| e7925081-545b-302b-be8b-c04963b9719b | -3.0687 | -50.3746 | 2024-10-16 14:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 500.2 |
| 81567133-dfb8-3b8a-9222-e9d34d04f22d | -18.1013 | -56.2905 | 2024-10-16 14:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 0129e19f-30fe-3349-a764-885bf110812e | -0.766 | -48.7042 | 2024-10-16 14:35:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 750c5acb-b940-309d-be05-608ef4033391 | -1.0796 | -48.8721 | 2024-10-16 14:35:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| edd54355-2001-3a7d-9f5c-c57806b5014d | -0.9829 | -52.4415 | 2024-10-16 14:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| ff562d06-d152-308e-917e-b54fa813abb2 | -2.499 | -49.6745 | 2024-10-16 14:35:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4913c8b3-d15a-39bb-8ec0-93646dee7b9a | -2.5175 | -49.6741 | 2024-10-16 14:35:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 30e02bff-90a1-391e-b071-3ed0fe89924d | -2.6119 | -49.0772 | 2024-10-16 14:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 197.6 |
| 726c25ae-b0d2-3166-a536-e58c2b620437 | -2.6303 | -49.0767 | 2024-10-16 14:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 016c5da5-2c4a-3c6c-9ba5-712ac7560a90 | -3.0687 | -50.3746 | 2024-10-16 14:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 398.2 |
| 6d0cd686-07cc-3da8-b544-d245a2fee475 | -3.0688 | -50.3536 | 2024-10-16 14:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 233.6 |
| 0f41f9f4-d324-39c2-a402-eba4e7f64f92 | -11.7104 | -65.2235 | 2024-10-16 14:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| fa83c7e7-e316-3be9-81d1-24ede9e02253 | -11.6917 | -65.2243 | 2024-10-16 14:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 91321499-b143-369e-bd4b-0f284e27dde5 | -18.0811 | -56.314 | 2024-10-16 14:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.6 |
| 271a8003-d720-3a48-b468-c36c372c818e | -0.766 | -48.7042 | 2024-10-16 14:45:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 24757ae5-3e2d-3e2b-8b7b-8fb16875c863 | -0.7661 | -48.6828 | 2024-10-16 14:45:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 446ea257-57ab-39c4-9923-9e71167cd007 | -1.1345 | -49.1911 | 2024-10-16 14:45:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 5938095d-df2b-3308-b1df-ee5587ee45c6 | -0.9829 | -52.4415 | 2024-10-16 14:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| c86d8601-a8de-3e9c-882a-3be2fe283c1b | -1.153 | -49.1696 | 2024-10-16 14:45:13 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 489008d4-443d-32e5-b993-256e0572763c | -2.5175 | -49.6741 | 2024-10-16 14:45:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 5c8b02b2-2230-3655-bab4-da43357ba95d | -2.499 | -49.6745 | 2024-10-16 14:45:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e9700be7-4c3c-39a6-81f9-f0a8161942cd | -2.6118 | -49.0985 | 2024-10-16 14:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 273.6 |
| 8aa3e174-c287-36ca-93f2-aa6ce7e32239 | -2.6119 | -49.0772 | 2024-10-16 14:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 254.1 |
| 083234aa-c36d-3d28-b5f8-f9cf125e19b8 | -3.0687 | -50.3746 | 2024-10-16 14:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 342.2 |
| 51c1415e-78f8-37f5-8cf0-59eed690d14b | -3.0688 | -50.3536 | 2024-10-16 14:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 222.0 |
| a7f0ef0c-e8be-34b2-b56e-80ca0e92e9a1 | -4.285 | -50.9586 | 2024-10-16 14:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |


