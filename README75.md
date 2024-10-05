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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcdd7d45-eec0-334e-a099-5a3a39b334d7 | -18.66714 | -57.28075 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 7abb59f1-4ae5-3074-ab74-268f129de686 | -18.66613 | -57.28525 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| c2d70808-cd41-32cc-9ccd-4282c9e447a6 | -18.66511 | -57.28976 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f5e58cdc-84f7-387b-84c3-9aee76400b03 | -18.665 | -57.27747 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 1c18b90f-7ee8-3834-89b2-8379f65cdc3c | -18.66401 | -57.28199 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 46942a1f-f188-3d8f-a3b0-4a09422d2ad9 | -18.66302 | -57.28651 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 86d894c4-52ac-3a69-b2fe-baafb44a9bcd | -18.66203 | -57.29104 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7be6693e-c924-3074-8a8c-d4285eb939c7 | -18.65912 | -57.276 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| c3c2371d-de1a-353b-a695-70588ba80828 | -18.65812 | -57.28053 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 9f19685e-fda1-36c2-9b20-335050063708 | -18.65713 | -57.28504 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 7498a87e-e701-3ae4-a7ac-4c1a7462f594 | -18.65614 | -57.28957 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a6add1c6-aff8-3824-84ac-8520af18f4e8 | -18.65224 | -57.27905 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6fdaf540-36a7-3144-988e-e954055f8a02 | -18.65125 | -57.28356 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 783e752b-0fb1-3339-8f30-4ea210c82935 | -15.92836 | -43.93517 | 2024-10-05 04:17:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ca22edc7-c092-3aeb-9e02-b786c23e4709 | -15.75147 | -43.84209 | 2024-10-05 04:17:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1951650e-9443-3538-89d5-c3be8eef14d1 | -21.92473 | -48.41132 | 2024-10-05 04:17:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be293857-595a-3d18-a19e-75cc47edcb4e | -21.89647 | -48.475 | 2024-10-05 04:17:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64743508-d907-325e-8ac3-16388817facb | -21.85168 | -48.36487 | 2024-10-05 04:17:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e90fb719-9b74-3654-b615-8995d9655458 | -21.84853 | -48.42508 | 2024-10-05 04:17:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a832bd6-7d1d-35e9-baa4-5209de65143b | -21.84786 | -48.42902 | 2024-10-05 04:17:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47225bc5-a211-3c92-9ec6-30ebbcdd2f46 | -21.84512 | -48.42442 | 2024-10-05 04:17:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1285eadb-d6b1-353a-bd60-9bba9b2287b5 | -21.84445 | -48.42836 | 2024-10-05 04:17:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e7908bd-7346-3846-a44d-bf62581f4be3 | -21.81158 | -48.74624 | 2024-10-05 04:17:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d3986c64-06e8-336d-8bb1-3d60967ca906 | -21.8109 | -48.75025 | 2024-10-05 04:17:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5ad75433-a7e1-316e-8ef0-759d144c1adb | -21.80814 | -48.74556 | 2024-10-05 04:17:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3f7b49df-1c08-3121-a46b-304dadd7980c | -21.80745 | -48.74957 | 2024-10-05 04:17:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b8f44f56-2b50-39d8-b427-33ce10c2b212 | -21.80676 | -48.75358 | 2024-10-05 04:17:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75c646d5-aa66-32bd-887e-e5d6c9a25b59 | -21.8047 | -48.74487 | 2024-10-05 04:17:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cc658eb-6657-3b18-aac1-4a0f8f09b546 | -21.80401 | -48.74888 | 2024-10-05 04:17:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e152093-a42d-3c0d-a5b7-2fd8b6a99f8d | -21.79989 | -48.75217 | 2024-10-05 04:17:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9440d1b-268c-3e05-89fa-fca96ada05de | -21.50941 | -48.06971 | 2024-10-05 04:17:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37de73f5-a85b-36bb-b28b-33506e8d788b | -21.33186 | -48.88638 | 2024-10-05 04:17:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7a70b9d-9ee0-3b84-9755-8e49cb61bced | -21.33115 | -48.89049 | 2024-10-05 04:17:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0fc83f6-e031-339d-ba84-cd42bb71f4bc | -21.14166 | -48.44958 | 2024-10-05 04:17:00 | NPP-375D | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8777391d-f2a4-3d2e-98f1-439d11ed5d38 | -20.72131 | -54.87746 | 2024-10-05 04:17:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3000998-c068-3449-afac-16b37470cf0b | -19.15113 | -48.22459 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6bf45422-eb3b-345b-8220-5dfd43c4ade0 | -19.14926 | -48.22316 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eaa3df4-982a-3caa-ab89-27ca0e27fa5c | -19.14857 | -48.22713 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3127e761-04d6-3cd5-a18a-d8f18a512bda | -19.14767 | -48.22394 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10f3bdf5-48fe-37e3-aa31-8177b3656553 | -19.13314 | -48.22538 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| deae4d9e-fac7-387b-91f5-36d7ab93ec97 | -19.09235 | -48.23411 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7249bad-5fc2-3c7d-8e03-526e53c6c6a9 | -19.09026 | -48.2254 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c73d0104-6660-3782-abf6-74145957fa45 | -19.08957 | -48.22942 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 51ee5e55-5686-3c57-ada5-cb3208199a85 | -19.08889 | -48.23344 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ad4ed32-7325-35ad-bb24-9f08154e6aea | -19.0882 | -48.23746 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3fd7567-7fd6-38ce-85de-f6941bcadea4 | -19.08474 | -48.23679 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6039e063-59fb-329b-aff3-df106a19f06a | -19.08197 | -48.23209 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| da429de8-c67e-35ba-b641-bbaf3f930680 | -19.08128 | -48.23611 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 986b47a6-9e6f-33dc-a376-c8c22090694d | -19.0806 | -48.24012 | 2024-10-05 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 662f9fc9-1f22-3d0f-b828-2e59a6bfa98c | -18.88925 | -54.53116 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 332f1182-25a5-395d-b008-0e2895c0e326 | -18.88795 | -54.53748 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1b887b78-39da-3a61-b056-0431f763f958 | -18.88389 | -54.48156 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 28dccec3-5115-3067-8449-31b8173bda40 | -18.88272 | -54.48724 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 651462e4-5248-3e39-bdea-24bef8142a53 | -18.88006 | -54.47506 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 604a91c1-0a24-3042-bc23-8a99be70a0da | -18.8794 | -54.52851 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db435676-328f-39ff-9c7b-2f67fcce2583 | -18.878 | -54.53531 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07ab084d-aba7-3c0e-9efe-66c0742a6e2d | -18.8766 | -54.54209 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fe893fe-a269-3c02-b383-88aed570d829 | -18.87317 | -54.53351 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14f33caa-bd3f-3c07-83b5-e5fe45952637 | -18.86168 | -54.5388 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3a7de573-bd2f-385a-98d9-ad6b613f6d72 | -18.86035 | -54.5452 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| de827eab-6bff-39df-954a-94a66f00faee | -18.86032 | -54.52028 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bdfd2352-4f5f-37b4-838f-5a21bafea45d | -18.85908 | -54.52626 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c03bdf7d-dbd6-39a3-b888-8c59470bf9ec | -18.85553 | -54.4679 | 2024-10-05 04:17:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7a69e6b-6c11-318e-86be-deac7c81d344 | -18.85548 | -54.46867 | 2024-10-05 04:17:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 458850d6-9d6c-3887-a1dd-e80ce0e881a4 | -18.85449 | -54.52481 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| de15aed0-4217-3e26-955e-4bef65d63252 | -18.85406 | -54.5254 | 2024-10-05 04:17:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0286c346-8962-33a4-a192-54384772fff3 | -18.85067 | -54.46633 | 2024-10-05 04:17:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b673b6f-e61d-36e2-b617-163bfcbc20f6 | -18.85063 | -54.46708 | 2024-10-05 04:17:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b9ef429-67fc-3f4a-bd48-9eb2f0f18e86 | -18.84952 | -54.47203 | 2024-10-05 04:17:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3e8e4cb-be86-3ac4-bf0f-f3a0e8374ccd | -18.84944 | -54.47278 | 2024-10-05 04:17:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9987dcaa-e0ee-3e64-a6ee-468dd7706dcb | -18.81851 | -53.7616 | 2024-10-05 04:17:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6362b0b-b293-3e45-b3d5-6874ba4e0cdb | -18.81741 | -53.76708 | 2024-10-05 04:17:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7453423-d906-39d2-8d0e-ddac48130b71 | -18.78502 | -52.63342 | 2024-10-05 04:17:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 349d3b40-194f-304f-8f62-36a1622c41bc | -18.50417 | -52.84657 | 2024-10-05 04:17:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3ca1ba0e-a51c-3087-a4ef-84062930ba57 | -18.49967 | -52.84562 | 2024-10-05 04:17:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 4092e7aa-8ee8-398e-acce-6376a98a33f1 | -18.49895 | -52.77692 | 2024-10-05 04:17:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 70585e33-42ee-3d35-bc97-13fd92f0e12c | -18.49875 | -52.85036 | 2024-10-05 04:17:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| bbe2a223-8c57-3459-b256-4b7cc9a52bb0 | -18.49784 | -52.8551 | 2024-10-05 04:17:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8d8031d-d360-33cd-a268-34b06052f360 | -18.49449 | -52.77594 | 2024-10-05 04:17:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a70136c-3bbe-3a69-9d4f-bc77957c43d4 | -18.49426 | -52.84937 | 2024-10-05 04:17:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 8593b19f-a266-3397-96b9-a77f5eb28136 | -18.49357 | -52.78063 | 2024-10-05 04:17:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a3cb5fef-17a5-375f-bfbc-89c5d5254770 | -18.49335 | -52.85408 | 2024-10-05 04:17:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| f4ad4162-dad6-3471-9a41-e87316dfbea3 | -18.49244 | -52.8588 | 2024-10-05 04:17:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| a6d94e92-1498-3047-b7ab-bb1d3650c46f | -18.48887 | -52.85301 | 2024-10-05 04:17:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 9b689c68-9be2-3ffe-9c20-c0dafeb726da | -18.42334 | -49.76022 | 2024-10-05 04:17:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| c37f3cd9-a965-3f28-b759-7c41a38dc572 | -18.42251 | -49.7649 | 2024-10-05 04:17:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| e827f3ab-f3a5-38fd-876d-825399016dfc | -18.4196 | -49.75945 | 2024-10-05 04:17:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 5831c510-4364-319a-923f-b1146c69264d | -18.41877 | -49.76413 | 2024-10-05 04:17:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| baa5ecc3-d04a-3784-af6a-46eb55628f79 | -17.90932 | -48.91233 | 2024-10-05 04:17:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 931c0ee5-d0da-30cd-8d74-9cae60a8138c | -17.53975 | -49.23173 | 2024-10-05 04:17:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 061f10b7-1803-391e-94bd-e2b4c05e83e2 | -17.3325 | -53.1973 | 2024-10-05 04:17:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c50dba5e-8847-33ae-9fd9-4aa47f09e4fb | -17.13552 | -51.72678 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8bc4d003-2728-3b1d-b526-77a602467da8 | -17.13471 | -51.73103 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0949b663-f595-3503-bd51-f56541ec5089 | -15.20428 | -47.50074 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b30d9ee9-ec12-3c70-91fb-56e8d0d7867e | -16.74481 | -49.36983 | 2024-10-05 04:17:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c38e4b0-92df-342e-99eb-6cbf07e290a1 | -16.42181 | -49.92304 | 2024-10-05 04:17:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16cac469-5f5d-3b5e-8c40-46a67762f0ae | -16.24076 | -48.01988 | 2024-10-05 04:17:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 739bd659-52e8-3aeb-84c6-38637b2141e7 | -16.1708 | -49.26279 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b8f5d0dc-faa2-3b2b-b44b-1974380e0961 | -16.16996 | -49.26751 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f7ba2a2-5f75-378e-b2cb-a9a511487522 | -16.16701 | -49.26229 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |


[Clique aqui para ver as próximas entradas](README76.md)
