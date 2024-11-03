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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa234815-4acf-3ef8-b002-e7e24f6eca69 | -2.11916 | -48.90759 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4af014c0-b35f-3896-b9f9-81519ae4f32d | -2.11636 | -48.90355 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e574241c-d8ec-38e1-85b1-7f89c36cb9b5 | -2.11582 | -48.90707 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a6bc726-1ed9-30f1-9a7c-f0db4af39e7a | -2.11224 | -48.99658 | 2024-11-03 04:44:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 256b0b9f-3f86-3caa-9399-468c1247ae61 | -2.07494 | -48.82158 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49be147f-7d19-39ca-b390-f148ecb35569 | -2.0716 | -48.82107 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a072eaa9-d8cb-3ef8-94d9-765590404e61 | -2.06166 | -48.86295 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cb6c80d-a0c9-392b-b068-fcf8f60dfbcd | -1.03773 | -49.32068 | 2024-11-03 04:44:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d86ca74-3c47-3c30-ac5e-c35c081b9a82 | -1.03442 | -49.32018 | 2024-11-03 04:44:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc28ff61-c18e-348d-99c2-52cf49e95cfa | -0.71185 | -49.42831 | 2024-11-03 04:44:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4364ba0c-860f-3f3a-8a88-0b2dd64b26e4 | -2.08683 | -49.73084 | 2024-11-03 04:44:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2e70d02-88cb-3547-b192-2acfedcbdc46 | -2.08139 | -49.74407 | 2024-11-03 04:44:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 045a0e2b-2322-3c0e-bf38-d1e4dd00af9c | -2.07809 | -49.74356 | 2024-11-03 04:44:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d9fd04b-2f2a-3a5f-9920-77403847a2f3 | -2.04046 | -49.699 | 2024-11-03 04:44:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9220217f-85d2-3d2e-9804-5ff03791eebd | 2.35957 | -50.75733 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 692423e5-0927-39eb-b525-5a050d7f00d3 | 2.2006 | -50.86742 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0569e19-4c10-3338-80f0-555b14955f46 | 1.84463 | -50.52415 | 2024-11-03 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98bc43a1-cd73-3a1c-b30e-1cc8dfb4ab9c | 1.84407 | -50.52061 | 2024-11-03 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6cb8a219-88be-35c4-8100-f4115c416329 | 1.84352 | -50.51706 | 2024-11-03 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 88b418db-708b-3a1a-950f-e84c3c0b0f7f | 1.7901 | -50.43822 | 2024-11-03 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1737792c-d51b-3f88-a15a-3b83b9d1c0a8 | 1.78955 | -50.43468 | 2024-11-03 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5845be5d-ff37-31f1-86d7-5c2a6a8d17f2 | 1.78675 | -50.43873 | 2024-11-03 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24ba9ad9-6282-3a5d-8fb9-07d680fa994a | 1.7862 | -50.43519 | 2024-11-03 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5a08511-c0db-31b3-9735-2eaa0ebff419 | 1.78286 | -50.4357 | 2024-11-03 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3f49e10-58e9-3dd7-ae69-281026b3736e | 1.4302 | -50.99148 | 2024-11-03 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98522d66-1f80-3c1a-8389-f7dff40b2434 | 1.25666 | -51.14118 | 2024-11-03 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a1ed2d8-bd76-3494-a07e-2296b52b4d26 | 0.88956 | -50.6605 | 2024-11-03 04:44:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fe88853-142b-3b4a-ab6b-a2ff2c0f542e | 0.88621 | -50.66101 | 2024-11-03 04:44:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d0a430f-9a14-399d-ae04-59bd3cac7e73 | 0.87365 | -50.86671 | 2024-11-03 04:44:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7c59d24-f7dc-3683-9f97-0d3ca26d90dd | 0.86484 | -50.76588 | 2024-11-03 04:44:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e22998d0-ec87-3c6c-9287-cf123a9868b2 | 0.84323 | -50.21198 | 2024-11-03 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc7a6e18-7385-3d5f-9c9d-35baf144e928 | 0.45131 | -50.27353 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58e9f433-dc6f-348b-85b4-7b44bc5d66a5 | 0.01263 | -51.36061 | 2024-11-03 04:44:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86c41eb1-18cd-3464-aeda-450440fce156 | -0.62715 | -50.44856 | 2024-11-03 04:44:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a46d5952-5515-321c-a0e5-265b23df8b23 | -0.24126 | -50.9617 | 2024-11-03 04:44:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0d3a88a-6151-3494-9d56-bca7a42581b6 | -0.15081 | -51.29987 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e159a70c-0c43-3cc9-8dcf-77ba4b435eef | -0.03105 | -50.75911 | 2024-11-03 04:44:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9daa46e-f556-3da0-8242-0c502cf1722e | -1.8124 | -51.02908 | 2024-11-03 04:44:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d19b208e-9bcc-3379-a240-0f4baf3151e8 | -1.81185 | -51.03258 | 2024-11-03 04:44:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8a6a36b-1284-398a-9fec-ca0e53968aba | -1.76862 | -51.11212 | 2024-11-03 04:44:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58358636-3575-35f9-ad28-e85eeba452db | -1.71971 | -51.18763 | 2024-11-03 04:44:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae3e2ded-4e4b-3412-baf8-b39feadd9cfd | -1.62414 | -50.53736 | 2024-11-03 04:44:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf45f993-525d-3ee2-bbff-d1ae4b39d60f | -1.57977 | -50.4493 | 2024-11-03 04:44:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1eea3a2-a347-3053-9efd-507cadfa29a2 | -1.56347 | -51.27178 | 2024-11-03 04:44:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cf7f113-ea80-3c50-879a-2cb998977183 | -1.52004 | -51.18175 | 2024-11-03 04:44:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c89c0ca-0ee6-3049-aeec-3e906d38b761 | -1.50849 | -51.53439 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca00e682-038a-345a-8f8b-cc08f4ecd77f | -1.50625 | -51.52666 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d2d0b78-8058-3059-8ec2-49d036f2ea2f | -1.47128 | -51.55085 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17b9276e-badd-356b-970e-daf32422b809 | -1.4629 | -51.50541 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55f81665-2d8f-3152-bf1f-20768c87e149 | -1.40541 | -51.58538 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d98d9354-08c2-3138-aead-197a29356b22 | -1.39215 | -50.58205 | 2024-11-03 04:44:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1241423-2480-34c3-9fdd-a3eacb4d2960 | -1.38962 | -51.57553 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb226c20-bac0-3aed-9e90-669aa80a2e3b | -1.37633 | -51.41849 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4101c1a-a306-30c1-b9e1-32637400eb71 | -1.37576 | -51.42208 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 567f30cc-8318-3aae-8fef-0760223d0aba | -1.37519 | -51.42567 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d38046ec-95ea-33da-bb0b-0c03fcedc56d | -1.37463 | -51.42926 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 618d2eda-c6d5-318c-aed0-edac683d4e62 | -1.37456 | -51.41819 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62629cbf-8e2e-3443-8661-f20a4e43f5d1 | -1.374 | -51.42178 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 072adc87-55e1-3717-8a9e-30e116f9712f | -1.37344 | -51.42537 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3f0bd65-4410-3d2b-9624-c7dbd2be9c2d | -1.36556 | -51.40947 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef44a71b-d78c-3011-b57f-0aa9540b29a9 | -1.365 | -51.41305 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b591efea-774d-35eb-a4e6-a143d3337aa6 | -1.36163 | -51.41253 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 269c3abf-fa49-3b76-a255-eabdebcf6169 | -1.35826 | -51.41201 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efe170f1-764e-3f6b-88a0-1a9da0d09cf7 | -1.3577 | -51.4156 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 995e607a-e03f-3084-b0f9-a9c89743ffee | -1.35433 | -51.41508 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af9cd976-1c3d-3aef-96d3-4249f70456b9 | -1.3504 | -51.41816 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bb56bb9-ef2d-33f7-9c5e-e71b26466bed | -1.34984 | -51.42175 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f759c0ae-ff2e-3183-9ae9-acb178874594 | 2.33584 | -51.64704 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ca09633-5b69-377b-af41-5b4c366cbf0c | 3.54653 | -51.43115 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d7efdaf-5d18-3a66-87ed-278bedd1d0a4 | 3.53572 | -51.28939 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0636a9d-8035-3be4-8b5a-8c8e82d357d6 | 3.53513 | -51.28552 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b0adf1d-89b4-3fa3-b728-68cd28b00364 | 3.53164 | -51.28604 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27f70680-1758-326b-91fe-bdba2c4bfb3e | 3.52173 | -51.26778 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37f1acc5-075d-3eea-8db3-9aceedb43f25 | 3.51825 | -51.26831 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e268c05-7d6e-380a-b18f-b7c1a805545b | 3.51535 | -51.27269 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26a571d5-612f-39c8-93fd-251a15de0074 | 3.51477 | -51.26883 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2258401-62b9-3c75-94cf-c379deaeca78 | 3.51245 | -51.27707 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69a468f7-417c-3079-811c-dd78e52359db | 3.51187 | -51.27321 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e740dda9-b671-3e9a-a424-8672a412cab2 | 3.2274 | -51.22069 | 2024-11-03 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d134341-b04e-3a8d-b3e4-b02d35534153 | 2.55668 | -51.10405 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1ed4b0c2-8e6c-3c72-91f4-eb450f496434 | 2.55325 | -51.10457 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 86f925f3-00ae-34c9-a1af-2467c287f5b7 | 2.55267 | -51.10085 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9cc7226-dfa3-3bab-954a-c36682a6824a | 2.54924 | -51.10137 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fe409a1-36a3-344d-bf82-e6b33976c12c | 2.54866 | -51.09764 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b95ed8e-d5aa-3d4a-b947-9f40b9e6801c | 2.54523 | -51.09816 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b48e4298-93d3-31c6-9497-2fcd90d29b93 | 2.5418 | -51.09868 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f382996-b1fb-39b5-b0be-9b213de096c7 | 2.54123 | -51.09494 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6389637d-25fb-3e59-b026-3178896cb5dd | 2.5378 | -51.09546 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e378bd46-f99a-3021-b187-7e3db19b263c | 2.53379 | -51.09225 | 2024-11-03 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5775471c-8391-3790-aeb3-2ecba6b391ea | 1.07271 | -52.54305 | 2024-11-03 04:44:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9e6db4d-b9e1-319e-a0f2-77381599d961 | 1.01092 | -52.21922 | 2024-11-03 04:44:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db15133a-d268-39e2-9759-da47f482afe2 | -0.11665 | -51.56408 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd14057e-58c5-3c0f-8166-c83649a7ec91 | -0.11608 | -51.56777 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eb01af5-9d7c-3f02-b86c-d0a87e56f915 | -0.09837 | -51.59157 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d3cc84f-f40f-346e-aba2-483f7553eca8 | -0.09496 | -51.59104 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fb580a8-64ed-36cb-ac08-4330499d56a4 | 0.54443 | -51.68549 | 2024-11-03 04:44:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 393e291b-30e5-3989-85b5-6259ee2679cd | -0.75703 | -51.9584 | 2024-11-03 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 74af96d4-0050-389c-b390-0649de06e243 | -0.74073 | -51.70435 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c290c421-9eff-3cd3-9a00-84556d7bcfa9 | -0.74016 | -51.70803 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a9f5458-bf43-325a-b262-73b43e679379 | -0.7038 | -51.67225 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README32.md)
