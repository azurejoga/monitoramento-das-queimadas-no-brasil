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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce5954c6-1083-395c-a4a6-11dcbaaa67b8 | -4.2832 | -59.6554 | 2025-10-30 04:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 4fdc9995-b3a2-3d9a-af38-6ab55f94b940 | -5.4372 | -45.3323 | 2025-10-30 04:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 0bda6a11-7c62-30ef-86e8-006bddfbbe5c | -8.3313 | -47.9219 | 2025-10-30 04:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6a2fb6fa-7989-3499-8637-5ed7bd15293a | -4.2545 | -43.6918 | 2025-10-30 04:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 7cf95910-7ef7-3c28-93ed-3f825b380b6b | -4.2544 | -43.7149 | 2025-10-30 04:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 289.3 |
| eb2c9c88-89e4-31a8-8862-1689714576f3 | -3.7867 | -43.9011 | 2025-10-30 04:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 6a3037e6-da70-3cd9-862c-99220c68e1fe | -3.8054 | -43.9002 | 2025-10-30 04:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| fdbccea4-2121-3c2b-9788-1300f90bb2e6 | -12.5141 | -50.566 | 2025-10-30 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c90498b2-0047-373a-9fff-18ba44a7348b | -8.3313 | -47.9219 | 2025-10-30 04:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e2308a9a-d9cc-39db-9410-a01da1c480c5 | -4.2545 | -43.6918 | 2025-10-30 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 39cfd44a-fb74-3ea9-82df-9627f9a16368 | -12.4953 | -50.5469 | 2025-10-30 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e60eeaa0-d9dd-3337-90d8-6bedd46a4d13 | -4.2731 | -43.7139 | 2025-10-30 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 4cc409f8-0a7d-34bc-8d9d-b68ae52117b8 | -3.7867 | -43.9011 | 2025-10-30 04:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 5da7fe5a-ca21-378c-95fd-d95d9cadfcfe | -12.5141 | -50.566 | 2025-10-30 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9be8bdc5-71e6-3896-ac74-bb4d5ea811a9 | -12.4759 | -50.5707 | 2025-10-30 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| eb57e04d-bc6d-3e52-ba47-e6b7ea30776b | -4.2544 | -43.7149 | 2025-10-30 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 233.4 |
| fe40134d-ee07-3ca4-a285-353425c8783b | -3.8054 | -43.9002 | 2025-10-30 04:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 6d03ca0f-f264-3047-8b6b-359ef52ae0c1 | -12.495 | -50.5684 | 2025-10-30 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 316450e0-4ed3-38be-9763-a8f724bfc05b | -4.2732 | -43.6908 | 2025-10-30 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| e000a006-8dc8-3833-b710-73ced09dfc7d | -5.4372 | -45.3323 | 2025-10-30 04:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 4e010f8f-3200-3deb-8b21-860ead490470 | -5.4372 | -45.3323 | 2025-10-30 04:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 2b3f7d5d-4956-35fa-995d-610d1906b728 | -12.4755 | -50.5922 | 2025-10-30 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 7b55419c-41e1-3495-9349-c9c73498309f | -3.7867 | -43.9011 | 2025-10-30 04:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| bd74e17b-64ac-30ea-b3d7-807a6dfee859 | -8.3313 | -47.9219 | 2025-10-30 04:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 33fa1a72-2eef-3e3b-9422-dbf4fa354e74 | -3.8054 | -43.9002 | 2025-10-30 04:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| afe495a5-6d60-33c0-9a6a-12440ed87ab3 | -12.4759 | -50.5707 | 2025-10-30 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 72a1472f-1328-33c4-bf7a-de6ead76e548 | -4.2544 | -43.7149 | 2025-10-30 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 9d1434af-807e-36a3-bcd2-98b560543a5a | -9.8238 | -47.5736 | 2025-10-30 04:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9046611a-99d1-3722-848d-e0dacf0f5eb3 | -12.5141 | -50.566 | 2025-10-30 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| deb401cf-7ad5-3cf5-8cbb-c37a8ee3fdc5 | -4.2731 | -43.7139 | 2025-10-30 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| bef832f0-ee53-32f9-9309-e7c45715f181 | -12.495 | -50.5684 | 2025-10-30 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 9a7c73e4-65e0-3063-a631-7cccda58e49c | -4.2545 | -43.6918 | 2025-10-30 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 3aec9273-63f6-39ae-ac89-82403f236be3 | -4.2545 | -43.6918 | 2025-10-30 05:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 44ea7d2a-b191-3b1d-abdc-fdc07f4ebae8 | -4.2731 | -43.7139 | 2025-10-30 05:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5703ffd0-1d89-350b-9f1e-8799cc1249ba | -3.8054 | -43.9002 | 2025-10-30 05:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| d8900040-5571-385a-b576-3373da5cd0aa | -8.3313 | -47.9219 | 2025-10-30 05:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7daa057b-ccb6-349c-b83b-d7862205df3e | -12.4759 | -50.5707 | 2025-10-30 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 91371d37-a1c8-332a-ba4d-1436ce9ca7f1 | -12.4762 | -50.5492 | 2025-10-30 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4202da75-19ce-3030-aded-930e6a232b87 | -12.4953 | -50.5469 | 2025-10-30 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 17e1449d-8a74-347f-8d24-c483d7c93349 | -12.5141 | -50.566 | 2025-10-30 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| fa4a61e9-bc5e-35a1-ac67-c27caca19ba3 | -4.2544 | -43.7149 | 2025-10-30 05:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 192.5 |
| c3aafff5-7ffc-3d67-b8ca-04d03971d590 | -12.495 | -50.5684 | 2025-10-30 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| dcc1259b-7712-311a-9a96-95d0d045639f | -3.7867 | -43.9011 | 2025-10-30 05:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f51ed82c-9e1d-3449-98f5-54533daed590 | -5.4372 | -45.3323 | 2025-10-30 05:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c8212b49-1b46-3b78-af9f-08cb5ba3c221 | -9.8238 | -47.5736 | 2025-10-30 05:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 6500d101-8d83-3377-9d6c-b8bf727c18ec | -4.2731 | -43.7139 | 2025-10-30 05:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 645e89fb-8e96-3102-8387-66bfb5143aa5 | -12.4953 | -50.5469 | 2025-10-30 05:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a3c687ad-e47f-330f-bc0c-8c292a8de779 | -12.5141 | -50.566 | 2025-10-30 05:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| d78a6c77-448c-3e26-b52f-94c0d136a9d8 | -12.495 | -50.5684 | 2025-10-30 05:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| f2244212-094a-3623-9c5f-e74eef7a97c3 | -4.2544 | -43.7149 | 2025-10-30 05:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| b863b8d8-a909-31fe-8da1-53e3b986a267 | -12.4759 | -50.5707 | 2025-10-30 05:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9e1c56a1-3d1c-33f9-a66c-b1ddc32939ec | -12.5145 | -50.5445 | 2025-10-30 05:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 32153d58-ad7c-31de-b606-31e94bf774e0 | -3.7867 | -43.9011 | 2025-10-30 05:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 527bbd1a-1036-3f11-993b-20662c740194 | 0.44593 | -60.47507 | 2025-10-30 05:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 17806af9-8a8a-3157-a88c-9d3176fe0c3d | -1.7388 | -55.73468 | 2025-10-30 05:14:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 649fdc93-16ee-3761-b748-5a1dcc1a6f37 | 4.48834 | -60.72688 | 2025-10-30 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8583bcc5-8684-3903-a119-3e27b2a28ed0 | -1.6126 | -54.65567 | 2025-10-30 05:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 427897a7-8cfa-3d6f-b9c5-fa472889ce19 | -2.79278 | -50.28689 | 2025-10-30 05:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e2ec2a4-5388-38bf-92b9-e9fc37c8907a | -1.52109 | -55.96466 | 2025-10-30 05:14:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 909b288c-8e79-3e65-9e40-2b769bf24768 | -2.76956 | -45.39899 | 2025-10-30 05:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 66417d68-41e1-31bc-8247-d74f90e8bf20 | -1.10124 | -56.287 | 2025-10-30 05:14:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a277dec6-1adc-3eea-888c-ce580393f93a | 3.14287 | -60.69573 | 2025-10-30 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 748bac8d-13ff-36e6-9cf9-f8a728fa7fa3 | 3.62457 | -61.04466 | 2025-10-30 05:14:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb1b7d5a-2610-35a3-86cd-931aaf7ebdfe | 1.31268 | -60.40746 | 2025-10-30 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d54b1586-b0a1-33e2-bd54-af830d64a689 | -3.22904 | -46.88012 | 2025-10-30 05:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 630ae899-5d88-3217-8117-2ce7d75c84e4 | -2.76647 | -45.39314 | 2025-10-30 05:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2ca6f65a-70b7-3e04-93fc-861813b0a97e | -2.20041 | -51.36516 | 2025-10-30 05:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27b5d418-9ce3-3404-bfe5-bd9ef211c566 | -2.77309 | -45.39439 | 2025-10-30 05:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dcad80f0-3faf-384a-9a8f-2b3dc6f42d25 | 1.60541 | -55.68769 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 326d4d4a-5906-3dd6-a470-94f3cd75fbb5 | -1.63091 | -54.21608 | 2025-10-30 05:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 669125bf-ac15-37e5-add9-116f7d163dcb | 1.60876 | -55.68718 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5bff9e28-517c-3524-95bf-0c09befe721e | 2.34391 | -60.21461 | 2025-10-30 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d39a93a-a36b-3755-a712-aa4e97c873e3 | -1.53095 | -54.44607 | 2025-10-30 05:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a60ee5f-6f48-36bc-a547-daca8d94105a | -1.63458 | -54.21666 | 2025-10-30 05:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d729ec3-29ad-3f50-ab83-c2939de726d8 | 1.59285 | -55.68948 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0de4aa03-a2d0-3985-8bb6-ee1a48655013 | 0.44657 | -60.47923 | 2025-10-30 05:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ba8f6262-198e-33f7-ad44-c932807a6373 | 0.31986 | -51.09935 | 2025-10-30 05:14:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc7b56f9-a7a8-3fb0-8998-0f0268d1e985 | 0.68406 | -59.46218 | 2025-10-30 05:14:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 088ebe19-5662-36b8-9ff3-027a9f1ef4e5 | 3.1391 | -60.69635 | 2025-10-30 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaa6f074-1b2f-3409-a6c0-bce332a573cb | 3.14356 | -60.70037 | 2025-10-30 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd16d1f6-8939-342d-807b-f1c5d60943d2 | -3.22876 | -46.87938 | 2025-10-30 05:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 719eca54-7f6a-3f3a-b013-69b15f1a1ae2 | -2.57342 | -45.79588 | 2025-10-30 05:14:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0efadb92-925d-3102-9841-ecf2b6dfddee | 3.9009 | -60.08056 | 2025-10-30 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a25006b-f659-310b-acea-373ad466f716 | -3.22977 | -46.87506 | 2025-10-30 05:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 98ff6c05-61ff-3a6b-b61a-9b298ec15b41 | 2.08859 | -50.85939 | 2025-10-30 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 76fefb2a-f077-3c42-9e09-6e13d98d2761 | 1.61322 | -55.69373 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58d4b3a0-9d95-3a0d-9971-0dbadaa046e4 | 0.30449 | -56.87402 | 2025-10-30 05:14:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdd1ef83-7e12-37be-b81f-99f0657c9290 | -1.06165 | -57.40761 | 2025-10-30 05:14:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 990e4169-df85-3178-9504-4de2e62589c2 | 1.17203 | -51.26019 | 2025-10-30 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7215171-dd4a-38e3-9d60-438d8dfa1f8f | 0.83372 | -59.31666 | 2025-10-30 05:14:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d747741e-eb2c-33c7-8825-7bf0ab262892 | -0.13832 | -60.7686 | 2025-10-30 05:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b364e112-f434-3965-81a2-39bace16561a | 1.31631 | -60.40691 | 2025-10-30 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0ca3bde-e4c7-3c54-bdd9-73064c367d83 | -2.79762 | -50.28764 | 2025-10-30 05:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bb88cb5-ba0a-302d-a7e8-436e22416d7b | 2.07933 | -50.8567 | 2025-10-30 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81bc56ec-9f72-32f9-b426-505bf907fdc9 | -1.77334 | -55.73926 | 2025-10-30 05:14:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b401446-fd55-3ba6-b0a2-3b786fab2200 | 1.6774 | -55.64375 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4d59d0a-bce7-35b1-8f94-786366f04da4 | 1.78423 | -55.67404 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 497efd7c-6337-394e-be36-e84caa20c7a9 | 2.07568 | -50.8615 | 2025-10-30 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b36ee806-8c5b-3c6b-bef9-c89e9a8afeaf | 1.59954 | -55.68843 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2057f76b-a9c9-3406-808c-dd1d20e307ca | 1.78368 | -55.6705 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README62.md)
