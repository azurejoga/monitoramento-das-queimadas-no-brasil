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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07246732-1e79-318f-b883-08a9cf449ebc | -1.29233 | -52.22693 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e579da25-45fa-3b25-9b80-6d7dcee6ffc1 | -1.20046 | -51.77174 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb501c10-feda-3621-b17c-1dad0d68418c | -0.29648 | -51.60338 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ce3c2da-50b0-3557-a1ec-2f8267d58f2b | -1.14462 | -53.40562 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3d73105-75ce-3e88-ad88-f046953fdc14 | -1.46617 | -55.45271 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 521ad15c-ee4a-324a-9cae-1baed875dece | -1.3956 | -52.17559 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe7137fd-7ef2-378a-8d8e-f9d00e3b7673 | -1.38947 | -55.18041 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59868a67-8710-39ae-8a5e-55d5e6c0c93d | -1.72789 | -53.02217 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2f8b1285-925e-3fc8-88c8-d22c066dc7e0 | -1.49381 | -52.54594 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a72398a-89f0-3115-98f7-19c63d8da891 | 0.18657 | -51.22004 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16ed6516-660b-353c-84e5-c61dc485329d | -1.02058 | -51.81657 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d110c09-4247-36c4-a690-bb4b32cd1d88 | -1.245 | -51.61867 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b926ffde-cff1-37b4-a5c1-81bfa9f7a927 | -2.29351 | -51.11982 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd26b2e3-65ee-3106-944c-f6426c27ff47 | -1.64437 | -52.66754 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1475cfa4-7737-38d7-9bf8-7cb07d20c8f6 | -1.6221 | -52.59352 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fac4cae-f7e9-3bf0-8605-65bad28ca9d2 | -2.06762 | -53.43389 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea0f56c1-c016-3e06-ae8e-afc4dbf628e7 | -2.03194 | -50.07495 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14660059-c1e8-32e7-bbc5-a7ac68dc15ce | 0.0507 | -51.71553 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdd0ee43-b97d-31c3-96d0-155b329b69d8 | -2.14257 | -53.7772 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52be0c3a-951d-3cb7-b21b-296850716ae3 | -2.13415 | -49.80197 | 2024-11-21 04:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daec0c6b-e5cb-3a4c-b8f5-818d74f0d735 | -1.75656 | -52.66768 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfd02497-d702-330e-a546-f536dbdb0e09 | -2.01698 | -54.53231 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| ff453fa4-77b2-3a22-8d84-dbff2f77d161 | -1.64256 | -52.61435 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 70bd964c-bed4-33ba-8b63-28c8f269a25a | -1.64034 | -52.60694 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec37c65a-8247-37de-957c-4a2b43e4e681 | -2.2262 | -50.85402 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8790fdf8-9ad2-3b9f-9b37-295c4a933f7d | -1.36045 | -55.5112 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8433872-6339-3cdd-954a-e843f9b9635e | -1.34243 | -51.39471 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84d912c4-9538-3bcb-a3c6-1a7ad662c417 | -2.4021 | -48.61275 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f757635-393d-3cba-8ea4-b09bdec88668 | -1.51474 | -52.08684 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c3f5c5b-b393-3db3-9788-f8de61d01e31 | -0.7111 | -51.79708 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 447de8aa-c927-399f-a24f-55f83dd72257 | -1.79 | -47.19921 | 2024-11-21 04:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ccdcc2b-8714-3ec6-9320-27ffeada658d | -2.25284 | -53.68167 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4166c89-2ff2-3406-b67b-c6a4daea2e58 | -1.26741 | -51.60752 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cb54410a-7cde-310c-b739-059d05835137 | -2.09062 | -50.62862 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b882f8c0-f011-3608-9210-0e4f6b70dc7a | -1.12167 | -53.39814 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 12895b38-57e4-33c7-aed0-85411626613a | -2.20152 | -50.54441 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fee0c45-78cf-3872-804e-f2e1f07be734 | -1.21548 | -51.74145 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cf89e08-7ef0-3a20-a1ea-e2f3fd92f9e2 | -1.21886 | -54.18621 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3355c8de-b61f-315d-a168-98fa8d143052 | -2.83011 | -46.67862 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8125a0f-4799-3378-8c63-4c7b71acac74 | -2.09268 | -50.5004 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2668d8c9-243b-34dc-a7e8-7dcd4683ff6e | -1.44213 | -51.68196 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54f8a061-5473-3a74-ac07-47817a69ad8f | -2.38181 | -48.92042 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb5cd130-6824-3f3b-b09c-6319302a148b | -1.07309 | -53.36242 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 345810c9-2f76-333f-b32b-14bcf3892e63 | -1.72192 | -52.69404 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cc5cd92-2cfb-33d1-a79a-58f96b04e6ac | -1.1241 | -53.60006 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17dbab27-4d27-329b-a201-e6cb21b63f7b | -1.72152 | -52.7398 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfdc33e4-c904-3872-9834-7d143aa65118 | -1.61987 | -52.58611 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3e585a6-6d82-39fb-8fb5-5016e2d278fe | -2.83253 | -46.68057 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6473889d-7b72-38cb-bd69-5ba46d12bd8f | -3.5946 | -43.62583 | 2024-11-21 04:53:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92827eb8-0884-3104-865a-d5082d1988d5 | -1.40933 | -52.10987 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acc7c8fb-cb84-377c-9410-86799845370b | -1.21164 | -51.78794 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b45db16-f365-342f-b6ed-1f0b1ad8521d | -1.72746 | -52.70195 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 94d5626b-3719-31fd-bf6b-8cd7c531a2a3 | -2.18092 | -52.12883 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4ba3f2d-da36-31f5-8dad-a77ac6f58cf1 | -0.35466 | -51.40905 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 794e0e6d-cd31-3e8c-85f1-b6d5f9184a49 | -1.728 | -52.69851 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9befbe59-c239-317b-aa6c-2400f9655dab | -1.65941 | -52.52863 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 352e47e5-4f45-3768-8bd8-a27223528b27 | -0.40045 | -51.63417 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 257db47a-9c5f-3b41-93f0-881442c3cd78 | -2.2653 | -50.80889 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31b2fb26-89b4-3b39-91b3-b6a3d15386e3 | -1.33793 | -51.43076 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94d7640b-3568-3520-871f-e8e4bd9b6d7f | -1.78813 | -53.61252 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ef18ea2-e865-3a2a-b4e5-a933f6dcce37 | -1.25906 | -51.76993 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6baeddf-2c0a-3033-8c42-a0667a41c755 | -1.91085 | -55.40228 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98731ae3-6119-32c7-99e8-87712784320b | -0.79909 | -51.49192 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b8e626f-9642-39ae-838f-591e1b8f7718 | -0.91382 | -51.78181 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff009f53-b749-3be6-918c-1b1b1bcf5a21 | -1.12817 | -53.70337 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0738d1c-9a5c-35a6-a4b0-e2868c0dc2aa | -1.38638 | -51.58545 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab2a82ac-249b-3f8f-bf1a-af002b07c277 | -2.93624 | -48.34028 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6e22e17-0e8f-35eb-b185-420dacc54e72 | -1.17053 | -53.62849 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a4dce1d-c4dd-3da9-b866-8eaee19879d0 | -1.96307 | -48.38841 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70d474a2-5b02-3823-a128-f16443af142a | -1.21828 | -51.74551 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 795b57be-8d45-338e-b71c-f95055cb6667 | -1.13085 | -48.34876 | 2024-11-21 04:53:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c81d33e-5253-3a70-8d62-f88dd6609235 | -1.78586 | -53.58393 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e486891-025e-3888-ac1a-a2030058a6ac | -1.84239 | -55.10806 | 2024-11-21 04:53:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bf38476-a22a-349b-88d4-693b264d440f | -1.63486 | -52.62021 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80eb6a90-0937-3637-8618-bd6bd299f1ce | -0.77156 | -51.75628 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c8e5e19-24d0-3c26-a627-dd815b7c1a03 | -0.93569 | -52.98263 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66fe453e-a03f-3be6-9129-6c10f098a0bf | -1.42882 | -52.28755 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62ca4a1b-f0e7-398c-8536-419405b87786 | -2.09264 | -53.33932 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adfa29b8-6ffe-3c16-8d92-e4096f39090c | -1.61824 | -52.42312 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd84d4e6-533b-3757-9722-32444de26532 | -0.96426 | -51.78264 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eafddfe6-b428-3ccd-981d-101482a21fe2 | -1.65279 | -52.5276 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0770db4-e98e-3557-8fcd-eadf188020bd | -1.08858 | -48.21097 | 2024-11-21 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2bd1c3b-4df8-3fed-905b-22a5341f8c1d | -2.68794 | -46.25324 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c50ae6d8-319c-36cf-bb24-4cb933299f44 | -1.40888 | -54.27337 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f02ee6f6-c7a2-3a1a-8006-396d3f0049f8 | -1.97764 | -53.33567 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cd8f00e-7b41-3392-b9bd-259c9dfc5fce | -1.0872 | -48.21309 | 2024-11-21 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06dc449a-7e9e-3684-9b20-fb3bda517c2d | -0.82717 | -52.87436 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef6c52b2-791d-39fa-98f6-81a06e2786be | -1.57382 | -51.26232 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0dc5473-bef4-3ab1-9e66-12f504065d58 | -1.69673 | -55.09726 | 2024-11-21 04:53:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a336faf3-bc06-3eb8-ad72-4e4cd65e1d9d | -0.89591 | -51.72126 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4714039-381c-3f2e-95cd-a5d23f5717a4 | -1.64389 | -52.69214 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e806fdb-3289-3211-b9ae-afb136a9bf17 | -2.01138 | -54.5241 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6c51e525-a09d-323a-b432-0cd685baefa1 | -0.24951 | -51.03574 | 2024-11-21 04:53:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43ad270b-bbb5-3041-8ab3-c18ecd39402f | -2.2553 | -48.70477 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 279cbdd9-d703-31c5-bf2f-13654b549c46 | -0.95784 | -51.71998 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d9befd2-4f02-3c06-ab0a-a341bbff2564 | -1.78478 | -53.59082 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 659c63e6-fae2-378b-8593-b14c3b5203c9 | -1.20712 | -51.75103 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0451ae91-8a73-30b4-8f76-ecf1530fc5de | -1.38076 | -51.55525 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be7973c6-2740-3a26-976c-837822672736 | -1.79692 | -54.05052 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f219d736-e210-3ac2-9830-0f489a7e32fe | -0.80975 | -51.48991 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README62.md)
