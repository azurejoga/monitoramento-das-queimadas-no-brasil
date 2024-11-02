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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9da55e7-7d7b-3839-a8a8-c1df8db3a631 | -2.91427 | -52.59752 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 050b2a75-3931-3e1d-8652-7962c50d2f23 | -2.91079 | -52.59697 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0f2d135-a499-36fe-930a-a35a318a237c | -2.88 | -52.89087 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb0a361f-708b-373c-b219-9dd3f25de82e | -2.87942 | -52.89464 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c64d4a6-1172-3bab-9710-4349d1a0cae4 | -2.87657 | -52.89034 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d7e4c5c-5c10-35c0-8c85-1aa36b312583 | -2.87599 | -52.8941 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 186f5b48-bb4a-3a56-84c4-e7554c1978f7 | -2.87313 | -52.88982 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45e93ca6-a909-3d29-b60e-eb5819ded11f | -2.87256 | -52.89356 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b30ac0b6-285a-30f4-b3b6-d8a20a8fb3a2 | -2.85417 | -52.41919 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a312d703-624a-3574-8e7b-cfddc70040c2 | -2.85067 | -52.41864 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db637e97-5e9d-3f09-9cf6-5789a0a75b60 | -2.84278 | -52.88126 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e306afe8-a41a-38e8-b924-768f5c831f9a | -2.84116 | -52.87033 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 648f433e-ecee-3ab8-af32-49fdad268f95 | -2.84057 | -52.87411 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8d371654-e6b8-3edb-828e-4156375806d5 | -2.84049 | -52.8732 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f83fed5-796e-3a45-ba45-e534721dc4c0 | -2.83998 | -52.87788 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| edc81c13-d976-3874-8122-94a265ac4edd | -2.83991 | -52.87697 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 474ca50c-fed7-39d6-8fbe-af8b834fa7c9 | -2.83939 | -52.88163 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d1ff0cd-57e1-322d-be57-e262f0e2d67d | -2.83934 | -52.88073 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2979db7a-dbcd-3b34-9d04-c683b9f42192 | -2.83772 | -52.86982 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b47eb3c-5b5a-302a-ac65-587d3ad5f003 | -2.83713 | -52.87359 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| caf09b4f-4710-3fff-8643-d9a66f5b1881 | -2.83654 | -52.87735 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 18dc4379-816f-3c5a-95f6-b52ff5142240 | -2.83596 | -52.8811 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70b35491-798b-315a-9cb7-c35525493545 | -2.83369 | -52.87305 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c80a164c-44c5-3949-9b3b-1b39d1317920 | -2.83311 | -52.87681 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| daa94fbf-3c45-3439-b5fc-901284fca6cd | -2.82809 | -53.0009 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a88a5ca-d76b-3637-bb74-fb5dff3d8cbb | -2.82752 | -53.00467 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70746cf4-1e3b-362c-b311-124b56d25a54 | -2.81457 | -52.99581 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b49e679c-cdbc-3105-b953-c21ccbb8fc47 | -2.81399 | -52.99956 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d134646-2afc-313e-9e1d-59034dda52bb | -2.81115 | -52.9953 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| faf798ae-622a-32dc-b2ab-2734b53a9b06 | -2.80773 | -52.99478 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 346c3674-97c5-3bab-96ee-de15c8d42ef8 | -2.80714 | -52.99855 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a7f4351-223a-3477-933a-ffc39c853641 | -2.8043 | -52.99426 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85c3cd63-dee4-3b29-9853-8be0662f03b9 | -2.78443 | -52.89598 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6cf32a1-21fb-37a5-8fdb-cfbb92075043 | -2.78386 | -52.89972 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db8a1f8f-8e9f-34f1-83b1-0c4c07018334 | -2.78099 | -52.89552 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6367353d-418b-35fc-a2b7-fcd3f92e0b3b | -2.78042 | -52.89924 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5fe207d9-81a8-3702-8a74-8dbadaebfd71 | -2.77698 | -52.89874 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e7f6d1f-836b-3da8-9640-b532dbf86716 | -3.5168 | -52.94699 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a83df34-37fa-3da3-a39c-6502f3588fc5 | -3.51336 | -53.01565 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c72f3cfe-0e0d-3ba5-a03b-f0f9c9ffba10 | -3.51049 | -53.01138 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bcaffd23-9329-3367-b44d-b937aae47077 | -3.50992 | -53.0151 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43da3529-72d1-3598-ac15-ab801110f5da | -3.41677 | -52.72626 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f04c8bc-e002-30ab-b055-59a7462eda8d | -3.31927 | -52.72322 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71a72bf0-da7f-32ae-a630-df18cead1ff1 | -3.3163 | -52.85907 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7b56ab0f-2d5e-30dc-967d-7cf4613e6a26 | -3.31572 | -52.86285 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6a4561b6-5e87-33a0-b2be-0e6555cc8bd8 | -3.3007 | -53.12112 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e93fcb44-e8be-31da-8d5b-0464c04a368e | -3.29729 | -53.12059 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 199864ea-27d2-3232-aaf7-b839f4753994 | -3.2933 | -53.12376 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 79193cb5-441b-3d8b-bd62-bb893d225542 | -3.28988 | -53.12323 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28fd6006-02ac-319b-9e58-3b27fba0d238 | -3.27442 | -52.81482 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1677097e-139f-3929-b6e6-f1ccc1900a3b | -3.25621 | -53.0686 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 960bb89a-92fd-3e2d-8411-84c8bfc19503 | -3.25564 | -53.07232 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07c2250b-eb4b-3d72-884d-354cbd3b92e5 | -3.25278 | -53.06807 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 81eedabf-3cc0-30e0-b6c4-541afd280abc | -3.25222 | -53.07178 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec86cd1c-13a2-316c-a5de-edf187db4455 | -3.24936 | -53.06752 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aff4241a-3dc3-3265-bee2-312d4e3a7a63 | -3.24823 | -53.07495 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9aa926e0-5d9a-382a-9fa9-8970520c548b | -3.05588 | -53.6451 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 619de846-3f7f-30ea-9e44-a1a00c1eb77b | -3.00967 | -53.44015 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfde5359-182a-34f2-814f-cebfb66d909d | -3.00912 | -53.44374 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 734e4335-85b6-3653-8c7e-f6a3e19449e7 | -3.00856 | -53.44733 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe6a102e-2bf6-39b3-8902-699c100bef6a | -3.00629 | -53.43964 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67d153c2-a8e2-3cf3-b8fc-be452671a1fc | -3.00574 | -53.44323 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74dcba9c-3826-3884-9306-84d3248aeaf2 | -3.00519 | -53.44682 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27b92eae-eebb-3d48-a818-d54efa0dffb6 | -3.00236 | -53.44272 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f3d427a2-2bb3-3407-be93-32842613bdfb | -3.00181 | -53.44631 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e92a685-c4f9-3e90-bb94-240997e6eb0e | -2.99333 | -53.43403 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77e4331d-92a5-327a-ab0d-d28c7037695e | -2.98995 | -53.43351 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9678750b-fe96-395e-bece-a3dab53d6c06 | -2.13504 | -53.28843 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f4521bd-17c0-3149-b437-5171c47a9a76 | -2.13167 | -53.2879 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9acc75e0-0a39-3412-9f2e-bc251a5b8374 | -2.1175 | -53.42499 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e161573-62ff-3a5c-b6d3-33a847cf4cc5 | -2.11695 | -53.42855 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb800217-96d2-3558-aae0-2d309ebb4264 | -2.11359 | -53.42803 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24800f27-5fe7-3ad9-b2be-16d965f3692c | -2.09376 | -53.23092 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7c31af1-8b0e-3ae7-b446-23d804927bf5 | -3.73624 | -53.7343 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc5e0635-5409-354f-816a-9bab99fe08db | -3.73188 | -53.78495 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26055fe8-d435-39e6-b7e5-22ca81cd3c75 | -3.71323 | -53.72712 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a27e728-7dde-314d-97d0-e424ef3c9ec7 | -3.71275 | -53.7527 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed43da99-2881-38d7-bde5-00eca00111de | -3.65672 | -53.63427 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0731e373-85f5-344a-8352-981689cbd5f4 | -3.65335 | -53.63373 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28b6e090-7d06-36e4-aba9-a866195d3675 | -3.73324 | -53.38626 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b139328f-acad-3001-8949-69174454d125 | -3.73268 | -53.3899 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec28922a-03a0-3cf8-b7fe-f47c68354629 | -3.72247 | -53.38837 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 230d72a4-6897-381d-aac5-48dea8c8f82e | -3.71907 | -53.38786 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c5081a7-5e21-37e4-96fe-fdb04cb568f2 | -3.71625 | -53.38364 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44e0211f-2bed-3fa1-a75f-149a24589b41 | -3.81442 | -52.347 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed95135e-fafa-385e-8149-6788a3ea50b1 | -3.79823 | -52.31215 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d9e4033-dc71-3843-8bed-c0b85731cdd8 | -3.79796 | -52.31139 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ffcf2cd-169c-30c4-bb39-37846c802c6f | -3.79532 | -52.30748 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cb70955-222a-3bb1-975e-b01d5deda224 | -3.78529 | -52.30176 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd754214-b5d3-35cd-ba59-a45ce980a9c8 | -3.77736 | -52.42338 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b041c5d6-1048-3524-9200-66b85ddb18d4 | -3.77706 | -52.42679 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1410023-9692-3e78-911c-306d0de91b9a | -3.77674 | -52.42735 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a08e0c3f-53a6-367e-8409-b8068be8a774 | -3.76737 | -52.4178 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7282b35b-f4b1-351d-80f2-e15927739d66 | -3.75493 | -52.4281 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 009aa399-fbeb-34fc-9c01-0dcccb0bc1b6 | -3.75056 | -52.36221 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c1a2001-cf42-3af1-ae34-6c80a1bc7526 | -3.74702 | -52.36165 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 283d4a38-d882-3560-8c27-15a2f3ac63e5 | -3.71253 | -52.42166 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3166d26c-a15a-3b2a-b462-3f960ea7449e | -3.71193 | -52.42562 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d255309-5d6a-383f-b3b7-c2f166024548 | -3.709 | -52.42109 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7920a839-9877-308d-909d-febf3c2c4bca | -3.7084 | -52.42507 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README77.md)
