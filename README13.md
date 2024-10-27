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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02862ad9-3934-38d1-9e74-208ab51d8000 | -1.7875 | -46.3844 | 2024-10-27 00:35:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e15b1ff1-20d9-3072-a028-f6b61281884d | -1.806 | -46.384 | 2024-10-27 00:35:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b2cfb38a-ff8f-3495-9dd0-54964258b91c | -1.906 | -59.9839 | 2024-10-27 00:35:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| defeab57-fdd2-33a9-9239-975116da6058 | -1.9243 | -59.9837 | 2024-10-27 00:35:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 67206cfd-336c-3567-8407-5832dc0998e0 | -2.3578 | -47.6641 | 2024-10-27 00:35:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 1b2bf300-bc8c-37db-8b37-d014f6ea18b6 | -2.4567 | -45.8567 | 2024-10-27 00:35:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| bd5b41b6-4a46-30ec-8d19-44e288a229ae | -2.4568 | -45.8344 | 2024-10-27 00:35:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c15b85ac-8b23-3b23-adea-d3a6bc183a76 | -2.4598 | -50.412 | 2024-10-27 00:35:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| bf589dd1-a2ba-3a26-a795-f1ba648f4601 | -2.4753 | -45.8561 | 2024-10-27 00:35:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 132a2dc9-7745-3a50-b0da-2229109b6f18 | -2.4753 | -45.8338 | 2024-10-27 00:35:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 990d47fa-5859-3cb8-b20e-d551826b85e7 | -2.4786 | -50.2858 | 2024-10-27 00:35:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a0d21445-3ed3-303e-8ee1-2a1e5f117689 | -2.486 | -48.0507 | 2024-10-27 00:35:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| aab0a5f8-90ee-3834-b8db-8f36dadc4ddd | -2.6321 | -54.2975 | 2024-10-27 00:35:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 9ea48628-c1c0-3052-9b8d-be1b6bc57bf1 | -2.6482 | -49.2465 | 2024-10-27 00:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b15acba1-e9b0-3890-ad55-19a942577100 | -2.6483 | -49.2253 | 2024-10-27 00:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7dfca0be-1074-3179-90c6-4ed65c06a071 | -2.6505 | -54.2971 | 2024-10-27 00:35:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| fea53446-3a02-3315-94a2-6f0a563ad1e4 | -2.7033 | -49.33 | 2024-10-27 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| a3d71d41-f5ac-3d14-a846-7302cdc0e7cf | -2.7034 | -49.3088 | 2024-10-27 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 2d6733a2-b5f4-3fd8-a80a-634443fc9c0c | -2.8145 | -49.2418 | 2024-10-27 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2d2fce25-824f-3569-b465-78176dd7338a | -2.8329 | -49.2626 | 2024-10-27 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e6e33986-5547-3b23-81cd-3fbf53e433c7 | -2.833 | -49.2413 | 2024-10-27 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 4510e572-668e-3e6e-8967-28071b5aa94b | -2.8465 | -45.8666 | 2024-10-27 00:35:21 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8943dc8d-e66f-3692-b238-dde41680fbf9 | -2.8501 | -45.0131 | 2024-10-27 00:35:21 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 339.8 |
| ddc13501-d50d-3e0d-9222-4a24af3cbe11 | -2.8502 | -44.9905 | 2024-10-27 00:35:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 330.3 |
| 0c13d402-8bca-31c2-a92d-bd30e4de198d | -2.8422 | -51.8148 | 2024-10-27 00:35:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 83753a63-e67f-3f1f-843e-aa65d758899d | -2.8423 | -51.7942 | 2024-10-27 00:35:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 999c6caa-c755-375e-9e9a-923644f4277e | -2.8687 | -45.0125 | 2024-10-27 00:35:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 268.0 |
| da5c17ad-3ecb-38ad-9d57-5616e6cc84a1 | -2.8688 | -44.9899 | 2024-10-27 00:35:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 254.5 |
| 42ac93ff-4ac4-3030-a578-44932992defd | -2.8939 | -47.8439 | 2024-10-27 00:35:22 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| fb46472e-f8e1-3486-9fdc-0484d3038fe7 | -2.916 | -51.7716 | 2024-10-27 00:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| daf89c69-1501-3656-b678-c3be2a9dbd13 | -2.9161 | -51.751 | 2024-10-27 00:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| d77a78ce-cfab-353a-bb91-2e0b4f671007 | -2.9214 | -50.295 | 2024-10-27 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 3bee66a1-29c5-3ddc-b075-fcb0c8a4fcce | -2.9215 | -50.274 | 2024-10-27 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 275e6052-0a83-304c-8ddf-bd38a13a61e3 | -2.9345 | -51.7711 | 2024-10-27 00:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 6d9a181b-fa04-3570-9ec2-efadf4263e39 | -2.9345 | -51.7505 | 2024-10-27 00:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c9bda966-6bcc-3f65-9a55-2c1794d55205 | -2.9399 | -50.2735 | 2024-10-27 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| edfa6d16-9a84-3624-bc74-b656cc2a6f1f | -2.9669 | -53.0389 | 2024-10-27 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6f9c4a40-a06e-3b7c-9c31-6ec666b3603b | -3.0703 | -45.6575 | 2024-10-27 00:35:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 91.0 |
| ec0aa813-bb62-388f-8881-3f41b4774348 | -3.0888 | -45.6568 | 2024-10-27 00:35:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 75d71869-0a25-3a60-b1e0-4c33ca658b47 | -3.1106 | -44.9809 | 2024-10-27 00:35:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 94.7 |
| c2345b63-41b0-3a41-a47c-07fc40984fd1 | -3.1057 | -50.3525 | 2024-10-27 00:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 0a17431b-d413-3405-bae3-21e391d03ed6 | -3.1292 | -44.9801 | 2024-10-27 00:35:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 93.8 |
| bbdb8248-1eba-3504-a6a0-b1a869624521 | -3.1242 | -50.3519 | 2024-10-27 00:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6b7af878-79f4-3a3d-b798-59680e81919c | -3.3256 | -50.7641 | 2024-10-27 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 92916022-675a-36d0-9d5d-98812301bf3f | -3.3256 | -50.7432 | 2024-10-27 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 4c7d9d53-189d-3d4f-8a13-8cd71ea7d1c2 | -3.344 | -50.7635 | 2024-10-27 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 156f06eb-d4f3-3bfb-9c3b-03b82b84a37d | -3.3441 | -50.7426 | 2024-10-27 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f8fa5a48-03b1-33f7-a166-97f7aba75b45 | -3.4392 | -50.0896 | 2024-10-27 00:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 404fe170-7a94-383a-b996-7db43b676a87 | -3.4762 | -54.5772 | 2024-10-27 00:35:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 1d52be16-52bc-380a-b132-82a701464af1 | -3.4763 | -54.5572 | 2024-10-27 00:35:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 00743fc0-1351-311f-afd5-0f3666967516 | -3.5202 | -52.7384 | 2024-10-27 00:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 19f634ae-2429-3e02-a930-81f9fbbba858 | -3.5442 | -51.4223 | 2024-10-27 00:35:25 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 34a24286-0045-3816-a1ab-eaf3c983b4bc | -3.5626 | -51.4217 | 2024-10-27 00:35:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 4796c4b2-1170-3d3f-9845-081c4a6cbc10 | -3.7748 | -49.4856 | 2024-10-27 00:35:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0575806b-0785-34dd-87fa-804d61d66519 | -3.7934 | -49.4849 | 2024-10-27 00:35:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f00e223a-b995-3d3c-87f5-6c30e9a4dbb2 | -3.8149 | -48.8874 | 2024-10-27 00:35:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 69fa480b-446a-3dc9-a0c5-fb8081c12df2 | -4.254 | -63.153 | 2024-10-27 00:35:30 | GOES-16 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4060cf2e-6a7e-31ac-98d3-92e2235290d6 | -4.3841 | -49.7571 | 2024-10-27 00:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| a0ae2067-4f26-37bd-8b6c-b5d125eb9c20 | -4.4696 | -50.9926 | 2024-10-27 00:35:31 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c768ec98-68cd-3085-9a11-7d57c53b1c29 | -5.2896 | -60.1632 | 2024-10-27 00:35:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 86f39d40-67ac-304d-8bdc-67be92fb8577 | -6.8534 | -45.8794 | 2024-10-27 00:35:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 394012df-31a7-3515-8a16-0e0fb246d314 | -6.8722 | -45.8779 | 2024-10-27 00:35:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 41fedf53-17a5-3561-a4de-7568b62effc1 | -7.2264 | -46.0498 | 2024-10-27 00:35:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ba45f987-cf82-3f37-83d4-50d99ead53f2 | -7.2267 | -46.0274 | 2024-10-27 00:35:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 11041cfd-d747-37d6-a6a5-ac36336ec462 | -7.245 | -46.0707 | 2024-10-27 00:35:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 080f87da-32f0-3b8b-81db-cfc41a9f7d52 | -7.2452 | -46.0482 | 2024-10-27 00:35:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 4514337a-0b64-35ec-9b84-5bfa5e207854 | -10.5424 | -45.1463 | 2024-10-27 00:36:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 7dbda491-d1bd-354c-aa70-360f75e7fd6b | -12.6646 | -44.2297 | 2024-10-27 00:36:16 | GOES-16 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6dd51a36-6117-39bc-82ab-8536cdc08893 | -13.0747 | -42.1261 | 2024-10-27 00:36:18 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 67.2 |
| f5a53ebc-7081-3d28-831b-f078aa1a4d94 | -13.3803 | -45.1149 | 2024-10-27 00:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 17e66a49-f7f2-372a-9195-2d541651d2cb | -17.6553 | -40.182 | 2024-10-27 00:36:42 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 89.1 |
| d25af0a8-f39c-379c-9a84-9df1cf9b277c | -17.6561 | -40.156 | 2024-10-27 00:36:42 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| f7322756-89dd-3da4-a928-8eb1efc497e7 | -17.6756 | -40.1765 | 2024-10-27 00:36:42 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 137.2 |
| 52852bea-e4b2-3ad8-8f57-69fc8b36f8a6 | -17.6763 | -40.1504 | 2024-10-27 00:36:42 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 153.0 |
| 34b493a0-7ee0-3d43-9d24-a6e7fb5aac3f | -0.9815 | -53.7192 | 2024-10-27 00:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 63cc77b6-a99e-3684-b48b-ee1a10d622e5 | -0.9815 | -53.699 | 2024-10-27 00:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 265.1 |
| 38b51fba-8bb6-3109-a4f4-285d29ab705c | -0.9815 | -53.6789 | 2024-10-27 00:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 211a8fee-a599-324f-b92a-10175ae2f7d3 | -0.9998 | -53.719 | 2024-10-27 00:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| db624a8c-d043-391a-bb20-299080c3d51a | -0.9998 | -53.6989 | 2024-10-27 00:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 301.1 |
| 00f9188d-362b-39be-9d5d-994ed7bf9004 | -0.9999 | -53.6788 | 2024-10-27 00:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 1a703f8d-d2a4-37e4-8262-d8bab8dde262 | -1.1831 | -53.8985 | 2024-10-27 00:45:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 2c7e2f59-1cf2-3e2c-97ba-e702f1df78f4 | -1.1831 | -53.8784 | 2024-10-27 00:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 4a338962-5860-3c65-955b-009b68d6b85f | -1.7874 | -46.4065 | 2024-10-27 00:45:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 89b685a7-c080-345a-8d08-f2965058217c | -1.7875 | -46.3844 | 2024-10-27 00:45:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 33a711d9-dccd-3ff5-875b-ab3fdea49463 | -1.906 | -59.9839 | 2024-10-27 00:45:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 86bf90eb-a245-30f1-bb8f-ab8fccc7b440 | -1.9243 | -59.9837 | 2024-10-27 00:45:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 106.7 |
| b0e2aacf-8d53-332f-8f9e-6a3d2f956fed | -2.3578 | -47.6641 | 2024-10-27 00:45:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b19bea55-eae1-36ee-ad84-c2a119d6cb8e | -2.4567 | -45.8567 | 2024-10-27 00:45:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 91b5f8c2-18f1-3b0b-ad4d-ebd54b770f67 | -2.4568 | -45.8344 | 2024-10-27 00:45:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 71213916-0759-35df-a176-5b2dd07edf81 | -2.4598 | -50.412 | 2024-10-27 00:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 93e1b651-809a-3ea6-8c1d-5792a0a8283a | -2.4753 | -45.8561 | 2024-10-27 00:45:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 117.9 |
| ec8e0d01-d09a-3c03-9783-3571f2e41e4f | -2.4753 | -45.8338 | 2024-10-27 00:45:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 144.1 |
| a20b6de3-4087-3704-a83d-119c5aa84f37 | -2.4786 | -50.2858 | 2024-10-27 00:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| db8f83bf-1b0b-3ce8-9ec2-497cd2111246 | -2.486 | -48.0507 | 2024-10-27 00:45:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9dbde628-caaa-3e75-a47f-5076b1bb0e34 | -2.6321 | -54.2975 | 2024-10-27 00:45:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| b32efb62-d2c5-3367-8c20-e33847dd7e27 | -2.6482 | -49.2465 | 2024-10-27 00:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 82042326-f6a0-3ccc-aa99-c18549e77dee | -2.6483 | -49.2253 | 2024-10-27 00:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 907f170d-4e9d-329b-9d28-dfa7cb96f6d3 | -2.7033 | -49.33 | 2024-10-27 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 7ea7af2a-4eb4-39bd-aff7-76f4216159d1 | -2.7034 | -49.3088 | 2024-10-27 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| f517f91e-30f3-3fd5-b274-43047d5b892f | -2.8145 | -49.2418 | 2024-10-27 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |


[Clique aqui para ver as próximas entradas](README14.md)
