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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dd25bee-3625-3281-81b3-0ab7b13aeea5 | -2.8523 | -45.862801 | 2024-10-27 00:14:40 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bcc19cd2-2e35-3cfd-bcfd-a2daa9035fdf | -2.7719 | -45.411999 | 2024-10-27 00:14:40 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81a5e750-c9c3-382b-b159-6dfbb107af7c | -2.7735 | -45.419102 | 2024-10-27 00:14:40 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c99ffe9-b110-37f4-8b4b-d720b0256b41 | -2.7722 | -45.965099 | 2024-10-27 00:14:42 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8686c9b8-29c0-3b7d-835f-87554ed76ce1 | -2.7739 | -45.9725 | 2024-10-27 00:14:42 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f41e01d0-b69d-3d2d-995e-85ab1c8d9473 | -2.5489 | -45.107101 | 2024-10-27 00:14:43 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e36fd18-673c-3b53-95ab-1fe89d166f71 | -2.5505 | -45.113998 | 2024-10-27 00:14:43 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a87a6e47-243b-3903-b3a4-bf057989d330 | -2.5391 | -45.109299 | 2024-10-27 00:14:43 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8405ce3-c495-3e5b-b189-13500d56a3fe | -2.5407 | -45.116199 | 2024-10-27 00:14:43 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 366156af-2290-353a-9f18-c545126c227f | -2.7363 | -45.9884 | 2024-10-27 00:14:43 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3debdcb4-7ae4-3585-84e2-69d9381111b7 | -2.5041 | -45.182899 | 2024-10-27 00:14:44 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87384cdc-2730-3574-94aa-3e527111e26d | -2.5057 | -45.189899 | 2024-10-27 00:14:44 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d168ecc-5782-3125-a741-a957de70a4e5 | -3.0804 | -47.7612 | 2024-10-27 00:14:44 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6dcae4e-f174-3810-94ea-fe7d5f4ed849 | -3.0823 | -47.7701 | 2024-10-27 00:14:44 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 752d68f4-d893-3d09-8e59-2eca47abbb6b | -3.1593 | -48.3484 | 2024-10-27 00:14:44 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be7635db-7227-3b4d-bdc2-01630ba4f385 | -3.2545 | -48.778099 | 2024-10-27 00:14:44 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef3a8ab-f2bb-3116-9e93-afe860181715 | -3.2568 | -48.788502 | 2024-10-27 00:14:44 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 489f0486-330c-3741-8ca8-968562236388 | -3.4349 | -50.0606 | 2024-10-27 00:14:46 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78e3a1ed-2a17-321a-8ced-c0fcb74540fa | -3.4377 | -50.0732 | 2024-10-27 00:14:46 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea02fd58-72ed-372b-890e-f47275bd0503 | -2.4631 | -45.826099 | 2024-10-27 00:14:47 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 318bbae2-390c-3091-aafd-fe7970396fc3 | -2.4648 | -45.833302 | 2024-10-27 00:14:47 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 83d16dff-4550-3be1-93a1-dfb4a454b87f | -2.4664 | -45.840599 | 2024-10-27 00:14:47 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7cec38f1-81a0-3260-90ac-3d1ca4bce751 | -2.8904 | -47.8307 | 2024-10-27 00:14:47 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44d37d55-0930-3e21-afdc-7159f336f195 | -2.8924 | -47.839699 | 2024-10-27 00:14:47 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ccb1def-a304-3ff8-a15b-7446ea00c483 | -2.8806 | -47.832802 | 2024-10-27 00:14:47 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad3d101-f832-3c69-b721-15edcabbb319 | -2.8826 | -47.841801 | 2024-10-27 00:14:47 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee92263b-711d-38d8-a66f-50272c8bda97 | -3.3988 | -50.269199 | 2024-10-27 00:14:47 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 348bba9f-8b1c-34a2-afd6-bf63157cde6e | -3.3302 | -50.096401 | 2024-10-27 00:14:48 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4920fdf9-e940-30f1-a9fd-8bb81280c2c3 | -3.3274 | -50.083801 | 2024-10-27 00:14:48 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d728d696-661a-33c2-906d-5ba04bca8c27 | -2.4392 | -46.178101 | 2024-10-27 00:14:48 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfd4432f-c4f1-333c-b742-ee9cd942314b | -2.4408 | -46.1856 | 2024-10-27 00:14:48 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ccd1cd8-235f-3aad-9593-48a2ed0a160c | -3.2926 | -50.064999 | 2024-10-27 00:14:48 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 009733ab-bdf0-3299-bf61-4e51bcd6ede6 | -2.3487 | -46.004299 | 2024-10-27 00:14:49 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d81fe42b-74af-3d04-b16c-b5c59bcd1653 | -2.3503 | -46.0116 | 2024-10-27 00:14:49 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 29d24697-7290-3e87-8fd4-e158475bde8e | -3.3135 | -50.206501 | 2024-10-27 00:14:49 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84b2e8ac-4a98-3474-8e49-0a05d576832b | -3.3163 | -50.219299 | 2024-10-27 00:14:49 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c41f89bc-81c0-37b5-96aa-71a6be65738b | -3.5543 | -51.396801 | 2024-10-27 00:14:49 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93577bf9-229c-3c92-852f-9a362e34bfb3 | -3.3342 | -50.7192 | 2024-10-27 00:14:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21944689-192d-3edd-acba-afb5887d15da | -2.3394 | -46.192299 | 2024-10-27 00:14:50 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef928033-83b0-3026-af1d-86e19b9408ab | -2.3411 | -46.199699 | 2024-10-27 00:14:50 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0a58ee8-0515-3e87-925c-2d262930f86e | -3.3373 | -50.733101 | 2024-10-27 00:14:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11ad84a2-0dd6-3a03-b9c8-c443ed666fe3 | -3.3245 | -50.721298 | 2024-10-27 00:14:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93770324-ffd4-3aa1-8e2a-b5b2241d16d2 | -3.3275 | -50.735199 | 2024-10-27 00:14:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5661b45-f0ed-3e89-9d5b-2dabdb45d296 | -2.1955 | -45.688499 | 2024-10-27 00:14:50 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 14530e1b-b88a-392f-9048-a984d401169c | -3.1977 | -50.191299 | 2024-10-27 00:14:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c231004-9c89-3a0e-ae2d-64946666d766 | -2.5495 | -47.315701 | 2024-10-27 00:14:51 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54f81c16-6cbe-3a3d-9d88-c1da92893f22 | -2.5514 | -47.324001 | 2024-10-27 00:14:51 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ea68e9-9562-316c-9625-f4326df58311 | -2.2622 | -46.123699 | 2024-10-27 00:14:51 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f88510e4-f712-3b13-9d8f-4112bd0a515e | -3.2514 | -50.621601 | 2024-10-27 00:14:51 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a20ae035-ec36-3186-bd86-8578fd539dc1 | -2.3133 | -46.627201 | 2024-10-27 00:14:52 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9602c77c-9111-38ce-b054-f6f5a124eb37 | -2.315 | -46.634899 | 2024-10-27 00:14:52 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e473997f-725d-3721-aef1-71772a46cda2 | -2.3167 | -46.642601 | 2024-10-27 00:14:52 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddbb6aa2-6638-3df0-9291-88c5573fdc24 | -2.3185 | -46.650398 | 2024-10-27 00:14:52 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fff907f4-c52c-3f4d-9781-e081f0d9c851 | -2.3069 | -46.644798 | 2024-10-27 00:14:52 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6703d72-2d2a-3374-866a-92f488501e7d | -2.7517 | -48.684799 | 2024-10-27 00:14:52 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6cc185e-5c59-3e30-80c5-4ad3d940176b | -2.7539 | -48.694801 | 2024-10-27 00:14:52 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7de4cee2-8595-3baa-9462-53e33f1fd1b4 | -2.7561 | -48.704899 | 2024-10-27 00:14:52 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4906d03a-ef0b-35af-9b86-7f0e65ea5792 | -3.1129 | -50.3172 | 2024-10-27 00:14:52 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd650e3-7ccc-38d4-9ebb-e2a3e9498c9f | -3.1158 | -50.3302 | 2024-10-27 00:14:52 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddcfa8c6-74ba-3491-a989-06c22197c760 | -2.3595 | -46.9716 | 2024-10-27 00:14:52 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf8bb03-7a01-342f-b191-92e41447d031 | -2.3613 | -46.979599 | 2024-10-27 00:14:52 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e9af853-9c43-3b22-99da-74c93e09a737 | -2.72 | -48.681198 | 2024-10-27 00:14:53 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3f062e-a0d8-331d-b2b5-364ad437189f | -2.7223 | -48.6912 | 2024-10-27 00:14:53 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64dd6420-64ff-3e52-87aa-cdabe56fa306 | -2.8281 | -49.214199 | 2024-10-27 00:14:53 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a1d389f-b9e8-334e-8b3a-97bfe8457c30 | -2.8305 | -49.224998 | 2024-10-27 00:14:53 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e020b40-950e-3699-8701-22cf36e95733 | -2.8329 | -49.235901 | 2024-10-27 00:14:53 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e87b868-c58f-3b10-8255-1ad9638fca12 | -2.8183 | -49.216301 | 2024-10-27 00:14:53 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f939b64-a06a-3566-b043-d3d461d98e5c | -2.8207 | -49.2272 | 2024-10-27 00:14:53 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7927f21-86b4-34ed-8363-c109c0c6b654 | -2.8231 | -49.237999 | 2024-10-27 00:14:53 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f466b2-70c3-3f4f-9504-bdc798e84183 | -2.8109 | -49.229301 | 2024-10-27 00:14:53 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fabc5f6a-441d-3971-b21f-a58306064432 | -2.8549 | -49.427799 | 2024-10-27 00:14:53 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19ec0b71-6b7c-3077-9f5e-ed427047e523 | -2.6381 | -48.5434 | 2024-10-27 00:14:54 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c0a59fc-f270-3d91-b9d4-e7031a3fa979 | -2.7961 | -49.301102 | 2024-10-27 00:14:54 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50c7e7a2-e25c-35af-8bca-215e365deb87 | -2.4932 | -48.030998 | 2024-10-27 00:14:54 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a71cdc2-3c21-3bfd-b35c-f7e4aef574d2 | -2.4953 | -48.0401 | 2024-10-27 00:14:54 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b7cf4e0-e734-3054-8f93-0c3454b0515d | -2.4834 | -48.0331 | 2024-10-27 00:14:54 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76ea0440-293e-3ba4-a59f-ec47d5e633c9 | -2.4855 | -48.042198 | 2024-10-27 00:14:54 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69623c31-0e1b-3f76-8af3-ab489e6883d7 | -3.5054 | -52.7118 | 2024-10-27 00:14:54 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdee586c-b7e4-3261-8d8b-2a26db80485d | -3.2367 | -51.530499 | 2024-10-27 00:14:55 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61309ded-048a-3345-ae40-952354f2b55f | -2.367 | -47.649601 | 2024-10-27 00:14:55 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcbb4bc5-cb84-3f2c-aa61-06d343938c40 | -2.369 | -47.658199 | 2024-10-27 00:14:55 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8245d489-021d-3518-bfe5-3e5543cc8d90 | -2.3572 | -47.651699 | 2024-10-27 00:14:55 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebcad4af-e035-36fc-8112-b8e577ed1abd | -2.3592 | -47.6604 | 2024-10-27 00:14:55 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1894ae1-478a-37cb-9a44-cf47500db104 | -2.934 | -50.248199 | 2024-10-27 00:14:55 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9225b21-99c0-3354-8629-95a46f113bcb | -2.9214 | -50.237598 | 2024-10-27 00:14:55 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a4ba3ee-a007-3e50-8c06-e3632fdec28a | -2.9242 | -50.250301 | 2024-10-27 00:14:55 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04cffdf4-85d8-320f-8c0d-89640b795125 | -2.927 | -50.263 | 2024-10-27 00:14:55 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb2285b8-168d-3844-a523-1ff48548472a | -2.7008 | -49.287399 | 2024-10-27 00:14:55 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d71b008-460e-33b1-804d-3c3692070659 | -2.7032 | -49.298302 | 2024-10-27 00:14:55 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5fd0ad6-647b-32de-ae39-4a85e7faf58c | -2.7056 | -49.3092 | 2024-10-27 00:14:55 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f32abb7d-8b4d-3f16-b7ba-43ddb875302f | -2.9116 | -50.2397 | 2024-10-27 00:14:55 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99f34cfb-041b-3449-baf5-166170ba87bc | -2.9144 | -50.252499 | 2024-10-27 00:14:55 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 411d5ffd-0167-30ae-b5d6-7cceb31cae70 | -2.9172 | -50.265202 | 2024-10-27 00:14:55 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e91977d-9bc0-36e5-a6b9-a8e2c3e6597c | -2.691 | -49.2896 | 2024-10-27 00:14:55 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db750708-b0b2-3da6-a743-fe0acac0bd29 | -2.6934 | -49.300499 | 2024-10-27 00:14:55 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f8d1eb3-7904-3b3c-be3b-13fc37006395 | -2.6958 | -49.311401 | 2024-10-27 00:14:55 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f14e4746-965e-3cf6-b24d-2c40f728f737 | -2.9047 | -50.254601 | 2024-10-27 00:14:55 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0741fdff-af84-3bf5-b9cd-e2e9bcd09b4c | -2.652 | -49.252399 | 2024-10-27 00:14:56 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22e391a6-0974-3f50-81f4-4bb6b65c168c | -2.6544 | -49.263199 | 2024-10-27 00:14:56 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc649a28-5f8a-3a9d-855f-87213e0fbc92 | -3.088 | -51.224899 | 2024-10-27 00:14:56 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
