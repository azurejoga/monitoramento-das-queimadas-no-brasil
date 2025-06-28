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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 081a2cdf-7e39-3259-b5cd-41999589ce8a | -10.8571 | -53.7631 | 2025-06-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 50ce00ca-229f-3d48-8c64-a390696bf50e | -12.1141 | -54.5685 | 2025-06-28 14:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 142f55c7-ff06-3755-9f6d-a4149066deb1 | -10.8382 | -53.7648 | 2025-06-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| bbef85b7-2ef5-3af2-a25d-b0157eb4ef3f | -11.2664 | -52.7527 | 2025-06-28 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 256.4 |
| adf98e42-3c99-33b5-8465-d9408be3eef8 | -6.911 | -43.9602 | 2025-06-28 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| fc3eab34-07a7-3679-8b30-153048f7f0cb | -11.2664 | -52.7527 | 2025-06-28 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 228.7 |
| 2346ceee-e596-31b2-b0d7-9b3113187366 | -16.2625 | -53.6694 | 2025-06-28 14:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 40f15be4-ea2d-3f3c-8ec7-23423454c430 | -8.8686 | -50.1599 | 2025-06-28 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8f36dce5-4e1d-39d4-a061-84da286e248a | -10.8571 | -53.7631 | 2025-06-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| acfe8a86-91e4-3bb7-afd2-c4617aed5a47 | -16.2621 | -53.6906 | 2025-06-28 14:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 5f0e859d-f8f0-3b14-a611-9782f0a6bfa2 | -10.5579 | -52.0289 | 2025-06-28 14:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 57294a2c-d264-3c0d-badb-05b61120ae79 | -10.8382 | -53.7648 | 2025-06-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| db811562-e810-394d-94b3-ec25e6186882 | -10.5576 | -52.0499 | 2025-06-28 14:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 2c012e80-df47-3ad5-b72d-400859239ffd | -16.2429 | -53.6721 | 2025-06-28 14:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 7360c21f-1eda-3f1e-ad87-bda0831b937d | -8.8499 | -50.1616 | 2025-06-28 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 2e249da7-c069-354f-ac7e-0c3d790b53de | -12.1141 | -54.5685 | 2025-06-28 14:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 8fec9978-8dd0-3cb5-b013-0fa9e258b230 | -12.1138 | -54.589 | 2025-06-28 14:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ed97af9f-5642-3bb5-8b5d-85f281c9fa42 | -11.0455 | -55.3773 | 2025-06-28 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 3e034b59-8bb7-34ce-843f-3e4f42b6440d | -6.892 | -43.9851 | 2025-06-28 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 5e80f02f-863f-32e1-8707-b23f9d392c61 | -10.8385 | -53.7442 | 2025-06-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d1f86621-5179-37d2-9271-4e3342e7032f | -10.8385 | -53.7442 | 2025-06-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| fc7fef00-d4d2-35e8-bec6-f4f12b9343f5 | -10.8382 | -53.7648 | 2025-06-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 1ed29964-31c7-3600-87e4-bf54b0180ce7 | -11.2664 | -52.7527 | 2025-06-28 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 0535248f-84e4-337a-aebf-6d8675cac135 | -10.8196 | -53.7459 | 2025-06-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0694d8fb-d38a-3457-85a7-edbe0eaf0d3f | -6.911 | -43.9602 | 2025-06-28 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2e139d56-af5a-3cd8-a627-af94871d40fb | -10.5579 | -52.0289 | 2025-06-28 14:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7b81d6dd-7d6e-3a0e-a8f7-d0d5eca39c76 | -10.5576 | -52.0499 | 2025-06-28 14:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 4df8ca3a-14cf-3c84-bcea-d0e97a8223a1 | -8.8499 | -50.1616 | 2025-06-28 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 977e979b-cafc-3711-b478-32fc41abef60 | -10.8571 | -53.7631 | 2025-06-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| a00925c2-791e-3427-975c-49a44019f11e | -11.2853 | -52.7508 | 2025-06-28 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 93da2467-06e7-3f57-ba69-8e9adab63c69 | -11.0455 | -55.3773 | 2025-06-28 14:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 94fe9103-7ffe-3ad6-9ef6-9c2bcee47047 | -12.1141 | -54.5685 | 2025-06-28 14:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 12776346-3771-304f-a64d-3889d24a0ff8 | -12.1138 | -54.589 | 2025-06-28 14:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1c64a548-5855-3230-bd2b-a658d48b9437 | -16.2625 | -53.6694 | 2025-06-28 14:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 89d66b7c-f428-39f4-91b8-7a6377effc66 | -16.2621 | -53.6906 | 2025-06-28 14:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 79bd7ed6-8034-321f-afc7-f2489f9166a5 | -6.892 | -43.9851 | 2025-06-28 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |


