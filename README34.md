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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 297a8792-91bc-35e7-b1e3-8d5a477ab0f5 | -1.1064 | -51.7354 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b77c0493-a317-3d62-b085-545ac7629db8 | -2.80486 | -53.01294 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a633e746-3b3a-3163-9ca6-aa69296d0703 | -1.38051 | -52.42989 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ed56902-04fd-3fdb-bd36-146da3567eac | -2.81222 | -54.08016 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25f3d8b7-7977-38e5-90a9-abc0d2a65e48 | -2.9657 | -53.92263 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fce3e85-55eb-3609-8d06-ce0d4bb96b09 | -1.20672 | -51.74354 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56fd65b0-7cce-3ad6-85a1-09319105e8b1 | -0.81291 | -51.49366 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3798ee74-fd1b-3d4e-afd5-d9fd898b8453 | -2.87162 | -55.18008 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffe25daa-8e47-31c8-8f86-b9c821bac518 | -2.71149 | -46.26476 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e3e9081-b0b1-30cb-8730-37b886bbf31b | -3.6183 | -51.47421 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 570693bb-e8c1-3705-972c-46a35adcaa81 | -2.58826 | -51.72479 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a1f9ef4-d754-3f7b-922b-d7e93013dba4 | -1.08059 | -53.36432 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4b8d67d-5eb4-3efe-a610-c8b5bdf65b6d | -3.21142 | -51.42112 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ba4b0bb-91a0-3fc5-89e7-4e42c1b87b4b | -3.70851 | -47.11643 | 2024-11-25 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcae7f8f-ca5c-330c-aab7-39a22489bac7 | -4.36988 | -48.56794 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f5e332f-7b9a-374c-9d6f-6a080b9cfc45 | -2.78769 | -53.99773 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3aed2c5e-50fc-3a07-af5e-b0590e38e777 | -2.46342 | -53.69781 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0080b2f-a111-317d-9d47-ce5f7f2b56a7 | -1.24182 | -53.3971 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6671919-62f5-3eb0-b8de-eb1f7c23e295 | -4.36639 | -48.56366 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9ee7b28-ac0e-30b5-be94-762f9caaf09b | -2.89259 | -53.96063 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8f6ab6a-50be-3240-b48f-f1338d13d239 | -3.3515 | -51.64316 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8307750c-b1d1-39c7-bdad-4e0a32297e95 | -1.59982 | -52.58041 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 949f9949-d20b-3be4-a775-bae7be803a7c | -3.11295 | -54.14531 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3c6e748-2d66-3133-a969-56cf6000b14f | -2.77362 | -54.04915 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2fda3ae-d20e-3bfb-98ff-3c3a06e64a16 | 0.33043 | -49.72021 | 2024-11-25 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 909207be-fe0c-33f1-90ef-d0473d4b8ae7 | -3.74449 | -54.67304 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d58e34e7-49f3-387a-bad5-f3eaddd291ad | -2.54619 | -54.0533 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 220fc56d-7e73-37c2-bfe7-3ac1e640e0a7 | -0.90729 | -51.647 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 945013ca-1102-304b-9b94-04c7ee7291af | -0.36325 | -51.41387 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b551a75e-7445-327f-9513-884e3a4afce1 | -3.10785 | -54.00522 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdcd3cfb-1078-3606-931f-ceed88f73c6b | -1.59084 | -52.23099 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43e2c952-6e65-3892-953b-4b5e7cc11742 | -4.19581 | -50.68901 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 496648f5-ef5c-3f9e-9f69-2f72df93c719 | -2.79768 | -53.01535 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b88edd62-238b-3af6-94ba-08f8bddb35be | -3.81509 | -52.22788 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3653b5a-07b0-3813-916e-72050b5051cf | -2.99309 | -51.45715 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a45048e-27af-3919-a60d-09b95a1f337a | -0.79903 | -52.42418 | 2024-11-25 04:55:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cfe9bf9-f360-3d3d-8ebc-af06afd6d194 | -1.11056 | -53.39023 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b992871a-c1ac-375a-a8dc-1f3ac5ef2024 | -2.17276 | -53.26357 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f55d715c-a94c-3b6d-8085-dd465fd5fbbb | -0.94373 | -51.65628 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7eba6994-03fd-306b-80a7-ec881f0b8e9e | -3.9431 | -46.89503 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4609f009-814c-3dcc-87bf-e87b0b2b863c | -1.00032 | -52.43404 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49810838-f226-3c89-ac86-e1d8e72416e5 | -2.8054 | -53.00948 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49b8fe4e-a373-3db6-92bf-0a1e864dea97 | -1.64337 | -53.87259 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1646cfa2-ecd6-364f-af20-af0adbfef6cb | -1.25994 | -51.75542 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1de0d67-f2bc-3238-b7d0-461dcc582b97 | -3.63609 | -51.51883 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb84a830-3a95-3c92-b780-d155fec56e97 | -0.97377 | -53.70318 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a8f56b1-29ce-3524-8f62-3c9287912fe1 | -3.52948 | -53.82637 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49c79a8b-8886-36a1-892c-07dd90f20388 | -1.95025 | -52.07508 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5045b57-61c8-308a-afc2-8ad74e139337 | -2.8189 | -54.0812 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d03f1fbd-4ea3-3d7a-8a4b-0c2bfe9d14ee | -3.6402 | -50.22801 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b72ace9-fd3c-3af3-a7f9-b0a8a82d2dc9 | -0.27311 | -51.61411 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4c81b57-177f-3ca9-b8c7-866e96f72466 | -3.28229 | -54.1718 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 958f4eb0-8c9f-34bd-bc5a-a63a3e64c1d8 | -3.66639 | -51.57288 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 852081c6-15a1-322d-8bf3-d6f73c4b1aa7 | -3.38534 | -50.7378 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59c79371-2df0-31f0-8583-e17ab35e2419 | -0.79434 | -51.80999 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae73a802-9504-36bb-bfa3-3581a256352c | -3.54266 | -50.39771 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13ab4f28-b19b-30e2-87b3-196f55af212f | -2.91464 | -53.90041 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b61d78a0-db30-39b3-9ee8-93de3f24e908 | -1.19498 | -53.88134 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cbfc812-f1ca-3baf-b164-0703e4a4b208 | -3.67333 | -50.25462 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b3fca95-3f18-368c-821f-b667f20abd87 | -1.23288 | -53.36743 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37845f2d-a184-31e8-a472-3bcaf3168b35 | -2.7441 | -54.01955 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3626b681-a161-34a2-af21-b7ad0f57f3d4 | 1.85128 | -55.90242 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b0f86277-8bf6-3e9b-b7b4-f943d9c6af56 | -2.19249 | -52.13019 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ebe2eee-f3fa-398f-ac26-06517c96966c | -0.93081 | -51.62885 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8160b15-6999-37f6-8259-9ff96a36919b | -3.94184 | -47.98949 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 192316ad-8ed3-3049-8470-735dede35345 | -3.28527 | -53.01001 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 391fdb03-12cc-3771-beaa-9f2a57bf2866 | -1.48179 | -52.51625 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac9b82b4-3f3c-3b11-9de6-0da2f097283c | -2.77746 | -54.02474 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ae80adb-f5a1-3cdf-9cda-d0c4cc50c724 | -0.27367 | -51.61059 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6093753e-e6ee-316f-b5e3-1476a3bb08b4 | -0.27702 | -51.61111 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4daf6648-210d-3625-a72e-4b242422a30d | -3.03511 | -54.01896 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a229507-6caf-328a-851c-df1413830461 | -2.52788 | -54.24792 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91c8715a-b32c-3aef-a97a-95a5ce922c7a | -0.81416 | -51.59596 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64828fce-3049-3786-bb15-b71e5e407843 | -3.10055 | -53.73426 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dc1b26e-399d-3983-91e2-ce721bb4033a | -1.73875 | -52.73347 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6c230d6b-52a4-3436-9a8d-b3a9d7380ffc | -2.65932 | -51.71682 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a831ef48-166d-3d0d-b4ca-57f2027dfe5e | -3.95629 | -52.22358 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e96241c-0476-3912-abad-2377d1f6bade | -4.19519 | -50.69311 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c8cc557-d397-393c-82b2-d9b638a150d7 | -3.28784 | -53.85551 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7634d4b6-ab90-396c-a4bf-43cab6276760 | -1.62019 | -52.43489 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4de23c8-f412-3334-9bd0-4b338b45c8ba | -2.85675 | -54.10144 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd7d91f5-e60b-3798-8afa-b11a8dd322c7 | -3.70793 | -51.79717 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fbd0371-2915-3f6e-92fc-c362ebab39f5 | -3.18915 | -51.61046 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d480ae5-9097-3db3-bfe2-b6d0f18d71db | -3.22478 | -53.93461 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b226a10-0c87-30e8-80ed-789702f4411e | -2.21995 | -52.27505 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 560de761-9e61-387d-b14a-f0c9bb73483b | -2.62225 | -54.25911 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bb9aa2f-32e6-3e8b-b07b-8b872c27afc2 | -1.67164 | -53.2029 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4ed8fd8-92cc-36ca-b1b9-02ea0630a5e3 | 1.4094 | -55.88693 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef3be65d-152a-32b8-a72c-7e62fb668b56 | -3.87119 | -52.20686 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18c77666-a310-31c5-8b99-de2ea22bc31c | -2.84605 | -54.01757 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88bd73ce-d018-348e-8f4b-dbddaa734cf8 | -1.52354 | -52.07747 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0321f783-c5a0-3d22-8b6f-4d9439b89149 | -2.3079 | -51.26317 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 573910e9-5132-38f6-905a-8fff1fe7f4a9 | -2.00864 | -51.16957 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31f85a27-4d54-3b36-a1d8-b4c39c6a8dde | -1.66998 | -52.524 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc2f5418-b194-3fd0-a0b1-6f8934521042 | -2.40991 | -53.84233 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21d560b8-c1cf-3c32-a80a-16f16b64169c | -3.53203 | -50.44233 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdfaea6d-8bce-37f9-a824-7670ee38d543 | -1.12536 | -51.68026 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 565e4658-8192-3067-8a9d-0359d0bf8f72 | -1.19879 | -51.96965 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37f65d21-e452-34b0-a815-aea71b4146b1 | -3.54784 | -51.52486 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ab3d7b8-e166-353b-a69e-a04355bb3d1e | -4.05288 | -46.68908 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README35.md)
