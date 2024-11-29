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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10f4894b-1109-3677-9450-fae012c4d08f | -3.16392 | -53.64503 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11d66352-1339-36ba-ae69-a2f2dc493036 | -1.68427 | -52.53036 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 750a133f-adf2-3e8b-af15-4e66c160f5d7 | -2.14834 | -50.9074 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 742c9669-cb2a-33ac-b4b7-db5ff1810d89 | -3.10516 | -53.25514 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82dd09c5-b367-3c7b-aa11-8515b9486e03 | -2.8623 | -51.82116 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53a9e6ec-c87d-367a-a4b3-836dfbdd0ded | -2.93791 | -48.589 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2053272-aebd-3d1d-b8f0-67e01c1a2675 | -1.69014 | -52.44915 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5a03945-b5c0-3d41-85e0-5d516d0a430a | -2.467 | -53.96857 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 447d83b8-df45-3df8-b3da-fc1e9f27ba49 | -4.82634 | -48.09828 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51219631-5fe9-3698-9a20-86bac39d0b54 | -3.22996 | -53.39483 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abb424bb-8f43-36c6-b356-bade8e159592 | -2.10927 | -50.36517 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccda31c6-20fc-3bb6-9cd9-9468d21c31f1 | -2.79651 | -54.12263 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ffbfcbb-dddc-3bab-a743-44e708aff7ea | -1.45374 | -54.48627 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77957c81-50c9-39d0-a2d7-940778af8633 | -1.35962 | -54.97694 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1036514b-5d8a-3880-b9c2-0ade37bc4caa | -3.8577 | -54.08116 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b89c9391-c8c5-31a8-a648-a20543a247df | -4.06081 | -49.0689 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 505efecd-8ece-32b6-bd43-b028b20eb6c2 | -1.70346 | -52.4512 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 78caae0a-4e15-30c6-946b-665be4374cdb | -2.46766 | -53.70063 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b3d61ce-3756-3d1d-9661-6e0b7cae8d3b | -1.99056 | -53.29232 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b4670a0-e9fe-34ea-9039-988e9443bc1a | -0.95005 | -51.65784 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a796dd15-559b-32ac-a8f2-bf89b87cd9b5 | -1.88456 | -54.40642 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09e7a0d2-a2d6-3d20-9628-26545e55b9ca | -3.34874 | -50.15054 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb25cb41-4bf5-3845-82ad-dad2d460ace9 | -3.34888 | -50.51717 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 391e9eda-e105-3123-aa50-21913331959f | -2.97422 | -53.28785 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| bc55ccc0-c5fe-3796-ad61-1236c161d122 | -3.09551 | -53.73234 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9f79be2-312e-339c-ae7e-e9b23cd80fce | -3.22944 | -54.09516 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a87ca72-c054-3521-a14f-ec4a0d7b1ea0 | -2.80999 | -54.03648 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adb75208-724a-3177-a2a2-fa67185799fd | -1.7951 | -52.73626 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 188211e6-b2d1-3c76-9300-35a0e8f6e10c | -1.09841 | -53.60566 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81d5ef04-8885-385c-bae2-596e04ed9ea1 | -2.15488 | -50.60827 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06f5f9aa-1aa1-31fd-9181-bc12f1118b49 | -1.40761 | -51.58266 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04825c2c-0a8b-3659-a387-a8306352eb2b | -1.62047 | -53.87791 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 890712b3-3fa4-3455-ae56-4c4f96ab399f | -2.89779 | -53.95502 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a00de22-d2a3-3be5-9e81-6f830142d5b4 | -1.20067 | -53.88635 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47d281ea-94df-368d-83c4-25cc7599e215 | -4.21258 | -49.31089 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8872ea0b-d74b-3409-92ec-afea6d6ff215 | -2.54333 | -54.04383 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 892d64f9-3acb-3a9c-bcde-66071e1ba31c | -3.04391 | -54.04102 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13a928e4-23b1-3f52-82f7-5b7be02d4f79 | -3.7149 | -47.14446 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b8abe91-9bb5-33bd-bd49-8fdef6bdb513 | -2.87283 | -45.79188 | 2024-11-29 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aea4cdd-6a88-37a4-90b7-b3d0573603c9 | -3.16739 | -48.5873 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b57ae49-5e7e-3919-b875-8bb9b877e95d | -1.45708 | -54.4868 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f4dbe96-9d81-3bb8-882e-52de17a28501 | -1.42457 | -54.30209 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 143fd5a7-c581-3924-95f6-b0c50e976a41 | -1.08352 | -52.43414 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f30b4860-3c70-30cb-a776-73724e62293a | -1.30752 | -51.95766 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26a243ed-197a-39db-91d6-69adcd140aa6 | -2.24884 | -53.62103 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae11ff2-e11a-3b6b-b833-ddeeb3e3fc04 | -2.46384 | -55.28093 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 397888de-4ed5-32bc-8235-7f954fc5f7f0 | -2.95573 | -51.28676 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbaaeb36-17c2-3f97-8d4e-204e67bf5b8a | -1.61699 | -52.13237 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2570ad9c-9e2e-3a23-ac87-1901d253200f | -3.05574 | -52.76484 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71f6c137-180f-3f63-9543-85e47ac50a4b | -1.38262 | -55.68151 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7ea11677-b239-3fcb-8b23-b5ea76739e74 | -2.75328 | -54.11519 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74efc1ff-b0cc-3754-9768-93f4e32660cb | -3.0954 | -54.55996 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bedab05-09d4-386e-9d21-7b248f0a3570 | -1.18288 | -53.41137 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 163aea95-cb20-3745-8610-3777ce5b570b | -3.47079 | -50.2549 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6915afc8-a6ff-3860-8e5a-cc8606b443b0 | -1.16968 | -53.66936 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1519c061-817e-3cd3-bbc2-f16b7071df7e | -1.93552 | -52.88181 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1413ee34-ef29-349e-b66d-6f3212d646ad | -2.88183 | -51.58159 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 796bde4e-3f7d-3bb4-95b1-26118d68d92e | -1.17641 | -53.88969 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4b1a9e77-62a4-3787-be5a-ac4aaa3927fc | -2.25929 | -53.74918 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c76e08b1-6789-3973-92dd-0396f4175bfc | -3.79403 | -51.25769 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 55c1997e-1f14-38c2-b7ea-73c25e155850 | -2.78579 | -53.20879 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c0450a6-09a4-3b85-ace7-64d2bb2fd593 | -1.29351 | -51.37045 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f07b3aca-bc09-3f86-b497-e7c4103fdaae | -0.27633 | -51.63553 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d63f5662-5c25-342f-9df1-9144a26d7a61 | -4.48405 | -48.19071 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d211dbf1-b6cd-30fc-8f0a-6c1608925950 | -2.00096 | -51.17744 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b52feaf1-702d-3c11-82dc-f929e7c239ed | -2.83391 | -54.10014 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6419944d-ff51-3093-b86d-e90493e075c7 | -1.11596 | -53.73153 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf50846b-1251-3139-ac3f-2bf02ce674b2 | -2.19337 | -53.78125 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e59054d9-45ce-300e-91eb-4e36a923fb00 | -1.61806 | -52.45237 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f7308d3-8bba-3886-8e78-562b3e39c447 | -2.60381 | -54.07096 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d02ddab8-0559-383e-b398-63bf1a1e81b8 | -2.3306 | -50.50532 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f090861-156f-3310-a154-e34b1a5900cf | -3.38629 | -50.11916 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d27ea480-ece0-3775-afea-4d43d5811052 | -1.62378 | -53.87843 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64d79030-e45a-39c7-9325-a490ebade35a | -3.17609 | -54.32725 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27919d89-d756-339b-819c-1ca69515445e | -1.56804 | -52.00493 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fc71b46-14a7-3ae5-bc75-b78a18d55941 | -1.71546 | -52.63536 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4109121b-ddb0-3c2e-89c8-f3d1f123d1c1 | -1.10395 | -53.22012 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af10b139-2c67-308f-81b9-a65a6e2dcb58 | -2.11636 | -50.59824 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28a20b6e-4a4e-3f59-8900-40d549192a5a | -1.07775 | -53.38805 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b80f29f0-71ed-3cc4-b225-806c8b00459d | 0.73778 | -50.87102 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| aa37a57e-3e0c-380a-b2c2-f4a629fd2003 | -1.74982 | -52.65486 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b594eea-9da4-3679-b451-07c04f59c8e0 | -3.12098 | -53.26471 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d092dfc-18e9-3ccc-8245-fd46cc895461 | -2.98691 | -53.29335 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 770e66c6-55f0-31b6-8aa6-41c364ad70b2 | -1.03942 | -51.73753 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83b8f096-2ad2-3219-ac4d-d29b67d55eb1 | -2.42056 | -53.89389 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6aadf20c-9bb4-371c-85ad-f9256532d1cf | -1.62451 | -52.28149 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79b64b08-5123-317b-9949-6d30c4907280 | -4.17327 | -48.62785 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a14de1fe-b02a-379d-80f4-63280729e46e | -2.64287 | -54.27868 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bd6edf9-e801-3512-a75e-091e2edb33dc | -3.31534 | -54.09083 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e549933-d9e7-35ad-acf8-5a64eb4d6ab8 | -3.87017 | -47.07263 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1945140-4a79-3764-8c5d-dd48bed61537 | -2.70695 | -56.82529 | 2024-11-29 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3e7366c-d8d1-363c-ba0f-ed43c5d54592 | -1.72483 | -52.48721 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2059655a-f52f-39d4-90bf-c029c3403efe | -3.22716 | -48.82259 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 908eb748-de76-315c-b8a6-5dffc0276078 | -3.00198 | -53.72132 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c69cc29-3cd2-3af6-96d2-8be9634107b5 | -1.39066 | -55.00045 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19615ec9-8bad-307e-95ea-539cdd225f1c | -3.33427 | -46.7007 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19345fd7-7ce3-3add-ab65-98693480297b | -1.10403 | -48.36786 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2016269a-7d71-3281-b511-f8f64074ced2 | -2.45992 | -55.27689 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 799cc22a-4648-31f1-b576-174faaa57f5c | -2.55881 | -54.33676 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 812d3f67-025f-3365-b632-a27081dd3a91 | -2.26507 | -51.23558 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README48.md)
