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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32835fee-18b8-3d4d-9bc0-096225916313 | -2.19831 | -53.74942 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0b723183-47fc-3d16-99bc-bc68845051f7 | -1.68376 | -45.78679 | 2024-11-30 05:01:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b267282d-0b7f-30b2-9f4f-da6b08b1b3ef | -2.62416 | -54.20954 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 843f2dc9-2ade-3b55-b57b-d485cabaa15c | -0.9606 | -51.65007 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc796b3f-89f6-3a6f-8158-c0884edb6a0f | -1.2473 | -51.6329 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e1ada16-3070-33c7-b1a7-17a98a62a48a | -2.83893 | -54.1113 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4485dab-abde-3488-9bf7-9c0de7c6dcae | -3.02889 | -54.01849 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2483b773-48d0-3062-86ad-4a338a5a80e3 | -3.23401 | -50.44632 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28e3361c-2d4d-35b2-97bd-aa93d0ee779f | -3.82658 | -50.13383 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbc65bb8-1e2d-37b4-961b-683a9fea84c8 | -3.69971 | -51.79911 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a37f91af-d4ce-38f7-83d9-749c0569ac71 | -2.45978 | -53.7035 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7530cbe2-9510-3c91-b373-358503fd0452 | -2.44741 | -53.97872 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4131c010-8cdb-3b88-b724-dd461f09f85c | -2.65986 | -48.78698 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f25ba1b8-4e26-3e6e-b1f2-f9139ca3285e | -2.46286 | -46.57026 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ce9b5a5-f0f1-3952-9f76-e07a03851773 | -1.7398 | -53.74732 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c999a4d-55bf-3e1f-b66c-0bfe5d504893 | -3.48688 | -53.81391 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ac4d478d-04e8-3602-89cf-4b30963364f5 | -2.14191 | -51.41502 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ba51b16-1e99-3cfb-9473-e9e7f4b051a6 | -2.32525 | -50.68109 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99ce993c-f86c-38d0-80ea-1709ee15bba7 | -1.25611 | -51.78691 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aaa063d-7217-3c83-8e8a-723df493805a | -2.94767 | -49.44679 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e59897ec-11c0-321c-8a03-eb642efd5fe6 | -3.67625 | -54.27326 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3af2acdf-1f7d-3a13-b3c4-b29511ad4c4e | -2.61394 | -51.76345 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4bb5592-88e0-30ef-b632-f11bac07a706 | -3.0267 | -54.03252 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b51851c-5940-3b53-8f29-5cb47994c8ce | -3.20981 | -53.84098 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 392c40a9-13ea-31b9-97e7-d8501b035921 | -2.97956 | -53.88495 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10099b40-3d6e-3f5f-9af6-2c4d86fa5f52 | -1.38474 | -52.5631 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abda56fb-ed50-3cc6-b94a-962476d62b6d | -1.89729 | -53.01503 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8d19d15-ba86-3b37-96cb-d095a652e00c | -3.1083 | -53.10733 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 121c6b31-ac6c-3002-aa9c-474354eaa8cb | -2.13753 | -49.49963 | 2024-11-30 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8a934ad-02d7-3cc3-b030-32ca97b519ce | -3.1827 | -54.33246 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 809abf1b-6a5c-36dc-af49-511799b6a00c | -3.49135 | -53.80733 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c099c57-5689-3864-84b4-9eb92dd00c2b | 0.9497 | -50.75735 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5d38d94-6a62-31d0-b3ab-13b077176a8b | -3.53738 | -50.18348 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e79d77b-47ca-3e30-947e-3ef772400897 | -2.60399 | -54.35926 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7e61e25-b754-3e4c-b430-68868c914719 | -3.61257 | -54.74396 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9888a446-d9c5-3e21-83e6-36baec6277ff | -3.29091 | -53.65985 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c297ce4-a6fc-39ce-b392-5b8403dbb5d3 | -4.30846 | -48.23225 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1965421-7e09-30a2-b62f-9b2bd86e3f1f | -2.31893 | -50.6465 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c55c41d-114a-314b-875d-6494f285ee92 | -3.44053 | -54.06762 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23224813-0eff-3974-8a0e-240ae9d3a2ba | -1.18496 | -51.77592 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42174501-af46-329e-bb91-6aa940d91464 | -1.59163 | -51.26361 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32f9fb1b-00a6-32ec-907d-69a2cec3a767 | -3.41968 | -50.16565 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 125d56c5-db0d-3ea5-92d3-b50265633d49 | -1.26331 | -54.55675 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 203275ac-1886-3f36-a063-2bdc68eeb9f8 | -3.3756 | -50.18051 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c40f933-2030-3968-b832-7dca9038eaee | -0.10817 | -51.4979 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36b11608-7e02-3c6e-880e-d4e8fefd1fbf | -1.69985 | -52.64467 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 02470cb4-0429-3a9d-8de6-4f372cabf7e5 | -2.83692 | -48.47617 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76185bca-563a-311b-aefb-e2b01d6d1fec | -3.04902 | -54.04317 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be1046f5-9840-3ea2-9e8b-67100fc6f516 | -2.60919 | -54.0001 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21a6e67e-e6a4-300a-8a56-204affe54043 | -2.42166 | -50.47899 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 910be0fd-1ac2-313c-a36c-5a6b1b0cb54e | -2.24306 | -47.98982 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34a61bd4-f71d-3046-b7a8-51227f3f10c5 | -3.05142 | -54.41547 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf967885-4caa-361a-b78f-caa9cbbbb30a | -3.78841 | -46.69463 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba99afc5-a042-3af5-85b2-338eff3160b2 | -4.43466 | -46.00917 | 2024-11-30 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83e7a099-35fb-34d4-bfeb-25e7c228faec | -1.11156 | -51.74136 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a65be5ba-1e1f-3033-8512-691dec4a4f1b | -1.59219 | -52.2883 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b423bac-7a47-38ee-9002-26877dab4e65 | -3.0852 | -49.2132 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa009266-3fc7-3d2b-8d4f-4ced0d9d6976 | -3.33254 | -54.15547 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4bee435-2ea3-3acd-9368-6be41f89e5ee | -2.78839 | -51.7163 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 870426b3-dcb2-3e4b-9378-c72df2f873af | -2.96696 | -53.72342 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2cee02e-9395-3ae9-bf21-08c7269691db | -1.31683 | -51.74174 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e7db35a-3f4d-3232-bf22-b32a5e670a5d | -2.91261 | -54.11549 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62f66ba8-06a0-34c6-9fb7-39e7798b13a1 | -3.3187 | -54.17833 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e284dbed-2185-3153-a916-7828010d3d3f | -2.98741 | -53.90063 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81f7e03f-d1c4-358b-a22c-30e1e6eb9dd6 | -2.79978 | -54.03359 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 28272ac5-b972-3573-9577-09e0afa14552 | -3.84503 | -46.52182 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3f415f7b-8d19-3b89-af48-1202d0497712 | -2.73726 | -54.02761 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 665f09cb-07d1-3e3e-85a4-030070651c8e | -3.34532 | -50.52368 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1cae91a9-7a2d-3a6c-9a3f-173363618b7b | -3.86127 | -52.39382 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a0321bc-0d0a-3cfd-b65a-57eaa47b1093 | 1.10192 | -59.58876 | 2024-11-30 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c8d7a8ce-3ef1-32e9-9ae5-23a516c2d40e | -3.11366 | -53.27389 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32f5b9fe-1b6f-3e96-b9f3-983f0f2b99bf | -3.0989 | -53.81244 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8227b7c-f3fe-3777-a17c-18ec2fbba0b0 | -3.48355 | -50.21404 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd557463-cbd9-3c0e-a1a6-54bfebbb1d83 | -3.69875 | -47.1348 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36df4993-d60b-3d00-a098-319d89c0648c | -3.09483 | -53.72832 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37e8f1ec-139e-36d2-8d7d-af3a7830ff30 | -2.00642 | -51.16337 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b4da64c-daed-3c65-b663-1e05ccb54e19 | -2.98488 | -53.29176 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a4e4254-c0e9-3b06-bbf1-3af8e633576b | -2.27924 | -46.43707 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc1c2e93-8991-340e-ac23-67e3d1e424ca | -1.32102 | -51.73829 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0c7e236-ce1b-364f-a75a-9a70ca8cbe70 | -2.96359 | -53.7229 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 276e69f8-5b44-3eb2-8e7f-1719f5ffadd5 | -2.45027 | -54.02569 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e3e44ae-cd83-34a1-b16b-ac772a710ad9 | -2.264 | -50.36084 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bb4a056-a9fa-31f8-85c4-53f90ea84842 | -3.86483 | -52.39432 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f8acbaf-92f1-310e-b330-998eb6b07e2c | 0.10498 | -50.47815 | 2024-11-30 05:01:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8721da46-2c4d-30ea-862d-73474d6fb345 | -1.49292 | -52.43719 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4cb3eca6-ce66-319b-a88c-50f02209b9e3 | -1.83354 | -54.52602 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 452b818f-5a2b-37eb-bee5-5ed14b0a1368 | -2.04364 | -54.69242 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39c37f05-9aa9-3678-9eb9-4aa846b6f286 | -3.98972 | -46.65624 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6611380b-2283-3a75-9e4b-dac77a983634 | -2.85207 | -48.10008 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1517a0fa-aa4e-3337-a7f9-948e000bcb81 | -2.78354 | -49.82842 | 2024-11-30 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 484296b2-9290-376a-abb2-0363bca175a3 | -2.1026 | -50.34404 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 416e7a84-c096-30c0-8642-d5f1d0c538b7 | -1.69133 | -46.77974 | 2024-11-30 05:01:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 243e0181-64c1-31e7-ae2f-c70d15053e4f | -3.35466 | -50.51499 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d202778-6332-342a-a416-65d364391dc1 | -1.05534 | -53.21559 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b88b88e-6477-33a4-ad85-62a6816cf6e6 | -3.43523 | -51.20343 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3c8e2f6-8ad4-38de-b9bf-4ceb1e3a6181 | -3.05342 | -48.52669 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3b62149-770b-3ff6-8470-cbae234e7506 | -2.96059 | -53.8964 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5fb7ff3-2888-36d2-8b8e-e12929ded4cf | -1.3038 | -51.73146 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af05d848-aaf4-342a-bccc-e644ca6f531c | -2.41519 | -54.00951 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9292457e-b204-37b5-936c-51de49d4f89f | -3.46792 | -50.53406 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README113.md)
