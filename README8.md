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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fa71888-0a5e-32ce-a56a-10a63950880d | -1.04326 | -47.62809 | 2024-10-25 00:28:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 9d8ec85b-a3ec-3c38-9b50-3fc3371c4aa0 | -0.00043 | -51.22138 | 2024-10-25 00:30:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 5502a080-f242-3978-aa5c-77653defae5c | -1.1834 | -53.6771 | 2024-10-25 00:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 8c54c1e5-163f-3e9c-aef5-947e1439bcfb | -1.1834 | -53.6569 | 2024-10-25 00:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| d79c7dda-3d37-3e0c-a378-b7a26488bd80 | -2.6192 | -52.4564 | 2024-10-25 00:35:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| a48b50e6-e40e-311a-b236-5d0847b7d56b | -2.6193 | -52.4359 | 2024-10-25 00:35:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 1f6fdbad-115e-33bc-bad9-ced3189cf910 | -2.6297 | -49.247 | 2024-10-25 00:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| f44a4f5a-47e6-3237-abe4-ecf0f2798290 | -2.6482 | -49.2465 | 2024-10-25 00:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 75be0123-c1b1-325a-9bf2-c4eebc795892 | -2.796 | -49.2636 | 2024-10-25 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 9a673df9-763d-3724-b57a-7b24aab07248 | -2.796 | -49.2424 | 2024-10-25 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| de7e272c-643f-39a3-b3f9-c38040f53d08 | -2.8144 | -49.2631 | 2024-10-25 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 248.4 |
| 6faebf5c-b131-39e2-b9f0-0b620982708c | -2.8145 | -49.2418 | 2024-10-25 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 283.9 |
| 47b2a526-1853-35d4-b506-ff9fcb1e6860 | -2.9578 | -50.4198 | 2024-10-25 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 668a3920-48c0-3efc-964b-79def16f7c8d | -3.1071 | -45.7232 | 2024-10-25 00:35:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 87.6 |
| cc4cdbb4-bb47-3b1f-9dec-895b8e9ac383 | -3.1072 | -45.7009 | 2024-10-25 00:35:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 121.8 |
| b8bc1f3b-edd2-3fb1-9767-11d08ca4c9cf | -3.1258 | -45.7002 | 2024-10-25 00:35:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 40fc99bc-87bc-3bc2-b2f5-429b1b749749 | -3.2368 | -45.8077 | 2024-10-25 00:35:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 84f4d10e-9123-3ca9-9760-c8614891bcbc | -3.2552 | -45.8293 | 2024-10-25 00:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| ddd4e13e-f167-3bad-aaf9-f63eef850c28 | -3.2553 | -45.807 | 2024-10-25 00:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 203.5 |
| a13b926f-e737-3be3-a5d2-f43e3a061674 | -3.3124 | -49.5235 | 2024-10-25 00:35:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 05711d7b-dc16-3ff1-90a5-67de542aefc4 | -3.4047 | -49.5415 | 2024-10-25 00:35:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9bfaffb6-f44d-3d12-bf53-f632d7c3818c | -3.4048 | -49.5203 | 2024-10-25 00:35:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ef4ed644-4006-3b33-8ed8-c5c1ee408156 | -3.4605 | -45.6645 | 2024-10-25 00:35:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 79f237dc-7828-3bb0-8175-d655ca378622 | -3.4791 | -45.6637 | 2024-10-25 00:35:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ea39c8a5-9ac6-3cf6-bd91-18a37bc8da7b | -3.9394 | -46.445 | 2024-10-25 00:35:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| ff3a22b8-5c50-31ab-adf6-60ddd75c301a | -3.9396 | -46.4229 | 2024-10-25 00:35:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8cde2857-38d9-3115-ae44-5d14b842a29a | -3.958 | -46.4442 | 2024-10-25 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.0 |
| facc617a-9420-334a-8b7e-29161d7f79b6 | -3.9581 | -46.422 | 2024-10-25 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 9d54b3b8-2942-3d71-affe-16ec2816b6cd | -4.2427 | -48.5689 | 2024-10-25 00:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3294dece-7aad-3dfd-b09b-672fee4eb52f | -4.2429 | -48.5474 | 2024-10-25 00:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 73ffd2fd-742d-3a65-b927-1bb72a3b7c2d | -4.244 | -48.3535 | 2024-10-25 00:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| c8144583-d13c-3d04-b1ab-882e4bc1ac76 | -4.2441 | -48.332 | 2024-10-25 00:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| d7f85da2-f661-3f46-8253-c6483468b0f3 | -4.5231 | -48.2108 | 2024-10-25 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 9a9699d3-077a-3e87-8257-ea0cb2602aa6 | -4.58 | -48.0132 | 2024-10-25 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 397d8c9a-1a89-3abf-a891-672f706b86c1 | -4.5945 | -45.8108 | 2024-10-25 00:35:31 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ccd5cc03-f684-3e15-ac8b-34fdf45016c4 | -4.8423 | -45.0309 | 2024-10-25 00:35:32 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6d3b45d1-ad06-3821-ae17-16a03084d57a | -5.6291 | -46.9699 | 2024-10-25 00:35:37 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 6572d8ef-5625-3a5c-9cdf-04c446c7b77d | -6.5219 | -60.0457 | 2024-10-25 00:35:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 2597f00c-1cc3-382f-9f6c-394c0bdc408e | -6.522 | -60.0266 | 2024-10-25 00:35:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| b43f3d3b-928a-316d-88d1-29889906d168 | -6.6472 | -47.8642 | 2024-10-25 00:35:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e54b84a8-fa66-3e31-be96-ae08129dda1d | -8.9064 | -48.544 | 2024-10-25 00:35:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 80.8 |
| ae416610-4584-3803-8606-a2f84a2f3627 | -11.883 | -56.4152 | 2024-10-25 00:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 77fba3a8-44b9-3d15-8fc5-b08a71dc1dd9 | -11.8854 | -56.2138 | 2024-10-25 00:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9425c36a-4f3a-3173-abbb-e47a0e2910b5 | -11.902 | -56.4135 | 2024-10-25 00:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 632142b8-ecac-35d4-91e1-276bf0c44547 | -11.9022 | -56.3934 | 2024-10-25 00:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 81e14e39-424d-3056-933f-b9a7df192f92 | -12.3782 | -63.8821 | 2024-10-25 00:36:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| d81a66f2-974e-33b8-afef-5f9ba4df61f6 | -12.3783 | -63.863 | 2024-10-25 00:36:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| bf0a5620-4cc3-3ca1-9ac5-f1b70ed0e9fc | -12.3971 | -63.8811 | 2024-10-25 00:36:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c4be5ebd-b694-3823-a115-415cd8ce74e4 | -12.4589 | -63.1895 | 2024-10-25 00:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 6121eaa0-26e6-389d-b5f0-c097889ecfeb | -12.4591 | -63.1704 | 2024-10-25 00:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 8840f204-de97-31fe-84c2-f97609c85b2f | -12.478 | -63.1693 | 2024-10-25 00:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.1 |
| bb44044e-c956-3d71-a1ad-ccc55559df89 | -12.5356 | -63.051 | 2024-10-25 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 3e2e7afc-0d13-3d69-bffe-e7001f2b8dfc | -14.1339 | -44.3037 | 2024-10-25 00:36:24 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 3460e280-d8df-329e-99d4-6b06949d4cb9 | -15.6836 | -59.734 | 2024-10-25 00:36:34 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| be55a7e7-81ab-3603-bf64-07ac5c2f5df1 | -16.94 | -57.5268 | 2024-10-25 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 068f390d-c4d2-3893-bda7-7099cee250c8 | -16.9596 | -57.5245 | 2024-10-25 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.2 |
| a02dc955-9692-3033-9017-aeaacf3366ba | -16.9792 | -57.5223 | 2024-10-25 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.6 |
| 1d1e7da6-44f6-3262-aaa2-354ac1e84ff5 | -17.2186 | -57.2485 | 2024-10-25 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 195952a5-2ee3-31ff-9ab5-b7ae425ff21e | -17.2386 | -57.2256 | 2024-10-25 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| df527319-1eaa-3f25-b55b-87fa09c95b01 | -17.8032 | -57.5684 | 2024-10-25 00:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 1764c72d-a22d-3d8b-8a4e-38e4dab446f2 | -18.0056 | -57.2555 | 2024-10-25 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 7bb68e69-0972-3314-8beb-ed3a74c18988 | -18.0254 | -57.253 | 2024-10-25 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| bb0948cf-ec79-38ba-8a8c-a052804958e6 | -18.0441 | -57.3126 | 2024-10-25 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.3 |
| a06044a5-787f-31f1-a4ea-52af3b3bb011 | -18.0844 | -57.2663 | 2024-10-25 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.1 |
| 6229bf1f-4622-380e-ac69-83a9bcf20d7a | -18.3004 | -56.2222 | 2024-10-25 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| fd471923-8535-3a3b-a474-e9e96bc4674c | -18.3199 | -56.2404 | 2024-10-25 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 791ec55a-4c92-3350-9d7a-91a97ac12830 | -18.3203 | -56.2195 | 2024-10-25 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| 0ca1712f-00ec-30a5-abed-ce76bfa3e2c9 | -18.321 | -56.1777 | 2024-10-25 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 5bd6e281-a721-312d-a813-349ca80a7e63 | -19.6434 | -56.873 | 2024-10-25 00:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| dab26efa-73aa-307f-bf77-2aee934188a1 | -19.6438 | -56.8521 | 2024-10-25 00:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| b940dd12-6312-34e0-a58d-03f1606750cb | -1.0445 | -47.6237 | 2024-10-25 00:45:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ae2c0816-cdb2-361b-aecd-1df26098d699 | -1.1834 | -53.6771 | 2024-10-25 00:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6c534a6b-405f-3794-aa0b-ee094910627b | -1.1834 | -53.6569 | 2024-10-25 00:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 48e4de86-88dc-3abf-8f3d-c42981780bee | -2.6192 | -52.4564 | 2024-10-25 00:45:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 0299da44-2317-30ef-be40-b663b6dec733 | -2.6193 | -52.4359 | 2024-10-25 00:45:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| be447719-34a6-300b-a134-bf79d854883a | -2.6297 | -49.247 | 2024-10-25 00:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| e3fa8020-08d0-35e7-b266-ab9f96111fb7 | -2.6482 | -49.2465 | 2024-10-25 00:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 817b83cd-2d85-3d2d-b81b-28a4513fe007 | -2.796 | -49.2636 | 2024-10-25 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 3d3516f5-0d3d-333a-86cd-2225399855d8 | -2.796 | -49.2424 | 2024-10-25 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 6e9f9689-92b9-33b4-8b0b-cdfe466761ef | -2.8144 | -49.2631 | 2024-10-25 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 183.4 |
| 99cac987-73ee-3fa4-b90b-cc018d2ebcae | -2.8145 | -49.2418 | 2024-10-25 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 212.7 |
| 95071c18-cda2-3a56-b257-eda34d337b0b | -2.9578 | -50.4198 | 2024-10-25 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 31a98532-8203-36a3-981d-03ed852fd68d | -3.1071 | -45.7232 | 2024-10-25 00:45:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 090d2243-68c5-36f2-a464-9c62f53430e6 | -3.1072 | -45.7009 | 2024-10-25 00:45:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 024f6e7a-8d15-3b76-b833-c480f47ab217 | -3.2553 | -45.807 | 2024-10-25 00:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 676cb3b4-cada-3de9-be71-bb02dd5bbb25 | -3.3124 | -49.5235 | 2024-10-25 00:45:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| fabc2e22-aead-364a-b467-e58385ac721b | -3.4047 | -49.5415 | 2024-10-25 00:45:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e73da3ad-ecbb-3fc3-bdf1-e0c6502350e7 | -3.4048 | -49.5203 | 2024-10-25 00:45:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4080d195-9b0c-359d-a3f7-9db6e697107f | -3.4791 | -45.6637 | 2024-10-25 00:45:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0b065ff4-91da-3c8d-a0ce-3cbda40e08b2 | -3.9394 | -46.445 | 2024-10-25 00:45:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c08b0ff2-2407-3964-a2e0-23d27348ba23 | -3.9396 | -46.4229 | 2024-10-25 00:45:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| da2e48af-843d-37de-b8b3-629b67e3f41a | -3.958 | -46.4442 | 2024-10-25 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| fd2986e0-3c68-342e-825c-530142e47e50 | -3.9581 | -46.422 | 2024-10-25 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 76280edd-63e2-3836-955c-6e73180979dd | -4.2427 | -48.5689 | 2024-10-25 00:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 856fd742-d69b-3eee-865c-2a0b954d1265 | -4.2429 | -48.5474 | 2024-10-25 00:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 3534f3cd-8e11-397e-adde-b958e97eecb7 | -4.244 | -48.3535 | 2024-10-25 00:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| cdfe6c46-653e-3b8f-9972-6b5c2f946f09 | -4.2441 | -48.332 | 2024-10-25 00:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 183f8f23-42a6-3a50-a612-024ff4ac7406 | -4.5045 | -48.2117 | 2024-10-25 00:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 448a6571-6f34-376c-90f0-dc5083ebc5d4 | -4.58 | -48.0132 | 2024-10-25 00:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 768f450d-b738-3341-b7cf-e013d8050816 | -4.8421 | -45.0536 | 2024-10-25 00:45:32 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |


[Clique aqui para ver as próximas entradas](README9.md)
