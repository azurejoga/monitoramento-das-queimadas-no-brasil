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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ac126eb-29ba-3c91-94c3-a7b336e16ff0 | 0.41327 | -50.81496 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09e55dce-574e-301a-80ae-9ff5a9973528 | -1.62007 | -52.47654 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2827f09-fa6e-3415-9dcd-dea29d7e6809 | -3.59297 | -43.63723 | 2024-11-21 04:53:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a25b3426-4214-397e-853d-99cf1e255bd4 | -1.22393 | -51.79707 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29d12aca-d2c5-30cc-afdf-a1e35f9f086d | -1.76822 | -52.70123 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 199b6273-564c-3f8d-ac46-60d33691b734 | -1.50174 | -51.97355 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3557be8c-4efe-3e8f-871d-579b4c52c3bf | -2.24805 | -49.20295 | 2024-11-21 04:53:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2bafeb2-4ae3-3326-92c9-c7660ff9c290 | -1.17686 | -51.94471 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff41a6e3-c65d-32ee-ad46-ef06d8cc2cb7 | -1.26719 | -52.12686 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b7e24dd-f4a2-33f5-97d8-8d2c331600e7 | -0.78996 | -51.76994 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbd69738-1459-321c-9ded-6e1ea7bf343e | -2.09004 | -46.32628 | 2024-11-21 04:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e1f1245-98cf-3217-8995-30e3ac47151e | -0.27452 | -51.393 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db808418-affc-3de0-8399-3852f2525c8b | -2.90137 | -48.32066 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f3896b2-59f6-3ee5-a380-b2fc3ddcc30a | -2.14475 | -50.49122 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 311eab36-c6b0-33c8-aea0-28ce9e66d341 | -2.84636 | -48.67261 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e32289b0-2030-37f8-bb1e-f1559a6e7f35 | -2.19877 | -53.65914 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| dfda1798-407f-39a9-9caa-53a80d3d9d62 | -2.27023 | -49.08285 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e69993fa-18ac-3475-a57b-be6ad3cc790e | -1.06979 | -53.3619 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a518fee-c3fd-33c6-b1e5-b27df02a4c88 | -2.20938 | -53.7208 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a645e0b-3f60-35e2-a837-5a70c65292fb | -2.90596 | -48.31776 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4907db3c-3564-3fad-9b96-0e7ba9470748 | -1.78453 | -53.485 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3494365d-37b9-375e-9ffb-ba24b3adafa9 | -2.92869 | -48.33558 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75b56fb0-2fbe-35dd-9785-02c6036b8b70 | -1.51334 | -52.2259 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d535e897-f1e6-3f22-ace3-e74e8fb23d92 | -1.39132 | -46.50752 | 2024-11-21 04:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45c3b0ee-842e-3ffa-8d83-a01c1ea1d88a | -1.72076 | -53.26355 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c306b59a-1628-3fd7-bc31-caf4d0c43d36 | -1.19935 | -51.7788 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e11c391-22fb-3aaa-8ea7-d8eadbc31f26 | -2.73699 | -47.54162 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 338d6dd9-edd1-36b0-8700-713bad4adf4a | -1.51751 | -52.37264 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e64e7fb2-0491-33a9-8ad1-46a49c3c6bed | -1.28863 | -52.46778 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45da96bc-1f38-3ab4-9e0b-059e88fd73a2 | -1.63324 | -52.63055 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1902e0d2-a9cc-3868-9736-a528df28ec84 | -1.52058 | -51.15627 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01d6842a-03d6-34e5-9402-4a8d76407858 | -2.16818 | -50.61966 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b4edb13-4aae-339d-935f-1071526c9431 | -1.56083 | -51.23404 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1371b9b7-1435-3ff9-987b-97da8cce6a47 | -1.23228 | -51.78751 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f89f8427-4cc9-3dbb-a89d-d68555a2a920 | -2.63025 | -48.48655 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b766db02-3c57-3687-89c4-cbb89db9055b | -1.29351 | -52.26266 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1f20b97-6b4c-3bc3-9479-b5e5a913c768 | -0.00712 | -51.77821 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 382a7da6-6165-33e6-88a8-5ad24ce030ef | -0.79275 | -51.77398 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22e5b747-3de7-3777-8853-92e3bb1075e1 | -2.83546 | -49.54033 | 2024-11-21 04:53:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82a9f712-0632-3028-a74b-7dbf2e4d43af | -2.26671 | -48.41969 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14892165-7059-34e7-a8b0-0832146fb3c6 | -0.81177 | -52.49543 | 2024-11-21 04:53:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4266c3a-9e64-3e27-b81b-2c842c524b01 | -0.9803 | -51.72368 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94ea6006-e07a-3a17-8a1f-2ed7daee2221 | -0.80628 | -53.05018 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce4e6af0-74d7-31cf-96e8-1dce025aa0df | -2.00802 | -54.52356 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a2dcbadb-fdcc-3bbd-bbd6-11502fdd19dc | -1.22274 | -51.73895 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c1972aae-7490-317f-9f16-bf88eb4e2082 | -1.61224 | -52.61317 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab69380e-728d-3e5a-a8a6-d040c503765c | -1.78151 | -53.61149 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d94d45f5-d808-32f4-933d-8b3cd740deb9 | -1.23922 | -53.364 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b3cf605-e427-30a3-832b-746203d4551c | -0.8987 | -51.72531 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b138080f-3b0a-38e7-9189-b161f5313d3a | -1.24844 | -51.75017 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1fcb35f-6efb-371d-b273-df397f8e7b70 | 0.75952 | -50.24714 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de62e237-f5df-332f-b411-c93a425558fe | -1.4862 | -51.12838 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfc94032-d518-3b1b-88fd-2e1a613eefdc | -1.96385 | -48.3833 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dee5b31-4597-33d8-8e7e-a73d6a0fb373 | -1.48503 | -51.13577 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04f0bd9b-63ce-3d81-b3eb-0502f24f91b9 | -1.3182 | -55.45377 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34cd65d2-ec2b-3525-9218-88041d604fd9 | -2.36013 | -49.07483 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26a8aef9-769c-30d3-9927-13f78e930287 | -2.27864 | -50.81488 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ab4247a-0ba9-391c-a0f0-6def44f2b01f | -1.48095 | -51.16157 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b4f0c13-ef97-30f1-a82b-716747c00798 | -1.78537 | -53.60856 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab98ec0f-a15a-3830-ba15-33c42bf86b6d | -1.56378 | -51.19311 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2bfa667-9d51-3854-903e-18f245481a8a | -0.94389 | -51.72144 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a20c316-af76-33a3-a330-4227304909bd | -1.46138 | -51.99613 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddc3229c-5b43-3340-8b5e-eeb1bcc4bf3f | -1.33452 | -51.40089 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57d7828c-7cf0-3986-bcb8-e37829e2eb8b | -2.55879 | -47.29117 | 2024-11-21 04:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c6782b2-9012-34ef-ad46-96fcbae15acc | -1.15793 | -53.66544 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44fb784d-7db0-3982-8eb1-2aef569ee534 | -1.79061 | -47.1952 | 2024-11-21 04:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b275e3b3-43e2-36da-b4b7-8ae07dd0f72b | -2.13385 | -49.80318 | 2024-11-21 04:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e467f793-ac37-3dbf-8c12-65e152c43d42 | -1.60272 | -52.4142 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d8fcaeb-4d78-32a5-8d48-4f5e295706b3 | -1.13294 | -53.60855 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e80a0d42-427c-3a65-94a7-1d74e86d20d2 | -1.20546 | -51.76164 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29ea7c20-1c17-3a3a-89f8-6c0dacdd4dba | -1.60235 | -52.24358 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b6a3cc9-6e3f-3cc5-a223-276022fa4848 | -1.22838 | -51.79052 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cd16563-a7bb-3abb-a127-effec10b6c70 | -1.46685 | -51.11784 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c79cd18c-2650-3265-9188-554c0b2bad6d | -1.06169 | -52.39699 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0707718f-944e-3e4c-95ef-7b2ab1c74e72 | -2.55449 | -47.29049 | 2024-11-21 04:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8cdd225-2f27-3303-8c0a-48b65a1b0c02 | -0.97136 | -51.71506 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 788b441f-8d9a-3e61-a6c6-faf78f3a02f6 | 1.01914 | -52.27634 | 2024-11-21 04:53:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20ed6c10-7e35-39c4-a4fa-6c16974e5adf | -1.19661 | -53.67858 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39678e3c-5310-3ac7-9fff-c3894898bad1 | -0.86271 | -51.8459 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d886e57-9e0a-3a2a-8b6e-8fd8ecde996a | -1.72968 | -52.70935 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e5a97e5-7cdc-317f-bc39-5f9c4ff18b03 | -1.04617 | -51.7411 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98dff97e-7756-36da-9f0c-73f81fda59a8 | -2.53471 | -45.4365 | 2024-11-21 04:53:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6267d80d-d1c6-3d84-be68-4d9556130219 | -1.61878 | -52.41965 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0f4f675-0804-3f97-a93f-42b5754aa0da | -2.63517 | -46.22604 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bab59166-1e48-32e6-9162-8f38f7c9f06b | -2.66082 | -48.48765 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0e5c2ef-93ac-3823-9857-410a9068afc3 | -2.32848 | -45.66584 | 2024-11-21 04:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e921792-4d2c-38dd-a79d-28361792832d | -1.60881 | -52.41868 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1f7ebff-1b41-3503-85d0-1fb65e891f4d | -0.77659 | -51.76787 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5eb0b03d-6172-3ece-b59d-987a32ce6486 | -0.96063 | -51.72403 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 978367e0-e2fe-35db-84d7-280b0c85e142 | -0.92486 | -51.64602 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 683b83a5-d410-37f7-86a1-f10569b802a3 | -3.12286 | -45.44883 | 2024-11-21 04:53:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d2bd599-a022-330c-9486-333a7657da5d | -1.11441 | -53.18597 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cca4c50-7043-3400-acae-0efe1ae0c50f | -1.2911 | -51.36826 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16cbcf29-b242-3282-9374-8f659d767d5b | -0.22112 | -51.19467 | 2024-11-21 04:53:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 990e635c-6e4c-3e9a-a833-12266129aeea | -1.46418 | -52.68904 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19565df8-b640-30f8-bcb2-d08b01f12412 | -1.14027 | -53.66977 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 634744e6-11ff-318c-add1-e2608c9fbbe4 | -1.13934 | -51.68651 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87635f16-9638-3bb0-9ef9-526259ea528e | -2.35505 | -48.96523 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75b29671-d9b5-3dab-8f7e-693417f8f0c0 | -2.94013 | -48.07236 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d38954c9-3255-35e1-ba68-3cedc082f62d | -1.1999 | -51.77526 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README57.md)
