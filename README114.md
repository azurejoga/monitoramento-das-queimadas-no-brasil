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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75c63b7a-bad7-39c8-a0c8-d27269f75e2d | -3.9493 | -48.16407 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 688b05b0-6406-37f0-bbf5-d439b54f45f4 | -2.98203 | -50.30251 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85076b1f-1c3b-3aa1-aaa5-6c9d29d105b7 | -3.7799 | -45.187 | 2024-11-10 04:38:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55fc3c8f-28ed-36c2-90a0-6214c4013c31 | -5.24054 | -46.66147 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff9dec08-94b6-3abb-9216-3fcb8645e6ee | -5.64018 | -46.97387 | 2024-11-10 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bb578e5-a0e6-39f0-b753-f6bd9ff58bca | -2.61315 | -49.23783 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d128c4f-e203-36e6-a449-39e4afc114ad | -3.24473 | -50.27614 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88a7c0e1-a597-3727-bd69-6f91b9077240 | -3.89122 | -51.20568 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ecae4d7e-0496-3f8f-bf7c-fb92178157f0 | -3.05835 | -51.38319 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 950596fd-abd9-3f0c-bc82-b433a5f0cce3 | -1.67376 | -55.17566 | 2024-11-10 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd65e709-3940-333f-9452-e4e5ff24eceb | -5.41196 | -46.41264 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13aee24e-738a-3af3-a23e-93727a8fe50c | -3.10274 | -49.41434 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98af6cc2-1173-3109-8351-ed07c80c24c5 | -3.81662 | -50.78808 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7c81f29-d04c-3ee1-bdc7-2a33b1a8fd5f | -3.19844 | -48.66291 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc5940bd-29d3-3785-aa70-80f10acc2f51 | -3.81799 | -49.85805 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99c10eaf-fc9b-37ac-824e-f91f9c4a16a7 | -3.10284 | -45.78121 | 2024-11-10 04:38:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8405802b-51d9-3cb6-a54a-1afdbba77ae4 | -2.66245 | -49.84901 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc3253e0-72aa-3f7c-85b2-1c303b7a41a4 | -2.38695 | -54.09663 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16ba6529-72a5-36df-8047-2e36d7459e6f | -5.97274 | -45.36594 | 2024-11-10 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c1cce5eb-5c2b-3129-b774-e036ec42d771 | -2.60229 | -49.81391 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4d2ac69-c467-38f1-b735-2bc0afef0f9c | -3.48962 | -54.58669 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8880535-f22e-33bb-9dd8-19b3c51c5eb4 | -3.7801 | -47.74029 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f50ddd3-5a22-33f3-a71c-8dc32c682548 | -1.47022 | -55.64801 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2c201fbe-0fe6-3eaa-a6bb-5ed3aea96538 | -3.88539 | -49.91923 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caa22310-8ed6-3f3f-832c-7e8e83129fc2 | -6.2405 | -45.684 | 2024-11-10 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86ae2ce2-a3d2-347a-a431-63919d83d323 | -2.66234 | -48.49758 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 917d5f43-2c4c-33c2-a015-25635270e26c | -3.35757 | -53.41259 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0a90b6ec-b870-3ff5-9892-df1e446b6ea4 | -2.86372 | -50.32225 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f45b86d7-1f0d-3ff6-84fe-0cab108433c0 | -2.62301 | -51.91396 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06db7ba8-4033-3141-adf0-c0d4a79607df | -2.06593 | -53.28079 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 481d4412-d479-38a4-a5dc-967b2432ffd7 | -4.05 | -48.25807 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a977241b-258c-305a-9917-d4e7fa3ba94e | -2.73416 | -49.17801 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e644c64-f8fa-3cc9-8d29-a8774fc26af3 | -3.2498 | -45.99283 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a48c90b-8d9f-3624-8556-c3aa213df1f6 | -1.48862 | -55.43853 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 79312309-2e45-32c1-9121-3f55fb179581 | -3.11402 | -50.15547 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 017c51f1-5320-3b66-9948-4ae413ac4654 | -2.16042 | -53.65197 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5955e6d3-a1c0-3fcd-8283-89348a23a4eb | -4.8939 | -48.61721 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d96c271e-40fd-3365-81ce-4cf1ad365d11 | -2.8323 | -46.63808 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3079dcf5-c9f0-3631-9fc2-df805f244709 | -3.04239 | -49.54529 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ff68b46-a2ac-3b9b-8f45-de56bead644e | -4.1243 | -46.92652 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac4d5c39-dc1f-375d-aabe-cfaeea2d7240 | -3.58637 | -50.23627 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c361df2-ddb7-3822-95fb-ac11a38c321d | -8.41147 | -44.13005 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43527f4a-f21d-3883-bef4-d8ca208fda4e | -3.94481 | -48.14914 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| bb271597-031d-3ce0-a90e-fccb012f22eb | -7.43708 | -39.76709 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1fac47ba-6a09-3b84-abb0-8657108b2154 | -3.5096 | -51.66972 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f0b398d2-7b94-3bee-bc0b-fe019c1922fc | -5.23994 | -46.26603 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96f52d00-c911-3d1d-b311-c07f1ab86b61 | -5.68859 | -45.17699 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2b58dee-324d-3c5e-8438-7c06694abc74 | -2.9136 | -49.52166 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c655531c-972c-3a35-a2c5-6428ca2c40fe | -4.07349 | -48.32568 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f96d80a-9736-3d92-9382-164dbd301d1e | -8.85074 | -47.694 | 2024-11-10 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39a41eb2-3c4d-358f-9420-a3cf486e6e43 | -4.607 | -48.69964 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7bad58b-759a-3837-9138-fa7ac5bfd51f | -3.23111 | -50.27397 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2b46086f-10d9-31f2-ace4-f3c67288493a | -3.86768 | -50.07327 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e93a0b05-c73a-3e33-a1a8-674349a2d60b | -4.08739 | -42.93182 | 2024-11-10 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbca0ee7-5467-3306-b5d2-484a5c3a50ba | -3.71219 | -50.43446 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f7a0841-ec55-314d-8225-3f0db11de8f6 | -2.71996 | -47.97972 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67681e00-a9c0-38de-a229-43713c0bfe16 | -7.22731 | -44.99534 | 2024-11-10 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24fd274f-aba2-3d4d-b071-629953f53290 | -3.54071 | -49.26187 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5d960db-6e87-37ec-9fa2-4807c80301e8 | -8.38845 | -44.11056 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7ae8955-fd40-3509-bf18-aede436ed75e | -2.45901 | -50.27506 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc3172f3-7b49-312e-8d68-06579fd59902 | -2.60774 | -48.33054 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81d6ea48-67d4-3025-85be-c3752da633ba | -5.23857 | -48.15956 | 2024-11-10 04:38:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17fed760-136f-3f79-9f86-6ce343bc14bc | -3.70664 | -50.15869 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4b188bf-2772-3042-b2d7-760933d28ac7 | -2.21799 | -50.56375 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dde9e73-c622-3c16-839d-60f3112265ff | -1.93251 | -52.17254 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16acbe9c-926f-381c-9050-4a353ac518b3 | -2.92184 | -49.36137 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d75d44a5-3c23-3bb2-9558-6940dc0f2e4a | -4.75972 | -48.93276 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d9fd170-b378-3220-b131-563ef8c423b7 | -3.60666 | -48.94583 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f86e26f4-665d-3422-af85-9ea61f6105ac | -2.98944 | -50.29989 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bfc30c3-af17-37a2-a24b-ddda6c415f02 | -5.47176 | -44.61609 | 2024-11-10 04:38:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb01ac10-9bb0-3282-95f9-6bb78e460869 | -3.79552 | -46.92974 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 426127ae-b1bb-3a63-8907-2be6d4f12514 | -2.46743 | -51.15224 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c925fdcb-9b63-3feb-bbeb-26622c672418 | -3.4567 | -47.66496 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f31eff9c-c4a9-3330-b5d8-2cbbfe5f3ca7 | -2.65848 | -48.50051 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a54122e4-15ac-3f2a-ac67-c819316ea539 | -4.64409 | -48.74417 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34d14917-e3e0-3cb6-bcdf-de346bf8de9d | -3.70325 | -50.15816 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62893b2b-e2c4-3ccf-b2da-cccf2bd3c624 | -3.69221 | -45.81039 | 2024-11-10 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a259e082-9900-3eb4-9d1e-5a2e311a8606 | -3.63306 | -51.08327 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b074049-6b8f-3927-a323-ffe29689a81a | -4.52176 | -45.69659 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50dedf2e-a70c-311f-b62c-2601aced0540 | -2.61841 | -54.39503 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 13041618-a272-32ed-a428-2e8a5a9a9cf6 | -7.22639 | -44.99765 | 2024-11-10 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eeb9dd3d-0d7c-374f-bb3a-72b8f7e76a1c | -4.89113 | -48.61324 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e6dabb1-1fea-3edc-93c8-2f812a1986a3 | -4.1192 | -48.5064 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 79aede1e-75ab-377b-8ff2-924a14458fab | -4.92147 | -47.63563 | 2024-11-10 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a38e6909-5c85-3333-bc08-83cd296abcaa | -3.1854 | -50.58406 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f82e1d6-0007-3a93-8d57-b4e6436771f7 | -4.75263 | -48.58813 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 714b4d18-c4f5-3a12-a9c0-473fc9c3c979 | -3.80783 | -49.94365 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7271bf1d-ba6c-394a-b048-29e3d8e06227 | -1.64425 | -54.43848 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be66446b-845b-341a-b2ab-e23e6c3812db | -2.9494 | -52.57373 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 51571015-884e-3a98-a2dd-b338f0adf85b | -3.29066 | -50.23082 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0108a94b-d79c-330e-927b-9856e479b3ce | -3.14663 | -45.96209 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e200e9fe-83b0-3a82-8af7-da648e7a63e2 | -3.43621 | -50.30167 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5760e877-a7e1-3d01-ad01-2da9aea5b5d8 | -2.67369 | -49.88749 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c9048ac2-73d7-3b95-9610-de56457d40bb | -5.24404 | -46.662 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9e80e40-5bd7-33b2-ab73-055585161877 | -1.5251 | -54.99456 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e15c4c27-796d-379b-8d8c-d4d03570e240 | -5.69306 | -45.17295 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c5f5f48-1197-32f2-b2f7-dddfe17d5c11 | -2.85225 | -49.2256 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9e3b678-1019-34fd-a845-b57cb271c01c | -2.31897 | -50.67591 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2cd97889-ef4f-3623-876c-bf36fec5d2b8 | -2.87677 | -49.40807 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f1ba4189-2cab-3dd7-a02c-92b29beb3921 | -3.24878 | -49.58862 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README115.md)
