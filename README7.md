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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eb46a1e-cb35-3392-9ad9-88b2bea435fe | -2.9856 | -51.344601 | 2024-11-13 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd6da159-fa3b-3573-9502-082606baa33a | -2.7252 | -51.732899 | 2024-11-13 00:52:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20855054-cd7f-302d-960e-75dd28ca572a | -2.5529 | -53.997002 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8136a40-5eaf-310d-9c9a-127919f78bb7 | -2.3935 | -53.658901 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bb8e951-bb42-3bb6-bbc0-05821b210235 | -3.1251 | -59.010399 | 2024-11-13 00:52:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b47046c-bd6a-3835-bc80-6afa0e6dd9f2 | -2.6599 | -51.717499 | 2024-11-13 00:52:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 998ce2ec-1c77-319f-ac1d-c7bb8302efbe | -2.5614 | -54.034199 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273118ae-2431-317c-8143-a1116ddc6930 | -1.4098 | -51.110001 | 2024-11-13 00:52:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19d0d4ff-d46a-3614-a9ea-29462327bd76 | -3.0973 | -54.3064 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d57e864f-306b-3c61-a013-7eea4dab3244 | -2.2061 | -53.741199 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa7eb5a9-7d56-3313-b48f-fb672ac418e3 | -2.6844 | -57.362 | 2024-11-13 00:52:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7490fe2-0fd5-3cc5-9a06-d4f75c07fc55 | -3.1027 | -53.9674 | 2024-11-13 00:52:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0be11f39-f3b6-3598-9531-aba716bd8bb5 | -2.3977 | -53.7225 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62064e2b-f50a-3995-bc5f-312b4ce3c12c | -1.6417 | -52.529499 | 2024-11-13 00:52:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5a95259-ab63-3ea4-ac16-efcf12ae10c0 | -3.0832 | -53.249802 | 2024-11-13 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca7a03bd-fa70-34bc-b8cc-e0880ffcf074 | -2.2453 | -53.732399 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aa6d326-f34b-3116-bc8f-0fefe4c0f869 | -1.6437 | -52.5383 | 2024-11-13 00:52:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9681e63-c5dd-3eb6-9de9-d8013a9fecc6 | -2.2355 | -53.7346 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f82cc7aa-0bce-3939-8ad5-c285bf0d22e0 | -1.7618 | -55.5994 | 2024-11-13 00:52:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 354401c4-b71d-37d1-a62e-d681f7de3448 | -2.2488 | -53.7477 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec047d5c-4cd6-3e2f-a3a8-b8c694191caf | -1.1902 | -52.129398 | 2024-11-13 00:52:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ebce73d-4601-3313-ba89-cf48937b739c | -2.5644 | -54.0023 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3621d828-5ccf-3590-917e-47b15375874d | -2.3879 | -53.724701 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbc18b1c-4a47-3929-9411-8b6ca3558a6c | -2.7438 | -54.656101 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eeab040-7cfc-3486-8419-d94868c7aaa3 | -3.1402 | -53.2286 | 2024-11-13 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44199d3a-f415-3419-9d29-521e0827772f | -2.623 | -54.260101 | 2024-11-13 00:52:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf72f24-5e8c-3f44-ba94-0bf3aaaa1f61 | -2.7093 | -54.6861 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74650cf7-fcbc-329a-b4cd-d5e29ab314d8 | 1.0574 | -60.5849 | 2024-11-13 00:52:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 67e73a50-284e-3860-9e7c-90dda2999cc2 | 1.5947 | -55.8853 | 2024-11-13 00:52:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a64cc4dd-5711-3c50-931b-31228a3ad7e8 | -2.2027 | -53.7258 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56af37d2-345b-3374-8f6a-d4c98d6aa646 | -2.4544 | -53.972 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24198987-3205-376a-a99f-aa132c7532d1 | -3.0322 | -50.566898 | 2024-11-13 00:52:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d56d70a-8290-3ae4-b551-55444da627e3 | -2.2506 | -53.755402 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3924615e-be3d-3c06-98bc-8e6cb194516f | 1.1398 | -60.5849 | 2024-11-13 00:52:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fcedfae4-7ec5-3125-a477-c5f8985b1f54 | -3.1462 | -54.476398 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b441a0ea-45ed-306f-bb9e-37ed2b0a0142 | -3.1055 | -54.297001 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8f16b5a-7c0b-312f-ad27-8ae36be909d6 | 1.0692 | -60.5783 | 2024-11-13 00:52:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e96468a7-e631-3520-b7af-8b66161757c7 | 1.0672 | -60.587002 | 2024-11-13 00:52:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6c9a049b-54c9-37b6-99b1-e3974908221b | -1.8707 | -53.580002 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac16b63-1ff9-3a9c-b77b-0a0a666c9138 | 2.7034 | -60.9529 | 2024-11-13 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 544547b3-53c7-367a-84a5-89074c5f3270 | -1.7633 | -55.6063 | 2024-11-13 00:52:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbc6c9e4-7ca1-36f0-bd3f-a1343422f290 | -3.1038 | -54.289799 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38dba805-cec5-3ed9-8fb2-c9eccffda140 | -2.8289 | -57.087799 | 2024-11-13 00:52:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61aff43c-fd26-3a7b-ab29-8a43d6576a3b | -3.1542 | -59.1413 | 2024-11-13 00:52:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 232a2c16-18e1-30d8-b6bf-93d4d97fb291 | -2.7681 | -54.717602 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 482cabe5-15e2-3ef1-a1f8-10154048c075 | -2.4748 | -54.061401 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0c2860-1138-3270-aac6-ecd2533d00f1 | -2.6148 | -54.2696 | 2024-11-13 00:52:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdc3342b-859a-3954-b731-c75c78cce90d | -3.0851 | -53.257702 | 2024-11-13 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f75752ba-2862-3778-936b-2bd7feaa8218 | -3.1232 | -59.002201 | 2024-11-13 00:52:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b9e583a-8eac-33af-9ff3-e15efdf10fa8 | 2.6916 | -60.959499 | 2024-11-13 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b68a9b0f-7bbe-3fdc-80a0-3edca3857a05 | -0.2804 | -51.6548 | 2024-11-13 00:52:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 75ac828f-ef19-36ce-a52f-84474a1b99a1 | 1.3137 | -50.8666 | 2024-11-13 00:52:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f47efd83-020f-34f9-b984-61038f692549 | -2.5627 | -53.994801 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cafd3d5-2a3e-3bf2-9393-eb6e199a7f3e | -1.8782 | -54.202599 | 2024-11-13 00:52:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0180b2f3-13a3-3ebd-9bfb-681c8321659a | 1.0594 | -60.576199 | 2024-11-13 00:52:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf24158-9fe0-3f4f-a90d-58115df5b4a1 | -2.2079 | -53.748798 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdcb4121-5d3b-38f0-a42a-86aa560b6344 | -1.2106 | -51.767399 | 2024-11-13 00:52:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e1ac4ee-1974-3eaa-946d-221ec5700b0d | -1.3001 | -55.745201 | 2024-11-13 00:52:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19670e48-7df7-3889-a13d-539527ede6c2 | -1.5189 | -54.981098 | 2024-11-13 00:52:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbf1c3e4-40a0-38f4-96e7-279244ca9dad | -2.3854 | -53.6688 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58ec26a0-1769-3461-b6c7-c42010324dde | -2.239 | -53.749901 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 729999d8-e7df-3850-9449-1651c74d147c | 1.5931 | -55.8923 | 2024-11-13 00:52:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4354f965-f975-3549-bd6c-63fc39edd1f1 | 2.6743 | -61.169998 | 2024-11-13 00:52:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4da26abf-fa41-3df9-96fc-64a61967d880 | -2.454 | -53.924801 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53f5ef30-c2a8-3a9a-b0d7-a73281f53662 | -2.7804 | -51.3913 | 2024-11-13 00:52:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbc1ea48-ac9d-3c04-b151-cd01258cfcc0 | -3.1439 | -53.2444 | 2024-11-13 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8764adf-b332-3462-9a23-827954580209 | -2.7713 | -54.731701 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c584db57-5e16-3fe7-acb1-abea8df12634 | -1.2781 | -52.4697 | 2024-11-13 00:52:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7af3d438-5109-3bc7-bf47-fbdcae1b290b | -4.3597 | -48.080898 | 2024-11-13 00:52:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a37857c8-cd2d-3a57-bd8f-f593b4c81e38 | -2.2471 | -53.740002 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 912186cc-7abb-31ab-918e-abc6ef137db7 | -1.8864 | -54.193001 | 2024-11-13 00:52:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75faf448-cdcb-35b5-afe6-5398ac9f9cfe | -1.414 | -53.474098 | 2024-11-13 00:52:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b51c5ec7-feb1-36f6-8810-9cb4cc308b94 | -1.6555 | -52.544998 | 2024-11-13 00:52:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de0ca422-6b0c-38db-bc96-ae792070bb42 | -3.1479 | -54.483501 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32b008c4-dfa1-315d-93c8-0dcc3d35f287 | 1.0554 | -60.5937 | 2024-11-13 00:52:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b46edfac-452c-32d4-b172-3be617ce83aa | -1.4073 | -51.099098 | 2024-11-13 00:52:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb10eab-8fd4-3790-a438-e7e3f77ae0c5 | -3.094 | -54.292 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 575c899a-ac94-30b8-bd10-9008acb15412 | -2.7454 | -54.6632 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34ddda14-83de-364c-a518-6b37f116bb08 | -2.7697 | -54.724701 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 229286c8-c782-3252-a256-abca0e0f5076 | -2.0366 | -53.947102 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9b81fd9-55c4-39b6-8db6-5d0c8adecda5 | -1.6535 | -52.536098 | 2024-11-13 00:52:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffe9ea33-0436-31c3-97bf-d136b44d973a | -3.2589 | -54.5186 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01b8c43e-5a06-3354-8d97-00a8e635caac | -3.2605 | -54.5257 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e77277d4-d121-3b55-8b75-94f16a2b45cd | -3.0957 | -54.299198 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84081597-3b1b-3a5f-a8d9-1d23b8e399e5 | 2.7014 | -60.9617 | 2024-11-13 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a3873388-e2c8-3ed6-bc06-83aca361a8ef | 1.0652 | -60.595798 | 2024-11-13 00:52:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d7c4a846-74ae-3857-81e7-3b5245252409 | -2.6247 | -54.267399 | 2024-11-13 00:52:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84d6ad3c-e086-3b28-a799-d3463db9954d | -1.8766 | -54.195202 | 2024-11-13 00:52:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3989f43a-8f72-33c6-b0a5-3e8e8f27e9af | 1.3109 | -50.878899 | 2024-11-13 00:52:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d61ed1d9-42d9-3ab4-aeba-1fbf3bbc157d | -2.3994 | -53.730099 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54e409c2-02ba-3aa0-9679-946759d1a199 | -3.0605 | -57.2939 | 2024-11-13 00:52:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3380cee-45b2-3db4-812e-83a1459f2512 | -2.4339 | -53.881901 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6572db1-c355-3334-a5f6-5d837ed14abd | -1.6515 | -52.527199 | 2024-11-13 00:52:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2be91d01-63a3-368b-8733-deeefe0c28fb | -0.2827 | -51.665199 | 2024-11-13 00:52:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 571d6674-d456-376c-9306-6ea1a3cfc1a4 | -3.1444 | -59.143398 | 2024-11-13 00:52:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e168b9f4-0067-31ce-99e4-f84e7836e1eb | -2.2408 | -53.757599 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1ba9490-965a-3d03-9197-1a517fd90812 | -3.1044 | -53.9748 | 2024-11-13 00:52:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34ba8053-a006-3c62-acbd-d30ac5955772 | -2.2044 | -53.733501 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4a053ac-53e8-3d0d-8abb-ddb89340462b | -2.5512 | -53.989601 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 735992be-05d1-33a0-805c-0e7e783debed | -2.2159 | -53.738998 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
