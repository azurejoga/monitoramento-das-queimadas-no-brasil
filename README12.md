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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b188dd28-7326-38f1-9947-ff0f0845c8bb | -3.82888 | -50.23678 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 737e5e68-f29c-3e2b-9756-181eda74bf0e | -3.69055 | -50.96439 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7cfa1307-c1f8-3abd-82a3-b0d3437b79bb | -4.05402 | -44.77004 | 2024-11-17 01:04:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 041e5abb-ea39-3171-b676-ef87ed186b17 | -2.67937 | -52.43577 | 2024-11-17 01:04:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| df6ce58a-cb1d-3655-81c4-fb55cef36cac | -0.83303 | -52.34162 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b8ffbbd-c638-3c32-a671-0c91fcb20930 | -3.95259 | -46.707 | 2024-11-17 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 04131cef-6032-38ae-9e31-e6be3bb93bbf | -2.93104 | -48.32363 | 2024-11-17 01:04:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 21cafb05-b166-3220-914e-6e63fca9e813 | -3.52661 | -50.51455 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b4ff5e61-ad49-3bb5-adf3-8462cb6392bb | -4.58504 | -48.01906 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4c849c6a-e5fe-36f0-9051-979a016cf997 | -2.95768 | -45.79537 | 2024-11-17 01:04:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 4d92d2c5-5623-3b73-bdeb-cfc958a526ea | -1.32867 | -51.86625 | 2024-11-17 01:04:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c1f6ebee-27e7-3c04-ac6e-f59b10045c57 | -2.83141 | -46.67001 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| fc60c2e5-05e0-3fb7-b3f3-fe88a980a61e | -1.2055 | -51.7733 | 2024-11-17 01:04:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1799d242-99dd-386d-bb43-2be7df42fa93 | -1.86816 | -50.05525 | 2024-11-17 01:04:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b6996f5-77fa-3163-b0c1-126551b38fb8 | -4.21427 | -50.69135 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59af29da-5817-3315-965d-a100d26a8637 | -3.86736 | -51.16986 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cd1faea8-a7b7-37d3-bce4-80355c8d611d | -3.04439 | -45.75891 | 2024-11-17 01:04:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ed4c9b75-8d08-362d-a1bd-18a67734bda9 | -3.48388 | -53.9809 | 2024-11-17 01:04:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f9de60d0-7b01-3da3-97a9-f1e2aa4a5566 | -1.55483 | -53.09534 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7840bd7c-44a4-3fe0-b90f-824eec8bf3e1 | -2.83903 | -45.49433 | 2024-11-17 01:04:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 161.6 |
| 80908cc9-e688-3a68-bda4-cdaaaf57f685 | -0.93231 | -51.7313 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ad906e0e-f8e6-3c3f-b041-acf5712ac91a | -1.52713 | -53.56236 | 2024-11-17 01:04:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b38c84ea-f5df-3523-9568-b9a92620fb22 | -3.17703 | -46.60058 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5dd33391-4cdb-31f4-89be-ca5ec90f54c3 | -0.8683 | -52.25847 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ed1fe131-d302-32c0-bde6-3218ace8e15d | -2.81043 | -52.92045 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 94b67fb3-020b-353a-a042-e11bda3f7b3d | -3.72157 | -51.84925 | 2024-11-17 01:04:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adb9654d-5a5a-3425-85cd-eeb108cff322 | -2.60782 | -51.78947 | 2024-11-17 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9764d84d-89e0-39b7-9115-f0495cd2185c | -2.62542 | -46.03873 | 2024-11-17 01:04:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 41.3 |
| b49055d7-f749-3787-a530-2f733a64cda5 | -2.92693 | -45.40821 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 253f992c-ff98-316f-947b-54ec6b245ba2 | -1.64128 | -52.51977 | 2024-11-17 01:04:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b45ddda8-33f5-31cd-ae3f-ed769cd8f17b | -2.57793 | -47.56216 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| d373db39-5cf3-35de-954d-605cb37569f0 | -2.65076 | -46.21533 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f539b946-f485-36d7-a831-50f3d0696e7a | -3.02073 | -47.44213 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 43b3339b-ce3f-3c01-9c9b-bfe03600a808 | -0.11507 | -51.62352 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 27.1 |
| a6c03930-4d71-3ab4-9dde-54616e49ab93 | -3.53693 | -50.45842 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2188ac7c-02c4-3a5f-a36b-5658feb1e84a | -2.82946 | -46.66122 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a4976f56-074a-30fe-8532-d4d237bc2117 | -0.90579 | -51.73504 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| af714298-5606-3fb2-8735-4b7adf2cb61f | -3.35185 | -46.06269 | 2024-11-17 01:04:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 34cb1b84-7921-3956-8c95-4061aeae0c0d | -1.52578 | -53.55255 | 2024-11-17 01:04:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f476dc59-6425-3ad2-961d-37f39993c1d3 | -4.29899 | -48.09016 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6b29b3d3-29cd-33cd-b449-2da8161160eb | -4.56381 | -48.01091 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| d51efea1-cdab-371f-95d7-40e81f1829cb | -1.2056 | -52.03361 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ec080151-3b42-336e-8943-dae733fe19b5 | -0.88545 | -51.79792 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0275013f-d578-34b7-ae28-e8803339803e | -3.52595 | -50.24913 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 378.2 |
| 32f11a45-d0b0-335a-b946-9f898e5508dc | -0.11262 | -51.6059 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1871d0af-e8cb-3ec7-83a7-8d0a9d49e947 | -3.34243 | -53.30735 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 1e01b81f-34b8-3833-a2a7-e60634702196 | -1.40465 | -51.0887 | 2024-11-17 01:04:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 15011d9f-eab6-3166-bb18-4639f19dfb89 | -1.19703 | -52.04961 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 25a082a7-e04a-3e16-88c3-c99184f9596d | -4.59014 | -49.62557 | 2024-11-17 01:04:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5222e8ab-ced7-34ae-ba84-1517db1fde53 | -0.89499 | -51.93104 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0c95a595-d7f5-316e-8c65-11c429d8a61a | -3.62578 | -43.15829 | 2024-11-17 01:04:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 34c58081-8175-34f4-93dd-cb36c129cfd9 | -2.17476 | -49.10566 | 2024-11-17 01:04:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c809e3a1-5dc2-3d56-8320-a49e979d1c9c | -1.83169 | -46.59459 | 2024-11-17 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 51c236ef-8cbd-3af4-8f59-6c6203bab1ec | -4.73152 | -46.84487 | 2024-11-17 01:04:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| ea9ef71c-45b6-365b-b572-b432e5337f7d | -2.57971 | -47.57479 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| d6e5da57-cfe1-34f9-98c8-57011eac1574 | -3.32582 | -52.7793 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 40478771-acba-307c-b86f-1ceafff08a61 | -3.61411 | -50.15039 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 64f837cb-7cab-3463-87a4-c9e1514d25bb | -2.93233 | -45.41917 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 924279cf-9ce2-365f-9710-99cc2bf79879 | -5.32008 | -45.45326 | 2024-11-17 01:04:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 40ecf7d9-edfd-3726-bbf7-a09f66797cc2 | -1.84572 | -46.53018 | 2024-11-17 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ce89e947-a45e-3983-abad-5291381845ba | -0.10255 | -51.59834 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2b398c4b-bbc2-3482-84bd-6077277c3ca4 | -2.68555 | -46.21002 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8cb383b2-aa2f-36d6-a011-4f47886a7ca2 | -0.99501 | -51.77928 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3c07dc2f-ce11-33b2-a577-57b158cabca8 | 1.39763 | -50.67522 | 2024-11-17 01:04:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e522c7b3-f40a-30cc-be68-ab10b1a5f6ed | -3.02982 | -54.09621 | 2024-11-17 01:04:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| ddfa3245-4f0a-3b08-bc56-b526a595ad01 | -0.04742 | -53.24903 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 81b3a5a2-9b37-3166-9dc6-8eedb1b59b4c | -2.29988 | -49.1339 | 2024-11-17 01:04:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3ab60607-86b0-3520-9e16-35e38409d81a | -2.60905 | -51.79831 | 2024-11-17 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cf2dc828-35d5-31b2-b127-f98b23c68007 | -3.32995 | -50.49091 | 2024-11-17 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 46e1e228-d5f4-30e1-a3f7-0fc2afe814a3 | -2.67029 | -46.20583 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| ea102960-09ec-3862-b17c-80364990daf1 | -0.32199 | -51.51296 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6e1b2736-3d2c-3d37-ad3b-3286b647bf2f | -3.60793 | -52.22615 | 2024-11-17 01:04:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 16b403bc-31b3-350c-ad39-cdf5d5b7212a | -2.66556 | -46.17426 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 49728ac8-7fba-387f-ad5c-862f2422d9d8 | -4.407 | -45.52647 | 2024-11-17 01:04:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 183.7 |
| 6a4aec84-f021-3cd4-89e1-16e8fe83f763 | -1.28782 | -51.9618 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 25bf45e8-ec2a-32c9-8245-b2bb37451d33 | -4.20163 | -48.70048 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 86c0968b-5a7e-3c07-b9a0-fb7683e92eb7 | -1.07261 | -53.00395 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 716466c8-33a2-3200-a949-c96d244c300c | -4.68226 | -49.6249 | 2024-11-17 01:04:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ae707b15-a652-3cd6-82cf-21f7f0481f7f | 0.91113 | -52.0502 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f435352a-a375-37a4-9bdc-b884771ad948 | -0.3119 | -51.50539 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 283b7115-839c-3595-acd3-c3cc5d9b1d56 | -4.30566 | -48.06654 | 2024-11-17 01:04:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9fbd93ba-7828-3e04-b112-33c2ca72f42e | -3.80359 | -51.37337 | 2024-11-17 01:04:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4aa27b2c-0d59-37d5-a954-cca0504313cc | -3.21195 | -46.67764 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6ef37b61-fc8f-3517-a53a-d4e83b426a9e | -2.8183 | -46.66286 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 806843af-0bf5-39f1-ae8e-1cb280da251d | -1.49799 | -47.38783 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 27041551-44cd-38c9-aecb-3ede515caa36 | -3.68299 | -49.00791 | 2024-11-17 01:04:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| da244f41-52ca-36bc-96ff-9030a9b8b07b | -3.52721 | -50.25813 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 227.0 |
| 6a21c03a-fb6d-31b1-805f-ca75013bd2fc | -3.69104 | -50.11165 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 8beb57dd-2bf1-3408-8930-90d000b965af | -0.95 | -51.72881 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 31.8 |
| d4fbfdae-3937-39c0-95d2-ae42a254880d | -4.32645 | -49.38483 | 2024-11-17 01:04:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6475232e-b3d5-350e-b8f0-800c62103844 | -2.60444 | -47.55249 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| c3b189a4-ff5d-3a3c-b564-955673f2a977 | -3.82761 | -50.22776 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc87f1ae-d111-325b-88b8-77466fd84b94 | -3.44979 | -49.11079 | 2024-11-17 01:04:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| bbcc6a32-0fd4-3078-8398-1ca5d388c098 | -3.77171 | -46.03329 | 2024-11-17 01:04:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7c2025a9-366c-3e29-b176-955611b179e1 | -1.37898 | -51.56633 | 2024-11-17 01:04:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8525f58d-9951-3b21-94bf-c0e15737fd0b | -2.29844 | -49.12376 | 2024-11-17 01:04:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0de3e49b-f3f2-34fd-be9e-cd56de1cb30f | -3.53676 | -50.52223 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f9c159d3-1561-30e5-a803-f627528b6400 | -3.03565 | -47.98356 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a2fdde6d-e128-3668-9f49-2f56b73ffa9b | -1.01727 | -52.27644 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 634deadf-2ddd-32c7-99fa-e4cf68890be2 | -3.46231 | -43.88865 | 2024-11-17 01:04:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |


[Clique aqui para ver as próximas entradas](README13.md)
