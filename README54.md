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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8cfd075-0e58-3cd4-92bb-a5ed76f393c7 | -16.13091 | -54.00292 | 2025-10-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99869570-9dfa-3e08-8a09-a0d504cd8513 | -14.42543 | -50.95844 | 2025-10-24 05:31:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 605e1f22-923a-376d-a897-011c4ba2e2d9 | -18.35784 | -51.70643 | 2025-10-24 05:31:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c738e982-b957-32e4-aaf2-ff012e37f014 | -14.43211 | -50.95926 | 2025-10-24 05:31:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 180ec311-6b8c-352b-b5a3-19e72150c053 | -20.92424 | -55.77348 | 2025-10-24 05:31:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bacd7bd0-935e-3c3d-aa3f-72d8b37ee6e7 | -21.76005 | -52.26653 | 2025-10-24 05:33:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 21ecfe05-83a0-3fd2-8cee-88dc3b4316b0 | -22.3896 | -53.52816 | 2025-10-24 05:33:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2ba1b002-ad8d-37d6-a4d4-708a7529bf16 | -22.39584 | -53.52886 | 2025-10-24 05:33:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 458bb4ec-f6fc-3e1a-847f-78aa25aab43e | -21.75957 | -52.27275 | 2025-10-24 05:33:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4ae11217-cf79-30a2-a4b9-3db050cf723d | 1.55712 | -56.00677 | 2025-10-24 05:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b8595ac-6e8a-3f9e-a07f-7224eb921e38 | 1.56072 | -56.00896 | 2025-10-24 05:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e83c1cf8-b29d-33e8-8f04-27f34acce1ce | -1.54326 | -55.40765 | 2025-10-24 05:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dd479b6-90a1-34fb-a125-327bc8dc23e7 | 1.56001 | -56.00476 | 2025-10-24 05:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de64aef5-a8c2-3d9f-bebd-42baf26e88c4 | 1.64227 | -55.75587 | 2025-10-24 05:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38cd39ba-80d2-30dc-a4a2-5b3145e66a71 | -1.54889 | -55.41411 | 2025-10-24 05:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b536fe57-8aa3-3a8c-9131-e0b8e9e32712 | -1.54972 | -55.40873 | 2025-10-24 05:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 422789cd-929b-32b7-9ea6-76c5bcd04f5b | -1.8419 | -60.00185 | 2025-10-24 05:55:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05d9f979-bece-3791-9391-b81e89689be3 | 1.5631 | -56.00596 | 2025-10-24 05:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5476313-8c93-3bb4-80dc-7d4461f30ec2 | 1.64299 | -55.76038 | 2025-10-24 05:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7eabac1e-1e75-31df-9d98-6166b472901d | 1.56737 | -56.01221 | 2025-10-24 05:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b78232c-2934-3f49-b390-0e63f9cfdbbf | 1.5697 | -56.00908 | 2025-10-24 05:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad236e4f-db2a-3801-8ab7-22b22181be0a | 1.56666 | -56.00799 | 2025-10-24 05:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8942b8e-b9ae-3c8c-9fb9-6d7faacefc56 | -9.44475 | -56.65394 | 2025-10-24 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fcccd852-aa79-3497-824d-01bb140e1d9e | -9.0271 | -63.70836 | 2025-10-24 05:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b5ab69c-3f6c-31ec-8b57-7d6f82e6bfcb | -8.6583 | -64.27712 | 2025-10-24 05:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d6f7ab0-e475-390d-a8c4-a03c16fec642 | -9.44156 | -56.65359 | 2025-10-24 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 008db3f1-5fee-3c83-8ee0-ce6cedf7e734 | -9.44824 | -56.65424 | 2025-10-24 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57806567-2f56-38aa-a12b-29a4117b69e4 | -14.78843 | -59.24428 | 2025-10-24 05:59:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76bfc43f-0c4e-3613-a311-dd813970ee83 | -12.3897 | -57.52771 | 2025-10-24 05:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06861e8b-61b3-31c7-b28d-b72e77a6d5f6 | -12.37391 | -63.87042 | 2025-10-24 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07ab4378-f999-366b-a99a-c23890ec40c5 | -10.02037 | -63.73643 | 2025-10-24 05:59:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44d173c2-334b-3026-9fc6-bff9b89150b5 | -12.37766 | -63.87516 | 2025-10-24 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f87cdef-b6c0-36c3-8ccc-224806752760 | -11.77011 | -64.8521 | 2025-10-24 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 277c3019-bc0b-3ee7-ab4c-838c8b72f497 | -9.46356 | -63.23145 | 2025-10-24 05:59:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1b76b62-a975-3a7e-a968-4e64f0fb4dca | -11.78358 | -63.18319 | 2025-10-24 05:59:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62864382-af4c-3a02-a3cb-dadcfbc663da | -9.85578 | -65.19382 | 2025-10-24 05:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 985ca7ad-116b-3434-af45-57ae082b3c31 | -12.37336 | -63.87455 | 2025-10-24 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 858239be-bb71-3f18-8dec-7416973f2995 | -12.37821 | -63.87103 | 2025-10-24 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d20c438b-9547-3b47-8cc5-c44220da98a1 | -10.13394 | -63.72378 | 2025-10-24 05:59:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c43e85dd-ebe2-358a-baa9-23795b729bf6 | -10.1336 | -63.72486 | 2025-10-24 05:59:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddc5fab8-7b72-336a-b12e-cf2a19be0654 | -9.5861 | -63.49918 | 2025-10-24 05:59:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b86267c7-f7dd-36a7-a30d-c3aa566fa008 | -14.7889 | -59.24 | 2025-10-24 05:59:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e15dcd08-ef06-356b-af01-d33b2bf181bd | -13.64331 | -59.78324 | 2025-10-24 05:59:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de03041d-3103-3e50-9d1f-323c6533e1e5 | -11.7661 | -64.85151 | 2025-10-24 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 696aec2c-3c5f-35c0-8f8d-1f377ae30ceb | -10.01617 | -63.7358 | 2025-10-24 05:59:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e61ee157-6e7e-3196-924f-3e3f64e048dd | -9.64823 | -64.10524 | 2025-10-24 05:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 813fa640-2446-395b-9f2c-7f16a67ffd77 | -12.37421 | -63.88063 | 2025-10-24 06:20:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fa86c23-2f07-39ae-b6f4-948b71a8ef84 | -12.37483 | -63.87525 | 2025-10-24 06:20:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75bf6c17-6145-3107-8efb-be5ec7f35820 | -9.97357 | -65.11951 | 2025-10-24 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4bca2472-8908-3439-8314-359eb71f9882 | -9.9741 | -65.11541 | 2025-10-24 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ae1715a-51ff-32e5-a424-7a4833500d59 | 2.07381 | -55.70404 | 2025-10-24 06:54:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0c44c96a-9d31-3232-9566-35eb74481e24 | -1.54842 | -55.40561 | 2025-10-24 06:57:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| eb45d393-08b1-367b-8ce0-2bd0a3ff8ea4 | -16.4743 | -43.9774 | 2025-10-24 10:40:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 96c8eeb6-293e-338d-a402-300508492566 | -16.4743 | -43.9774 | 2025-10-24 10:50:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 109.0 |
| c0233660-88cf-3471-b926-d52aea331b74 | -12.7786 | -47.3752 | 2025-10-24 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 563a9f6c-c87b-3bf1-954c-70126bbb81e8 | -12.7786 | -47.3752 | 2025-10-24 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| dd3cf866-0871-37df-932a-e6b0c101073d | -15.1405 | -43.8014 | 2025-10-24 11:30:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 498f69bc-fde9-3abf-8add-b07c03f2a858 | -12.7786 | -47.3752 | 2025-10-24 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 6874efd9-ddb7-312c-ae7e-0d2374a79d7b | -12.7786 | -47.3752 | 2025-10-24 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 0fc4d02a-a82d-37a6-9ac9-81d6bafee2fc | -12.1696 | -49.4211 | 2025-10-24 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 74efde52-2d8d-3df8-b77d-39645c582e36 | -11.9635 | -49.1858 | 2025-10-24 11:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c90d78a7-7c83-321d-8490-3fe6ff5cb9a3 | -15.1405 | -43.8014 | 2025-10-24 11:50:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 194526c2-7d0d-3391-a983-6ba22d94ef36 | -12.7786 | -47.3752 | 2025-10-24 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 9390389d-aa75-3887-a8ca-edf97fc254d6 | -15.1405 | -43.8014 | 2025-10-24 12:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 4e5dd32a-8d92-3fd0-a29f-387496935cf1 | -12.7786 | -47.3752 | 2025-10-24 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e24ce915-1086-30a3-addc-021e6be5907b | -12.7786 | -47.3752 | 2025-10-24 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 4b14ef68-b76f-321a-a731-57f8247381f5 | -10.9387 | -50.3835 | 2025-10-24 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| aafbec1f-06c2-3000-848f-11813517424f | -15.1405 | -43.8014 | 2025-10-24 12:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 113.9 |
| a0d01336-f05d-32f3-9b5d-bec0ca4cdc62 | -10.9577 | -50.3815 | 2025-10-24 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 53df4bde-6fdd-30c0-bffd-199c9d74c2ec | 1.35338 | -50.69957 | 2025-10-24 12:14:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 9520298f-8fc1-3008-978a-b2a5ccabb817 | -1.43721 | -47.16894 | 2025-10-24 12:17:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 08fa8943-8e43-3250-8cb1-507ceaf8d790 | -6.83721 | -41.54375 | 2025-10-24 12:17:00 | TERRA_M-T | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| a68306ab-3ffc-38ea-a6c8-4525f828a59e | -4.88112 | -47.54461 | 2025-10-24 12:17:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cbf7b133-483c-334a-997f-8747061a2a04 | -3.59131 | -44.95401 | 2025-10-24 12:17:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 29612b25-24ab-3e7c-a0a4-5abbfecd795e | -4.15919 | -46.78843 | 2025-10-24 12:17:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a2b9d3d4-89f4-38c9-9133-77256cbe044c | -4.81902 | -47.78777 | 2025-10-24 12:17:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f86c62c9-5bdc-3987-ae65-085e2c343021 | -6.18434 | -42.61687 | 2025-10-24 12:17:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 29.6 |
| 91b40c67-08d7-37e9-986d-3768796b2d75 | -7.28263 | -46.94558 | 2025-10-24 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fe28f595-c8fd-38f9-94c5-a45e9b17e3aa | -0.81909 | -48.64392 | 2025-10-24 12:17:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 251ee10c-0bec-359e-a45f-71a650aa3535 | -3.74673 | -44.00143 | 2025-10-24 12:17:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a2dec448-7d79-35fc-8ed9-735578aff2a0 | -5.86132 | -38.26315 | 2025-10-24 12:17:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 595c0b39-e341-31ed-a446-f0c56e909cb3 | -4.10323 | -43.21421 | 2025-10-24 12:17:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 589a1747-0216-3d11-8da4-f3992ce783e9 | -6.44112 | -45.66233 | 2025-10-24 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 244110e0-fc69-3de3-a661-aa0c1517d6f8 | -3.74907 | -43.99704 | 2025-10-24 12:17:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| afdee925-9b6d-3124-ab48-c22abe73af74 | -5.62066 | -39.23545 | 2025-10-24 12:17:00 | TERRA_M-T | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 5ba4235e-057d-3d49-a5bb-4e919b9e865d | -1.29271 | -48.82368 | 2025-10-24 12:17:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| bca0f65d-6f91-3695-b8b6-d0cf3c871c56 | -6.37048 | -46.48997 | 2025-10-24 12:17:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 98f063fd-eb10-3f45-8082-9ac4d9c16e66 | -6.94594 | -44.02037 | 2025-10-24 12:17:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e882e5b8-ea82-39c2-9f8a-274ce07b9ed3 | -1.45569 | -47.30453 | 2025-10-24 12:17:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d0b78fa7-17a8-3da6-9a32-0dd81006f441 | -6.73686 | -45.38832 | 2025-10-24 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c31b02a3-deb4-3e65-b1ba-d7094215dd47 | -3.22373 | -49.3684 | 2025-10-24 12:17:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6427ae6c-0eb0-37b6-9a29-77bc6d83d41b | -1.45366 | -47.11716 | 2025-10-24 12:17:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ca2e01e6-0b41-334c-9ac3-ff57ce84b634 | -3.7483 | -43.9904 | 2025-10-24 12:17:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| e5d95b76-ceaf-3dc9-907b-133e32a227ed | -5.45341 | -45.40919 | 2025-10-24 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 291db993-6d6d-3afd-bbd2-7325733da15b | -7.0576 | -47.22925 | 2025-10-24 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3a8fce4b-66d4-3751-9657-f9863085590b | -3.75059 | -43.98597 | 2025-10-24 12:17:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 6e94c8b5-186e-3239-8cf0-307abb1d2ece | -2.87518 | -45.25233 | 2025-10-24 12:17:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 34eebd55-340d-3d92-9252-ee75d68147dc | -3.80648 | -42.85931 | 2025-10-24 12:17:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8c4c485d-c045-323b-a68b-e45a9e81ac71 | -3.14753 | -50.2449 | 2025-10-24 12:17:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3cf5801f-f759-31e5-928d-1a2730fddddb | -6.03841 | -38.22507 | 2025-10-24 12:17:00 | TERRA_M-T | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 52.4 |


[Clique aqui para ver as próximas entradas](README55.md)
