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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35cf8e8c-f474-3f85-83d4-72dcd6c2ba71 | -4.07053 | -47.65622 | 2025-12-11 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 83700a8b-1b1a-3d90-a36a-eb9d3246c00b | 0.94187 | -50.08918 | 2025-12-11 00:15:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2a19530f-d2d4-3577-a458-6157a411b609 | 0.94344 | -50.07814 | 2025-12-11 00:15:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 16.6 |
| bf30dc5f-3092-3696-a85b-4427d5d56f31 | -6.0315 | -43.7105 | 2025-12-11 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| eacd54e9-5225-3383-a6cd-c0f81abfe8ed | -4.5322 | -44.0449 | 2025-12-11 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f6e52885-4790-35fc-be79-d4c51b00c9c0 | -2.9798 | -45.1214 | 2025-12-11 00:20:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 0f581408-2ac4-3841-95c2-ea322703d336 | -2.9799 | -45.0988 | 2025-12-11 00:20:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 10acb22a-c8ac-399a-8a21-03c9e851d693 | -1.6944 | -46.563 | 2025-12-11 00:20:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 209.0 |
| cf23ac41-ddd9-301a-ba3f-c210aac7ecb5 | -6.0317 | -43.6873 | 2025-12-11 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 8dd0abad-4a17-390e-970b-bdaa5d12684c | -3.2525 | -46.4075 | 2025-12-11 00:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| e86a77f0-aa9f-3f94-9897-fd562ada9bdd | -3.2289 | -47.4847 | 2025-12-11 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| a15caca6-4f33-3c73-a5ae-696845754907 | -2.2169 | -45.4159 | 2025-12-11 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 130.3 |
| c6a4c1a7-aaa9-3888-bc4e-773534ba6cfc | -9.9711 | -36.1719 | 2025-12-11 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 107.4 |
| ddd15b7f-e1c4-3f80-b8ec-63f18aeaa5ba | -3.229 | -47.4629 | 2025-12-11 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5f2c3d62-5358-366c-9074-08f581bb66d6 | -3.2524 | -46.4297 | 2025-12-11 00:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 3a9e04a4-a59e-3f15-902d-c8c647c0eb21 | -1.6759 | -46.5413 | 2025-12-11 00:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 852c1472-a9b8-3a9f-98f9-6a75eeeb703b | -1.6758 | -46.5634 | 2025-12-11 00:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 104ced53-a949-3068-8205-3854f4cedf7b | -4.0866 | -43.6779 | 2025-12-11 00:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f701e5f0-7a06-37fb-ba71-43213644405c | -9.8542 | -36.2465 | 2025-12-11 00:20:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| 4957030b-b249-3472-a1e2-ad6613c3374d | -9.9518 | -36.1753 | 2025-12-11 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| 6ae36083-67d4-3cbf-9ef3-85e33fe954f3 | -4.0865 | -43.701 | 2025-12-11 00:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e0984810-536a-3bb2-980b-9dff84e33f9c | -4.5508 | -44.0438 | 2025-12-11 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 145497f9-4d20-3e78-86a6-4638e9b8ac1b | -1.6944 | -46.541 | 2025-12-11 00:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 180.6 |
| da3f8484-6a2d-35dc-852d-70e642c67ac0 | -4.0678 | -43.702 | 2025-12-11 00:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ee3a1c20-dfd9-30a6-b4b8-6c58d26bede9 | -2.217 | -45.3935 | 2025-12-11 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3c277fd2-76bf-3fec-b6a5-60767a2383fb | -1.7129 | -46.5627 | 2025-12-11 00:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| bc0b895e-0e0e-3041-a0a9-423d689ad066 | -1.6759 | -46.5413 | 2025-12-11 00:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7bda7fa7-9d1e-341e-9ffc-b6430db1c020 | -6.0317 | -43.6873 | 2025-12-11 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 6886dff8-b37f-3792-84ba-a5dfd90c73ab | -4.0678 | -43.702 | 2025-12-11 00:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e94f6033-1af9-39f7-8575-8e14537e8702 | -4.0865 | -43.701 | 2025-12-11 00:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 51837048-4df0-339b-89a2-c65146131c36 | -3.2525 | -46.4075 | 2025-12-11 00:30:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 27093059-bf10-3206-a0d5-e94d5427f443 | -3.229 | -47.4629 | 2025-12-11 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 55611fa4-72b7-3a52-97a1-2175d777ec61 | -2.9798 | -45.1214 | 2025-12-11 00:30:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 526ad0c5-46b9-3df8-b38b-6c8031e81c55 | -4.0866 | -43.6779 | 2025-12-11 00:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| d50184e1-1dab-38ac-ae8a-852e24967c08 | -1.6944 | -46.541 | 2025-12-11 00:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| c2560aad-84cf-375f-8532-3a35521635b1 | -2.2169 | -45.4159 | 2025-12-11 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 99f69215-d07b-3368-bee6-4962106e5f8b | -2.9799 | -45.0988 | 2025-12-11 00:30:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 000184a9-280e-3b91-8c04-d856846559cd | -1.6758 | -46.5634 | 2025-12-11 00:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e01b6a76-4689-3cdc-86a8-9561d4bf3908 | -3.2524 | -46.4297 | 2025-12-11 00:30:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1722abc6-4164-30bb-9396-b274d91bfc8b | -3.2289 | -47.4847 | 2025-12-11 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| bd4e13b0-ccf4-3d80-9970-51f5bd5a6259 | -4.5508 | -44.0438 | 2025-12-11 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 9649dd27-a8ca-31a3-8520-a8aabd6668a2 | -1.6944 | -46.563 | 2025-12-11 00:30:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| bdcc1649-0b19-3ded-bbd2-bba6d861e52e | -6.0315 | -43.7105 | 2025-12-11 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| b062a230-f923-3cef-93ab-abf70b61d4fa | -1.6944 | -46.541 | 2025-12-11 00:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| cd5e3e96-fd00-3fb6-8134-a27c8ea902e4 | -3.229 | -47.4629 | 2025-12-11 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 374c35d4-7ce2-330c-a469-62100fcbac41 | -6.0317 | -43.6873 | 2025-12-11 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 01077d58-e499-344d-9712-0cc6a5f4b3cd | -4.0865 | -43.701 | 2025-12-11 00:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e2c3ac01-3cdb-3a76-9391-ce5bfe14c53e | -6.0315 | -43.7105 | 2025-12-11 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| bd22ee26-17bc-3c40-9b47-33e8bc89ebd2 | -2.9799 | -45.0988 | 2025-12-11 00:40:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7d4f6158-0284-3ec6-a4e3-60c8e42ff479 | -2.9798 | -45.1214 | 2025-12-11 00:40:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 224.8 |
| 5f133876-15eb-3d5e-8079-035eb851f1e0 | -2.2169 | -45.4159 | 2025-12-11 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 54197ae1-0e68-3185-9041-715145903fce | -4.5508 | -44.0438 | 2025-12-11 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f72b9403-0a6e-3309-bb81-4a3e4e2e9c5f | -1.6944 | -46.563 | 2025-12-11 00:40:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| e327d0a8-e49d-3d7b-84d7-6ececf38334a | -4.0678 | -43.702 | 2025-12-11 00:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 733b894a-8b49-30ed-a227-f4a22754af84 | -2.9797 | -45.144 | 2025-12-11 00:40:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| cbe55ccb-4886-3188-9acc-19e539470302 | -2.5501 | -45.6975 | 2025-12-11 00:50:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 553a6722-8726-3cc5-8ba2-c7456ba80c77 | -4.5508 | -44.0438 | 2025-12-11 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| bbf9de9e-35bd-302a-ba0d-b0d9b5cc70d4 | -3.229 | -47.4629 | 2025-12-11 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0be7e21c-89af-33d1-97a5-da969be4ab9b | -4.0866 | -43.6779 | 2025-12-11 00:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| e0e4e494-9c1c-3898-b9ef-f593411f8523 | -4.068 | -43.6789 | 2025-12-11 00:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 035bbd37-10a4-32ad-8bce-2b39a24a1f48 | -4.0678 | -43.702 | 2025-12-11 00:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 9645fb58-c4d4-3738-980f-ad8dc96488d8 | -2.9798 | -45.1214 | 2025-12-11 00:50:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 2136abcd-eebc-3d9a-9ea7-118a97ca3165 | -4.0865 | -43.701 | 2025-12-11 00:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 330ec78c-6fe9-360d-a645-96992789cac2 | -4.5322 | -44.0449 | 2025-12-11 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 35f9831c-f00a-3435-9cc9-ce9d4049a210 | -4.5507 | -44.0668 | 2025-12-11 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f11e19ab-efa7-3146-93da-c9c02bc6fafa | -3.2289 | -47.4847 | 2025-12-11 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7ef1e443-b22c-36b5-9a6f-b216f4ce1019 | -2.5315 | -45.6981 | 2025-12-11 01:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 7c83ca5e-b32f-3610-a150-0dfacf39710f | -6.0317 | -43.6873 | 2025-12-11 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e591e6f6-318c-3397-afaa-2e58caa93fa6 | -4.0678 | -43.702 | 2025-12-11 01:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 42a4412b-f6c2-3477-a566-5fa48699abb2 | -12.5046 | -58.3591 | 2025-12-11 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| e24c5729-bd61-3661-878f-7de6c58cceb4 | -6.0315 | -43.7105 | 2025-12-11 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| e84c61a0-c708-3476-8020-df14a90872d8 | -2.5501 | -45.6975 | 2025-12-11 01:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1610044c-2165-37da-8613-c53fcfa2cbd5 | -12.5046 | -58.3591 | 2025-12-11 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 24466a69-2dda-3bf6-9138-6e98de1cd444 | -2.5315 | -45.6981 | 2025-12-11 01:10:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7b24ba3d-ca15-38f6-8135-1792113372a2 | -6.0315 | -43.7105 | 2025-12-11 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 22576085-db28-3bf8-828d-e11ac5b7da5a | -3.229 | -47.4629 | 2025-12-11 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 7de93358-5df1-36b6-8484-e40ccb568b2f | -2.5501 | -45.6975 | 2025-12-11 01:10:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 09df92ec-0050-3a35-bfc4-aef0f2ec2185 | -4.0678 | -43.702 | 2025-12-11 01:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 726581bb-998c-3970-9264-b5c8fdd8e907 | -6.0315 | -43.7105 | 2025-12-11 01:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e1e14ae5-e9cd-3469-836f-2070bfd4b9c6 | -2.5501 | -45.6975 | 2025-12-11 01:20:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2f51c789-2360-30bd-949f-9d01475203c4 | -4.0678 | -43.702 | 2025-12-11 01:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| d2a903a6-cb64-394a-86ba-d4dc222845e1 | -6.0315 | -43.7105 | 2025-12-11 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 28ab4b49-fab4-3114-9091-e6c0874218e3 | -6.0315 | -43.7105 | 2025-12-11 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| f94e537f-ced9-329c-9677-01b171f9b48a | -3.229 | -47.4629 | 2025-12-11 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 8d894afa-9a40-351a-9039-9fce4f5557d6 | -4.0678 | -43.702 | 2025-12-11 01:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 57b0c229-1d16-3987-9872-db80fb681a9a | -6.0315 | -43.7105 | 2025-12-11 01:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 41f1d088-6bb1-366b-b212-9c4ed6c1deff | -6.0315 | -43.7105 | 2025-12-11 02:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e1fdc4bb-f4b8-3ab7-82d7-aff1e262ec73 | -6.0315 | -43.7105 | 2025-12-11 02:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 4350a396-55c4-3eb8-8c16-6c2eae9408c0 | -6.0315 | -43.7105 | 2025-12-11 02:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e83be81a-49ca-3380-be6a-b7227e9e8484 | -6.0315 | -43.7105 | 2025-12-11 02:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e7aee7c6-f947-3e78-ac1a-ed563c26acca | -1.8067 | -54.0516 | 2025-12-11 02:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c96b932f-815d-3762-bb02-0055df292e56 | -1.8067 | -54.0516 | 2025-12-11 02:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 43f94d3d-7223-3ee5-9c33-84839650a7cd | -1.8067 | -54.0516 | 2025-12-11 02:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| dc2481d8-5930-3a50-ae43-e26c84b87e13 | -6.0315 | -43.7105 | 2025-12-11 02:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 326627c4-be1f-3546-8769-8704b52ab69e | -5.1609 | -37.70269 | 2025-12-11 02:57:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| fb813fc6-30c4-39ac-9a2c-ddd58664b8e0 | -6.73227 | -35.02531 | 2025-12-11 02:57:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b7496105-fc0f-3750-9f5b-97fa911b7295 | -5.15382 | -37.70138 | 2025-12-11 02:57:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 11e85fb5-8fd6-37ec-ab7f-c9ead22623ba | -6.73303 | -35.02111 | 2025-12-11 02:57:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 915b9654-b4e2-321c-8865-bc2f7791cd07 | -5.8207 | -35.38763 | 2025-12-11 02:57:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c1ef5e29-30c9-32f7-88a9-d07cd5241a60 | -6.73892 | -35.02221 | 2025-12-11 02:57:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |


[Clique aqui para ver as próximas entradas](README5.md)
