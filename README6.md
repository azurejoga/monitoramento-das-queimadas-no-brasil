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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3bc11ba-c57d-3221-bb7b-c99b30810f9d | -21.0131 | -50.0217 | 2025-08-11 02:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.2 |
| 9fa019af-1a67-36f5-aebe-af78954958a5 | -8.9401 | -60.7288 | 2025-08-11 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7dc45231-e8c0-3140-a500-0d12213c7c95 | -8.579 | -54.696 | 2025-08-11 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e04a715e-4639-304d-bd8a-6f30c2dc7287 | -8.9399 | -60.7481 | 2025-08-11 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a721fd0c-01fb-3982-8f72-8c1a1b887ce8 | -18.6293 | -46.8394 | 2025-08-11 02:10:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 6f0b8b5b-58d9-348f-a0a5-f5011b7e6789 | -7.0614 | -59.1972 | 2025-08-11 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| a1a749de-fa73-3ed7-a831-6a641c5f10f9 | -7.0797 | -59.2157 | 2025-08-11 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 79b31353-67bc-374c-9d9f-4b8dac2beb07 | -8.9215 | -60.7297 | 2025-08-11 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| f8cef84d-56e8-30a0-9d62-8d915c6519eb | -6.5668 | -44.5655 | 2025-08-11 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c3ea9d8d-12fd-3f05-a841-674f15d6df7d | -21.0336 | -50.0172 | 2025-08-11 02:10:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| f6885c1d-583a-3a0d-bd67-b618630dd2ed | -7.0799 | -59.1964 | 2025-08-11 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 2ce1253c-de4d-32a7-9313-1e95c6b94c07 | -8.9213 | -60.7489 | 2025-08-11 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 8361e507-5bbe-3e4f-90c6-8fb7032b1568 | -7.0613 | -59.2165 | 2025-08-11 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| fcaefadc-4852-339b-9c04-72069867b6fd | -6.5856 | -44.564 | 2025-08-11 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| bb35bda8-d9e1-356a-80b7-5aba9343c52b | -8.5604 | -54.6973 | 2025-08-11 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c8ba94bb-64d0-3df4-99aa-2854c8451221 | -7.0797 | -59.2157 | 2025-08-11 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7886ecc9-5479-3c50-bae0-fea9944367f4 | -7.4564 | -43.9554 | 2025-08-11 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 74764911-d38a-362f-8192-e41fd55c9b74 | -7.0799 | -59.1964 | 2025-08-11 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 3554a2d0-0eec-3ee6-8178-55f7bc8952a9 | -8.9401 | -60.7288 | 2025-08-11 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 838749b0-a3f4-32f4-a976-98c7a3b3d7bc | -8.9213 | -60.7489 | 2025-08-11 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 9686086c-2d0a-304b-bf99-b05b7b0651e8 | -7.0613 | -59.2165 | 2025-08-11 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 73dd5dd4-1fa2-3587-beb5-c124fd85d863 | -18.6293 | -46.8394 | 2025-08-11 02:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b34daf7f-0563-36cb-97b9-def382d8361f | -7.0614 | -59.1972 | 2025-08-11 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| e39ce1bb-df45-3803-8c17-b1ca69217e3b | -6.5856 | -44.564 | 2025-08-11 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| a0e16ba3-e05e-32b8-bbdc-6a37372e65d4 | -7.475 | -43.9768 | 2025-08-11 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| c6185a1f-ffe5-3593-823f-4edfc5f71182 | -8.9215 | -60.7297 | 2025-08-11 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 65e878b7-b2d6-3551-a29a-68f9fc52872d | -7.4755 | -43.9304 | 2025-08-11 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 62d1476e-a5a4-3d62-b475-486e9595fc36 | -9.3806 | -61.5315 | 2025-08-11 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 441ae58f-bbc2-30f7-b496-82bd5e7e3d61 | -8.9399 | -60.7481 | 2025-08-11 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 59b076b3-5e33-3588-a552-96109ba251f4 | -7.4561 | -43.9786 | 2025-08-11 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 826e2e8b-9a5d-38c8-9ab7-4eae24b11939 | -7.4752 | -43.9536 | 2025-08-11 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 168.1 |
| ccbba9bd-5dad-3f1f-ba12-0adff525bac7 | -8.5604 | -54.6973 | 2025-08-11 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9aa754e1-ed29-373a-8161-68d5f1fddad8 | -8.579 | -54.696 | 2025-08-11 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f5d6b654-b9e1-35e8-bc99-b0fafe1c931d | -8.9213 | -60.7489 | 2025-08-11 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 28a606b7-61ba-3a64-a702-401f83c84314 | -8.5604 | -54.6973 | 2025-08-11 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1b115685-af39-3c1b-9bd1-988acc2dbe71 | -7.4564 | -43.9554 | 2025-08-11 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 37413488-d5a5-3f72-9dbc-1ad27662e8e7 | -7.4752 | -43.9536 | 2025-08-11 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 6e75180a-e328-3a6a-8abd-06c81f4e597e | -6.5856 | -44.564 | 2025-08-11 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 2a6c22bc-3600-3ee5-b6d9-c7a142a1a18e | -6.5858 | -44.541 | 2025-08-11 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e286c345-236f-3b96-876e-d70a41f9992e | -8.9399 | -60.7481 | 2025-08-11 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 95da5084-ceaf-36bf-bea5-13f038242669 | -8.9401 | -60.7288 | 2025-08-11 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 0fa4e053-9680-346b-9e61-8466ab2bbc84 | -7.0613 | -59.2165 | 2025-08-11 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2feffc7e-0894-3c23-b9a1-fac90d3d9215 | -6.5668 | -44.5655 | 2025-08-11 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| d0fd9d21-f3e3-3292-b5ad-acd05e1d8a5c | -7.0614 | -59.1972 | 2025-08-11 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| f2a2f42b-eab2-3aa5-bfbf-9bb7ca9973c2 | -9.3806 | -61.5315 | 2025-08-11 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| efa8d34d-fa74-3b83-b30e-baf77ec74665 | -18.6293 | -46.8394 | 2025-08-11 02:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 1ce8e94f-6b61-3d96-9a1f-fe7ec9ae890e | -7.4561 | -43.9786 | 2025-08-11 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| afd81649-a419-3d14-8300-23960c1c07a6 | -7.0799 | -59.1964 | 2025-08-11 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.6 |
| d31c1a43-4380-3b02-9f31-23a31aeb3624 | -7.0797 | -59.2157 | 2025-08-11 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| afc2ee96-75c3-35c6-ae8c-537232eaa71f | -8.9401 | -60.7288 | 2025-08-11 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| dc2d215d-a93d-3e41-999c-19cd6f9dbb77 | -7.0613 | -59.2165 | 2025-08-11 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 3e708f68-7f1f-32e7-829b-fbc9fe8c0606 | -6.5856 | -44.564 | 2025-08-11 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 0a433e1f-a666-3f60-874b-b58f60ab56cf | -8.5604 | -54.6973 | 2025-08-11 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a72adda2-8d0e-365c-8241-579e6dfeae54 | -7.4752 | -43.9536 | 2025-08-11 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 1460b43e-cbfe-3dc8-8fc4-68d26dd6865f | -8.9399 | -60.7481 | 2025-08-11 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1da778a9-9402-3920-bda8-434e6d69a12f | -7.0614 | -59.1972 | 2025-08-11 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 0f40bc0b-06d8-311b-a2f1-6606f8ccd3b1 | -7.0799 | -59.1964 | 2025-08-11 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| cfbafb81-5a3d-36b8-90d8-43b285f5db9d | -18.6293 | -46.8394 | 2025-08-11 02:40:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 64b9b94c-87b5-3a1b-bf85-d69a112a03a2 | -7.4564 | -43.9554 | 2025-08-11 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 0746da71-e0c6-3b8b-97db-3d62a9bea805 | -7.0797 | -59.2157 | 2025-08-11 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7e7f2acf-fab4-3264-912e-494d0af2e4cb | -9.3806 | -61.5315 | 2025-08-11 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 463dc1be-0131-307e-af6d-10ff8513df41 | -6.5668 | -44.5655 | 2025-08-11 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 4217cab1-bcaf-3ae0-af3e-c32509b95b8d | -7.0614 | -59.1972 | 2025-08-11 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| bfeacf51-cc86-3265-ad03-0328ae8e1911 | -18.6293 | -46.8394 | 2025-08-11 02:50:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 07c48d25-87f7-390c-99c2-c5cdf66dbb56 | -8.9215 | -60.7297 | 2025-08-11 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 836dec0e-b5b2-3a01-b7ac-c424013c899b | -5.4824 | -44.3969 | 2025-08-11 02:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| fe8c8ca3-07b0-38ad-a07b-f01ae51b9823 | -8.9399 | -60.7481 | 2025-08-11 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8018d741-d67f-3bf9-aac8-ab473dc4e2c8 | -8.9213 | -60.7489 | 2025-08-11 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d37d90a9-d51d-3906-8bdd-7c2a09e6c33c | -7.0613 | -59.2165 | 2025-08-11 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 8f1f1e4d-4057-32c1-befc-16efb7672548 | -7.0799 | -59.1964 | 2025-08-11 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 33079ec6-ae2b-3a48-94ab-cbc1dfb014d9 | -8.5604 | -54.6973 | 2025-08-11 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 94a2b9ff-3ebd-3074-b5f8-c58886f2e30d | -7.1706 | -44.2829 | 2025-08-11 02:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 6ab829af-eb8f-3826-92f4-551e5ebfa1c9 | -6.5856 | -44.564 | 2025-08-11 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 87f5a88c-5974-3ab9-8688-26c86a5fd065 | -9.3806 | -61.5315 | 2025-08-11 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 72da77fe-fce0-39e6-8bac-3a98f361e774 | -8.579 | -54.696 | 2025-08-11 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0ad4fb8c-ab64-3075-9c61-c8bacfa3b176 | -8.9399 | -60.7481 | 2025-08-11 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| a5a9ec77-24a7-3ee5-9fcb-a4335620675e | -7.0614 | -59.1972 | 2025-08-11 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1c73ecaf-d12a-320a-ac17-272c7ad279ec | -8.9401 | -60.7288 | 2025-08-11 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 526517f5-fb44-3e66-927e-c23fe40661be | -7.0613 | -59.2165 | 2025-08-11 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f7e9903f-d320-374a-8b43-a49ec747f41f | -5.4824 | -44.3969 | 2025-08-11 03:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 441b91cb-e4d4-3924-a8a6-17b9c0d5a1b0 | -6.5856 | -44.564 | 2025-08-11 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| da00c7b7-c087-324d-891f-3d12e3492478 | -8.9213 | -60.7489 | 2025-08-11 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 593c4824-9968-3e91-b196-6f20f7c3fdbd | -7.0799 | -59.1964 | 2025-08-11 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b3847438-b6e5-3ac2-9c0e-efcf199b2821 | -9.3806 | -61.5315 | 2025-08-11 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| a98365c2-8799-3e90-aa72-0ef1732bcf91 | -7.6113 | -45.2026 | 2025-08-11 03:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 48152256-682d-3b7b-a455-ab966fa1fe90 | -15.4407 | -53.9258 | 2025-08-11 03:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 4804c76e-89ab-3a8c-8a22-18f3995f07e6 | -7.0799 | -59.1964 | 2025-08-11 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| ec2d983d-04b1-3406-a5b1-9425f457d5dc | -8.9401 | -60.7288 | 2025-08-11 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5c5a9f6a-3c89-32e9-942d-86032150b32b | -7.6115 | -45.1799 | 2025-08-11 03:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 68e57360-e720-393d-a318-73907f925b0f | -7.0797 | -59.2157 | 2025-08-11 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 8d6952ad-3165-33a8-a0de-9a69df1f63f9 | -7.0614 | -59.1972 | 2025-08-11 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| da775743-649d-39ba-8966-9a135efa9214 | -6.5856 | -44.564 | 2025-08-11 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| ac31428c-6aca-34ef-86c2-11bbdc303796 | -8.9399 | -60.7481 | 2025-08-11 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| dc0c8685-1ac2-3d4e-9ffb-dddee4509d6f | -5.5011 | -44.3956 | 2025-08-11 03:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 927572cf-3367-3f4d-b7bb-f9a2b76d852b | -5.4824 | -44.3969 | 2025-08-11 03:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ddf32c3d-a64d-3531-998e-2c1db9acacf8 | -7.0613 | -59.2165 | 2025-08-11 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 206b6028-ece6-3d4a-a1f3-cc2862c094e3 | -8.5604 | -54.6973 | 2025-08-11 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 72414a18-9629-3c89-9d10-8d0777727e23 | -7.6115 | -45.1799 | 2025-08-11 03:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 8e090960-e099-3d57-811f-9b2e4582e798 | -15.4407 | -53.9258 | 2025-08-11 03:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| c94a6ac1-bb9d-387e-ad03-4cd31cfc97ca | -5.4824 | -44.3969 | 2025-08-11 03:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 195.5 |


[Clique aqui para ver as próximas entradas](README7.md)
