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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1eb7a055-8e18-3e2a-b3a7-8d860c9ce3cb | -3.4076 | -41.6432 | 2024-11-20 09:00:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 8af184be-20f7-3f5a-8faf-a33713337b4c | -3.92 | -42.39 | 2024-11-20 09:00:00 | MSG-03 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bae50b83-b490-338b-9096-6667d27e1611 | -3.92 | -42.44 | 2024-11-20 09:00:00 | MSG-03 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a260db8d-b40c-30c1-b46b-5f8459768258 | -3.3889 | -41.6441 | 2024-11-20 09:10:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 749e1d5a-4d64-385a-96a9-c50166e6f2a1 | -3.4076 | -41.6432 | 2024-11-20 09:10:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 145.0 |
| 07a41457-fcc8-3975-b70a-18383ef9dab9 | -3.3889 | -41.6441 | 2024-11-20 09:20:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| e3d77f6c-4967-3096-8db0-2473ab51245f | -3.4076 | -41.6432 | 2024-11-20 09:20:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| b619e5b2-b0cc-3227-8a5b-460cc3d0174f | -3.3889 | -41.6441 | 2024-11-20 09:30:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 9f56df90-a291-3218-a07b-299552ed12b9 | -2.9058 | -45.0337 | 2024-11-20 09:30:00 | GOES-16 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| b465ed48-c0a0-3b90-a9e2-019ce643c8a6 | -3.4076 | -41.6432 | 2024-11-20 09:30:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 157.6 |
| e9879dcc-17f8-3820-8e39-6e363497d143 | -3.4076 | -41.6432 | 2024-11-20 09:40:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 165.1 |
| 77ce5183-0f53-32d3-9175-c6870ac2911e | -3.3889 | -41.6441 | 2024-11-20 09:40:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 3ec35492-0384-3e29-a534-2ce32a68735a | -3.4076 | -41.6432 | 2024-11-20 09:50:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 132.4 |
| 5e0b5d66-50fd-3b7f-93d2-64d8b6a8d35a | -3.4076 | -41.6432 | 2024-11-20 10:00:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 4694f004-bca2-35ec-a802-d608c76b853f | -3.3889 | -41.6441 | 2024-11-20 10:00:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 0bc1b15b-f24d-334a-8071-786a21058dc3 | -3.4076 | -41.6432 | 2024-11-20 10:10:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| cf2d4b83-e8f3-3ad4-9b8b-798dd08a619a | -3.4076 | -41.6432 | 2024-11-20 10:20:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 68c304e3-966a-34f5-b278-fc686f733a29 | -3.483 | -41.5436 | 2024-11-20 11:30:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 3945b325-2107-3457-9c0d-406cf2729d4b | -3.405 | -42.1199 | 2024-11-20 11:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| b3dd3c20-0f6b-3483-af62-7c8ca8f896f1 | -3.483 | -41.5436 | 2024-11-20 11:40:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| e8b9d425-8818-3945-86da-7a1c5b6c683a | -3.405 | -42.1199 | 2024-11-20 11:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 3df9d0d7-e248-3f63-8dbf-94da17ed6617 | -3.5547 | -42.0888 | 2024-11-20 12:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| ad947749-6467-3090-9c49-1d71ca299cc9 | -2.63 | -47.93 | 2024-11-20 12:00:00 | MSG-03 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b6ec990-2574-337f-a501-0be59a7c8b6d | -3.57 | -42.06 | 2024-11-20 12:00:00 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ed599ab-f1f3-3179-9a35-0efd0986571b | -3.6 | -42.07 | 2024-11-20 12:00:00 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| baf4a5fa-7d63-3151-a4ff-8c573b6447da | -3.57 | -42.11 | 2024-11-20 12:00:00 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2fd37004-7c49-3af2-be05-befd96ff2802 | -3.6 | -42.11 | 2024-11-20 12:00:00 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b2e78d20-8d07-3778-b777-0512652cdd5a | -5.34018 | -40.30064 | 2024-11-20 12:08:00 | TERRA_M-T | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f8580084-b756-36cb-8262-65d973622a5e | -6.31857 | -38.32804 | 2024-11-20 12:08:00 | TERRA_M-T | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 75b96f1a-cf3d-32ef-8431-8390603b842a | -3.45291 | -42.54235 | 2024-11-20 12:08:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 714ce7c8-07d5-398b-9af9-26139880591c | -3.46117 | -42.3016 | 2024-11-20 12:08:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8b56e1e4-a837-3c29-a7d0-ddc84b561945 | -5.13119 | -37.34097 | 2024-11-20 12:08:00 | TERRA_M-T | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 9227414b-b183-3007-b402-6c463adb1cb7 | -7.47839 | -37.56141 | 2024-11-20 12:08:00 | TERRA_M-T | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 9343b7cb-99d6-358b-bd4d-0abfcd56b68d | -7.31951 | -37.2499 | 2024-11-20 12:08:00 | TERRA_M-T | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| f4984285-427b-3623-9e9e-cb7d473079b8 | -3.42168 | -39.09504 | 2024-11-20 12:08:00 | TERRA_M-T | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| ca26581d-6318-3d40-9e96-12cfbb2b270e | -6.33059 | -41.72959 | 2024-11-20 12:08:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 361c2548-fe8b-34b8-9139-14ac894c1aaf | -3.56629 | -42.07029 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 84294172-428c-3d8e-bc22-636f53d94952 | -3.298 | -42.30412 | 2024-11-20 12:08:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 70edee17-d0d6-31d7-965e-9d5d9af3ecf2 | -3.55424 | -42.08086 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| a050315c-326a-354b-a16e-b85fc17460c1 | -6.28504 | -38.87489 | 2024-11-20 12:08:00 | TERRA_M-T | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| cacb43cc-3168-3f4b-87d6-2131d5fe8ce3 | -6.16394 | -35.63626 | 2024-11-20 12:08:00 | TERRA_M-T | JANUÁRIO CICCO | RIO GRANDE DO NORTE | Brasil | 2405306 | 24 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 1df85e5e-cd39-3014-aef6-4d8c4717c319 | -3.40592 | -42.12191 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 495aba4b-6c10-35da-bc9a-cabb76bb2745 | -7.1552 | -39.05088 | 2024-11-20 12:08:00 | TERRA_M-T | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 95e73148-6c97-349b-b17b-4fceb05ef8ae | -3.41447 | -42.13569 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| f92227e5-e36c-30cf-ae9f-4e734c5e4a23 | -6.5875 | -38.05591 | 2024-11-20 12:08:00 | TERRA_M-T | SÃO FRANCISCO | PARAÍBA | Brasil | 2513984 | 25 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 835ea653-1cd1-3826-ab90-a5c36200b4e8 | -3.44863 | -42.53567 | 2024-11-20 12:08:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b8778a78-116a-3a92-b8f0-67fd97a8b610 | -4.61503 | -43.29708 | 2024-11-20 12:08:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| afddeb77-a351-3801-9bf1-0d8ef3d9b340 | -7.08543 | -37.99428 | 2024-11-20 12:08:00 | TERRA_M-T | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 07ecb720-b5ad-347e-9227-d5119afc0563 | -4.95143 | -38.97729 | 2024-11-20 12:08:00 | TERRA_M-T | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 5706b31f-ded4-384f-b776-f2620d32cee4 | -6.16231 | -35.64802 | 2024-11-20 12:08:00 | TERRA_M-T | JANUÁRIO CICCO | RIO GRANDE DO NORTE | Brasil | 2405306 | 24 | 33 | nan | nan | nan | Caatinga | 22.2 |
| df864494-456f-3af1-98cc-577248a268e5 | -6.25445 | -38.25798 | 2024-11-20 12:08:00 | TERRA_M-T | RIACHO DE SANTANA | RIO GRANDE DO NORTE | Brasil | 2410801 | 24 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 61a1033c-a2db-394c-a99e-617c35daf21c | -5.85928 | -38.31447 | 2024-11-20 12:08:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 668665bc-1e09-338e-835d-006b6efb41a4 | -4.24749 | -41.75842 | 2024-11-20 12:08:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 6eb3902c-7368-3614-8ce8-8ad1a762611c | -3.39319 | -41.64865 | 2024-11-20 12:08:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| f3f5bf19-872f-3f19-8cd9-9fe4c3618779 | -7.47975 | -37.55184 | 2024-11-20 12:08:00 | TERRA_M-T | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| aee7b968-00b3-36ea-b150-b9a6ab2f6ff1 | -3.56886 | -41.49603 | 2024-11-20 12:08:00 | TERRA_M-T | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| e107fe52-479d-3ac0-be0d-7d8b4076a427 | -6.93377 | -41.19776 | 2024-11-20 12:08:00 | TERRA_M-T | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 36.3 |
| 5693ca4c-2a01-39e6-bf9e-e37804247552 | -6.20627 | -37.43364 | 2024-11-20 12:08:00 | TERRA_M-T | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 6347c0d1-540d-331d-9a2c-91001217584e | -7.34287 | -36.94614 | 2024-11-20 12:08:00 | TERRA_M-T | LIVRAMENTO | PARAÍBA | Brasil | 2508505 | 25 | 33 | nan | nan | nan | Caatinga | 8.9 |
| f83cb8e7-22ee-3061-a332-db4f47e85df5 | -2.88457 | -41.76362 | 2024-11-20 12:08:00 | TERRA_M-T | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 385a912a-fb3a-3c77-95f9-ea20f2139525 | -3.56451 | -42.08235 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 415.9 |
| 61a03b39-d616-33a7-af84-45c5ab6bc5a9 | -3.39915 | -42.6502 | 2024-11-20 12:08:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 9078293e-48a1-3a54-a013-2ccbaa7dc3c0 | -5.93543 | -37.71643 | 2024-11-20 12:08:00 | TERRA_M-T | OLHO D'ÁGUA DO BORGES | RIO GRANDE DO NORTE | Brasil | 2408409 | 24 | 33 | nan | nan | nan | Caatinga | 12.0 |
| d8146958-b4dc-3c02-8982-fb51e0355612 | -7.21581 | -35.63311 | 2024-11-20 12:08:00 | TERRA_M-T | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 7abe2914-7b66-3073-9db4-cccae830bc38 | -3.41069 | -42.1418 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 444d83c2-a695-3ef7-916b-1e487295d68b | -5.48638 | -36.91218 | 2024-11-20 12:08:00 | TERRA_M-T | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 11.6 |
| a5a00bd1-05e8-3a6c-9d7f-29af996f5882 | -3.41625 | -42.12336 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 8b43e312-4c98-30ad-9a90-c8a7eee11da3 | -6.38278 | -41.53893 | 2024-11-20 12:08:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 8fff49fa-8122-3c9f-9d48-a299296b5ba7 | -4.12407 | -43.58628 | 2024-11-20 12:08:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c57f9ab5-fc9f-30e0-a54d-c3ef5afb27c7 | -3.53363 | -41.87686 | 2024-11-20 12:08:00 | TERRA_M-T | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| d8af2a56-6e47-3cd9-a3f3-07dd04609ae9 | -2.88284 | -41.77544 | 2024-11-20 12:08:00 | TERRA_M-T | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2d3ab707-7220-3aa0-96b1-98d039b7d491 | -3.59529 | -42.08688 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 384.1 |
| 09dedafe-8465-30f9-bd31-27da65a1fd60 | -3.73723 | -42.23218 | 2024-11-20 12:08:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 491131b4-93c8-3e8d-8ede-697bef0222fc | -6.65139 | -41.98832 | 2024-11-20 12:08:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| b371a6d1-8ba7-3b6c-ace9-a4102eab6720 | -3.4049 | -41.63862 | 2024-11-20 12:08:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 54224fd3-22d6-324b-ab9f-3419e09506f2 | -3.4796 | -41.54533 | 2024-11-20 12:08:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| eaccff94-9842-3e2c-9de1-7b7322ae8c95 | -3.3936 | -41.64251 | 2024-11-20 12:08:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 4e3219e4-7fcc-312f-89fc-4f02ac480173 | -3.40414 | -42.13421 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 2769eb14-ad5c-3fd9-b525-aa652426cb7f | -3.38202 | -41.44432 | 2024-11-20 12:08:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 4b631fc9-7569-30eb-9135-e376b8130789 | -7.07921 | -35.88979 | 2024-11-20 12:08:00 | TERRA_M-T | SÃO SEBASTIÃO DE LAGOA DE ROÇA | PARAÍBA | Brasil | 2515104 | 25 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 630789fb-1e12-3181-9e37-888cdd9d1b7f | -3.32456 | -43.0788 | 2024-11-20 12:08:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 8937db6d-c2a0-3837-a010-76d266060264 | -3.56271 | -42.09449 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 161.1 |
| 3833f7ec-f4ca-3235-9ce0-d4ea688a4cca | -6.42609 | -37.70227 | 2024-11-20 12:08:00 | TERRA_M-T | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 9.9 |
| edbaa96b-5572-3601-a6d1-7d9253252964 | -6.35406 | -35.1576 | 2024-11-20 12:08:00 | TERRA_M-T | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 644f6e4e-5329-3dea-add5-38b9a7e6ef9d | -3.59706 | -42.07477 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 935.2 |
| 66eea8f0-683a-3bd4-826a-0e248a85b54b | -3.39492 | -41.63723 | 2024-11-20 12:08:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| c6f8b11a-9292-36e4-8ab4-2e8ef1462124 | -6.69129 | -38.69284 | 2024-11-20 12:08:00 | TERRA_M-T | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 67d3f505-4523-3d7e-9dda-bd7eb8ff7100 | -7.43024 | -37.43681 | 2024-11-20 12:08:00 | TERRA_M-T | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 186691d5-da35-3da5-b7fe-27d611d1a6dd | -5.39532 | -35.867 | 2024-11-20 12:08:00 | TERRA_M-T | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 12.5 |
| a09ba030-9b36-336b-8046-62481e9ae44e | -5.04685 | -39.59115 | 2024-11-20 12:08:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ea56d058-a195-3f01-b0e2-34cf3e8c170a | -3.53192 | -41.88861 | 2024-11-20 12:08:00 | TERRA_M-T | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| c3694809-07e3-3502-8cf8-0ccb76b10790 | -3.84537 | -41.56579 | 2024-11-20 12:08:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 5cf2e7a4-9b27-3d2a-9763-f0ddee9249ac | -3.41257 | -42.12947 | 2024-11-20 12:08:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| c7564ac8-2319-32b3-a85b-81120b5bfea9 | -3.5547 | -42.0888 | 2024-11-20 12:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 6e75065a-f74f-3090-9e0d-c8dc1d753182 | -3.3739 | -44.4247 | 2024-11-20 12:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 17c25d5b-538f-3cf2-969a-7d148da60b5a | -8.84492 | -37.47245 | 2024-11-20 12:10:00 | TERRA_M-T | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 571a6e93-5d1a-30ee-9ec4-fed71523126b | -9.19785 | -44.72364 | 2024-11-20 12:10:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 7eb5c8db-e85e-3ee9-805b-64269f9f24ea | -9.18868 | -44.7164 | 2024-11-20 12:10:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 1149a6d4-1635-3ee4-871b-b8338e0f9c00 | -9.80089 | -41.96562 | 2024-11-20 12:10:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 0000a0b3-6e72-3939-acd8-028dad15d746 | -7.52709 | -39.99122 | 2024-11-20 12:10:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |


[Clique aqui para ver as próximas entradas](README77.md)
