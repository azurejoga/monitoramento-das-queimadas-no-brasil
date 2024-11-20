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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f541614b-50fd-389a-bd32-597e4718800d | -2.67033 | -46.22951 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07c0653a-800f-335d-8216-c65d87a63537 | -0.13561 | -51.6139 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7dc69f8-3263-3661-985c-0e031b1a99b5 | -2.16537 | -48.33757 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c94be77f-35da-3736-baf6-11b76a611688 | -0.13436 | -51.61221 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d66f9841-aae3-392e-b972-2104aa585290 | -2.30451 | -49.01148 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54356716-a8bc-3e1a-b7c0-2482ccb9d48b | -2.65844 | -46.60833 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d2268423-50b6-35e9-bc9a-986bd8bc7b79 | -2.75528 | -45.70731 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bc252137-66af-3626-9f7c-a7d9c59f09c4 | -2.61441 | -48.24751 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e187e358-4c3a-3b4a-bc94-3811ce510332 | -2.54018 | -47.32622 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a32a1ec-d91a-35ab-8a8e-a0930ebbb88f | -2.63149 | -46.5648 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ac0fef0-9eb8-3679-b08d-c60ffec60745 | -2.38431 | -48.93237 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2d27c445-9613-399b-b3db-cf667b33a749 | -2.68565 | -46.19653 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53a619ee-7bd3-39e1-a241-e5bb5360953c | -1.46123 | -46.26028 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe370c74-f940-369a-83f1-c581295877d5 | -2.72595 | -46.06865 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ab94bec-3ed9-3fe9-8682-f64d08cfa94e | -1.4755 | -52.52422 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f32718f-069c-3629-b20a-650767e95361 | -2.09778 | -46.38826 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e06da880-097e-3326-bccc-974e0e890dce | -2.03379 | -48.0919 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c480eff6-95d5-3bba-b949-715ac1c25dd4 | -1.05256 | -51.74347 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f16a31d5-8891-3523-91fb-dfc6ddfb2ec9 | -2.72327 | -46.08586 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 990c88ce-ad11-3178-ad48-eddf1d4a5c29 | -1.85618 | -54.27754 | 2024-11-20 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 88ea1d5d-d011-3735-866b-a82942a19a90 | -1.38855 | -52.41933 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ff7e2e6-df0c-39f8-913a-f443c174d50f | -1.85568 | -54.28072 | 2024-11-20 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3e6c9a5b-e667-33e6-a53a-1f227b510162 | -2.35776 | -48.60909 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b8b8c71-4e1f-3ec1-8ed5-fd2d2ae198b8 | -1.39176 | -52.42904 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92835daa-6ee1-37a1-8294-e86214aab1ad | -2.66072 | -48.48505 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c8b7846-4209-3c4f-8ead-3e191c42a729 | -2.71334 | -46.08433 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7fd5e99-1e36-3705-8091-5e726ea90b34 | -2.27416 | -48.45182 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 318fc5aa-3104-3e5e-b872-664aeda181cd | -2.84752 | -46.68466 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5db57966-8803-31c5-820d-62452b8705da | -2.22848 | -46.6381 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3bed292-4196-3fad-beee-d0430616ddc8 | -2.62063 | -48.18443 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51b5fa04-c6a6-3de1-8a84-37014f773499 | -2.16551 | -48.33764 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9329bb82-3f13-39bc-8153-1e5cbafd2b21 | -2.13919 | -48.56905 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 448cf116-012a-3b4c-b9ff-f31c40d0a621 | -1.31387 | -47.8055 | 2024-11-20 04:25:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e10fe987-07ec-3ef2-b4d8-d76a76474039 | -2.35841 | -48.605 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 859de188-c292-39d8-b603-95a00653ec15 | -2.91735 | -46.84658 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ea88d4b-2f26-3c7d-9df2-32c4fa6bb580 | -1.19959 | -51.98032 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7082fbd6-9a5e-3761-ae4e-00cd95d71dfc | -1.06351 | -52.39493 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22a2d1bf-5771-31e0-b75c-58b918527759 | -2.63107 | -48.48862 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c1bbbaa-7c3c-309d-8b52-818bbb6f90ec | -2.57657 | -46.54557 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 531a4f13-e557-35e7-87aa-dd52a4edd6c3 | -1.13667 | -53.6619 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3642927a-217b-3c6d-8143-10837bfd589d | -1.29871 | -52.24325 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6285b0d4-1a5b-3576-83fe-66b06355bbd3 | -1.24053 | -51.75168 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65d28006-493c-32ea-852e-8f6f0a8df41e | -2.64606 | -46.23284 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73175c38-c63a-3891-8b29-894e0e257e55 | -2.63883 | -46.21404 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef8f524e-1035-357c-9c67-8bbfc30e162e | -1.11525 | -52.39049 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5797c55e-78c3-39ff-a436-4375c4556f94 | -2.68689 | -46.23206 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c98a803-def0-3aab-9066-49593ff3ee74 | -2.74931 | -48.56768 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a079e5b7-5ba7-3a09-bd65-0fc432c0fa82 | -2.63095 | -46.56829 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd648e27-2290-322e-8021-903ffc1cef64 | -2.65643 | -46.5579 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2e68188-fe50-3052-8f31-5a1be37fb6ca | -3.79043 | -41.60788 | 2024-11-20 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e2f04ed9-1967-3ea4-9983-3191a0c56d29 | -1.48407 | -51.9743 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d54ecf78-9b61-3744-82a9-e8643415807b | -0.27688 | -51.39522 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dff304f-1d28-372f-86a8-cdf424312382 | -1.68457 | -52.08729 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5659a891-7a96-3794-9879-10e684699046 | -1.5365 | -54.90091 | 2024-11-20 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95c82890-c715-353f-bf50-d321321cc6df | -0.91501 | -51.78559 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 854f1e10-be71-306f-a13d-6cc2e6f2e4de | -2.69574 | -46.24051 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| de4accc9-6d86-3a09-b3fc-8483d0d7fe84 | -1.5457 | -51.1134 | 2024-11-20 04:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e10349b0-69a8-31b6-85e1-bf82d26bcef3 | -2.25734 | -48.42043 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ba3518c-131d-3e06-8e7e-e02d176078cd | -2.77652 | -48.58017 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a43611-a706-3b1e-9749-36c8d9799342 | -2.41844 | -46.51329 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39dc10dd-2040-38d9-b23a-e07cd0e3a69d | -1.20143 | -53.67832 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 627d47bb-82c7-35ec-9c9b-e21e9a5b3e39 | -2.35417 | -48.60855 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73d82090-08c8-39cf-8131-e2a91918b241 | -2.64052 | -46.2249 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90a90901-0ea9-3c39-9a90-4ca30dc5e953 | -2.92124 | -46.84358 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22a385d7-7c80-3010-9736-3489d292bf4b | -3.59004 | -43.62742 | 2024-11-20 04:25:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d92ea6f-09e1-359b-b6e9-a2c880869844 | -2.72638 | -47.97555 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63e1fb4c-3d59-39d3-845f-78b847f528aa | -2.64377 | -46.20419 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eff99a3-9797-3a18-91c5-cc844ea8e6e2 | -2.67011 | -46.16585 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e64c5f1-f1ca-38eb-8867-a200cd0e35a6 | -2.62587 | -47.96827 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc73ffc9-bc8b-36d2-be08-2ac7d124eef5 | -2.75198 | -45.70681 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77d20045-f625-3bab-bf05-55b3e3052443 | -2.66456 | -46.61285 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 49f27b7f-7fe2-33bf-bb9a-2550409bb6ea | -2.69405 | -46.22964 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9946742-fd99-3f98-84da-b75d81213d45 | -2.81584 | -46.66901 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3605e772-050d-3c37-b10b-faaa99e87d20 | -2.41899 | -48.97612 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0635b2cf-85c6-35f4-a207-0849e8d30b46 | -1.98401 | -48.71133 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60ca02ff-942e-346c-af90-b197111b06c0 | -2.6224 | -47.96774 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40b88db0-8ff4-338a-a9f2-a8e2334da258 | -2.08351 | -48.53555 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d103cdc7-0cd2-3226-8e93-24adbc916205 | -1.31609 | -52.39848 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de0feb40-fc19-3c9a-808c-5a77d9440a74 | -1.33675 | -52.23959 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00f6c7c7-78f3-318a-bc12-016452424878 | -2.13029 | -48.30775 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52a9dc0b-6bc3-3559-9624-863a4f3bbff1 | -2.53082 | -47.52344 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7f1f9d6-c97f-3727-992d-e5fd9e24b0f5 | -2.12341 | -49.11467 | 2024-11-20 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df6907b4-ca4e-3bd2-81c6-86f14d76a267 | -1.28691 | -52.46973 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90ca9122-d50d-34e2-9986-87e9bb5a8699 | -1.60266 | -54.64196 | 2024-11-20 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 62cf118e-1957-3fec-89fd-cf7dec25a0cb | -2.63204 | -46.5613 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb8fb669-78db-3a2e-8356-cf855231bed9 | -1.33293 | -52.23691 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dc137b2-5f9d-3d21-a20d-a44729d9f149 | -2.31429 | -46.84998 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fe1bbe0-1399-3db0-8f0b-2a6efbce0881 | -2.08645 | -47.06741 | 2024-11-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e4b5b18-50c4-3747-8923-d15aee26a50a | -2.26638 | -48.40949 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93d1a5b6-9e4d-39c3-88ec-a3350dc6a4e9 | -2.57879 | -46.55307 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be70aa49-5edd-32c9-bc4d-f62c559ce5f9 | -2.66208 | -46.23885 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ad15a65-49c6-31f4-ab28-a2f175a72b58 | -2.56174 | -47.28471 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63f22886-262d-3f69-8ed9-7adbe843e77a | -3.07436 | -45.84174 | 2024-11-20 04:25:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c17844b1-204d-3d45-bdff-3eebb33dafdc | -1.13623 | -53.66466 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84423b1b-4ce8-3629-a9eb-c1574b6007cd | -2.22028 | -46.47551 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01f8a1ae-bd36-3dbf-a819-84102527c65b | -0.08106 | -51.46718 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9d1105c4-6c86-3365-87d7-20440770428f | -2.18054 | -49.13071 | 2024-11-20 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aad02da1-075b-33fc-8399-a6b82a22c583 | -2.72308 | -49.35183 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8bb0d2ef-7965-3d74-9485-1b154f200958 | -2.54502 | -46.33418 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3247270-5453-33f3-9de1-9e038d7d2e28 | -2.54235 | -48.18032 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
