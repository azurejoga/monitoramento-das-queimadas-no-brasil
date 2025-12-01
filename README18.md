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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40e9b586-2f3d-3050-999c-be4d48462156 | -2.93956 | -53.28812 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e0672db-5a03-3d74-afb9-3a548eb5039c | -3.21217 | -50.12885 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e3ff767c-2fdb-3558-9d42-14053e34036d | -3.23774 | -50.05848 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29704e59-6472-3ffd-8cf3-96aa1c412c17 | -3.69314 | -50.62386 | 2025-12-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54752e02-b523-341b-8bb2-5b2107110609 | -2.94288 | -53.28114 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c20dc8a-c130-3a6c-b275-7a8b837a0a5d | -2.24437 | -45.61731 | 2025-12-01 05:16:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41498cb8-8972-3e4c-8a4e-5e074a985009 | -2.73828 | -45.21653 | 2025-12-01 05:16:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5eb73269-e230-3d87-ac95-05861ea2cf63 | -2.93886 | -53.28066 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 438a15ee-bbb8-3eb8-b0f7-168508da69d0 | -3.23122 | -50.67002 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fc6020c-8165-3292-9873-f232b676e2aa | -3.70857 | -50.6536 | 2025-12-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0860e96-1b50-3575-92b6-0403be858a7e | -2.9366 | -53.2809 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90f9fb4a-0c7c-3961-9de8-3d238280d1d7 | -3.26263 | -48.5698 | 2025-12-01 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 299f59ed-784e-35a8-9cc1-d64fcaba337e | -3.23632 | -50.66782 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36e9935f-a3b6-3fa3-a408-0d8399cec7ae | -0.99206 | -53.20365 | 2025-12-01 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8b26d32-ed09-3075-85fd-0c2da9003e8b | -3.23153 | -50.66708 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cf2b093-8960-3dc2-92a2-aec5194ad35d | -3.25723 | -50.69233 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19677a83-2c1d-3883-b79f-3ba14e2af65d | -0.99085 | -53.20693 | 2025-12-01 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbddfd84-f71b-3138-a65d-8e7487922ae0 | -0.65213 | -52.36433 | 2025-12-01 05:16:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da230f6e-bda2-36fb-aa89-e6ef8840ce9d | -3.50769 | -50.55478 | 2025-12-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 141e2cc8-6eba-3d8e-97f8-91bb6cda991e | -2.94009 | -53.28476 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb40e136-caa3-3801-83c6-6e4e9736482c | -3.24028 | -50.24768 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f1ebec7-0633-3a6c-9fcb-7a2bd4b80c6c | -3.69391 | -50.61859 | 2025-12-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 692a95fc-6f27-3aea-8129-c188ed6c19bd | -2.39343 | -47.60902 | 2025-12-01 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f07d8c33-baa0-3132-ab15-43b991254520 | -2.73589 | -45.22029 | 2025-12-01 05:16:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 82354944-8324-3f35-a89f-a42cf1469c89 | -3.23534 | -50.24701 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d3cc4ac-80e4-30ba-9650-0785e85b0236 | -3.21631 | -50.13533 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| adb03d0d-7fc7-3145-807e-52b6c3019f7a | -2.93418 | -53.27013 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ab75a6-c968-3f81-9f7b-59f7e6c45bb0 | -2.73681 | -45.21419 | 2025-12-01 05:16:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3606df13-b797-3fe7-92fc-06669ac873ef | -0.83456 | -52.34151 | 2025-12-01 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8da1d68-ed0a-32c0-88a8-605d238cdb8a | -3.57939 | -50.27456 | 2025-12-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87e1fb78-4424-3671-ba3e-7550ec59b847 | -2.93557 | -53.28754 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d79160d9-dded-3436-99f7-a1b43b4939f2 | -2.2638 | -51.88986 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95da27d2-8ae2-3dbd-a921-64cc75fb08ec | -2.93072 | -53.26607 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cf0af40-5efe-3097-abe1-9272b4a1f184 | -3.23601 | -50.67077 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7081f4a0-72c7-3566-ab39-fa7944d0d5ea | -2.24993 | -45.61496 | 2025-12-01 05:16:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebcf802f-9c4d-3048-aef8-ead2f3be311b | -3.21126 | -50.12867 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00ad8e91-3757-3a64-a6b1-1f243eb12ea8 | -3.17552 | -50.31167 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8992a8f9-2d13-3eeb-8247-f088b1c94b82 | -3.60406 | -47.26722 | 2025-12-01 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c95c18b6-ac25-3bfb-8ac9-792f334775f0 | -3.11581 | -54.17359 | 2025-12-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94ab3c22-c247-38b8-aff5-031b621b7ad7 | -2.31697 | -53.85097 | 2025-12-01 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0b33bd50-0baa-3f33-8e62-0e7d7177ad57 | -2.93837 | -53.28399 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 83dbb413-ace7-3d1b-9987-cefeebb39529 | -3.59735 | -47.27101 | 2025-12-01 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8252eb94-ad67-3c65-8276-f93957b6a8c6 | -2.93712 | -53.27756 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 257a83f1-811e-36c9-a483-20297f446b1b | -0.99162 | -53.20204 | 2025-12-01 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50b1ad6f-a851-3591-b8d6-45fd18db5436 | -3.60249 | -47.26681 | 2025-12-01 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56be27ce-4766-3b0b-b349-2dce1e9f3bca | -3.22593 | -50.56971 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80834d47-ba5d-3b1b-bddd-03d09d804df3 | -2.04423 | -52.10287 | 2025-12-01 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cfbc0e20-6c17-30ee-904b-b4b63cebd5f8 | -3.11202 | -54.17303 | 2025-12-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 983473f2-eae3-32b9-98e5-1265acad966b | -2.25095 | -45.61831 | 2025-12-01 05:16:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 15675d86-d4bd-3918-bc8f-c479f85dfe4d | -3.35881 | -50.49821 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4bedd16-03aa-3491-bbdd-91e02eb8c2ac | -1.88786 | -48.40155 | 2025-12-01 05:16:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 649b1009-d1cd-397e-9c07-5fb624dca843 | -3.6243 | -50.62914 | 2025-12-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b4dd2fe2-95ad-3cb5-ad63-e310554887fd | -3.44047 | -54.63745 | 2025-12-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afc6b04d-1b80-34c2-8a7b-73cbc5837de6 | -2.22478 | -53.64547 | 2025-12-01 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb7b8e54-410e-3b36-b906-65bd1f319144 | -2.34331 | -53.79925 | 2025-12-01 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abcd72a4-bf72-3b18-8443-c93e76df171d | -2.8277 | -52.36152 | 2025-12-01 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80875819-d939-3438-a8e2-a72642fdad3e | -2.65117 | -50.00247 | 2025-12-01 05:16:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c743bef-99d9-3359-8148-e671dd4fd37d | -2.04364 | -52.10682 | 2025-12-01 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e0b1ff97-2ff8-30bf-995b-2add606f3689 | -3.22517 | -50.57501 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f03d7416-5702-376e-8cb7-89383ab10940 | -2.31639 | -53.84797 | 2025-12-01 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| edb504db-44dc-36ba-b19b-1cd46b7a14b4 | -3.21039 | -50.1344 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 882d74dc-fd55-325e-899e-94d8231f40de | -3.60185 | -47.27115 | 2025-12-01 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25327ba9-dbbf-3b86-bce5-f821d1f5327a | -3.7134 | -50.65433 | 2025-12-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d6b67a01-02a8-3940-90c4-f04c247ee2a5 | -3.28685 | -49.89952 | 2025-12-01 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf62ee0a-140f-312e-9ff9-09b42c4c35eb | -2.3876 | -47.60819 | 2025-12-01 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8239bbe6-e1d5-3842-bd03-fefd39196739 | -3.21051 | -50.14027 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 6632185e-f250-3f14-8f64-703b0a830cfb | -2.26444 | -51.88571 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e34df6db-0841-3c17-a4f7-a0db5bccf901 | -3.26209 | -48.57347 | 2025-12-01 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe4e55a4-0737-3ccd-9478-be2806ebbd7d | -3.10823 | -54.17247 | 2025-12-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71eb6e12-d616-32d5-928a-a278128f4bef | -2.04849 | -52.10355 | 2025-12-01 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3036631b-b52a-38ef-89df-1c8de6f0e34b | -2.44926 | -47.08252 | 2025-12-01 05:16:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d82b79a4-18f8-30cf-9119-d1e67deb9dc3 | -2.0479 | -52.10749 | 2025-12-01 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a2f0398-fe5c-3c4e-99c1-1e2dedb45dc7 | -2.93788 | -53.28731 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0271c46-d4fe-3c1f-be81-bb87bed1da94 | -3.47661 | -51.36676 | 2025-12-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f7302604-87d2-3d52-8268-80a4334cbdb6 | -2.73126 | -53.20638 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b16319b0-b378-38ff-8d9a-5318f14af258 | -2.93608 | -53.28421 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bed2437-954c-38f5-8221-bbf3e3d7d5e0 | -2.93365 | -53.27353 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8699585f-5e58-32e0-9bae-be78aabd7a4f | -3.21549 | -50.141 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 12e43033-a708-33d3-952b-c6a0de1d1cf6 | -3.20951 | -50.14009 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cb3588b-332d-3625-9c5c-63485dcc5615 | -3.11132 | -54.17759 | 2025-12-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41eca76c-d867-3b0a-9735-ad748bbdf6db | -2.6462 | -50.00167 | 2025-12-01 05:16:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bad658a8-c254-3464-a865-7c7e9dffae5c | -3.44873 | -50.55114 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbc23a44-fcdb-32eb-a0e5-8577855a997b | -2.44325 | -47.08151 | 2025-12-01 05:16:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a337844-a3fa-3d6f-975a-4a53450f6f9c | -3.59574 | -47.27064 | 2025-12-01 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f4c76b2e-2d51-3801-87b2-76a69529b0c6 | -2.98635 | -52.62918 | 2025-12-01 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f26956d-95ab-30af-b25e-a72eb1d8ac8c | -2.99249 | -50.49752 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12368d00-1b77-3870-a53b-ab86fc84c683 | -2.93764 | -53.27417 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ffa1cd6-552a-312c-a757-05f0f45942cc | -2.24911 | -45.62062 | 2025-12-01 05:16:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9a003dc-0c7f-3f0f-8fc4-305c3f6a9f4a | -2.94237 | -53.28453 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3313e96b-bcc0-3ba7-a687-76325fd35f4a | -3.2532 | -50.68644 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf53aa61-7518-3c79-b440-6915b3199b4a | -2.39318 | -47.60845 | 2025-12-01 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eda500fb-cd96-33fa-8385-e699b4dd8519 | -3.2919 | -49.90039 | 2025-12-01 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67f0a868-1ab6-30a1-b650-699b7115c8bf | -2.31567 | -53.85274 | 2025-12-01 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11fdd435-2da0-305c-8484-658a4a3549d6 | -11.36163 | -54.34892 | 2025-12-01 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8170edc0-3fac-3ee5-ae47-2ec1db150d42 | -11.35377 | -54.34362 | 2025-12-01 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ead3253-5830-3da7-9a5a-2fc0eacc244f | -11.36217 | -54.34497 | 2025-12-01 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6455e22e-c8da-3a85-a281-bf86af4a2a7b | -11.35744 | -54.34825 | 2025-12-01 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c684816-3547-362d-8beb-dfc35d9191d5 | -11.35797 | -54.3443 | 2025-12-01 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e147948f-e9c6-3f9c-b4b4-ec5ca35561fb | -4.3703 | -43.1508 | 2025-12-01 05:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9557d53a-5bf3-3faa-8f10-4100d69a5b8a | -5.3396 | -43.5768 | 2025-12-01 05:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |


[Clique aqui para ver as próximas entradas](README19.md)
