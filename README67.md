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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d63e68fe-8a04-391f-9d03-440248c9f600 | -10.28927 | -68.85406 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7d79f7a-3816-3cec-b646-aca4f48d8591 | -10.28895 | -68.84679 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2af5efd-fe7a-3a00-8961-75c62cb51ed9 | -10.28818 | -68.85318 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 597918ab-fe9e-3e06-bc40-be860ba0d913 | -9.39645 | -68.98724 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebcd6bc7-2085-3ede-97d6-8981ed24e842 | -9.3938 | -68.98241 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dbad3ff6-359e-3346-8a11-14b8355c13bd | -9.39305 | -68.98851 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e37c09bc-5998-3918-b949-79a37c22c1ba | -9.38974 | -68.98623 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4584e5b-2004-3b30-b163-159921a9cb1d | -7.89447 | -72.44357 | 2024-10-17 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 678fd741-33cf-30c4-ac1a-adb0cec5fad5 | -7.89402 | -72.44688 | 2024-10-17 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe8f01be-fdcd-3f90-99bd-98bdbdefdced | -7.89365 | -72.4457 | 2024-10-17 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d1d07ef-ef7a-382c-b78e-4b6125eb2eb6 | -7.88826 | -72.44952 | 2024-10-17 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8c3f6f4-6816-3aa4-8436-f24f6abc0f69 | -7.81238 | -73.10858 | 2024-10-17 06:46:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c031f4cc-62c2-3fda-8536-76ce78a823db | -7.81197 | -73.11154 | 2024-10-17 06:46:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53505683-c64a-39b9-9535-eb64ec6a20e0 | -7.81181 | -73.10829 | 2024-10-17 06:46:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2438d66-5187-37dd-b51a-8dc415247796 | -7.81141 | -73.11125 | 2024-10-17 06:46:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbd93990-f1e8-3099-bedf-052c440ebf12 | -7.76994 | -72.85081 | 2024-10-17 06:46:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f25611cb-202e-3a3b-be5f-cac49ed00804 | -7.73121 | -72.95883 | 2024-10-17 06:46:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45f50a94-cf45-3061-bb59-4ece1ec22394 | -8.30497 | -72.81926 | 2024-10-17 06:46:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3db90aa-d512-3863-8f8a-dc6c1192436e | -10.85504 | -68.26942 | 2024-10-17 06:48:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c13f4e10-9e00-36c3-85c4-a789fd12637a | -10.63153 | -69.16257 | 2024-10-17 06:48:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d494397-6677-3452-b2e9-f9ec946eec5b | -10.90554 | -69.41135 | 2024-10-17 06:48:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3249cb7-cf8e-3189-ba17-6fa900ea2150 | -10.89819 | -69.4164 | 2024-10-17 06:48:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b82ac1a-29bd-349c-8771-4386c40c2894 | -10.86287 | -69.3932 | 2024-10-17 06:48:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2bca7ac-6a45-36ea-98e7-62808b1a8c0d | -10.86215 | -69.39919 | 2024-10-17 06:48:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e569eb8e-11dc-3583-af87-41973fe86390 | -10.86144 | -69.40508 | 2024-10-17 06:48:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95e3aaaa-a725-3669-bc43-e9feb245e0a2 | -10.67271 | -69.42268 | 2024-10-17 06:48:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a95eb3be-e5af-3452-a9e8-6a5124dd2ffd | -17.8052 | -57.4449 | 2024-10-17 06:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 4dd4c3ce-88e1-31b9-98b7-1976a94582ac | -17.8049 | -57.4655 | 2024-10-17 06:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| ed6c2fe6-50a5-37bf-9121-6b0fd065709c | -17.8641 | -57.4583 | 2024-10-17 06:56:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| c1d260ff-8cfc-33ac-a457-2fdc8d3c0fb6 | -17.8839 | -57.4559 | 2024-10-17 06:56:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| d637de44-7b73-3b74-8438-1cd820121d73 | -17.8835 | -57.4765 | 2024-10-17 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 670af5fc-9cb8-3aa3-9e50-0f570f5ae104 | -17.8638 | -57.4789 | 2024-10-17 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 17429975-4069-33cb-a6c7-bb2ce98b4a27 | -12.5147 | -63.3014 | 2024-10-17 07:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d7505584-b0cf-3858-a5a4-b36b4648e8cf | -17.8641 | -57.4583 | 2024-10-17 07:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 0f221067-c59d-3cc3-a64e-e0bf6d40bf8f | -17.8638 | -57.4789 | 2024-10-17 07:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 886a5d81-5396-3b9f-be50-08956fd8a982 | -17.8049 | -57.4655 | 2024-10-17 07:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| b79bf647-7cc3-3f7e-ae1d-266d3c62daa6 | -17.8052 | -57.4449 | 2024-10-17 07:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| fb8e05df-5996-3c83-8bb2-98468f8ddd56 | -17.8246 | -57.4631 | 2024-10-17 07:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 00507996-6593-358e-96f8-fbf58eeeb534 | -17.8638 | -57.4789 | 2024-10-17 07:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 5299fd5b-e45e-3cad-9813-429c3a2ef888 | -17.8049 | -57.4655 | 2024-10-17 07:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 8ed5c467-c1c5-3496-b8e0-832c27abe06c | -17.8052 | -57.4449 | 2024-10-17 07:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 70b8651c-4ba5-3ae2-8c4c-e41b0e2bfd4e | -17.8246 | -57.4631 | 2024-10-17 07:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 7d63f4b3-ecfb-313f-89ed-c646e35099c4 | -17.8641 | -57.4583 | 2024-10-17 07:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 6067e85f-2aa1-3eb0-b8a1-e36a7c8d9e16 | -17.9036 | -57.4534 | 2024-10-17 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 0e67e86c-9c67-3a8a-af20-35d34df35bfd | -17.8839 | -57.4559 | 2024-10-17 07:16:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 6357b322-9084-3f53-8ba9-a0375f6ededd | -17.8246 | -57.4631 | 2024-10-17 07:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| e84df9b6-73ed-39c4-8d04-a93976350292 | -17.8049 | -57.4655 | 2024-10-17 07:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| c08351ef-47ba-31f6-8b7e-238acde0d5d7 | -17.8052 | -57.4449 | 2024-10-17 07:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 5856ce1e-c7ed-30f8-9109-b466d7fcef5c | -17.8641 | -57.4583 | 2024-10-17 07:26:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 8731e203-9b89-3378-87af-ba3bfc328594 | -17.8638 | -57.4789 | 2024-10-17 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 015480b1-56c6-3b6c-a159-489dee607d25 | -11.8814 | -64.9323 | 2024-10-17 07:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f1c41539-c7e6-33c4-b19b-1633d6276472 | -17.8049 | -57.4655 | 2024-10-17 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 03b60701-4692-3309-8cf8-75a2f37a2a10 | -17.8052 | -57.4449 | 2024-10-17 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 8efa4b6e-c0d5-3b04-93ca-880d31ff8ff8 | -17.8246 | -57.4631 | 2024-10-17 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| a500a835-a196-3d74-953c-c21c60aae302 | -17.8638 | -57.4789 | 2024-10-17 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 89e63213-37d9-317d-bf51-ec51740bc293 | -17.8641 | -57.4583 | 2024-10-17 07:36:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 020e638d-988e-35a3-88a1-42d8476a3c48 | -11.8814 | -64.9323 | 2024-10-17 07:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 63a79280-ab0d-3009-978b-9beeb4c806bb | -17.8641 | -57.4583 | 2024-10-17 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| 58a1380d-4b5e-311c-830f-a8924fd4d555 | -17.8052 | -57.4449 | 2024-10-17 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 94b3733a-e0a8-33d7-9b92-8c26d295953c | -17.8638 | -57.4789 | 2024-10-17 07:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 9facb4d1-7079-3a04-8b78-3483bf0a955e | -17.8246 | -57.4631 | 2024-10-17 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| fc031ee2-6a18-3f8a-bf78-314f693fa739 | -17.8049 | -57.4655 | 2024-10-17 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 40c4f311-9c6a-3181-967b-cb8a77f3f189 | -17.8049 | -57.4655 | 2024-10-17 07:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 425c37d0-0767-378d-92f7-97412eb30889 | -17.8052 | -57.4449 | 2024-10-17 07:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 95160b62-2434-34f6-b794-7912ac6b5647 | -17.8638 | -57.4789 | 2024-10-17 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| de120019-b271-3bf9-84df-076230490409 | -17.8641 | -57.4583 | 2024-10-17 07:56:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| bab85c2a-448c-3713-9eb9-67fb5cd7118d | -17.8839 | -57.4559 | 2024-10-17 07:56:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| c8afea6f-1e5a-3265-bc83-1d0ae803db08 | -17.8052 | -57.4449 | 2024-10-17 08:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 8239c95b-5e18-3291-863f-e68bd5995fd1 | -17.8049 | -57.4655 | 2024-10-17 08:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 2b875856-96d6-31ca-9f93-4be6a3f64f5e | -17.9432 | -57.4486 | 2024-10-17 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 366ddced-b56c-38a1-9726-b2c89a8a84f6 | -17.8641 | -57.4583 | 2024-10-17 08:06:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 6f6a72d0-158c-3fa3-b6fb-669ea95a5120 | -17.8638 | -57.4789 | 2024-10-17 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| cba870b4-8d73-3b6e-9abf-0f6704581eec | -17.8052 | -57.4449 | 2024-10-17 08:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| f017f966-c315-30da-b3b9-65e3ad075251 | -17.8049 | -57.4655 | 2024-10-17 08:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| f514a5e2-88fe-38c7-95c1-0c457415b7ec | -17.8246 | -57.4631 | 2024-10-17 08:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 71ee19b0-8712-3515-92c0-2c945b8bf105 | -17.8638 | -57.4789 | 2024-10-17 08:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 86a3bf04-d05d-30c3-a79a-41ea36667da0 | -17.8641 | -57.4583 | 2024-10-17 08:16:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 9a083db5-8d4c-379b-9a2b-50c6c0bfeb71 | -17.8049 | -57.4655 | 2024-10-17 08:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 590e87c5-a349-3d00-91e0-49d53daf0259 | -17.8052 | -57.4449 | 2024-10-17 08:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 5af5b105-b3f1-3ce1-ab57-3f64228e7bf7 | -17.8638 | -57.4789 | 2024-10-17 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 43684356-952c-3eb7-8995-4de7a5f33f50 | -17.8839 | -57.4559 | 2024-10-17 08:26:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 27208e6d-b3c0-3041-a5e6-cfedf10b5a67 | -17.8641 | -57.4583 | 2024-10-17 08:26:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 4fcf272d-ab86-33f3-97ce-2a3b450c8317 | -12.4964 | -63.2258 | 2024-10-17 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 0ec129f4-5a80-3d87-a242-8d3a6ea3dd97 | -17.8049 | -57.4655 | 2024-10-17 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 06b2c70f-624f-34cb-a9f7-c0e916a666ed | -17.8052 | -57.4449 | 2024-10-17 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 0f53edd6-4ba9-3a88-9287-fd62974557d0 | -17.8246 | -57.4631 | 2024-10-17 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| e87a1fcd-a625-3a9a-a127-a5db92368f47 | -17.8641 | -57.4583 | 2024-10-17 08:36:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| cb88cd51-da7a-3783-9867-43aee0cbdcbc | -17.8638 | -57.4789 | 2024-10-17 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| d7cd558d-d393-3fce-9230-1fccb0432481 | -12.5338 | -63.2812 | 2024-10-17 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a8d55ff5-e43b-32bc-8458-88010835e1a1 | -12.5155 | -63.2055 | 2024-10-17 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 15af05ed-a520-36f1-8d29-a263cf6eb437 | -12.5153 | -63.2247 | 2024-10-17 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 92b2c459-654c-38b8-ae84-85c1510788aa | -12.5149 | -63.2822 | 2024-10-17 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 430528e9-fb22-3211-8d06-e6e6428e1dbf | -12.4958 | -63.3024 | 2024-10-17 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| cd5624e7-d1ec-35a3-afab-bc61743b4c11 | -12.5147 | -63.3014 | 2024-10-17 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 49c37550-ce4d-3d86-9eb6-2ccbb80214dc | -12.5338 | -63.2812 | 2024-10-17 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1f4cc4e7-f70b-3f35-85da-1fe3b1ccc9ee | -0.75341 | -48.69178 | 2024-10-17 12:23:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| ffbf98ae-58b1-3f1e-b66f-6a15943b6c6e | -0.75799 | -48.71021 | 2024-10-17 12:23:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 8cffd939-921c-31dd-a232-2db51f332ba7 | -0.76136 | -48.68673 | 2024-10-17 12:23:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f546ce61-c4a9-317d-8553-06dbe1551449 | -0.76728 | -48.69372 | 2024-10-17 12:23:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 38ce9c86-2b1f-3a34-8178-1e66a6718654 | -3.31603 | -42.27765 | 2024-10-17 12:25:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |


[Clique aqui para ver as próximas entradas](README68.md)
