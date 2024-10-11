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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02da5bb8-01bb-382c-8897-d06243ec76de | -7.57279 | -44.77898 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a61d523d-1dd3-370a-9ef0-a14aec4ff8b5 | -7.57111 | -44.79004 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5189fd14-bc09-3f02-af69-3cff06be6021 | -7.56772 | -44.78952 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db088637-db9e-322c-993f-902c56937b96 | -7.30639 | -44.96622 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8199c2c0-9755-30ff-a41c-9e410ea2b933 | -7.25934 | -44.92585 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c78227a8-6c23-3acd-91b8-157e139395e1 | -7.20097 | -44.86858 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d91fce6a-a885-385c-8db8-7e9a52f67650 | -7.17281 | -44.87171 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76014c09-9981-381c-afdb-7b43f26b95c4 | -7.12146 | -45.04814 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bc552c6-4b13-3840-9480-a7da529328a3 | -7.08301 | -44.68289 | 2024-10-11 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5a4a99c4-ed59-34aa-8bb3-94166b702ab2 | -7.05863 | -45.08617 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a9379ea-7421-3e63-ac16-eb7557b43a99 | -7.05582 | -45.08209 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43439852-55f5-3506-b3d4-d8fb1c453c2b | -7.05186 | -44.68207 | 2024-10-11 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c840a82-20e2-3063-bf11-bb8461d365a2 | -7.04911 | -45.08107 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65248afc-3998-373c-937e-fb82a467379c | -7.04855 | -45.08464 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed7996d7-5a7f-3d32-9a15-26143bedb370 | -6.96118 | -44.83551 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2787fd5d-aae2-376a-90f9-56e542ae1531 | -6.96062 | -44.83914 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12dada65-849f-33d1-925b-c0b741f6a0c2 | -6.9578 | -44.83499 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b311ba38-f818-331d-b70f-8c8f83647c60 | -6.95724 | -44.83862 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e981a8ea-71a4-395e-927e-b8babc033506 | -6.95443 | -44.83447 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67d2af3a-c751-3190-abf2-93d7d2cb518b | -6.95387 | -44.8381 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf968379-0f05-324a-820b-40efa007c41e | -6.93764 | -44.6046 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 304ba548-4302-347c-b4cb-2c6fe0293b92 | -6.93754 | -44.8319 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b852015d-0cec-3f3e-8c24-5e10188a402c | -6.93709 | -44.60826 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c44af8b7-48d9-3285-80d5-e16c9725594e | -6.93698 | -44.83552 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16a449d7-5c16-3670-9dfc-bc1cdfe5f8b3 | -6.93643 | -44.83914 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0720800e-76be-31ee-8a94-34ea50f8c1b0 | -6.93424 | -44.60411 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 177eb495-f0ab-3b26-993b-e5d2164759b9 | -6.93368 | -44.60777 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eed189a8-7866-3161-a78b-0edc49841bc4 | -7.93083 | -44.86357 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f201eaf0-f0c2-3518-9160-679bd6d5e071 | -3.61413 | -44.78661 | 2024-10-11 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ba8bb4b7-6454-33bb-9c7d-4b5dde3f7be3 | -3.61359 | -44.79009 | 2024-10-11 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 88183d57-4518-3191-903a-caab759d2429 | -3.61135 | -44.78261 | 2024-10-11 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 277f7161-8680-3a43-bfd1-1ad2e214ee5e | -3.61081 | -44.7861 | 2024-10-11 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 79ddeb22-72c6-33ca-94af-6ed37549914a | -3.61026 | -44.78958 | 2024-10-11 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f024b6c0-68d6-34b8-801d-5018ed8331b0 | -3.60748 | -44.78558 | 2024-10-11 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f6df87fe-770a-35a7-ba35-b2203cac0052 | -3.8096 | -45.48926 | 2024-10-11 04:23:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97f80a23-79e6-3297-bdc8-f889983e612b | -3.63786 | -45.95551 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1076f449-935d-3d57-aada-82f9521da164 | -4.90364 | -45.66079 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d372549c-e9d6-3ce6-b01b-cd6022409529 | -4.79893 | -45.33323 | 2024-10-11 04:23:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f39ce48d-3621-3417-80ba-ca3d06a62a6c | -4.70762 | -45.11258 | 2024-10-11 04:23:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1050bcb3-e178-3db1-bb34-1f2668ce65ad | -4.50332 | -45.59498 | 2024-10-11 04:23:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a6038ce-72a3-30df-9122-2e40c764ae6d | -3.73161 | -44.66467 | 2024-10-11 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89f4e119-d89c-3a53-b38f-508acb6abf1b | -3.70402 | -45.1022 | 2024-10-11 04:23:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a233ccd-a3d2-3d27-9e89-4b355c5267dd | -3.70348 | -45.10565 | 2024-10-11 04:23:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f60e0e9-03d8-3426-9870-0705b45a6115 | -3.72773 | -44.66766 | 2024-10-11 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d24661d2-2ad2-3aac-8dc2-90b6de755526 | -3.63731 | -45.95895 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8587244-9103-31af-a3d5-0b30d9168228 | -5.05381 | -45.59291 | 2024-10-11 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b68651f-e666-3b6f-bcfc-24bf60aef4c9 | -4.9395 | -45.73738 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2c49f97-22d6-3dad-8793-b44c9413a3d4 | -4.93619 | -45.73686 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10a52f9b-ecfb-3ac4-b0c1-d8817477554e | -4.91872 | -45.78353 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ea43cef1-6a91-323a-aceb-18e3bba5cb2e | -4.91541 | -45.78301 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8e04272-e6d9-3041-831c-310d5bc99437 | -4.90033 | -45.66028 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e754187-cccc-315b-abd7-03480eacd680 | -4.89703 | -45.65976 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4bbf5fe-0ca6-300b-bd79-2739d574e94f | -4.87428 | -45.7832 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ec5ac43-3966-3c2f-8e74-be27849c0d6d | -4.87374 | -45.78664 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2303977a-ec69-32c0-9d68-5248e81581d0 | -4.87098 | -45.78268 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2636723-ac69-343a-b2d4-b3688d3356b5 | -4.87044 | -45.78613 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9478a55-1087-34ed-80a2-c0c63dc9de0c | -4.85979 | -45.37823 | 2024-10-11 04:23:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03b3b8a5-3656-38e7-a8f2-de3bd1ebc4a5 | -4.83505 | -45.92517 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 46e4fea2-90c3-3ac8-9636-dc65500a5429 | -4.79839 | -45.33669 | 2024-10-11 04:23:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c2474ef-8b2c-3513-a01e-edfb49605438 | -4.68202 | -45.82009 | 2024-10-11 04:23:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c9d9bb7-191e-3f76-9faf-d0c8c8d49c62 | -4.6755 | -46.05524 | 2024-10-11 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 162e1906-5981-3b2f-9ce0-8a1969d7ad3b | -4.6722 | -46.05473 | 2024-10-11 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0e1125a-8168-3d04-b8eb-06da6fde7ca4 | -4.59729 | -45.60202 | 2024-10-11 04:23:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34b915de-9406-3fa8-9df0-74563bec5bb5 | -4.50916 | -46.20529 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6efd7307-aec5-36e0-bccc-81d49ac1b16b | -4.49833 | -45.58363 | 2024-10-11 04:23:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42956c73-e7ae-385a-8f9a-e3dc84356f7f | -4.49725 | -45.59052 | 2024-10-11 04:23:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f0f4540-f235-38b2-8023-740f7fb96539 | -4.49488 | -45.71351 | 2024-10-11 04:23:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 747ed317-bfcc-3898-9eed-62a5d52c3530 | -4.37939 | -46.10052 | 2024-10-11 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b5ffcc4-3562-3d2f-bd57-1027ae634b79 | -6.32389 | -45.70288 | 2024-10-11 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29e24ec2-024b-3868-8ac5-0ce4b4202c58 | -6.31457 | -45.71916 | 2024-10-11 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8888e42e-ec5c-3706-9e9f-5c545dfa93d1 | -6.14382 | -45.72473 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b37fb41-621d-31d4-bdaa-be5b9a60352d | -5.59964 | -45.05415 | 2024-10-11 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e2b200d-47a9-3502-b954-19d2cd34d956 | -5.5888 | -45.36399 | 2024-10-11 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c017165-3bff-3c58-8de1-41d478fa1cf2 | -5.43438 | -45.08979 | 2024-10-11 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec9360c0-f866-397a-bb8f-6019d477844f | -5.43148 | -45.0891 | 2024-10-11 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a10621fd-ed46-30b4-9833-575ab3c49670 | -5.36889 | -44.9427 | 2024-10-11 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4795501e-debb-31a4-9e49-b0a7380ad548 | -5.36835 | -44.94622 | 2024-10-11 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b61aa1b8-a0c4-358c-9634-122215352d9e | -5.35083 | -45.60365 | 2024-10-11 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c68f1b7d-2dfd-33d2-a3b4-ec6017d242da | -5.21871 | -45.71029 | 2024-10-11 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0a76f4b-0e78-3682-9d88-756ee05c8fb7 | -5.1357 | -45.32933 | 2024-10-11 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68d909d6-0ec8-33d4-be44-36e363d58362 | -6.08127 | -45.99465 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c755ec9-2477-3c82-bf8f-673e210e12e1 | -6.0785 | -45.99068 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba344e27-9ae9-3648-a529-236c7addf967 | -6.03349 | -46.53519 | 2024-10-11 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00f4e049-611f-3394-a76f-3b5a8eacf422 | -5.98608 | -46.34005 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a347a32-2415-3b0b-badb-bd746b288e63 | -5.98554 | -46.34351 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b30099f-08b2-3604-8763-53f24127869f | -5.97813 | -45.74094 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d5d1c02-0ff1-3e00-a88e-2c6abc9c08ce | -5.88389 | -45.58424 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48dc4f19-c3b9-3eca-815d-d300278868c1 | -5.86751 | -46.42361 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 518900db-b270-3d27-b913-cc9f0adb029d | -5.84023 | -45.9492 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 356185cb-5689-3ddb-b702-86e48957f655 | -5.83969 | -45.95265 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 771c52b8-195c-3291-a216-e238e5f8497f | -5.7735 | -46.1154 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af3a763e-44e5-39d2-91d8-9f67772ebad9 | -5.77296 | -46.11884 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bb73026-c487-3b68-8907-ae04a171c4ee | -5.60799 | -46.36812 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09df473f-4eb4-393a-a214-52aa8df3fcfd | -5.60468 | -46.3676 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 710795e7-ccb6-313c-9fcf-a057ca45f4bd | -5.60414 | -46.37106 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b4faa45-821d-3268-a3a0-19f6e5007921 | -5.60333 | -46.24722 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38f5769d-bcde-3ae8-8475-34a0fe979c88 | -5.45133 | -46.30486 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 860d8ff7-0ff7-3be2-bd0f-463ad80a8e11 | -5.43817 | -45.89321 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22e5f063-71f8-356f-9714-5884977e692e | -5.43763 | -45.89666 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a086e91e-813e-3dfa-8ea7-3635606b1809 | -5.43511 | -45.97746 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README56.md)
