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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 212a75a0-d4f7-300c-8faf-9f260b2dc5c2 | -1.28625 | -53.65565 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e068c38d-940b-3721-9d45-1b5b331056f9 | -3.92173 | -46.99009 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5bb1ab39-289a-313e-8314-c8e39574302d | -3.92258 | -46.9842 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 02aa9e10-0164-3dc7-87f0-fbf97bdaa410 | -0.06049 | -51.65677 | 2024-12-27 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7115e234-5bc2-3dad-b1b1-49db7e3bc8fd | -1.8921 | -53.28763 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 227d1ce3-ba4a-3a19-acfe-7c7c3238a7d9 | -3.93536 | -46.99193 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0b46121a-3779-3f79-9188-2432ff419f56 | -1.32229 | -53.42183 | 2024-12-27 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e95438c1-9607-3289-a9d3-3c8aea1ccbb6 | -1.89275 | -53.28344 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23b89ed2-679c-3fe1-a835-4a369cc78414 | -2.99707 | -48.0514 | 2024-12-27 05:20:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8fe1ea56-f545-35b4-aff7-a631ed7f390c | -3.06432 | -47.77291 | 2024-12-27 05:20:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d3c0994-af53-39be-8ace-d0bdeb84d86c | -3.59428 | -53.78663 | 2024-12-27 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f4b5ea9-4506-31df-99d0-72691844e83b | -1.35659 | -53.67778 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d15e9a2-e954-3ae6-a491-73c07847fd9d | -1.64152 | -45.87215 | 2024-12-27 05:20:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ddad27a-3a49-3a53-84d4-b9493816f7b3 | -3.5937 | -53.7906 | 2024-12-27 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f968b914-7863-363f-a2c1-a2dcf7cf591e | -1.4422 | -53.68212 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c46c2b3b-80fc-3808-8bf6-434f9b163ca7 | -1.64857 | -45.87322 | 2024-12-27 05:20:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 998ca7f0-9700-3fa1-a908-69560bc75914 | -3.93062 | -46.98556 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b656ee80-1a12-3899-88bc-1827e6c78990 | 0.96933 | -59.53296 | 2024-12-27 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30682835-9464-3c25-ba58-5627f13aca61 | -3.03824 | -53.23901 | 2024-12-27 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dec20c6-22f3-33cb-865c-9fec47275420 | -2.15537 | -53.74015 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c5c8e7d-7d92-38f4-a5a6-f60edd1b5a48 | -3.92856 | -46.99086 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3839ac3b-4234-321a-9b74-1bc5f4ecda9e | -3.00189 | -48.06236 | 2024-12-27 05:20:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3b3dc54-4508-3e21-bd46-1ac89a53f5d1 | -1.79777 | -53.22695 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a768aaa5-a6f0-36e7-862b-f37bc7c94d36 | -2.99634 | -48.05637 | 2024-12-27 05:20:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7fca4b40-9d2e-31a5-a773-a97a08039707 | -1.55689 | -53.501 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5605a99b-6451-3979-aa81-d256f8b8c616 | -1.44642 | -53.68277 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 080c8498-6751-3b38-b44a-478aeca26b33 | -2.15107 | -53.5969 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fcf9940-017e-3532-a703-b964a61e81b1 | -3.1406 | -46.35275 | 2024-12-27 05:20:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37ab17af-5d09-3f24-adf6-e7c3d87aa5e2 | -2.15597 | -53.73623 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48ca361c-1d54-3b81-b42d-c327269d0f9f | -2.15658 | -53.7323 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94509768-7b7a-37fb-8e4c-5632c32fe71a | -3.9366 | -46.99255 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ce037e9f-2461-3b64-a118-5e88f0d19c3d | -1.1926 | -53.59063 | 2024-12-27 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 073efc93-c68a-36ad-9ac3-7877ce4ffd32 | -1.59935 | -53.37035 | 2024-12-27 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e13914ff-095c-3edd-b9f9-25a62784ccfe | -3.06511 | -47.76766 | 2024-12-27 05:20:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7977d218-ec3e-34f7-8663-9eeb1dbea3e7 | -1.55199 | -53.5044 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2ee0446-db39-30f8-b63f-b2b88c86ce6f | -1.60368 | -53.37098 | 2024-12-27 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8c6ca9e-7214-3cd5-ad54-736552a61781 | -2.44256 | -51.7985 | 2024-12-27 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07002453-51b2-3935-9986-603bd72f7b2e | -1.55625 | -53.50512 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 04581495-316e-32fc-9902-fc36cb9138fa | -12.27799 | -64.3747 | 2024-12-27 05:22:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcfa5b68-4ce5-366a-a2f8-68c7b8e091db | -16.19007 | -58.95909 | 2024-12-27 05:22:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 176d12b8-6060-3857-a8d8-61b8bf3ad499 | -15.23007 | -59.92844 | 2024-12-27 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a35333d5-a416-3126-87a8-e76958683b21 | -15.23066 | -59.9244 | 2024-12-27 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 288b2c12-5f27-347c-aceb-19092ae8cd8b | -15.23358 | -59.92898 | 2024-12-27 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32f09679-8d77-3d73-9cb4-3b16c23468ac | -15.23126 | -59.92038 | 2024-12-27 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc002d14-d52e-3b24-a120-871a6a90f1d3 | -14.52749 | -59.74969 | 2024-12-27 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28a47cb9-b044-312f-847b-ed8473993fe4 | -22.00583 | -57.30262 | 2024-12-27 05:25:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f6a6627-be14-33fe-abe8-eadd725e87d6 | -15.48782 | -60.04328 | 2024-12-27 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26cdaf4c-83c1-330d-88c1-5ddd5b5f3719 | -15.23417 | -59.92495 | 2024-12-27 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06afb6a1-eec4-3277-b903-136cfdd4ccdf | -15.23477 | -59.92092 | 2024-12-27 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d32ea808-94a3-3599-a8a1-528c15511c68 | -15.23298 | -59.93301 | 2024-12-27 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8d4fc01-ecb1-3ab6-b068-4ad79394c77f | -14.4888 | -59.96756 | 2024-12-27 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87b7f733-7c5a-3650-bff8-6a449fdabea1 | -28.03705 | -55.20561 | 2024-12-27 05:27:00 | NOAA-20 | PIRAPÓ | RIO GRANDE DO SUL | Brasil | 4314555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1deb1eb3-821b-38e9-bb86-90b747296dc5 | -5.9024 | -43.4883 | 2024-12-27 05:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 18f6ae1b-426d-38cf-825c-e163aab4c643 | -3.9364 | -46.9746 | 2024-12-27 05:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 689bee75-b39f-31d6-8853-71b7d6a53cd8 | -5.9211 | -43.4869 | 2024-12-27 05:50:00 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 047c64a4-03c0-3b2a-ad6d-45bb75e3ab6d | -5.9024 | -43.4883 | 2024-12-27 06:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4f2814a0-18eb-35ae-9b1f-6bc061fc363a | -5.9024 | -43.4883 | 2024-12-27 06:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c2749ba4-a448-39c5-9a6f-a5513cbcf48c | -1.5535 | -53.495 | 2024-12-27 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1a5916f6-c455-30ec-9f67-81f916e9fb4c | -21.61802 | -52.32001 | 2024-12-27 06:16:00 | AQUA_M-M | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 28.8 |
| f6a940b6-3d07-31be-adea-a55a66644d91 | -12.35151 | -64.17242 | 2024-12-27 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a89ac12-f28c-329d-9b9a-5f71dd34fb0d | -12.35164 | -64.17329 | 2024-12-27 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b466a443-08e7-3c85-bf84-88892c951362 | -5.9024 | -43.4883 | 2024-12-27 06:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ec312602-c4f9-37f9-848c-487d5cbfe38f | -5.9024 | -43.4883 | 2024-12-27 06:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b7943ccb-bf27-34cb-aa0f-7e0e60fc37c4 | -5.9024 | -43.4883 | 2024-12-27 06:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| af04a44a-c57a-3530-83e6-9d4143fb3fed | -5.9024 | -43.4883 | 2024-12-27 06:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 714d24c0-d9d3-3026-b7f7-457ce6e8c731 | -5.9211 | -43.4869 | 2024-12-27 07:00:00 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 07b4885f-cf9e-3c60-a3ea-1827e0a37208 | -5.9211 | -43.4869 | 2024-12-27 07:10:00 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 479c8974-51e8-3c98-9b10-7c3c37983439 | -5.9024 | -43.4883 | 2024-12-27 07:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 7fba7089-06e3-3197-86ac-948de80284cb | -5.9211 | -43.4869 | 2024-12-27 07:30:00 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| a2dac87b-6e51-37ba-baf6-e144c69aca7c | -5.9024 | -43.4883 | 2024-12-27 07:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 095f2c7d-9688-3973-ab3f-6794107c50c4 | -5.9211 | -43.4869 | 2024-12-27 07:40:00 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 0ce39ec8-f88a-3ffe-939c-65042329c0b9 | -5.9211 | -43.4869 | 2024-12-27 07:50:00 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 1ae74945-ad58-39b8-8f79-a0e51e66915e | -3.42 | -44.9 | 2024-12-27 12:00:00 | MSG-03 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b40051b-97bb-3975-a966-9cd5939b013f | -5.55746 | -41.09206 | 2024-12-27 12:10:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 0a13da7d-a195-3c6b-a6da-b14dedba7308 | -4.15974 | -40.55203 | 2024-12-27 12:10:00 | TERRA_M-T | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 5c467f28-b8fa-3ee3-bfa6-0ba14e6d0a41 | -4.59033 | -38.46739 | 2024-12-27 12:10:00 | TERRA_M-T | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 224.6 |
| 6ad1670d-deb3-371b-a5c4-75264758c60e | -5.35844 | -39.34428 | 2024-12-27 12:10:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 22.6 |
| a7a81ad6-6b27-3114-940d-4ebc4e6490a2 | -4.94208 | -38.5877 | 2024-12-27 12:10:00 | TERRA_M-T | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 457b0508-7454-3cbe-b1d0-3bdcc1f24103 | -3.71772 | -41.68804 | 2024-12-27 12:10:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 86bbe193-c6b8-34c3-8800-686ef7e66c27 | -5.54172 | -42.94535 | 2024-12-27 12:10:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 7e42146b-65b6-3f59-841b-75a568c279db | -4.16105 | -40.54298 | 2024-12-27 12:10:00 | TERRA_M-T | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 368779b1-143a-3331-9850-fc02d4aa0bdd | -2.82768 | -42.38778 | 2024-12-27 12:10:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 06090ef9-9665-34ba-a8eb-5c53304fe257 | -3.48975 | -41.22398 | 2024-12-27 12:10:00 | TERRA_M-T | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4d461524-0fc6-3d51-b136-a1afcbeb755f | -3.69898 | -43.41437 | 2024-12-27 12:10:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0a85cbd0-145e-37e4-8a4d-f641b7657855 | -3.28305 | -41.87215 | 2024-12-27 12:10:00 | TERRA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7c2402e1-0d13-3de0-be98-137d9857d5f8 | -4.55399 | -40.50405 | 2024-12-27 12:10:00 | TERRA_M-T | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 13ea7536-2b19-3a51-8b0d-6190fcf2f0d9 | -3.2787 | -41.21255 | 2024-12-27 12:10:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 20.5 |
| eb0a8392-e8e9-38be-8ca0-01da4e009537 | -5.83866 | -43.15335 | 2024-12-27 12:10:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 118970a0-34cd-3cca-91b2-b77b41cb8301 | -6.48247 | -37.52122 | 2024-12-27 12:10:00 | TERRA_M-T | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 19b14766-b6dc-3427-b0c3-318ef2ceb283 | -3.66728 | -41.63995 | 2024-12-27 12:10:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 9d345d27-7627-3baf-9643-4747b7e8b24a | -4.55528 | -40.49508 | 2024-12-27 12:10:00 | TERRA_M-T | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 75f4579a-d9d1-3c23-9bf2-3ad29eb1bcfe | -5.35717 | -39.35314 | 2024-12-27 12:10:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 72d8d3ed-4eb5-3adc-97ae-5330b6df7f79 | -5.79328 | -38.2431 | 2024-12-27 12:10:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 18.3 |
| c713a2e7-5be2-3fb5-aed1-9aeddb2be7fc | -5.24634 | -41.39056 | 2024-12-27 12:10:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| aef3d6c1-9a81-3ccd-9155-9f3da5c99e4a | -3.53596 | -40.59328 | 2024-12-27 12:10:00 | TERRA_M-T | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 79d01b41-22be-32c4-ab4b-1fb7155718c1 | -5.7377 | -35.55849 | 2024-12-27 12:10:00 | TERRA_M-T | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 2be752a9-8000-3923-8e9c-1561eb61334a | -4.55553 | -38.1266 | 2024-12-27 12:10:00 | TERRA_M-T | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 579243fe-e939-33cf-a2d6-c236c0d014e2 | -5.64288 | -43.7144 | 2024-12-27 12:10:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 6844ccdd-f579-3dba-8903-5f73bfdd1d4d | -5.65067 | -43.70871 | 2024-12-27 12:10:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 41e625a7-7021-36c9-88a0-7a23a5d76359 | -5.62911 | -38.10141 | 2024-12-27 12:10:00 | TERRA_M-T | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |


[Clique aqui para ver as próximas entradas](README17.md)
