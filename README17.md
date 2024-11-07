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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6147806-edfc-30f8-9fe6-89197f5bb17b | -2.82 | -52.9409 | 2024-11-07 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 994e155d-6368-37f8-b183-65817819a625 | -5.1581 | -47.6997 | 2024-11-07 01:00:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 04ddd3d0-f37b-3bb4-9204-989f0945d3c3 | -5.0526 | -46.851 | 2024-11-07 01:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| fbfd1d60-5ca0-37a1-b5d4-586e846dc196 | -3.0396 | -53.2805 | 2024-11-07 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 551b8cf3-11a6-3901-a8d3-2b823529de62 | -3.7218 | -48.9979 | 2024-11-07 01:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| de277f00-fd17-3103-84b4-32ec2a2cc11d | -5.9788 | -45.3621 | 2024-11-07 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1456089c-9d19-3598-a098-b4a567d637d4 | -5.158 | -47.7215 | 2024-11-07 01:00:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 3d1a844a-2c9b-344c-b9d1-82357af53f11 | -2.7639 | -53.2265 | 2024-11-07 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| eb6ae80b-d584-3e72-8b04-d91a3b7b1bfd | -9.7493 | -43.5791 | 2024-11-07 01:10:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| c9bb530c-0ec3-3762-a855-3fc147e9a63a | -5.1581 | -47.6997 | 2024-11-07 01:10:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 3cd02bc1-207b-33ec-bbbc-58f2c4a59f75 | -2.6228 | -51.3038 | 2024-11-07 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ef2e529a-0aca-3e66-9c1e-b2fe44e50413 | -2.8688 | -49.5375 | 2024-11-07 01:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 23e9173f-563d-3994-b880-20d7740bcd14 | -1.1466 | -53.7177 | 2024-11-07 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a0cc2913-70ce-3652-a0f2-3558c0601893 | -4.522 | -42.8608 | 2024-11-07 01:10:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| dadb164d-9b79-393a-a529-1f227d645d40 | -4.5033 | -42.862 | 2024-11-07 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 9fcbb94d-2d88-3371-b666-2b1b92280257 | -2.924 | -49.5994 | 2024-11-07 01:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fdc13872-dd96-3cbd-99a3-06090e544983 | -5.1395 | -47.7008 | 2024-11-07 01:10:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a046bf3a-549f-36e5-b3e8-6727fdb70c7d | -7.0019 | -34.914 | 2024-11-07 01:10:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 157.7 |
| d6937711-5fcc-3aac-b236-b0ef15bb9b2a | -2.8537 | -48.6642 | 2024-11-07 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 87ae1be7-d155-3d71-b51e-ea9b024fb8ec | -3.9669 | -48.1716 | 2024-11-07 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 3a59f34f-7f5a-344d-abb9-fa1d6d78c515 | -3.0207 | -53.443 | 2024-11-07 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| bae5a339-3114-319e-9327-5f0095c69287 | -1.2014 | -53.8983 | 2024-11-07 01:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4b233252-2613-3139-b37b-2e73e5b178e9 | -7.0211 | -34.9115 | 2024-11-07 01:10:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| 63c7c827-1f8e-3d97-94a3-1fa9a0035753 | -10.0357 | -44.7287 | 2024-11-07 01:10:00 | GOES-16 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| a28d7eaa-90b8-3aa3-bdfe-f0323162a443 | -6.3323 | -35.1071 | 2024-11-07 01:10:00 | GOES-16 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 84.6 |
| e4b35118-1cf7-3742-b9b9-ae376593b76a | -17.293 | -57.5062 | 2024-11-07 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| 75cf1168-7564-3526-a14d-01aa9ced4a5f | -2.82 | -52.9613 | 2024-11-07 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| b158d18e-699b-3fb7-b7ef-5d8c2b4f5ab1 | -3.0397 | -53.2603 | 2024-11-07 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 1e5c2d4b-036d-3f9b-86c9-4cabab58d469 | -5.0528 | -46.8289 | 2024-11-07 01:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 6ed62a08-2481-38f9-88c3-3021d67f6d76 | -5.0154 | -46.8531 | 2024-11-07 01:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| fd02eda3-ef63-31fa-9df9-06759774ab0e | -3.967 | -48.15 | 2024-11-07 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 17ea6ae9-8f5f-31ec-91bf-b785d021855d | -3.4564 | -50.3832 | 2024-11-07 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 909f2c2a-fbe4-3015-9a6e-02c650da815b | -3.1617 | -50.2038 | 2024-11-07 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 2de17fc7-8201-367f-a829-04e6fc1df282 | -5.9786 | -45.3847 | 2024-11-07 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 93b611a1-e53c-31be-b817-d78f09303c54 | -5.9788 | -45.3621 | 2024-11-07 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 047b8372-9056-3c7e-a4f8-bf122e226bb0 | -2.82 | -52.9409 | 2024-11-07 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 2ce02e8d-8d5f-3731-a314-9a14a42ab050 | -5.0526 | -46.851 | 2024-11-07 01:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a13f8338-c5c9-3dc5-bb3f-d534e5cf06fd | -2.8536 | -48.6856 | 2024-11-07 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 4dceed6d-4c6b-3b3d-ad95-7e573ea47321 | -5.0342 | -46.83 | 2024-11-07 01:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 32c36b78-7aef-3e20-9809-7465c8da842a | -4.5218 | -42.8843 | 2024-11-07 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5e12abc6-cf44-35b7-aa8b-15ba563ae70d | -5.9975 | -45.3607 | 2024-11-07 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 0b2b66bc-36cc-3348-a8e1-ac3c386b0010 | -1.1283 | -53.7179 | 2024-11-07 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| cbb4bb8d-faa5-309d-96df-d8e2f579cb11 | -5.034 | -46.8521 | 2024-11-07 01:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 201.1 |
| a5b44608-7bdd-3897-8b61-51eb739e0724 | -17.7055 | -57.5186 | 2024-11-07 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 6bf24829-400a-3833-bcf8-9e9843beb403 | -5.0155 | -46.8311 | 2024-11-07 01:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c8d765c7-6706-344c-9cb2-316e1fce9e32 | -1.1831 | -53.8985 | 2024-11-07 01:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 50954515-e1c7-3d75-8763-e0a8cfa3676a | -3.0396 | -53.2805 | 2024-11-07 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 22973d23-407b-34aa-b005-1ad17fb7f0b7 | -10.036 | -44.7056 | 2024-11-07 01:10:00 | GOES-16 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| f27526c5-dbf5-334c-afe6-df71999f0f34 | -23.9186 | -54.055 | 2024-11-07 01:15:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb94a3ab-fc9b-36e2-ae44-7be328f4b3bf | -23.9555 | -54.035198 | 2024-11-07 01:15:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3f5f372-6f04-39b2-8174-8f8824d8e496 | -9.3685 | -62.636799 | 2024-11-07 01:15:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2dcf06-ca01-3cfc-8e11-3d56bac5190a | -17.704399 | -57.5033 | 2024-11-07 01:15:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 98144dc0-d210-3233-afb3-d07364e09974 | -23.9575 | -54.044102 | 2024-11-07 01:15:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f081aa3-b369-3979-b52d-5649890f344f | -9.3701 | -62.644199 | 2024-11-07 01:15:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf7836fb-5826-3783-b17c-da79d0e7e4a1 | -23.9263 | -54.0434 | 2024-11-07 01:15:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 376eeb83-32a0-30b4-8afe-1c74b332d532 | -23.9534 | -54.026402 | 2024-11-07 01:15:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 99199abf-0b3e-35c2-8564-20d784683f06 | -17.7061 | -57.5107 | 2024-11-07 01:15:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d786f1e8-d5be-35e9-a6e0-eb22b4ab79a0 | -23.916599 | -54.046101 | 2024-11-07 01:15:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c6c475cb-110d-3cd5-a85d-9cece187bceb | -17.298 | -57.4856 | 2024-11-07 01:15:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4e8085d-2c4b-331d-9007-528c83aa576a | -16.9415 | -57.643101 | 2024-11-07 01:15:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3c231a5-4d91-3e0e-904f-ff4a7006ec46 | -17.712601 | -57.4935 | 2024-11-07 01:15:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea693a32-cf90-3282-9495-f4250e769a73 | -17.299601 | -57.493099 | 2024-11-07 01:15:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58055eac-04e1-3ec2-aebd-f2b1d3457018 | -23.9242 | -54.034599 | 2024-11-07 01:15:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 15de14fb-1656-33e1-a724-ee8ed1c11382 | -17.702801 | -57.495899 | 2024-11-07 01:15:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ef77fe05-c927-36b9-bffb-9f2d914962b9 | -1.127 | -53.7015 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91820975-3708-3664-bd97-d41a0201e6a1 | -2.8156 | -52.930698 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da29dcb6-92a3-3eba-8947-573f880974fa | -3.0046 | -53.426701 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6955241-a9b9-34c1-a082-b8dd6c2985be | -3.0266 | -53.260201 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1be40d36-8df9-3a0c-bc72-c1c89f67d579 | -2.8251 | -52.884899 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7195ba7a-f1ef-3f5c-9a43-7a2b8b6fe790 | -2.0689 | -52.018002 | 2024-11-07 01:17:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01b35263-6b19-3f90-8503-50e9d4791dc0 | -2.8108 | -52.953499 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afd0e3af-c143-34da-8a2b-72bd5e12540f | -2.7566 | -53.199799 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4a9248b-559a-3f36-8a31-e2756fc21ab7 | -2.4212 | -53.6423 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a053d85-21ff-3c4a-aff9-112e9f9b6089 | -2.8059 | -52.932999 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a581522b-6af9-3975-8849-6684a204425b | -1.1367 | -53.6992 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffb8762c-f8c4-327a-872a-5da2ed0e3dc3 | -2.8107 | -52.910099 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e669c4a-7b65-34b1-92ce-5129526498cb | -1.1905 | -53.887402 | 2024-11-07 01:17:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bbb3f7e-fe7d-3347-bf30-fbe804ebbc62 | -1.1605 | -53.7141 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d58b6afc-6da3-3c93-b937-c2d3127df2fa | -2.8204 | -52.907799 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfd14c5d-5d4b-3f20-8bf0-2eb8262d9b79 | -2.4309 | -53.639999 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a795c797-1182-3a8b-bc65-ce6f04e9beee | -2.801 | -52.912399 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ccbd2fe-6f4c-342e-9858-55336ba76bf7 | -1.1411 | -53.718498 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd81ac43-9105-3669-a365-60615a205fab | -1.1508 | -53.716301 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42419796-5649-33de-98a6-9ca39b38a49b | -2.7962 | -52.935299 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8604a492-767c-3a9f-8c36-adc083484edd | -2.7469 | -53.202 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 210ccee2-c6cc-3e4a-a1c0-56319532852f | -2.2282 | -53.6478 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 210832cd-1783-3cd0-9d45-53a9aa035064 | -2.7613 | -53.219501 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 340b0046-fe07-3466-89f2-0c3b705ee3f7 | -1.1808 | -53.889599 | 2024-11-07 01:17:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9a835b0-38cb-32bf-a817-63e2c932fb08 | -3.022 | -53.240799 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c7e1582-3316-32b3-a581-4abb4535bd57 | -3.6528 | -52.328098 | 2024-11-07 01:17:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d93b0461-40ee-39bd-be70-386b787a71d5 | -1.1861 | -53.868599 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b94412e-c9b9-39d6-a3ca-7f5a6d697d76 | -2.83 | -52.905499 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8c650b3-baff-3d94-86e3-5f725903d476 | -2.0747 | -52.0425 | 2024-11-07 01:17:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e72baf4-c821-3031-b481-48c709f8a123 | -2.603 | -51.266899 | 2024-11-07 01:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7db94d23-fa92-312e-acf7-1d4bac029660 | -2.7516 | -53.221802 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e0f4a6a-734e-33cd-b67f-4fdda265978b | -1.1764 | -53.8708 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a9dd3d-c49a-302c-85fb-93a31934f455 | -3.0143 | -53.4244 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88bd6bdf-35b6-347f-9f30-353b8624a803 | -2.2326 | -53.6665 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54b22606-d7b9-31df-a3b9-a5cb6fc8c721 | -3.0002 | -53.407799 | 2024-11-07 01:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed6f779-e074-3cd4-b5ef-6f8222edf395 | -2.4256 | -53.6609 | 2024-11-07 01:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
