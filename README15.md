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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 906e4293-d0ed-31ff-b303-7255ffb59324 | -5.9788 | -45.3621 | 2024-10-17 02:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e4f0d385-8b30-3638-b633-a9c98aa1d59f | -6.7274 | -43.5589 | 2024-10-17 02:15:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 64ece00b-35a8-3c8c-a9c1-773e90f3651d | -7.8727 | -45.3593 | 2024-10-17 02:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 03f91c46-70c3-3db7-beb3-209d9a17be8a | -17.1667 | -56.8232 | 2024-10-17 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 34e529df-b2d6-393e-b4be-68599ecd35d8 | -17.2177 | -57.3102 | 2024-10-17 02:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 615d9ad4-3f2e-3213-9dd0-f7c9ed6b5c30 | -17.8641 | -57.4583 | 2024-10-17 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 61f90829-5435-340b-b160-1db3af0dc2e5 | -17.8444 | -57.4607 | 2024-10-17 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 0bd43688-7419-3d21-b7e3-08cae5723927 | -17.8246 | -57.4631 | 2024-10-17 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 67eb2ab9-6360-39b9-a8d0-23eb88e2033c | -17.8052 | -57.4449 | 2024-10-17 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| 71655499-ee42-3a2c-bd62-f5a7531f5022 | -17.8049 | -57.4655 | 2024-10-17 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 7c7069f4-317d-3f63-8278-8da24f4b921e | -17.9036 | -57.4534 | 2024-10-17 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 7c424db2-3a2e-302b-825e-b9c753837ab4 | -17.9234 | -57.451 | 2024-10-17 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 0ea19cb6-ceed-36a3-a098-730de1b8fd1b | -2.6147 | -48.2629 | 2024-10-17 02:25:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 1a6d465d-de0b-3d83-b040-0b5b663e53b4 | -2.6148 | -48.2413 | 2024-10-17 02:25:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6ba721e7-e27a-3c22-9a05-6d1f7b033237 | -2.8518 | -49.1556 | 2024-10-17 02:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5c64cf9e-1cb5-3529-b372-1de203060f26 | -2.9673 | -48.0147 | 2024-10-17 02:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 3b4fa377-6da3-384c-bab7-ee2e2e5eaa3f | -2.9674 | -47.9931 | 2024-10-17 02:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 440f17b5-039c-357d-b0ae-b5e9f33bbe67 | -2.9858 | -48.0141 | 2024-10-17 02:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 9c0c0019-91f6-3740-87de-98da06294ae7 | -2.9859 | -47.9925 | 2024-10-17 02:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| b71fdcce-d2a2-37f5-816e-43c59d464f12 | -3.3526 | -53.2112 | 2024-10-17 02:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5d1ea7c4-c82c-33cf-b6e4-25b6441d7124 | -3.5086 | -51.1122 | 2024-10-17 02:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 3e6cc07f-a6a5-3cfc-93c1-d23c2fcff906 | -3.7007 | -45.9223 | 2024-10-17 02:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 9cf72653-8f1b-3ea6-80ce-9f2c565cad07 | -3.7009 | -45.9 | 2024-10-17 02:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b608a914-1168-3c07-bfc6-cf3a65618f7e | -5.5716 | -44.8927 | 2024-10-17 02:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c008edc8-e284-3cc5-8c9b-fe51f554db72 | -5.9788 | -45.3621 | 2024-10-17 02:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 0449ba50-17bc-370d-9953-5aaeb4e74054 | -6.7274 | -43.5589 | 2024-10-17 02:25:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| feca4c6f-512f-3fbc-adab-673f2557c4f4 | -7.8727 | -45.3593 | 2024-10-17 02:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| b0cde401-e762-3b30-95e0-84e4ca3aecd0 | -12.4819 | -43.7178 | 2024-10-17 02:26:16 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f4e07f88-95bb-3b89-893e-424a2c81a211 | -17.1667 | -56.8232 | 2024-10-17 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 1d073e09-1590-3251-b3ec-91a489a571f0 | -17.8049 | -57.4655 | 2024-10-17 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| b4624aac-cb9a-3564-adf9-56e20ac183cd | -17.8052 | -57.4449 | 2024-10-17 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 39190edb-1746-33fc-b906-dcd4a626fdaf | -17.9036 | -57.4534 | 2024-10-17 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 6b7a731e-5484-3278-bfb2-2618731828cb | -17.8246 | -57.4631 | 2024-10-17 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| b247afad-a748-3f85-b7bc-f12222647397 | -17.8444 | -57.4607 | 2024-10-17 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 1c32dde2-5cc5-34c0-aa50-24abe2eb3255 | -17.8641 | -57.4583 | 2024-10-17 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| a30978cd-5ba9-35c5-a612-ad626fa77fc6 | -17.9234 | -57.451 | 2024-10-17 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 09d441b3-69e8-3022-a371-3662747deb7c | -17.9237 | -57.4304 | 2024-10-17 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 353333d1-36b7-32f0-8440-3c8ead1a0cf4 | -2.6147 | -48.2629 | 2024-10-17 02:35:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 43493da7-1459-3946-85ac-d405ef5966f8 | -2.8518 | -49.1556 | 2024-10-17 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8fa2db22-e350-39c2-b5f3-b1e6b860f71e | -2.9673 | -48.0147 | 2024-10-17 02:35:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 98ac2c3a-fc6e-3ea7-aa04-d47d7f7b7adf | -2.9859 | -47.9925 | 2024-10-17 02:35:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| af5a7c93-35db-3bf6-873c-475dabcd3f19 | -2.9674 | -47.9931 | 2024-10-17 02:35:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 7c2d655e-8392-3893-b22a-c125ca8c7011 | -3.3526 | -53.2112 | 2024-10-17 02:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e454edc6-9e3b-3317-a329-a3bfeaf4a64d | -3.5086 | -51.1122 | 2024-10-17 02:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 991be2b1-27a3-38e2-a8a9-913c1f44dd85 | -3.7009 | -45.9 | 2024-10-17 02:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 780c0783-95e0-3edc-8076-f01226d0cbcd | -3.7007 | -45.9223 | 2024-10-17 02:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| dc03e73b-f0a6-3c8f-8ab2-8b80c83749a0 | -5.5716 | -44.8927 | 2024-10-17 02:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 397eeeb5-b19c-38b9-ab1b-d5bcb22dc8e7 | -5.6714 | -48.6872 | 2024-10-17 02:35:38 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| cbc4e303-6fc5-361d-9c0f-677e47786b71 | -5.9788 | -45.3621 | 2024-10-17 02:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0e017745-669b-32d4-943d-b55a66e88351 | -6.7274 | -43.5589 | 2024-10-17 02:35:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 09a16d43-2af0-32a4-9fd5-5fe53e758cf8 | -7.8727 | -45.3593 | 2024-10-17 02:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 876a2eed-77c4-3545-8af0-e74d153f55b6 | -9.1737 | -61.9039 | 2024-10-17 02:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d52dafd4-5fc3-364d-ae4d-9903f69f9a09 | -9.1552 | -61.9047 | 2024-10-17 02:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 23a04b35-c6fc-3142-b6a0-75c0fc405392 | -12.1274 | -64.7126 | 2024-10-17 02:36:15 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3975b3a0-6dbf-3b53-83b2-cd5a995b3699 | -12.0896 | -64.7333 | 2024-10-17 02:36:15 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| cbf10a5d-2ea4-34c8-a2c4-6b55cf04b9a3 | -17.1667 | -56.8232 | 2024-10-17 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| a3abf33c-c71d-35bf-b9ac-645596344774 | -17.2177 | -57.3102 | 2024-10-17 02:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| ea5bd68a-2a4b-3a93-a9fe-c7ecca7692a4 | -17.9036 | -57.4534 | 2024-10-17 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 16577631-ceff-3aa3-a6b6-c53797fd1310 | -17.8641 | -57.4583 | 2024-10-17 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| b611d71b-6676-30a7-9709-fb287f163b8d | -17.8246 | -57.4631 | 2024-10-17 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.7 |
| 4475026d-e575-3a16-905d-16ba4f2e9afe | -17.8052 | -57.4449 | 2024-10-17 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| bb842b6a-36c6-3026-8a8e-36e61dbb0787 | -17.8049 | -57.4655 | 2024-10-17 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| d3c3abdb-f007-3d33-9c6b-7615bf9a5bec | -17.9234 | -57.451 | 2024-10-17 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 9dbba597-a223-3232-82ed-c09b539415d7 | -2.6147 | -48.2629 | 2024-10-17 02:45:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f550474e-e4da-32d0-a87b-39503da4f6b0 | -2.8333 | -49.1562 | 2024-10-17 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f39143d7-2906-3310-8e87-b4fc1fc4d49a | -2.9859 | -47.9925 | 2024-10-17 02:45:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| bb31b3ff-6282-3cee-8f1f-778dcb42d2a5 | -2.9674 | -47.9931 | 2024-10-17 02:45:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 717d4da9-f1d5-3bf3-ade1-314849972c14 | -2.9673 | -48.0147 | 2024-10-17 02:45:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| e072b022-d2ec-3eff-8069-11a9cd526a0d | -3.5086 | -51.1122 | 2024-10-17 02:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3a1ddd59-62c0-365d-8f43-ef669db135e5 | -3.7007 | -45.9223 | 2024-10-17 02:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 093c835c-61fa-306c-8b66-a7a85c0c1b38 | -3.7009 | -45.9 | 2024-10-17 02:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d87e9f9a-42bd-39ba-a40a-2191fee8c388 | -5.5716 | -44.8927 | 2024-10-17 02:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| cb072728-4e45-3585-b43e-de7648c57cad | -7.8727 | -45.3593 | 2024-10-17 02:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0109c0ef-bd72-3b5e-90d0-346ea2ea7448 | -9.1552 | -61.9047 | 2024-10-17 02:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 14173bb5-a49f-3224-b6c8-647c98e3e296 | -9.1737 | -61.9039 | 2024-10-17 02:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 796db06e-0767-36d6-9481-b1db23002ad2 | -10.1288 | -56.7921 | 2024-10-17 02:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4d9e7e65-ee25-3ea7-a042-77ef0851500b | -10.129 | -56.7722 | 2024-10-17 02:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 82cf4657-d76f-38a7-a3b4-49493376b904 | -10.1292 | -56.7523 | 2024-10-17 02:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 4d95816b-2ffb-35d8-adcf-4c7967f53755 | -10.1477 | -56.7709 | 2024-10-17 02:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7e71bca7-7cf7-3300-bded-3bfba5ab2cfc | -17.1667 | -56.8232 | 2024-10-17 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 47138007-664f-30e3-9246-7419fac23ec5 | -17.2373 | -57.3079 | 2024-10-17 02:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 0d4b4eeb-ed98-3cb1-bf08-68a3c59bd4af | -17.8049 | -57.4655 | 2024-10-17 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 696a1970-05c8-3d12-9d57-f8785807d018 | -17.8052 | -57.4449 | 2024-10-17 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.8 |
| 042f2526-a556-379c-8492-48818872c9aa | -17.8246 | -57.4631 | 2024-10-17 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| 823bd25d-c71a-3328-8dfc-d7ba1984c109 | -17.8444 | -57.4607 | 2024-10-17 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 053b505c-1c9a-329f-83cf-0cd0218ca0fb | -17.8641 | -57.4583 | 2024-10-17 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 5408469b-f137-346f-b1a9-bc7064043d80 | -17.9036 | -57.4534 | 2024-10-17 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| c1cd3fa0-7b59-3634-9f7b-18454233a643 | -17.9234 | -57.451 | 2024-10-17 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.7 |
| a4a2fae0-fc07-3b48-8162-079653a01a0b | -2.6147 | -48.2629 | 2024-10-17 02:55:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b6159cd9-977a-3948-8be5-7c07f83da5f6 | -2.8979 | -51.6896 | 2024-10-17 02:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 45b42727-5142-3f4c-9e2a-6df91953a383 | -2.9859 | -47.9925 | 2024-10-17 02:55:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ffd3f98d-7ae2-39a9-8d3f-c0b76405bf0d | -2.9674 | -47.9931 | 2024-10-17 02:55:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 1574aadc-c46f-341f-84ff-050b696612e4 | -2.9673 | -48.0147 | 2024-10-17 02:55:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 7e9f8076-ac70-3938-805e-1f29ed1a4346 | -3.7007 | -45.9223 | 2024-10-17 02:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 349159d3-2b44-35c0-95ad-07c01b2cbc00 | -3.7009 | -45.9 | 2024-10-17 02:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 83333d83-a523-38ac-9827-9503de6c4021 | -3.9267 | -42.401 | 2024-10-17 02:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 2f97836b-e25c-3a42-9896-8f4e73e42310 | -3.9265 | -42.4246 | 2024-10-17 02:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 0eb68dce-869a-3c4d-9fd5-ebac932d519f | -4.58 | -48.0132 | 2024-10-17 02:55:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 7892231d-58b9-3b97-adb9-bc29b97e5f2c | -5.6714 | -48.6872 | 2024-10-17 02:55:38 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 5ec7e690-c7d8-335d-af43-5a56c46ff50e | -5.9788 | -45.3621 | 2024-10-17 02:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |


[Clique aqui para ver as próximas entradas](README16.md)
