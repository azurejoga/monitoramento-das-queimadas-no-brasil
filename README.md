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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f438630-4567-375d-b291-5fdaf8a2eccd | -13.4939 | -43.237 | 2024-10-30 00:05:05 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aa58d058-1716-325d-b687-d79ba0c63c31 | -13.4967 | -43.2509 | 2024-10-30 00:05:05 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3a668d1b-ff2c-38bf-85aa-80aaade63443 | -13.7152 | -46.105701 | 2024-10-30 00:05:11 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c242345-d1af-398d-b1b4-305102b4c79b | -13.7111 | -46.083698 | 2024-10-30 00:05:11 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f141134-b797-3aa4-be7d-5342b1342fa2 | -13.6973 | -46.063702 | 2024-10-30 00:05:11 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fbd2bd91-2c78-395a-b692-967e443cef64 | -13.7014 | -46.085499 | 2024-10-30 00:05:11 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa329414-a6d9-3469-ad4b-cb71214292de | -13.7055 | -46.107498 | 2024-10-30 00:05:11 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3dd6494a-0c75-3205-b077-f24caaef952f | -13.6917 | -46.087399 | 2024-10-30 00:05:11 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c08f8b7-23d0-392d-9acd-34a04be89248 | -13.6958 | -46.109299 | 2024-10-30 00:05:11 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0481d766-a6b9-3d1e-861e-f12b5eaa863b | -1.063 | -47.6452 | 2024-10-30 00:05:12 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 64b3801a-66b3-3b35-9314-5f1d8b82ac5e | -1.4211 | -54.2171 | 2024-10-30 00:05:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 273180fc-306c-3122-ae1e-82440beec565 | -1.5348 | -52.1284 | 2024-10-30 00:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b2986a06-92f2-3892-a579-3da114a87f8e | -12.1433 | -39.394402 | 2024-10-30 00:05:14 | METOP-C | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0ad2bad5-13f5-3d5b-927f-e3037061f593 | -12.1993 | -40.853199 | 2024-10-30 00:05:18 | METOP-C | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9a5d6605-cd32-3b0d-b34e-8d704b5a7aeb | -12.2013 | -40.862598 | 2024-10-30 00:05:18 | METOP-C | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 203f3067-0efc-304b-9c85-aea51d218dd0 | -12.8907 | -44.5947 | 2024-10-30 00:05:19 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b0ea08b3-a4ff-3640-abfe-3b3dee6f1eab | -12.894 | -44.611599 | 2024-10-30 00:05:19 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9141762f-6a5a-39ee-b6aa-6a576aa759fa | -12.6831 | -43.802299 | 2024-10-30 00:05:20 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 141e2d87-1c48-3c1e-b117-0f9bede62b33 | -12.6705 | -43.7896 | 2024-10-30 00:05:20 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a989de01-22f9-33cb-8e4c-ee563e892a05 | -12.6734 | -43.804298 | 2024-10-30 00:05:20 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ca52c07-532a-3301-afdd-dc5fad3c1610 | -12.6763 | -43.819099 | 2024-10-30 00:05:20 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06f83948-3602-3cde-a9b0-981d5eb91826 | -12.6636 | -43.806301 | 2024-10-30 00:05:21 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4614d5d7-d1be-3873-868d-936a3366e15e | -2.833 | -49.2413 | 2024-10-30 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 1712b248-7c36-379b-86aa-9ed7efdb8add | -2.8331 | -49.22 | 2024-10-30 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 6cd49d1f-cfca-37a4-9e10-2c31dbb67f06 | -2.8515 | -49.2408 | 2024-10-30 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 7f06482e-c77a-3963-8a88-f675e3a5d647 | -3.0734 | -54.167 | 2024-10-30 00:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 2aab9931-00f1-3149-a820-a9c00bcffe2f | -3.1028 | -51.1041 | 2024-10-30 00:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 046003fe-74e6-343a-aba6-914e1d274de7 | -11.1612 | -37.417 | 2024-10-30 00:05:23 | METOP-C | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a5dd7c8-4073-31b9-aa9a-83fce1c5ea9b | -11.1628 | -37.424 | 2024-10-30 00:05:23 | METOP-C | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 082e3c44-dba1-3595-8dd3-fe839b01de38 | -3.1097 | -54.2865 | 2024-10-30 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 14f3331f-15f4-342b-9f33-8623aad7d66d | -3.1098 | -54.2665 | 2024-10-30 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 66ca2a57-2838-3b73-94fd-5f630c33997b | -3.1281 | -54.286 | 2024-10-30 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f2b2cc4f-8a96-31f1-99e6-b4d0201f7683 | -3.1281 | -54.266 | 2024-10-30 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 0d56d450-56c1-3373-81da-3799c16a3a57 | -3.16 | -50.6231 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 3ac9efdd-5e47-3804-8275-af54a0d44579 | -3.1601 | -50.6021 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7f14f453-fb3f-36e4-90c0-beaaf7c50ec7 | -3.1602 | -50.5812 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 557c4484-3701-3947-a0d6-3bcb40800b43 | -3.1786 | -50.6016 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ceb0af01-d2c5-397b-86ed-5c0031d87eec | -3.1787 | -50.5807 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3afb1bbb-d6bd-377a-b8d9-6611609724e7 | -3.2172 | -50.1811 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| b9966c10-7762-3c26-b38c-444e34179a7a | -3.234 | -50.5999 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 98978998-9e1b-3480-8c34-82d0cb44dc13 | -3.234 | -50.5789 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| af18840d-7deb-3b14-ad1f-9fae3890a9aa | -3.2356 | -50.2015 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 9bb35185-fded-339c-83e6-dd4e8d46ff73 | -3.2357 | -50.1805 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 5591bc0e-70ac-30c0-beef-c01a424fd0ba | -3.2535 | -50.3479 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| de07a32c-6e89-3772-b10b-008d2c223d16 | -3.2719 | -50.3473 | 2024-10-30 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3d17933d-25a2-39ae-95ff-f736458dd8ad | -3.2908 | -50.2417 | 2024-10-30 00:05:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 0c7946c9-aee2-3d2d-8f2d-74fda8b2c04a | -3.5171 | -49.2402 | 2024-10-30 00:05:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c020287a-aa62-3987-8cbd-faf36c71a163 | -3.5172 | -49.2189 | 2024-10-30 00:05:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 4b592206-1cb7-39e7-b8a8-8528b410078a | -3.563 | -47.4066 | 2024-10-30 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c332c46b-556b-3f2f-99a8-b23a4c12fe56 | -3.5631 | -47.3847 | 2024-10-30 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 270.1 |
| 45296296-6686-3e1c-9ac7-53e6cb43346d | -3.5632 | -47.3629 | 2024-10-30 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| bda9dc5a-cfb8-375f-82a7-562593a506e4 | -3.5688 | -50.043 | 2024-10-30 00:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 7ca505b2-2312-36de-9049-e65b6fa4ddca | -3.5689 | -50.0219 | 2024-10-30 00:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 6bb06886-60dd-3a30-a01f-97d45e035511 | -3.5817 | -47.384 | 2024-10-30 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 2634bcbc-903e-3898-ae69-db11eb3241ce | -3.5818 | -47.3621 | 2024-10-30 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| eb08ee92-cc54-313b-807c-0a7ac4abd37d | -3.7852 | -51.1651 | 2024-10-30 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0ae32e4b-483f-33d8-a2f3-31712f535384 | -3.8037 | -51.1644 | 2024-10-30 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| b8c40213-2a11-329f-b4f4-8683e940b5ef | -3.8038 | -51.1436 | 2024-10-30 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7ce0e1a7-5920-3f4f-8d20-b842f9508cdc | -3.9326 | -41.4957 | 2024-10-30 00:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 150.3 |
| 674a284a-ce43-346f-922f-886f01b602d2 | -3.9327 | -41.4717 | 2024-10-30 00:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| aee859a1-e282-3d68-8fad-dbb208293a26 | -3.9513 | -41.4946 | 2024-10-30 00:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 107.3 |
| fe7b3bb4-81a0-3389-aade-a62391f93ec7 | -3.9514 | -41.4706 | 2024-10-30 00:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| eed6f36b-2080-3925-8d98-ae2e61a3d4ab | -3.8221 | -51.1637 | 2024-10-30 00:05:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| ec876829-2274-357c-9fbf-dc92a641c4a6 | -3.9486 | -48.1291 | 2024-10-30 00:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 142b308a-134f-3a4b-8690-fcc52b6d4bff | -4.0705 | -46.2836 | 2024-10-30 00:05:29 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3a001f75-519a-3936-b4a8-3a1d119dc088 | -4.0681 | -50.024 | 2024-10-30 00:05:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 705e7e1d-de48-312c-8364-74921296e71c | -4.0682 | -50.0029 | 2024-10-30 00:05:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 63fe6999-ed82-3379-85fe-7f1238cbc201 | -4.2561 | -43.46 | 2024-10-30 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| dc6ec6d7-9614-3620-8f7f-dc33c43f4420 | -4.2563 | -43.4368 | 2024-10-30 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| da0b3946-7ded-3a0c-8d60-0e9a4cd4c425 | -4.2748 | -43.4589 | 2024-10-30 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6034f525-7651-3fac-b455-b91ae663de10 | -4.2749 | -43.4357 | 2024-10-30 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 09a5e740-f15a-374b-86b9-4a6c3e703350 | -4.3473 | -43.779 | 2024-10-30 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 7350ae86-e44a-3203-a5f9-c68415332b4d | -4.2496 | -50.6677 | 2024-10-30 00:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a228d8ed-61b6-3b79-9ecc-cc19f8c33c13 | -4.2679 | -50.6879 | 2024-10-30 00:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c60bb644-dd6b-333f-b747-2b6f4815677f | -4.2681 | -50.6669 | 2024-10-30 00:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| d463dd8a-9d52-3562-a739-1002bb24cca1 | -10.6494 | -37.0228 | 2024-10-30 00:05:30 | METOP-C | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 99f97575-0ce1-3b72-9269-c6723bb78b0f | -10.651 | -37.029701 | 2024-10-30 00:05:30 | METOP-C | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e83d0fe-7252-3afb-8500-dc138e069737 | -4.4269 | -45.8199 | 2024-10-30 00:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 935a7460-1944-3604-97c0-f095d445b299 | -4.4455 | -45.8189 | 2024-10-30 00:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| bdb438b5-43a5-38ac-9882-be38cae089e3 | -11.8931 | -43.810902 | 2024-10-30 00:05:33 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0cba381-5070-3a44-9e5d-50ee50d95207 | -5.0154 | -44.3595 | 2024-10-30 00:05:34 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| cd375a8d-0794-3dd9-8bc4-e5f5cf85998e | -5.2306 | -47.9566 | 2024-10-30 00:05:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 873b4fb3-2ee3-3717-a91c-c1ef1a69b118 | -10.1833 | -36.472301 | 2024-10-30 00:05:35 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 73e5f78d-0216-3f93-adaa-194e854205a5 | -5.9786 | -45.3847 | 2024-10-30 00:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b4b41cea-b7b7-398d-907b-09eda222b693 | -5.9788 | -45.3621 | 2024-10-30 00:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| c784aca1-02aa-3708-b7c3-90ba12a69cfb | -9.7612 | -36.252399 | 2024-10-30 00:05:41 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b6aff78d-92d1-3503-a5bc-bc2a58ed9860 | -9.7514 | -36.254601 | 2024-10-30 00:05:41 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab196dec-466e-3637-a508-590a18d398e7 | -9.7531 | -36.2617 | 2024-10-30 00:05:41 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ff5cfdd-45a2-3052-8e7d-b8d3e9e468b6 | -6.8408 | -59.0519 | 2024-10-30 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 272fec87-378a-3d9b-9c55-a30949916570 | -6.8591 | -59.0705 | 2024-10-30 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| c01e0efe-9512-3714-8352-19a1c39abfd1 | -6.8592 | -59.0511 | 2024-10-30 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| f63d7541-aa66-30bc-89a3-365c8cbc140e | -6.8593 | -59.0318 | 2024-10-30 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c354df0f-66d5-3ad9-a604-ff400d951596 | -9.2725 | -35.524799 | 2024-10-30 00:05:46 | METOP-C | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a68b6a18-8f0c-3bbf-bacb-ef67946edd05 | -9.2743 | -35.532101 | 2024-10-30 00:05:46 | METOP-C | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7269131-1efd-3e1b-9d58-d385767ddb3f | -9.0719 | -35.328701 | 2024-10-30 00:05:49 | METOP-C | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35afe69f-9cba-323b-b2b0-fccbec586f7d | -9.0736 | -35.336201 | 2024-10-30 00:05:49 | METOP-C | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4bc829fe-cf5f-3513-a278-d3004b855fbd | -9.0754 | -35.3437 | 2024-10-30 00:05:49 | METOP-C | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d0412d3-d76c-32bd-aadb-6353d42df562 | -7.8736 | -46.9065 | 2024-10-30 00:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 34920887-cf10-3b0c-bf3b-d8bd3a29da5d | -10.8853 | -44.3992 | 2024-10-30 00:05:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 22e0cc11-59db-3120-8251-0d3f7752a874 | -10.8908 | -44.5257 | 2024-10-30 00:05:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
