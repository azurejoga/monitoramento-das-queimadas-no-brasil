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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6625fe5-5bd8-3c80-b4b0-398e74f0f0fe | -4.05584 | -51.12204 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 316611f2-9a5d-32e2-a144-9e89e83945f3 | -4.05057 | -51.12146 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e61b735a-5853-3e87-b654-14ab0d69bef7 | -5.79695 | -51.61186 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72a83fc6-0584-3273-8565-4634f99a2ea8 | -5.7965 | -51.61506 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8396234-9f6d-32ff-b3e5-e77a3990e53d | -5.77168 | -51.45126 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19ab4ab9-f5a3-3df4-8ca7-df1644f77ec8 | -5.77137 | -51.45171 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6629cfa1-1df0-3fd0-b48f-0c83599e0149 | -5.77121 | -51.45451 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bd22d2f-773d-35c6-b0c0-e53186c51729 | -5.77092 | -51.45498 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b06731e-ba42-3b90-8911-a992b0c8e0e3 | -5.76642 | -51.45059 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e85673e2-ecb2-3ebf-a583-359f6642be52 | -5.7661 | -51.45103 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47684c63-b749-3eb2-9915-64e3e05aedea | -5.76594 | -51.45388 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e5804c2-e71e-395c-b1b3-b4f1f9b59aab | -5.76565 | -51.45433 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bd71d19-bcd4-3c9e-b302-d3e53d60d10f | -5.76084 | -51.45032 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1f3bd8c-3824-36d6-a398-032d54a74353 | -5.76068 | -51.45318 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcd4ea67-1d01-357f-a173-a0abe6e1c40d | -5.61312 | -51.16632 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 398acc1c-2461-3549-8b01-c64ec36cb67f | -5.61265 | -51.16973 | 2024-10-08 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7508a38b-ebaf-3cf6-81e9-628efefea4dc | -2.2008 | -51.95696 | 2024-10-08 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f336b72-e66a-3603-a7cb-cc913acb3195 | -1.63671 | -52.58223 | 2024-10-08 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b442a137-dd78-388b-bf21-b3cf36b37e18 | -1.63601 | -52.58686 | 2024-10-08 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f86bad1d-7461-383c-b4c6-eeea846b837d | -1.63285 | -52.57691 | 2024-10-08 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| aebf856c-86ca-3d6a-9359-5b933c6d5f2a | -1.63215 | -52.58155 | 2024-10-08 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3728b362-ed9c-36e3-859f-62ef54c25af1 | -1.63191 | -52.57852 | 2024-10-08 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f43bec7c-2a74-3e39-994e-bfbeaac22c26 | -1.63117 | -52.58315 | 2024-10-08 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b552357a-2a78-3c4f-bd8d-5c4de0668fe9 | -1.32414 | -52.81026 | 2024-10-08 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05b879ff-084f-35ae-ae5c-22e1df23644d | -2.87848 | -52.89948 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b8533a4-9123-335c-8bc9-80eecbfd9d91 | -2.87779 | -52.90414 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9738c5d-690c-3665-9627-e44cc4447c20 | -2.87722 | -52.90108 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 841a6097-7cb0-3a27-a007-7d1f8afc9b52 | -2.87711 | -52.90876 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12999911-e5b9-3549-a00b-845a72c69d29 | -2.87649 | -52.9057 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ae25575-ecc5-3f6b-9a43-eb408547f418 | -2.87643 | -52.91339 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85cd58ec-61c1-3e83-a760-e27c1c22ea44 | -2.87578 | -52.91032 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e20b57c-f092-3f86-81a5-3854779f9b7a | -2.87395 | -52.8987 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a7f7a60-f58f-3743-ad8b-667f6285bc62 | -2.87326 | -52.90334 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8abba95-5f24-31e2-b395-07d1f8b00c10 | -2.87268 | -52.9003 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77707dfa-d7a5-3cdc-80a0-e41d867ba036 | -2.87258 | -52.90797 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f81dfa8-8cce-379f-9fa0-7fa2ea06a844 | -2.87197 | -52.90492 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8000d3ff-ccc2-38c8-8038-9023d31def8d | -2.8719 | -52.91259 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 311711c5-3b9a-313d-92f3-da79b681f0a4 | -2.87125 | -52.90953 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a687912-9c42-38f2-a1e8-dbf407435c6d | -2.86873 | -52.90255 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af684a26-d1f7-3965-a492-0f5d763d1394 | -2.86815 | -52.89952 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a88861f-70fe-3db8-bd06-972cc028c86b | -2.86805 | -52.90717 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f249bd55-3e52-3bf6-a9e9-bc28cf939ac0 | -2.86744 | -52.90413 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 733ee5d7-3558-3328-a204-1a3e9c32f6a9 | -2.86737 | -52.91179 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0d450f9-c1da-32c5-90b4-0fd5a642e134 | -2.86672 | -52.90874 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2062907-f5d3-3416-a260-abb6ca00cd41 | -2.86601 | -52.91337 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e2da7d5-bd43-331a-86a5-56c2414f193f | -2.8642 | -52.90175 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b22a7b3-db49-3767-94ac-f7d36b49c057 | -2.86352 | -52.90636 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f46683ad-369d-3f16-8605-0303464acaf2 | -2.86291 | -52.90334 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 114bb885-80a3-30dc-9b15-7e162a339a4c | -2.86284 | -52.91099 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d59ba0f9-0f97-3cee-b0b3-59a8ed917f29 | -2.8622 | -52.90796 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c266f28-4aa4-3f21-b1c2-286b83cb7ded | -2.86148 | -52.91261 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc4f24fd-93a8-3b2e-92f7-26a8400ae7a2 | -3.5438 | -53.1491 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d2bfdc7-2b6f-34bf-a10c-dd4bd9a3e25d | -3.33191 | -53.39278 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96719b8b-ab5e-355d-ac11-ec703181040d | -3.33124 | -53.39709 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d13016fa-f386-337b-a2ca-8f4b6d789ff0 | -3.33073 | -53.3952 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a370739-27ff-32f4-9a65-a50c58422b0f | -3.32749 | -53.39206 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3bf8354-981b-320e-9eda-ad178ba0afdb | -3.32694 | -53.39016 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 26e86a55-d139-30af-8775-ea19dab6d4bb | -3.32683 | -53.39637 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 805f41f0-3c13-331f-94b8-a94d1a424d77 | -3.32631 | -53.39447 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96c2296d-c083-389c-b5e5-56aa35284e0e | -3.32308 | -53.39133 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cd120f2-bfd7-300a-be6e-40a3b7976d28 | -3.04865 | -53.03871 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 196aa90d-47f6-3daa-89f2-4ca3e3ad0731 | -3.03891 | -53.04198 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e14cdb2-4ff5-38de-827f-9282d7b4a46c | -3.03822 | -53.0465 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7d35390-0d9e-3c3d-84f2-5e8581acfe74 | -3.0344 | -53.04127 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4963ac10-840c-36a8-8cf8-821ecd0e12f4 | -3.03371 | -53.04579 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1c2876c-b68d-336a-8861-a0637bef2244 | -2.84353 | -53.31829 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6597e738-bf53-3b4e-be95-3a3ae8a94d83 | -2.84289 | -53.32259 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc7b4a52-598f-3d76-870c-9e317c1a178b | -2.77429 | -53.21135 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ab78ecf-3a2d-33cd-a7d7-dd8037b8380b | -2.76986 | -53.21064 | 2024-10-08 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a732ba7-499b-3666-acd3-0b306b31f16f | -4.04662 | -53.51266 | 2024-10-08 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72e61200-1de0-3717-83cb-d599b1ef6d07 | -3.88083 | -53.71856 | 2024-10-08 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff9cbf13-760a-3c5b-b547-9d9662fccfa0 | -3.88021 | -53.72269 | 2024-10-08 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 393f0db1-c8fb-3292-8f1c-f720782f1f48 | -1.24052 | -54.20688 | 2024-10-08 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0277ad5-1c40-3e42-acbd-7f31cad40038 | -1.23054 | -54.70318 | 2024-10-08 05:21:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 897671a8-873b-345a-b83c-1ed270f9fab7 | -1.19689 | -54.22067 | 2024-10-08 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07635a06-5867-3289-8b6b-e4c07c35a904 | -1.19633 | -54.22427 | 2024-10-08 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5b9919e-c282-3f50-bbb3-19177ffdd9a4 | -1.12709 | -53.63352 | 2024-10-08 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b52802be-d980-3b1e-bfbe-dfa19cb3d1eb | -1.12344 | -53.62931 | 2024-10-08 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9d8d076-34b1-3353-b39a-eb09e8e04cea | -1.09359 | -54.16096 | 2024-10-08 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54b3e47c-d160-3549-ae78-8df5bc4f8a41 | -1.09008 | -54.15675 | 2024-10-08 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60743db0-927e-3ac9-8f66-44d40bdfa5bb | -1.08602 | -54.15613 | 2024-10-08 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48261289-5048-3291-9cdb-602f24c4d133 | -1.08547 | -54.1597 | 2024-10-08 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2c3bbb7-9da5-3a72-9119-670e8517e974 | -1.04223 | -53.54015 | 2024-10-08 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3198970-1219-3df7-ad79-70c321f6d560 | -1.04211 | -53.54051 | 2024-10-08 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37fedb73-976c-33f4-95ff-ca1559e57424 | -1.038 | -53.53951 | 2024-10-08 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6aa6617-f77a-35e9-8ee3-69758f376b39 | -1.03789 | -53.53986 | 2024-10-08 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e678059-e8ed-3a03-ab0b-7dfe2f06ff75 | -1.02988 | -53.73463 | 2024-10-08 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb4f855f-cc89-3f15-80ac-8866dfb033c2 | -1.02695 | -53.7258 | 2024-10-08 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5450f290-d418-3056-ab11-a5abd91ec29b | -1.02634 | -53.72979 | 2024-10-08 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8086a62-9a4c-3059-975e-8c053b54757f | -1.02571 | -53.73397 | 2024-10-08 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78f6e131-ea78-338d-b098-33ec01ae4762 | -1.02271 | -53.72559 | 2024-10-08 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31ef3022-c8d6-3c37-8e76-299b93e09aff | -1.02212 | -53.72952 | 2024-10-08 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef69db08-7db4-341b-85ab-33620865b2ef | -2.69623 | -54.59418 | 2024-10-08 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cd58d95-4f0c-3e44-84cd-135a8b56edf1 | -2.69569 | -54.59768 | 2024-10-08 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 040583e7-46a1-37c5-af16-97d1fa0a9952 | -2.69303 | -54.78575 | 2024-10-08 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77dd5b63-4b88-325a-8ca7-0d2c7b00ebf7 | -2.69095 | -54.78627 | 2024-10-08 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f9038c1-f86c-300c-aa76-b7715be20930 | -2.64153 | -53.96926 | 2024-10-08 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44fc6dcf-2d76-3753-bbec-1aa95ab6cda9 | -2.60287 | -54.55069 | 2024-10-08 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 633ac0e7-dadf-32d9-bdaf-203db63e1a9b | -3.56745 | -54.33716 | 2024-10-08 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f0111f19-dc5a-390d-901a-e74f2d9c6d46 | -3.56689 | -54.3409 | 2024-10-08 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README111.md)
