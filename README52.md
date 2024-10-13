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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62621b83-5fe7-30db-bed0-4f5f96de2465 | -3.93296 | -46.43318 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| bca3f867-3b0b-329f-a472-95bd08591f6b | -3.92839 | -46.41652 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fe88eea-206b-3414-86c5-8277ab404fb9 | -3.89343 | -46.45869 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a64c568f-5f8b-3b9a-af81-b72cb4ed155d | -3.88995 | -46.45816 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7499c4c6-c82e-37e2-a014-8e1c8f278cbb | -3.87957 | -47.52372 | 2024-10-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e05cda5f-54e9-3a84-b4a7-d1ba49f1709b | -3.86329 | -46.46972 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4767b842-c7ac-3ddb-af60-6bdf87745ab4 | -3.86116 | -46.46979 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2d8afcf-13fe-3a9a-96db-8f0ba42f5834 | -3.85982 | -46.46918 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bbf3cb3-1d6f-3271-8e02-873e8c99e47d | -3.85147 | -46.91505 | 2024-10-13 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0301e20e-9839-3b48-84d9-6a32cb631938 | -3.8509 | -46.91871 | 2024-10-13 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f91a48a9-7b5b-3403-bd12-84dcb82ef9f6 | -3.83914 | -46.47416 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b31d09be-6998-309d-b463-f198116d082c | -3.73551 | -47.32952 | 2024-10-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f9c1aa5-ecd3-36d3-8c61-50ccb1a5f114 | -3.73214 | -47.329 | 2024-10-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f36c2221-4a55-3067-bf4f-463f01c436d3 | -3.609 | -47.51099 | 2024-10-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbd17cba-345a-378e-bf7f-2e021ae04d70 | -3.60846 | -47.51453 | 2024-10-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94d412c3-28e1-346a-b13b-e598d285d13c | -3.60511 | -47.51402 | 2024-10-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebc01673-0999-3fc4-ae1c-365bf0457484 | -1.15948 | -47.22926 | 2024-10-13 04:38:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f149a68c-d0a0-35d6-95ce-c35451ae2e03 | -1.0997 | -48.06481 | 2024-10-13 04:38:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f64273d7-0855-32d7-b333-edf6399cd86e | -1.05417 | -47.92446 | 2024-10-13 04:38:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8c81f9f1-c0f8-3621-9bb8-565f755d018a | -1.05364 | -47.92788 | 2024-10-13 04:38:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 522898fc-b060-34f2-89f3-a47b96c49b2b | -1.05088 | -47.92394 | 2024-10-13 04:38:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b46bb210-03a8-3270-8145-29def40f8cf5 | -1.05034 | -47.92737 | 2024-10-13 04:38:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 54c5e260-e1e0-3036-9c44-db995902a81f | -2.09559 | -48.53026 | 2024-10-13 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2e00cb0-f058-3afe-96cb-56796696d676 | -2.0586 | -48.6368 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6212de8c-ae00-3059-a06e-cb1523396616 | -1.78152 | -47.84155 | 2024-10-13 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eed5a013-abe2-30ad-9421-84b0ea7e287f | -2.1818 | -48.8252 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ab0253f-ed58-3310-bcc8-9dfc84dcacad | -2.17459 | -48.80651 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f220c2e4-d5ba-3e0e-ae1e-6e9d98516b33 | -2.17129 | -48.806 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4123444-c8aa-311b-acb8-edbaa2a43726 | -2.17075 | -48.80943 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a78d9ab-03d6-38d0-81c1-64b59b46c06a | -2.16746 | -48.80892 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3d52d398-d03f-3110-a382-beb09cb699e5 | -2.16692 | -48.81236 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f2ee4dfd-d0c8-3523-8d42-67fd7319c858 | -2.16638 | -48.81578 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77532f51-8f6a-3b29-8f25-ea2853d6a19d | -2.16416 | -48.80841 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a1900124-3d1c-323f-ade2-309b701e01d4 | -2.16362 | -48.81184 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1537f850-e1b1-32a7-953d-6816ba602dd8 | -2.16308 | -48.81527 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02eee635-1a2c-3d03-93a5-0043ae74fd21 | -2.16086 | -48.8079 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd656733-1e4f-35a5-b021-bd40c32aa8ca | -3.22177 | -48.92253 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9c6415d7-ac86-35ce-9591-fa08d2645dff | -3.21847 | -48.92202 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 693919d5-1e79-3d31-83a9-0aa80447b033 | -3.21793 | -48.92545 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9700e51e-8941-3e80-b19a-2e06e6fb0ca0 | -3.16264 | -48.36879 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b250c26f-f619-3723-8fcb-64f2b399ff4d | -3.135 | -48.97569 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad5a4b55-097a-30b2-ab4a-d6884284af5b | -3.12886 | -48.60601 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b655f57e-92a1-3821-8556-096cfc3e52c0 | -3.12556 | -48.6055 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb0f64b7-9e67-3862-8c9d-9139185ed577 | -2.83322 | -48.45056 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d82df9b-cab0-38ce-8434-76efdb1c8ab3 | -2.83269 | -48.45399 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a74c6db9-aedb-3240-af01-1dff882eb74e | -2.83029 | -48.5554 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fff6350-001a-3afc-a375-28b53c077a60 | -2.81896 | -48.45537 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff69b686-35ab-318b-9b32-675c302ccaf3 | -2.80495 | -48.69534 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67f2d35d-dff0-36d3-90ce-88b456296839 | -2.80165 | -48.69483 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e09b210b-9cd5-3baa-ba66-2f7529de2483 | -2.78739 | -48.69964 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1aeee942-dc9d-30d5-b187-c4eb392da7c5 | -2.78685 | -48.70306 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6be2c1ec-99a4-3f8e-91ae-36c334d80f67 | -2.78356 | -48.70255 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ae5db18-c1b3-332d-8307-dbf99861413a | -2.75496 | -48.6911 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63befeb5-f41b-3c6a-9d36-75b5106daa73 | -2.75221 | -48.4022 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3d6b0ae1-f0cc-3499-b700-3552e395292b | -2.75168 | -48.40562 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7551003c-3851-3be3-a93b-6161b94e1157 | -2.75099 | -48.68976 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b791587e-84b6-3200-8631-e191bc2c2e29 | -2.75045 | -48.69319 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d91928bf-8a38-3881-85ae-9331a3ae75fd | -2.69642 | -48.62868 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1860bef-aaa7-3436-a19f-5ecc9acaa25f | -2.69588 | -48.6321 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e7abd70-71c7-336c-b6b2-e6e499e00a5f | -2.69259 | -48.6316 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28faabc7-2cc0-3100-b357-30aeb93e0893 | -2.62693 | -47.98484 | 2024-10-13 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03ecca34-652e-351d-a80c-5b0c7c4a5c0f | -2.58083 | -48.04127 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b29757c2-7df2-3858-8988-e89d32af5674 | -2.57753 | -48.04076 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37481d68-7871-35ec-8922-134f0dcd14c6 | -2.55019 | -48.40937 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 615affa2-9abb-394e-a2b8-02fd7c9c131d | -2.54689 | -48.40886 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb40fbc-5ec7-3103-915c-e6b646feb7de | -2.48345 | -48.05381 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89ddef06-9418-32c4-95cc-3003aded36dd | -2.48324 | -47.99028 | 2024-10-13 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f79d604d-7de8-34f9-80e1-e44700d57a4a | -2.48015 | -48.0533 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ca02952-c55f-3198-8aea-21c96b0d264c | -2.47663 | -47.98925 | 2024-10-13 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c8bb4f1-20bf-3295-831d-43c7ecd77b81 | -2.4751 | -48.19336 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e471384-3209-3a43-bde0-1c032076c326 | -2.47469 | -48.06656 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 554cf95b-e21e-3eb4-98a9-eedf0d11ceec | -2.47457 | -48.1968 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ed2429c-9808-33f5-ba17-49d0ec6e3181 | -2.43074 | -48.23922 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62b9d531-b824-3478-b6b9-c5a2424b804a | -2.41721 | -48.45476 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e876b744-59b5-31ad-8434-56a16d594d68 | -2.20868 | -48.3311 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2056a02-5376-3b7b-ae05-5773806701ad | -2.17525 | -48.35048 | 2024-10-13 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b1eb6e8-8cd4-33c6-81e6-bc324c45f718 | -2.17196 | -48.34997 | 2024-10-13 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0663acd-fb3d-33fe-8c33-4c93d8a2476a | -2.13019 | -48.37431 | 2024-10-13 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38de2225-6555-3322-b2e7-f2632581199c | -2.11436 | -48.56123 | 2024-10-13 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7abe6815-237a-3306-8919-7b3df827a8c1 | -3.22123 | -48.92596 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c09cc744-745b-3899-98ae-101b13d935a5 | -3.16318 | -48.36536 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 31b4dd88-a022-3a15-a528-78e4be46853c | -3.15988 | -48.36485 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32b06ac0-2938-30cc-bce8-d4f9455be950 | -3.13446 | -48.97912 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 018c37ec-559f-3968-9fec-54817ad3f96a | -3.08785 | -47.77968 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3402909-f32d-3d08-a0ac-31a074d4f54e | -3.0873 | -47.78316 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1519c6b-d656-3303-a5ab-2b579a8feaa9 | -2.9392 | -48.51263 | 2024-10-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55a8bb55-1ab2-3a40-adbc-9d047ee49bf0 | -2.89125 | -48.62454 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1d52a84-2926-3a10-818d-aece19218e4e | -2.88662 | -47.84839 | 2024-10-13 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83922099-2eca-3433-a9c5-16042f96a2c6 | -2.88627 | -48.61324 | 2024-10-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f5b5c63-3aa8-312b-8770-64b91d751a42 | -4.10531 | -48.49903 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a76b12f7-3a49-3559-8548-9235448262fa | -4.102 | -48.49852 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d57bbec-3923-34dc-a92a-486e9f832e61 | -4.0987 | -48.498 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99c17e3d-ad97-3fd7-9a6b-e26aa98441ee | -3.98609 | -49.03955 | 2024-10-13 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1084535a-80d6-3aa0-8b9d-190161082677 | -3.98441 | -49.02874 | 2024-10-13 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7ac2c27-471d-3b91-b4dc-44a83c5d880f | -3.98111 | -49.02822 | 2024-10-13 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faf3e4f2-f19b-3453-b268-25ea0cf9a374 | -3.95257 | -49.03786 | 2024-10-13 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6625b142-8342-318e-a5c3-b35242cf3c13 | -3.92367 | -48.35428 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3ffe0a7a-e08c-3cce-8c0b-6f28d484c3fb | -3.92036 | -48.35376 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9a55e487-3acb-3293-afb1-ee5bbd544312 | -3.91982 | -48.35722 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 90381e82-9d34-3347-86a2-2283bee082c5 | -3.91928 | -48.36066 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |


[Clique aqui para ver as próximas entradas](README53.md)
