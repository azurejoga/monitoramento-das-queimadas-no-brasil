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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f7ff198-d0ac-343b-bdda-7acd4a4cc60a | -12.6723 | -54.0395 | 2024-10-05 08:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 138b85b4-b44b-3554-870b-eefffb02bb33 | -12.6092 | -53.1129 | 2024-10-05 08:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| cf37a94e-d836-3a5b-b180-bb1746adef8e | -12.6089 | -53.1338 | 2024-10-05 08:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 7942361f-38f9-3a8e-8b0b-edb5657df0cc | -12.628 | -53.1317 | 2024-10-05 08:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8b3b9019-f9d8-3536-b0e9-cc741045a2d4 | -12.8202 | -50.5495 | 2024-10-05 08:26:19 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a1d0e62e-2d9b-32b9-9900-7543ec758fa7 | -16.554 | -57.2237 | 2024-10-05 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 9e90c581-cccd-3c7a-b9c5-a15943da6583 | -16.7647 | -57.4856 | 2024-10-05 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.4 |
| 8f562b1a-9cfc-3dc5-a410-0ab24f8af2e4 | -16.7843 | -57.4834 | 2024-10-05 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 92e972db-0ca7-3ce4-8885-786985505592 | -17.1178 | -57.4244 | 2024-10-05 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.9 |
| e6d0e4ca-e315-32ed-8319-cef9bda913a7 | -17.1182 | -57.4039 | 2024-10-05 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.6 |
| 9e700e89-5b6c-3be4-9234-2be9365dd9ba | -17.1375 | -57.4221 | 2024-10-05 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |
| f63a6696-c807-35f5-a496-e3fc53f980cb | -17.1378 | -57.4016 | 2024-10-05 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 5ad449fc-7346-3055-aa55-c0b81402a168 | -18.4853 | -52.8659 | 2024-10-05 08:26:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 230.3 |
| 5de28571-6c97-3c88-8367-f23299d072f3 | -18.4849 | -52.8876 | 2024-10-05 08:26:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 289a12c2-11c5-3a49-b584-0e992fb42cb2 | -18.5058 | -52.841 | 2024-10-05 08:26:50 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| cf50082f-2358-3826-ac9d-3ab5c6c76d15 | -18.5048 | -52.8843 | 2024-10-05 08:26:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 618177b6-d837-3db9-ab8a-334736fc7586 | -18.5053 | -52.8626 | 2024-10-05 08:26:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 346.0 |
| 327220ff-14e2-3b91-b885-d10e7399b59d | -18.6586 | -57.2759 | 2024-10-05 08:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.0 |
| 6a6ddb4e-a1e3-3479-940f-822ccdf5b3fa | -18.6582 | -57.2967 | 2024-10-05 08:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| c3020bbf-0c6c-3f77-ba29-a0efed4f5563 | -18.6785 | -57.2734 | 2024-10-05 08:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.5 |
| c825dca6-ff52-3b1f-8030-de0da4460db8 | -16.5345 | -57.2259 | 2024-10-05 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 26b233bc-1212-3d8e-ae75-85cc4be2fb90 | -16.554 | -57.2237 | 2024-10-05 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 7ac671f8-70e8-3259-9eac-8c416f87d58d | -16.7843 | -57.4834 | 2024-10-05 08:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| c83f611f-5283-35f1-92bc-708d419f314a | -16.7647 | -57.4856 | 2024-10-05 08:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 5db55858-e99b-38bc-b1d7-040b49a595f9 | -17.0316 | -56.6956 | 2024-10-05 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 65ec6c48-31cf-37b4-a946-c64cedf749b6 | -17.0303 | -56.7781 | 2024-10-05 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| e60ab4da-8d62-3cba-805f-b3e4cf68291f | -17.0299 | -56.7987 | 2024-10-05 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| ea819ee1-ea53-390e-89e4-08078c71d00c | -17.012 | -56.698 | 2024-10-05 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| e4d479eb-0bd2-32f0-85ce-76f7ffd60bfd | -17.0106 | -56.7804 | 2024-10-05 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.3 |
| dd10d91b-28df-3430-a2cc-e4cc3848351c | -16.9907 | -56.8034 | 2024-10-05 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 78f23f31-3f46-3815-a3ad-602e8dde79c4 | -16.991 | -56.7828 | 2024-10-05 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.4 |
| 03ae5aba-9ecd-3c31-876e-dd644cdc3560 | -17.0103 | -56.8011 | 2024-10-05 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 166.4 |
| ee4216cc-096f-3547-9f23-8276b37447ce | -17.0319 | -56.6749 | 2024-10-05 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 32aea522-0bd3-39f4-8805-a53663fb251e | -17.1378 | -57.4016 | 2024-10-05 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 17b6d440-401d-3fd4-9485-f0c47d26e809 | -17.1182 | -57.4039 | 2024-10-05 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.9 |
| a93e95f1-e7a6-3bc1-95f9-97b6f76a4897 | -17.1375 | -57.4221 | 2024-10-05 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 0349e404-a7d9-39ab-8f02-f4c52c8999a9 | -17.1178 | -57.4244 | 2024-10-05 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.4 |
| 4538dd0e-14b8-332b-b94a-0f2c01877667 | -18.6586 | -57.2759 | 2024-10-05 08:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.2 |
| c85c5a43-bd39-362a-8d53-a3b0716a53cc | -18.6785 | -57.2734 | 2024-10-05 08:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| b8d46c6b-45d4-307b-bf23-286818c90dea | -16.7843 | -57.4834 | 2024-10-05 08:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 08b7e5c7-9f82-3165-97b7-4618e157d76e | -16.7647 | -57.4856 | 2024-10-05 08:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.3 |
| 1f93ba2f-a1f5-3e5d-85fa-dd44dac1d8ae | -17.1378 | -57.4016 | 2024-10-05 08:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| a8fa91a6-9061-31b3-b683-299869ef7ccb | -17.1375 | -57.4221 | 2024-10-05 08:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |
| c4a1fc21-a187-3444-9c31-a38da112a174 | -17.1182 | -57.4039 | 2024-10-05 08:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.1 |
| 3fa1aaab-98ed-3002-a1d8-55c93aeb0ac5 | -17.1178 | -57.4244 | 2024-10-05 08:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.2 |
| 2513e68d-3c2d-3f4f-ad70-52baea62951c | -18.49 | -52.91 | 2024-10-05 09:03:38 | MSG-03 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a00ff1e5-4f7f-3364-bb46-23b40c7f65fa | -18.4844 | -52.9092 | 2024-10-05 09:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 235.7 |
| 40e25390-b35a-3872-bedf-40a30e765080 | -18.4849 | -52.8876 | 2024-10-05 09:26:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 435.3 |
| 7ff0afaa-bbee-37f8-a8de-041e489e8392 | -18.5044 | -52.906 | 2024-10-05 09:26:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 97c79170-02d4-3a14-b5e6-2943ee8a446a | -18.5048 | -52.8843 | 2024-10-05 09:26:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 309.1 |
| 78290eda-9a64-3b2e-a72e-9c4e8e8b0320 | -18.4844 | -52.9092 | 2024-10-05 09:36:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 255.1 |
| 224de9ed-b7f2-3241-bb7d-af39f9f57f12 | -18.4849 | -52.8876 | 2024-10-05 09:36:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 346.1 |
| a9bfb51a-6384-3777-848f-5c857b1dc256 | -18.5048 | -52.8843 | 2024-10-05 09:36:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 49e23bab-25a1-323a-8e86-f0278c60d573 | -18.5044 | -52.906 | 2024-10-05 09:36:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 129.1 |
| bb5fc66e-ff34-31eb-b28e-98171079a25b | -18.6785 | -57.2734 | 2024-10-05 09:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.7 |
| b86e1aaa-6335-3c10-8e6a-1179f4663d3f | -18.6586 | -57.2759 | 2024-10-05 09:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.4 |
| a96036ca-5b16-3d70-8959-fc43d4bee6f1 | -11.2232 | -46.6248 | 2024-10-05 09:46:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 221.2 |
| f89a1943-f0d3-39aa-ada9-6475a3fe4d4d | -11.2423 | -46.6222 | 2024-10-05 09:46:09 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 6f5244e9-5427-347c-bde2-2749efd0f045 | -17.0103 | -56.8011 | 2024-10-05 09:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| 4393f584-603b-30e3-85fc-f027ee8c2e4d | -17.1182 | -57.4039 | 2024-10-05 09:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 1849efc1-01f6-31d8-b664-51bf8eec8e9d | -18.4849 | -52.8876 | 2024-10-05 09:46:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 313.6 |
| d711a1da-4bd3-3dc0-affb-35445291b41e | -18.4844 | -52.9092 | 2024-10-05 09:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 325.0 |
| 855e6475-b1ca-388e-a658-70412a7b1c8f | -18.5048 | -52.8843 | 2024-10-05 09:46:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 149ddc2e-7df8-3cdc-9629-94258044838d | -18.6785 | -57.2734 | 2024-10-05 09:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 78f1c10e-3270-338a-9956-1e89d14754d4 | -11.1487 | -46.5219 | 2024-10-05 09:56:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 3e8a2055-9950-3fe5-a499-a6673c6c92ef | -13.3976 | -61.957 | 2024-10-05 09:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 127.4 |
| bc69c517-fb55-36fb-8b4d-5a8af8e5834e | -13.3978 | -61.9376 | 2024-10-05 09:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 109.6 |
| ff3fa81f-1aba-377e-bd93-f65cae74261c | -16.554 | -57.2237 | 2024-10-05 09:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.2 |
| 01ef0da9-1b02-328d-9903-93754d692674 | -18.4849 | -52.8876 | 2024-10-05 09:56:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 9c5a5565-9ea4-3409-a7f8-e0bd3068c546 | -18.4844 | -52.9092 | 2024-10-05 09:56:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 186.4 |
| e05314cd-d287-3406-bf3f-c1c0329a45a1 | -18.5048 | -52.8843 | 2024-10-05 09:56:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 07561a24-bfd9-3f00-88f0-3331cb5b3b4f | -18.6785 | -57.2734 | 2024-10-05 09:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.9 |
| ad518e7f-a236-3130-8541-7b7ee79b4c64 | -11.23 | -46.64 | 2024-10-05 10:04:20 | MSG-03 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a45bc63c-bdde-3853-9f82-fbe8d00f37cc | -11.2232 | -46.6248 | 2024-10-05 10:06:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| dabed2c1-6090-32e4-b09a-a4f34c3f93db | -11.2423 | -46.6222 | 2024-10-05 10:06:09 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 240.9 |
| 32cbda05-8628-3157-9ff2-2aa25d3dc987 | -13.3976 | -61.957 | 2024-10-05 10:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 97.5 |
| c0c88e30-b295-391e-8416-ac87a277b0ca | -16.554 | -57.2237 | 2024-10-05 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.5 |
| 51e072ec-4903-3a7d-a0bb-4efce9ed9fbc | -18.4844 | -52.9092 | 2024-10-05 10:06:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 153.8 |
| ee82ce11-7077-3df2-9b15-9936165f8036 | -18.5048 | -52.8843 | 2024-10-05 10:06:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 644a2e4f-961b-3bb8-8e14-218950845fab | -18.6785 | -57.2734 | 2024-10-05 10:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.0 |
| b6488c3e-aeb4-3a41-80f8-b940f7414e1c | -11.2423 | -46.6222 | 2024-10-05 10:16:09 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| cbf9a753-ce83-35b5-a55d-a456d4d60e09 | -18.4844 | -52.9092 | 2024-10-05 10:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 7130787c-121b-3b06-9d2f-04b55d46b4c3 | -18.4849 | -52.8876 | 2024-10-05 10:16:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 7f6b30b5-5120-3306-9293-0e85be4ec5ee | -18.5044 | -52.906 | 2024-10-05 10:16:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 9f5edc72-a648-3d9c-aa02-f17c0428cc37 | -18.6785 | -57.2734 | 2024-10-05 10:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.7 |
| ea4e837f-7200-3cf8-8143-c25098d43575 | -11.2423 | -46.6222 | 2024-10-05 10:26:09 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| b94c6af5-f687-3106-81bb-7988374b46a5 | -17.1178 | -57.4244 | 2024-10-05 10:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.3 |
| d5aaefd6-1a81-32cb-bb1b-c837cce70a4d | -17.1378 | -57.4016 | 2024-10-05 10:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 4cf50679-5c41-3ef4-b109-0cfa0ab45bf4 | -17.1182 | -57.4039 | 2024-10-05 10:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.6 |
| 6c0cebc5-d7df-3422-8b86-3ffbaea79bfd | -18.484 | -52.9309 | 2024-10-05 10:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 115.8 |
| c0319520-3c7c-3f90-8dbf-b2d902091204 | -18.4844 | -52.9092 | 2024-10-05 10:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 398.2 |
| 30f3fcaa-5534-3077-8713-aff5d12c4139 | -18.4849 | -52.8876 | 2024-10-05 10:26:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 149.9 |
| c639b435-6fbe-364a-b139-05a271f46930 | -18.5048 | -52.8843 | 2024-10-05 10:26:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 40910576-973e-3f53-b935-7257335becb2 | -18.5044 | -52.906 | 2024-10-05 10:26:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 98082ac5-bf89-32c5-80a2-519d1f139ef6 | -18.6785 | -57.2734 | 2024-10-05 10:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 18293aa0-8226-354e-a106-c8fbeb1f4956 | -18.6586 | -57.2759 | 2024-10-05 10:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.8 |
| 72bd17bb-0079-3f3b-9e6c-37b39e4fbfef | -11.1487 | -46.5219 | 2024-10-05 10:36:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 69c9c7a7-cb24-3b3c-9fd3-2d41643e375d | -17.1182 | -57.4039 | 2024-10-05 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| bf50d56e-86e2-34bc-bd73-d69c2272e761 | -17.1378 | -57.4016 | 2024-10-05 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| d3660590-f222-3dc2-bbf9-cdb6dd6645dd | -17.1375 | -57.4221 | 2024-10-05 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |


[Clique aqui para ver as próximas entradas](README156.md)
