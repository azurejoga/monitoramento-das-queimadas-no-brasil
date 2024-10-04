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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f06a1b31-b085-3558-a4ae-fa2815f6aa08 | -9.32319 | -50.79403 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 61c400e5-79cb-3ff7-8e95-a786a541fdaf | -9.32307 | -51.13609 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 515243a0-3f6b-3a32-8a34-42951abbcfe0 | -9.32251 | -50.79877 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4dc6169d-f81c-3078-a6de-251b97bc3ee1 | -9.32183 | -50.80355 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 300d41cb-d992-34b4-b59b-199e3a1c182f | -9.32133 | -51.12222 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d6838b9-c2a3-33d6-bc27-49d622b26ecd | -9.32008 | -50.7888 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8a04fce-1803-3b84-8653-bc851fcf82ef | -9.31941 | -50.7935 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc20c3f5-113f-3cec-b73d-d001007a434b | -9.3174 | -50.80757 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2e5295b-8712-330a-b791-bd2c747d2533 | -9.31698 | -51.12608 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82d5d99f-0cba-3c1f-9aad-910e166b70ac | -9.31611 | -50.81654 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3aa18343-edd8-3926-a9cf-965d9142917d | -9.31564 | -50.79293 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86d23f77-bc41-3687-9221-242801ab368e | -9.31362 | -50.80705 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 700868c0-92d8-301f-8f21-acdacb1f85f6 | -9.30986 | -50.80647 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65fe3c4b-8182-351d-8f48-adf819eabcba | -9.30857 | -50.81545 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ebf7fad3-c218-3cd4-a42c-0942555b0a44 | -9.30782 | -51.11113 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2982a51c-25bf-3035-b69a-a2479c58244f | -9.30717 | -51.11557 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe2a837d-8094-3a9a-9019-ea3a4deecf87 | -9.30689 | -51.06556 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a11ae105-4945-3dd4-b7f5-6fa5b8d5a93a | -9.30676 | -50.80121 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc992d05-1961-37a7-acbb-5091fe3091ae | -9.30559 | -51.0745 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f42fa6d4-efef-388b-a100-401cff37f047 | -9.30187 | -51.07394 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14fab010-6ba2-3962-a5bf-254f059aca38 | -9.29881 | -51.06894 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f7f25f4-205f-3441-9a25-d86ede3d7898 | -9.10788 | -50.92005 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 510a02dd-559a-36ed-a609-ac7fd38d694f | -9.1048 | -50.91497 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cfe5c473-619e-3c48-9a0f-82c256b6ea3d | -9.10414 | -50.91949 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c0bf390-fce7-33c1-90d9-c11033204409 | -9.10106 | -50.91442 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bb2b66d-5743-3e0a-96da-5b90685764bb | -9.09798 | -50.90935 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18c1ce01-405c-319d-a323-1af886989afa | -9.09732 | -50.91388 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4b281ab-1a92-3fee-ac8b-8bc43a2a473c | -9.09554 | -50.89974 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 048200bc-86bc-3077-80ef-3fd60b7f5be9 | -9.09424 | -50.90879 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80aa55b1-0a37-3fa4-9f07-cf121c0999eb | -9.09181 | -50.89918 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52b2ccfd-e6b8-3d38-b5ac-12947a69d705 | -8.38361 | -50.82346 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dc0a96c-3421-3f4d-8691-24fe5600970a | -8.33601 | -50.86333 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ab14580-c88f-3ed3-b6b9-884a7a4dcd6f | -8.16936 | -50.49331 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7a6793d1-f593-3a6a-b1c0-247441dfaaea | -8.10735 | -51.1257 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d3809e4-8a6f-3840-99f9-c51dde76f2b9 | -8.09219 | -51.10203 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa13f278-3374-3cac-baee-481f9c2448b8 | -8.09149 | -51.13219 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b070b4a2-f649-3ea6-91f0-556e5bd3338e | -8.09098 | -51.11024 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebf6a09e-0c75-388d-845b-2a48e892cc78 | -8.08853 | -51.10157 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27969bfe-fa1a-3543-8525-c1e67cf6bada | -8.08848 | -51.12727 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b37bcbae-6d5e-36f3-99c1-c3244f78d3ae | -8.08785 | -51.13155 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49330093-da26-3eb1-b80c-6281d723cfac | -8.08549 | -51.12225 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ba54a64-68a7-3237-a880-63d423516b5f | -8.08296 | -51.13947 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdee4485-8f1f-38d2-8f33-9b5f7d190aa1 | -8.08184 | -51.12168 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2711d81f-6d18-3803-8a84-e2342a4341fc | -8.08121 | -51.12599 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 275d4d29-26b6-394f-9b47-37bc37f26906 | -8.08058 | -51.13029 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ae23389-d46a-303a-9573-1262e4ec9e11 | -8.0782 | -51.12111 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03c6a3b3-c84f-3bdc-b359-0a705ce44afd | -8.07694 | -51.12973 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 130eecf4-659d-3d8d-8adf-21cad010544c | -8.07443 | -51.14685 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 083c4ee4-48e7-3a23-a26f-09a9535e5e97 | -8.07381 | -51.15109 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62398849-f27a-3557-bfe6-3d801c32a423 | -8.07079 | -51.14627 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b693290-2efb-311f-8c49-e4ea461ecd49 | -8.07017 | -51.15057 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24f49ddc-5efc-3fac-b744-e5a243384fe0 | -8.35026 | -50.86955 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3cb6765e-b3e9-32a1-baf4-e89260b8ae16 | -8.29601 | -50.91307 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4355ee8-fdc7-3230-996c-d9cb5471f8e9 | -8.16869 | -50.49794 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 596dd800-3581-31db-a836-6c270f6b9786 | -8.1649 | -50.49741 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5afc05f2-28b7-3ed7-9099-4db04619098b | -8.02818 | -50.90237 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dbd2b34-7816-368a-8300-752a2d58ee20 | -9.36837 | -50.74852 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f49dd9a0-e65c-3009-8564-6670b6ebf730 | -9.3639 | -50.75267 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08dc55e9-8975-3e64-8028-5789b4c322c8 | -9.33387 | -50.80015 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 01faadbb-cf08-3821-9e37-1568a95795e9 | -9.32386 | -50.78935 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 80acbb75-7d43-3763-b373-ff55d52e1a1f | -9.32118 | -50.80806 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 88dd6736-e23b-356f-8955-1ecd76c9227b | -9.32054 | -50.8125 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7922ffa6-9d73-3c63-85b6-20963967d9d8 | -9.31873 | -50.79826 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f888becd-e12b-3fd9-8558-5563793eafa9 | -9.31805 | -50.80305 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fa546d6-eb0c-3dfb-8d68-e7acfea0c119 | -9.31677 | -50.81198 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51ff6fed-992f-39c8-a1d2-6b7a238abe0c | -9.31496 | -50.79768 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc27391a-b788-3e0f-8b7b-5be3ba840a58 | -9.31427 | -50.8025 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c58eda6d-1812-3249-b698-96399c7fcd3d | -9.31299 | -50.81146 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d3c65e4-cce6-335f-922d-c9dd210e491e | -9.31234 | -50.81599 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 404a5c06-bd18-3971-b983-61e5d4c214d8 | -9.30922 | -50.81091 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd546b7d-644c-3788-8f35-bded1d05751c | -9.30863 | -50.81309 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ca126bd-80f9-32b4-9313-b1c405a7da0a | -9.10545 | -50.91047 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2f808caf-a347-34de-a00e-27352a92dcb2 | -9.10171 | -50.9099 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b1c1bf6-4f05-3721-9ddc-27a6c60841d4 | -9.09929 | -50.9003 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2950cae-f1a9-3af1-8971-55c163d39cf1 | -9.09863 | -50.90483 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 074324c7-e09b-3921-96f5-5727c3e9f3fd | -9.09489 | -50.90427 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5feec9f-dd0c-3cd9-9d32-1917dfdc2f10 | -9.09115 | -50.9037 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64a3b92c-c66d-3f39-bf79-74e510e89088 | -9.32437 | -51.12723 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bf820b6-8f2f-3729-aad2-4aee31e60ef5 | -9.32242 | -51.1405 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21714e90-9cc3-3367-a6a5-83ac748c97dd | -9.31763 | -51.12167 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b0fa01d-1886-3c6e-aff6-52d1caedcf00 | -9.31522 | -51.11227 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e713c041-57e0-3828-90c4-6f8fcee08ef4 | -9.31392 | -51.12111 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70551ef0-805e-3f8b-9377-fc391a84ee2b | -9.30346 | -51.11501 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3def2070-eb6e-3aab-b8f7-d20b5f579399 | -9.30252 | -51.06949 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21fb9afb-64b8-3b6c-9fe7-cb775ac91bdd | -9.30123 | -51.07838 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98f8b9b3-6d3b-390f-9c5d-d13465b99db9 | -9.29816 | -51.07339 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4b85781-9beb-321f-a070-8ce5f6bec81b | -9.2964 | -51.05941 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c41f644c-e590-399d-836e-8855193a1f49 | -9.17047 | -51.68296 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50e6c0a7-73f5-3e9f-88b5-6f6718d841b6 | -9.1225 | -51.5355 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fe2ffb4-95e3-391e-a4a7-650066c83354 | -9.12012 | -51.52657 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a4e4de68-cf25-3f1e-9acf-a5d5ef20e46f | -9.11824 | -51.53934 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36c513d7-3f1d-3abe-96d7-573bfb01d321 | -9.11411 | -51.51712 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2767a7ea-7ee5-3cb5-b3a6-014584dcc1ec | -9.11348 | -51.52142 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7741e2ab-c3b0-3f33-b154-aed44e3590a0 | -9.11224 | -51.52994 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec4aad6e-25ca-3c39-ad1a-dd9e03c64747 | -9.1116 | -51.53431 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1ddb1a6-fa06-3bf4-a3e2-26e64f39f509 | -9.11097 | -51.53856 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 667fc20a-0a01-310c-8480-f547bf98b971 | -9.1105 | -51.51655 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76713c93-ac8c-3ce7-a2cf-3af3f3875155 | -9.10987 | -51.52085 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6352362-a56a-3705-926e-1e3a34ba00c4 | -9.10925 | -51.52511 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df226641-b6ea-37fa-b1fc-6076b843df58 | -9.10862 | -51.5294 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README146.md)
