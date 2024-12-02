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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b1cd735-b2e9-3a91-af65-4bd41674ad97 | -1.82124 | -46.6461 | 2024-12-02 04:48:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 784825b9-799f-38e1-8f2a-86d8306f4322 | -1.91764 | -52.66059 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a5b7690-bb42-3b33-8e55-3353e5f8ffb9 | -2.87687 | -46.79679 | 2024-12-02 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3db07973-2ab8-33ad-9288-11759a1ea1ca | -4.07821 | -49.0552 | 2024-12-02 04:48:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c642c14-cb47-3cdd-a1f4-72a564da57b0 | -1.34403 | -51.38569 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58b35d5a-df60-347d-8eb0-e0e228cc6e1b | -2.45784 | -53.96551 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c03e3544-a6a3-3092-94b0-e6a0024b9751 | -1.58901 | -52.28984 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c694653-441c-3fd9-a533-18c1dad055e9 | -1.27101 | -51.63451 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0173655c-5bfe-3a01-bbdf-7d1cba203760 | -1.29447 | -51.37468 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abad5983-58e4-3b1a-abb7-30171c097a48 | -0.98974 | -53.67543 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b2a7039-b3fa-3691-9725-78432ff85db0 | -3.92973 | -46.71924 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5954f484-fa69-351e-9870-f9c3d20fc978 | -2.61145 | -53.99591 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f00084c-4bd0-3880-8696-4a6cc2ecb310 | -2.86886 | -53.98055 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb1b3587-afeb-3fb2-9583-aa5da1b34828 | -1.49821 | -51.93832 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70a907c2-7afd-3bb6-9394-ea5c4004ab36 | -3.08902 | -46.55733 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3cca165-7fc0-343f-99b6-6ad125888013 | -1.91975 | -53.00763 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab25d629-7779-3ab2-892d-9c10cdc8032a | -1.74623 | -52.65181 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6641f19b-ca27-3cd0-b269-72429ad45181 | -3.9036 | -49.74174 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b50f5359-73fe-3067-aabc-94e68cddaf21 | -2.45686 | -54.01651 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f62b2ec-b01f-3f35-a4b4-59d010b83048 | -2.78215 | -52.99816 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3722cfe4-989f-39dd-8cb5-e4d67493048e | -4.28881 | -49.94493 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9091913f-e7f8-3b4e-a3cc-2b92e427ae81 | -2.55507 | -46.56593 | 2024-12-02 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d599485f-8226-3856-a4d1-4f88428316ca | -3.19388 | -46.5798 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b907c07-b40c-3aa9-a875-644e3f177976 | -3.06976 | -53.68918 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| de274137-b244-3ab1-8f11-a1c1a0180e26 | -3.13982 | -53.84448 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 637ff755-8fef-39b7-bf07-eeda26d6360b | -3.1649 | -54.30103 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4866b40-da61-38aa-8712-11d16325b4e5 | -1.38983 | -53.55829 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcf708b6-9e80-3065-a1a7-fac18a85c5de | -1.68836 | -46.19207 | 2024-12-02 04:48:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4da1c88-734f-37bb-8612-0940b56f8824 | 1.1071 | -56.00407 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3fd6fd3-3305-3666-8aba-064d679c6c40 | -3.7534 | -54.51791 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef7521d5-f49b-3bad-abaf-ce1f76f16afd | -3.15544 | -50.62431 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23c8a721-089a-320a-8653-4b88ad42d961 | -3.18794 | -49.24856 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12a0b0a1-4787-3765-8938-dbde8e5f86ec | -1.4972 | -55.85265 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3220fba5-0949-3286-bf07-a30d07106cb0 | -4.63905 | -46.8969 | 2024-12-02 04:48:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb2844c0-4c0b-3b3a-a42e-03e12c40d14a | -4.26757 | -50.84996 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f45c19d6-252e-36d9-a098-359fd6b5176c | -4.2065 | -50.67652 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28c64536-fe60-3dd7-9ab0-402504d2bb80 | -3.25081 | -51.14055 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 444bcef4-1cfe-394a-978d-17f0ada49cad | -2.30497 | -53.8956 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5b46e4d-a13c-3fef-8333-9f97a8e667b2 | -2.75008 | -51.75402 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab752ef1-d65b-37a4-8f34-76d9b8f973f4 | -0.31447 | -51.77408 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14c5b520-b1ff-3793-849b-0cf34496a0c3 | -4.19193 | -50.68163 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 28f24a3b-18aa-3a32-afb8-404bdc0302ff | -3.646 | -52.62289 | 2024-12-02 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48606151-e0a8-3ccc-bad9-af50a98b4be3 | -1.18514 | -53.70132 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00b28eb0-dfff-3a38-b7f9-9f822253b0c6 | -2.36037 | -54.48515 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7c96fe2-c014-381e-baa7-e8291e992485 | -2.38861 | -54.35428 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dc6bcb9-64aa-30c4-bf5f-a6aada85f543 | -1.09975 | -53.59891 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbc23a1b-c428-3295-adce-a4f97c3ce1cf | -1.57161 | -55.33964 | 2024-12-02 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab34360b-6ab0-3894-82ed-29662b2ca5eb | -4.19473 | -50.68572 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eb813e8-ebd7-34fb-b674-10cb147c85b5 | -4.32779 | -48.09449 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40ed3c5a-2dfb-349f-9720-9159b970e161 | -2.61779 | -54.00085 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aa5ab94-4d00-3582-995a-d85cbd5161be | -0.61871 | -51.69842 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7813a9fc-1412-3713-8f4d-5d9726c6b0d3 | -2.44256 | -53.68808 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a34c8851-61d7-3642-8ef1-e77c1e286272 | -1.45201 | -55.19309 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 98eb599e-9159-3b07-af92-48fa624512c7 | -3.16824 | -46.28951 | 2024-12-02 04:48:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 746ffd78-e182-37a0-b456-64e7cf36dfef | -2.41793 | -54.01435 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1214951b-700a-35b1-a9fc-779286517e50 | -3.49837 | -50.31954 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4e73aea-2f44-3b57-be16-f66c58ce5f10 | -4.5376 | -45.70056 | 2024-12-02 04:48:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37eed7bd-b880-380d-92cf-16caaab752df | -3.14096 | -45.98943 | 2024-12-02 04:48:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a78da373-ed14-38b4-8d18-1532e757c5bb | -1.99558 | -51.17471 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54ea78c4-379c-3518-9311-8e4f6a23a2ab | -2.56912 | -53.3974 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f6536ebb-fca9-3503-bd47-a03fbad99f75 | -1.18696 | -52.12352 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84bfff54-96ab-30f0-b335-f96cac0fd3f9 | -2.30728 | -51.26595 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21f5dbe2-57b5-3f1d-8090-1133ba6c5d5f | -2.86703 | -53.99196 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 026ab855-c647-3a40-ba5c-337341e84b0b | -1.78871 | -53.72374 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96d2b5f0-4129-3ef7-acda-5e7bded96559 | -3.25429 | -50.55645 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc3008fe-a0bc-34b2-bcbb-fcaf2c2c063a | -4.18857 | -50.68111 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fbf377ce-3df3-3674-a178-03d8d1632e0b | -2.15908 | -46.07994 | 2024-12-02 04:48:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba220415-9050-35a6-9073-e04253148e4c | -2.70731 | -52.00441 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ab1b6bb-eaf3-3b67-b2e8-8df4e42e8b30 | -5.61006 | -43.47379 | 2024-12-02 04:48:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42f37849-d54f-3df6-aea0-e7bd01b5c4f7 | -1.72926 | -45.61045 | 2024-12-02 04:48:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0fca03a0-690d-32ba-bc77-288b8c12d5f9 | -1.99095 | -53.28583 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d44eb4ac-26ed-3c4f-9a90-560576007786 | -1.59977 | -51.27127 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3ca653e-14d0-39c1-bb68-ba015f9ea3b1 | -3.26023 | -54.11817 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d221d632-aa54-3474-bc20-8ccebada35b8 | -3.33487 | -53.54169 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a660d7f8-3362-3c09-8eec-c2fc6a1e2e70 | -1.34903 | -55.19896 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8df924fb-d974-3957-afd0-9b20b30d2ee2 | -3.03033 | -54.18596 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6c40ae8-fa05-3d4b-a088-d77cd0d22fb4 | -2.95334 | -49.45424 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc8ba8a9-029b-31a5-9bf6-902b78009547 | -2.9943 | -51.0649 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aba8a6c6-4160-3788-831b-00bda4819727 | -2.8512 | -53.94309 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5b39d19-6e2a-3f92-bdb6-05f7365748de | -3.62165 | -52.49829 | 2024-12-02 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1edb428c-9a41-3aa7-91cd-cf9ddfa3fa69 | -3.33752 | -53.37104 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31c513fd-646f-399a-bc24-ff5f4c87c14b | -1.09543 | -53.64862 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f766f63b-63e4-3288-8add-64cfb28a9527 | -1.01802 | -51.72867 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f7c579c-d046-3a50-90d6-56c48531bd2c | 1.13335 | -55.98526 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11ca3a55-97b1-37e1-b14b-a6c83daada84 | -2.4654 | -53.96279 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83d5a504-c9c3-35b5-ab85-91407b14f90f | -1.26116 | -53.37752 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57411572-8c47-371a-8b79-f183ef821271 | -1.67762 | -52.52195 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 115f08d3-33f4-3435-9507-74a0f3a580c8 | -1.62142 | -53.89357 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9110a22-e340-37b9-aee1-7313f2562fdd | -2.56822 | -54.33983 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7288fe5e-ca87-3f7b-977f-2a450bbac699 | -3.05907 | -48.52905 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d39b29e1-203c-3042-bca1-b79dfd9e4aa5 | -2.35932 | -53.85655 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 546fd773-0a5e-366d-bc30-bc64e224b258 | -2.41244 | -53.8572 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4ebad8f-9408-37a0-b8d2-6c4eae29db7d | -5.12318 | -43.20953 | 2024-12-02 04:48:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 02a3df47-243a-350f-b7dd-968577a844c4 | -3.15584 | -51.1187 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68319ab9-99b4-39e8-a3b3-ef2b82c8e629 | -1.59869 | -51.27814 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8601b6c7-6e43-3cf3-b766-5cad22282d23 | -2.85334 | -54.0995 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7de80c2-6f21-3718-bf23-be6b88479a9d | 0.86246 | -59.68727 | 2024-12-02 04:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cadba05-040e-3c7e-bbe5-373d7347f0d9 | -3.26151 | -53.82843 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d317d7f8-fb4f-3eae-a814-6dd628957782 | -2.46103 | -46.5802 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baf8184f-e2c3-3d42-af46-7ae5ebfd43f1 | -0.92513 | -47.61689 | 2024-12-02 04:48:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
