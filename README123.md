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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 162607c1-6969-3517-8d95-c17ff2093d3a | -8.86998 | -69.17468 | 2026-10-07 06:46:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c8874800-bc43-3bf2-97ae-e0ce33deedac | 3.52841 | -51.27719 | 2026-10-07 07:16:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d5412c7e-acda-3c9b-b0c9-a933be5925b9 | -3.08655 | -54.26744 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c632e632-a532-39fa-9fc2-4b127c822563 | -3.04538 | -54.22001 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b26a810-ebff-3ddd-91d6-1069946632c3 | -3.27145 | -54.00762 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5c6d4748-c60b-3e55-b3dc-0c2631e8389c | -3.06294 | -54.24618 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| df7c8ec1-3999-36a4-b45a-4e367a22bb90 | -3.07517 | -54.28354 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f9cc8de-60f7-3d5b-b4ad-9e0ac5c20268 | -3.85078 | -55.98436 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 5cb1dd1c-0d42-3752-8536-c71029b8d870 | -3.57424 | -54.65235 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 12c6269d-e4c7-3a3e-ba60-a2cda9301da1 | -2.77296 | -54.07203 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b55ded45-2a3d-3bb4-9172-35ef38394352 | -3.26617 | -54.04251 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| de2d25be-af88-3e73-9abe-3c6140633a5b | -2.79789 | -54.08459 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f8141fdb-a979-38d9-bcec-43d3ea2ea67e | -3.18593 | -50.55744 | 2026-10-07 07:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 700d9647-54b5-36d1-9285-744c07e4d4e3 | -4.57298 | -54.94925 | 2026-10-07 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ebed6b0d-9937-3d1f-8d89-84e64f1d6026 | -4.34306 | -55.12655 | 2026-10-07 07:18:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f29a6fca-cfc0-3c7d-8ed4-8f59055973df | -3.5164 | -54.65597 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 383404c4-959d-39ff-9e0c-b80bd88017c7 | -3.09398 | -54.27742 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f7fc31e0-3f80-327a-8766-1799f8371cce | -2.95127 | -54.05724 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 072eb539-fbb0-374b-8a3b-2fe6c9379a7e | -2.76158 | -54.08814 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8096a0a7-cf7f-3b72-8805-876e304240fb | -1.1278 | -54.11789 | 2026-10-07 07:18:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 74bee40d-8a6f-3f99-9b33-19ba5c991abe | -2.7677 | -54.10682 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 295.7 |
| 6feafccc-bed2-35e7-9750-22c7459b0207 | -3.29899 | -54.02632 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 943afda0-1ab8-3aac-a655-2f0279ec85cd | -3.35202 | -54.16539 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 37ba5e90-02b9-3864-9ff0-8f2a136732e2 | -3.05592 | -54.15041 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a9c0e423-f988-33b8-b162-452b8b74e0f0 | -5.6805 | -53.49082 | 2026-10-07 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e1c94ae0-c515-37a3-a974-242d02c13e56 | -3.52383 | -54.66598 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a0d496ea-d647-3780-b7c6-95f1e19b903f | -2.87237 | -54.19989 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5b21245a-4a9c-3062-9d9b-b2e6efdce8e1 | -3.18411 | -50.5698 | 2026-10-07 07:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 250fc3fa-592b-34de-94c4-8c2eccfc5636 | -2.99863 | -54.1153 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b65b9450-313b-3810-bd08-6cd0463b00ef | -3.98139 | -56.21741 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e834aca8-0a32-3ce1-8600-4d64fd66da0c | -3.17379 | -50.56831 | 2026-10-07 07:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d019072f-405e-3c78-9e31-3381e7ba60bb | -2.99204 | -51.04509 | 2026-10-07 07:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9dd8deff-f784-3b0e-aaa7-54c69e5f49cb | -3.00475 | -54.13399 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 254ac9bb-0bae-3a0d-ad2e-1f734de2004e | -3.28006 | -50.13782 | 2026-10-07 07:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| b8320ff5-7022-3030-bee6-23d1f35c1aac | -2.83964 | -54.0617 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8f46d2f3-9aae-3425-b917-ce0bae6046a3 | -3.06203 | -54.1691 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 39a5203e-4794-3b70-a7eb-d66e2fcce4bd | -3.05544 | -54.2126 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b5f5aba9-3bc9-35f0-a15d-18a66923a9dc | -2.7629 | -54.07944 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 289b5a0b-e113-3ca1-b7b6-4d254f6488dc | -3.05676 | -54.2039 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| cdc35404-0a73-3f53-8fb0-930e37a695d8 | -3.28279 | -54.01503 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| f6750822-24fe-3537-9c6b-9b4f618082f7 | -3.29023 | -54.02504 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 34e15d10-fb04-3e61-9d1c-3dc4b407518b | -3.11276 | -53.77507 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 1f239694-64d1-33be-9f35-21f10e26df44 | -2.75895 | -54.10553 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 40630101-6b3d-3934-a3ab-081f27c76de5 | -1.29245 | -54.56291 | 2026-10-07 07:18:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d841c2f6-df72-3fe2-ac08-efe203c84970 | -2.1263 | -54.79557 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| abd31935-18a0-386e-ac05-9adb62a426e4 | -3.48667 | -54.61596 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2d6509d2-ad24-3c01-abb8-ed7cb61a584c | -3.50172 | -51.68355 | 2026-10-07 07:18:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| db4fcc85-f559-3e77-9041-577ae3d2df90 | -3.10531 | -53.76501 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| ab8aed93-9964-3f92-9259-657c973e10b2 | -3.04378 | -53.93485 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 58e0a687-9265-3c21-968b-67f3d693688e | -3.04754 | -54.26478 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e3157183-8aee-3a25-a13c-ff9e402236db | -3.12339 | -53.70483 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b279e82e-b41e-36c7-bd4b-e1a0cfa13f3f | -3.10398 | -53.77377 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4d0aead1-31b1-3f45-886d-7d8afa1116b6 | -2.98891 | -54.04497 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 54a64ff3-3069-35ab-95a4-5667b8f9420e | -3.73202 | -55.97913 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d2ec5d51-613f-3e61-bde6-48dba5705286 | -4.75289 | -55.65313 | 2026-10-07 07:18:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d60840ca-0493-38b7-b540-82417e6bdadd | -3.27621 | -54.05865 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ddc33d25-60ac-3067-8b18-d86639d28b2a | -4.26387 | -54.86653 | 2026-10-07 07:18:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1072ef25-90d4-33d9-b395-4f95308d259b | -4.4599 | -47.90836 | 2026-10-07 07:18:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| ad90972a-d93d-302a-9f2d-066eee668546 | -3.29504 | -54.0525 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 5677bb17-74f4-30e8-adcb-9a89af69b62b | -3.08523 | -54.27613 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 218a861c-6dfb-34ea-8f42-e7308a8bfc7b | -2.90005 | -54.01719 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 67c8e704-878e-3afc-b635-9f0ab70b9fbd | -3.28365 | -54.06865 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 1d84b68e-f8a3-31b0-852c-1d5dfa3dac36 | -3.11109 | -54.16435 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0a8e8671-7909-3332-bff0-35cd795f3a3b | -3.29241 | -54.06993 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| d4a6baaf-554d-33ae-96df-dd0fed2cabff | -3.10273 | -54.27871 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1d215e78-0044-389e-8835-5be9858658aa | -2.9412 | -54.06466 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ef67cb4a-6fbf-37ba-92a6-02878f5b4348 | -3.96995 | -56.05569 | 2026-10-07 07:18:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a7024cc9-b530-3114-b348-e7fb30f69c27 | -4.44238 | -54.96788 | 2026-10-07 07:18:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 189b7bee-30d6-3fd5-aab9-ac60ecaf9c85 | -1.28366 | -54.56161 | 2026-10-07 07:18:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9ae6c394-9c34-3335-942b-ce460b18de23 | -3.96431 | -51.90591 | 2026-10-07 07:18:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 34a7ceff-b977-3414-ab6e-1c926f894bd4 | -3.28628 | -54.05122 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 8edca19f-309d-303e-8748-09fc9bc4c7af | -3.10404 | -54.27001 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d7505cd-36b9-357a-b891-d5cf12da8f34 | -2.99731 | -54.124 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a605b5a6-14c4-386b-8b8e-eae55c5bbc95 | -3.21103 | -53.87368 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 119895d0-2d18-3d36-9bad-5f999923837c | -3.80331 | -51.03411 | 2026-10-07 07:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 949193d3-3d11-3f0d-9e27-443ef00b3b57 | -4.44707 | -47.92052 | 2026-10-07 07:18:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| cd5f1df0-f49e-31f1-9227-0ca720175e0c | -5.72209 | -45.14648 | 2026-10-07 07:18:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| df8a4175-c995-3a35-bf7f-9317c321a64b | -2.88075 | -54.08554 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5903ffe2-f0e1-3625-9f1b-a9d58ec4bb77 | -3.8598 | -55.98567 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 42163665-4b8a-31f0-a0ba-894a6043c5e7 | -2.77776 | -54.09941 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 137b5e7c-164b-313d-bbef-30da80166992 | -3.53655 | -54.64113 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 8ce75dfc-34e3-3a8d-a53b-b34cefac8c34 | -3.18775 | -50.54502 | 2026-10-07 07:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1035a47c-6f93-3625-a1d9-9944b8efd31d | -3.01481 | -54.12657 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a8a0992a-bf33-3af0-8fcb-9a47a623142f | -3.1774 | -50.54354 | 2026-10-07 07:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c14e9ea0-2969-334c-b413-fece33c11769 | -1.10504 | -54.15009 | 2026-10-07 07:18:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e036691d-2d44-3901-a779-2104709c66b0 | -3.07301 | -54.23878 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f53adaf8-b4c3-322c-a265-a9456cf12c00 | -3.28234 | -54.07736 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 696cf1db-01cb-3376-9bac-31a2e69067d2 | -3.07912 | -54.25745 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 6489a406-3662-3e07-bb09-88581a084576 | -3.26749 | -54.03379 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 8bca4c8b-cce2-3eed-aaf9-256400cc97c1 | -2.93679 | -54.15295 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 256d4767-69ad-3d5b-b8a9-dda3090c74fd | -2.83832 | -54.0704 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2a59e420-1154-3a68-b799-30378d810b96 | -2.89173 | -54.15521 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ca21f70-2b51-3d4f-b2bd-5ccba428fdf2 | -2.97573 | -54.13199 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 267767f3-5661-320b-b6c6-8be6bad2911e | -2.76027 | -54.09684 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9673bb22-4d9d-38ab-9543-52f0550fd833 | -4.15597 | -55.14017 | 2026-10-07 07:18:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 272ae319-5ca4-3d55-86d6-e340da023653 | -3.28016 | -54.03248 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| a3725413-4a39-361d-b8fa-ea8f0c3527b5 | -3.13735 | -54.36162 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56411a2c-524a-376d-bb15-5cea20fce8ae | -2.78281 | -51.67998 | 2026-10-07 07:18:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 34efec62-d152-3c5e-b3f3-a54b02a7902e | -1.29378 | -54.55414 | 2026-10-07 07:18:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d56c7689-cb57-3d1d-8d6d-6533fb1df53d | -3.27884 | -54.04121 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |


[Clique aqui para ver as próximas entradas](README124.md)
