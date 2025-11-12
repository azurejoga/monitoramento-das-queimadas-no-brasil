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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da26287c-ed22-336c-bacf-64277205a0ed | -4.10094 | -48.01023 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 430c214e-d95b-38f4-aed2-dc0407e03125 | -4.10871 | -48.02571 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26448242-5ae5-3ad3-8324-e9dcee1ae9e4 | -3.84389 | -50.06347 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2cd5f336-d84e-30b5-9188-804ba9d42bb5 | -4.11423 | -48.01226 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a0fd7b9-2a94-37cd-8d13-f3be6104ddde | -3.09316 | -49.27135 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cbb48284-924f-3f27-8e2b-55624ecaedb9 | -3.49051 | -49.96151 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32f0b310-32f3-313f-9ffc-cf21a34ecb11 | -4.24477 | -50.0543 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ffc814e-0dfd-39df-b233-9af32cd4b529 | -6.99857 | -41.28741 | 2025-11-12 04:31:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e11d3a1d-269d-390f-bf95-e70900a9e7b3 | -4.11535 | -48.02675 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ca82008-a648-3dfa-bb02-5dcf48375316 | -2.39393 | -49.3945 | 2025-11-12 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 725945f6-c5bc-3342-a8f3-aec7f7c08d0a | -7.13416 | -41.86737 | 2025-11-12 04:31:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b84458a4-bc67-39fd-acd8-30bdc1f49a28 | -2.86873 | -51.47701 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| aa50d4a3-d680-3ffc-a3b5-47bd88934a1b | -3.4928 | -49.97013 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d5c65fa-307a-3b0a-8729-2c926fa5de07 | -3.95881 | -43.77514 | 2025-11-12 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2101c6aa-190f-39f4-b34b-7999f6ec9aae | -2.86562 | -51.47148 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e3a41e43-7117-3900-a914-083ef1357e7c | -2.63806 | -49.20249 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3e282a12-77d1-34da-a335-94dbb5f3b61f | -5.23187 | -49.58235 | 2025-11-12 04:31:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 784c9b86-30ab-324c-b54b-715ceb409fe3 | -4.94107 | -44.29235 | 2025-11-12 04:31:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a4763ad-0380-3010-bd07-3fd19bb8a144 | -2.4399 | -49.22655 | 2025-11-12 04:31:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 708c08a4-006d-384d-9b49-18db6f5ee5d4 | -4.78387 | -49.81421 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b537c829-e122-3f86-a09e-bc8340954cd9 | -3.71212 | -45.82031 | 2025-11-12 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6183e0c2-f7ad-3189-862c-13fafc1f6d42 | -5.65222 | -45.98518 | 2025-11-12 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6df453e-18fc-3523-b1ae-939d2023f0a5 | -6.78517 | -42.84394 | 2025-11-12 04:31:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 181e5f3d-b81c-3943-bba4-f72c5afdf398 | -7.30478 | -45.28596 | 2025-11-12 04:31:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a35954a3-cfb5-37ef-81ce-9db4a6892c0d | -3.43209 | -42.464 | 2025-11-12 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f6a416f3-a12c-3ebf-aab3-38329faee9ae | -2.87264 | -51.47761 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92077d19-d741-3dd9-aea8-7e747e6bc66b | -3.77336 | -48.92552 | 2025-11-12 04:31:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcbd2715-e12c-351b-a0e9-35c0154868b4 | -3.07523 | -51.33696 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 311bd0ff-a87d-3e0d-b4b8-408d5562f3c4 | -3.24208 | -50.04051 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 283502b5-42b1-384e-81b0-e685b5231e17 | -6.6404 | -46.54064 | 2025-11-12 04:31:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c65c367-7280-348a-a7f4-16f296785004 | -2.61303 | -49.226 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ecee17b-0a3b-3079-bfd8-8d5f1ddd9898 | -4.92076 | -49.99881 | 2025-11-12 04:31:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0805c8d-d832-374f-8406-6b894ff064c5 | -7.00038 | -42.78527 | 2025-11-12 04:31:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 89ceecad-ea00-3c4d-aa8f-aaf333ac4897 | -10.1404 | -44.87363 | 2025-11-12 04:31:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eee74407-fa82-3ea1-8eb6-9982fea0d589 | -5.60487 | -41.07464 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e8a2d37b-b4d7-3b25-9262-af004525ddf9 | -6.1182 | -47.18663 | 2025-11-12 04:31:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7de2f8cb-5246-3014-aeb1-1b386e720d37 | -2.72933 | -47.40677 | 2025-11-12 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34bf7513-9f03-3edd-bfdd-80cbe49d3be6 | -6.09496 | -41.62506 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b3f31413-e9fb-33c2-8d4c-aca4a28fa415 | -7.45807 | -44.74848 | 2025-11-12 04:31:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a9e6c13-c1c9-31f8-8b89-dde17d69962e | -5.60995 | -41.07093 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 671a9956-60a2-3e31-8f86-d18e8599893f | -4.29547 | -40.04966 | 2025-11-12 04:31:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3d1deb56-f173-314e-b6bf-f5542be9f71b | -3.83815 | -44.54902 | 2025-11-12 04:31:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cac49fc5-a317-3f52-9d58-e22e7ea6aeb8 | -2.94773 | -45.55002 | 2025-11-12 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d01a84a-6bd6-32e3-bfb9-04e6f06e1e26 | -7.47445 | -42.55539 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a9f86b6-5f65-370f-859e-301a5e271620 | -7.4005 | -43.33406 | 2025-11-12 04:31:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e047bb77-9024-394f-8a5c-e1b7de7b6eda | -5.38009 | -48.09909 | 2025-11-12 04:31:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61f74a93-29f1-34e6-8674-999194ea9d1a | -7.13605 | -41.86547 | 2025-11-12 04:31:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c73fcce4-2b75-32cf-8b67-b3ca5f518ab3 | -6.89872 | -42.06998 | 2025-11-12 04:31:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a4bd264a-ee6d-34ce-a25b-7b8b814ba615 | -1.75307 | -53.87869 | 2025-11-12 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c792e3b-94f4-3097-ba01-7d4eabb92f22 | -1.35555 | -55.48473 | 2025-11-12 04:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7498fb6-8d0a-3fe7-a1a3-6d3bfcbf08b6 | -3.08329 | -49.46655 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 951f8d65-78e9-319e-a6cd-2dc94697cf07 | -4.96638 | -43.72188 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a389013f-19b9-33a6-821a-69fa66f9ba1b | -4.90762 | -49.32553 | 2025-11-12 04:31:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85206024-232f-3bc6-8a77-be9fc68afdba | -4.77128 | -42.66157 | 2025-11-12 04:31:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8f47125c-1714-33f4-8f09-e3a165a14bbd | -2.62285 | -49.23145 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d939954a-8ce5-3447-a37c-5a35a56e80ba | -6.09919 | -41.56695 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b2624bbb-7a5b-3215-b046-25bc3d9afad4 | -4.4022 | -49.65637 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fa22bcd-7d2f-3c85-8dc8-09e0d6a9889d | -4.66443 | -46.84888 | 2025-11-12 04:31:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ba2e76c-d544-3ff7-9fbb-bc14574f7b8b | -2.64153 | -49.20302 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f809bc7c-6bb7-3827-aeda-b40bf51af678 | -4.94852 | -43.71458 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e65a391-bb46-35e7-a113-f13751812ea7 | -2.9807 | -44.5864 | 2025-11-12 04:31:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec5f62b9-562e-3ce7-a34c-950e22c0079f | -4.10149 | -48.00676 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56cba63a-d9b8-3b9f-b923-e9c0831acdb4 | -2.9543 | -47.36131 | 2025-11-12 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 531f1a4c-fddb-3300-98e3-5336c518a6ad | -2.95109 | -45.55054 | 2025-11-12 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27f9932b-4916-36aa-b82d-0e95a62134bf | -4.1004 | -48.01369 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a430f50d-821b-3865-bd80-50e75bc8212d | -9.66844 | -43.90099 | 2025-11-12 04:31:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e2e3f643-caee-3e7e-a6f7-0a71150dc8c2 | -3.09662 | -49.27189 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad55da1b-2e19-3107-a1e3-f615500e8b38 | -4.33725 | -50.81881 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d65a7dd6-d145-399e-b8c1-028bb8562005 | -4.64666 | -45.7544 | 2025-11-12 04:31:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0525097-9918-3834-95a9-5ff056647b05 | -4.10926 | -48.02221 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae50a9d0-24de-37bd-99ed-8bbdec1cf403 | -4.15912 | -48.22334 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ec81a53-20f9-3ec8-915a-09ab6878c5f2 | -4.66504 | -47.92834 | 2025-11-12 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b53a0707-6f52-3db7-98fb-c21dce6ef393 | -3.83874 | -44.5451 | 2025-11-12 04:31:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e1abe35-ce91-3a0a-849a-49990f90a092 | -5.724 | -46.72646 | 2025-11-12 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47edb294-78bf-3ba8-9abf-06ab86719430 | -7.47804 | -42.55981 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3a81b28e-9b79-3680-a191-e113371b3b4a | -5.09044 | -43.74387 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc63466e-a866-3c05-b0be-8857f4c72c47 | -2.64588 | -48.04288 | 2025-11-12 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 967c6df3-fb78-310c-8298-08fdfc1d7ebf | -1.64081 | -52.04974 | 2025-11-12 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47eebd5b-fa49-36da-b608-38ef54f15b20 | -3.98157 | -47.29795 | 2025-11-12 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 8aed82e9-3f7a-3080-a80c-181d7e037a87 | -7.11085 | -40.21253 | 2025-11-12 04:31:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6dfabdbb-7c7b-3ec6-87b3-f6b6af543a9d | -3.44007 | -42.77345 | 2025-11-12 04:31:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12694c7d-4eac-3f49-bee7-a00697c57467 | -7.14903 | -46.23081 | 2025-11-12 04:31:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39b2b9c6-ffcc-3066-9fda-d706fea4d73a | -2.98671 | -52.51839 | 2025-11-12 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cde60003-9348-3155-a63d-e4f120801009 | -2.87184 | -51.48254 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3027fb0-9e2c-34ea-a215-0d03b7883a3c | -4.10759 | -48.01124 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e70b8c3e-efe3-3365-b1e2-e81407620b1a | -3.86979 | -51.29015 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9927717d-6c54-31d6-86d9-4cb3e81b6c30 | -9.67304 | -43.89654 | 2025-11-12 04:31:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2092ad1e-ac1c-3ec0-bbd3-95d9c9988f0c | -3.89682 | -52.11548 | 2025-11-12 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6854557-f08c-360c-a085-37d14e3a9688 | -4.09266 | -48.01962 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0210a873-394f-3383-80c0-c17e16005bd6 | -10.50084 | -44.93351 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba3d9c00-08ec-3020-8909-ad1d3a337435 | -9.45551 | -44.87754 | 2025-11-12 04:31:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60dab64b-d26c-3e1d-8f24-7597dbb03636 | -2.87343 | -51.47269 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d192ace9-2c65-3fe9-90ff-f89614e8ef4b | -4.72122 | -43.05462 | 2025-11-12 04:31:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86f2acfa-e677-3ead-bc2e-1f21213d5086 | -2.86483 | -51.4764 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a2e2349d-be20-3f2c-a877-209a08de543c | -4.11922 | -48.02378 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbe25b01-1315-3c44-95bd-a7297f38cb3d | -4.4395 | -50.08375 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea54a7bc-d344-386b-aaa7-ee3029a23630 | -6.98767 | -41.27807 | 2025-11-12 04:31:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 76e0aa98-a238-34c7-8e6b-b119d7ab053a | -10.49587 | -44.94183 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b6db23e1-dc8a-3b97-977e-f559f7d58098 | -7.28659 | -41.5766 | 2025-11-12 04:31:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 58425bad-db00-3fdd-ba09-fd75b0e340f8 | -6.98257 | -41.28182 | 2025-11-12 04:31:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
