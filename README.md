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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50f0a2fb-bcf3-3144-b720-d18b0177ad2a | -17.88 | -57.49 | 2024-10-16 00:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d810dd13-5ab8-3172-ac64-d186edec7d11 | -17.91 | -57.43 | 2024-10-16 00:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9cd71f8d-7a53-3535-98d2-cdd6786e59d3 | -17.84 | -57.46 | 2024-10-16 00:03:44 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 637b0ed3-eb5e-3e68-ba49-e89b13aeff5c | -9.12 | -47.01 | 2024-10-16 00:04:34 | MSG-03 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a2cb9f4-d71a-3238-b494-0c642c94d1cf | -9.15 | -47.02 | 2024-10-16 00:04:34 | MSG-03 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| baaf8a6f-55c6-3e24-9546-6832fd353c65 | 1.0199 | -52.2162 | 2024-10-16 00:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 633fd26c-0fda-3439-9e4a-4b1eaa01c9c7 | -3.11 | -54.24 | 2024-10-16 00:05:11 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33a7d7fd-8afb-326a-af01-e12e9f43e6c0 | -2.8795 | -51.6901 | 2024-10-16 00:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d4b8e511-6308-3938-ba1d-fddca2e2c155 | -2.8795 | -51.6695 | 2024-10-16 00:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 79e45fc9-4a12-3a9c-9b17-76925e60f433 | -3.1099 | -54.2263 | 2024-10-16 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b8831d52-156c-35d7-9f59-c0cd0b177e35 | -3.1283 | -54.2259 | 2024-10-16 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 132c4426-59fe-3521-95ca-274d55309893 | -3.204 | -48.9312 | 2024-10-16 00:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 97216596-6bff-3e65-ad3f-a242ce5fbb64 | -3.2041 | -48.9098 | 2024-10-16 00:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| dca031e2-acc5-3351-a235-6d79e42459b7 | -3.2225 | -48.9306 | 2024-10-16 00:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 3c3b921c-f3bb-3f96-bebf-5df689033d5d | -3.2226 | -48.9092 | 2024-10-16 00:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9b4fef38-1b0b-362d-9747-d69936583d27 | -3.2502 | -46.8929 | 2024-10-16 00:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 69be7207-ce56-39c0-89d5-d93ec5627e1e | -3.2695 | -50.9327 | 2024-10-16 00:05:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e00a7b14-9b7c-3c55-b291-f3560ce6459c | -3.2879 | -50.9529 | 2024-10-16 00:05:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 722ab5e1-0de2-35d9-b244-a1ba47a6dbc7 | -3.288 | -50.9321 | 2024-10-16 00:05:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 21d428d4-1625-3907-816e-1d420ca054b3 | -3.5107 | -43.2429 | 2024-10-16 00:05:26 | GOES-16 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 6998ac72-c90e-39a0-97e4-6e05c5730fbc | -3.9581 | -46.422 | 2024-10-16 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 08bebe37-6db8-3217-8624-da2ecb521ad9 | -4.3588 | -50.9764 | 2024-10-16 00:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| cdc0f546-ab1f-37a8-acae-564e27e1eb48 | -4.8283 | -46.9958 | 2024-10-16 00:05:33 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3b74092f-edae-3e15-a2f1-a1b669e6f069 | -5.1677 | -44.0049 | 2024-10-16 00:05:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d18d8f75-48a6-3e05-b688-780f46d8e1ae | -5.2306 | -47.9566 | 2024-10-16 00:05:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 120.9 |
| b41f8542-96ef-3547-b607-0d78e18539f8 | -5.4991 | -46.9121 | 2024-10-16 00:05:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 74f81118-dcfc-3ad4-9385-f600ca2b03c0 | -5.4993 | -46.89 | 2024-10-16 00:05:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 02cf0c34-3f42-3f7b-8702-e332c00134de | -5.5178 | -46.9109 | 2024-10-16 00:05:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 37a7d7a9-03c5-337d-8242-09b5bb4bc878 | -5.5179 | -46.8889 | 2024-10-16 00:05:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 9c6d7f90-9a3c-3eda-9c05-31c4d38be117 | -9.1727 | -65.4132 | 2024-10-16 00:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| fa2f3608-af76-3fdb-bb4a-99ba9acd85a9 | -9.1728 | -65.3945 | 2024-10-16 00:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 4e52bc62-d756-317b-866f-a4dd5419204d | -9.1914 | -65.3939 | 2024-10-16 00:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 93dc5649-1df3-3688-8e5e-c79bd70bca98 | -10.2442 | -47.2824 | 2024-10-16 00:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 428ce51b-d7ef-36ac-a0b9-ad74cb33fad5 | -11.6915 | -65.2432 | 2024-10-16 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 2c41c863-89ca-37b9-b82e-7c9365912ecd | -11.6917 | -65.2243 | 2024-10-16 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 03553607-5a5d-395e-bc85-625b697c9676 | -11.6918 | -65.2054 | 2024-10-16 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 68638498-a8c1-3da3-a0bf-849db09caeb2 | -11.7103 | -65.2424 | 2024-10-16 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 80b2f654-78b5-33b4-8b3f-b6941d826d3f | -11.7104 | -65.2235 | 2024-10-16 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 3c0d45f4-d0ff-32e9-b9be-bb2587f87f3f | -11.7106 | -65.2046 | 2024-10-16 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| be9ef9a0-508f-31c6-9f57-21d9cdf8e6b2 | -11.9381 | -64.8729 | 2024-10-16 00:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| edfaad19-e56a-3953-9e34-3e0d6d7c7696 | -12.3793 | -63.7294 | 2024-10-16 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 3a0c3837-6211-32fb-907d-c07cd4aa6eae | -12.3795 | -63.7103 | 2024-10-16 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 97ffe84d-eee1-3079-a3c7-1117c31c8713 | -12.3982 | -63.7284 | 2024-10-16 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 115.2 |
| c5f6f0e5-ca3a-3b36-9625-876a7ee781f6 | -12.3983 | -63.7093 | 2024-10-16 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 61e2d739-43d8-3ef0-b7d1-b7c9b1aee3ff | -12.4602 | -63.0361 | 2024-10-16 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 39f7c0ad-2e99-3a5a-9b32-9c988e6632f8 | -12.5149 | -63.2822 | 2024-10-16 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| a258eebf-6b72-38ae-ab50-ea07dba5f68f | -12.5338 | -63.2812 | 2024-10-16 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 37ae8acf-c4a7-38c7-b044-9ccb65ea260e | -12.5339 | -63.262 | 2024-10-16 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 110.0 |
| e9d097a5-c7d7-3048-9767-42ded93f472a | -12.7633 | -62.942 | 2024-10-16 00:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| fc25f703-bf7b-3e41-a780-74c52acc2960 | -12.7822 | -62.9409 | 2024-10-16 00:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 700a1249-b0ae-325f-a018-f82d6302a27c | -12.9757 | -62.448 | 2024-10-16 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 49d21633-3a88-3aeb-822a-94d2a4e0b57f | -12.9759 | -62.4287 | 2024-10-16 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |
| c5feed72-a08b-3a65-bffc-f90784521517 | -13.0325 | -62.4638 | 2024-10-16 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a0bd2d43-ab00-3494-98b0-51d5372b02ce | -15.6612 | -59.975 | 2024-10-16 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e0323752-b42e-3b09-a893-0b434c61f33a | -17.2439 | -42.6575 | 2024-10-16 00:06:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5e97a95f-168b-33f2-8b76-ba743f5e8127 | -16.9154 | -57.856 | 2024-10-16 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| 7e7411aa-4206-3eb9-be19-4e3b65f996c2 | -16.935 | -57.8538 | 2024-10-16 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 8c114de1-19f6-32c6-b9b8-29ca8ad4c633 | -16.9546 | -57.8516 | 2024-10-16 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 195.0 |
| 03d357e5-cf7e-38f6-be12-d54e1f684370 | -16.9549 | -57.8312 | 2024-10-16 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 251.0 |
| 422c488a-b530-3b50-b9f6-7690fe99e2a8 | -16.9742 | -57.8494 | 2024-10-16 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.9 |
| 7ed4cc02-f534-327a-89ef-efab44c51a89 | -16.9745 | -57.829 | 2024-10-16 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 171.2 |
| 43126fee-03b8-3bc6-98f5-cdd884111f70 | -17.0066 | -58.2934 | 2024-10-16 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 388b0d93-1d52-3a2e-9db2-d516537a1f51 | -17.0262 | -58.2912 | 2024-10-16 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.6 |
| a338aa85-f1c4-399f-a5ff-3c23bbbe3d55 | -17.0678 | -56.8764 | 2024-10-16 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 5d2fe835-8a09-340e-a7fa-0c91753dc88b | -17.0682 | -56.8558 | 2024-10-16 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 49255017-2b71-358e-91c9-952b42fc0370 | -17.1754 | -57.4995 | 2024-10-16 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 25116397-9053-370c-8d8f-1f3bd07ad32a | -17.1758 | -57.479 | 2024-10-16 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 7f5d38ff-7286-3e98-9a0a-c94b0d996a5f | -17.1951 | -57.4972 | 2024-10-16 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 8f696cab-f024-3cf8-b50f-c8d548570592 | -17.1954 | -57.4767 | 2024-10-16 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.0 |
| c0272495-b09e-3df5-b9e9-91ac8f47b673 | -17.196 | -57.4357 | 2024-10-16 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 6bc9e305-d194-39a0-8dea-934921c4521a | -17.2177 | -57.3102 | 2024-10-16 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 079b7651-a45a-34a3-a13e-f5fc9cd680d7 | -17.8675 | -57.252 | 2024-10-16 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| a118b292-6cd9-3481-9c75-832f72a3eabf | -18.2544 | -56.5821 | 2024-10-16 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.5 |
| 73780f42-4f4a-373b-86f8-91829cb86cd1 | -18.2548 | -56.5613 | 2024-10-16 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 0b399b0d-dbad-339d-9bee-7c280965ee77 | -18.2742 | -56.5795 | 2024-10-16 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.9 |
| 501bc6b0-d511-30a4-b15e-cb62a8afdec5 | -18.2746 | -56.5587 | 2024-10-16 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.8 |
| 941484d9-ab0d-3fc2-b5ce-5339438468b0 | -19.5615 | -56.968 | 2024-10-16 00:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 177.1 |
| 244e77f9-b56a-3d93-a69b-a9bc4a5c51f9 | -19.5619 | -56.9471 | 2024-10-16 00:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.8 |
| adcaddf7-7b15-3803-83ef-6c8272fc0321 | -19.5816 | -56.9653 | 2024-10-16 00:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.0 |
| 49836766-a435-378b-a341-36dfdc629753 | 1.0199 | -52.2162 | 2024-10-16 00:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9568a2c1-97a5-33cc-935e-9e2b00928c0f | 1.0016 | -52.2164 | 2024-10-16 00:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 67e508d8-52c8-335e-abbf-dacf09a52a04 | -3.1098 | -54.2464 | 2024-10-16 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 689a48a5-98d4-32e1-950b-e143ff294a8e | -3.1099 | -54.2263 | 2024-10-16 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 216.2 |
| 345b009b-5797-3644-aba3-9a938ddebc18 | -3.11 | -54.2063 | 2024-10-16 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 62969000-ea80-3625-835c-3448793eaba8 | -3.1282 | -54.2459 | 2024-10-16 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 5ee2deef-bdf5-3f9c-a517-6fe7a44662c4 | -3.1283 | -54.2259 | 2024-10-16 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| df30e1b9-c38a-3fa9-a32e-bbcc2f4e6061 | -3.2225 | -48.9306 | 2024-10-16 00:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 8dc1ff37-7cc8-35eb-90e5-dcf403646aac | -3.2226 | -48.9092 | 2024-10-16 00:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| ad467d8d-566b-32bb-a54b-9216f1182634 | -3.2879 | -50.9529 | 2024-10-16 00:15:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 14f63cec-5cdd-3294-876d-2819d4f5398b | -3.288 | -50.9321 | 2024-10-16 00:15:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 9a106f43-dadb-371b-8949-bd23255ef571 | -3.5107 | -43.2429 | 2024-10-16 00:15:26 | GOES-16 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 757c6e84-d1f2-33b8-b8d2-53584266da4c | -4.3468 | -46.6907 | 2024-10-16 00:15:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| effa83e5-d64f-3db9-a710-c4dc65775fa0 | -4.3588 | -50.9764 | 2024-10-16 00:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| f74bfc47-746c-3e25-9646-36e46a7de8a1 | -5.1677 | -44.0049 | 2024-10-16 00:15:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 950bca78-a6d5-394a-9bbf-94df1150f696 | -5.2306 | -47.9566 | 2024-10-16 00:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| c0e5665e-8efe-3cb1-9a7f-9847fb4f8476 | -5.4991 | -46.9121 | 2024-10-16 00:15:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 175.1 |
| bff4cebf-595f-3d98-aa99-e47fdefc64f1 | -5.4993 | -46.89 | 2024-10-16 00:15:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 156.1 |
| af8b9a01-509e-3dc0-8066-48e45230577c | -5.5178 | -46.9109 | 2024-10-16 00:15:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 274.5 |
| 6d9bcad0-4562-34d3-ac0c-86e958e49044 | -5.5179 | -46.8889 | 2024-10-16 00:15:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 2b0f3201-fff4-357f-8591-1564e055c791 | -5.5364 | -46.9097 | 2024-10-16 00:15:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |


[Clique aqui para ver as próximas entradas](README2.md)
