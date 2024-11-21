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
| f3e9e73c-aebf-3d7b-9361-9866b3758d89 | -6.30284 | -45.33822 | 2024-11-21 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 757787ce-76e6-3892-8d9e-06c150a026b4 | -6.71605 | -35.40929 | 2024-11-21 04:08:00 | NOAA-21 | DUAS ESTRADAS | PARAÍBA | Brasil | 2505808 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1418ed3f-fefe-3ca3-bbd2-202c117afaf2 | -2.14762 | -53.56939 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d1df2da-760b-3132-b6ee-bc24b2456325 | -1.97445 | -46.36512 | 2024-11-21 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7674d359-76bf-39dc-b760-158880cc3612 | -0.77751 | -51.7671 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c8b65a5f-f55d-34a0-b271-b7d41683cfe3 | -2.95893 | -49.5433 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cac4ec50-ca6e-3dd0-9eb4-db087eec3a79 | -5.19793 | -44.2218 | 2024-11-21 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a779f50e-72fc-396b-9c27-6032f46d4cc2 | -1.96428 | -48.38484 | 2024-11-21 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72fba0b6-f45d-321e-a8d4-1c26248ab2d4 | -3.10317 | -49.4498 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c3a3331-a545-3eb5-ace3-0546fa9be63c | -3.45939 | -52.72677 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae2f9306-1e99-339a-8442-69cce5146f38 | -5.5875 | -46.3698 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 391dbb93-f4f5-3410-895e-79b68c341e6f | -2.24406 | -46.85625 | 2024-11-21 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0977d5ca-5f0d-3d0d-9db1-a181f1081dd3 | -3.34068 | -50.49545 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41fa4631-ecf7-3d37-b988-436ccd346bec | -2.69711 | -46.22409 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d47e8b62-c9c1-3397-a3e6-dffe42ac4687 | -3.0376 | -49.46713 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e76e4570-3b0e-33f6-aa56-815a3c346a5f | -4.96672 | -45.51915 | 2024-11-21 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 878d313d-9602-3a07-8ed3-6760e5b67773 | -2.36947 | -53.83487 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 33f9a428-fd04-36ff-9213-b8f26c1d0c1f | -4.62943 | -49.54649 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9f461e3-f296-36f5-ae61-23322da76f83 | -0.95528 | -51.72055 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05a9afd3-b65e-32f3-a47c-a95829c5a915 | -3.03711 | -49.47007 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ed3f4f50-a95a-30da-b33a-9975890fefbe | -2.6742 | -46.23542 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff0268d2-4b49-3848-8279-9ac15b3c831b | -3.77094 | -50.70419 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84aa5dac-15e7-3185-a4d3-6970c05224c7 | -3.28661 | -53.82587 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a23e6b39-e2b3-3c7e-8e1e-8ad26ac58962 | -2.63999 | -45.76768 | 2024-11-21 04:08:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94f126ca-9387-3211-86d3-d021c3c2c17f | -2.6882 | -46.25283 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3828dd4-d533-32b4-8c35-90c2c4be16fb | -1.19917 | -51.76816 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ebdbff-28f3-3cf5-b2d3-645ad02f5d95 | -4.12884 | -49.43285 | 2024-11-21 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2598c0a0-e064-3edd-8af1-03cbd30929ed | -2.79994 | -51.76958 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eaef857b-c4fb-3ec5-91a7-1cdd423ba265 | -2.36703 | -53.83957 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f0f62e5a-216f-3014-9dce-8377867b3054 | -1.23348 | -46.74429 | 2024-11-21 04:08:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 853c6fea-ffbd-3bc4-bc9d-0ab4d3c773b0 | -3.28027 | -50.52219 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4af8ddbf-156b-3559-820b-c064e271b971 | -4.60967 | -45.74322 | 2024-11-21 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3017cdae-13d1-3e89-a1cf-af48211d4066 | -1.65875 | -45.74616 | 2024-11-21 04:08:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11bf4a0c-fb2b-324c-ba5b-add35fb0090b | -2.25734 | -48.70189 | 2024-11-21 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 30b350ae-44ea-36b0-afb5-4a3fbed28b66 | -0.94775 | -51.7242 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 682ef5a4-30a2-3f93-87a5-135bb04934e7 | -4.38744 | -47.7594 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 39d402cb-6d7b-3fe8-8ea8-68280a29e48f | -3.69852 | -51.27802 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89ad58a9-4049-3065-a732-731aff941225 | -3.66142 | -51.5757 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f801274e-4e56-350e-8c33-ac2499f47e4d | -1.62128 | -52.59362 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50dca122-975b-3bc6-817d-cd636e150533 | -3.59787 | -43.63317 | 2024-11-21 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79900d65-738d-342c-abce-8f16de88108f | -3.29491 | -53.85773 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f0f3c846-2b00-3187-88de-a4f1e5d37d6f | -2.67368 | -46.16428 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d7c39d5-5e58-3398-909a-bd6fb814acfa | -1.74985 | -52.06062 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a3bca80-c4d4-36ba-9d77-0aac28df50f2 | -3.28492 | -45.97518 | 2024-11-21 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7af23284-97c4-3581-bc9f-9cb84995ff8e | -2.75501 | -52.11323 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 26df7bd0-679b-3efa-9f99-c65e6fc7ef94 | -3.80469 | -51.26559 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aeeda94-cf7c-3ff5-b094-b4e537ae235d | -4.7537 | -44.34451 | 2024-11-21 04:08:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10eb89e3-da68-3caa-8cbe-0863afcb6851 | -2.67394 | -51.88248 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f687200-671c-37e9-8a20-00009e85af8c | -3.81345 | -52.34553 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ffa34536-5dad-3283-a936-dba2f26ff616 | -2.9355 | -48.33478 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7800f49-839e-3242-bf67-7a4cd3480f0f | -4.63491 | -49.54445 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37e5f820-b5c4-3dda-9961-e1cec59941b1 | -1.3925 | -46.5088 | 2024-11-21 04:08:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7cb7835-4ed1-3474-b422-babff0265593 | -3.81012 | -52.36446 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 59937c09-ab5c-3151-a41a-c309fe103efc | -3.69503 | -51.27689 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51f94471-a0c7-3de8-8f87-f6eabd6f4948 | -4.629 | -49.54774 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86e4437c-a5ed-3817-823c-5c1fbe9a9628 | -3.23426 | -45.57026 | 2024-11-21 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77bfcba8-6a2d-3ecb-ad10-fb1750347089 | -3.03661 | -49.47303 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1990165d-307e-33e7-baaa-b583e3099dbd | -2.64795 | -46.14162 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d53738a-08a6-3f84-bb63-768e1ab890af | -5.00638 | -44.79945 | 2024-11-21 04:08:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38bd52a7-3fee-3ac1-bd3a-ee06bb68d4ce | -4.92332 | -42.04208 | 2024-11-21 04:08:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4dbe5fb6-5865-3630-bd88-56d142cc8472 | -1.39381 | -53.58311 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 770c8a62-4d3b-360e-833c-2073ee9091b7 | -3.59088 | -43.63203 | 2024-11-21 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92a4f0c2-bc88-3029-82ca-03c11e4081dc | -3.80942 | -47.79351 | 2024-11-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ba06cd4-9ff6-36db-8c6b-cd014099dff6 | -5.24045 | -42.6409 | 2024-11-21 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0785c89-41f1-352c-9192-a2cf8edd7644 | -4.41873 | -48.85265 | 2024-11-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f376bb0-8800-3f21-8584-8162db040c29 | -2.21093 | -53.7196 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c0b0b9ec-2bcf-35ad-b3c7-c4983b87c9e4 | -1.6497 | -46.9644 | 2024-11-21 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47961ffb-960b-39f1-93da-c26e02e7f834 | -2.62823 | -47.96577 | 2024-11-21 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 232c0f24-618f-3b9b-b448-eea97e9fb581 | -4.05877 | -50.60899 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f360d247-97f4-39c8-8ec0-5c7dc401971d | -4.38576 | -47.77451 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e0b68c22-a4e0-33ba-944f-6363e183973e | -3.95718 | -46.90548 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a71831cd-8e19-3a7f-b8f0-d937d8603367 | -4.92601 | -47.13925 | 2024-11-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4376a61-f6fb-3e21-b64a-9c35c3ca95fb | -2.68881 | -46.24913 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c242dc2-7887-3a06-a5af-300d91587409 | -2.17805 | -52.13553 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5e976906-c5dd-3614-8c55-595b61a2a832 | -1.05763 | -51.74864 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82bb4499-eea6-3e76-a9ce-0633574f00ff | -4.10861 | -46.91003 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1753297-0574-3d36-b6cc-1201b19c87fb | -6.18551 | -43.41245 | 2024-11-21 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c777db52-17ed-3a75-8ff5-dca6382a0bdb | -2.67799 | -46.24382 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d63335c3-8bed-34ee-956a-809246951b5a | -3.10459 | -50.20193 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2eab498-c83d-3280-9f8a-c20e262b9d17 | -3.09806 | -49.4491 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ec4385f-4bd7-3a3d-a2dc-d6c82296f22b | -2.54242 | -48.18024 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57f5002d-16ba-3893-9cc4-2a1a9ff333c0 | -4.15017 | -43.88067 | 2024-11-21 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 83d2c8e5-fc10-3aff-b057-962719014732 | -1.22717 | -51.79203 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66b946d0-6e4f-37e9-9268-b24a86bde7b8 | -1.04618 | -51.7421 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 831a335d-1c0b-33d7-8094-0764213d53ef | -3.01014 | -51.01437 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9776ffd-be28-3977-bcb7-4e543567749c | -3.27646 | -48.80293 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36b4849d-35f5-3c05-acdf-96b8205869b7 | -2.85226 | -46.68277 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20068920-26f5-3b6d-9e0f-5b6bcc32a8f3 | -5.61845 | -46.74814 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb45f37f-d652-3ff9-8688-ef898124473a | -3.67265 | -45.2403 | 2024-11-21 04:08:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf3a85d5-e2b2-3095-b93e-3e54c511b1e9 | -4.99705 | -45.28931 | 2024-11-21 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc9d461a-a9e0-3266-a09f-0da22fee31c0 | -2.09006 | -46.32003 | 2024-11-21 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 791f32cb-6f06-3ad2-a98b-bc4ad939e1c3 | -3.26893 | -50.62194 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5319b57-ee9a-3184-930c-5986184b0465 | -3.49987 | -48.22123 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 737cbdd0-616e-37ef-a8d5-455f44a5e157 | -2.69292 | -46.24978 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1c9fc08-a7cd-389c-9c41-2e949fbb419d | -4.4419 | -46.5375 | 2024-11-21 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 819bdf76-9a41-3898-b0d1-4d1171c730ca | -3.29008 | -49.18835 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1068bd41-c957-3b3c-9635-4733e99ff6c6 | -3.00858 | -51.305 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0e3db9f1-715e-3d1f-b871-7892949dc3b6 | -4.24835 | -40.63579 | 2024-11-21 04:08:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9af6fe7a-88e4-32dd-b8fc-0884f97fba51 | -3.61949 | -51.09086 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ba3e0f60-4580-308d-9485-0cddf78a5a34 | -2.94546 | -45.19564 | 2024-11-21 04:08:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README21.md)
