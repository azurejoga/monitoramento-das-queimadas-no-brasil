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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ba62c9d-5c03-3429-b2f4-3978444850c6 | -5.6894 | -46.435 | 2024-10-21 02:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 52996f9f-c21f-32fb-80aa-12cf0dbab352 | -5.6896 | -46.4128 | 2024-10-21 02:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 0ec1297e-8e4e-3395-a45a-391b03c7ea48 | -9.3718 | -66.4891 | 2024-10-21 02:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 063c5688-478a-3f0b-ab8f-436677389f04 | -12.5147 | -63.3014 | 2024-10-21 02:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 31.7 |
| d9005368-ebb1-3a21-bf83-d01262a848ff | -12.5168 | -63.0329 | 2024-10-21 02:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.9 |
| b8cb538b-fd8b-35a9-b13c-80690aed04f5 | -17.7065 | -57.4569 | 2024-10-21 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 5c3613cd-8393-3605-9584-45b1c5c94645 | -18.2832 | -56.0785 | 2024-10-21 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 3c23f37e-17fe-3536-8dce-e612c8f90cf9 | -18.2828 | -56.0994 | 2024-10-21 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.4 |
| 89280eff-bfad-3603-be2c-d38819eed1e1 | -1.1834 | -53.6368 | 2024-10-21 02:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 741cd157-983d-377a-9829-21cb4e11c92c | -1.1835 | -53.6166 | 2024-10-21 02:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 8e52ecea-2993-372f-a992-7be3bc2de023 | -1.2018 | -53.6366 | 2024-10-21 02:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b767ca5f-3fca-3182-9fa3-aac10f2f550f | -2.2199 | -50.4594 | 2024-10-21 02:35:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 146597be-ffd3-330f-a317-d2b46d003e8e | -2.4824 | -49.1233 | 2024-10-21 02:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| eea5ad79-dc2b-3fc3-af32-1a4a87a6dabb | -2.4824 | -49.102 | 2024-10-21 02:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 3a60d720-66dd-3c87-8c80-2727227a910b | -2.7773 | -49.3067 | 2024-10-21 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b45f2e7a-ef1a-3b8c-a700-13d0b9217e33 | -2.7885 | -51.3618 | 2024-10-21 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 30a34283-e079-30cd-bfe8-8b70797171d4 | -2.8069 | -51.3613 | 2024-10-21 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 54972e1e-74d4-398c-8d97-d56795ac08d4 | -2.8668 | -45.4631 | 2024-10-21 02:35:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 543c6bf2-597e-38c1-ad12-c8306fcba37b | -2.8555 | -53.3459 | 2024-10-21 02:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| fa2a52f4-79fb-362a-b2e4-8864dabb88fb | -2.8556 | -53.3256 | 2024-10-21 02:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 077ec450-47d5-3f41-b8d0-7324a5e6cee4 | -2.905 | -45.2143 | 2024-10-21 02:35:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 9a96083a-4fb2-3fd1-8eba-e663edc3af45 | -3.1138 | -53.1163 | 2024-10-21 02:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 300df0e0-4541-32e6-acaa-d12c0338525c | -5.6894 | -46.435 | 2024-10-21 02:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 17c1a9aa-af13-3bce-a215-a40ca4bb3dac | -5.6896 | -46.4128 | 2024-10-21 02:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| dbcda084-0c5a-3c83-8a9c-c71e8b606349 | -9.3718 | -66.4891 | 2024-10-21 02:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 925e492a-631f-3cbf-b5eb-82e44bfa305f | -12.5146 | -63.3205 | 2024-10-21 02:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.9 |
| cf519338-1656-39f1-a4d9-08add68692da | -12.5147 | -63.3014 | 2024-10-21 02:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a7e77878-55b6-39e1-9e39-b05b948526c5 | -18.263 | -56.1021 | 2024-10-21 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.9 |
| 359a4503-5b26-30c8-b48a-dfeace60aa59 | -18.2828 | -56.0994 | 2024-10-21 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 9faf9bd8-c7f4-325a-95ff-67f7c69ec96b | -12.51278 | -63.30795 | 2024-10-21 02:41:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 76d45158-3f98-34c3-9750-82336dd53090 | -1.1834 | -53.6368 | 2024-10-21 02:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 28a3e184-e57e-3a3c-8c17-5086a06a95a3 | -1.1835 | -53.6166 | 2024-10-21 02:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 99afcaa5-0214-3a17-b28a-695a6a268fd6 | -1.2018 | -53.6366 | 2024-10-21 02:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| fc7359bc-5466-3632-a977-dcdce88b4bc0 | -2.2199 | -50.4594 | 2024-10-21 02:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 10b608cc-ea64-3c2e-9583-3419e21c93b8 | -2.4824 | -49.1233 | 2024-10-21 02:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 593967ce-6d78-3bcb-b4df-b5175d874aa0 | -2.4824 | -49.102 | 2024-10-21 02:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 2fb258a1-1ede-3e43-bbd3-65a91e6b88c8 | -2.7773 | -49.3067 | 2024-10-21 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 4b823633-d6ab-341e-a189-6715b4b70c10 | -2.7885 | -51.3618 | 2024-10-21 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 93b6fdaa-d369-390d-bc48-c275a7b420d4 | -2.8069 | -51.3613 | 2024-10-21 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 05716713-1141-332f-9365-dee3982ce7e0 | -2.8556 | -53.3256 | 2024-10-21 02:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 4a7ffe90-a931-36c2-8890-de930619acae | -2.905 | -45.2143 | 2024-10-21 02:45:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 79f9d6bd-3e93-32df-bfa6-1dcb8238cd3a | -2.9051 | -45.1918 | 2024-10-21 02:45:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a99919aa-1215-3e47-818e-4ab4eb8de4c8 | -3.1138 | -53.1163 | 2024-10-21 02:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 8e9d7a28-1263-3c91-af99-83ffbe9a4eea | -3.2146 | -50.8093 | 2024-10-21 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 312d3e38-a6af-3a75-90ec-b3b2bee7cfd7 | -5.6894 | -46.435 | 2024-10-21 02:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| a3f35d84-f627-31f4-84c8-f47cbab9c902 | -5.6896 | -46.4128 | 2024-10-21 02:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7f539c09-f738-3e71-b40f-41fe210df250 | -9.3718 | -66.4891 | 2024-10-21 02:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 159add66-7778-332a-9fa3-34b51227d571 | -12.5167 | -63.0521 | 2024-10-21 02:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 36.3 |
| f2975e4d-27f0-389a-9ee1-26fe762645ce | -12.5168 | -63.0329 | 2024-10-21 02:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 03b448fc-5719-391f-9440-01f7b7e62a82 | -12.5357 | -63.0319 | 2024-10-21 02:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 2cbe7ec0-32ad-3a0c-8fd1-662d90b59235 | -18.2828 | -56.0994 | 2024-10-21 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 6ac711cc-8a8b-3ad7-8295-4f59668cfa14 | -1.1834 | -53.6368 | 2024-10-21 02:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 3c077b93-cc02-3d9c-99a2-b497689ada8a | -1.1835 | -53.6166 | 2024-10-21 02:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 252dbd62-1579-3248-9908-5b6b380218b1 | -1.2018 | -53.6366 | 2024-10-21 02:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 1b06a7c1-abab-34b3-890b-99bf2e2c8c57 | -2.4824 | -49.1233 | 2024-10-21 02:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9b7515bb-5dd3-3300-90c6-b84434abf3c0 | -2.4824 | -49.102 | 2024-10-21 02:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 994524a7-ddda-3895-aea9-c8a178898fba | -2.7885 | -51.3618 | 2024-10-21 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b3df573a-9740-3347-b58f-4d16b3fec963 | -2.905 | -45.2143 | 2024-10-21 02:55:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| e3222e76-b847-3125-ba6d-ae8009f316f6 | -2.9051 | -45.1918 | 2024-10-21 02:55:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 5a89d773-eb9b-34c3-a6a9-ff393f6bdccb | -3.1138 | -53.1163 | 2024-10-21 02:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 74ff7015-735f-3fb1-8b70-4013d2d23cea | -3.1962 | -50.8099 | 2024-10-21 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 44171c77-d283-3d7d-9910-07b4abe2c041 | -3.2146 | -50.8093 | 2024-10-21 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7436e54e-4a3f-3d7c-a585-de0398fd51a9 | -5.6894 | -46.435 | 2024-10-21 02:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 1e7fab45-83c7-313f-b45d-80bb34536038 | -5.6896 | -46.4128 | 2024-10-21 02:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 227e7334-e618-3f49-84cd-06726507ab12 | -12.5147 | -63.3014 | 2024-10-21 02:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 41104c15-bce1-3bf6-a871-c93cab1e7dff | -12.5168 | -63.0329 | 2024-10-21 02:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 0f0c2766-e589-309f-bae2-d09fa4b24e25 | -12.5357 | -63.0319 | 2024-10-21 02:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| d82ec84b-74e5-3463-90da-0224233ef02d | -18.2828 | -56.0994 | 2024-10-21 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.2 |
| dd3dcf38-6f32-30c0-8595-e34ea1adc4aa | -10.69838 | -37.06472 | 2024-10-21 02:58:00 | NOAA-20 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 14b79bb6-80ef-33ab-b0b1-a7dea96ba3f3 | -10.69738 | -37.06976 | 2024-10-21 02:58:00 | NOAA-20 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4d9620c0-7e15-3afa-91cc-5100688f940c | -10.28411 | -36.30851 | 2024-10-21 02:58:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ca46e87e-59b3-37b9-892b-7db51e140cff | -10.2832 | -36.31312 | 2024-10-21 02:58:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74b242fe-2ec7-3630-821f-3aa69c9724b3 | -10.0998 | -36.34258 | 2024-10-21 02:58:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 346d798a-4c84-33c3-a2d3-e1cca717a6c9 | -10.09464 | -36.33667 | 2024-10-21 02:58:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 44e6f5d0-ffc6-3d11-89cb-d8fa82d07422 | -10.09376 | -36.34116 | 2024-10-21 02:58:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 946553df-3e52-3d13-ba47-0a299aaa8349 | -1.1834 | -53.6368 | 2024-10-21 03:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| efdc7f16-bb0d-3eca-94d7-13ae30c6b3f9 | -1.1835 | -53.6166 | 2024-10-21 03:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 8aed285b-a0d8-3e7f-b4ae-38bf411c71f6 | -1.2018 | -53.6366 | 2024-10-21 03:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d4a27af6-304a-3d92-a0d6-adc7f014205e | -2.4824 | -49.1233 | 2024-10-21 03:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 22a67c61-62e8-3119-ba95-8094e422b25c | -2.4824 | -49.102 | 2024-10-21 03:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 0f41b54c-2952-326f-b6cd-b021f2eb7d20 | -2.7885 | -51.3618 | 2024-10-21 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 99519383-02ff-3787-b1f1-f8408fe81792 | -2.8668 | -45.4631 | 2024-10-21 03:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 25db656c-ca49-374c-abfc-6696249dff3e | -2.905 | -45.2143 | 2024-10-21 03:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 517cedcf-b6f5-35ae-a41a-0c35a4c4a9d9 | -2.9051 | -45.1918 | 2024-10-21 03:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 817c86ca-09a2-333e-b15f-bc0d9e46b520 | -3.1138 | -53.1163 | 2024-10-21 03:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d3c423ab-816a-3040-ac8c-a4b823c8f2c4 | -3.1962 | -50.8099 | 2024-10-21 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3d62b9e9-6e8a-3459-8e6c-ebfdd3702b81 | -3.2146 | -50.8093 | 2024-10-21 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1ef8cef1-9653-339c-a339-d21fafac66ad | -5.6896 | -46.4128 | 2024-10-21 03:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 892585b0-1158-3547-bde7-0e216ed2272a | -5.6894 | -46.435 | 2024-10-21 03:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 8bf1b33f-78a8-3a02-a829-8e522b7250f4 | -12.5357 | -63.0319 | 2024-10-21 03:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 9bcb8a0c-5237-3d77-ab4c-8317935c50c6 | -12.5356 | -63.051 | 2024-10-21 03:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 30.6 |
| d0465bdb-9830-3b4d-9be1-e2243f676b20 | -12.5167 | -63.0521 | 2024-10-21 03:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| cff078bb-9951-39e1-accb-b2523d171438 | -12.5147 | -63.3014 | 2024-10-21 03:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.1 |
| f7e64ee1-120b-318e-89e7-cd8b8b030145 | -18.263 | -56.1021 | 2024-10-21 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 58bd1f0f-cc41-3900-a819-eea7c0198f28 | -18.2828 | -56.0994 | 2024-10-21 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 1e4f9d24-2a60-38f2-b652-ad390e7c0e4a | -1.1834 | -53.6368 | 2024-10-21 03:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| a2ff315b-e2e6-3717-88a6-0c04e6b0db46 | -1.2018 | -53.6366 | 2024-10-21 03:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| fffb8591-fd7b-3731-b643-bed645911f52 | -2.4824 | -49.1233 | 2024-10-21 03:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| dc41629e-ca65-3ae5-96a0-407325a3209d | -2.4824 | -49.102 | 2024-10-21 03:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d4e4744e-2cfe-363b-a853-1c85fb54c01e | -2.8069 | -51.3613 | 2024-10-21 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |


[Clique aqui para ver as próximas entradas](README20.md)
