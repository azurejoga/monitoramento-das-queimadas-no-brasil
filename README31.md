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
| 7178d43a-3746-3a4d-a6dd-34d39516c243 | -3.9624 | -49.0096 | 2026-09-09 13:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| d4c2d5ff-3379-34de-9abb-f1ddf39d0581 | -10.6995 | -46.038 | 2026-09-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 666.9 |
| 1d011744-6780-327d-9ff8-19ee9b84ad44 | -10.7387 | -45.9649 | 2026-09-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 3f884c59-1ebb-391c-9fbb-adc4bc0f2e48 | -3.2545 | -50.0957 | 2026-09-09 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| b9c6d1bf-463b-36a1-b34a-ceca3c32fc0f | -6.8708 | -46.0126 | 2026-09-09 13:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 0837e414-32a4-3881-88ab-674bb466d4fb | -9.7889 | -43.48 | 2026-09-09 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 1e644d23-01e3-33ce-b88c-1d348f929b64 | -3.2731 | -50.0741 | 2026-09-09 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 253e612f-a286-3729-826e-d4634151500e | -10.6999 | -46.0153 | 2026-09-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 5c133b9e-a7a0-3047-a4d0-1c46f24535b9 | -10.7578 | -45.9624 | 2026-09-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 5f813d08-1c11-320b-8704-8a3db74fda74 | -10.7674 | -60.7666 | 2026-09-09 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b82177fb-9969-36e4-9abd-52ecd9207949 | -3.2546 | -50.0747 | 2026-09-09 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| d3855b48-4a84-3b82-8162-3cc25c8f1b37 | -10.7391 | -45.9422 | 2026-09-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.8 |
| c12be44a-b1ea-34b3-9b2e-29e71aff2b8f | -6.1726 | -44.6432 | 2026-09-09 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 83353d32-ca47-3e92-86cd-2c77c8ea3955 | -10.7182 | -46.0582 | 2026-09-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 9388b699-ff12-3de3-99a1-624fb275abf3 | -3.5406 | -48.1889 | 2026-09-09 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8962011a-1470-366c-a882-1cbf013be3f8 | -10.7395 | -45.9194 | 2026-09-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| ab74ee75-b7c9-3df4-b88b-acf54541f492 | -10.2563 | -45.2062 | 2026-09-09 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 6a2c2ab7-265f-3135-8b06-c2fea9da8275 | -10.7674 | -60.7666 | 2026-09-09 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| cb96c5bd-3b23-3972-b131-c5633ed19a35 | -3.2731 | -50.0741 | 2026-09-09 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 226.0 |
| 360a2d58-8715-3604-b2ee-6900c25d9bca | -6.8708 | -46.0126 | 2026-09-09 13:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 5e53c475-3884-362f-b0e1-6aefd97c6735 | -9.7141 | -43.3956 | 2026-09-09 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 133.4 |
| aaea1fe5-c6f8-3802-9e92-58a5d4b47adb | -9.7134 | -43.4428 | 2026-09-09 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 237.2 |
| ab0d2d7a-e914-3b8e-9e5f-18793e64329a | -10.2559 | -45.2292 | 2026-09-09 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 373b2a3e-7d4e-36eb-a68e-13ad0bbd153e | -10.2372 | -45.2087 | 2026-09-09 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| aed97cfe-d2f7-3710-9531-1b1e1a20ea71 | -9.7892 | -43.4564 | 2026-09-09 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 3e1e25f9-505f-312c-ab4a-6dbeabfd4e4e | -10.7391 | -45.9422 | 2026-09-09 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 96a29558-e352-3d96-a635-c5bf369e6731 | -9.7138 | -43.4192 | 2026-09-09 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 187.4 |
| 0d5a4afe-f115-35a7-810c-480f3ff55ad0 | -9.7889 | -43.48 | 2026-09-09 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 361b7529-005f-3234-a79d-a630ca9e221a | -10.7395 | -45.9194 | 2026-09-09 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| c2693a32-168e-30ba-9c38-838b4898794e | -6.852 | -46.0141 | 2026-09-09 13:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4f51d1d5-6892-3548-bf88-05d8771c6bad | -9.6947 | -43.4217 | 2026-09-09 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 229.1 |
| ff531af1-4059-3e19-bb25-a78dbd9ba46b | -3.2546 | -50.0747 | 2026-09-09 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 50a02ec9-fca5-318a-8941-09308f0fa6c9 | -3.2545 | -50.0957 | 2026-09-09 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 982edef1-3afb-3dca-8d58-dec945884419 | -6.3304 | -43.8253 | 2026-09-09 13:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 419718a0-0bbf-370b-9657-187279346a8d | -10.7395 | -45.9194 | 2026-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 744be69b-cde4-30dd-88f2-06f38653a08d | -6.8708 | -46.0126 | 2026-09-09 13:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 189.8 |
| a43aa132-8d58-3692-b08e-e8223a8a7d1e | -10.7387 | -45.9649 | 2026-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 067022c2-e07b-3322-8fd3-150f4205da92 | -13.2477 | -61.7342 | 2026-09-09 13:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1be43f91-f7cf-33f9-927c-c957febb2167 | -13.2476 | -61.7536 | 2026-09-09 13:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ec575a8f-9c2f-3d02-81c3-2b4e48c6db06 | -6.1726 | -44.6432 | 2026-09-09 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 43fd90ba-d1fe-3dee-bccf-581ac6ffc375 | -13.2852 | -61.7899 | 2026-09-09 13:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| dbdf8997-a2c3-3a7c-8a7e-bb3ef749b157 | -2.9391 | -50.4832 | 2026-09-09 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 41929378-5469-324d-871c-fbe8aaba3977 | -9.7127 | -43.4899 | 2026-09-09 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| e105e2d2-25d1-38db-af96-715296fbcb4a | -10.7578 | -45.9624 | 2026-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| fad2a749-be36-37bb-a54b-67ade9d192c7 | -13.2666 | -61.7524 | 2026-09-09 13:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 82b89113-82f9-3622-a9e2-b72c22ca8cc5 | -3.2545 | -50.0957 | 2026-09-09 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 164.8 |
| f4fa079e-9917-3dd8-ac98-40cb04a938eb | -3.5591 | -48.1882 | 2026-09-09 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 999dd048-f498-3957-add4-c8391b7a5d9c | -10.2372 | -45.2087 | 2026-09-09 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 7974443f-fcf7-3f71-a1d2-64a1e6f879cf | -3.2731 | -50.0741 | 2026-09-09 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 160.9 |
| b446b20f-85a1-3227-ba88-3d324df0ed50 | -6.1538 | -44.6446 | 2026-09-09 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b022f33c-7089-306f-9d6c-a8da3e2ccf19 | -13.2667 | -61.7329 | 2026-09-09 13:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4a55ff5f-95b9-395a-b929-2fc5fabac869 | -10.7182 | -46.0582 | 2026-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e8f4fcd6-ba55-3013-a164-346503f4bbe3 | -9.7698 | -43.4825 | 2026-09-09 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 54308cc2-a4dc-33fb-b032-bbef2c6c5280 | -9.7889 | -43.48 | 2026-09-09 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 165.9 |
| aaf54560-5304-38a5-99b9-53c859bbc54a | -10.7674 | -60.7666 | 2026-09-09 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4e495cf4-ba1f-33ab-9fc5-e69d708e70ae | -3.2546 | -50.0747 | 2026-09-09 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 192.6 |
| 71fd42aa-ddc4-39e3-ba81-5f944e699453 | -9.7892 | -43.4564 | 2026-09-09 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 8bf9a328-ef13-3107-85b0-2e7abb25d6db | -10.6995 | -46.038 | 2026-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 580.4 |
| 6f9e3020-4255-33b9-8667-791a436cd818 | -10.72 | -45.9446 | 2026-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 65452ea0-ec14-3b8e-b1a2-fb9bfb1374f1 | -10.6999 | -46.0153 | 2026-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 298.1 |
| 16cd2721-e187-3f75-ba0a-9765f1c72b1c | -10.7391 | -45.9422 | 2026-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 426.4 |
| 4f756ede-11e2-34f7-baa2-26b93c7b0829 | -6.3304 | -43.8253 | 2026-09-09 13:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| bee5c9d3-a569-30b3-bb0f-8257e286d93c | -6.1726 | -44.6432 | 2026-09-09 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7d2aaf0c-7ad0-34c1-9c8c-9ff6aeff710a | -9.7138 | -43.4192 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 286.8 |
| 533e12e1-0c44-3a56-9a7e-7d3996b7ecc7 | -3.2545 | -50.0957 | 2026-09-09 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 06e37ae2-bb17-3266-b4a3-b54252ccfb41 | -3.2731 | -50.0741 | 2026-09-09 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 196.9 |
| 14bee301-a0c3-365b-a8eb-37ecc95ae894 | -6.3304 | -43.8253 | 2026-09-09 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b138bb4e-d1bd-3abd-9ee3-659911f927d0 | -10.7395 | -45.9194 | 2026-09-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| a9e57229-ede1-3a42-8139-773485099cd4 | -9.7134 | -43.4428 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| f410d6c7-7087-338f-a9ed-d2a7d310848c | -10.7391 | -45.9422 | 2026-09-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 366.3 |
| 3363941f-64d0-37af-9642-7a4ebe6e9662 | -6.852 | -46.0141 | 2026-09-09 14:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 017f1f26-0981-33a1-88f2-fb97de8bd9c1 | -10.7387 | -45.9649 | 2026-09-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 10f2900e-9e68-30cd-a51b-da732b0bcaa9 | -9.7698 | -43.4825 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 487726c5-3151-31e1-8759-666f06d80f71 | -9.7892 | -43.4564 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d4d12741-d081-3584-9668-f66273f9b0b7 | -10.7578 | -45.9624 | 2026-09-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 0d9ae4ee-6487-32b0-a7f7-e154cd19ea3f | -9.7141 | -43.3956 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 158.7 |
| 28b2dffd-49fa-3ebd-bb95-ad81e9a7ec71 | -13.2852 | -61.7899 | 2026-09-09 14:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| bca0ab74-6914-3f62-a88e-60f5ee4d3ff4 | -6.3307 | -43.8021 | 2026-09-09 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 726a1f70-7539-3533-8d2f-1ecf02377950 | -6.8708 | -46.0126 | 2026-09-09 14:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 7bbdfc9b-2813-3624-83fd-4a5fbc188dc9 | -3.8604 | -44.0585 | 2026-09-09 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 539258e7-92f7-30a1-8ffc-31091839eb7a | -7.4693 | -46.1406 | 2026-09-09 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| bd1c3df8-7631-3928-bc2a-e6966ce71a2e | -9.6951 | -43.3981 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 199.4 |
| 5e90b420-bda5-357c-99e7-263048ea7f3c | -9.7702 | -43.4589 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 6a7347d1-d903-36dd-a60f-b857ac7e356b | -9.6947 | -43.4217 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 584.1 |
| a11a73d0-507b-354a-97c8-57b3edbf484c | -9.6937 | -43.4924 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 21084e00-f4f6-31ba-985a-7c5fce7cb348 | -3.2546 | -50.0747 | 2026-09-09 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| a71c5b8a-ea8b-35b7-8f81-417f042f49e3 | -9.7889 | -43.48 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 20159e43-04b6-3e44-9fd5-37d59bc3b2d1 | -9.7131 | -43.4664 | 2026-09-09 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 9b0bb20d-6484-3dfe-9e49-37d3af7bbafd | -10.7182 | -46.0582 | 2026-09-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 8fc741f1-7fce-347e-9976-abcf043f7da1 | -7.4693 | -46.1406 | 2026-09-09 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 2beaa142-893b-3ab4-949f-230ee926506e | -9.7141 | -43.3956 | 2026-09-09 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 300.7 |
| 0542a31d-e725-3791-9c68-cbe58b6c7d2f | -7.1389 | -42.1051 | 2026-09-09 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 3971f3bb-7ec3-394c-b11f-fa82474e1f54 | -9.7889 | -43.48 | 2026-09-09 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 2ed34e25-7431-3cb3-9cf3-2021ff522171 | -9.6951 | -43.3981 | 2026-09-09 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 229.4 |
| a8d18b86-1b4e-3055-9a4b-4951545a299c | -13.2917 | -61.109 | 2026-09-09 14:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| a341b340-2e75-3943-9037-90b0f2b2a9b3 | -9.7138 | -43.4192 | 2026-09-09 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 661.3 |
| c6c557ff-6f63-34fb-9d3f-6d4accc72ddf | -6.3307 | -43.8021 | 2026-09-09 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e11bdfac-d3c9-3dd2-90f7-96ae93675a19 | -6.3304 | -43.8253 | 2026-09-09 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 2a0c91d9-2f64-30f2-9fde-118d029dc7fd | -10.7391 | -45.9422 | 2026-09-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 258b344b-54ee-3b4d-a139-721a82b7eb2f | -3.2546 | -50.0747 | 2026-09-09 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |


[Clique aqui para ver as próximas entradas](README32.md)
