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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37ae12ab-a67a-3f07-95d3-8b168165d76d | -9.53586 | -68.52374 | 2024-11-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 404cd710-5722-3eaf-9292-2cef4bf908a8 | -9.52798 | -66.65247 | 2024-11-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 446e4d12-a824-30e8-8b2a-47c52a425acf | -9.5273 | -66.65744 | 2024-11-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca6d39ca-e92e-385f-ad82-1cfb343ce466 | -9.52328 | -66.65178 | 2024-11-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b41e86aa-e29a-31ce-8ffd-23472415a26c | -9.52261 | -66.65678 | 2024-11-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f8b86d8-702a-3a03-9e56-4421cbcb7745 | -9.51739 | -68.59362 | 2024-11-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d2edae1-caae-3cf0-9add-5f9d7bfb34d5 | -9.51685 | -68.59735 | 2024-11-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f952d67-c5aa-3b27-9558-05e5c7b571f0 | -9.27233 | -71.89912 | 2024-11-01 06:14:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dbdcf62-d3f7-38e1-a308-84151a34d775 | -9.27225 | -71.89886 | 2024-11-01 06:14:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fdb482a-bd5c-3b45-9d4e-4fd24aa2c25f | -9.25864 | -71.87397 | 2024-11-01 06:14:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e74b1ac6-faeb-324e-a6ba-e48945eddf97 | -9.25795 | -68.33392 | 2024-11-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e3c570a-1101-3555-b4fe-fad2b62a4354 | -9.13168 | -68.18364 | 2024-11-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12cd0db4-af5c-3018-bb58-8e24a81f7f38 | -8.95086 | -72.41934 | 2024-11-01 06:14:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01bbb054-693e-3b51-9bfb-8b901de3ad07 | -8.81985 | -67.69946 | 2024-11-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59f15746-b64e-3f92-870a-e3342e28b3d7 | -3.0353 | -49.4901 | 2024-11-01 06:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0e433ef0-7a02-3b5d-a650-0b995122aee0 | -3.0354 | -49.4688 | 2024-11-01 06:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c040a550-2a7e-3881-9703-55d3b4e2c54f | -3.0538 | -49.4895 | 2024-11-01 06:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| aecd0505-df21-3e98-964a-ff7ea8d24355 | -3.0353 | -49.4901 | 2024-11-01 06:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f8099ae8-93e8-3781-bf78-b74c24cc3900 | -3.0354 | -49.4688 | 2024-11-01 06:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9d0743e0-f68b-3e9c-a65c-4e2c7386f8a7 | -3.0538 | -49.4895 | 2024-11-01 06:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3fde0590-1162-3f47-aa3e-d4af7d8c7c83 | -3.0539 | -49.4683 | 2024-11-01 06:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 94354aad-e5d3-36c2-b59b-b9d896ccc4a9 | -0.79331 | -63.08017 | 2024-11-01 06:46:00 | AQUA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f7c83719-bf5d-3448-a067-dcbab6f8c995 | -8.61816 | -69.71793 | 2024-11-01 06:48:00 | AQUA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a9ab1068-5176-3609-a97a-b7b1c5faa7dd | -10.11795 | -67.59277 | 2024-11-01 06:48:00 | AQUA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 53a96130-817c-3b4d-975d-3c10480cdf36 | -10.09705 | -68.36154 | 2024-11-01 06:48:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| de6beefc-0ee9-39fd-b1a7-6e3ea28153ad | -10.09572 | -68.37048 | 2024-11-01 06:48:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0471b85e-35a8-30f7-984b-38168057d7c6 | -10.09439 | -68.37942 | 2024-11-01 06:48:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 070a9dca-77fd-3b77-94c7-ab7553d94d5d | -10.08686 | -68.36916 | 2024-11-01 06:48:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 15ef8643-f01d-3c82-ab69-cdbbca00841f | -3.16 | -45.07 | 2024-11-01 07:05:10 | MSG-03 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42c5e3fd-71ae-3bcd-bf09-db80305dcfdf | -23.9717 | -54.0925 | 2024-11-01 07:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 99.0 |
| 064e2794-6af5-3e36-9d3f-a750c465e9b5 | -23.9929 | -54.0882 | 2024-11-01 07:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| d440a3ac-efb8-340c-bdea-487a8642961a | -17.6661 | -57.5233 | 2024-11-01 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| d33f9d6f-7714-35e5-8bb6-72b7d7635a79 | -17.6664 | -57.5028 | 2024-11-01 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.0 |
| aaa8b4d9-b83d-3648-9785-490faf30b2d9 | -19.4878 | -56.6227 | 2024-11-01 07:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| d15909b4-8ba4-3c00-bb1e-b47a44c47413 | -19.4882 | -56.6017 | 2024-11-01 07:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 6e17a2a4-2a7b-3f1f-a83d-0b6f668f4216 | -19.5063 | -56.7039 | 2024-11-01 07:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| c285b862-6bbe-3d73-8266-0df7179024c3 | -19.5079 | -56.6199 | 2024-11-01 07:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| c38e2688-c3f9-36b9-b527-ff5e243813cc | -19.5083 | -56.5989 | 2024-11-01 07:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 18baeebe-6737-39f9-b093-6b67b00615b9 | -19.5087 | -56.5779 | 2024-11-01 07:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 28344821-fef1-386d-a765-d718e53fc58d | -23.9929 | -54.0882 | 2024-11-01 07:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| ea20d675-4a97-3eac-8131-51977c9b83e2 | -9.9187 | -64.8058 | 2024-11-01 07:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 70eca071-6b76-3b7c-89ad-9d0469637e31 | -17.6467 | -57.5051 | 2024-11-01 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 9f9fa56e-1197-3926-8b2e-1240af00a371 | -17.6661 | -57.5233 | 2024-11-01 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 697590b1-ac39-322b-ba26-d5218f5ffb79 | -17.6664 | -57.5028 | 2024-11-01 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.3 |
| 9ea268ed-d353-35ac-a0ee-c76bbdc58d63 | -17.6861 | -57.5004 | 2024-11-01 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 9e1a463b-266d-3b3d-a10b-142d8c3a7980 | -19.5083 | -56.5989 | 2024-11-01 07:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| ad44edb6-63e0-3c34-97bc-8393dd662f6c | -19.5461 | -56.7192 | 2024-11-01 07:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 139ac9ce-bbc6-3a4b-b37c-38b132d16ebb | -17.6467 | -57.5051 | 2024-11-01 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 2b51fe57-59fc-3dd7-8750-edf6481eac7f | -17.6661 | -57.5233 | 2024-11-01 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 37bed706-08d8-3ca3-8955-c435631e8646 | -17.6664 | -57.5028 | 2024-11-01 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 0548859a-eaba-38a6-b7a2-85b371aad858 | -17.6861 | -57.5004 | 2024-11-01 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| ff79a0c7-1461-3cb3-8cdc-924c4efee18f | -19.5079 | -56.6199 | 2024-11-01 07:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 5506a0c1-abf7-33aa-a59e-f7c290b19833 | -19.5083 | -56.5989 | 2024-11-01 07:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| a068c8ac-0f95-3565-b642-3017bc3c5b89 | -17.6664 | -57.5028 | 2024-11-01 07:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.4 |
| ae578061-e4bb-3867-9b27-90de717c6d0c | -17.6661 | -57.5233 | 2024-11-01 07:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 61418d96-d04a-35ca-9cd5-8ebac90166ed | -17.6467 | -57.5051 | 2024-11-01 07:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 8d02c7f3-87f4-3855-9460-aa54eb61f184 | -17.6861 | -57.5004 | 2024-11-01 07:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 67e44a2e-9e74-3632-8ed1-d527a150fca3 | -23.9717 | -54.0925 | 2024-11-01 07:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 88.2 |
| 3f042681-f81f-39e0-a471-aa4161a081b5 | -17.6664 | -57.5028 | 2024-11-01 08:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.1 |
| 545da293-9c2a-33c1-8391-4f33a75d872c | -17.6661 | -57.5233 | 2024-11-01 08:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 727a3b47-40d8-3920-800b-841a9672c0a8 | -17.6861 | -57.5004 | 2024-11-01 08:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| a0a49aa3-ce65-3cc9-9d20-7098a310d51a | -23.9929 | -54.0882 | 2024-11-01 08:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |
| 099bfa65-5f34-344f-b57b-9f48b86077f3 | -23.9717 | -54.0925 | 2024-11-01 08:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 109.6 |
| 68424ee5-ef0d-3b16-9f5d-677568bb1939 | -9.9187 | -64.8058 | 2024-11-01 08:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| a8e28341-e861-3f8e-9168-6c2d0dfce6d3 | -17.6664 | -57.5028 | 2024-11-01 08:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 174.8 |
| c3e2d452-c2a8-3fc2-ad2e-cbcb1e8cbd7e | -17.6661 | -57.5233 | 2024-11-01 08:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.3 |
| b74e9975-5929-33df-8545-7f880cbfbd4c | -17.6467 | -57.5051 | 2024-11-01 08:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 061b9e9e-674b-313a-adad-8ec35de86c74 | -17.6861 | -57.5004 | 2024-11-01 08:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 1555b134-0796-36d8-8f02-d77678931013 | -9.9187 | -64.8058 | 2024-11-01 08:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 417d3ad3-ac22-3e1c-97e8-51d4b829421c | -17.6661 | -57.5233 | 2024-11-01 08:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 0d1968b7-36f0-304a-8323-0258bbe12915 | -17.6664 | -57.5028 | 2024-11-01 08:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.3 |
| 5a4e4939-33ee-3cbf-9a1c-061ea3f4a6ba | -9.9187 | -64.8058 | 2024-11-01 08:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 1de6ca39-195d-3ac5-a750-29736403fe55 | -9.9187 | -64.8058 | 2024-11-01 08:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b4ae97f7-7195-32bf-bf6d-84be1e0c35de | -9.9187 | -64.8058 | 2024-11-01 09:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5ea34fc2-48c8-393c-831d-151128de94d0 | -17.6664 | -57.5028 | 2024-11-01 09:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| f73bf861-5f5f-3e45-8486-a005f128d883 | -17.6664 | -57.5028 | 2024-11-01 09:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.0 |
| cf176bf6-0086-332a-ba45-ebd8be6a5446 | -17.6664 | -57.5028 | 2024-11-01 09:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.3 |
| ffa338ec-cf33-3bba-bbfb-1f666cf1cc6f | -17.6664 | -57.5028 | 2024-11-01 10:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.4 |
| aa7dd2aa-9fe8-3bd1-850e-d801a8315b49 | -17.6664 | -57.5028 | 2024-11-01 10:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.7 |
| 0d099df7-8f92-31e8-91a7-c39a333b9ce0 | -17.6664 | -57.5028 | 2024-11-01 10:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.5 |
| cd81f040-eba4-3a49-b13d-8299794ce497 | -17.6661 | -57.5233 | 2024-11-01 10:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.4 |
| e2d666d4-c749-394c-8d17-41358f31f2ba | -17.6664 | -57.5028 | 2024-11-01 10:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 179.1 |
| 73a24203-c621-39af-abd3-39ed3c649cdd | -17.6661 | -57.5233 | 2024-11-01 10:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.0 |
| efcd41d5-0d38-38f5-9ab6-8002acddcba3 | -17.6664 | -57.5028 | 2024-11-01 10:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 173.6 |
| 933908cd-77e9-34fc-aa6b-9fa50ae6c0d5 | -19.4654 | -56.7515 | 2024-11-01 10:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.6 |
| b854d7f7-f0f2-32db-82ba-a2d41f836fe0 | -19.49 | -56.74 | 2024-11-01 11:03:34 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a9636a7d-0235-358a-a6d5-ec471c75bb2b | -17.6664 | -57.5028 | 2024-11-01 11:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 167.5 |
| e9f6af14-548a-3e9e-a0a7-d0c256fa1f58 | -17.6467 | -57.5051 | 2024-11-01 11:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 6a75e223-276d-32cd-9fa3-58eeaf00e333 | -17.6664 | -57.5028 | 2024-11-01 11:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.4 |
| 61027289-0f82-352c-a86d-e4ff024e753b | -17.6467 | -57.5051 | 2024-11-01 11:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.4 |
| 9ed0febe-1832-3e95-b324-b1d4d502c482 | -17.6664 | -57.5028 | 2024-11-01 11:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 194.9 |
| f4dcd942-e868-3bef-9207-fe3f31b00484 | -17.6467 | -57.5051 | 2024-11-01 11:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.1 |
| 0432b393-1d9c-3b24-aff0-713d42fc0eb3 | -17.6664 | -57.5028 | 2024-11-01 11:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 214.7 |
| feb4639f-c694-31bc-b114-23ce31df5bdd | -17.6467 | -57.5051 | 2024-11-01 11:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.1 |
| 0ef82e89-16bb-3553-909a-201c1bac5f8a | -17.6664 | -57.5028 | 2024-11-01 11:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 233.4 |
| 862a3d4e-ae12-3ce7-9b9d-fec234680ac6 | -17.6467 | -57.5051 | 2024-11-01 11:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.8 |
| d3934aef-9dc6-32ec-a783-167a51fb638c | -17.6664 | -57.5028 | 2024-11-01 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 265.1 |
| 83c3c48c-9f8c-3764-8928-a6f43d43fb87 | -17.6861 | -57.5004 | 2024-11-01 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 4830f658-8721-3cd2-a094-14d9f0f36698 | -19.49 | -56.74 | 2024-11-01 12:03:36 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a545766e-1574-3021-a30b-adab3db88a76 | -19.48 | -56.66 | 2024-11-01 12:03:36 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README56.md)
