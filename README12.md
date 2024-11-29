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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32f093c2-c764-3976-a31a-863504fb718b | -17.5805 | -42.7483 | 2024-11-29 01:00:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 25b0358d-09ef-3d76-bcd6-92400bae311f | -17.6007 | -42.7434 | 2024-11-29 01:00:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c7d23b8d-b767-3df1-bab3-62e59a714289 | -2.1351 | -54.906 | 2024-11-29 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 512e91e5-1c00-3091-adb1-a643efc76808 | -1.5358 | -51.6142 | 2024-11-29 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 2343d9c3-2b90-359e-a096-c11847f6f4f3 | -8.1429 | -47.9826 | 2024-11-29 01:00:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 47be508f-e94c-3343-a4a5-f5d6db0e6aeb | -4.2411 | -45.7625 | 2024-11-29 01:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| b96fec09-209a-31ee-b0e2-3ed31d813888 | -2.99 | -53.31 | 2024-11-29 01:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edb85366-4e28-31c3-8211-5060d69f68a9 | -2.96 | -53.25 | 2024-11-29 01:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8218d304-bc3c-3a10-9834-19800f940e77 | -2.99 | -53.25 | 2024-11-29 01:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 322d8b83-c6d5-336f-a5a1-80bcf6dee98d | -2.6499 | -48.7772 | 2024-11-29 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| a87a9997-cd65-38d8-a8e2-22d039b297a7 | -3.0028 | -53.3017 | 2024-11-29 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 23f2f8f2-248e-3648-850f-e889436906e6 | -2.8665 | -45.5304 | 2024-11-29 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 154.1 |
| e3afb50b-571f-3742-9861-5eacf62f807f | -5.0399 | -43.6205 | 2024-11-29 01:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e87c5b18-3091-3bf8-a8f7-0a71fd5642c9 | -1.092 | -53.3954 | 2024-11-29 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 67c9e1fe-90de-3610-ac70-c58504fa83da | -2.9844 | -53.3022 | 2024-11-29 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 312.1 |
| 31ea849c-26cd-3002-9346-46a4363a1977 | -4.4405 | -46.5754 | 2024-11-29 01:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 43a2f3ac-571c-3b49-ad15-960ec9e65bd8 | -17.5805 | -42.7483 | 2024-11-29 01:10:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 42f47389-8bae-3544-abec-b8b1160fa94b | -17.6457 | -57.5668 | 2024-11-29 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.7 |
| 34c5f2b3-9447-37b1-80ce-39e140918dd3 | -2.6684 | -48.7767 | 2024-11-29 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 9f39615f-3297-3b06-856d-24f74d502b03 | -2.6498 | -48.7986 | 2024-11-29 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a1114680-0e1d-3768-a6c1-e813c25f97a9 | -3.0028 | -53.2815 | 2024-11-29 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 4ccda5fc-6b4b-3e6f-bc3d-b1fd50a8f044 | 1.8583 | -55.8018 | 2024-11-29 01:10:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 277f2770-44d7-30b1-ab14-329e58ace303 | -1.5358 | -51.6142 | 2024-11-29 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 2d3b3837-9567-361f-8bab-e8345fc601f7 | -2.8664 | -45.5528 | 2024-11-29 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 2f19ce13-faaf-36cb-85ec-3d5bb1cfa655 | -2.8425 | -46.8193 | 2024-11-29 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| ee73daff-ac07-32e9-95ac-25b3983b4066 | -1.5869 | -53.8336 | 2024-11-29 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 5977741c-1e2b-3251-acd2-c984fc161925 | -1.5897 | -52.2915 | 2024-11-29 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 2d201250-2590-3867-8447-26f4d56d8e02 | -2.9844 | -53.2819 | 2024-11-29 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 564.4 |
| 9e19c210-7b0e-37ce-a522-05b78037117b | -2.966 | -53.2824 | 2024-11-29 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 250.0 |
| ad067e31-5c02-3139-8046-029645d7524f | -1.5897 | -52.271 | 2024-11-29 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e07f5fd0-07ec-3daa-95cd-02a6c400df07 | -4.8529 | -41.2445 | 2024-11-29 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 21f81d58-41dd-35f9-8826-9c382b35b63f | -2.1351 | -54.8861 | 2024-11-29 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e06e638c-f567-3b24-a9ff-ff1c17d7565e | -2.6683 | -48.7981 | 2024-11-29 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| f9f68ca3-3d81-3ab3-9d4a-6c13a876fb85 | -2.966 | -53.3027 | 2024-11-29 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 9f0e973d-1aac-3911-8406-6b88f4dac985 | -17.6007 | -42.7434 | 2024-11-29 01:10:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 1353b84a-c0a8-3a10-941a-921cb088e803 | -8.1242 | -47.9843 | 2024-11-29 01:10:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 0d7e7cd7-22e6-3d9a-aac2-154dba4ef49b | -2.1351 | -54.906 | 2024-11-29 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| db104e61-e0f1-3e79-87ad-a60258700f48 | -2.6683 | -48.7981 | 2024-11-29 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 0c99e5e1-fbf8-3c4a-91aa-dcabf527af21 | -5.2352 | -44.9155 | 2024-11-29 01:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| d406434e-e95c-3339-8224-a2ba12d24f9b | -2.6684 | -48.7767 | 2024-11-29 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 3e52de74-c9bd-319d-881a-bb4dbade4c12 | -4.4405 | -46.5754 | 2024-11-29 01:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 2535b3e8-89bd-3d20-947e-dab14935e1ec | -17.6007 | -42.7434 | 2024-11-29 01:20:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1de4ba5e-d30d-3b63-9797-7c716509e63d | -2.6499 | -48.7772 | 2024-11-29 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| e2f793de-bfc6-38cd-ad25-bbd9c1d92812 | -2.6498 | -48.7986 | 2024-11-29 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 0c9dc8b9-6afe-388d-a924-68cb5ac5668d | -5.0399 | -43.6205 | 2024-11-29 01:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 3325b664-8585-380a-813a-745e021d9cbe | -17.5805 | -42.7483 | 2024-11-29 01:20:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0b7bc9b5-80b2-360a-8785-dd17773c825b | -2.1351 | -54.906 | 2024-11-29 01:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d01a2965-a7d2-31f4-b876-6111d2e5ff47 | -2.8665 | -45.5304 | 2024-11-29 01:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 9c6f9e24-73b8-325b-a962-57bb3eac90f1 | -2.1351 | -54.8861 | 2024-11-29 01:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e173f5b8-f8db-3dea-ac36-33bfcc74d770 | -1.5897 | -52.271 | 2024-11-29 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2a21a7d0-47ce-3eab-b24f-72545e3fb530 | -1.5869 | -53.8336 | 2024-11-29 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 11d1d033-90e9-3d0f-a17a-c183e0bfd339 | -1.5358 | -51.6142 | 2024-11-29 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 76a3a4fc-38b0-3e71-a3a2-912dfa2b9788 | -2.8664 | -45.5528 | 2024-11-29 01:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 101.1 |
| f1e3baeb-fd29-30e3-8531-1e80931f8854 | -1.092 | -53.3954 | 2024-11-29 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 47867d33-ae23-3c23-ad5a-0a39a86599da | -2.8425 | -46.8193 | 2024-11-29 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 5d371e08-42b2-306e-88c8-3655b08bb938 | -4.2411 | -45.7625 | 2024-11-29 01:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b6c0c4ad-7905-3fee-8090-479dc8eac3b8 | -1.5897 | -52.2915 | 2024-11-29 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 90342cf8-cc3c-356b-9e11-8970a6ba35aa | 1.8583 | -55.8018 | 2024-11-29 01:20:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 03a31cf2-50b3-361b-bd08-6b9474184b97 | -3.259 | -53.6388 | 2024-11-29 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d8e1364b-dac1-3284-b7e2-7aa0f677c05d | -2.9844 | -53.2819 | 2024-11-29 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 454.5 |
| 14831c77-56e8-385b-9654-a3449c3e8e12 | -1.5897 | -52.271 | 2024-11-29 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 0e7e410e-2f4a-353d-921f-16ead741ed77 | -4.4219 | -46.5764 | 2024-11-29 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 6dc25660-09de-389f-a469-0a5f2ef4940f | -4.4404 | -46.5975 | 2024-11-29 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| aedc2b39-15d3-3d5c-bbf8-d3b936beeab7 | -2.966 | -53.3027 | 2024-11-29 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 54b15cfa-3730-3326-abd4-9d5a07074e63 | -1.6997 | -52.4535 | 2024-11-29 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 35f1d38b-ff5a-3fec-8120-05621785e315 | -3.259 | -53.6388 | 2024-11-29 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 8e5e4321-8a84-3c2c-83d5-ed02d54bdbaf | -2.6684 | -48.7767 | 2024-11-29 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 265.7 |
| 8802669e-5d71-38d9-baf0-4d0a7baa977d | -5.0399 | -43.6205 | 2024-11-29 01:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 220e1bb5-916a-3964-afff-e8d2bc8b985a | -17.5805 | -42.7483 | 2024-11-29 01:30:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 114.5 |
| d9e916d4-09b6-3f77-834c-e611cee1a95f | -4.4405 | -46.5754 | 2024-11-29 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 185.9 |
| 02f8e669-6223-375c-8043-6b47e32fdf15 | -2.6683 | -48.7981 | 2024-11-29 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 224.5 |
| e99c07ba-6baf-397c-878b-4306c263c601 | -17.6007 | -42.7434 | 2024-11-29 01:30:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| cc29f453-6df1-339d-8408-7bada097bd02 | -11.4014 | -45.0977 | 2024-11-29 01:30:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 058e56c6-da94-35c5-b430-dfd77e7e8d60 | -2.9844 | -53.3022 | 2024-11-29 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 303.5 |
| 45500f0b-8180-3e6b-9bd7-20f8b4952f8a | -1.092 | -53.3954 | 2024-11-29 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9b3e3a9f-938d-3418-961f-adb9c87c3541 | -2.966 | -53.2824 | 2024-11-29 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 2b48f5a3-83bf-3adc-9aaf-a362806d5662 | -1.5869 | -53.8336 | 2024-11-29 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 1d778879-8461-3489-9b59-2416ebae4fe4 | -2.1351 | -54.906 | 2024-11-29 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 272f4cee-51c6-305b-b2b0-760c178269fc | -3.0028 | -53.3017 | 2024-11-29 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 38758b6a-8d11-3ed2-9de3-7df2ea3fe06c | -2.8664 | -45.5528 | 2024-11-29 01:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 4b4f071c-0170-3b89-bf12-c94e88d0d6db | -2.8665 | -45.5304 | 2024-11-29 01:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 1843f03b-f152-3dd5-bf10-0fce4b52f0ac | -2.6869 | -48.7762 | 2024-11-29 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3392a1c5-cc25-3c2e-9bf5-eeb304513e89 | -3.0028 | -53.2815 | 2024-11-29 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 663a2b71-7d5d-38f1-aede-c564d2a2f426 | -11.4018 | -45.0746 | 2024-11-29 01:30:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 2d216981-d5c9-33df-9c8b-bab298aa5e83 | -1.5897 | -52.2915 | 2024-11-29 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 31668358-dbfe-3d09-a05a-b2868dd0d073 | 1.8583 | -55.8018 | 2024-11-29 01:30:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ff3ed40f-705d-38f0-b338-5e6be6b5acfa | -2.6499 | -48.7772 | 2024-11-29 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 222.0 |
| 3eb38b23-1d67-39bb-8c6e-e5bea34f15d5 | -2.6498 | -48.7986 | 2024-11-29 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 201.2 |
| cdd1d660-b70b-3f6e-bfcf-a7ca0c5c9462 | -2.6498 | -48.7986 | 2024-11-29 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| b8436708-542f-3ad9-aaf1-cd7625a41106 | -1.9726 | -46.4467 | 2024-11-29 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 0efdec8b-daab-3fa9-b933-3382faa191c1 | -4.4405 | -46.5754 | 2024-11-29 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 190.4 |
| 19674be9-4172-3aac-9863-138c480b6fc7 | -1.092 | -53.3954 | 2024-11-29 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 2809482d-5d87-39a7-83e1-6677d68766ee | -3.259 | -53.6388 | 2024-11-29 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d0bccd17-59a5-3335-9d55-c0eb73bba864 | -4.4404 | -46.5975 | 2024-11-29 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 51c64124-d53f-3ed0-8b8a-747e368f34ec | -2.966 | -53.2824 | 2024-11-29 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| b9d0c238-fec8-3eda-a5eb-a7206c067356 | -3.3253 | -46.692 | 2024-11-29 01:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 242aaeaf-6a88-3830-893e-b4c84bef9922 | 1.8583 | -55.8018 | 2024-11-29 01:40:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2b5a72f5-0d0d-3a10-88e8-eba5cc29710e | -2.6684 | -48.7767 | 2024-11-29 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 187.3 |
| 317e1ed8-d6d9-39c9-80e8-ffb80d073409 | -1.6997 | -52.4535 | 2024-11-29 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 532707db-f858-3742-99e5-c97cc1d85b3e | -2.6499 | -48.7772 | 2024-11-29 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |


[Clique aqui para ver as próximas entradas](README13.md)
