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
| 481fe63c-1e11-3ba5-bb73-bc81e89d3221 | -16.0029 | -50.8801 | 2025-10-01 01:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 8cb690b6-3e19-3c87-a071-7560e64bd30b | -15.1389 | -46.4485 | 2025-10-01 01:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 1cf1c292-23cf-3d88-a18a-6c95bf409969 | -15.1806 | -49.1011 | 2025-10-01 01:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6c91d230-1d1d-374d-94c1-67485b42a4da | -13.2969 | -50.6821 | 2025-10-01 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 06ba5918-8990-3b7f-80e8-b5d5fdf0fc58 | -10.8242 | -45.3841 | 2025-10-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 6df44919-47ae-37c5-ba11-35bf0d00791f | -3.0827 | -47.0088 | 2025-10-01 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| e52099f7-ba37-3564-839c-faaf0abb5bb0 | -3.4762 | -50.0883 | 2025-10-01 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b9cd58b6-f08a-38f4-a1bd-3eff067a099d | -5.3382 | -43.7391 | 2025-10-01 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 0f3c3a06-e553-3e12-8a51-af49a87b90d0 | -9.3089 | -54.5229 | 2025-10-01 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2af1880f-05a2-3094-ab7d-73dc52e23616 | -5.3195 | -43.7405 | 2025-10-01 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 3aac6c2f-2916-3701-b6d0-cdfd6db2fb76 | -10.1084 | -50.299 | 2025-10-01 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 9596840c-6f0b-352d-8c8c-e6cbcf8573d7 | -14.7826 | -45.7981 | 2025-10-01 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| d3c5e892-f09d-3d3d-9535-af4f62543077 | -16.0225 | -50.8771 | 2025-10-01 01:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a90a4c5f-cfc7-3db3-9a47-c7423538ac20 | -20.6103 | -46.2098 | 2025-10-01 01:30:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 80.3 |
| a11ca522-1879-362d-b68e-02fe9f47b9c0 | -14.8021 | -45.7946 | 2025-10-01 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| adca0620-739c-311f-95d1-8be83289c785 | -13.2973 | -50.6605 | 2025-10-01 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.0 |
| a7771d12-b534-37c9-8e32-c29f2ffb03fa | -13.3274 | -47.8536 | 2025-10-01 01:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c33e28f2-b915-36d4-a8a3-f0639170c9ff | -9.9383 | -43.6483 | 2025-10-01 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 104f2826-11f9-34b4-a8a9-7e6d37e0742c | -7.8155 | -47.0667 | 2025-10-01 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| f4d8b8ce-8947-347b-90e4-47c06c9af337 | -3.1013 | -47.0082 | 2025-10-01 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 36d7e8f7-44a9-3d1a-987d-6f901e7a630e | -16.2558 | -50.9494 | 2025-10-01 01:30:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 2ca321f8-d06a-397e-8a14-f2ff5ce572a3 | -15.1611 | -49.1042 | 2025-10-01 01:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 28aa6e74-7cb5-36b9-84c9-dd1c3cec0ada | -9.938 | -43.6718 | 2025-10-01 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 35d6fff1-3d7d-34ca-99fb-e3125775b6fa | -11.383 | -45.0543 | 2025-10-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| b1417dc4-e2de-365d-b111-c9a4af8f4956 | -9.2902 | -54.5242 | 2025-10-01 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ca5c3276-7f41-3049-bdc6-11560536ee7b | -10.862 | -45.4019 | 2025-10-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 7450b957-867f-39c3-9ea1-8958049664ef | -11.1523 | -54.3104 | 2025-10-01 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0275d596-d967-348d-ac6a-0bf640a120ec | -10.8429 | -45.4044 | 2025-10-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.3 |
| f0347c62-4599-322b-8e78-6ced58fc27a9 | -16.2562 | -50.9275 | 2025-10-01 01:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 96edec2f-4aa1-35a8-a62b-b8e2f486f47a | -16.2361 | -50.9525 | 2025-10-01 01:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 2c3d7c08-067d-3612-bdad-2bbaad6834d2 | -11.6835 | -44.2908 | 2025-10-01 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 044724d2-0e24-38bf-ace4-44c1881dccd2 | -10.8425 | -45.4274 | 2025-10-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 06ac73c9-3786-344b-a0ee-1396c14aa41d | -14.8021 | -45.7946 | 2025-10-01 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b17d481c-bbf9-3a54-ae5e-f8b36ad2226a | -21.0572 | -45.6638 | 2025-10-01 01:40:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 5cc3c92e-886a-3a34-8faa-88cd42eef9bd | -6.1342 | -44.7375 | 2025-10-01 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 88a64604-adfc-3913-ae87-7cc7aaf00724 | -3.4762 | -50.0883 | 2025-10-01 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 9a46735b-aac5-354d-b1dc-d22b45e22e62 | -14.9181 | -51.6657 | 2025-10-01 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5589952d-98a4-3b29-93f5-dfd2329d1a76 | -3.0827 | -47.0088 | 2025-10-01 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 3b390136-7682-351c-a3fb-2ded6272ad20 | -3.1012 | -47.0301 | 2025-10-01 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 3eecf14a-5fbe-36bf-910c-89e0c6ef0a10 | -7.8343 | -47.065 | 2025-10-01 01:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 46020ba2-d4f6-32b9-a08d-4457dceee68b | -5.8469 | -43.3995 | 2025-10-01 01:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 959ee925-96c5-361c-a5fb-38d6d41841a8 | -9.3089 | -54.5229 | 2025-10-01 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| c9be67e4-0bae-3f90-8968-38d595d9b8e2 | -13.3165 | -50.658 | 2025-10-01 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5dc9f8ac-f422-3a64-8e87-2b7876b7ff01 | -6.153 | -44.736 | 2025-10-01 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 61140fe0-0daa-3d76-9f92-1221a3b6dc15 | -9.938 | -43.6718 | 2025-10-01 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 204e5a04-a196-313f-9da8-d5dfb6602fae | -14.7826 | -45.7981 | 2025-10-01 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 562b7bfb-03c5-396e-9123-9b19dde7a61c | -16.2558 | -50.9494 | 2025-10-01 01:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d92da664-82d4-364f-b22e-259b56c6686b | -20.6103 | -46.2098 | 2025-10-01 01:40:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 98097154-e20b-353d-9174-59cfb36fa183 | -10.1084 | -50.299 | 2025-10-01 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 39308f97-7de2-3407-8509-b2bf0e55a862 | -11.383 | -45.0543 | 2025-10-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 23bc584d-7a22-3d36-9a79-ab1add7df1d4 | -16.2366 | -50.9306 | 2025-10-01 01:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 196.8 |
| a6705c66-44d4-377b-b1ff-bed274f97885 | -9.9383 | -43.6483 | 2025-10-01 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| c1f306e8-99bc-37fa-a8b5-4cdf845ff8f6 | -20.6309 | -46.2046 | 2025-10-01 01:40:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 8a9a4da5-4507-3549-8c6e-1e7e1b43205c | -10.8433 | -45.3815 | 2025-10-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d40956f8-66fe-3cc4-a68b-14440b3f0244 | -16.2567 | -50.9057 | 2025-10-01 01:40:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 46fbbfcb-69f4-3ac8-beed-ad2fa11feeae | -18.71 | -49.1621 | 2025-10-01 01:40:00 | GOES-19 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 968f37a5-521c-3573-83fa-e4de7d95d0ab | -14.9914 | -46.9549 | 2025-10-01 01:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2f0250de-5f02-3239-8cf4-5e499c5e7ba7 | -14.8026 | -45.7713 | 2025-10-01 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 1e531c95-4a3e-3f86-b57f-3040a7b9d8aa | -5.3195 | -43.7405 | 2025-10-01 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 5c63f9e4-253c-3aa1-83a3-ce29337d94e1 | -14.7831 | -45.7749 | 2025-10-01 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| ec28371a-1d59-3e3d-8bdf-cfbc906f939d | -11.478 | -45.0868 | 2025-10-01 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 39042374-ff25-3ce4-966a-78ccf393740f | -3.1013 | -47.0082 | 2025-10-01 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 157.9 |
| fa6550db-a7e6-3de1-a627-faeeb0183cae | -11.4588 | -45.0895 | 2025-10-01 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 49d3b93c-99c2-3c16-b300-79038289c428 | -10.862 | -45.4019 | 2025-10-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 3b864c49-bd35-3f7b-96ab-093d8c63a16b | -9.4394 | -54.5739 | 2025-10-01 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 65235c05-3c0f-340c-b283-7bd1b6cb6d04 | -10.8429 | -45.4044 | 2025-10-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 223.3 |
| d6cf53c2-2e90-353b-8174-380efbb2958c | -13.3467 | -47.8508 | 2025-10-01 01:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b96f82f5-c8bf-3fc4-bff3-32e185847a03 | -15.9431 | -48.1245 | 2025-10-01 01:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 9fa599f5-a67e-3cc5-a295-32450f676403 | -13.3274 | -47.8536 | 2025-10-01 01:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| eb02864f-9406-32af-b735-dc73018492b7 | -7.8155 | -47.0667 | 2025-10-01 01:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 752da442-8963-373a-b011-8b133d110fbb | -9.2902 | -54.5242 | 2025-10-01 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 26f5a973-d360-3159-a5d7-5549a1a4f696 | -5.3382 | -43.7391 | 2025-10-01 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| cabf1438-11bf-3b27-a708-5ef19ce9201f | -10.9773 | -46.5217 | 2025-10-01 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 03a1120a-d367-3d1e-9b9a-420a2270ff08 | -13.2973 | -50.6605 | 2025-10-01 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 809b5a11-81c0-3d1a-94ce-5cda59cacf71 | -15.1806 | -49.1011 | 2025-10-01 01:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a5818f81-ecd7-38b4-9c32-40748a2fe54d | -5.8657 | -43.3981 | 2025-10-01 01:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 61308f09-bfb3-31c4-bda4-3d40b8c49557 | -14.7826 | -45.7981 | 2025-10-01 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 9c92857a-9084-3a7a-9402-d074eaa0aa46 | -10.1084 | -50.299 | 2025-10-01 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| fd3be419-bc7c-346b-a856-e3c2f2fc059d | -10.9384 | -46.5717 | 2025-10-01 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 83cb9ddc-6864-37f3-a4b2-1e1c8cbddb34 | -3.4577 | -50.089 | 2025-10-01 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| c9715417-92a5-31f0-91ee-97236bf4992f | -6.153 | -44.736 | 2025-10-01 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 44dac61c-a542-3c78-989e-6799fafe4c64 | -3.1013 | -47.0082 | 2025-10-01 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 192.7 |
| 41f26464-af37-3ff2-90bc-c44b97c6ad41 | -16.2562 | -50.9275 | 2025-10-01 01:50:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 0e39b2ec-e0a1-329d-a1b9-906fe0b7c56b | -11.478 | -45.0868 | 2025-10-01 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 816c136c-5058-3f36-9a4a-2e2e08316aa5 | -16.2567 | -50.9057 | 2025-10-01 01:50:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e0565b29-fff9-3449-b962-a799f98aebb8 | -18.7094 | -49.1848 | 2025-10-01 01:50:00 | GOES-19 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 28dbde08-7123-344f-bf21-c62bd14f7e7d | -6.1342 | -44.7375 | 2025-10-01 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 2bc6ba56-ebfe-335a-a49e-f6b3a2f84658 | -16.2366 | -50.9306 | 2025-10-01 01:50:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 2e28af19-0da4-341e-9139-7d2f7088daad | -14.7831 | -45.7749 | 2025-10-01 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 228.3 |
| 9c4ce625-294a-32d4-b88c-6bf797fe9fcf | -14.9909 | -46.9777 | 2025-10-01 01:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| fc4d3b1a-5304-3b7e-86ed-bd5ef6e2fbdf | -15.9431 | -48.1245 | 2025-10-01 01:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 50.3 |
| e493b443-2868-3109-93fa-b7bd9ee742b6 | -14.8021 | -45.7946 | 2025-10-01 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e55babf6-ee3a-3208-a15b-d3f2faab9e15 | -7.8155 | -47.0667 | 2025-10-01 01:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 01356f2d-bf92-39d0-9a0a-73a2b3551636 | -5.6361 | -43.9258 | 2025-10-01 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 73f743c7-ccea-369b-a9d1-b446fd4c6fb7 | -16.2558 | -50.9494 | 2025-10-01 01:50:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 82230a2f-2164-384f-ad65-3d2c9ef03a73 | -18.71 | -49.1621 | 2025-10-01 01:50:00 | GOES-19 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 96d900bf-2ee7-319e-aee4-4fb9ccab58a1 | -3.0827 | -47.0088 | 2025-10-01 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c11f2ff4-64a7-3b18-af94-bf3fb8bf7f5c | -10.1081 | -50.3203 | 2025-10-01 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 13befeed-e33e-3b16-bd73-0bec0f0d7e1a | -7.8343 | -47.065 | 2025-10-01 01:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 0627a474-8e10-3589-aa39-92bd825f5a87 | -6.5631 | -51.1126 | 2025-10-01 01:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |


[Clique aqui para ver as próximas entradas](README9.md)
