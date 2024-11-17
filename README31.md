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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d9d525e-c015-36d4-b766-898aed076da2 | -3.78712 | -46.03619 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e181105c-fc26-3a99-9d13-e725c26a288a | -4.14117 | -44.18686 | 2024-11-17 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3a999794-2d8b-3ba7-8f50-68c829833208 | -3.41492 | -46.13622 | 2024-11-17 04:06:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76eec65f-2d06-399f-b9e8-1dfb729df04d | -3.24305 | -53.5262 | 2024-11-17 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 130ea3be-960e-305f-b8ea-fb8e35a671c0 | -2.24139 | -46.8362 | 2024-11-17 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b6d5b47-c428-39a9-9e10-b7c6d6e70c97 | -3.18663 | -53.24753 | 2024-11-17 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc2d49bc-9e7a-3709-ab84-ff703b88f177 | -2.86299 | -46.71998 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b401858d-cb44-3235-b35c-f9f3d805b1ec | -3.62158 | -50.21753 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fed2afa-bcc3-3122-8a88-fe6b4cbcdc17 | -3.91711 | -46.52906 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e3946751-78ff-3666-abdb-a692038b1d4a | -7.27699 | -45.79786 | 2024-11-17 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a3bcd04-cb36-32eb-9922-a6a06c55a369 | -3.48571 | -53.99234 | 2024-11-17 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b194947d-7a14-305a-895d-7b4c7b491c9d | -3.79687 | -51.37381 | 2024-11-17 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf6c4ac8-d601-3511-910c-7236bccc7bf1 | -3.66411 | -50.6069 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7949e524-5395-3919-b394-0f935d41ff1d | -5.69424 | -46.56767 | 2024-11-17 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4a69cb9-cc15-3bba-bf3a-8da548c9b90b | -7.47575 | -47.17939 | 2024-11-17 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c12b65b6-3d80-3936-99d8-b39153fc5d6c | -5.63206 | -46.36576 | 2024-11-17 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed4e0bf1-e279-32e1-9aac-a6774b9a1c8e | -2.66541 | -46.20658 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 349fa643-0d15-34d1-92ae-48b6dec0f01f | -3.52735 | -50.242 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8862bd16-2252-33d5-a767-fcb2fd76af1b | -4.55733 | -48.01093 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6ee28e76-c34e-3b1d-937a-626ebd16318b | -4.3696 | -43.00567 | 2024-11-17 04:06:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e3f96276-3ac2-3a94-b594-e2b2058c5a9f | -3.53644 | -50.25495 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dc6e4c11-10e9-37a0-bdc4-ac3e332ec37c | -7.30028 | -39.16102 | 2024-11-17 04:06:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 01eddc27-f722-3b86-8376-a0b49414e0b1 | -3.94866 | -46.70469 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a748e88-cc12-3b65-b88c-f6549a0035f3 | -4.57889 | -48.02449 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a14fd3e1-789e-385e-829c-dc19fc05f31f | -6.9521 | -46.4007 | 2024-11-17 04:06:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 171eabc0-a08d-38d9-9865-e06bc8a08328 | -2.65354 | -46.20144 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ed8d923-169d-3ab1-8b50-0e8b270de443 | -4.37536 | -48.56475 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc95115f-9b03-30b4-8f46-3e06b9ad01c1 | -5.40603 | -46.34994 | 2024-11-17 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cdd1a5f-f6ea-35ce-9aa6-b9d0b1e53eeb | -2.07723 | -48.53178 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c73d2a9f-e233-302b-b322-60ea577d5e2e | -2.68295 | -46.20546 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6df6f8e-0dc1-3d0b-bd64-6114b02b86d6 | -2.06474 | -46.54552 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8509175-c3e4-3e27-af78-5ccb28edb2df | -4.45503 | -44.54561 | 2024-11-17 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10606952-af00-3abd-9c5a-a754896fafe2 | -3.56451 | -50.25599 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 781d01f4-afcb-36ae-b3c3-daa21341ce23 | -3.03897 | -47.98086 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 086adabc-2f5f-3e46-a91a-717f78ec5920 | -3.00683 | -45.42575 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 21b71a48-39b8-3c26-bfc2-b77088fe3e1e | -3.21061 | -46.67963 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 025645e2-4581-3995-8a37-bf8010cb48f5 | -2.40226 | -48.45175 | 2024-11-17 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| daa63f75-9eaf-345c-b547-f51b1ee147c4 | -2.64711 | -45.43555 | 2024-11-17 04:06:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7f1bdf1-94a2-34ed-846f-28f80684470f | -3.90572 | -43.04265 | 2024-11-17 04:06:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46825691-c095-30d7-959b-374b8a117338 | -3.93645 | -46.16931 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dbd7d1b-003d-324c-bc52-fd9ff017489c | -4.29805 | -48.09851 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f82869d8-4951-3eb3-a0af-6a4d5ec5ae10 | -3.56393 | -50.25942 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a4853a77-7e3e-3bec-81cb-fc74ff835bd1 | -3.95356 | -46.70158 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d030b94c-f380-35f0-9ec5-fc1fb397425c | -6.94188 | -42.82074 | 2024-11-17 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9cb8f231-62ad-3a2f-9b12-19501ab498ac | -4.52041 | -42.95195 | 2024-11-17 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3602fa75-d89b-3d32-9fc9-60fdfdd4a297 | -3.63194 | -50.22337 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14d80900-82a1-3046-80e2-0d9122e4cfb4 | -2.17908 | -49.10514 | 2024-11-17 04:06:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 803110dd-8bab-3480-bbb5-69aafe02eaed | -2.21545 | -47.21809 | 2024-11-17 04:06:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| baf83709-07ce-3e71-b3f4-b369c2d8e3ac | -3.51999 | -50.25203 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 22661a8d-8aab-3835-bd17-81ad78ae6052 | -2.58388 | -47.56829 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c7bdbdea-1450-3932-95f5-73649e24e6e0 | -4.30043 | -48.07171 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5cda01f-1b24-3d48-a473-7924d756fe61 | -6.93514 | -42.81963 | 2024-11-17 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e90ba811-629e-3ce8-85a5-bd572a5c7971 | -4.1821 | -46.82235 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb16ba08-7109-3a96-b9b4-5558fab8ef97 | -5.08531 | -42.56494 | 2024-11-17 04:06:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| df3a5868-054e-3684-af44-c52a54518b3a | -6.01947 | -41.87758 | 2024-11-17 04:06:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 27408346-aef7-312d-9173-0ba960c99f0a | -3.63138 | -50.22602 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fd2c62a-0ed2-3d0c-a9ef-cabfb0150598 | -3.36 | -46.08104 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f92314a-d558-37f4-adf0-a43da2bd1420 | -2.08862 | -48.26942 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| de2a122c-3205-39ae-a104-469f3f803bd0 | -4.29963 | -48.0766 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe5a7636-a3bd-3a29-9755-9a14407f74b9 | -3.62711 | -50.21813 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 395d4360-1d67-37fd-b3ea-9426f329868c | -2.64471 | -46.14836 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bc6525c-ad68-3fd8-b8f0-a7681fc5cab6 | -6.49636 | -47.50154 | 2024-11-17 04:06:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36e89f8d-635b-3fae-9c4c-618689cb0cd6 | -7.13327 | -46.63791 | 2024-11-17 04:06:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3658348-9d7c-33d8-b647-7ddc2679a3b6 | -2.67937 | -46.20088 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f569a4c2-9730-381d-95d4-362b9d21126b | -1.13712 | -51.6852 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac7f03f8-5d15-3851-a990-0cff26bccf46 | -5.69485 | -46.56398 | 2024-11-17 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01a6093b-0488-3f9b-b820-9162851513bc | -2.65292 | -46.20534 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79a3a1cf-a7ee-3983-9ed0-4bda9236f6b5 | -3.41908 | -46.13688 | 2024-11-17 04:06:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d889698-1b68-34f8-8058-bb62d8739115 | -2.82695 | -46.6671 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1a7fb072-cbc4-30ad-9d61-97aca386353a | -1.9057 | -45.60993 | 2024-11-17 04:06:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f16e24ff-745c-3b83-9593-97fde876e9e7 | -3.49554 | -43.78773 | 2024-11-17 04:06:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1e4061d-4d78-3129-8cb4-4ff86ef0e3c3 | -1.13985 | -51.69241 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eb96f799-bb01-3d52-a1a0-527adcf03b33 | -3.18241 | -53.2517 | 2024-11-17 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 275ece2a-bfe4-3ba6-ac2f-5390948afdd1 | -8.55187 | -40.58213 | 2024-11-17 04:06:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 27232b44-71cf-3de6-861d-c8578cf7e443 | -1.14181 | -51.69606 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc0b33d2-b320-3305-bb73-c880de18e7e9 | -4.37451 | -48.5698 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eba0773b-d5a5-34b4-a5e5-43a19e5bb04e | -3.17449 | -46.60225 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56a39004-f7a1-3271-aae8-6b55d61c597a | -2.99325 | -52.60707 | 2024-11-17 04:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cde5f49-6263-3e65-af04-3002caafa827 | -3.95955 | -46.7188 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7f9be63-e2ff-3624-b4a9-eb228edba59c | -5.628 | -46.36497 | 2024-11-17 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1829a6da-6de5-34b1-a418-e70aff10e1cc | -2.62586 | -46.18488 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f244bb7f-0e7b-3f65-b7ca-d02b9ea38b6f | -2.46455 | -45.61282 | 2024-11-17 04:06:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbf00126-5f9b-3776-9753-9fec885839cd | -2.6523 | -46.20921 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5278e246-3d89-3d8c-b1c1-2006ee7d4259 | -4.22074 | -48.65117 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f043509-0db4-3fbe-be7e-edd7a34d66e2 | -2.61678 | -46.1874 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b55708a-f142-3d2c-91b0-7a42295d9e6a | -3.52648 | -45.90427 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92e857ea-c58a-3ead-a8ed-c5ae3468c25b | -3.53781 | -50.51692 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0c21514-ca8d-3eb1-acdd-959f990f23d3 | -2.68214 | -46.86143 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8843b95-9a44-3b52-875d-57d9e97f6ecf | -2.1623 | -46.4124 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e2293ef-eff8-3449-b61a-43a0f8166c2e | -5.39862 | -42.77041 | 2024-11-17 04:06:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| aac91de1-dbef-33ff-a1b9-3b89d0fcb665 | -2.14853 | -46.554 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbb5314c-a059-3c13-a307-d7513a46a0dc | -4.84217 | -44.48676 | 2024-11-17 04:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c93c5b1e-1ddc-3a49-863c-b2bebf88e3d4 | -5.85924 | -46.45092 | 2024-11-17 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11b85e9b-3061-3e3e-8abc-d1eea7f2ec6e | -3.94736 | -46.71257 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 082289f8-24a7-384a-a0d4-b1536f4ca838 | -4.11733 | -40.54576 | 2024-11-17 04:06:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4081ca82-d611-3769-af4f-29b78fdc0e72 | -4.93416 | -40.84418 | 2024-11-17 04:06:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 47fff7ea-789f-3cf1-9cfa-f9065d3087ee | -3.65789 | -50.6096 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a940cddb-38fd-3b14-9f21-8110efd8c192 | -4.1701 | -48.71495 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49321665-fc7a-362c-b218-e22e8c7e3434 | -2.64932 | -46.20071 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d5a8351-ec40-3112-8a80-442b51f7bcda | -2.66858 | -46.21596 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README32.md)
