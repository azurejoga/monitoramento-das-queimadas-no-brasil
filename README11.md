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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0308901e-19a6-36cc-a951-beb11c86c462 | -4.0212 | -46.955601 | 2024-11-11 00:51:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc90b5a-f22d-3cc9-b525-71898a8c8370 | -3.0253 | -54.210701 | 2024-11-11 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef8a1b11-3505-30b4-ab31-4178bb247de4 | -13.8003 | -51.080101 | 2024-11-11 00:51:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da846470-c836-374d-b1a9-15dde5b7c974 | -3.1355 | -54.469299 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16997756-bd17-306c-a313-76962648a418 | -3.2834 | -53.669102 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a80a58f-d181-38c7-b463-8d9b392340bc | -2.2315 | -53.666599 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbf8c045-6caf-3aa4-8f17-ea6e75863853 | -3.7581 | -51.818001 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b4f9d33-4fb0-32cf-8e95-3cc66a41b43b | -3.6889 | -45.2509 | 2024-11-11 00:51:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74532e25-92cc-3150-9a6b-58fc333f128d | -2.5991 | -51.712399 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ecaf48d-ee52-3e46-876e-c11a6a37246d | -3.2505 | -46.484001 | 2024-11-11 00:51:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79a30805-808e-3632-a9e1-43d88dbebe1e | -0.953 | -52.451401 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1112e37a-c4e0-33ef-8c71-c95e06841bb6 | -2.7714 | -49.373001 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 627f0123-fc44-3009-9e9c-62c5cabff06f | -1.2361 | -51.752102 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dce355e1-749a-3a07-a2b4-5eb12ca24b1a | -3.2358 | -50.309898 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d810f93-f85e-3db5-b307-38fc32405129 | -2.812 | -53.9977 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edb5bed6-ec52-39e2-9add-6ec20fb6662f | -3.524 | -49.949799 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cc471eb-e8b9-3095-951b-4b1b3a63f82c | -1.6341 | -52.5425 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48c47759-e4e7-3802-8106-0fdc63acdefd | -1.2423 | -51.7794 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 917cbcbe-5720-399e-befe-91c6e1e216f7 | -3.6207 | -54.111301 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab19592e-6e67-3dd2-a7c3-ace33d863b77 | -2.7696 | -49.365299 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1ba8195-448b-363a-85ea-88f035a15e84 | -2.7508 | -49.3288 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c836231f-b601-394a-811e-5622c3dc624b | -2.6091 | -54.011398 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f2877b3-fa28-3615-af13-9da485d91ccf | -3.2736 | -53.671299 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b48e22d-3a61-390b-ac38-602e3d3adc07 | -3.8474 | -55.983398 | 2024-11-11 00:51:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 496ba268-8cdd-3268-80ea-43a046be1e58 | -3.0428 | -50.323399 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bb4d7e7-ab03-3484-9122-cd6c1fb7ae28 | -2.9494 | -49.517899 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02dffef9-e753-3eb7-a570-1741e1c55783 | -1.656 | -52.638 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d8b60d4-67db-366d-8fc4-b6c8f1e55b84 | -2.3105 | -50.681999 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a452761c-badb-34e1-9de0-2ae74b5bed43 | -2.8953 | -51.7892 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7577b51-861e-3b78-8d8b-15599753d048 | -2.9336 | -49.3606 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 547c99e1-a77e-3905-8936-88e5eaa1e209 | -2.8384 | -53.344398 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f886822f-98de-3560-9a9c-fd5e0fcb357f | -2.9112 | -49.486599 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e7b0e9e-bd76-3d81-ae21-e69046de0a43 | -3.0681 | -49.3624 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7653891d-48f6-37a1-95c0-66e6fbcb5df5 | -3.0168 | -50.970901 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a35eb9cf-60ee-300a-a335-364d16821dfb | -2.4762 | -53.9711 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1affe80-31b2-3f18-a6c7-8b5ce9f95ebb | -3.2251 | -53.050999 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ace1fa15-df11-3d59-8f7e-a08d786ab5b6 | -2.3318 | -53.879902 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e026f342-9b79-3dd3-bc79-0ead3b23f3c5 | -2.606 | -49.817001 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40ce2aa9-78ce-3e6f-8351-b57f9047792d | -3.7616 | -49.594601 | 2024-11-11 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ae04cb-9477-3b61-81e7-7c4a96dc8025 | -2.9753 | -45.841999 | 2024-11-11 00:51:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be809b68-c42b-385b-9898-4fa56a8b956c | -2.3954 | -53.8428 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e5b616d-29df-3665-b939-91dfd18ccfd1 | -1.213 | -53.631199 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8cabedb-afaf-3fc3-887d-f298462f3dae | -3.1372 | -54.4771 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38233fdf-746d-3beb-a639-11b5f914c6c9 | -2.9086 | -49.3419 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 059038ab-9728-3a74-bb55-b34b7d5c47bb | -2.2201 | -53.661499 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbc27a9b-d128-36cb-bfe1-8083091937be | -3.5082 | -53.797001 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12fa7aa6-0b68-36ff-a5cf-bfd47306b84d | -2.374 | -50.330898 | 2024-11-11 00:51:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1e3075c-1d07-3f6c-9899-708d490eda02 | -2.1686 | -46.698299 | 2024-11-11 00:51:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e024abe-92c3-3b73-8b17-eb675398e053 | -3.0153 | -54.030899 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7e86fcb-b2ad-30c6-94f2-56ad36766956 | -1.5055 | -52.206799 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4adf2e5f-0d1c-30bb-a9d5-1c431cd32063 | -3.5159 | -49.959301 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50533fc9-331d-365e-99f9-a2640986b3e3 | -3.097 | -53.7104 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6198025e-b818-37f9-9aa9-e5b039a02a14 | -3.3566 | -53.401901 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 483ab643-85fd-3954-a953-6618d96218ae | -3.8862 | -50.087898 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db17a7a9-b6b1-3e40-9738-449efe03dcc3 | -2.1743 | -53.686798 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b17a93a-0291-35e3-9c83-92236f308885 | -2.9416 | -49.3507 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a4cb819-8895-32cb-8f30-9405956b7b8c | -2.6412 | -49.523602 | 2024-11-11 00:51:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8597cd79-3a47-3a5b-9a46-dbe23b211209 | -2.2217 | -53.668701 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b201b4f6-73be-37f6-bf82-e2f2f75d440d | -2.2681 | -50.676701 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b22f6420-3fd2-316c-b3c0-88d06f24a839 | -2.3054 | -53.809299 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a84a393-ccb4-3614-b3aa-48d5d177c58c | -3.6511 | -54.654999 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5374a38-0f6d-3701-af6c-ddc13f129a3b | -3.1084 | -53.7155 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac549f20-d6a4-3b3d-85c4-03fc76ea7ec4 | -1.3912 | -52.0681 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40bf0cb6-d331-3430-916b-2e20c488f9f2 | -3.1488 | -54.4827 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5916b1ae-46ff-3dda-9f77-5ce5d5109be3 | 0.4655 | -50.9445 | 2024-11-11 00:51:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c93aad99-0723-39df-8e15-5e9c57999ed2 | -2.0948 | -46.515301 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e533014d-3792-33d9-b22e-dae633446712 | -3.2374 | -50.4958 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 470a2e1f-82cf-3689-a2ab-af13c8191743 | -1.5029 | -52.150299 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce9b4d2-77a1-37a3-ae7d-c2e68d4e1671 | -3.5529 | -53.494801 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67984a9a-24ff-387e-98f0-448bcd6f206a | -2.3471 | -48.522598 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a01cdb3c-b8a5-3e1b-8c20-e0766bcab582 | -3.2436 | -51.553902 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33842150-c910-3952-ad72-60480fd121ee | -2.1842 | -53.684601 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d9c7d3-6adb-31b9-a03e-ce89419a5513 | -1.7099 | -52.468399 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4f6e0e-b14a-3280-ab5d-10ab5826720c | -2.7861 | -49.2141 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 070ab479-4057-3c3b-9c54-fc427c6adcce | -3.0911 | -51.070099 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1fb3df7-4e67-3233-81f4-bbfa71df6812 | -2.2611 | -53.750801 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67701e86-3c49-310d-bd68-3348122cef55 | -2.5776 | -48.139801 | 2024-11-11 00:51:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dba84150-8b4c-311e-a438-50f82df02fe4 | -2.5671 | -50.676201 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 876dbeda-82a6-39bd-a681-f223dc5f16a2 | -4.2123 | -48.6045 | 2024-11-11 00:51:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4e5bb4-6120-359c-accb-bd17ba4198ae | -2.7309 | -51.747299 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d84da032-a298-36f3-ae3a-ff465f7eff1f | -3.2406 | -46.310902 | 2024-11-11 00:51:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f111d3d5-03d1-332d-aeb2-88775b9d298b | -2.9024 | -49.3596 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0401b15-6655-374f-8e67-bd49157b79f2 | -3.1067 | -54.297001 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c99cc907-3cc4-3db6-93a3-cb2ae175ca73 | 0.4622 | -50.9589 | 2024-11-11 00:51:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| de68d113-682f-32b6-8d33-6f86832b0a89 | -1.4637 | -51.485401 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1edc26d-59e5-300d-8dbb-ac77c18852f2 | -2.6347 | -49.8964 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 982d80fc-2586-3daa-b1fa-d1a702472f13 | -3.1982 | -50.280899 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 523041bf-aa4e-39d0-abb3-bfa2a424fb41 | -2.4383 | -51.9557 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 137984b7-0fb4-3f13-90ee-592770630f42 | -3.3908 | -50.131901 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90d66d61-50fb-3aef-8397-69bb307d2bd5 | -2.2463 | -53.7313 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0114595e-2543-35a0-bd85-99872cb96e4b | -1.1998 | -53.7085 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd4c397d-8b66-348d-878b-dec7f45b3206 | -2.9262 | -51.4744 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0e5f7fd-1ce1-392a-af2b-7155da06eec6 | -2.922 | -49.355099 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54f7eae9-0131-3463-84c0-2a2121f43be8 | -2.6539 | -46.7925 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeeb1771-6af9-3828-ae34-205140a5b503 | -2.4134 | -46.5135 | 2024-11-11 00:51:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0215961b-da67-341a-903c-31b8f522adf2 | -17.590799 | -57.538502 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2efb5721-12f5-38ff-88aa-c54226a882cd | -3.1001 | -49.411701 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0918af7d-d918-3b98-b785-c4a7861e3a48 | -2.4639 | -53.690601 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdc6bad1-6f22-3497-9c66-1080a04fe04c | -1.1459 | -53.6535 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae1bf5b5-2353-3fef-a707-06948fb40089 | -2.9477 | -49.5103 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
