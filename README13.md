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
| 5d2c1a52-92f3-3132-86ac-de6911a3f9bd | -3.1453 | -54.078098 | 2026-10-01 01:11:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bf695a3-4eea-3ea2-aece-8468fad277e6 | -10.529 | -57.766499 | 2026-10-01 01:11:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a52cb0f-da5e-3cec-a722-fb600a38d0ef | -9.1411 | -64.399597 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 175b74f0-2359-385e-842e-e4eae576143b | -6.6651 | -58.876701 | 2026-10-01 01:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e68be58-cb82-3911-82db-209aadd8aa7c | -8.5792 | -67.012497 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16636e2a-f594-388d-9561-9e0e07cdf6c8 | -3.1703 | -54.1394 | 2026-10-01 01:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fadfc2f-80d1-325c-9664-2c97a78cc350 | -8.9872 | -65.691299 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dbbb7c88-c706-353c-98cd-588e9e57f87f | -9.1281 | -64.388 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f278000f-3222-3089-8271-dde64fe0330a | -9.0131 | -65.714897 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04f8088e-086b-37c0-9697-a5502eabe493 | -18.051201 | -51.1698 | 2026-10-01 01:11:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cb03dad3-6423-3edd-94f7-8b3b7827375f | -8.5547 | -66.994301 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e82b6eb8-4c88-33df-8b86-228afa3d3927 | -8.5645 | -66.992104 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83da06f1-a746-3dfa-8c9f-4a2a89e90b9e | -13.6535 | -53.961498 | 2026-10-01 01:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e667fe5-405d-31c5-b893-92c77e3d220f | -12.902 | -61.714199 | 2026-10-01 01:11:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ffee1e17-6f70-3786-a0b3-e5b8bce39119 | -8.997 | -65.689102 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 646b16e0-d34d-39c4-ba50-696db46eb130 | -10.5518 | -57.775101 | 2026-10-01 01:11:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6b65b1e-cf82-3263-8277-32042727e727 | -8.5465 | -67.003998 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a3fbed3-846e-3407-868b-0d962d979f88 | -8.6515 | -62.661701 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 02a428ec-81d0-3b2f-9964-8a4edf7abe14 | -14.4411 | -51.294102 | 2026-10-01 01:11:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 247e1844-22bb-3397-aede-8f4d006fde00 | -2.9037 | -54.170502 | 2026-10-01 01:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54a09d2d-e786-3252-9c41-6f93e82f6657 | -3.1799 | -54.1371 | 2026-10-01 01:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9daa9f4-13b4-3045-b388-45708664e13a | -5.8532 | -57.7715 | 2026-10-01 01:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d6105ac-4884-3d47-a06d-b1081384bfd6 | -5.1182 | -56.016499 | 2026-10-01 01:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a9f951c-5ad1-3792-8de7-ee1567e13076 | -6.678 | -58.887501 | 2026-10-01 01:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8cec99b-50db-3c76-b6da-5136d27a0c0c | -9.1395 | -64.3927 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bcb2aeb9-8fe1-3226-8672-fd0b8cc26cb8 | -3.2862 | -53.9067 | 2026-10-01 01:11:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acb8252e-46db-3ff8-a1d2-d3f6b952c694 | -5.1139 | -56.040699 | 2026-10-01 01:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81681697-d501-36ee-9c96-ca8e02175742 | -14.4227 | -51.2654 | 2026-10-01 01:11:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5653c631-d9dd-37ed-8199-bf3dac4c2f71 | -8.5628 | -66.984703 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a837fab7-e287-3b48-879f-408b1025c286 | -3.2958 | -53.9044 | 2026-10-01 01:11:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42594e8a-e837-3c30-814e-9235bf3f0d25 | -3.153 | -54.110001 | 2026-10-01 01:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7972e99c-6857-3061-b299-e4d9541f841e | -9.0001 | -65.703102 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93b16b8f-2147-3b95-909d-d8469c6984e2 | -9.0017 | -65.710098 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28a0f6c4-65b9-3161-be42-95b5d36e4ae2 | -5.8629 | -57.769199 | 2026-10-01 01:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84322903-2335-3378-8fff-3e0055d42b89 | -9.05 | -66.1138 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9278b0a-827d-3a80-80bc-e83e224dbf00 | -3.1548 | -54.075802 | 2026-10-01 01:11:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a7e70de-b252-36ef-a770-220abd01a8d2 | -7.4827 | -55.0172 | 2026-10-01 01:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 317832b6-16ca-3a66-a528-c39ce871ff8a | -13.6477 | -53.9398 | 2026-10-01 01:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3f79d1a1-f201-3d9c-8360-8773535f3ec9 | -14.4126 | -51.302799 | 2026-10-01 01:11:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08c0c2bb-7f6f-3c76-8cb6-f197ca4a7947 | -10.0704 | -63.088699 | 2026-10-01 01:11:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d35cff61-c94d-3ed0-b69d-e61d2a083178 | -8.5449 | -66.996498 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0009215b-566f-3292-a49f-fe95559b3981 | -9.0048 | -65.723999 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6513161-7c3a-34e5-affb-b95cccf73c5e | -12.9002 | -61.706501 | 2026-10-01 01:11:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01570763-a4e3-3183-a77e-832ff766d9cd | -10.5324 | -57.779999 | 2026-10-01 01:11:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd87f1af-4f9f-379c-9ad5-4a84311f42fb | -3.1722 | -54.1054 | 2026-10-01 01:11:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55b70bcf-7139-30cb-810e-0be35b6bb416 | -9.1328 | -64.408798 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 383544c4-92ba-373d-8bc0-e9692659bc70 | -13.6439 | -53.964199 | 2026-10-01 01:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd74d9d2-1ba4-31c8-9bf2-9155e709dbde | -13.6631 | -53.958801 | 2026-10-01 01:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a5f72e4-a739-38f2-96f9-1d1f0a00da6c | -8.5759 | -66.997498 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e4d537d-40fe-3feb-b943-113925a1ed78 | -10.5615 | -57.772598 | 2026-10-01 01:11:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2291b66a-e9c7-39e6-a1ec-6bfea0dd9dfe | -2.894 | -54.172901 | 2026-10-01 01:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25c09b8d-ddc4-3a6c-9fc2-0eafca0efa02 | -8.5776 | -67.004997 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5ea773e-ae78-3d12-84a9-03497518e735 | -11.41 | -43.39 | 2026-10-01 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71eb9f7a-1a3e-30c8-bb9a-4da5a85aa407 | -4.26 | -50.81 | 2026-10-01 01:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06a118c6-2ab9-3c9d-965a-ef3585f1c8a6 | -11.44 | -43.4 | 2026-10-01 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6247e513-7657-38ab-86c4-d0e7c55f3c28 | -4.26 | -50.75 | 2026-10-01 01:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 448a5d69-1f44-3a6c-afc3-570a776a6ba9 | -11.45 | -43.44 | 2026-10-01 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5fd46170-254c-3cb3-94f6-2f0b8dbb1b20 | -4.26 | -50.7 | 2026-10-01 01:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae82a409-99eb-31f3-9efa-d423d1e939b8 | -4.29 | -50.76 | 2026-10-01 01:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b00b5caf-6f6c-3e46-a1c7-f4a855d3d2bb | -4.29 | -50.81 | 2026-10-01 01:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f095738c-d973-37a4-8d0b-b4384880f50f | -10.47 | -46.79 | 2026-10-01 01:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c2715bd-efd0-3de7-b137-5dd910ba1bc9 | -11.42 | -43.43 | 2026-10-01 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f2aec05-907d-3a6f-8e18-4ef437762515 | -13.07 | -51.24 | 2026-10-01 01:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d689588e-76ce-34b1-ae03-39183ee6a88f | -3.17 | -54.06 | 2026-10-01 01:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbff5a80-f362-3763-81b7-866da43cafe1 | -4.23 | -50.75 | 2026-10-01 01:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8fa0558-1875-3c5a-a0f2-851f3dcc0450 | -3.17 | -54.12 | 2026-10-01 01:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c02b1b06-e928-383f-bad5-dff93c6aa017 | -11.2087 | -45.1939 | 2026-10-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 5fc01acc-dd31-3e5f-85d9-e273c8634c41 | 3.2924 | -60.6101 | 2026-10-01 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| afc06112-73da-3060-ab0c-08189bd7fa40 | -14.4225 | -51.2624 | 2026-10-01 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| cdda63e9-8deb-37be-828e-d3ae375387cd | 3.2741 | -60.6294 | 2026-10-01 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 262cfb7a-5aa5-36bf-acb5-87121ac25cca | -3.5623 | -51.4838 | 2026-10-01 01:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 257663b8-b700-3617-af68-8d87806a5a39 | -13.6479 | -53.9336 | 2026-10-01 01:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 32595816-b5da-3df7-9035-922092b06649 | -11.81 | -50.4999 | 2026-10-01 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 739d6b79-adef-399f-ab6d-a3394886c3d9 | -3.1245 | -50.289 | 2026-10-01 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 53be2d60-6050-368d-9cc5-9716bd2e0b59 | -10.4791 | -46.7862 | 2026-10-01 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8e638b40-5367-3709-a786-9450698e634c | -5.7561 | -45.1747 | 2026-10-01 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| d1d76d63-adb8-338b-b987-0e2e23549df6 | -3.1061 | -50.2686 | 2026-10-01 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 1c06f70e-3704-3e01-bde7-78354c8e026e | -14.4418 | -51.2597 | 2026-10-01 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5d700775-d408-380f-bb32-99f682f35444 | -5.7355 | -43.2916 | 2026-10-01 01:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 4cc01f70-5a1f-3433-8948-5983c2d8d445 | -11.19 | -45.1736 | 2026-10-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 76e2fa28-5623-385b-92e1-f5a34a30bfed | -6.0179 | -49.5648 | 2026-10-01 01:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| fdc3c380-5b76-39a2-b885-342324e5e440 | -16.1671 | -42.8587 | 2026-10-01 01:20:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c29965b3-417a-3a6f-a87e-a50d6020e661 | -5.7563 | -45.152 | 2026-10-01 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c62b6e71-5c25-3a5c-8128-91fff7af49ee | -10.565 | -50.0382 | 2026-10-01 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 5e827290-71d7-3630-975e-f4a82d5a2e18 | -11.1896 | -45.1966 | 2026-10-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 80c672a5-4fbe-3609-9098-cbcfa5931806 | -3.295 | -53.8597 | 2026-10-01 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 291bf446-e942-3b1c-ad30-1abbf991e0ff | -9.1221 | -64.4031 | 2026-10-01 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| b3cbce15-62a5-391b-b563-b69c969d4d74 | -2.908 | -54.151 | 2026-10-01 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 46fdcbf2-2071-3268-ad69-5084ae66cd97 | -18.0658 | -51.1301 | 2026-10-01 01:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 9e1284ad-4e3c-3a0c-8ee4-40d65a192925 | -3.106 | -50.2896 | 2026-10-01 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| e5f67597-db06-3cfb-8ffb-b577699ab2b2 | -18.0458 | -51.1336 | 2026-10-01 01:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 10fa7f3a-ec60-3ef6-8ebe-385879dac510 | -13.6671 | -53.9314 | 2026-10-01 01:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 06ce4413-834b-3fa3-b667-81fd22304b96 | -5.7542 | -43.2901 | 2026-10-01 01:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| ee1198d4-e9d7-364b-8ee4-2d8867c129e6 | -3.5808 | -51.4832 | 2026-10-01 01:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 4b6d09e8-f9e2-342a-ac96-29c4cc9b7dd4 | -5.7544 | -43.2668 | 2026-10-01 01:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 4c11cfe6-54f2-33f9-8a5e-87d125e30136 | -3.1245 | -50.268 | 2026-10-01 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 21cccae5-aa73-30a3-af7f-af62af12b6f3 | -9.6637 | -40.5819 | 2026-10-01 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.3 |
| a036f32a-a9ab-366b-9dee-a9a4a8b4865e | -9.1222 | -64.3843 | 2026-10-01 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 108e869d-1961-39f0-b33b-44fa72e142cc | -5.7357 | -43.2682 | 2026-10-01 01:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 47e0292a-57cb-3fa7-a1c4-b6167e62bdf6 | -9.1408 | -64.3836 | 2026-10-01 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |


[Clique aqui para ver as próximas entradas](README14.md)
