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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 778cb405-0c23-309f-bfa4-ebc963bf5151 | -1.64663 | -52.04062 | 2024-10-25 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1f2e0c3-e27b-3f62-94d3-52af351a91b4 | -1.53219 | -51.92165 | 2024-10-25 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7027a5d-9097-32c0-94e7-8b0430e7ff18 | -1.10463 | -52.24585 | 2024-10-25 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa825277-fe14-38e3-b796-251b436d9523 | -1.10396 | -52.2499 | 2024-10-25 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0651cffc-fd9b-3d97-816c-8e883e6869a2 | -1.60412 | -53.31179 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| e516ddc9-2376-3427-ae26-4512089c6172 | -1.59878 | -53.30586 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 546731cf-a6f6-388f-907c-95b6a4fec48d | -1.59799 | -53.31069 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 7ab44d94-21f1-3cba-885e-9805129c85f3 | -1.59265 | -53.30484 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a3aea4cf-2562-381b-9b92-af4289449cbe | -1.59185 | -53.30967 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2f5d1e2f-a63b-3cf4-a5c7-fdf29f6165f3 | -1.59105 | -53.31453 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 12aa5dba-e262-3f5c-9d06-8415a011c096 | -1.5857 | -53.30869 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 627ad289-e3a1-3723-ad57-2413e0acfe97 | -1.5849 | -53.31355 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25efc931-245c-33de-9f3e-f98a29b2b2fc | -1.57875 | -53.31257 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b375f8c-4974-3e25-b9db-8d0e0089308b | -1.57795 | -53.31741 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d028641a-4b19-32b5-864e-ed3638e185c8 | -3.21537 | -53.36507 | 2024-10-25 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a74ee573-d35f-361a-8ecc-9e64289d36c9 | -3.21462 | -53.36954 | 2024-10-25 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 154eb2c2-88e2-30b8-a68f-a5c44c64efe4 | -3.07427 | -53.2368 | 2024-10-25 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 536794ba-585c-3f8d-b8ed-883f4361a639 | -3.07354 | -53.24105 | 2024-10-25 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2723eb1-bf87-3318-940f-c2164dc300e9 | -3.06825 | -53.23601 | 2024-10-25 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a11c562-73be-3d7e-9b21-5c6770757a76 | -2.99547 | -52.85913 | 2024-10-25 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9d671f3-4d08-357c-8660-2c40da754987 | -2.74024 | -53.19918 | 2024-10-25 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9000392e-5573-3e5e-b872-33b2c7695503 | -2.73945 | -53.20378 | 2024-10-25 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17f386b1-a590-3bf4-bc23-9989fb5748a1 | -2.73734 | -53.20119 | 2024-10-25 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5d2ba422-8b97-3937-b93c-7f48a0cb193e | -2.6232 | -52.44428 | 2024-10-25 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cb4629a6-f418-323f-a9f3-b837edc5be5b | -2.62256 | -52.44813 | 2024-10-25 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| e4cf32d1-4c0d-33e5-b1ac-bd57dd964975 | -2.61748 | -52.44333 | 2024-10-25 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7b5e3f8f-f842-3139-a45e-c06dc9b7eb7b | -2.61684 | -52.4472 | 2024-10-25 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ff44480f-5422-3f38-9f9c-f9c05805bcbd | -3.45335 | -52.62294 | 2024-10-25 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8f61d07e-02c5-30e9-9c82-a50d28d0841d | -3.45402 | -52.61897 | 2024-10-25 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 727cd75a-0cbf-330b-8633-fcddb5c34dcc | -3.68566 | -53.42796 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3dd92c51-e3b5-309b-adf0-a87367d6e5c9 | -4.22262 | -53.78698 | 2024-10-25 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 798d47ae-f9fd-3531-88b1-a912b05c7390 | -3.89556 | -52.31444 | 2024-10-25 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 455ce566-98c4-378a-a5d4-29ea91b1e08d | -3.69161 | -53.42918 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c49dd967-34be-3109-a0f3-f99dbac556d3 | -5.70074 | -53.45562 | 2024-10-25 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e01bea6-36f1-323f-9cd3-629f0e8b1a6b | -5.70002 | -53.4596 | 2024-10-25 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51408a81-f5e3-3cd0-89bc-8d8397ee5098 | -5.70032 | -53.45877 | 2024-10-25 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ab71ed5-2eee-37bc-9d88-bf7e5b317b3f | -1.1854 | -53.67163 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| b48d44fc-48b5-3365-a260-2f452d21406f | -1.18062 | -53.66131 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a0068a69-2178-3377-b8d5-bc7bdde90103 | -1.17979 | -53.66632 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 25b63b37-7fd4-364b-8701-c47ee041f364 | -1.17646 | -53.66741 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 6bc0598f-858e-3a1e-aa07-fa13c6e6c522 | -1.17565 | -53.67254 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 0ddb23e2-01c0-3783-b7ab-5c35e26841fa | -1.14119 | -54.09947 | 2024-10-25 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccc749a0-8b3f-39b2-91e3-2cff4eead845 | -1.07446 | -53.65619 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3f0cbb10-8d4a-3616-9407-f1987803a4f0 | -1.07368 | -53.66089 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72a00fef-a16a-37d9-9786-4c0221647cf1 | -1.07121 | -53.65857 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5c6b558d-0bf6-3c33-a402-d8cb4f5609bf | -1.1862 | -53.66677 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3df33793-e8dc-3f80-98ca-e1123abc46bc | -1.18366 | -53.66292 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| bdfb1856-e887-3569-a750-6b78f4e42958 | -1.18288 | -53.66783 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| a9b898ce-deee-3102-b676-5afe3b9df05d | -1.18208 | -53.67287 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| c297ce57-5317-3452-996d-6feed136c855 | -1.17894 | -53.67145 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 0f9c4523-847c-3c6a-88e2-d226801659df | -1.16832 | -54.09654 | 2024-10-25 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47b5cbbd-9df9-350e-a871-fa5f503b680b | -1.1616 | -54.0969 | 2024-10-25 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27228545-bb7a-3d68-ab89-e3cc82c54b8a | -1.16085 | -54.10154 | 2024-10-25 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f2a96879-5e14-3b7b-b1f8-e4983139d185 | -1.14031 | -54.10484 | 2024-10-25 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cf8c6b2-e97f-333a-a000-a96651e5c2c7 | -1.0728 | -53.66621 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12546c9e-3f86-3a31-b637-c88e7c62e284 | -1.07189 | -53.67172 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86b58552-1f42-363f-82e1-ba79c4cfefd2 | -1.07046 | -53.66332 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5c7f85c2-d2a8-3206-9f9d-2e8d59b29eb9 | -1.06959 | -53.66877 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 04544f77-8aed-3b8a-8637-909fc4f87384 | -1.0673 | -53.66017 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7eb6a4ed-2bf6-3692-9751-fa8ca324b355 | -1.06647 | -53.66523 | 2024-10-25 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ce3ac6ab-58df-397a-b717-a7b6f2a94799 | -3.63024 | -53.96629 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6eb49a23-e49c-3017-89f1-17393f33bd76 | -3.48817 | -54.44685 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2420268f-ed45-3988-bf73-131c57740e55 | -3.48802 | -54.43852 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c894fd7b-7d00-39d2-afcc-a4f2f7ad3123 | -3.48703 | -54.44436 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f329c3aa-6e62-3727-ae23-637940b9d9d8 | -3.4812 | -53.9863 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1cbecad5-9493-3879-80ea-6821574c6137 | -3.45549 | -54.63215 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca99a1b9-ef22-3905-9278-b2b136cb8140 | -3.10983 | -53.72807 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ee33726-c7ca-3585-9b1b-634bed606d1c | -3.10901 | -53.73285 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23fdfef3-dd8f-3499-8959-e64f3b64b89f | -3.10866 | -54.16765 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7219e4a8-22b9-310b-b15e-339052f184c7 | -3.10795 | -54.1558 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bb00eb1-3e40-3ce8-8daf-51a7947a0333 | -3.10634 | -54.16542 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53a5b11b-46a1-36b6-b714-0014bd86aff6 | -3.10483 | -54.15228 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34de29c5-4855-3eb2-bc95-89e03903a8ac | -3.10448 | -53.7223 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 54a66c88-0dc1-3c78-9e02-95ca7f5eb9f3 | -3.10399 | -54.15712 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23f790e4-f8d8-31bf-aab1-c7f308fa9239 | -3.10366 | -53.72706 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 053c1bd5-eee4-3c95-9e15-ce004cf154ba | -3.10316 | -54.16186 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64df3e01-d63e-3e2b-9c52-7edc87f60583 | -3.10284 | -53.73183 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9506d49d-81fe-3eba-a68a-faf0d98c677f | -3.10232 | -54.16665 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2670d7c8-6916-3d21-bc98-74bd32d57a97 | -3.1016 | -54.15487 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 064d4a8d-70a6-3045-ac32-db16593319ff | -3.09832 | -53.72128 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 41ade185-b3f6-3844-8424-fe5937f66079 | -3.098 | -53.72607 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5a7027d8-8669-39f4-8bd1-3ec542f26bee | -3.0975 | -53.72603 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 084f3a41-5842-3391-8fe0-a23f69099696 | -3.09526 | -54.15383 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 325fc863-1a5e-34d0-8da4-e68158ee4223 | -3.07422 | -53.82394 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20594ef8-af47-3913-bd6a-f58a55bda4f7 | -2.49781 | -54.13726 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc61286f-d1a3-34d7-9215-83ef4ce9298a | -2.49691 | -54.14254 | 2024-10-25 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ee3cfc6-f790-3a9b-99a8-4d7e45f180ff | -3.6365 | -53.96704 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60476142-40ae-3d84-a08d-a8ba3db06b13 | -3.57033 | -54.58842 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70dd8404-4c94-3204-9927-5b17e2f1c141 | -3.48918 | -54.44113 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56854c3c-aced-328b-9403-78a916a8827a | -3.48324 | -53.98429 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d5947ac-2745-3241-8020-51c1d5435e92 | -3.44816 | -54.63456 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cfc25b34-2cbc-302d-9c0e-e42b8f1da969 | -3.44804 | -54.63651 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5772b0d6-24d1-3526-9fc8-1aa95a570996 | -3.44724 | -54.63996 | 2024-10-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08021f37-282b-3b9d-bf4e-f3dcedd60afd | -3.1353 | -54.27802 | 2024-10-25 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d2b9408-22c2-32b2-ad0c-301c94999918 | -3.10877 | -54.15088 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb910f28-ecea-37f6-a49b-2e4fcb0ce1a5 | -3.10714 | -54.16061 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95917877-1cde-32dc-b5d3-d5e30b2368cc | -3.1057 | -54.14732 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b360ecdf-0c1e-3dec-9b59-b46b5488be9b | -3.10553 | -54.17025 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed376d95-9387-37cd-bd5f-cfe05c8788d3 | -3.1008 | -54.15963 | 2024-10-25 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 854615da-7c18-32eb-b7e9-bb51f3a3acda | -3.09879 | -53.72131 | 2024-10-25 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README36.md)
