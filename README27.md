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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa05b7cd-d062-3954-9371-d2dcbd8dd460 | -6.00456 | -45.94739 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70d5d212-149a-3db7-a0dc-adac16b8970d | -6.00327 | -45.95543 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 77c649b0-8f9b-35ce-ac81-43bd3d99ec5a | -6.00239 | -45.95503 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ba3452e-fb36-30a0-a2f1-8cfbd1052175 | -6.00172 | -45.95909 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 893a50a2-bcd2-3df6-a49c-6ee75fc8c438 | -5.99906 | -45.9589 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e632f355-b784-3484-bf17-5b69716c8421 | -5.99816 | -45.9585 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 778dd8f3-758d-35b8-80c9-225ceb9d3628 | -5.84414 | -46.38852 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f2c7b4fe-1f5d-37c2-9432-374bf1698e56 | -5.84327 | -46.23587 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec2bf87c-35e7-36b7-8989-b29231d5323c | -5.84257 | -46.24006 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ecabcab7-e155-3953-be54-246e9c27a4fb | -5.842 | -46.23695 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 40f1a9a1-c2af-3569-bef7-1e9c7b7c9b21 | -5.66642 | -46.35017 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff5c41b9-324d-351a-a8c0-e60064a79368 | -5.64633 | -46.40419 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0180998c-554f-31db-8368-a82c4819e8e5 | -5.463 | -46.35474 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51af4443-155e-385a-9045-bf10d1f2b99f | -5.45933 | -46.35416 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3db2ba2f-9a20-31bf-9e75-a969ece119a2 | -5.43989 | -46.28916 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b920b0c-4ef8-31a9-86b8-b94c42254fc7 | -5.20722 | -46.31128 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c72ff2d5-0f55-3d5f-85bf-dc061c6c4d18 | -5.17024 | -46.12255 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da965132-20eb-38f4-87f3-c1dac8a0cc79 | -5.10171 | -46.10437 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01aac948-dad8-31e0-abe2-2db7d137d45e | -5.09807 | -46.10386 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3d30592-097f-3e6d-80a9-e8813f7e0896 | -6.26285 | -45.82928 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9330b1b1-4f26-340e-b961-14ca29c1d623 | -2.81078 | -49.25801 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e544b576-e05d-3dad-a188-77c6bfeadb8a | -6.24943 | -45.44162 | 2024-10-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f815acc-37e3-3862-98e8-59d42326fa32 | -5.98427 | -45.36876 | 2024-10-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85fb9a99-cd88-3144-9a99-2f0874070bf8 | -5.9814 | -45.36436 | 2024-10-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 7114d889-5712-3195-b0d5-8d226d40fbab | -5.98079 | -45.36821 | 2024-10-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 44eaac48-9587-321a-bc21-3245f7400642 | -5.98018 | -45.37206 | 2024-10-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| b7541bc9-8630-30bd-a79f-bf3347fb2dce | -5.97731 | -45.36767 | 2024-10-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 3be05dfb-f36d-3530-9679-82591d1ac3ba | -5.9767 | -45.37152 | 2024-10-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| a22a03bc-c1aa-3f55-877d-8eb9b9ecd6bf | -5.70828 | -45.00644 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 363dae0c-c9a9-3e3d-a411-1a0e050542d3 | -5.70768 | -45.01017 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| fe2bd892-71b6-3d2b-811d-cfe1c0b7ba44 | -5.70632 | -45.16835 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc5924ba-87f1-323e-962a-1b7f07eaca73 | -5.70484 | -45.00588 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf494613-33a9-3d63-bfb7-f34f578b9d8b | -5.70425 | -45.00961 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9e4b79f1-ccda-38af-9a6e-aa492d82c219 | -5.34267 | -45.63889 | 2024-10-25 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 281e0365-1450-3e14-a51a-00840ff9a0b7 | -5.33151 | -45.5514 | 2024-10-25 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f18e43f8-3273-3284-a6b7-27affcefa71b | -5.28592 | -45.74145 | 2024-10-25 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f685fe0c-d5d7-36f8-af30-ece689f58efd | -5.27543 | -45.51493 | 2024-10-25 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d48c6030-d9e2-3758-a087-a0187c8ee5f5 | -5.09405 | -45.82986 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 574012b6-a692-34d1-b4dd-ef71bb9cdacb | -5.06537 | -45.8254 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddc32188-ad51-38f9-aac9-0f268842f3a0 | -5.05509 | -45.86579 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1696df53-2791-308d-89d7-35d25613eeab | -5.70651 | -45.25461 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9754266-0827-36d8-a639-58cbe1ef1545 | -5.4623 | -46.35906 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 618ae53f-7247-3ecb-8888-be2d96e9ef80 | -5.38626 | -46.1558 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf0b2431-8272-3d42-8c45-6e5c56a04f8c | -5.34595 | -45.44054 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a27c7d37-7c7f-31ea-8d1e-a34bde29f8ab | -5.3453 | -45.4445 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06bafac4-e249-3299-9450-59cdc3616129 | -5.33913 | -45.63832 | 2024-10-25 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfece43f-df39-3c22-9f11-4504c4717721 | -5.33086 | -45.55536 | 2024-10-25 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4cc701da-2850-3b53-b684-9ceda715f57a | -5.25134 | -45.77873 | 2024-10-25 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47e9cbb3-40d3-3946-a5ed-ca11ba24eaea | -5.17381 | -46.193 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93f3600a-4549-3472-9219-f8a872b29113 | -5.0947 | -45.8258 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86ac55a4-a2a4-31ae-9f01-2110e8ac4ebb | -5.07217 | -46.05654 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 289c85c6-d3be-322d-a932-bd82887d2852 | -6.94045 | -45.23069 | 2024-10-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fad8100d-c703-3313-b094-136a3bf4849b | -7.88139 | -45.43088 | 2024-10-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af5045cc-fcd9-3aa9-bd6c-cfd2c2a71995 | -7.83164 | -45.43423 | 2024-10-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47d0a615-0152-3e7c-9fbc-a3218207d5d5 | -7.94028 | -45.69584 | 2024-10-25 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d114c5d3-7563-37b4-9325-204c4ae86b49 | -7.93967 | -45.69963 | 2024-10-25 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97f24ec7-8f33-3703-82c5-f61fd5d3b64f | -7.93681 | -45.69535 | 2024-10-25 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be96169c-9cfa-3dc6-aca9-7707e3380e02 | -7.91771 | -46.43074 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95ff3b12-5422-33db-92ba-58a103e98e3f | -7.88427 | -45.60944 | 2024-10-25 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 676b580f-a074-3491-8705-4b1c55bad66d | -7.81679 | -46.51642 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25d27846-88a6-390b-9b28-b3be3ee6f22d | -7.81439 | -45.58244 | 2024-10-25 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 752d04fe-04da-3151-9a15-dcf8cd3eaffc | -7.81096 | -45.58181 | 2024-10-25 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0fbaeb0-0056-3c5b-ac84-4b64bd17444c | -6.57288 | -46.56853 | 2024-10-25 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2720ac8-742e-381f-8d1e-3ed535824303 | -6.49967 | -46.16146 | 2024-10-25 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1f40471-0ab6-3cd0-b9f7-075bc441cec3 | -7.70549 | -46.59825 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c50ae10d-f47c-3a64-9bc0-189ff6bd53c0 | -7.67521 | -45.94074 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee03cd60-ea51-3d84-b1fa-c5f9fbc99e38 | -7.63338 | -46.60791 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 151d66b0-40c5-3eed-a186-786c1b832e8c | -7.56438 | -46.79479 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9af3c27-6aa4-3fc2-ae85-82e4fc820508 | -7.56073 | -46.79417 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 087ff018-29b8-3ff8-8653-64009056eff6 | -7.5407 | -45.84741 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d35b4a61-5a40-323d-b77a-a199f1c8203b | -7.54014 | -46.75987 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daa2d94d-b4a1-3cba-8b3a-8309a9ff405c | -7.54008 | -45.85131 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88b0cd5e-7711-3ca3-829e-1e3b50711c00 | -7.53945 | -45.85521 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b66e122b-05e4-3ecf-83ef-1144503d09f7 | -7.53721 | -45.84683 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6370d92-a27e-3135-8675-f500293bfed0 | -7.53691 | -46.87017 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dbb0cc23-35d6-3d22-873e-63ab6bd19fa4 | -7.53659 | -45.85073 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f312724e-d5ab-3fff-aa7e-21e84dd23a54 | -7.53596 | -45.85464 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83ccf2c8-8f57-33d2-956b-54364f0dc77f | -7.53498 | -45.83847 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 97afc3fe-e9d4-3828-bada-fcc38c1e8302 | -7.52934 | -45.41296 | 2024-10-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b0fb09f-0f1f-30f0-969b-f4450b16220a | -7.5285 | -46.10432 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad05dda5-c810-392e-989c-95501719e234 | -7.51967 | -46.63023 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 730a60c1-8c4f-3804-8e0d-9179ad0c9ecc | -7.51899 | -46.63445 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b3d8469-14ae-37df-9f67-4817a8dab344 | -7.51536 | -46.63385 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0283a57-5776-3a1e-a72e-af681a573694 | -7.48319 | -46.69407 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65c69763-06dd-393e-950e-3a2896f26fad | -7.47955 | -46.69346 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e286f34-b7e0-3f7e-b284-bb50e6be7b02 | -7.47383 | -46.59214 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7f0e9af-0ef8-33f8-b8fc-d1e875fe89b6 | -7.45129 | -46.866 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05a613a2-4dd8-3ff0-8141-735efb54a2e5 | -7.44824 | -46.83867 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6751bcf2-857e-3673-abbb-591da5169278 | -7.44752 | -46.84303 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04975534-0998-313d-b644-d9c113ca44af | -7.42706 | -46.64967 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 949c70b9-9bc8-34ca-97ed-5dea82363baf | -7.42636 | -46.65388 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ec733f89-c4c6-3da4-9fe4-9d0ebd8ebde2 | -7.38469 | -46.53994 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58baf9ac-e4e7-3bf9-8333-02941c001c9f | -7.38108 | -46.53933 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08750a89-fe5a-3a7d-b3c5-72762427d5a6 | -7.37726 | -46.16398 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 060fe9c8-7a35-3835-b061-7400c0b33c27 | -7.37163 | -46.52913 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4adbaa9a-4530-3358-b4d5-34f18a9574b8 | -7.33129 | -46.29001 | 2024-10-25 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cbd7d45-0acf-302f-9b86-6d5e8e0fd583 | -7.32706 | -46.2935 | 2024-10-25 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d01cf488-27b7-3481-90c0-a9eb58b50657 | -7.27215 | -45.82871 | 2024-10-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2424dfff-8ed8-340c-9b8c-2e783addb96b | -7.26716 | -46.05954 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5295a8ec-601c-3788-a41d-ea75a04090ba | -7.26427 | -46.05497 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README28.md)
