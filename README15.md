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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f371a0d1-5905-3668-934d-050a75c97ed4 | -14.7457 | -52.6683 | 2026-06-18 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| d70adb06-8504-3fbf-b682-8588a8e55833 | -12.7746 | -44.5162 | 2026-06-18 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 379.1 |
| 201c79c9-a609-3add-b397-46a6850edc6b | -10.9222 | -46.3936 | 2026-06-18 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 8704be9f-46eb-355c-b012-a76fdad12fb2 | -10.9222 | -46.3936 | 2026-06-18 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 8b71e572-3f1e-36da-97af-aa18305219fa | -10.1491 | -56.6314 | 2026-06-18 13:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 8b850f19-d1cb-384d-83cb-ad084b4e15f9 | -14.7457 | -52.6683 | 2026-06-18 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| ed322d8a-65fd-38ad-ae39-b0361bf235a4 | -11.0622 | -52.4603 | 2026-06-18 13:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 360.5 |
| 626edaa7-5563-32f1-9866-0ff970e11250 | -12.7741 | -44.5396 | 2026-06-18 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 50698dde-69f3-35fa-80ba-5434902b0975 | -10.9032 | -46.396 | 2026-06-18 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| ce62f357-21c5-3460-8cbd-73ff8edc6a0d | -10.1493 | -56.6115 | 2026-06-18 13:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 5b9ffc13-7c89-32c6-8f0c-2500cda7397f | -11.0622 | -52.4603 | 2026-06-18 14:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 357.1 |
| 97fd3133-a4c1-3893-9950-deeef0297534 | -12.7548 | -44.5428 | 2026-06-18 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a7e375a6-4801-3933-912a-b8d8d6a5d26c | -10.9226 | -46.371 | 2026-06-18 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 54b5e2d5-0965-3eb7-b9e2-e21a1d9acb31 | -10.9032 | -46.396 | 2026-06-18 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f680b0ce-0644-322c-9fec-1626b84d8a63 | -10.9222 | -46.3936 | 2026-06-18 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 4a8f1511-4c28-3985-9573-cb826462b8a3 | -14.7457 | -52.6683 | 2026-06-18 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| c1467b11-0f8c-340a-a033-05187539524e | -11.0622 | -52.4603 | 2026-06-18 14:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 355.9 |
| cdbe81a2-b8f5-3d89-995f-371ad8d61d6e | -10.9032 | -46.396 | 2026-06-18 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| ff8cd625-9042-3d14-8865-914ae2e3e03e | -14.7457 | -52.6683 | 2026-06-18 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0c400b67-770a-36ef-834e-b4cc17c1a098 | -11.261 | -46.6423 | 2026-06-18 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 0e459b40-e02e-3309-ab4b-0782e6e12f2d | -11.0622 | -52.4603 | 2026-06-18 14:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 323.1 |
| e81a509b-f9df-3ce5-b6f6-878f4a7befc0 | -10.9219 | -46.4162 | 2026-06-18 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 57897411-71ce-3714-93e9-3ff5d116be21 | -14.7457 | -52.6683 | 2026-06-18 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 6c8dc4aa-71c8-3b04-b4b0-12bc559cbfd3 | -12.7548 | -44.5428 | 2026-06-18 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| db94f5b5-610e-3043-9f0b-aec0456404dd | -10.9222 | -46.3936 | 2026-06-18 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f3dcb2b7-b7e0-30fe-b820-2c70c4b619b9 | -10.9222 | -46.3936 | 2026-06-18 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 74dd9370-0f01-3773-a074-b94dc55f680b | -11.0622 | -52.4603 | 2026-06-18 14:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 268.5 |
| a0b02524-b9ed-36bd-ace0-a958650f5a03 | -10.1227 | -52.1741 | 2026-06-18 14:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 49b14626-9305-3113-a634-cabbb6edf650 | -14.7457 | -52.6683 | 2026-06-18 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 8963d27a-8e5f-32de-8f70-933045d03883 | -13.9412 | -53.5667 | 2026-06-18 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b6f8f98f-5ec0-375e-b8bc-c95e9c616f3d | -2.9192 | -42.1177 | 2026-06-18 14:30:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4fbdb403-2ddf-3642-97be-45af022ecd24 | -10.9219 | -46.4162 | 2026-06-18 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 795488b9-27e3-3097-9e86-e6042792adf1 | -13.9412 | -53.5667 | 2026-06-18 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| b5f0fb0d-1a80-3271-b6ff-631f9ea45604 | -10.9032 | -46.396 | 2026-06-18 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ce05f59b-69d0-33c9-a882-96838338e8b8 | -10.9212 | -46.4613 | 2026-06-18 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| fa9c53cf-56c2-395f-9b1b-f0473f6d1325 | -14.7457 | -52.6683 | 2026-06-18 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 6d5a68f6-7067-3001-b6d9-cb5e4ebb3b61 | -10.9222 | -46.3936 | 2026-06-18 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| d13b8afd-76eb-3e56-b2a5-a75e3a5cbf68 | -10.1227 | -52.1741 | 2026-06-18 14:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 04e1838e-c64c-39d9-833a-1d675565c2ad | -10.1227 | -52.1741 | 2026-06-18 14:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| df1b9951-8104-383f-9ae0-c1459ed67e6c | -10.9032 | -46.396 | 2026-06-18 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 2cf74a2f-dab2-3a68-a6ab-031475b97037 | -10.1493 | -56.6115 | 2026-06-18 14:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 5e457e87-9188-3c7a-8bb3-5069ac7a9fad | -11.0622 | -52.4603 | 2026-06-18 14:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 245.1 |
| a5fa05b5-18ef-394d-a602-f2725bbe73cf | -13.9412 | -53.5667 | 2026-06-18 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 4fbf2967-62fc-3641-b35d-69ba31837e66 | -14.7457 | -52.6683 | 2026-06-18 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| b83fb58c-0413-3f6f-84b9-b592f984bf15 | -12.2143 | -52.7801 | 2026-06-18 15:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3ddf038e-164e-3588-9a61-db6f75b07288 | -10.716 | -56.2494 | 2026-06-18 15:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e467bd78-f0e6-320a-9c8f-0d1fe53f56d6 | -10.7838 | -53.5846 | 2026-06-18 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| eebfd7d8-31d7-3110-a67e-21a9388c9694 | -13.9412 | -53.5667 | 2026-06-18 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 2f636a01-a6c6-3d04-a807-cbb6aee75c1f | -14.7457 | -52.6683 | 2026-06-18 15:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f8c25158-31f3-3352-9c30-5ade8d41421f | -10.9032 | -46.396 | 2026-06-18 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| e7df7343-3810-36f7-bdb6-d40e0bfa4e20 | -10.1227 | -52.1741 | 2026-06-18 15:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8da0b308-d4b8-3073-aac8-ef6c8fce2c22 | -10.716 | -56.2494 | 2026-06-18 15:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8c780574-e557-371f-980c-349bde8a5da3 | -10.7838 | -53.5846 | 2026-06-18 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 6c134ec1-663d-3cab-ac2e-ea95e67168f1 | -12.2143 | -52.7801 | 2026-06-18 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 626fa18f-8073-3211-ba62-76d3c2b95768 | -10.9222 | -46.3936 | 2026-06-18 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b78e552a-0575-306c-8d5c-4c58094bb446 | -13.9412 | -53.5667 | 2026-06-18 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d23f25d6-ef64-3679-8566-5e5783868bdd | -14.7457 | -52.6683 | 2026-06-18 15:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 29303604-85c5-34d2-8cd0-921f7307922e | -10.1227 | -52.1741 | 2026-06-18 15:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6e2c8ca0-b3af-37fd-890f-166c597a000d | -20.2335 | -55.4991 | 2026-06-18 15:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 6d5d1891-56b1-38b7-ad52-b0bf694abfea | -14.7457 | -52.6683 | 2026-06-18 15:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| af5ba009-19ed-3c51-a406-34db22e4d16d | -13.9412 | -53.5667 | 2026-06-18 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| d41c03e7-d349-3e23-b065-69baff52252a | -12.1952 | -52.7821 | 2026-06-18 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 6f934fbd-7251-3a5b-b69d-60eb3076e964 | -10.7838 | -53.5846 | 2026-06-18 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| e6521265-9f15-3cb1-9e61-6b5ba91eba63 | -10.1227 | -52.1741 | 2026-06-18 15:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 821b5d02-d6d8-302a-9ebc-7b98bd8ae526 | -12.2143 | -52.7801 | 2026-06-18 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 6f02114b-896d-3d88-a53b-cdd9ccddffde | -20.2537 | -55.4959 | 2026-06-18 15:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e280e41f-ba80-30ec-b00b-d8d2bf36aaea | -12.2143 | -52.7801 | 2026-06-18 15:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 0b2af63b-8d9e-3a15-9f55-04b93fc0c5b8 | -8.9449 | -46.9582 | 2026-06-18 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| d1a5eadd-65c2-301f-8751-efba4c1e797c | -13.9412 | -53.5667 | 2026-06-18 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| da10246b-f85a-3262-a6cd-0ab8afab0937 | -10.1227 | -52.1741 | 2026-06-18 15:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 1c573f38-473a-3055-a07a-859c477db833 | -12.1952 | -52.7821 | 2026-06-18 15:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 90f9c1d5-7715-38a3-a5c2-4d272f3e8172 | -8.9452 | -46.936 | 2026-06-18 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 9d28b57b-c642-3965-b97a-04a079e66d85 | -10.7838 | -53.5846 | 2026-06-18 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| f7119f51-e193-3354-8586-5b5d70344270 | -20.2335 | -55.4991 | 2026-06-18 15:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 79c57323-0d99-3cb3-a470-3ddd9a2997f5 | -20.2537 | -55.4959 | 2026-06-18 15:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 2030a0c9-e5ef-3db2-b939-0096dbbe2590 | -14.7457 | -52.6683 | 2026-06-18 15:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6e67ca92-9238-356c-b796-08d17a115f61 | -9.5508 | -48.2182 | 2026-06-18 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| fe8d6c5f-10cb-349c-8f75-02560f1dec55 | -10.716 | -56.2494 | 2026-06-18 15:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e4e2a4a1-c9b5-3832-b527-5d82be56c73f | -12.1952 | -52.7821 | 2026-06-18 15:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 103037f7-6f45-309b-9b56-1c685091884d | -8.9638 | -46.9563 | 2026-06-18 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 27d004b5-dbe4-31c1-9fb8-959c902b5ed8 | -12.8354 | -44.3657 | 2026-06-18 15:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| f4921b9e-5307-34fd-b4bb-51500ec907a1 | -10.3397 | -49.9333 | 2026-06-18 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| f291452a-9d2c-30d1-b4ab-db5973d3b59f | -13.9412 | -53.5667 | 2026-06-18 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 84d5afe7-b411-3a23-9d67-a648b279393d | -12.2143 | -52.7801 | 2026-06-18 15:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| af095697-8535-3f02-85a0-2a0c7d1dcb2d | -20.2335 | -55.4991 | 2026-06-18 15:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 144.8 |
| f91faf99-e6d6-35cb-9707-1e454c11c0f2 | -8.9635 | -46.9785 | 2026-06-18 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 06f07f38-13a9-3861-94ad-36136602b631 | -14.7457 | -52.6683 | 2026-06-18 15:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| e506e0f7-edfb-3db7-8cca-6a3d8d4a1f5d | -10.7838 | -53.5846 | 2026-06-18 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 56117c45-8d31-3c38-a0e5-a56bfe732d12 | -10.7838 | -53.5846 | 2026-06-18 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 7cefd7bd-ca20-3693-84b1-e9f74e0b2969 | -20.2339 | -55.4777 | 2026-06-18 15:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 19f3c4d8-53ff-3c04-88e5-56549f4c5fe9 | -13.9412 | -53.5667 | 2026-06-18 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| cc83659d-2623-333a-8ede-116fd6426704 | -9.5319 | -48.2202 | 2026-06-18 15:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d6e9ea2c-d683-3a03-baf9-368c2ab66287 | -8.9449 | -46.9582 | 2026-06-18 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| eaec1383-9d7c-3ed2-a7dd-2e46250390cd | -14.7457 | -52.6683 | 2026-06-18 15:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1ad3b094-31ce-3408-a19c-e9c622eb3b4c | -12.1952 | -52.7821 | 2026-06-18 15:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 4420d4e8-e080-3d33-b9a9-b5c79923e3b1 | -12.2143 | -52.7801 | 2026-06-18 15:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| df616873-1faf-3d18-8a26-e18128046a89 | -20.2335 | -55.4991 | 2026-06-18 15:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 7ff891ba-3424-3a2b-bfb8-b7b40e611d47 | -10.716 | -56.2494 | 2026-06-18 15:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 5bce41e1-91c2-3d92-9ff9-1a7b3385a9c7 | -20.2537 | -55.4959 | 2026-06-18 15:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 90d9f645-d505-38db-9bdc-6e942837af86 | -8.9635 | -46.9785 | 2026-06-18 16:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |


[Clique aqui para ver as próximas entradas](README16.md)
