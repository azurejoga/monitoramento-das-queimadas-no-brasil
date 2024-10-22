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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e86c0e4a-f5e8-3ca6-894d-861e47e67931 | -2.1327 | -46.726501 | 2024-10-22 00:18:04 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 379017e6-328b-399c-a295-ca5e5c11a8d8 | -2.7061 | -49.292 | 2024-10-22 00:18:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e08c7f14-9ae9-304f-a45a-53d052e4dd19 | -2.7082 | -49.301601 | 2024-10-22 00:18:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba424eab-a9fe-3df7-a55e-ad98e3166fed | -2.7104 | -49.311298 | 2024-10-22 00:18:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30eb829b-a528-3b56-b10f-775711ae5721 | -2.6963 | -49.294201 | 2024-10-22 00:18:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db8347d7-5849-3f86-89e9-404752699ae4 | -2.6984 | -49.303799 | 2024-10-22 00:18:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9f7365f-b4e2-38c5-9d82-c96394056277 | -2.7006 | -49.3134 | 2024-10-22 00:18:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffbb97ee-a058-3133-93fb-563ddc1f28fd | -2.707 | -49.3424 | 2024-10-22 00:18:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c27ef061-f0b1-315b-9b80-858434d6aa0f | -2.7092 | -49.3521 | 2024-10-22 00:18:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a44bd4ef-26ae-34fb-a664-bafd67766f4d | -2.9056 | -50.514999 | 2024-10-22 00:18:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00b36ed8-f610-31bc-aa6e-29cd4b5b2998 | -3.0231 | -51.232101 | 2024-10-22 00:18:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6facb85a-fc6b-3930-85ba-42317ace3e32 | -3.026 | -51.244999 | 2024-10-22 00:18:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ef4c95d-d112-367e-9094-f5035765f1da | -3.0288 | -51.257999 | 2024-10-22 00:18:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b9499e1-3cdc-340f-8a91-a98bec708b6f | -3.0133 | -51.2342 | 2024-10-22 00:18:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82994574-ee9e-3756-8567-144193c81514 | -3.0162 | -51.247101 | 2024-10-22 00:18:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a7f3f5-4955-318f-83a1-f24b719bad57 | -2.151 | -47.5425 | 2024-10-22 00:18:06 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b97425bc-3af0-3c13-a2c4-0ba908a371cb | -2.2221 | -47.905899 | 2024-10-22 00:18:07 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c97b7c8b-2ef5-332f-8c76-e3f6ffd5f83a | -2.4283 | -49.1049 | 2024-10-22 00:18:08 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 404e5af0-d42d-3601-8b82-c68ed9a52ca6 | -2.4185 | -49.106998 | 2024-10-22 00:18:08 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd533921-da36-3564-84dd-adb2f5940e28 | -1.8057 | -47.1045 | 2024-10-22 00:18:10 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a921896-7ae4-3ef2-b9ac-fc866d20116b | -1.8074 | -47.1119 | 2024-10-22 00:18:10 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c716e07d-b746-3e32-898d-e0ae671b6532 | -3.0447 | -53.0919 | 2024-10-22 00:18:12 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01f77f94-87ef-3323-9b06-fac99478c6cc | -1.6044 | -47.033401 | 2024-10-22 00:18:13 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf0dbf14-3686-3463-bfb9-a99b41fe3e1c | -1.9201 | -48.670399 | 2024-10-22 00:18:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 671ffbbb-f80b-3041-a066-d8234395c5a3 | -1.9221 | -48.6791 | 2024-10-22 00:18:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27f1190e-b8d3-31ad-9bf7-8157a258a5e7 | -1.924 | -48.687801 | 2024-10-22 00:18:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c48de027-4a98-30d9-aedf-d02c3581cd3e | -3.0469 | -54.1217 | 2024-10-22 00:18:16 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66fde0a5-cbc7-3357-8a5c-e90e31ed3647 | -3.0327 | -54.103298 | 2024-10-22 00:18:16 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcde8e16-4121-31f6-85da-a494f8281cc0 | -3.0372 | -54.123798 | 2024-10-22 00:18:16 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd23420e-a745-3406-8480-96601756d23c | -3.0417 | -54.144402 | 2024-10-22 00:18:16 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ad7a31c-e41e-3654-95ae-d4a4e2174821 | -3.0275 | -54.1259 | 2024-10-22 00:18:16 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a82d9ba-943e-336f-b5c2-32a024463830 | -1.5038 | -47.318901 | 2024-10-22 00:18:16 | METOP-B | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52c31c25-501a-35c4-a73f-9a1f09e28bff | -1.5055 | -47.326401 | 2024-10-22 00:18:16 | METOP-B | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 151830a8-d298-3750-8f5b-526c67f74735 | -1.4758 | -47.285999 | 2024-10-22 00:18:16 | METOP-B | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03fe7bda-f213-3f7d-b5ae-c99897c3cbb3 | -1.4775 | -47.2934 | 2024-10-22 00:18:16 | METOP-B | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 484d4fff-0890-3cc0-92df-c185ec6e6aad | -2.1635 | -50.450199 | 2024-10-22 00:18:17 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95e87668-5e19-3e6c-b7cc-eee13dd938cf | -1.4195 | -47.7682 | 2024-10-22 00:18:19 | METOP-B | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbdf1b5b-2aff-3468-acb7-99bb6057244e | -1.4212 | -47.776001 | 2024-10-22 00:18:19 | METOP-B | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e80b491c-c0e1-3419-8069-67436b28bac9 | -1.423 | -47.783798 | 2024-10-22 00:18:19 | METOP-B | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08d98709-4bb8-3a00-8f67-35996a43bd8b | -1.0635 | -46.826698 | 2024-10-22 00:18:21 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae497b9-9df8-343f-a108-53e1514dfcd6 | -1.0651 | -46.833801 | 2024-10-22 00:18:21 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21c41a9a-f9c6-314a-b6ae-c1600973b5a5 | -1.0537 | -46.8288 | 2024-10-22 00:18:22 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13f50a4d-4cba-3aaf-b8cd-01b9f80b3e87 | -1.0553 | -46.835899 | 2024-10-22 00:18:22 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a9135eb-8519-3052-b153-3f44866c04f4 | -0.9876 | -47.495499 | 2024-10-22 00:18:25 | METOP-B | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58e8faf8-fb61-32d5-b071-d61158d7e2ec | -1.1132 | -53.621201 | 2024-10-22 00:18:45 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6092d01-a3c6-33e9-9128-327437def59c | -1.1172 | -53.638901 | 2024-10-22 00:18:45 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b4a10d3-72f9-385a-8278-f793496f717a | 1.8967 | -50.481899 | 2024-10-22 00:19:23 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9875c9aa-2c63-385c-9c2d-081b0cf3138a | 1.8944 | -50.491699 | 2024-10-22 00:19:23 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6d93008f-6948-3e78-a650-b8e2968e3dca | -1.165 | -53.6571 | 2024-10-22 00:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 2a7453aa-759b-3f90-815a-128f5e0251f7 | -1.1834 | -53.6569 | 2024-10-22 00:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| dbbc1ba7-04ae-398f-a30a-9bc76d015d14 | -1.9849 | -48.6865 | 2024-10-22 00:25:17 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 0483eb24-037d-3225-be0a-83178e4d005a | -2.7403 | -49.329 | 2024-10-22 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 4ba6f2ac-c6ec-3565-bf42-c7143457b5c5 | -2.7404 | -49.3077 | 2024-10-22 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| a8a2fb47-7400-3ca5-b3bc-7c062025f1a6 | -2.7588 | -49.3285 | 2024-10-22 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 23ce1ddc-f08e-3540-8be2-8c3e680fc922 | -2.7589 | -49.3072 | 2024-10-22 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 231.3 |
| 59b46c84-023b-3fab-be93-8647f2fe4f6c | -2.7773 | -49.3279 | 2024-10-22 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| a21e7e67-6d76-36f7-bd28-61d334821a2a | -2.7773 | -49.3067 | 2024-10-22 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 460952a8-2bef-3775-9265-d05676495885 | -2.7867 | -58.1492 | 2024-10-22 00:25:22 | GOES-16 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ee24a281-0137-367a-8f9c-a2ede414bcbe | -2.8482 | -45.4637 | 2024-10-22 00:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 31b39f54-2617-3be9-a72f-edc3c8663302 | -2.8668 | -45.4631 | 2024-10-22 00:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f3656c5f-f710-3840-940e-ff82a6492866 | -3.0581 | -53.2395 | 2024-10-22 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 67b0e20d-ab5c-3c69-b73a-67afa4756a8f | -3.0654 | -51.2506 | 2024-10-22 00:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0744712b-e7e1-3da9-be07-a16944959e55 | -3.0765 | -53.2593 | 2024-10-22 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4a35a9ee-9754-3511-9538-052924c3c3ce | -3.0765 | -53.239 | 2024-10-22 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9fce4283-5754-3e49-8b86-069f003df265 | -3.0837 | -51.2708 | 2024-10-22 00:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 13ac8b23-c65e-31a8-8449-cca01a814ac9 | -3.0838 | -51.25 | 2024-10-22 00:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 77047f5b-6a35-3c2d-a60b-11c95f5011e0 | -3.0917 | -54.1867 | 2024-10-22 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 621c26eb-db94-3028-8766-ec468d005446 | -3.0917 | -54.1666 | 2024-10-22 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 150.2 |
| 27c0bc6b-2706-385b-9144-8d1940df8539 | -3.0918 | -54.1465 | 2024-10-22 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 2b2dca60-5057-3a87-9c3c-4158dadb3c09 | -3.11 | -54.1862 | 2024-10-22 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| bebfcde4-6845-3eae-bd93-934b85e7c788 | -3.1101 | -54.1661 | 2024-10-22 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 67037f56-c63a-3cab-b426-844b50f65b17 | -3.1102 | -54.146 | 2024-10-22 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 7d149366-42a0-3e6c-a049-ecf5286086e2 | -3.9975 | -46.0425 | 2024-10-22 00:25:29 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8b7c6d50-d175-3cda-bf55-0ff5a3909985 | -3.9977 | -46.0202 | 2024-10-22 00:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 1b2c3898-e674-3fa0-913d-5538eba33adb | -4.0161 | -46.0416 | 2024-10-22 00:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 94fa4fd0-0bfb-3aaf-8760-f3b0a79e6234 | -4.0163 | -46.0193 | 2024-10-22 00:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 45a13e56-11d5-33b0-8191-bd6eff7d0681 | -4.4655 | -42.9112 | 2024-10-22 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5186948b-f95a-381a-9861-fd271f153791 | -4.4657 | -42.8877 | 2024-10-22 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 35de5618-d652-3680-ba82-23cd431d0916 | -4.6191 | -42.3835 | 2024-10-22 00:25:32 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 06b3f9b6-0fa7-37d3-9060-10ce470c732d | -4.5572 | -45.8128 | 2024-10-22 00:25:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| f266484b-e252-3765-b0fc-e86549ab176c | -4.5574 | -45.7905 | 2024-10-22 00:25:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0146c605-9db2-3adb-8612-004aafd1cfed | -4.9513 | -45.4309 | 2024-10-22 00:25:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 04ee294b-7947-3d17-a518-bef16d19d06d | -4.9514 | -45.4084 | 2024-10-22 00:25:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| bdf35156-34c7-3941-8993-304919c2ef48 | -5.1514 | -46.0911 | 2024-10-22 00:25:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c7a89eac-9cea-32a1-8972-68f254d1d091 | -5.2305 | -43.1886 | 2024-10-22 00:25:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4c4cac82-5b4b-333b-bd54-0511cdbb961e | -5.5905 | -44.8687 | 2024-10-22 00:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| dc994506-580c-3f6f-a651-eea5442895a0 | -5.9036 | -45.4127 | 2024-10-22 00:25:39 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| c140a99f-7cf9-369b-97b6-b4e834cdc3c3 | -6.2334 | -44.1565 | 2024-10-22 00:25:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1ddc0ab4-57ad-3044-a8a2-7d6ab6240669 | -6.2336 | -44.1335 | 2024-10-22 00:25:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ccf54adf-4f26-3c99-90f0-28fbcd027105 | -6.2522 | -44.155 | 2024-10-22 00:25:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 152c71e4-c2f2-3b6d-aaf6-b21ac1042534 | -6.2524 | -44.132 | 2024-10-22 00:25:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 4a762ec6-5f42-31b0-b475-6278756d24fa | -7.8245 | -61.3709 | 2024-10-22 00:25:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 5ed595b0-3d5f-3820-b6b0-0293d45786a9 | -12.5147 | -63.3014 | 2024-10-22 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 50bded58-f5a2-364e-b1e8-7cfff98c05c5 | -12.5167 | -63.0521 | 2024-10-22 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 36e91f48-6a04-3601-937b-7f94d00c9901 | -12.5168 | -63.0329 | 2024-10-22 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| add927d3-ae50-3b21-9505-ae2cbf351424 | -12.5335 | -63.3195 | 2024-10-22 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 35b083bd-ffa4-3ab5-956d-d65afdd0b3ca | -12.5336 | -63.3003 | 2024-10-22 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 12d274ac-fa77-3a5a-aa24-7fb05c7f06fe | -12.5356 | -63.051 | 2024-10-22 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 118.4 |
| fc45f61c-0d87-3d6a-b5a8-15a3f1be82f2 | -12.5357 | -63.0319 | 2024-10-22 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a13a37a6-6270-36c4-9e06-a45166a0665c | -14.3029 | -59.3399 | 2024-10-22 00:26:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 218.6 |


[Clique aqui para ver as próximas entradas](README6.md)
