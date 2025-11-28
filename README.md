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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d2d6041-0469-34fd-956f-091d32d6795b | -2.4198 | -45.7908 | 2025-11-28 00:00:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| b13aee97-3ae3-3778-af53-99cfed98520d | -2.7191 | -45.2208 | 2025-11-28 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 479.1 |
| d32776e5-ab97-33a4-8e3d-28a01ff47c49 | -3.5822 | -47.2747 | 2025-11-28 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| c3e2456b-ef44-3456-a15a-90f6ed712d4b | -2.4384 | -45.7903 | 2025-11-28 00:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 96f5be06-2703-3447-afe1-188c79eb9d8f | -3.8431 | -47.0666 | 2025-11-28 00:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 5b811cea-7187-3c91-a78d-a558b9005f7e | -2.5134 | -45.5868 | 2025-11-28 00:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 1454543b-cce0-39bd-b293-70ca15dad8aa | -3.8618 | -47.0438 | 2025-11-28 00:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 49fe48fc-1136-3af3-8a3e-739f2090462d | -2.7192 | -45.1982 | 2025-11-28 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 777d7819-5b1c-33e0-ae17-b12a0aabbcc4 | -3.8631 | -40.653 | 2025-11-28 00:00:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 1dc82673-c290-315f-8b12-e18453737c0a | -2.4949 | -45.5649 | 2025-11-28 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 956dd8ff-e1cb-3d05-a6b2-020030e2a401 | -3.1684 | -48.6113 | 2025-11-28 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5ce042ba-eee2-3b91-b796-a5a573746acd | 0.4648 | -60.4494 | 2025-11-28 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8feff43f-9cb9-322d-b3f6-2c23c8cce91d | -1.8245 | -54.312 | 2025-11-28 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| dc727d74-57af-3e3f-ac8a-f019f12feee2 | -1.8245 | -54.332 | 2025-11-28 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 676db1c4-e0f8-37ff-8793-fdf20d01438b | -9.4 | -40.3722 | 2025-11-28 00:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 149.8 |
| fe34e016-08c8-3484-8de4-5cde506187ac | -2.7006 | -45.1988 | 2025-11-28 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 4c9a5b48-adf9-38a4-9b0e-24db7bc90140 | -3.9903 | -47.301 | 2025-11-28 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| b6ae9a46-527c-3c0a-aa87-a883b2b8e528 | -2.267 | -47.0994 | 2025-11-28 00:00:00 | GOES-19 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c738e8d4-a36f-36c8-ac8e-fe333e3014f5 | -9.3809 | -40.375 | 2025-11-28 00:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 362.5 |
| d72f80dd-549f-35e9-b029-25f2930f1915 | -2.4199 | -45.7685 | 2025-11-28 00:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 45b0fa38-8450-3485-90d6-f3daa901e883 | -21.6473 | -48.615 | 2025-11-28 00:00:00 | GOES-19 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 29a85823-7792-31ee-b4aa-f53be2225bec | -3.8793 | -47.2403 | 2025-11-28 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 26fa0e7c-d8b0-339e-b718-615802fdf8aa | -3.8978 | -47.2395 | 2025-11-28 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 1880715c-4f49-3042-8c8e-a76f2b9b9d5f | -3.3502 | -45.4223 | 2025-11-28 00:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| bc71ac08-3050-30ed-9f64-6e422d00bccd | -3.8432 | -47.0446 | 2025-11-28 00:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 27657a54-e0e6-3d6e-9b61-a1c384818625 | -9.3813 | -40.3501 | 2025-11-28 00:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 358.7 |
| 372b6dcc-7bf0-3ec4-91a5-835e75b16a23 | -3.9717 | -47.3018 | 2025-11-28 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 11566489-4a7c-3d47-98eb-9954f14723bb | -2.5135 | -45.5644 | 2025-11-28 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 225.7 |
| c9c3b72f-ada5-35e1-9eba-ec95143ac4a7 | -9.4004 | -40.3474 | 2025-11-28 00:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 145.6 |
| 89ad091a-6649-3c9f-be2c-bbef96541bb6 | -2.7006 | -45.2214 | 2025-11-28 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 239.1 |
| c707724d-3c14-33f1-adf5-27ac830fa2e2 | -2.719 | -45.2433 | 2025-11-28 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f6f406d1-f146-31a9-bff2-04dd0580a6ba | -3.8617 | -47.0657 | 2025-11-28 00:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 9b987377-f0bb-3070-a941-27a95477e808 | -2.532 | -45.5638 | 2025-11-28 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 3fee1e49-246a-3475-abab-b08e4232dd7b | -2.42 | -45.7462 | 2025-11-28 00:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e0e52b71-e622-3a3a-92db-9d5d04981af1 | -3.8978 | -47.2395 | 2025-11-28 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 8b77df89-aeba-327e-800c-2635e94b3a8e | -9.3813 | -40.3501 | 2025-11-28 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 312.3 |
| b28d4f42-a474-341f-a480-e39a0f749e33 | -3.8618 | -47.0438 | 2025-11-28 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 0e7dcfa6-d1f3-3edb-93b9-c97907cf19ae | -9.4004 | -40.3474 | 2025-11-28 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 132.9 |
| 3bd340c6-f27d-3518-8e76-fc76c34653df | -3.8617 | -47.0657 | 2025-11-28 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 957bb04c-cf33-3f13-8add-620e9f56a0a9 | -3.8431 | -47.0666 | 2025-11-28 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 0a13d39e-bf51-3fc6-8fb4-d354cc28f2eb | -4.1795 | -43.7422 | 2025-11-28 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| fb507b0d-406a-3be3-9f1a-64beda5b60a3 | -9.4 | -40.3722 | 2025-11-28 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 19c923f3-5e38-354b-a9a7-59ce4ca67870 | -2.532 | -45.5638 | 2025-11-28 00:10:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 6d7eb0cb-cf3a-3162-b1b3-9450372b1fbd | -9.3809 | -40.375 | 2025-11-28 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 337.9 |
| eb2da4c6-04e5-326c-aff7-a86e4747879e | -4.1794 | -43.7653 | 2025-11-28 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d3082188-a81a-3713-8cfb-d7d78f45f9ea | -2.4198 | -45.7908 | 2025-11-28 00:10:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 83d2af47-fe3d-3454-92d3-a1c6c490bcef | -2.5135 | -45.5644 | 2025-11-28 00:10:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 5d846d2b-20b9-37d5-8144-79ef5e7c5f85 | -4.9473 | -48.6204 | 2025-11-28 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 97f725ba-1bc1-364c-b0d4-1660ecf0b68c | -3.8631 | -40.653 | 2025-11-28 00:10:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 7bd66d44-5521-3593-a381-37067a7313c9 | -3.9717 | -47.3018 | 2025-11-28 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 4163231a-7ddf-39ce-8615-745edf6744c6 | -3.8432 | -47.0446 | 2025-11-28 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 389fc3a8-63a2-3e75-90cd-572371536acd | 0.4648 | -60.4494 | 2025-11-28 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 40.9 |
| b48c9b6a-387a-3851-8d61-8ede39a0a1a6 | -1.8245 | -54.332 | 2025-11-28 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 42871988-b563-36c7-bfcb-948b94e653dc | -2.4199 | -45.7685 | 2025-11-28 00:10:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| efb52c39-eaa5-3926-bd31-eafb799c376a | -2.42 | -45.7462 | 2025-11-28 00:10:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 163b2a22-dbc5-301d-b4e3-be4e5037fba4 | -5.5396 | -46.5115 | 2025-11-28 00:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 7f2ee685-0553-3489-864b-c6be4c08f0c4 | -5.5398 | -46.4893 | 2025-11-28 00:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 789ac3b3-346a-3d71-a68c-e5c69a5e056f | -21.6473 | -48.615 | 2025-11-28 00:10:00 | GOES-19 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ee9f7ae0-164a-394e-a7ef-b6b031e8f5a5 | -2.5135 | -45.5644 | 2025-11-28 00:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 19e57a1e-6710-309f-b1bb-95b92c8031f5 | -1.8245 | -54.332 | 2025-11-28 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 1c5b4e1a-6e0f-3b52-8044-2c36bb21223f | 0.4648 | -60.4494 | 2025-11-28 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 74ae7eea-8b79-3708-bb42-2d40bf0a2961 | -3.1684 | -48.6113 | 2025-11-28 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 21c79903-3859-3680-9673-5a36138cb24b | -2.532 | -45.5638 | 2025-11-28 00:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 4b4e5120-df22-3541-91ca-7442f37c0180 | -9.4004 | -40.3474 | 2025-11-28 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 119.5 |
| d2d3978a-3e51-35f6-aa21-729cb8bd6a9b | -5.5396 | -46.5115 | 2025-11-28 00:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7b681eae-6e94-3c59-86de-1ed14f117a29 | -3.8618 | -47.0438 | 2025-11-28 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 83453372-edcd-3ca2-a7dc-7158dd490e93 | -2.7104 | -47.4147 | 2025-11-28 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a8fa2e1e-2775-3dca-a9e2-1ee77239536e | -19.9973 | -49.9861 | 2025-11-28 00:20:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.3 |
| f5c7703b-60f6-39d0-bb91-89da6b4ac219 | -9.4 | -40.3722 | 2025-11-28 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 146.4 |
| 329aa874-bf31-3d3e-bdc1-9565fa80902e | -3.8978 | -47.2395 | 2025-11-28 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 66fd10ff-772e-3b39-891e-48fdf9bb6945 | -9.3809 | -40.375 | 2025-11-28 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 321.0 |
| 436cc6f8-f7b5-3923-b220-20e90a344a66 | -2.5136 | -45.542 | 2025-11-28 00:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a61655a4-42d5-3d2c-912d-3ed9e1352b7f | -5.5398 | -46.4893 | 2025-11-28 00:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 30f902ea-2629-3177-a653-86beb496f6d4 | -3.8431 | -47.0666 | 2025-11-28 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 7437c52d-ccf2-3b3d-a581-26f310696bdf | -9.3813 | -40.3501 | 2025-11-28 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 244.8 |
| 53fd5c04-e536-3a48-a883-01685fbaae06 | -2.42 | -45.7462 | 2025-11-28 00:20:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 19d05f75-071d-3f33-93af-0a769ada0d59 | -5.5582 | -46.5102 | 2025-11-28 00:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 9036d989-203b-33a3-a085-313a36a1b1bb | -3.8432 | -47.0446 | 2025-11-28 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| dec3ea14-ec8b-3bd6-88bb-73aa94875e9d | -4.9473 | -48.6204 | 2025-11-28 00:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 39723dfc-e3fe-3db2-b506-9e3cecd7bb4b | -3.8617 | -47.0657 | 2025-11-28 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 208.5 |
| 05816c48-0804-3da0-a1a5-fdc9ebead3a0 | -20.4715 | -47.4711 | 2025-11-28 00:30:00 | GOES-19 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0a9f87f8-7b2c-37e4-afca-fc1cff582e61 | -9.4 | -40.3722 | 2025-11-28 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 147.7 |
| 711c78e8-0525-3123-9307-c1752df9c8a5 | -2.42 | -45.7462 | 2025-11-28 00:30:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ab106e50-5a61-3b62-bbe8-5801fff0952b | -2.4949 | -45.5649 | 2025-11-28 00:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 66c95823-71b3-3019-b303-202108c3fb26 | -1.8245 | -54.332 | 2025-11-28 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8d73af15-2191-3892-8a58-dc878f06eb5b | -3.8431 | -47.0666 | 2025-11-28 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 183.0 |
| e64ec3be-6281-3bed-ab52-e277d9cba452 | -3.8617 | -47.0657 | 2025-11-28 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 227.3 |
| 62ab9a2d-94f2-3b5e-831e-138d26119519 | -2.532 | -45.5638 | 2025-11-28 00:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 59323f0b-4bae-38fb-b5b9-4d10d02b7576 | -9.3809 | -40.375 | 2025-11-28 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 371.0 |
| 0af13d19-defe-3a86-8414-9044e5afe96d | -5.5398 | -46.4893 | 2025-11-28 00:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 2b2a320a-28f9-34f7-b294-94d595ba9964 | -3.8978 | -47.2395 | 2025-11-28 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5ad01610-79f0-306c-ac04-09d078828117 | -5.5582 | -46.5102 | 2025-11-28 00:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 9b6da354-aa87-37f8-82a4-6e0222c33d95 | -2.5136 | -45.542 | 2025-11-28 00:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9fd6f995-dfa0-3877-b90b-1d071dd7301c | -3.8432 | -47.0446 | 2025-11-28 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 77c3ee62-e15e-3ff7-b53d-3dec96f7c0ec | -5.5396 | -46.5115 | 2025-11-28 00:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7484ba1f-9077-3ef3-aa03-633efc012ec0 | -2.5134 | -45.5868 | 2025-11-28 00:30:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 4b3614d1-fcbc-31c7-a65c-cae72fffc110 | -9.4004 | -40.3474 | 2025-11-28 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 3f26c1fa-9714-33b9-803f-e42f89ba2610 | -2.4148 | -47.2268 | 2025-11-28 00:30:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8b16c182-aee1-317e-ab20-236bc62ff4be | -9.3813 | -40.3501 | 2025-11-28 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 259.9 |
| ac90de19-9170-3ec4-a2f0-95621ff418de | -5.5584 | -46.488 | 2025-11-28 00:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |


[Clique aqui para ver as próximas entradas](README2.md)
