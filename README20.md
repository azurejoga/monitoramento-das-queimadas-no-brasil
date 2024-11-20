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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cba6446-d463-3bde-ae38-1ee3ab00890a | -20.41494 | -43.55245 | 2024-11-20 03:38:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 50e00566-d370-35cf-9514-9e4e820316ee | -22.06351 | -47.08107 | 2024-11-20 03:38:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 357b4804-fc71-3485-9010-1dfed0997cdf | -17.71435 | -41.83379 | 2024-11-20 03:38:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9cfc115f-c513-3961-b28c-75f356ef0ecb | -20.34707 | -40.36002 | 2024-11-20 03:38:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f91f29fd-2fac-3351-a07c-62a3cb64b6bc | -20.41451 | -43.55463 | 2024-11-20 03:38:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fa8e4350-8b43-3810-8a75-83d71d7b124d | -20.34644 | -40.36231 | 2024-11-20 03:38:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f3c3435e-b12c-334b-b111-5bcf13ca1906 | -16.67908 | -43.88389 | 2024-11-20 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d1645b9-c1c6-32d8-b68d-1706ca8f838f | -22.06428 | -47.07755 | 2024-11-20 03:38:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 32f303d1-a31d-3567-aae1-7e458a3a14a5 | -20.89891 | -43.82125 | 2024-11-20 03:38:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e224572b-d92a-3dea-aa35-b838771f9c92 | -20.74083 | -40.59996 | 2024-11-20 03:38:00 | NOAA-20 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1c4be843-1faa-3c62-8d39-5342aae5d5d9 | -17.85589 | -44.71162 | 2024-11-20 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d7a533a-8123-3a8b-80f2-67da7033140a | -22.0687 | -47.08263 | 2024-11-20 03:38:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dafcb3e-e453-33b3-98f7-ee369ce9167c | -17.75204 | -42.89832 | 2024-11-20 03:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0011ba4-c658-35e2-aaad-b4afcfc20226 | -17.71358 | -41.83787 | 2024-11-20 03:38:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 15e61c04-0a64-3801-a2f9-1d167e703ad1 | -22.06735 | -47.08185 | 2024-11-20 03:38:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba32cf14-73d7-3efa-8d9d-a80e023c77a0 | -17.75874 | -40.69349 | 2024-11-20 03:38:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 78269814-5047-3a68-ac3d-1da26c95bb78 | -22.06813 | -47.07837 | 2024-11-20 03:38:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a40d6f86-3fc5-39da-b07f-4f1efc18912b | -18.60908 | -42.83656 | 2024-11-20 03:38:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 92f974a5-ced1-300c-9ad3-8b0b0590c9d4 | -3.8206 | -47.7879 | 2024-11-20 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 042de3c7-7b2d-3953-936d-536604085e7d | -4.4405 | -46.5754 | 2024-11-20 03:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 81d1b892-44f2-3125-bfbd-2832c6f5854d | -1.2017 | -53.6769 | 2024-11-20 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3d33df26-7c4d-3791-83af-4b1ad0f095f1 | -2.7501 | -51.8171 | 2024-11-20 03:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ce1de19c-970a-305a-ae41-59b022ac393d | -3.2014 | -54.3243 | 2024-11-20 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| ae46bd40-20a8-38c7-adbb-a713e09459c2 | -2.6212 | -51.7997 | 2024-11-20 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| bb8d7994-03f3-3f01-a870-6dfad6d3a301 | -11.092 | -54.6221 | 2024-11-20 03:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 5f547866-f4f9-3a97-a2cb-457075c41464 | -1.4603 | -52.6812 | 2024-11-20 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8f50c5dc-907c-3be2-bb4d-d38279cca7b1 | -3.2379 | -45.5615 | 2024-11-20 03:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 98.4 |
| ea4f76df-8f64-301f-9ec5-33d777fd7c6b | -11.1109 | -54.6204 | 2024-11-20 03:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7626d642-2893-3ade-9f53-af603d27d76f | -2.75 | -51.8377 | 2024-11-20 03:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a94722a1-e796-34ba-a433-c77078d17e32 | -3.8205 | -47.8096 | 2024-11-20 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c2929619-ea8f-3918-9836-099f4c87944c | -5.9742 | -48.063 | 2024-11-20 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 5a6abac2-8a4f-32fe-9fa3-9f48ed79742d | -4.4404 | -46.5975 | 2024-11-20 03:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0ea1815e-a19c-3f7b-8675-16584fb20c7e | -11.1106 | -54.6408 | 2024-11-20 03:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f0cdf737-e2c3-3ff9-b268-92da059ad9fd | -5.9556 | -48.0642 | 2024-11-20 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 6669ed40-7675-3f63-9a27-fb757f964972 | -2.6212 | -51.7997 | 2024-11-20 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 326382cb-14a6-3ddc-9d32-1c98918ea829 | -11.092 | -54.6221 | 2024-11-20 03:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 350e0fa8-3562-381f-bb2c-b23ee25d19e9 | -1.2017 | -53.6769 | 2024-11-20 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 14cd1df9-1e37-337b-90d9-7d03ad55308e | -2.7501 | -51.8171 | 2024-11-20 03:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 101252fd-4b93-3125-9875-553c09438bc2 | -2.2996 | -48.4863 | 2024-11-20 03:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 208efa09-4ecb-3f4b-b3dc-c518320057b0 | -3.8205 | -47.8096 | 2024-11-20 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ff78cce8-a243-3303-9a26-0e46eee14fbf | -5.9556 | -48.0642 | 2024-11-20 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| e1036ae1-c6da-3536-a983-81e2917b05a0 | -11.1106 | -54.6408 | 2024-11-20 03:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 3b4f96a5-a35a-3c66-8e02-75bff37816a2 | -4.4405 | -46.5754 | 2024-11-20 03:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c279000a-7634-39bd-95cf-3a4fab99cf17 | -3.802 | -47.8104 | 2024-11-20 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a4b33419-8a9a-347e-ab84-3b3cf61b224a | -3.2014 | -54.3243 | 2024-11-20 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 037ea3c0-90c0-365b-8a98-0472733d40f8 | -5.9742 | -48.063 | 2024-11-20 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 27897b4f-cc3f-3b33-96d6-1c9c53332149 | -2.75 | -51.8377 | 2024-11-20 03:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 9a3082bf-473d-3c71-8250-c6e533446638 | -3.8206 | -47.7879 | 2024-11-20 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 837aeca3-fd8e-3b15-9c6b-c8552d10b0cc | -11.1109 | -54.6204 | 2024-11-20 03:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 0669c6d3-2c6d-3d4a-bb69-4c5f49dd97a7 | -2.7217 | -49.3508 | 2024-11-20 04:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 8d197c26-518a-32f1-a888-79abcc674a8b | -2.7501 | -51.8171 | 2024-11-20 04:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 9a651951-1c1e-39ad-864e-c00e8b9e3a5f | -5.9742 | -48.063 | 2024-11-20 04:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| f176ae31-097c-3b5f-85cc-a24842f8a5e1 | -3.8021 | -47.7887 | 2024-11-20 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 9e567762-dcdc-30b9-8127-8b54aaee649a | -4.4592 | -46.5745 | 2024-11-20 04:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| efa0038d-7800-3e6d-9590-960984daa877 | -2.6212 | -51.7997 | 2024-11-20 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| fc202e73-f2af-3c91-a35e-cf20874cb79f | -11.1109 | -54.6204 | 2024-11-20 04:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 7cefa70a-952c-3deb-ae85-a9d4f73f3a94 | -11.0917 | -54.6425 | 2024-11-20 04:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 17251a53-f819-31a7-b633-53848bde75d7 | -2.75 | -51.8377 | 2024-11-20 04:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| b1b22d7f-bc61-3de2-80b8-a2fcfddc00d0 | -11.1106 | -54.6408 | 2024-11-20 04:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fecd9108-c78d-3d3f-b23f-74cd88366374 | -3.802 | -47.8104 | 2024-11-20 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| cb78fdfc-d29b-3cb0-a96e-83a88efae102 | -3.8205 | -47.8096 | 2024-11-20 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 002fb6ce-46b3-3a54-bc0a-adc108621ba3 | -1.2017 | -53.6769 | 2024-11-20 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e1d8b151-c9c1-3512-891c-2903df9e71f0 | -5.9556 | -48.0642 | 2024-11-20 04:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| ada4f935-fc15-3c9e-806d-ac499c228e7f | -11.092 | -54.6221 | 2024-11-20 04:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 1e902e34-be69-3842-9d73-fb761a11fe34 | -4.4404 | -46.5975 | 2024-11-20 04:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 1c65f276-e989-3246-9820-f477c861876f | -2.9116 | -53.0606 | 2024-11-20 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c7d465f0-a259-3bec-939c-422462e6f4de | -3.2014 | -54.3243 | 2024-11-20 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 542dd329-384c-39f7-b089-722cfa658b68 | -4.4405 | -46.5754 | 2024-11-20 04:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 9ff66861-a7b3-30be-a81b-cb379465b87e | -5.9742 | -48.063 | 2024-11-20 04:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 46219365-fb5b-3174-b95c-dcc38a1b73d5 | -2.93 | -53.0601 | 2024-11-20 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c4ce0b11-fd38-3d88-8aec-cb8ed99b6012 | -5.9556 | -48.0642 | 2024-11-20 04:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 362d495d-8a3c-3c43-bc9d-b218b3df8a13 | -3.8205 | -47.8096 | 2024-11-20 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| d0fa43af-3ac7-3959-87c3-001405922ae3 | -2.7501 | -51.8171 | 2024-11-20 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7234a86f-f466-36d3-9ca4-584ebf4ceb4e | -2.75 | -51.8377 | 2024-11-20 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b2054ea9-6481-33ed-aeae-4a4cb095423a | -1.2017 | -53.6769 | 2024-11-20 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0ff7a813-4b83-32a4-8f8c-2e4f092d1088 | -2.93 | -53.0601 | 2024-11-20 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 222a2079-5751-3fed-93d9-6edd72f1fc80 | -2.7317 | -51.8176 | 2024-11-20 04:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| f7a8a1e4-d161-37a2-a353-621be304d258 | -2.9299 | -53.0805 | 2024-11-20 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 3c8cebe1-2c4a-3f06-879b-759dfe1569e9 | -5.9556 | -48.0642 | 2024-11-20 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d16c47e4-256c-3512-9846-e9664a4795d8 | -2.7501 | -51.8171 | 2024-11-20 04:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bbde1a0b-ddbc-36ff-b769-71e5221f2161 | -2.75 | -51.8377 | 2024-11-20 04:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| fa2ab340-8bb8-3d03-8d48-d741685722da | -2.7217 | -49.3508 | 2024-11-20 04:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 90d2aaa3-48c8-3eff-aba3-1a3fbbdf0682 | -11.1109 | -54.6204 | 2024-11-20 04:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 9ec315ff-32c4-35f3-a032-1e1224a0f723 | -1.2017 | -53.6769 | 2024-11-20 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ba3630dc-2911-3935-995a-515a17e5ee56 | -2.9115 | -53.0809 | 2024-11-20 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 678751cd-cab3-36b9-9861-a989544916f7 | -5.9742 | -48.063 | 2024-11-20 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2957037c-0ed1-3b23-a8a4-6b9e6b532df4 | -2.9116 | -53.0606 | 2024-11-20 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 058d77fe-b5cf-3d91-8535-124c57e00ceb | -1.20398 | -51.78155 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4502d992-fc61-32d7-b3a9-526537656fd2 | -1.4783 | -51.15552 | 2024-11-20 04:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdc4879f-66ff-3dcc-ba15-28a5d02054af | -3.02437 | -45.33438 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f01a7a9-56c0-3649-9aa6-132f6cd90200 | -2.10862 | -48.10276 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19dc5677-3b3a-3eb9-b2a4-ae0bdc95d5a5 | -2.71706 | -49.34188 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d596586-2b98-3520-9bbf-258371c4f13c | -2.81251 | -46.6685 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebb6c854-bcb2-3759-937d-f4275ff908ed | -2.75223 | -48.57226 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 741b8544-5b6f-34a7-a340-65eeae994f4a | -2.40299 | -47.021 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3ac42aa-39f8-39ca-920a-bb72a2039c0e | -1.47724 | -51.97049 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54a136e2-aeb1-3e37-8a5e-01f089a92e66 | -1.31454 | -52.40806 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1dedfae2-0956-39d4-a0de-9cd6091ba06f | -1.3112 | -52.40495 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 387f43ec-8229-38ce-a336-9fa410896045 | -2.65575 | -48.78721 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d13e1e7-954e-37a5-af2c-3abe69110fd4 | -2.43012 | -46.52581 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README21.md)
