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
| 6e86de14-1e4b-3a4d-a983-990831c1f8e5 | -12.4462 | -58.5023 | 2026-06-30 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 66655de9-5eea-3c2f-9692-ca025838a487 | -7.4306 | -49.8942 | 2026-06-30 00:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ee6bf410-03f2-343d-85b9-a74cfc0faf7c | -11.2279 | -54.3036 | 2026-06-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 6ff584e2-5572-38d4-abbd-d75008247c8f | -10.1388 | -52.4017 | 2026-06-30 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 9acba8a5-ec4a-31d0-85e3-ad6c4672cedb | -7.4309 | -49.8729 | 2026-06-30 00:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e0af7eaa-088c-3adf-a61d-ddd170fcb3a8 | -11.2277 | -54.3241 | 2026-06-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 202.8 |
| aa2d3534-c195-3eaf-86c7-c812455c978e | -17.712 | -46.7798 | 2026-06-30 00:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ed5eeb10-ef7e-3d33-b549-b8a1043b424b | -13.245 | -56.8167 | 2026-06-30 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6e7a5ce5-c534-33b2-bf7c-6caf2ce2e853 | -13.264 | -56.8149 | 2026-06-30 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f8b732db-26a2-3696-be36-d31abecb581f | -6.3135 | -43.6411 | 2026-06-30 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| d85b3f13-61ac-383c-a560-55c60c2bbd4c | -11.2088 | -54.3258 | 2026-06-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f132034a-8c9a-3511-84c7-6cd16c603b7b | -12.4464 | -58.4825 | 2026-06-30 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| fd701941-bf71-35b4-850c-e1ba98fbbd1b | -13.2643 | -56.7947 | 2026-06-30 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 170.1 |
| ce00dbf5-fb39-3575-aaed-4bd99f2cba7d | -12.8543 | -44.386 | 2026-06-30 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 94dea822-6124-3f8d-a7fa-74241dda529e | -12.2222 | -56.5467 | 2026-06-30 00:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 60283453-5837-3acb-a3cb-1fe971064c9e | -9.6037 | -56.9276 | 2026-06-30 00:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 38cf4c82-dbc2-3df7-84a8-1241f9f5e7e7 | -10.9401 | -43.0355 | 2026-06-30 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| d63767c6-caf3-3984-9694-218eb396dc5f | -13.2452 | -56.7965 | 2026-06-30 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 159.8 |
| c5c83406-141e-31eb-81c6-4a91fbd370a1 | -11.2279 | -54.3036 | 2026-06-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 7c6ef892-5cdd-3577-bb62-354ae3599071 | -7.4309 | -49.8729 | 2026-06-30 00:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| d4dcdd23-cb0a-3fdb-82cc-20a6956e12a9 | -6.3135 | -43.6411 | 2026-06-30 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 781d950b-0b6b-3ff7-82c2-a70da7bd74ea | -11.2277 | -54.3241 | 2026-06-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 159.7 |
| a572b7c3-22d6-3d9c-8f11-b3f96e3c9a59 | -13.245 | -56.8167 | 2026-06-30 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7772001c-8824-368a-99a9-0e492e8251e1 | -11.2468 | -54.3019 | 2026-06-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b195155d-09e8-3e67-b742-4e7abb81656d | -7.4306 | -49.8942 | 2026-06-30 00:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 4c395b69-842b-32f3-8d09-809b0b9c81b0 | -12.2222 | -56.5467 | 2026-06-30 00:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a4945498-9cda-32e6-bace-d00c9486c02e | -12.4462 | -58.5023 | 2026-06-30 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 0b30b7c5-da25-3279-a433-17d7a49a1db2 | -17.712 | -46.7798 | 2026-06-30 00:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2c929e15-ffd3-36bc-bf82-60ee8f6bfbc4 | -13.2452 | -56.7965 | 2026-06-30 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| c381af7c-6f98-3b7b-9bdc-86f6ab6290ad | -13.2643 | -56.7947 | 2026-06-30 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 142.6 |
| c09daf93-a132-3ffe-9240-04b7724eb3ff | -12.4464 | -58.4825 | 2026-06-30 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ea2e7007-90d1-3245-9ebf-a00bdea3a573 | -9.6037 | -56.9276 | 2026-06-30 00:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 221f823a-282b-36e7-8045-d92485faa909 | -12.8543 | -44.386 | 2026-06-30 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 85de40a6-b091-3a6f-b24b-b06d98fc7717 | -13.264 | -56.8149 | 2026-06-30 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 82bca267-1d38-3feb-bef5-a2be189a04ae | -7.4122 | -49.8743 | 2026-06-30 00:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 93ba0038-a68c-33df-bdb4-4a5580aef2fd | -10.1388 | -52.4017 | 2026-06-30 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 9062835f-33fd-3516-8149-f7d1a7ae3e70 | -13.2452 | -56.7965 | 2026-06-30 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 36aa336f-5331-3761-aa2e-054c3c22926f | -13.264 | -56.8149 | 2026-06-30 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 30c87e54-1539-33eb-9071-789792a74151 | -10.1388 | -52.4017 | 2026-06-30 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1be2cf1a-cfb2-34d7-90b3-51a47763599d | -12.4462 | -58.5023 | 2026-06-30 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 1cb1465f-40d9-3564-8591-e6de85f1c0cf | -12.4464 | -58.4825 | 2026-06-30 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c871d642-8b3d-30f1-85cd-a738cb9f2285 | -17.712 | -46.7798 | 2026-06-30 00:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 22411108-89a9-381f-8a3b-8f8f43d05141 | -7.4309 | -49.8729 | 2026-06-30 00:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 9a34347e-1987-3a86-afbb-3947c7d745dd | -6.3135 | -43.6411 | 2026-06-30 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3e263878-7576-3159-b5a4-1279070934fa | -13.2643 | -56.7947 | 2026-06-30 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| ad3ab256-e54b-3e89-9094-89841d79cf57 | -11.2279 | -54.3036 | 2026-06-30 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.4 |
| c523d8cd-d34c-3e40-9dff-9a101f856ba0 | -9.6037 | -56.9276 | 2026-06-30 00:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e88cb25d-3980-31a2-b985-2916eb07a47b | -12.8543 | -44.386 | 2026-06-30 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 75e673ec-8e63-320e-85ed-5aa2a6ae5df4 | -11.2277 | -54.3241 | 2026-06-30 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| ded8aec6-d041-305b-a6bb-7c0b14461cb0 | -10.9401 | -43.0355 | 2026-06-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 25985dbe-295c-3410-ac3d-334f1ea22b23 | -17.43756 | -47.16207 | 2026-06-30 00:20:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 91804b0d-175f-31f7-b2df-7e2ecdca4b17 | -17.7059 | -46.7751 | 2026-06-30 00:20:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| afc05d5e-5d88-3079-9255-28ff4f55daee | -17.71479 | -46.78034 | 2026-06-30 00:20:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 7d3420b7-892f-3523-a435-3dfa14ac5be9 | -16.19462 | -59.31277 | 2026-06-30 00:20:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 5adedf74-4a91-3ca7-ae7e-1163fc161af6 | -18.24949 | -53.84656 | 2026-06-30 00:20:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a3ddbf7b-fd12-3627-bf9e-bc63c40ffe66 | -16.19736 | -59.34105 | 2026-06-30 00:20:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| ddfd1cb9-8af1-35e0-a91c-f0f2dcf3184e | -16.62915 | -49.76287 | 2026-06-30 00:20:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e1410360-4816-3412-903d-a3e854563fbf | -20.97366 | -49.7439 | 2026-06-30 00:20:00 | TERRA_M-M | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 59e332d9-0c68-3764-800b-bed733fc612c | -22.79547 | -49.34473 | 2026-06-30 00:20:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d4405b2f-8248-3c98-8f90-601f6f858d9b | -17.70985 | -46.80048 | 2026-06-30 00:20:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 60a3744f-f54a-3ad5-acbb-0210555f3a9b | -22.78662 | -49.3462 | 2026-06-30 00:20:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 3869296c-8668-3446-b468-bb581cd1607e | -18.23887 | -53.84137 | 2026-06-30 00:20:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4dc9e11f-b765-315a-b43c-b17dd18c4ca8 | -17.43945 | -47.17413 | 2026-06-30 00:20:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 262a8b12-b227-358c-b602-4053ec585496 | -16.63811 | -49.76152 | 2026-06-30 00:20:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 319e9f54-ea9d-3809-ad3d-9f5b230f1e74 | -17.70788 | -46.78786 | 2026-06-30 00:20:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 144.0 |
| c498f3db-62ba-3bcc-83fa-ea0718199d55 | -20.32814 | -50.88639 | 2026-06-30 00:20:00 | TERRA_M-M | NOVA CANAÃ PAULISTA | SÃO PAULO | Brasil | 3532843 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 7d06eac5-9942-33a5-a502-55414ab950b5 | -16.63674 | -49.7519 | 2026-06-30 00:20:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 962aedfb-9822-3d0f-8e5e-91f0c941948b | -17.71684 | -46.79302 | 2026-06-30 00:20:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 49.4 |
| ba5fac3c-9e9c-39eb-bf9f-cb09bee4aa67 | -18.23946 | -53.84788 | 2026-06-30 00:20:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 29531ea1-df35-3709-bb1d-cdd6d7095392 | -17.71818 | -46.78625 | 2026-06-30 00:20:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 97292f8b-84bf-31f8-bc65-37073b744d68 | -21.3178 | -48.53418 | 2026-06-30 00:20:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cec85e26-4c49-3ac1-8b75-e6bc4c7c5e7c | -16.19449 | -59.31921 | 2026-06-30 00:20:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0277af73-d5e6-3331-b4da-cae302ca0ff5 | -21.31922 | -48.54392 | 2026-06-30 00:20:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 59e86631-0d5b-3a3e-bcd0-7897e278eeca | -16.62777 | -49.75327 | 2026-06-30 00:20:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 66cb572a-eb0f-3efd-95c1-d562106ea389 | -18.24039 | -53.8536 | 2026-06-30 00:20:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 559da359-2bab-349c-a0a4-a30c6efdd67f | -12.21149 | -56.56644 | 2026-06-30 00:22:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| ff8d2788-3a96-3456-863a-5a5a31733fc9 | -14.62951 | -54.47007 | 2026-06-30 00:22:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7260e6d0-bff3-3a53-a44f-30bc3b5f5049 | -9.20398 | -45.34009 | 2026-06-30 00:22:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| dfb8043d-0fc5-3946-bb42-0f84a30f8cdd | -12.50415 | -48.27099 | 2026-06-30 00:22:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| eaed202c-cd8c-386b-9ff5-f695fd552537 | -11.90294 | -57.13365 | 2026-06-30 00:22:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| e7a89e1e-4e7f-3ce9-95d7-e9f688468e92 | -10.90801 | -56.85271 | 2026-06-30 00:22:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 7f1780e8-09a5-3732-aa3f-ea3ca5c332b0 | -11.10722 | -54.14661 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 927f5cd2-1610-3427-ad64-6442e90bec4f | -13.25846 | -56.80744 | 2026-06-30 00:22:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 188.6 |
| a8aefae0-c53f-3c86-8287-bc321f078364 | -12.19669 | -52.87018 | 2026-06-30 00:22:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 975e0fc9-2ea3-308e-bdab-aa9a274dc26d | -10.38601 | -49.60086 | 2026-06-30 00:22:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| aad90b3c-5f89-3615-8280-f9faa0576bbb | -11.92635 | -43.40114 | 2026-06-30 00:22:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 22d23adc-e3d3-3758-b3cb-b912e3575c30 | -14.62803 | -54.45837 | 2026-06-30 00:22:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0ed0238e-efcf-3480-bc38-a819de7c334c | -10.29459 | -50.18212 | 2026-06-30 00:22:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| b5c10f9b-7ce6-3e6c-a2ab-e60e32479f73 | -11.3148 | -54.47259 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 80d27a1f-31f9-3147-a562-849283261763 | -11.63946 | -59.00557 | 2026-06-30 00:22:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| af9c0a98-24ce-3a50-af97-ab20042a2d7a | -10.38449 | -49.59028 | 2026-06-30 00:22:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a44eb4c1-12b9-3919-bf0a-b7b99f6fadc7 | -10.7881 | -54.10664 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| e047bdef-f6db-325f-83e5-92d18d0ba1bf | -12.50588 | -48.27647 | 2026-06-30 00:22:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 197ee77c-85e1-33c7-836c-fca6a72dca63 | -10.90772 | -56.84715 | 2026-06-30 00:22:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 19874e56-f0c8-37df-8658-c402a13fc97e | -10.30192 | -57.13454 | 2026-06-30 00:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 2d5ceb18-40cd-340a-95a8-ac3d048bc168 | -11.21292 | -54.32342 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 491d1677-281e-3b12-be86-57e50e0e9a03 | -11.15506 | -49.18526 | 2026-06-30 00:22:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 4e4865df-4cab-3452-be85-34d94ef04597 | -9.75116 | -49.03366 | 2026-06-30 00:22:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 4afcc02a-6970-39ca-ba53-78b79cf12127 | -11.23632 | -54.31393 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 797b0fc9-2e45-36e0-89b2-870791b25c21 | -11.48781 | -50.47736 | 2026-06-30 00:22:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README2.md)
