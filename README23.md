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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0c533c6-b1a9-3cd1-b15b-be9807bf22a6 | -16.27576 | -59.40472 | 2024-12-28 05:03:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78509581-3ad9-3a0c-8361-69e83899327a | -12.34947 | -64.17622 | 2024-12-28 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79a107e6-62d8-3435-97d0-b51fa4d8cc95 | -16.10154 | -60.07748 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 06f6580e-097b-303d-a9a2-eb4684029394 | -15.276 | -59.88763 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dc42866-cdfa-3277-a74c-769d53ba21e6 | -11.13233 | -43.30966 | 2024-12-28 05:03:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 712c674e-490c-3d1a-97f0-3df4f47aad0f | -15.49142 | -60.04876 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7372d242-cd0e-3d22-8668-e368cae17374 | -11.14007 | -43.30383 | 2024-12-28 05:03:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 26b27fda-3e39-3be7-b1b6-f4972749b1ee | -12.44905 | -64.14865 | 2024-12-28 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a996e51c-d35c-3cc3-bebf-ba318044fa05 | -15.27321 | -59.88316 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 459db747-03df-3053-b16a-b0f9473679d8 | -16.10134 | -60.12154 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b32cd1d-5865-3136-9436-2b316bea15ee | -15.09485 | -59.62852 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e2a019f7-42c1-3c2a-883c-e542203727ef | -15.51791 | -59.42465 | 2024-12-28 05:03:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 103ffb56-a37a-3f8a-b050-d8c98c40d93c | -11.97415 | -63.51451 | 2024-12-28 05:03:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa48dff9-8759-3f1a-9600-95fb9dcf501c | -15.60923 | -57.34175 | 2024-12-28 05:03:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fe552ec-baf8-3ca3-ae8d-4ac301abbfcd | -16.09875 | -60.07298 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 59360869-5a53-3005-8e42-191d84757f7f | -15.27665 | -59.88377 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c76a7d5a-04c8-3167-8d92-b0afdf8b62d0 | -15.7453 | -59.55588 | 2024-12-28 05:03:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2bf0e268-b08a-3b56-b40b-06e7e2c4be2f | -15.48451 | -60.04753 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c31eb27-1152-34da-b3fb-e239196a047d | -11.97494 | -63.51016 | 2024-12-28 05:03:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 944ca5d1-6a09-321d-b753-6391abd52a0b | -16.20151 | -56.8156 | 2024-12-28 05:03:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16a1ab62-d120-323f-8562-3118a8d108de | -14.10916 | -59.93937 | 2024-12-28 05:03:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d89377af-a39b-3e30-8d6c-5e3de383ec85 | -12.2787 | -64.27924 | 2024-12-28 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a48a431-4bab-398c-ba5d-92fced4d746a | -12.34491 | -64.17532 | 2024-12-28 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0090784-711f-330b-a91e-b2028a53eb60 | -14.10501 | -59.94272 | 2024-12-28 05:03:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ae96d4b-2caa-3e8a-ae4f-d2c6145a1fac | -15.55052 | -57.78374 | 2024-12-28 05:03:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c49ee32e-3631-38a5-8625-293da91d10b2 | -11.97054 | -63.50933 | 2024-12-28 05:03:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5a1c212-abfc-3a69-9fa5-ad65b333a742 | -15.51514 | -59.42033 | 2024-12-28 05:03:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dbf4472-fec2-382b-a7c1-0964cd21be9e | -16.0981 | -60.07687 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3b0eac2b-2775-36bb-b656-63bb47da6128 | -15.48797 | -60.04814 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d37ca8c0-29c4-3471-86b1-ff491088d750 | -16.27464 | -58.93265 | 2024-12-28 05:03:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| eb52c426-3ccd-3e29-ae47-cfcc43192537 | -16.10219 | -60.07358 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c78ac379-6ab2-3e81-83ad-9e6a6bbdcf7f | -16.21309 | -59.93342 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4037c8ad-9e66-3086-9b90-403c81563c1f | -15.09432 | -59.63132 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e407123-e13a-394e-a1fa-fb1a6962846e | -15.09496 | -59.62753 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 10cbffd1-ec79-31a4-afb3-0ffda5ce217c | -12.44817 | -64.15337 | 2024-12-28 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73daa056-5b6f-3ff3-af5d-9e1ebc261c28 | -11.90461 | -64.05379 | 2024-12-28 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99e07e42-5d13-3358-b631-a1bc9fdfb734 | -12.34919 | -64.17833 | 2024-12-28 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cfa34c6-5f5f-3364-abb6-e84d1204e921 | -15.09422 | -59.63233 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34a6fc1e-bbc5-3e93-98ff-d29578c62ac4 | -15.55384 | -57.78429 | 2024-12-28 05:03:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98a2af5e-fbc3-355c-8bac-81e5ef8e2c91 | -15.27054 | -59.88313 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3b1926a-fe9a-3f80-a2cf-0292d44d46af | -15.27117 | -59.87926 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f658bbfb-55b4-3748-ac26-8737c0c99bdf | -16.10055 | -60.12025 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9d02785-ac34-3db5-98df-22867430bb76 | -15.48862 | -60.04424 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abc76002-d0f1-3121-9af0-87bb172a8a6c | -15.03907 | -59.68945 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7510e552-50cd-368c-858c-15da1deee6b3 | -19.92067 | -55.74044 | 2024-12-28 05:05:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 55ce12ff-0605-3fc6-af36-355329badcd7 | -21.63395 | -53.43043 | 2024-12-28 05:05:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffa59db9-4aca-3963-b2bb-7718e9183977 | -20.26289 | -55.13708 | 2024-12-28 05:05:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b97d45f-5505-3a7e-b774-0961b414e342 | -19.92253 | -55.74251 | 2024-12-28 05:05:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 41395423-32e9-3107-919a-969a3ce53ccc | -19.92426 | -55.741 | 2024-12-28 05:05:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1077dbdb-0d20-3343-a66b-e3f999245080 | -24.24121 | -50.74089 | 2024-12-28 05:08:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cbf4649f-3e10-3759-a50f-39cfa631e9a7 | -3.96847 | -46.68122 | 2024-12-28 05:14:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f1020292-5d16-3fb8-a783-6b32aab76f72 | -3.95989 | -46.66695 | 2024-12-28 05:14:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 84b15ee5-7c76-38bb-bc80-131909d3d3d2 | -3.72746 | -47.18741 | 2024-12-28 05:14:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b9c09735-62cf-3684-a1f1-92cb6a18e502 | -5.57292 | -46.12608 | 2024-12-28 05:14:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 4189f1d0-27f7-314b-95ad-875909f28122 | -3.94562 | -46.75789 | 2024-12-28 05:14:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 31f06d33-da94-30e4-aa35-bb60fc37b3f9 | -6.98685 | -35.01833 | 2024-12-28 05:14:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 51.9 |
| 4ecf9baa-d9c8-30f6-a0fe-180bc348e300 | -3.7385 | -47.18904 | 2024-12-28 05:14:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1292312c-74b1-3a94-9468-c1b24b686738 | -4.08831 | -47.09484 | 2024-12-28 05:14:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4707660a-e58b-3cd6-ab52-48707f9569d2 | -4.07738 | -47.09343 | 2024-12-28 05:14:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| d4eff703-fd23-317a-9816-0d54c1e86f43 | -4.55807 | -45.98511 | 2024-12-28 05:14:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 9ceb40a9-9666-3da0-8599-d8a2f57d2c9e | -6.98906 | -34.99686 | 2024-12-28 05:14:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 8334aaa0-3d64-37a5-8e63-f6433933bf33 | -6.19536 | -41.56475 | 2024-12-28 05:14:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 556ed98d-421c-3ab9-979c-1f25e47e1978 | -2.29414 | -45.57139 | 2024-12-28 05:14:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 83aaa7a2-e9c3-3dc5-be38-46977a4c2bbd | -3.98959 | -46.68442 | 2024-12-28 05:14:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4db2804b-0d2c-3c8a-83a5-24ee0e78bbea | -6.19674 | -41.55516 | 2024-12-28 05:14:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7251de78-09e2-32f2-a02a-105e4e36fffa | -4.1318 | -46.67903 | 2024-12-28 05:14:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| beb9655d-3b2c-3278-9c7e-f4c0ad346984 | -4.00015 | -46.68605 | 2024-12-28 05:14:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 804971f1-c038-3cf5-95c3-5840d3b99ca3 | -4.03723 | -47.03925 | 2024-12-28 05:14:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 2bd5bd5c-41ab-3935-a011-5aa34f6dd4af | -4.03509 | -47.05315 | 2024-12-28 05:14:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 2cbee92c-9b8d-36ff-8e7e-e4e41c057617 | -4.12008 | -46.71152 | 2024-12-28 05:14:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| be083db4-6936-3b63-b1fd-9e0fc47bc8ff | -3.90587 | -46.9093 | 2024-12-28 05:14:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 15fa0af1-0231-36be-9eef-4516cc609697 | -6.99066 | -34.98977 | 2024-12-28 05:14:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 45.4 |
| 0386cb97-8c80-384c-8598-ec81ab0e2fcf | -4.07954 | -47.07973 | 2024-12-28 05:14:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 74499352-6889-3172-9522-8d526bd7db1b | -12.33539 | -43.67273 | 2024-12-28 05:16:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0ccb596c-23d0-3d5d-9fc1-b9429febe2fa | -11.13626 | -43.30169 | 2024-12-28 05:16:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 60f556e4-7549-343c-9813-11fdcad2a344 | 3.50934 | -60.67002 | 2024-12-28 05:52:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec7153d7-94b7-35b3-aeda-5f6b526602ce | 3.96025 | -60.56025 | 2024-12-28 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c628b9cb-83ab-348f-917d-c7155347cb7a | 4.17765 | -60.08163 | 2024-12-28 05:52:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0f399d4-9a72-33af-82c5-5f3c22f03b5e | 3.96321 | -60.5517 | 2024-12-28 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed0bdc3e-a375-3457-b170-a2e847a81b82 | 3.96654 | -60.54444 | 2024-12-28 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bfc284c-d2e2-3782-ac2e-3ef7597184c7 | 3.95962 | -60.55634 | 2024-12-28 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad6a45b5-f0ef-3f7d-900b-7b6b5f18554b | 3.50576 | -60.67461 | 2024-12-28 05:52:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a093d06-3239-39fd-9896-43ebd28b58e4 | 4.03257 | -60.5777 | 2024-12-28 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74749424-0107-3c6a-8e58-a2468a749bd0 | 2.81364 | -60.76918 | 2024-12-28 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b94e052-f6d5-352a-9acf-1392add9d3ea | 1.62742 | -60.33959 | 2024-12-28 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c30e7d7-8473-3daf-b1f7-d140a5ca6651 | 2.81352 | -60.76852 | 2024-12-28 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8f90ce5-150a-38d9-b2e8-ec07a9f52e00 | -16.09757 | -60.07567 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 10d10abb-7939-325e-bf91-c0266a5ee2f9 | -15.09049 | -59.63131 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 928fef6f-5da9-34b2-bb17-58e9c688ad18 | -16.1034 | -60.07649 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e55753f5-71ae-3dbf-a15a-f8b495cb3ec0 | -16.098 | -60.0715 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 260050f8-ffd8-3389-b2c4-d5aff9114856 | -12.44939 | -64.14925 | 2024-12-28 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70c14943-d716-31b1-a5ac-af79f7058a67 | -15.27551 | -59.88544 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5593ef08-4f1b-3f43-8fd3-4b39bcd7be1d | -15.09644 | -59.6319 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbe2347c-821a-3dff-823c-9fcc3a4c63c4 | -15.4882 | -60.04548 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac7cd43b-f336-391c-a3fe-8cfc00bf5354 | -11.90228 | -64.0492 | 2024-12-28 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26fdafab-35b3-30f6-af52-e2061178dabe | -16.09898 | -60.11902 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 452aef48-1c6c-34b6-9d66-59bac9944167 | -11.97418 | -63.51253 | 2024-12-28 05:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2542742-ecb0-37f4-9fe3-d51593fb176e | -15.09096 | -59.62683 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49f2984c-ec8f-380e-8015-3b241d9c8876 | -15.49401 | -60.0462 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd6e88d2-3ca6-309f-ac7f-ec7aa1b28e7c | -15.09691 | -59.62745 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README24.md)
