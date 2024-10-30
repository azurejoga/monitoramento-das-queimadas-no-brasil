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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aedc5601-1eaa-39ed-b5f7-db0439ffbabc | -3.22624 | -52.18374 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24f696eb-f29a-396f-99c2-a954960f118d | -3.20746 | -53.40104 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2241556-8fe5-3a1e-8d11-bd910c1a200a | -3.20383 | -53.4005 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e12f343-305a-33c5-99ef-c90a1dc8909b | -3.10342 | -53.05402 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4a2e702-8e6b-32d2-862f-6525034ba307 | -3.10277 | -53.05833 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69ea33bf-8112-3566-b0b5-90fce88957cf | -3.05839 | -53.25134 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0865866d-e551-3ee6-bfc1-e853d2ba8398 | -3.05817 | -53.25447 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1de64fc4-9bc6-325c-bd3f-3478c4d125e6 | -3.05772 | -53.25562 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 298bb06e-a1c7-3cbc-8368-5752c3cec35e | -3.00047 | -53.43202 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea558c66-5ff6-3b27-9259-2d46b1312dfa | -2.99984 | -53.43612 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 649546d1-81a5-3487-b655-1713d7f825a3 | -2.9992 | -53.44022 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dc432ac-f575-3132-a8ed-86d6960c23d9 | -2.99685 | -53.43151 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39fb0882-ca50-353b-855b-cf0210fff358 | -2.99622 | -53.43561 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f18f5041-90b0-3423-9df1-982c0904dc73 | -2.99558 | -53.4397 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e133a5f-c97c-3a25-87e8-0339ec4616b3 | -2.99261 | -53.43505 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 227216e0-f6e1-32dc-8be5-d822d12d8f5d | -2.94479 | -52.566 | 2024-10-30 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 504892b5-21ee-3187-af30-6973234dfa3e | -2.94457 | -52.56788 | 2024-10-30 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9300657f-3d09-3d4c-8640-ef215fff818b | -2.91308 | -52.59603 | 2024-10-30 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a04e036f-ab7d-3803-8d98-3538d590c9dd | -2.91236 | -52.60066 | 2024-10-30 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae579217-9186-3b1a-b9dc-0b7a3f46c544 | -2.9093 | -52.59543 | 2024-10-30 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be1ba2dc-2264-3114-8b00-05860f8279e9 | -2.78165 | -52.0957 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ea17508-4513-3d64-b5a8-685d1c9cc1b0 | -2.77776 | -52.09514 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d75f08f7-5e54-3036-a089-d1a5831078c7 | -2.86902 | -53.34135 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89544771-c292-3600-bb22-b3894f0a11ba | -2.86712 | -53.35371 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 591b64db-1c07-398b-8973-f9c13bd926a3 | -2.86668 | -53.33242 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e22620d9-8767-3efd-ab02-bb417fdcd335 | -2.86603 | -53.33666 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c638cb2-203e-38d6-9752-c7064ecf13e7 | -2.86474 | -53.34509 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2db9f1f-6f22-3acb-b8ad-d2b23dd9f5ab | -2.86411 | -53.34918 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4b15b53-80be-3979-8177-8a6e6358931a | -2.86349 | -53.35321 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64ebe345-d2bf-3f69-99d4-13aadfa58db0 | -2.86304 | -53.33196 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b63681ec-0ec6-3414-a651-e90393271ad5 | -2.86239 | -53.33619 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ecab74d-7036-3e1b-b1e6-2685a2061ab0 | -2.86111 | -53.34459 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e1e790c-0d0d-35fe-85ab-4864477bb94d | -2.86048 | -53.34867 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ddafdf6-3da9-309c-901f-a8bb805baccc | -2.85876 | -53.33566 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8489c38a-4155-3e0b-a3d6-887503fc2af6 | -2.85748 | -53.34405 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 238afa31-23d4-35d2-9cc6-07f2a23be0f5 | -2.85386 | -53.34351 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce6bd6fb-5f5a-3725-8ca1-c3b4b20ff844 | -2.85024 | -53.34293 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65a7191a-f539-39c4-9810-9ec6bbec7c5c | -2.84853 | -53.32981 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd850138-7658-3d43-aa69-ce7d075cedf7 | -2.84599 | -53.3465 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9f0c672-36e3-300c-a564-d45dc6c08f9f | -2.8449 | -53.32925 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcd2a568-6f4e-3ccc-a952-02550974e606 | -2.84236 | -53.34597 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d10ba7a-b015-3c66-84ab-545e98e2b89c | -2.83717 | -53.32482 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddaecdab-f0e1-324b-9f7e-37fce07c800b | -3.88576 | -52.38231 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67d6cc5e-dbdc-3147-af09-da76d41fd021 | -3.88187 | -52.38184 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc2afe2c-38a2-3e4c-93bd-c29634ee8872 | -3.87869 | -52.37658 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9148832a-da4f-3e7b-9916-028ef8e2a410 | -3.87797 | -52.38134 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 618a14f6-05b3-3557-a9bf-263bcad615ea | -3.77892 | -52.39828 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31cfc429-b719-329c-8768-6ddf9992c784 | -3.7782 | -52.40299 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1f2c9a5-f0cc-37f3-bf8b-d5373633669e | -3.71328 | -52.43015 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22065b82-3daa-3c51-b996-dc3b8f172aeb | -4.29969 | -53.72298 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b750c8c-a24d-3dde-8177-f7ca1d145ac3 | -4.25386 | -53.62706 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb750d63-6c20-3159-b6c2-e6635847029b | -4.25321 | -53.63128 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f74a98c-7b5f-36e3-9565-19d78c77dbbb | -4.25023 | -53.6265 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75fff629-feba-3a2a-8906-2fdfa95d03f2 | -4.2163 | -53.87242 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9aa198a-f920-3b9f-977a-993768037042 | -4.21336 | -53.86771 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cc47b1c-ca86-3f62-9cd3-93c1a218955b | -4.19668 | -53.46364 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc77a499-d0cb-348a-9dd3-340da919f88e | -4.01913 | -53.81498 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc97d4dd-e61b-33a2-97e9-a2ccac88feb6 | -3.72162 | -53.75267 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa931ed7-e593-3c9a-afa1-42245e62716f | -3.71803 | -53.75213 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8351efc8-0c73-300e-8378-321720b0b510 | -2.24242 | -53.72218 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a2c2cdf-e4bd-3ecc-8aa9-efcbac7d8846 | -2.24181 | -53.72615 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 510cb81b-b52d-3fca-a9e9-c4be13a0df49 | -2.2412 | -53.73011 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd9f08e1-33e4-3ee9-8324-1b39df48d2d6 | -2.2406 | -53.73407 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ee8aa42-078a-36e7-80b9-3f06d938b38b | -2.23828 | -53.72561 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc31f278-c44c-374d-9708-c7de78c18c03 | -2.23767 | -53.72957 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 074723a8-fe98-3a7c-a34a-56bfea5601ff | -2.21379 | -53.67402 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a346433-2861-357e-bb18-0543af67275e | -2.2007 | -53.68826 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5d5812a-6bf9-3248-922f-51284f18741c | -2.19778 | -53.68378 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12193452-71f8-338a-9970-0e84d9ab8f71 | -2.19531 | -53.69958 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10085364-68ee-321c-b6dc-6300cac466e4 | -2.18993 | -53.71088 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f97283b-c6eb-3b38-8ff2-354aed05a535 | -2.18392 | -53.72623 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d857981-9342-392b-8737-22775d148c79 | -2.17548 | -53.6641 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c16c38bf-7cf4-348b-8832-6684e5264e46 | -2.16779 | -53.66697 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e012ce2d-8719-3940-ad6e-35e345792d6f | -2.16718 | -53.67094 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43d07826-0145-3907-894b-24ebfbb325c4 | -2.1668 | -53.83616 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6d28eb1-930b-360b-b365-52f0436bb388 | -2.16426 | -53.66641 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb125381-811d-3f4f-a583-bfddcab7bc70 | -2.16365 | -53.67038 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab818367-7b79-356b-b885-c3829753e67e | -2.16072 | -53.66585 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79b5b8ea-7b34-3694-ba8d-b0dce2401219 | -2.16011 | -53.66982 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9076c706-53c7-33df-897e-f5fde5324017 | -2.14488 | -53.65108 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd05bb6c-0c59-37ed-9ddd-83e17d1c780c | -1.86917 | -54.89079 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18e1b96e-bb48-3153-9498-eccc0cd48e4d | -1.50119 | -54.86047 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9ad3af1-2735-33bb-bfd2-3f532a865b25 | -1.34551 | -54.65397 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3989e106-3702-3985-abeb-0481d6ed76bf | -1.34269 | -54.64984 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a86feaff-9849-32cc-9ce3-69e52804aa33 | -1.34213 | -54.65346 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09edadb2-05f3-3a9b-ae66-48e08eaf9739 | -1.33931 | -54.64934 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0941a39b-c7a5-3cae-956b-c534d73cbf92 | -1.33875 | -54.65295 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06a259c8-1f01-3ad2-a937-dcc4e6b2d86b | -1.28889 | -54.67432 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93bef86c-0ce7-3b90-b564-6aafec405de1 | -1.28551 | -54.6738 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b85a176d-a40c-3950-9960-36932e26a934 | -1.9546 | -54.05435 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4209b19-ede2-3f89-aba5-b8f9eb569bdf | -1.79724 | -53.67459 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a0c8e60-018a-39ab-9b58-7ef781eafc74 | -1.68629 | -53.80991 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a019f9cd-bced-3dab-a017-9e97a1f44c8e | -1.64659 | -53.87188 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a9bc0f9-2ffd-35d8-8207-45df3e8bacbe | -1.4573 | -54.06992 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90535c87-7bbb-38ff-8c18-a8d5168713f4 | -1.45671 | -54.07373 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e73aef3-6e32-3430-ba20-da9507202d54 | -1.45612 | -54.07753 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 117ae07d-d7fb-3942-a0d3-2fe062632f91 | -1.45385 | -54.06937 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 953d3a83-dc59-3607-b6fb-c6b2ac88925e | -1.45326 | -54.07318 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55a65079-a4f4-39e2-9251-7186cb2dda8d | -1.45266 | -54.077 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2907f8b-8b2b-350d-ae6f-290bda5ab797 | -1.45224 | -54.21534 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README91.md)
