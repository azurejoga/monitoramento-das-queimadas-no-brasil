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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d81a9a2-ec45-3cbe-90bc-cf996c7e211b | -2.88409 | -51.42813 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e69a569-a62f-35bf-83d0-1c237c0098f4 | -1.85074 | -56.37201 | 2025-11-16 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2293efe-5d2a-39fb-95d6-8df8b341cdac | -3.1355 | -50.29046 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e5f09ad-40c6-3653-a44a-a675abca6974 | -5.99215 | -41.91409 | 2025-11-16 04:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8bb4e593-76c5-36ae-92d6-0225c69be868 | -4.84298 | -47.55528 | 2025-11-16 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb79c295-119f-396a-91c3-fcf369285e83 | -3.06208 | -52.32106 | 2025-11-16 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1d91a09-38a1-33a3-9d91-00478c533d3e | -3.39991 | -50.18711 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a41f3167-1903-3700-882d-865361ec2421 | -3.40879 | -52.19066 | 2025-11-16 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f710b70f-f3ea-356c-b4e6-8f0dafd97feb | -2.86652 | -51.47432 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97919e65-4098-3604-b7ac-78c04cd1e8ac | -3.4368 | -50.11549 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fe9b047-8f14-3839-b255-139bda4c2985 | -4.11049 | -50.73082 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44db0c20-430a-3004-a406-50753a76ca10 | -4.4147 | -43.40284 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f26cf5d-7f53-3fb7-9c1c-7aed35b66ed6 | -4.42503 | -43.41257 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d41b7625-e7ab-3513-8f90-f1c559c4af22 | -4.68947 | -46.52693 | 2025-11-16 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fef3211-fb30-3cf6-b136-4e11cf3c3d77 | -3.58546 | -50.41998 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf7d2ca4-0692-37ba-a70b-aec2366e500b | -3.13191 | -50.28991 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a15d7f6f-a288-318f-96ac-b35ab15978df | -4.24813 | -50.05221 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5c908d44-67db-3b45-9e9f-55e6beaca4d7 | -3.36179 | -50.18639 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 143b08ab-62b4-3055-8846-86a7a3bb0669 | -3.33187 | -45.8548 | 2025-11-16 04:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d976ef48-6879-38df-b9ca-1a8493e9f72d | -3.08711 | -51.54491 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40403aa5-5a22-306f-af21-54e9b051c08c | -2.88824 | -53.28485 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2af543ae-c072-3643-a6ee-d82a40300b03 | -5.96332 | -43.74948 | 2025-11-16 04:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0a6b26f-0f03-3105-a823-eedb07983a66 | -2.31871 | -57.01117 | 2025-11-16 04:55:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eddbf2f2-b3c9-3ae5-a024-4a8a753af5f7 | -3.09214 | -49.50398 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 569e1dd2-0c42-35cf-93e7-58359d046421 | -4.69831 | -46.31936 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c30d65a4-1748-3b23-a806-8855f4a65e74 | 1.67237 | -50.9014 | 2025-11-16 04:55:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e50b0ac-e05a-3595-b2e7-eb6657fef0be | -1.64739 | -53.66683 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf6024bf-b243-3452-a04c-de5c3f34036e | -3.02489 | -51.60313 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38de02d7-9246-3dee-aef5-dffdbb086c61 | -2.6939 | -49.85573 | 2025-11-16 04:55:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c19a4fb5-3c2d-3d5f-9740-0accc1430dc6 | -3.38943 | -50.13389 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4c8bdf23-9ca7-3258-a972-65c2eeffacd1 | -3.39331 | -50.18183 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9892ad2b-bfae-36d1-8f73-72e0d7b16f72 | -2.5759 | -51.85875 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b4e1301-fa24-347f-b4bd-0ec5e804f23f | -1.75507 | -54.80321 | 2025-11-16 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9df6adf2-5907-3899-aebc-7fe82f3f68bc | -4.27864 | -49.67938 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bebc834f-ea08-3d8b-a98d-73bb2fcfcd93 | -4.21347 | -49.1326 | 2025-11-16 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a02533a7-4f17-3328-8ad3-355275ef674b | -3.22242 | -52.60292 | 2025-11-16 04:55:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2488d224-c54e-3c27-81bd-89908d0e30d3 | -3.03523 | -54.59744 | 2025-11-16 04:55:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15919587-ebd4-3e48-b55f-864ae216c458 | 2.34119 | -51.64747 | 2025-11-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 702ff46d-cdbc-3f70-827f-c692ebd17aea | -5.24819 | -43.911 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75e6d0f2-9ed9-3426-9783-62263d651d80 | -5.96277 | -43.75352 | 2025-11-16 04:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6359c5e-df89-3426-89f3-cac84befe9da | -4.6561 | -50.92833 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2982f559-c350-305a-a5cd-868adc3f5ea1 | -2.83101 | -52.36384 | 2025-11-16 04:55:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5eb529b-89c2-3557-beb6-dda54b2ba847 | -0.33499 | -51.74698 | 2025-11-16 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e655a24d-a114-3c46-810b-5630c7a7bc8a | -5.22362 | -46.91946 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 213187a6-f026-35eb-bbc1-d5a142831f75 | -4.84051 | -45.42733 | 2025-11-16 04:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27d8c07e-c797-3c36-a3ad-7565b1690bba | -3.46288 | -50.11517 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11bf7db6-a0b3-3d02-8c24-a115d8806773 | -4.67879 | -46.73249 | 2025-11-16 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e2cc590-1860-3ed3-b52f-33f132b64dae | -2.90372 | -49.1374 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 868b0b83-bd4c-3bbd-926c-82fbb1194402 | -4.4931 | -47.65679 | 2025-11-16 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 352943a7-2dde-33cc-88c3-f4053f306af8 | -2.47614 | -51.79986 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62ab3e51-fe98-34d2-9da2-71d8886d4573 | -2.62525 | -54.67508 | 2025-11-16 04:55:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2a49e28-8f44-325d-8834-75c815970d6f | -2.51975 | -47.8156 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9e34477b-9f5f-3f4f-a5fe-5dcf80d7addd | -3.40933 | -52.18713 | 2025-11-16 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d16f47c-98f7-331a-b63b-d3cef9ad0100 | -3.4652 | -50.12417 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26927f2d-00ea-3b6b-9ead-6f208ac31c31 | -4.34749 | -50.67406 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30bb4732-d59f-37b6-92ca-cd1e800b7519 | -3.58775 | -53.48621 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99ca7e06-b57b-36b4-9282-131766d836a4 | -3.30286 | -53.84947 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2672ef4-fa05-3307-b725-2c6e2207d7fe | -5.48741 | -46.9118 | 2025-11-16 04:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 06afbaf3-b804-3ef3-9e10-bcf1d215fef1 | -2.32447 | -55.70986 | 2025-11-16 04:55:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45da8e27-90b3-38ab-89de-8108095c64f0 | -5.72213 | -41.40196 | 2025-11-16 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 61c52a36-8d64-3ee3-ac84-f51100d6a68f | -4.43133 | -43.40954 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ac350a42-1602-3a76-ba09-6291911c5319 | -3.99566 | -44.27781 | 2025-11-16 04:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19781ee8-3156-372c-b60f-e7d4f36c17a6 | -4.69565 | -46.31451 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| de191ed4-7d11-3b8a-b731-9ac0deb27dc3 | -1.8365 | -51.07708 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 974d8bd8-5ee4-393a-b198-597ed4eb8fbe | -5.99861 | -41.91492 | 2025-11-16 04:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3c9d8c06-16ad-310a-af21-14045da1ebd1 | -3.3348 | -50.16945 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccdf55a0-22b0-3037-998b-9625bda6a4e1 | -5.24999 | -43.9117 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24c604bf-cf7b-3e46-a84f-940cd07ce92d | -2.96936 | -53.22011 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ad2fa75-1f77-3260-b439-1d13cfed432c | -2.41701 | -53.94363 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44bfbf95-96ac-3d73-9d84-d5581f86e8eb | -3.32038 | -44.56041 | 2025-11-16 04:55:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84b2b560-207c-3341-a926-1196ac79d0f9 | -2.97097 | -51.04756 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8051d7d1-0291-38d4-8fc8-349eab61f736 | -4.43304 | -43.39758 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98747bc3-596e-31c0-a8c3-c64889b72a7c | -3.0358 | -54.59389 | 2025-11-16 04:55:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a12b292-3957-315a-9bae-4e2b54bdac22 | -3.32895 | -50.27908 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3582235-11d9-3c59-8602-7d10208c72f5 | -3.91157 | -54.13326 | 2025-11-16 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79328b3b-a65d-359c-9bb6-74b03e4da5bf | -1.93737 | -47.03769 | 2025-11-16 04:55:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6178408c-aac0-3e74-b44b-61095a68aa59 | -4.57346 | -50.44835 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fa9283f-95d6-3193-8281-8cf308b795ee | -3.15547 | -49.16549 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3387dc30-b3e4-3352-83b8-b3aeb035e352 | -3.39301 | -49.76649 | 2025-11-16 04:55:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cc4d2d3-2883-3865-b461-bc376a424da2 | -5.58124 | -46.1457 | 2025-11-16 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a951e7f7-4950-320b-8194-d42c12bfe1d4 | -3.12833 | -50.28936 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9250cf80-1220-3ec4-a6f1-5e6b5eb6772d | -1.80742 | -54.6551 | 2025-11-16 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75b0e679-aba0-3854-91d2-8677d4041ff5 | -5.7329 | -42.72677 | 2025-11-16 04:55:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7b4c7f4a-9efa-3738-8c7c-f1732d67cb32 | -2.42697 | -45.70824 | 2025-11-16 04:55:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebeb95a9-eee5-390a-bda2-6265bbfac0bf | -2.75165 | -49.52642 | 2025-11-16 04:55:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95c77f0e-fc91-36d0-ab27-18385d013b97 | -2.88466 | -51.42446 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c175c5ef-9430-3055-977f-beef1fc6f5a3 | -4.73422 | -46.38229 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| f55aacdc-43a8-32bc-ba24-15cbcdf00b36 | -3.13002 | -50.29229 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9852c9dd-1cce-32db-af5c-c2ff37bb36c3 | -2.31497 | -57.01057 | 2025-11-16 04:55:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 449b85a1-1797-303d-9bc3-97d545541620 | -3.19424 | -57.04893 | 2025-11-16 04:55:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1fde0b9-e59a-3781-9514-c5e0cc469516 | -1.16837 | -49.20338 | 2025-11-16 04:55:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f2bc9f9-c502-3534-8657-85ab799a15ab | -3.18868 | -51.50052 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08db1e06-aafb-3588-8fd3-a4a166364905 | -4.30893 | -50.87788 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d441d99-44b6-32ea-a6d3-1d3b20afeed9 | -3.28736 | -53.81886 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d473ba2e-6900-3da3-b924-584ddd56737f | -3.36114 | -50.19058 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0780382-ffc8-3026-acfa-61b72e3e3ca1 | -3.82178 | -52.09764 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a9340b6-25f9-3b73-a069-bb47f6dabe74 | -3.10281 | -45.78086 | 2025-11-16 04:55:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca466163-d309-3587-a5bd-cdf6f0206ad3 | -5.73228 | -42.72838 | 2025-11-16 04:55:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 00491a47-9cb2-3b17-9a28-7cfeec4f9aaa | -4.83985 | -47.54604 | 2025-11-16 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58be27e0-d781-3e58-928c-c58d27a07122 | -4.42731 | -43.39664 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README50.md)
