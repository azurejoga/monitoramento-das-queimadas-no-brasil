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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fbb853f-1d6b-36bb-b746-47b531d16749 | -3.259 | -53.6388 | 2024-12-01 08:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a419d49c-bb02-3baa-aeb0-804cfdaa117c | -3.259 | -53.6388 | 2024-12-01 08:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9f5d3cf6-6a19-3ee5-95cf-676784eaebbf | -3.146 | -45.3629 | 2024-12-01 09:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 7b2d1736-125e-3100-a788-e2aab596b990 | -3.146 | -45.3629 | 2024-12-01 09:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.9 |
| b3a439f8-b265-3b0d-8233-bd1544700c6a | -2.4297 | -48.2895 | 2024-12-01 10:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| e46b2d15-5c2a-3ffe-a29d-074b13ca035d | -2.4297 | -48.2895 | 2024-12-01 10:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 69197e73-fa22-3f52-9890-fb0c3139caed | -2.4297 | -48.2895 | 2024-12-01 10:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 70f0e4ea-9945-38e1-8b76-e423c71d5c65 | 1.1439 | -55.9871 | 2024-12-01 11:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 98384610-9402-326c-86bd-9d6c194ca027 | -4.8897 | -41.3385 | 2024-12-01 11:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| f54287d8-22cd-33a3-afe8-13b55bf59e66 | -4.8897 | -41.3385 | 2024-12-01 11:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 939cb86f-ca83-3d92-85cb-4b541a7c2849 | -1.4586 | -53.6942 | 2024-12-01 12:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 72cfa9e7-6200-3d66-ba01-f64723faf9e8 | 1.1622 | -55.9672 | 2024-12-01 12:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 3751609f-9635-3325-bbab-52f1d277fd1f | -4.8897 | -41.3385 | 2024-12-01 12:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 148.5 |
| 0f86abaa-8e1b-3c98-8865-c119c8de7777 | -2.15483 | -46.6273 | 2024-12-01 12:55:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a7164551-234a-3a21-9551-277fa9b4f1fd | -3.19424 | -42.39121 | 2024-12-01 12:55:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ec2e8c5c-7456-3f74-8e95-f09cfc3c89ec | -2.12788 | -46.52923 | 2024-12-01 12:55:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 1ebae9c2-bc35-3de7-a152-851fa7d19784 | -1.3075 | -52.85648 | 2024-12-01 12:55:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6bd7ef6c-05a4-3623-8a22-f7bb22b9ef6f | -3.07222 | -53.80484 | 2024-12-01 12:55:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| bca000de-7df9-374e-8474-e70ecb13c585 | -4.55143 | -45.72165 | 2024-12-01 12:55:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 1e155dfa-aed2-3795-9f30-4529e034e7ba | -1.66649 | -53.77331 | 2024-12-01 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 3e904b78-cd9d-310e-a06c-401250b1bfc5 | -2.49237 | -47.2776 | 2024-12-01 12:55:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 1b89ebd4-e47b-3616-806a-8d31464d3b70 | -3.13529 | -54.53345 | 2024-12-01 12:55:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| ac570180-0dc7-3675-9188-6eaac055540d | -3.22248 | -54.17482 | 2024-12-01 12:55:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b556d07f-c073-36b3-bab2-fe2a8ec82acb | -3.13421 | -42.37639 | 2024-12-01 12:55:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 73c9a539-8f9a-3581-b07e-ddcec1e3c329 | -2.88664 | -42.05433 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| ca3b041a-76fe-3e4c-a910-a102cda1ac26 | -2.79295 | -49.2952 | 2024-12-01 12:55:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3a38b68a-b712-3414-978c-d8bb80b32759 | -4.55342 | -45.7072 | 2024-12-01 12:55:00 | TERRA_M-T | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ffe7a8aa-d5b7-3f37-817b-94c9a7473d4c | -4.03562 | -46.93202 | 2024-12-01 12:55:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 0ba01b43-62ec-3c26-b94e-a1361af8ffd2 | -2.93151 | -54.12705 | 2024-12-01 12:55:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 445e3e23-3aef-3e29-8493-c2635559b131 | -1.4775 | -55.3809 | 2024-12-01 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| cf5e2709-df16-369b-a5a2-058c8ada5fb8 | -2.90605 | -42.14465 | 2024-12-01 12:55:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| c17b4797-6d65-35e3-826c-ebbd16b67811 | -1.4388 | -47.35051 | 2024-12-01 12:55:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 38ca2b10-b885-3f06-b387-1b7034a6a873 | -4.87629 | -41.34291 | 2024-12-01 12:55:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 7c81e01e-74c5-3acf-9285-80346b3f6eee | -2.63954 | -48.63453 | 2024-12-01 12:55:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0452e045-aa56-3a1d-b1c2-7cab83499919 | -1.50253 | -52.64777 | 2024-12-01 12:55:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 76a6efd5-27cb-3884-9d36-e5cddcf28610 | -1.4428 | -52.76795 | 2024-12-01 12:55:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ce3dc7a8-ed07-33d9-bb62-4413a225a9fc | -1.52568 | -47.15155 | 2024-12-01 12:55:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 690938c1-8d31-3bbb-972f-9f43d638149e | -2.11784 | -50.33578 | 2024-12-01 12:55:00 | TERRA_M-T | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c073c573-d37a-3f26-a75b-68d981be8b1b | 1.1847 | -50.89609 | 2024-12-01 12:55:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 5fbdc25c-17db-3c58-928c-22b3ba3e59b7 | -1.56773 | -48.64435 | 2024-12-01 12:55:00 | TERRA_M-T | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| e9a876aa-a3fa-3b41-b1cb-fe6d9962b67b | -4.02119 | -49.93859 | 2024-12-01 12:55:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4263067f-4419-3534-bc4f-121186b6ade7 | -4.18332 | -48.61319 | 2024-12-01 12:55:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 20071611-d1cb-3ab9-849e-73f4292889b1 | -2.50201 | -47.27895 | 2024-12-01 12:55:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| e9c610ce-c6a3-3c6f-9415-6b7e2d677362 | -1.49595 | -54.95649 | 2024-12-01 12:55:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 81cd1ffc-7922-358a-9cfe-5a84447991a7 | -2.64015 | -54.19537 | 2024-12-01 12:55:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 35b7402e-0d9f-3950-9179-35596aff64d9 | -2.90084 | -42.16354 | 2024-12-01 12:55:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| aa8df209-2930-3d5a-a68f-daa2786089da | -1.1462 | -53.66572 | 2024-12-01 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 23904e08-bca4-350f-ab94-431f33389d72 | -0.93224 | -47.99784 | 2024-12-01 12:55:00 | TERRA_M-T | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b1a224c1-bf8e-3f6e-8b10-db4bafee23ca | -3.13354 | -54.52621 | 2024-12-01 12:55:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 155.2 |
| a95aa30a-32e6-36d7-b2ad-0a22f95ba98d | -3.13099 | -42.37028 | 2024-12-01 12:55:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a9a64975-c4ef-3eb9-925f-3f123bdc47ec | -2.89108 | -42.03476 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 734caf46-87c4-3458-a5ca-9479ae259881 | -3.20888 | -41.69983 | 2024-12-01 12:55:00 | TERRA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| a3c4b4d3-6a5f-3979-853c-44a384e39f07 | -4.01574 | -47.00012 | 2024-12-01 12:55:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 34abacdc-cccf-39ab-8f36-ed6b4a33233b | -2.50353 | -47.26834 | 2024-12-01 12:55:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 578b9dd1-ba87-3f0e-a107-45d7041886cd | -2.02634 | -55.26907 | 2024-12-01 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c62dacb4-7df8-368f-858f-5f1e5a77e260 | -1.49276 | -52.64641 | 2024-12-01 12:55:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0b4f6237-95ba-3e42-b666-8b4ab0b836cf | -4.40617 | -49.76499 | 2024-12-01 12:55:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2c0473ff-c48e-3429-9d76-dac9dd7f968a | -4.4049 | -49.77386 | 2024-12-01 12:55:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e10a48c4-e952-32f5-84df-1f7d2e4b9bd3 | -1.93917 | -49.78204 | 2024-12-01 12:55:00 | TERRA_M-T | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 50e41a05-8239-3dac-a72d-460f31a2f513 | -2.92696 | -54.12027 | 2024-12-01 12:55:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 4b0cca1e-b691-3f75-bd4c-b53c8285e6ec | -1.56191 | -48.10957 | 2024-12-01 12:55:00 | TERRA_M-T | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f60101e5-5720-3040-a85c-536181ddd2ea | -2.99914 | -42.34614 | 2024-12-01 12:55:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 68aa5043-4c05-306e-ad42-0f98a6561795 | -2.1565 | -46.6158 | 2024-12-01 12:55:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 02ddb80d-f84f-3f56-9013-83579f5ac2a3 | -1.78555 | -52.74021 | 2024-12-01 12:55:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d207419d-73b4-394a-bee1-87707896fd36 | -1.44025 | -47.3403 | 2024-12-01 12:55:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 52cf13a3-52b2-3ec0-8875-fc681e02041d | -2.42896 | -49.33475 | 2024-12-01 12:55:00 | TERRA_M-T | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e2d11de9-cc3c-3bae-851a-e5c7494b0934 | -1.24505 | -48.32288 | 2024-12-01 12:55:00 | TERRA_M-T | SANTA BÁRBARA DO PARÁ | PARÁ | Brasil | 1506351 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9801b697-6245-3dfd-8f45-ea705c2e9c20 | -3.26655 | -50.05205 | 2024-12-01 12:55:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eac3a68f-6f79-3a7a-9091-9794ba0fa5b2 | -3.616 | -50.18848 | 2024-12-01 12:55:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ee3fa055-8597-3ae7-84fb-07744a0e57f1 | -4.32187 | -48.09112 | 2024-12-01 12:55:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 9d095dd8-cce9-373a-a275-ac324a19420e | -4.89231 | -41.34443 | 2024-12-01 12:55:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 50.1 |
| 233fb4bf-7cd1-3027-b287-50069f838599 | -2.14904 | -47.23775 | 2024-12-01 12:55:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 21f423e8-ac62-38e1-8f45-15ecac353da8 | -1.99784 | -50.40254 | 2024-12-01 12:55:00 | TERRA_M-T | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 618bf157-1d1c-367f-9824-82917d9bdbee | -1.59184 | -47.43585 | 2024-12-01 12:55:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3c34df46-3ddd-3027-8c3a-4690f633ff3f | -2.21729 | -50.5359 | 2024-12-01 12:55:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 093c76e6-cef2-3026-a4e1-ef5d917b4f0b | -2.04786 | -51.19534 | 2024-12-01 12:55:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 05dfd66c-3993-3146-a173-a5b7955710b4 | -2.49389 | -47.26697 | 2024-12-01 12:55:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 91ac5209-032e-3ecf-90e3-865759197a56 | -2.83337 | -54.09361 | 2024-12-01 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9e5a28df-fbf8-3fd1-b6c8-418bd2b8fe91 | -1.93508 | -52.9779 | 2024-12-01 12:55:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9dcdfc12-0fc5-3396-b73c-4e54fa21d2ad | -4.17417 | -48.61189 | 2024-12-01 12:55:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 61cbbbd2-8a37-332f-bd37-8d2a003ea7a0 | -3.07034 | -53.81727 | 2024-12-01 12:55:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 642ba612-1e60-3884-875d-78928a2e6c3b | -3.21062 | -41.69453 | 2024-12-01 12:55:00 | TERRA_M-T | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| f80e789b-3392-3742-8ef0-f9e08932580b | -2.13135 | -46.5771 | 2024-12-01 12:55:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| da7ffc29-9ad5-3b61-a16a-8f40d65980ab | -2.43153 | -48.28251 | 2024-12-01 12:55:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 167.2 |
| 1de2fd5f-4fab-3f21-b158-1421b1297762 | -1.407 | -49.11785 | 2024-12-01 12:55:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 1704fa16-8f05-35a5-8847-c8f41b77d93f | -1.66835 | -53.7604 | 2024-12-01 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 42ffb46d-f43c-3dde-ba62-a61e86fe6a2c | -1.13935 | -53.6717 | 2024-12-01 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 8f5fe7e2-4c11-309a-90ce-d19ba3b22073 | 1.1911 | -50.87585 | 2024-12-01 12:55:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e7965e1a-953a-3dfb-b8a1-4526e92efb24 | -2.15056 | -47.22718 | 2024-12-01 12:55:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b792d7a6-bb7a-38ee-b6f1-640013d4d38d | -0.65552 | -47.53901 | 2024-12-01 12:55:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 0bacdd10-7e02-3966-bb88-24b7ae1b7e53 | -2.45416 | -53.62208 | 2024-12-01 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 93e94b88-dda4-38a9-aca0-bf053a4916b5 | -0.65413 | -47.54881 | 2024-12-01 12:55:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5a20d804-d25f-36c9-91d0-07a282fb62e9 | -3.00115 | -41.99478 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 21957880-8f97-3210-97d8-bd0530a577ce | -2.87644 | -42.03281 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 93fae1fa-440a-33f2-a107-7887691b3553 | -3.00175 | -42.00001 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 055fa1fe-c16a-3b69-ae87-5a39738befe7 | -1.47813 | -52.67778 | 2024-12-01 12:55:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3288c797-d8eb-3ea5-8aa2-92af6ce00cb2 | -2.04362 | -54.66665 | 2024-12-01 12:55:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 80c5f619-8135-3277-9c5b-aac22c7f24ca | -1.40828 | -49.109 | 2024-12-01 12:55:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f623c389-4277-35ef-94f3-856ca1a319ba | -1.69915 | -52.63264 | 2024-12-01 12:55:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 4bfd4875-6e96-3d39-a158-db96b4c5518b | -1.48792 | -52.67916 | 2024-12-01 12:55:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |


[Clique aqui para ver as próximas entradas](README102.md)
