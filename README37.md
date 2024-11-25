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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 603c5e22-3b45-3777-bcd0-05df2b3cb893 | -5.13454 | -46.19631 | 2024-11-25 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00851868-cdd4-3a9c-b6d7-8f754a23ec15 | -1.77279 | -53.6326 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b79d59aa-a9db-3563-871c-da5c1d7a4f75 | -0.10477 | -51.74317 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0efa42f-df47-3555-8e26-1f5ed097e2fb | -1.76966 | -52.70998 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc1e10f8-e3bb-39c4-9c8e-a1d8bfbdca4a | -0.93474 | -51.62582 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 791a6bf0-4844-322a-ba7d-11c436cbaf61 | -0.68856 | -51.87995 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47582ca7-e8dd-3c69-85b1-1512d1e27855 | -2.74579 | -54.03051 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ff65e13-5949-38d0-adfc-a675395a214f | -1.31104 | -51.74485 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24f01852-3040-39fc-9f78-04d0312d5307 | -2.85268 | -53.99718 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 463d5f34-b66f-3459-a6b3-107e03666241 | -1.19613 | -51.76727 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cedad4b0-7ab0-3825-b0e4-0a554a18c4af | -2.18294 | -53.8 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 860be804-6529-3cb9-a3ec-e7aafb4e5af0 | -2.7492 | -54.07394 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 174b4c63-da31-37cb-93e3-384167657ba1 | -2.82168 | -54.08521 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6554d32-2cbb-347b-be96-513b22fd3a5a | -4.15295 | -53.66949 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83a7ef7b-e39e-3748-a1f9-5432f48421b5 | -1.11775 | -53.38781 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e299a0c-8ef3-3f20-8da1-dd753beb5df1 | -2.28722 | -51.32805 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de9e462a-b2d7-3a5f-9a7e-927b57a1444a | -2.01435 | -51.17805 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 207a94aa-097c-3248-a573-9421cad8210e | -0.92928 | -52.65282 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b1f892d-8ecf-396f-b191-2990e77b5cc2 | -3.03451 | -53.72401 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 540327b6-7463-3a29-905b-93fec59cbcea | -1.51183 | -51.1514 | 2024-11-25 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a25c12a-b01a-3d12-9137-994f094d17ac | -0.98132 | -51.71273 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0bfc764-cfcf-3f8e-9dbb-15fce3813ba2 | -3.47198 | -50.25526 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da7bac20-5342-35dc-9050-e0c14ac27a73 | -3.49651 | -50.45789 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 484174cd-485d-3fba-bc31-e96d433f80b9 | -1.6755 | -53.19997 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afd11570-da0c-347e-988c-1f346ade6a5a | -1.60539 | -52.26891 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c6445c8-aa11-367d-a578-bfba9d06a557 | -4.09702 | -51.07381 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9096c0c4-f3de-358c-8563-74b38f3a47c4 | -1.08514 | -53.63847 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c2ea1b8-3939-34df-a005-0a6c9709c1b6 | -3.77323 | -52.40672 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77e3172a-9fea-3fb7-93c7-3e99e5bef9e1 | -0.36439 | -51.54843 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5538c68f-c436-3de1-9329-b9f077aebf4e | -2.71789 | -46.28527 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 967d89ad-57b4-351d-875f-671abd7b0d39 | -2.80943 | -54.07615 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f888c34-caee-370b-b492-a50ead5712a8 | -4.24106 | -48.59488 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1116968-52d4-31b0-b722-2c5d4e6534fc | -3.93405 | -48.92879 | 2024-11-25 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c89eb4e1-71e0-3603-87c6-d64d4da25eaa | -3.70857 | -50.43687 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a069b48-441e-33ec-83ab-ed8891e75870 | -3.63824 | -51.14887 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e12c0037-e56c-3399-95e1-a842ea1da58d | -3.70784 | -47.12079 | 2024-11-25 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39470c5a-3862-3d15-9cc9-e0bbfe7c1044 | -3.66446 | -51.71986 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ef497b0-d9d3-3d54-9174-49431eb0c794 | -2.76247 | -54.03312 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf1478dc-df11-3257-813f-cdcb982a923f | -3.2355 | -54.10009 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d456b8c5-a1fa-3a27-bccd-6aea19651c2a | -1.05684 | -53.64466 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b36b7d6-13b4-33ab-bb3c-24b7ab3b25b3 | -3.22624 | -53.62282 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1331f064-028f-351d-8365-b268bcd15fd3 | -0.99167 | -47.22109 | 2024-11-25 04:55:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f37cd0b3-5453-345c-95cc-8c977b48f4de | -2.83271 | -54.01548 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99a89dae-0c6b-3e49-92f4-00e9fd3cfc9e | -1.98716 | -53.13181 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4d3bf9b-e136-3c20-9781-921d7ab80c3e | -1.15397 | -53.78197 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b74db8f8-90bf-3472-831e-12875494cd7a | -4.41776 | -49.70421 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e19807a-bdcf-383e-90d7-ec3edc61442d | -2.83883 | -54.02 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 081b02ce-1b94-3bd5-823c-c5b49931d65d | -0.75679 | -51.74286 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 543499c9-1f08-3fa8-b31e-b6d678fe9c59 | -0.39002 | -51.45063 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e7b97f3-9475-31a0-9a24-7eb071824e95 | -0.91402 | -51.64804 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df558b5c-654c-3b8f-9939-72b3beaabc65 | -3.50955 | -53.82323 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9860b797-05af-397a-9103-649fa3f4ab4f | -3.28472 | -53.01346 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c30073e-4dec-3ac1-91f5-8cc9406ad4e3 | -3.7782 | -51.90891 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d6d2125-c455-3a0a-a021-acbe601a988c | -2.36736 | -53.85707 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3df74288-937e-3195-a3c0-cc7ee5041cef | -3.38596 | -50.73384 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f85c84a5-edcd-39eb-9b57-7cd5d16a6063 | -3.74369 | -51.83635 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22e371ec-2af2-37c0-b98a-8bc4fe4cf524 | -1.48936 | -52.44654 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fb9084b-f788-31eb-b570-81d7413215b0 | -3.89698 | -52.13017 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dacef284-21b2-3f2d-8524-fc706b98bde8 | -3.09893 | -54.00401 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbae3be4-bddf-3c00-aef3-4538b2388d06 | 1.41443 | -55.89511 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 675325f0-c849-31d2-9b01-a7ed15a581ab | -4.02747 | -54.63421 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bad5cc00-f5a5-33a0-b2a6-591f8008e2cc | -1.44449 | -52.45021 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfcf29a4-25fa-3158-9cc8-e600659a8601 | -1.25213 | -51.7832 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cff20402-c19b-38ea-b81b-bc89d4e0ee37 | -1.44486 | -52.57779 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73d09a82-4355-3036-aaae-cd52e28fef0a | -0.74115 | -51.95249 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebde1c44-691d-3f0b-80b8-3bb725c6e26a | -3.09478 | -51.32438 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ccce6fe-8269-3838-a959-d87d0607e5a0 | -3.32042 | -54.09523 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c254caed-d763-3db4-b78a-f264365fb2a9 | -2.82885 | -54.03987 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2232d39d-c1d6-3801-b524-36a089483e96 | -3.2292 | -53.06868 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb44faf6-80f0-3c4f-848d-2655907ccb1a | -3.2551 | -54.21398 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b458c23-325b-38a3-ba13-62fb45d921d3 | -1.78246 | -52.73672 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 990c3b51-7abc-3a62-bc47-734de5de9290 | -4.20583 | -48.1213 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcfe3783-e422-38c7-9bc0-f6808197c85f | -3.21922 | -53.92661 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07168e5d-15ef-3507-ad8e-1293998131c3 | -1.31721 | -51.74944 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 714dc2e0-8b53-345c-a458-fea7d3d63de6 | -1.25157 | -51.78673 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06bd953c-7eb5-3083-b1b6-07a18af4e4cb | -3.79196 | -49.76608 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 975c784b-5be3-319c-8a46-53f41eff2037 | -2.76864 | -54.05909 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3eacca7-035f-3412-9ca2-88c5911406c0 | -2.57465 | -53.97537 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 472c6dd6-950e-3243-a13a-0b503962cdc4 | -0.79769 | -51.81051 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 365c5d8f-a2e4-3e5d-8096-4fc5a4ba985d | -4.32653 | -46.82985 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d8a9f2e-5a1e-3a29-a4ae-a3e1f583616b | -2.96237 | -53.92211 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e68c4b6-0c9a-39db-baf9-a284533f3f76 | -3.10878 | -53.70368 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10546bcd-960a-3653-be65-89d047760e21 | -2.62715 | -51.76725 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8b073cf-1dd4-3b97-bf1c-5ad86ca3e91f | -2.85543 | -53.97977 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06e520e8-7f72-3f87-a4a5-c57fac0fde78 | -2.67173 | -51.83672 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c1631ef-1eff-3d9a-b9e9-a78a66170d43 | -2.90249 | -51.5679 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e1d16a5-b28e-3f52-91dc-a925976af9e5 | -1.12928 | -51.67723 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5951bac-fc8e-31a7-a183-642b7f8db785 | -2.61244 | -53.97414 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e157834-34dd-327e-98af-01fe7feb86cc | -1.35832 | -51.3743 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bc2c8c0c-b44d-3f88-bc5f-8903c5299ee5 | -2.8283 | -54.04336 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff7308b5-ded8-34c7-9d4e-a938b3ffb0c5 | -4.70525 | -49.63977 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24a0be12-deaf-3c0e-8136-2c4f2a753e94 | -2.02005 | -51.18652 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0f2e824-6c0c-3df1-93f1-a53892c24db4 | 1.84091 | -55.94274 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a59c8f0a-a67e-3a8a-9b70-0e7708be0909 | -2.80438 | -54.02175 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b5f866e-b089-3b13-9027-02f389b33186 | -3.95422 | -50.85579 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d957f0b8-aa47-3d16-ab69-f737ab1ea05a | -2.79608 | -54.07407 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 362f38a1-3dbb-3119-81ca-d0a891b168c2 | -3.2806 | -53.83665 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24814b95-6f08-3c68-8813-2261f57aeb71 | -2.3313 | -53.86926 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 99577148-387f-385a-abb7-3936672d91b8 | -0.11923 | -51.65192 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11871de5-d761-3104-8454-8a41d07261ca | -1.28963 | -51.74187 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README38.md)
