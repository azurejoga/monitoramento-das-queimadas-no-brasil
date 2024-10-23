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
| 8ec2c907-32e0-3574-b722-55125641e208 | -2.5041 | -54.1197 | 2024-10-23 00:05:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 02a2eea9-d857-343b-bb13-9db5587fb5c4 | -2.5041 | -54.0996 | 2024-10-23 00:05:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 207bbd69-4f65-35d8-9415-23e8924a4a65 | -2.5224 | -54.1193 | 2024-10-23 00:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6ef0ae00-3dad-333a-9cda-8e99e4b0019a | -2.5225 | -54.0992 | 2024-10-23 00:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8faa65e8-84f3-33d7-9b73-eac0ceff31c8 | -2.7589 | -49.3072 | 2024-10-23 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 3a9b5393-94c5-33f7-b0d2-6ca309fa96fa | -2.7614 | -54.0338 | 2024-10-23 00:05:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| f462f873-12ea-3ab1-abb0-72ea40d218ac | -3.1101 | -54.1661 | 2024-10-23 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 1edd1b05-95e0-3abc-bbc1-c6f8a8c693c3 | -3.1102 | -54.146 | 2024-10-23 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 0a821382-fa69-38a5-9877-9396f7715446 | -3.0917 | -54.1666 | 2024-10-23 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 41b932bb-6327-3a4c-b9d9-82cf8716c970 | -3.0918 | -54.1465 | 2024-10-23 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ae93e797-8b49-3b0f-a063-68457eb4c277 | -3.2542 | -50.1799 | 2024-10-23 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b26cc5db-9d56-34de-8184-240343659948 | -3.5307 | -54.7356 | 2024-10-23 00:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b62d32e9-139b-3715-b7cf-53a7e9d33aa0 | -3.549 | -54.7551 | 2024-10-23 00:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9e882191-a306-359d-bda6-e89b23a3b1a0 | -3.5491 | -54.7351 | 2024-10-23 00:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| ccdda065-bd1e-30e9-bf93-945620543235 | -4.1719 | -47.9894 | 2024-10-23 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| e5c914d4-43a0-3218-b048-c3b8811df790 | -4.1905 | -47.9885 | 2024-10-23 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d8fa3084-39b5-3f44-9c92-04a0d8aae5a0 | -4.1906 | -47.9669 | 2024-10-23 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 373018a0-dbb0-34f4-bfbf-13398ea54784 | -4.6016 | -47.5337 | 2024-10-23 00:05:32 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2b8cfe55-7b50-3e61-b7d6-891b0ed52e1d | -4.5995 | -50.9245 | 2024-10-23 00:05:32 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 937681ab-c861-353b-82d8-85b6908b6fda | -4.618 | -50.9236 | 2024-10-23 00:05:32 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 6b5214b6-9f4e-3fb3-87b0-0c688b2a6cef | -4.6588 | -44.61 | 2024-10-23 00:05:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 9875fce3-a929-3782-a7e4-f986c08a2b5d | -4.659 | -44.5872 | 2024-10-23 00:05:32 | GOES-16 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| aac1d038-c0a5-359e-b146-24a7a7b615af | -4.6775 | -44.6089 | 2024-10-23 00:05:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 236.4 |
| 7896c52c-30a1-3cce-98b4-976d68e85277 | -4.6776 | -44.5861 | 2024-10-23 00:05:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 546dac70-5cd1-3b56-8ce7-0608376002a1 | -4.7254 | -45.7363 | 2024-10-23 00:05:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| dc036521-e5a5-3abc-971f-faa29b8f9680 | -4.7375 | -46.6701 | 2024-10-23 00:05:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 23d03e3f-03f3-3720-99aa-5004abd81e6f | -4.7565 | -46.6249 | 2024-10-23 00:05:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 6e9abd98-4579-3d46-ab4a-c4cf273f5400 | -4.7566 | -46.6027 | 2024-10-23 00:05:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 628686d5-322a-39fd-967b-5a2754acb00b | -4.7068 | -45.7373 | 2024-10-23 00:05:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 70bd2e29-fa12-3d0a-838f-ade958ea8a04 | -5.2118 | -43.1899 | 2024-10-23 00:05:35 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7930c12a-1fbe-3382-b94f-29795ea8ff99 | -5.2305 | -43.1886 | 2024-10-23 00:05:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 272caeed-7354-3eb4-8abf-1a261a065f67 | -5.2307 | -43.1652 | 2024-10-23 00:05:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 921c5c5e-5341-35c6-b7c4-144aa8ce8353 | -5.5671 | -43.2576 | 2024-10-23 00:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| b2cc09bb-294f-36af-9b41-15c9c3340933 | -5.5858 | -43.2562 | 2024-10-23 00:05:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 6c753098-1a60-386c-9fb3-8dc1e00e6589 | -5.8553 | -44.5302 | 2024-10-23 00:05:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 9329867c-a529-35c7-83de-0056b7d03e09 | -5.8555 | -44.5073 | 2024-10-23 00:05:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 33cdbfe5-7455-30ab-b38c-bdc226647860 | -6.6765 | -43.0491 | 2024-10-23 00:05:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 4e1c271a-1ccf-3129-8401-6f8e5d313a9d | -6.6767 | -43.0255 | 2024-10-23 00:05:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| cb39b610-4da2-3f4b-9ca2-22c776297dde | -7.161 | -45.153 | 2024-10-23 00:05:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ec571b98-d00d-38d9-a5ce-19350a79d081 | -7.1613 | -45.1302 | 2024-10-23 00:05:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 25a03dfe-c2fc-357d-a57e-03619a3be7d4 | -7.1798 | -45.1513 | 2024-10-23 00:05:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b2c85f0e-5e71-3f8e-8731-3e20c4fe7ac8 | -7.1801 | -45.1285 | 2024-10-23 00:05:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 255fb7db-50b2-3749-b8f9-aec54d3598a1 | -7.4518 | -49.637 | 2024-10-23 00:05:48 | GOES-16 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 3d3b4207-46cb-3dbb-893a-c72f04cc8624 | -10.0295 | -36.1344 | 2024-10-23 00:06:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| 1d69681d-05df-3f4d-b618-aec6b3a9d986 | -10.6725 | -58.749 | 2024-10-23 00:06:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8d832744-e15d-3621-895d-c78e373a3cc9 | -11.3406 | -54.3547 | 2024-10-23 00:06:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ca37be70-34ea-3bb6-a95e-2fb2037fe823 | -17.6667 | -57.4822 | 2024-10-23 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| e2fda264-519a-3917-8853-145c150bb65c | -17.6671 | -57.4616 | 2024-10-23 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.3 |
| beccec15-1191-372a-95ff-fee3d275a537 | -17.6674 | -57.4411 | 2024-10-23 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| 6a03e887-1ca1-3651-9c72-4f98c139b2a7 | -17.6865 | -57.4798 | 2024-10-23 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 6ad36dfa-1d5b-35e7-9e98-be20566a5eb5 | -17.6868 | -57.4593 | 2024-10-23 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 197.8 |
| 308e6d1d-8b80-3a19-acd0-67faa8946495 | -17.6871 | -57.4387 | 2024-10-23 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.5 |
| 3bde6877-6cdc-39d5-aca3-d0cb3ed92e43 | -18.2633 | -56.0812 | 2024-10-23 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 8ba183aa-9074-37af-9365-450f9d17219d | -18.2637 | -56.0603 | 2024-10-23 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 942d6515-f53f-30b3-ad41-704b77f65eea | -2.5041 | -54.0996 | 2024-10-23 00:15:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0d05f295-ff28-3f84-bb86-6b9eb19c58e6 | -2.5225 | -54.0992 | 2024-10-23 00:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d0d8acc7-960c-38e7-872d-4a95d4e1b52d | -2.7431 | -54.0342 | 2024-10-23 00:15:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 29931510-e55a-3d4c-ad9f-62dd5e39c0c7 | -2.7589 | -49.3072 | 2024-10-23 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 4cc79779-81ab-3472-81cf-eda2a555a521 | -2.7614 | -54.0338 | 2024-10-23 00:15:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 28592c73-a938-3ec6-904d-bb596efdb1ae | -3.0917 | -54.1666 | 2024-10-23 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 44067a56-6269-3090-8d7e-cb167457c94d | -3.0918 | -54.1465 | 2024-10-23 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 6d12fa20-10bb-3c88-87de-9a1b73df1cdc | -3.1101 | -54.1661 | 2024-10-23 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| c3c2c2af-86ba-3ff3-8e10-a16c112e1b46 | -3.1102 | -54.146 | 2024-10-23 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 615c6c3d-c1a6-322c-9e4b-5451e5c5da5f | -3.2542 | -50.1799 | 2024-10-23 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 18d6c80c-cb0c-30d1-8524-c7ebfc9b3647 | -3.5307 | -54.7356 | 2024-10-23 00:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 4cf0f46d-ad51-3d36-87dd-2a965038ed55 | -3.549 | -54.7551 | 2024-10-23 00:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f58c4c43-91b6-308e-b414-6fa19414453a | -3.5491 | -54.7351 | 2024-10-23 00:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| db5b9a1f-ccfd-3e61-b92c-37964c568248 | -4.1719 | -47.9894 | 2024-10-23 00:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 559ea29c-6150-3b9c-9337-d15546a41800 | -4.1905 | -47.9885 | 2024-10-23 00:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 14b37769-f11c-3aa6-a990-03b0139533d3 | -4.1906 | -47.9669 | 2024-10-23 00:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 10c7d87f-d54a-347c-bc6f-81959f532558 | -4.6016 | -47.5337 | 2024-10-23 00:15:32 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ba986b46-d4b1-368e-a798-ce908cd27c8b | -4.618 | -50.9236 | 2024-10-23 00:15:32 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c8e2c9e8-58a6-3d4b-94da-19d78eb7dde6 | -4.6588 | -44.61 | 2024-10-23 00:15:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| cd324813-e8a2-3471-82e5-5376a9a29486 | -4.8404 | -42.817 | 2024-10-23 00:15:33 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 92d0960e-78f9-3027-8d88-245e67013a0a | -4.8406 | -42.7935 | 2024-10-23 00:15:33 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 8a226688-805c-39f5-ac0c-be762766306d | -4.8593 | -42.7923 | 2024-10-23 00:15:33 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 0042e8d8-6f5d-3633-abf8-c2d2d082fef3 | -4.6775 | -44.6089 | 2024-10-23 00:15:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 3c8fc049-1460-3ce3-89da-562f484f2c3d | -4.6776 | -44.5861 | 2024-10-23 00:15:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 823294f5-c711-3163-bd86-41ad06a96db8 | -4.7068 | -45.7373 | 2024-10-23 00:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d2b928fd-310e-3284-b324-c1187926b693 | -4.7254 | -45.7363 | 2024-10-23 00:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c113b83b-3a9d-354d-9459-82c615b52dde | -4.7375 | -46.6701 | 2024-10-23 00:15:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| fa4c35cf-47b0-3937-8c93-390438ea70c8 | -4.7565 | -46.6249 | 2024-10-23 00:15:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 45911176-7c8a-3c83-a701-1c593b6dfeb2 | -5.2118 | -43.1899 | 2024-10-23 00:15:35 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 59c72eac-8ea7-339a-9afd-2730838f479c | -5.2305 | -43.1886 | 2024-10-23 00:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 8b619e2f-ec9b-3466-b462-8cc12f0d658d | -5.2307 | -43.1652 | 2024-10-23 00:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c35b529f-6888-382c-8240-d30a4450fd96 | -5.5671 | -43.2576 | 2024-10-23 00:15:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 1af0e62f-056e-3faf-a8b8-bb38967cf16d | -5.5858 | -43.2562 | 2024-10-23 00:15:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| bec3e132-0115-3002-b5d6-adc9571efb66 | -6.6765 | -43.0491 | 2024-10-23 00:15:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| df062da5-a172-34df-ac64-4ca7f84bddbc | -6.6767 | -43.0255 | 2024-10-23 00:15:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 151c78d5-872f-38e3-aefe-ba7ca6d60236 | -7.2663 | -35.1263 | 2024-10-23 00:15:46 | GOES-16 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| a88bc917-a58a-336f-8084-709915985d12 | -7.2667 | -35.0988 | 2024-10-23 00:15:46 | GOES-16 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 114.3 |
| 525a6360-8cc5-345e-961c-614a74fbf929 | -7.161 | -45.153 | 2024-10-23 00:15:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c76de253-31ba-3364-a50f-2a2b935ad7d6 | -7.1613 | -45.1302 | 2024-10-23 00:15:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| a5c49945-7b57-3cf1-b6b7-324ebb7db1a4 | -7.1798 | -45.1513 | 2024-10-23 00:15:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 4c7b3d9d-16b5-3568-892f-04a54de55f04 | -7.1801 | -45.1285 | 2024-10-23 00:15:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| f7e4462d-994f-365a-afbf-c3eea3034c0c | -10.6725 | -58.749 | 2024-10-23 00:16:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ac4b1d35-071b-308c-a525-6fb6d22cc7eb | -11.3217 | -54.3564 | 2024-10-23 00:16:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 4bd5a59f-d404-3944-939a-15dd2bc946c2 | -11.322 | -54.3359 | 2024-10-23 00:16:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| cafc1622-8c67-3cc3-b8ed-dfd3dac2a832 | -11.3406 | -54.3547 | 2024-10-23 00:16:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 6f351af0-7864-349b-8882-76a68ae18b3e | -17.6671 | -57.4616 | 2024-10-23 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |


[Clique aqui para ver as próximas entradas](README2.md)
