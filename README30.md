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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f02d87e7-2e22-3a50-a758-98d09577c39e | -11.4793 | -47.2858 | 2025-06-19 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 225.6 |
| 571d6782-5c8f-389c-a0ac-0f6995606667 | -11.7754 | -54.3756 | 2025-06-19 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 95f48187-2f25-3572-81ea-47ba4b6b0662 | -4.0148 | -43.2408 | 2025-06-19 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 120ac9ce-f9ca-3026-afea-e18a22be80e1 | -16.3185 | -53.8094 | 2025-06-19 14:00:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 66a64419-03ca-3608-85e4-a1e2d3eabe3f | -6.6747 | -43.2133 | 2025-06-19 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 67.8 |
| eb6f313c-47e6-3f3d-8777-69ec45cce046 | -9.4807 | -56.0801 | 2025-06-19 14:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 287750b8-b64d-3e27-848c-161c93df883b | -6.6935 | -43.2117 | 2025-06-19 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 54ff57f6-7dac-37f8-ac82-217a647a0610 | -20.274 | -55.4927 | 2025-06-19 14:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 77.1 |
| d54a982e-5636-3832-b660-a6d5c2d2365e | -16.3189 | -53.7883 | 2025-06-19 14:00:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 15b93e4f-fb12-3c20-b696-50d3dc9fd028 | -11.1419 | -55.1869 | 2025-06-19 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 868a3834-441e-34b2-a171-901ed338eab9 | -12.2412 | -44.2277 | 2025-06-19 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| fb29eef0-0f61-30a1-b131-cd464212f552 | -7.3162 | -44.7056 | 2025-06-19 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 226.0 |
| e71388eb-8863-35af-8748-c581e98be255 | -10.8353 | -54.0112 | 2025-06-19 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 11514322-cdca-3f40-a08c-c84da0cea2af | -11.7754 | -54.3756 | 2025-06-19 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 5c6ea702-bf84-3b1d-847e-b3aa9f9a006f | -16.3385 | -53.7856 | 2025-06-19 14:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3a98593a-5e52-3864-8101-e1126cd34190 | -11.5366 | -56.9847 | 2025-06-19 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 432f9bc4-1e66-380a-974a-5a362eb1eed1 | -9.4806 | -56.1001 | 2025-06-19 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 373f06e2-73a6-3e0a-89b9-66189eaac374 | -11.9518 | -58.7574 | 2025-06-19 14:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 231d0991-a654-3f1c-bddf-291bb7fe2fc7 | -16.3185 | -53.8094 | 2025-06-19 14:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 143.4 |
| dc86773e-687a-3e93-be24-dcee7f200572 | -9.4994 | -56.0788 | 2025-06-19 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 853e6832-1514-316b-adc2-f84a63ba004e | -4.0148 | -43.2408 | 2025-06-19 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| e202ad06-109e-351d-983a-084c95fe7fac | -5.1222 | -45.0362 | 2025-06-19 14:10:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 1a9e3ee5-9020-34f2-882f-9e6fcadc4336 | -11.4793 | -47.2858 | 2025-06-19 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 74b60a47-0dea-32f6-988d-41d59e9be5d4 | -16.3381 | -53.8067 | 2025-06-19 14:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| fc48d34f-1ecd-331c-912b-f2b6ca557820 | -4.8375 | -43.1919 | 2025-06-19 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 290.5 |
| 26927b15-9bd6-3afc-8f55-ecac6da790c6 | -11.1419 | -55.1869 | 2025-06-19 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 339c3f0c-66fb-362d-a483-214ecf115f1f | -3.9961 | -43.2418 | 2025-06-19 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| f5c0faca-d39b-3e70-bf59-6b1904c99058 | -11.952 | -58.7376 | 2025-06-19 14:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7a9f80ad-5f43-3e57-b877-3140f962f2b1 | -9.4993 | -56.0988 | 2025-06-19 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| efd568ef-cb16-3d8a-8293-6211056dba5a | -9.4807 | -56.0801 | 2025-06-19 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 182.3 |
| c65519ae-86ab-366c-8644-316f8279d467 | -8.6115 | -45.0334 | 2025-06-19 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 743f6b23-f52b-3e30-9f59-e981d2e0e912 | -11.5177 | -56.9862 | 2025-06-19 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 7d36e743-7f15-3ce6-a254-1489983e7687 | -11.4602 | -47.2883 | 2025-06-19 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 6267758c-9295-379f-9c65-ddd33de4b86c | -16.3189 | -53.7883 | 2025-06-19 14:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 95b380ae-7129-3bb4-a6dc-cfa2d13622b1 | -6.6747 | -43.2133 | 2025-06-19 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 71.1 |
| 66301e7a-e2e2-3230-8661-34bfe3b43fd6 | -9.4994 | -56.0788 | 2025-06-19 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 5ab825df-5d57-38a4-ad7c-39ce209b96b2 | -10.8353 | -54.0112 | 2025-06-19 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 6d38ee80-41cf-3815-9e05-91f478cd70af | -11.4602 | -47.2883 | 2025-06-19 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 16838130-b24b-3897-9817-bf672852c4f3 | -11.5366 | -56.9847 | 2025-06-19 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 6c22d9f4-5cdf-3ee1-85eb-5cfa5d517ec7 | -9.4993 | -56.0988 | 2025-06-19 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 97b33e89-a75b-3872-8185-ebb92a4105ec | -5.1222 | -45.0362 | 2025-06-19 14:20:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 862592d7-65a3-30d5-b241-14a8f50eff4c | -11.1608 | -55.1853 | 2025-06-19 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 0e2c14ec-8a8e-3a86-91fe-8df990a412dc | -16.3189 | -53.7883 | 2025-06-19 14:20:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| cdfa86cb-d145-3131-b55e-fed09715ff09 | -12.2412 | -44.2277 | 2025-06-19 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0ea863b9-90ce-366c-a2ea-2297e44266f2 | -7.1441 | -43.2869 | 2025-06-19 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 2c65a80d-f6ae-3b11-9642-37d08a0285cb | -7.4483 | -43.0457 | 2025-06-19 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 0cc52da8-4f44-3465-8eb9-f15246b301cb | -11.1419 | -55.1869 | 2025-06-19 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 15319490-2526-3254-9c2d-bbe99e3a958c | -6.6747 | -43.2133 | 2025-06-19 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 204cf8e7-f911-351c-9ac9-d96c1b602a25 | -11.952 | -58.7376 | 2025-06-19 14:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c97a3619-a7d0-3c3e-b7a7-6e3f4ad4e2d7 | -4.0148 | -43.2408 | 2025-06-19 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 0e31a94d-7c90-3a22-8974-7ed65ec7a8cc | -5.1224 | -45.0136 | 2025-06-19 14:20:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| dee6cbd8-49e2-35d6-87d0-ee1bb12c2865 | -11.4793 | -47.2858 | 2025-06-19 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 8b80dc53-67aa-3f02-b7dd-ea78e32f4289 | -11.5177 | -56.9862 | 2025-06-19 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1a9c148a-111b-351c-8d12-e187c56b9c47 | -9.4807 | -56.0801 | 2025-06-19 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 289.5 |
| bc6497e7-9280-34c3-8bca-6652ea80dd8b | -3.9961 | -43.2418 | 2025-06-19 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 0bf22096-935f-3bb7-9a1b-b2e1cd03105b | -9.4806 | -56.1001 | 2025-06-19 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 95261d6c-0eac-3d68-8af4-676b67be6f60 | -4.8375 | -43.1919 | 2025-06-19 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 314.7 |
| 87e16537-3920-3878-b473-5c6fd4d8dc97 | -11.9518 | -58.7574 | 2025-06-19 14:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 53a5f0b8-8288-3360-9fe2-ae5c9c687493 | -16.3185 | -53.8094 | 2025-06-19 14:20:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 00bdb929-91dc-38f7-b79d-383795228bcf | -16.3385 | -53.7856 | 2025-06-19 14:20:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 2f28e0c7-1e70-3f46-a3d3-59593527b96e | -8.0589 | -45.5225 | 2025-06-19 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 15d2651b-6e16-3826-8662-7ab1efe674e0 | -16.3381 | -53.8067 | 2025-06-19 14:20:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 448eba90-748e-3428-b382-4150d2cb6003 | -11.5177 | -56.9862 | 2025-06-19 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 6dab64c3-5cca-3c12-b48c-bd36c1226ed6 | -11.1606 | -55.2056 | 2025-06-19 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d8ba0652-b7d6-3ab4-8072-a67ef83441d5 | -11.9518 | -58.7574 | 2025-06-19 14:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d46979b4-f27e-3050-b190-50bbe3efcf46 | -9.4807 | -56.0801 | 2025-06-19 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 371.8 |
| 4fa221be-1e0d-3e64-8e36-45d40f487eac | -11.4793 | -47.2858 | 2025-06-19 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 96170e64-7f8a-3efe-bf13-84e80809aca0 | -4.8375 | -43.1919 | 2025-06-19 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 7285c00a-48ba-3976-a181-37e3919dd4f3 | -11.1419 | -55.1869 | 2025-06-19 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| defa0f75-a955-3b0b-91fd-a8ac1e93c6de | -5.1222 | -45.0362 | 2025-06-19 14:30:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 0c6fa2fd-b1db-38c9-aef3-524164ce3eaa | -6.6747 | -43.2133 | 2025-06-19 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 1ea2d95f-709a-3633-8f88-8b5395af8862 | -16.3381 | -53.8067 | 2025-06-19 14:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| b5088f4d-633a-376f-a888-6c0802bc7e9c | -11.952 | -58.7376 | 2025-06-19 14:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 84c668ef-6bf0-3709-92ff-5e4e5068935a | -9.4994 | -56.0788 | 2025-06-19 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 153.5 |
| fc1debd5-b8b9-3467-b6ee-7a03dee38b67 | -4.0148 | -43.2408 | 2025-06-19 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8eb74a38-cb13-3016-8a13-ef6b0fd288f4 | -10.8353 | -54.0112 | 2025-06-19 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 62b1b254-27a4-3296-9213-43d70b8683c2 | -11.1608 | -55.1853 | 2025-06-19 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| bdf7f722-5451-3350-9bf1-ed24b70d9fda | -11.4602 | -47.2883 | 2025-06-19 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| c34fd61b-8aa9-35a3-85d7-9de336db2261 | -9.4993 | -56.0988 | 2025-06-19 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 544a285d-ea62-3f53-9883-0d6147f9dd66 | -9.4806 | -56.1001 | 2025-06-19 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 264df151-cb79-3d1f-8afc-994d3a86f995 | -3.9961 | -43.2418 | 2025-06-19 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 883f017e-5702-3f4d-897c-a35dbd287622 | -11.5366 | -56.9847 | 2025-06-19 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| d1a7bacd-e4d8-3dc2-ba3e-b5c171a271ed | -5.1224 | -45.0136 | 2025-06-19 14:30:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| cd548e21-f368-321f-851d-7a53ad0128c2 | -7.3162 | -44.7056 | 2025-06-19 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 8002ff5b-733d-326e-9c47-d16ee6436dfd | -6.7118 | -43.2568 | 2025-06-19 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 63.1 |
| d2dddfa3-2407-3fcc-94bd-39950bf66ff0 | -6.6935 | -43.2117 | 2025-06-19 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 78.6 |
| feca06f6-b2af-3b70-a4cc-6bad64823fec | -16.3185 | -53.8094 | 2025-06-19 14:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| c4014707-ef19-3f82-979f-1bfcb940e635 | -16.3189 | -53.7883 | 2025-06-19 14:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 322edbed-96a3-3c4c-92d8-92cb63964a83 | -16.3185 | -53.8094 | 2025-06-19 14:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 3793d88f-1887-312f-b4ea-aa600ee29599 | -5.1224 | -45.0136 | 2025-06-19 14:40:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 5a7922e3-82ba-3374-9829-8b2cb697fcca | -11.952 | -58.7376 | 2025-06-19 14:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 62324e32-adab-307d-9f45-b548768cc079 | -11.1419 | -55.1869 | 2025-06-19 14:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 201.3 |
| d5908aa9-2b9d-3c42-80f0-1be70efd25a6 | -7.3162 | -44.7056 | 2025-06-19 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8e58d1f6-51f6-3c9c-baa4-64089ae1be68 | -11.7754 | -54.3756 | 2025-06-19 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 175514e0-0abb-3540-9f07-2050f9ef40d7 | -11.9518 | -58.7574 | 2025-06-19 14:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 834ba3b3-4d1d-32e7-83db-54a623da8091 | -16.3189 | -53.7883 | 2025-06-19 14:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 8ae00b6e-f983-391b-8cc2-276b0a5c99b2 | -9.4994 | -56.0788 | 2025-06-19 14:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 336.1 |
| 0b7681c4-9eb1-39f8-a6a6-c7ad7fa84074 | -9.4993 | -56.0988 | 2025-06-19 14:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 2b0aa984-328a-3fb6-b7b4-06aafcb617f5 | -11.5366 | -56.9847 | 2025-06-19 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 6a773983-d78a-3171-9482-1dc81406c116 | -11.4602 | -47.2883 | 2025-06-19 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |


[Clique aqui para ver as próximas entradas](README31.md)
