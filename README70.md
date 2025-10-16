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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf3b3d4e-86aa-338f-9bf2-c73ff2c9e891 | -3.02005 | -45.38139 | 2025-10-16 05:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9ce7787a-60f7-3815-9b95-135e4d245bb7 | -4.15686 | -46.79225 | 2025-10-16 05:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9928da6a-4589-326a-bebf-57e3aea354f1 | -3.3017 | -52.95055 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a042c91-7ce1-34a8-8777-b293e9cabd6f | -4.10115 | -48.02337 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 8126e538-466a-3fe6-ad0b-7a7b33b9c0f1 | -2.87615 | -50.7316 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d67ae7ea-2fb6-36be-bb62-c17aa59c8dad | -4.12462 | -50.71465 | 2025-10-16 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75fbd8c8-285b-335e-aa53-118d820ebb2e | -2.72859 | -48.59624 | 2025-10-16 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2795c380-f43a-3e9a-9a5d-b0446a21b910 | 1.81064 | -55.88276 | 2025-10-16 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 701ab104-e37a-35ed-bb4b-3827a16c26ba | -5.13549 | -43.35215 | 2025-10-16 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09764d5e-50f1-36da-8796-2a4c8a6e21f3 | -3.84919 | -41.57075 | 2025-10-16 05:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d207d506-a973-39ff-9f12-cd709159cbad | -2.26726 | -47.85513 | 2025-10-16 05:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 472ffcb3-311e-3906-a663-2c98af21d607 | -4.22511 | -48.35912 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92e63916-72a4-3e2f-a2d9-79185adaf016 | -3.88625 | -52.07182 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc17e45f-a96e-3558-83f2-ed475c75aa69 | 1.82355 | -55.74113 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a3852f3-a297-3207-8ea6-0aad0f424358 | -4.27875 | -48.59349 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4786dca4-4375-386e-a382-7bc3f10bb42c | 1.82302 | -55.76001 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 953a8ad9-571e-349a-bb81-5309bd4e63ad | -4.42234 | -42.88796 | 2025-10-16 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d697b86e-fd30-3b26-aab7-de62926b5ae2 | -4.28011 | -48.58437 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25109bd9-1a18-31cd-8555-b67faf7a1515 | 1.86559 | -55.6749 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dfc7b31-e10c-3acf-abdc-69f6c7883800 | -2.2817 | -48.36203 | 2025-10-16 05:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0ed81f2-14dc-376a-af91-71b178ef05ab | 1.05308 | -51.03195 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e9a14be-418a-325f-ab1e-42ec91cd5a7e | -3.27613 | -50.04451 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fed9c5c4-810a-3a9d-8a81-eb276258d9a8 | -3.05959 | -52.65623 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01e39d92-c7f5-310e-bb9d-c3f618d7de76 | -4.66762 | -44.10525 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| ebfe8253-7a80-3489-8e4d-9938fa6ae4af | -4.66893 | -44.09586 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1bfe0ea3-7ab1-3610-a4d4-9307444e5062 | -2.87228 | -50.731 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f4f89883-4355-320f-aa26-7d85dec53ee0 | -4.11206 | -48.01495 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 09d90a94-2185-3cd2-894f-b2ceea1d0b91 | -3.23012 | -43.45678 | 2025-10-16 05:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b862c893-2296-344c-95d0-370b520ed546 | -4.95799 | -45.10113 | 2025-10-16 05:06:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8348761-bd87-3f9a-9706-d6eb2600ff4c | -3.46464 | -51.06273 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf98fa79-1c62-352f-a51b-7767ac52aeaa | -1.89574 | -51.01139 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5efd6a39-67d8-3e12-ba16-5696be8cf42d | -3.65206 | -51.75188 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b685674-a696-35f8-a04e-2e7bc53e4451 | -4.71758 | -46.16129 | 2025-10-16 05:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8a29e7a-7a7a-351f-822f-7731dfc4c4ed | -3.07374 | -49.50489 | 2025-10-16 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e61291f-ca1e-3207-8cae-abe879d44250 | 1.8953 | -55.88892 | 2025-10-16 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d97bd410-3d18-3806-a651-413f08bcd973 | -2.92551 | -48.30811 | 2025-10-16 05:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3406ee7-3e45-3bc5-9d4d-27374a672be4 | -2.92621 | -48.30354 | 2025-10-16 05:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26ae2d3f-edf9-3116-ac94-58b96d0c66b5 | -3.41579 | -51.47953 | 2025-10-16 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f01051c-2362-30cb-9533-25964458ffb1 | -3.88262 | -52.07127 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 392e81bc-f899-3c7b-95f0-6d0191897d4c | -3.27727 | -45.83892 | 2025-10-16 05:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc6fc278-f6e2-34d7-a0e7-a78208084051 | -3.22016 | -48.92928 | 2025-10-16 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93b1241d-8af1-3ecd-b4a4-85db9490254c | -3.05608 | -52.65569 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c899cec-9f38-39cc-b3cf-0ef0cb5c61aa | 1.78654 | -55.75066 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cde13cc-74ba-383a-94ab-8f99f9893977 | -4.66209 | -44.09949 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 132d2f68-dfd5-315e-ab8d-1eaba424ae59 | -1.11289 | -54.06787 | 2025-10-16 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5f809b2-1df9-326f-8d2b-4d458cbb69fb | -3.45487 | -50.0938 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f737ea04-e53c-34d6-b84e-92505c10cd9f | -3.53056 | -50.31019 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34f7e602-9e57-3d38-9020-48d6775232a4 | -5.13623 | -43.34687 | 2025-10-16 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94faa95a-aa10-3804-9e6a-c9a189b48b1a | -2.58864 | -51.34104 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c299f97-6606-3943-94d6-6f3fbfb8a87b | -4.918 | -45.98027 | 2025-10-16 05:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30f81889-4971-3fee-93e4-7c3da6e13ae1 | -2.89899 | -49.77372 | 2025-10-16 05:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 650fd58f-30dd-3acf-84e3-27f94af5e4bd | -3.27676 | -45.84234 | 2025-10-16 05:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 390b87c5-0b32-38fe-b82e-668402f86241 | -3.66417 | -50.27302 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 079427c4-6140-3d28-9a87-e640a8591b13 | -3.33296 | -50.10769 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0fd2f9c-3d01-3af5-b692-e9528efd1f1e | -3.52654 | -50.3096 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8b2a9b3-4b30-368d-b4f8-ed66797751b0 | 1.82817 | -55.77048 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f002f02-cb6c-354d-a564-a640ac5c8a65 | -3.07795 | -49.50554 | 2025-10-16 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be69f7de-8242-30f1-995d-2c385fff045e | 1.81844 | -55.75319 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a306c6a-9f82-3352-a902-2ef5c4da6767 | -3.01392 | -45.38423 | 2025-10-16 05:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2c198aaa-59de-351f-86b8-4496361127c7 | -3.34952 | -49.25484 | 2025-10-16 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a043b8ee-d086-3bd5-9440-dab84aeb92d2 | -2.69219 | -49.52243 | 2025-10-16 05:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2dff1a9-d3a8-384a-9c9e-6a68b6c51648 | -4.66142 | -44.10429 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 6caaf252-e17e-3b60-8405-16cc3ee29a7a | 1.86218 | -55.67544 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3378ecb4-75e8-31b2-a63a-84547e15a707 | 1.05385 | -51.1292 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3569d909-9bdd-35f6-8bdc-b6f2e9935afc | -4.17742 | -49.97652 | 2025-10-16 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b74aa223-110a-3526-bc1b-6af0dbc390c3 | -4.37491 | -43.41215 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7095c1cf-d7a7-315c-aa8a-fc41f87ddd8e | -3.51416 | -52.49437 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a53afa05-50b0-3aa0-9e83-43fa64a8e55b | -2.8791 | -54.23963 | 2025-10-16 05:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b76aaa86-2f14-3d9a-bc63-b8b821dbbcac | -1.48507 | -55.67998 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b8b378e-939d-3832-a8cf-bc849c3f8c18 | -4.12068 | -50.71405 | 2025-10-16 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5fa209a-c5a0-3019-a6bc-5a583be1d008 | -3.07749 | -51.17121 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a332630-66a6-36fe-95fa-1ead7a3c47c6 | -3.65574 | -51.75246 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b2b9b75-e5f0-36c3-a30b-4b4483a7a07b | -2.59912 | -51.34715 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd8227f-14d5-303d-ad6f-654b07fd6612 | -4.7181 | -46.1577 | 2025-10-16 05:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 631441ce-050f-3234-942f-7ea9e5fd2f40 | -3.84156 | -44.54933 | 2025-10-16 05:06:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee8a9e1e-d73d-37c6-aab9-6071c2b440aa | 1.82586 | -55.7558 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afd5d73d-5253-3fe2-8a3c-6e10a3f83a81 | 1.0567 | -51.03139 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0a0832f-2368-38d7-a8de-b6b0979adc7e | -2.95414 | -48.58607 | 2025-10-16 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b056f3a-48f7-34bc-9370-9743e51e48c9 | -4.17519 | -50.40325 | 2025-10-16 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35296a1f-c8ab-3817-a1d3-98145c517b21 | -4.66907 | -44.10402 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 33dbb510-fbf2-3e97-8e5a-a259c2ca785c | -3.41871 | -50.25105 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7afef8e7-54e5-3435-95d3-da9c5de362ec | -3.41032 | -52.88092 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 122cc6ed-95a0-3083-9ee1-1286f06f1b88 | -1.11676 | -54.06491 | 2025-10-16 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b388a9cf-eed9-35a1-9524-9fcfb2154bcb | 1.0604 | -51.12396 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92e3ed3b-dfc5-3731-b6fd-f1f35ee36e8d | -3.09668 | -50.38485 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9474f9b-cd9e-312f-9b2a-0f210b38bb66 | -3.12668 | -50.21295 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| add71b8c-363f-313f-8cd6-b7f92048de14 | -4.67044 | -44.09469 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| eb6f726e-22aa-3255-ac16-a77c91276a10 | -4.10045 | -48.02816 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| f8741446-b8ed-3a55-ab30-4f5822d99985 | -1.99043 | -56.91896 | 2025-10-16 05:06:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 848dd1a4-30b3-35a3-9c68-e708813888eb | -4.35694 | -43.39436 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 096503d8-2099-357c-afd7-1de7baa7bfb1 | -3.68247 | -47.62722 | 2025-10-16 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29c56951-bda4-322e-9f0d-c70938daa9e8 | -2.2707 | -47.19133 | 2025-10-16 05:06:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af434f0b-dc17-3b67-8eb9-ccb2edc60f28 | -4.63873 | -43.13605 | 2025-10-16 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 27989e3e-6076-3831-8d75-3c7813a41219 | -4.67382 | -44.10613 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 392dc16b-0497-3d77-acd1-8383744bc1dc | -4.80771 | -43.2053 | 2025-10-16 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dea8026-c463-31b5-95e6-2d57da6ca7df | -4.42154 | -42.89371 | 2025-10-16 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22068b7f-b00f-3efb-ac28-b2adc4d5b231 | -1.11343 | -54.0644 | 2025-10-16 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d54893c-df4a-3cad-a700-3aa172a27b10 | -4.10187 | -48.01846 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| a6ef558f-f649-37fd-83ee-5f39e1913f31 | -4.28538 | -48.58037 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1461046f-038f-359e-bcad-1a20329bce6c | 1.82413 | -55.74479 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README71.md)
