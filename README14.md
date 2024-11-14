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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d315670f-940b-3eee-959b-46effe0ed720 | -17.5869 | -57.5533 | 2024-11-14 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 173.8 |
| bdc0d9c7-6997-3d9f-b962-365668ecc6ae | -3.6402 | -50.5863 | 2024-11-14 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 1fe8db79-21a3-3c3b-bd72-379d54d39b36 | -1.2228 | -51.783 | 2024-11-14 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8ee25bb1-7d28-3e38-91f8-b88d5babcf4a | -2.1953 | -46.3528 | 2024-11-14 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| da8320d8-3351-3731-a341-4ac2be338ed1 | -17.5675 | -57.5351 | 2024-11-14 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 284ce643-0e4a-33c1-bf95-21aedf7064b6 | -3.0522 | -45.5461 | 2024-11-14 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 00de9916-cdb9-3e23-bf77-700c25403bd1 | -1.7922 | -52.1655 | 2024-11-14 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 168.7 |
| 6db28899-46c9-3283-a513-530822019c44 | -2.6564 | -47.0008 | 2024-11-14 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 1cd0aaa0-8112-3df4-9c0f-83b43f9d7d42 | -17.5872 | -57.5328 | 2024-11-14 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| e139ef8f-e891-3c02-b2c2-6af837882291 | -2.675 | -47.0003 | 2024-11-14 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 210.0 |
| 7e5b9956-2be4-3410-b017-95e987d471b4 | -3.3358 | -52.805 | 2024-11-14 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| cba10673-912e-3e2d-ad72-b1cc369e945b | 2.6703 | -61.169 | 2024-11-14 01:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| bb38a153-9f12-3338-9e68-d7757ee866e7 | 1.0674 | -59.2467 | 2024-11-14 01:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 42c6468a-1b26-3b05-bc37-6ad53baec0e6 | -3.0709 | -45.523 | 2024-11-14 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 102.6 |
| a0b4628e-face-3671-b2b3-acbd6a43896e | -3.2533 | -50.3899 | 2024-11-14 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 40209858-3d30-3e2f-a92e-b02c4b24e761 | -3.0504 | -50.3332 | 2024-11-14 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 8d07308a-2333-355a-80f5-76adcf920598 | -3.6587 | -50.5857 | 2024-11-14 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 28cf3670-4a0f-387e-89d6-00253a53ccf1 | -4.0003 | -45.5728 | 2024-11-14 01:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 98.9 |
| fa6dd52f-c876-3e63-8a50-37b917779ac0 | -6.0472 | -44.0331 | 2024-11-14 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 65608bfe-bb1a-335a-96cb-819f0cfa6826 | -17.6066 | -57.551 | 2024-11-14 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 4d235ff9-2d98-3b49-ad3f-4ae3d52ea909 | -2.6565 | -46.9789 | 2024-11-14 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 0d8f686d-39dd-35a9-b600-36a9fade9130 | -4.0867 | -50.0021 | 2024-11-14 01:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d3b76a0f-787b-39f7-b270-fcb98b3bcc0c | -3.3359 | -52.7847 | 2024-11-14 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 8b857a25-a507-3d3d-9c39-bc57d61a0e7a | -3.6401 | -50.6073 | 2024-11-14 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 0aa26d32-34ba-3496-b6e0-394d2c99573f | -4.0682 | -50.0029 | 2024-11-14 01:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 433fce18-8ad7-3a01-966e-cca67142e77b | 2.6703 | -61.1879 | 2024-11-14 01:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ace9ca61-f2b4-300d-94b5-ce5bf29192ad | -4.0005 | -45.5503 | 2024-11-14 01:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5b627a9c-8fdb-390a-9d51-5ebcbb3c773f | -21.828501 | -56.4711 | 2024-11-14 01:28:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f54cfa49-1678-3cf1-a71e-fc274b099b94 | -17.5278 | -57.488998 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e89e31c1-303a-3769-850e-e50ebd151606 | -17.516399 | -57.5751 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e53c7e20-1cd7-3d07-8462-d18b77c6bffc | -19.502899 | -54.903599 | 2024-11-14 01:28:00 | METOP-C | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 27ab0ae8-96a0-31dd-84c3-0092a054ef93 | -17.174101 | -57.476002 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 248ef77a-0005-3ef6-b5dc-c5508192611d | 1.379 | -60.444099 | 2024-11-14 01:28:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f865e0d7-7954-3052-a493-0d6c92a0ba8b | 1.3692 | -60.441898 | 2024-11-14 01:28:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a1671e58-7ac3-3387-8f00-19d16c35c59d | -1.7191 | -52.195499 | 2024-11-14 01:28:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56f52983-da75-30db-92b2-01e622916a32 | -17.504999 | -57.570301 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2f3c310-d234-343b-afb9-15ba353986b9 | -17.190399 | -57.502499 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8a883ce-7aab-386f-bc7b-7a875d087eaa | -3.2584 | -52.8116 | 2024-11-14 01:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1d8c782-475d-322c-8e60-51cd65016a75 | -3.6376 | -50.6292 | 2024-11-14 01:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9d7f4ef-6f51-3cb4-9d92-7491e8db673e | -1.5947 | -52.574799 | 2024-11-14 01:28:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10ccba6b-963c-328a-95b9-ee4359a46acd | -15.1992 | -60.225498 | 2024-11-14 01:28:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a815d01-06bc-35a7-b19f-e13a19e4b252 | -17.5131 | -57.560699 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c271f053-ad64-3090-8ff9-efc1f107f616 | -21.4785 | -55.834999 | 2024-11-14 01:28:00 | METOP-C | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a8d5c763-9fb1-371a-9f73-2d927628fe0d | -17.636999 | -57.5611 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88d830ef-7d04-3674-a878-4402496e730f | -17.516399 | -57.4842 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 678fac5b-858f-36d8-b5a3-f686888e9064 | -17.5555 | -57.565601 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95ac7442-9fef-3911-82be-f6457cf69a5b | -17.518 | -57.491402 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2152d5d-8edb-340e-b3dc-1e46dc9447ff | -17.519699 | -57.4986 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4ed61f4-20c5-33d3-8ce4-64b7723144f3 | -17.211399 | -57.322399 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2d6e917-7d52-337d-8082-ffb0c7483c7a | -17.164301 | -57.478401 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e3a498d-a6c3-3982-ab8f-e2c67d53731f | -17.496901 | -57.534401 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 757c1416-6cb8-3dcf-a8a4-3ade6396e579 | -17.514799 | -57.567902 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7cef0d4d-3616-367d-8a9f-2e9607c25b86 | -17.625601 | -57.556198 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cc0bd25f-325a-3a05-b44b-fd00bf58660e | -15.1518 | -60.243999 | 2024-11-14 01:28:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f592269b-9e9f-3d9f-8bf3-1633d26790b7 | -17.511499 | -57.5536 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9532b6f-da48-35a7-987b-5345c7e39c8f | -17.162701 | -57.471199 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 90e8f534-ba81-37b9-ab83-b85500dd9559 | -17.521299 | -57.505699 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 604b51b3-e74e-3b78-95f4-e2043b4a9e3f | -17.5116 | -57.507999 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1dc51a4c-a9b1-36b0-8c07-6d5846b1c4a0 | -17.524599 | -57.565498 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f377a191-5488-3b1a-80d9-f58dee9be3d4 | -3.6473 | -50.6269 | 2024-11-14 01:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf3dbce2-c67b-3afd-9308-c4f22aad581a | -1.7236 | -52.171799 | 2024-11-14 01:28:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a170a015-1c93-3073-9462-4259ac2f8ac9 | -17.5539 | -57.558498 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f090f5ad-7af4-3057-ac41-d9f2a1c7fcd4 | -16.025101 | -60.1003 | 2024-11-14 01:28:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3fae039-dd89-34e5-ae56-0a0d22b39202 | -17.635401 | -57.553902 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 466805ac-bf7d-38a8-a618-07c99e47ad9e | -17.179001 | -57.497601 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f5e569c-c01a-363b-9c61-1000262b2ee9 | -17.503401 | -57.563099 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 65f63f6c-75e9-379f-94a1-85c252d68ec3 | -17.552299 | -57.5513 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 372967aa-0467-3e24-b89e-c92b3f4a9349 | -21.7731 | -56.4538 | 2024-11-14 01:28:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3b94cd49-43c9-357b-aa91-d06042bf4b6a | -17.513201 | -57.515202 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0012a017-289d-3c01-bf93-7478fc5db9f1 | 1.1344 | -60.611801 | 2024-11-14 01:28:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d6418206-5dc0-3896-9dda-74336c30d01c | -17.488701 | -57.543999 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2d4a4ae-edc8-3ad7-bf0a-c79cdc1bab57 | -17.514799 | -57.477001 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 741b2af2-c59d-37f2-be70-d851daff0b2f | -17.508301 | -57.4482 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 190e45f6-654d-37d3-b8e9-e0b6a73e3482 | -17.498501 | -57.541599 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eeafe727-2915-380a-a910-418224308378 | -17.624001 | -57.549099 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0fdae96-3c7b-338f-869c-fe9b79e301b9 | -17.487101 | -57.5368 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea5e8413-0a36-3260-be30-577be1a74c0f | -17.500099 | -57.548801 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd9a4694-cb24-34a9-98b1-f7f5293a9a0e | -17.166 | -57.4856 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b5ebb0e2-c716-30d9-960a-c461758665df | -21.8302 | -56.4785 | 2024-11-14 01:28:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 19559656-17be-38aa-9389-4d2cb85a5d8e | -17.633801 | -57.5467 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01ec0d30-559f-324f-b81f-7df06481b6f8 | -17.5441 | -57.560799 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f4970ee-8141-3a8a-a963-15f31fb4e66d | -17.615801 | -57.558601 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89917d41-b86a-3f14-a8f1-6ab938bb1092 | -17.5229 | -57.5583 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24eb0785-ddfe-378e-af50-67bab34cfa4e | 1.3773 | -60.451401 | 2024-11-14 01:28:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ce5fbed1-9fdb-3c3a-84d7-809ca57e9e28 | -17.614201 | -57.551399 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c663a083-3bc2-359a-9b19-d4460883c61f | 1.3675 | -60.4492 | 2024-11-14 01:28:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9376245e-9751-3a2a-8a7b-e6e208873b37 | -15.1502 | -60.236599 | 2024-11-14 01:28:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 482e2a6e-c5cb-34ae-8b01-2553d7ea6e28 | -19.500999 | -54.895401 | 2024-11-14 01:28:00 | METOP-C | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ddc3c4da-63dd-3aca-b049-954dbe6500df | -3.6313 | -50.603699 | 2024-11-14 01:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d90c944d-cb69-39a1-96da-63b1be3347a3 | -17.526199 | -57.4818 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12b01453-512a-3673-8a7f-2b011aab0f12 | -17.529499 | -57.496201 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9fca582b-6e43-3b7b-9902-53ae2e4d10a7 | -17.175699 | -57.4832 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47562285-56b7-368f-b193-d9644b98d902 | -17.511499 | -57.417 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7e096b3-4f83-3847-b58e-9554b7d1beb5 | -1.714 | -52.174099 | 2024-11-14 01:28:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e0abe72-6f2d-3792-8c87-54074c4072fe | -17.1887 | -57.4953 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f341962f-3774-3667-bc82-ae17b7b57850 | -17.5327 | -57.556 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f7d786d2-3bec-3b65-b56d-a0f36fec4bc8 | -17.513201 | -57.424198 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73d0ab05-1f64-3e75-bd19-055cf1226ab0 | -1.585 | -52.577099 | 2024-11-14 01:28:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc253ea5-500f-3140-b76d-a71ac3afb004 | -17.177299 | -57.490398 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f1d42aa8-2f41-3d7f-8463-09413714fa04 | -16.026699 | -60.1078 | 2024-11-14 01:28:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
