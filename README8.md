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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79510a28-5538-3a5b-a5e2-c2fe7252f957 | -1.6328 | -52.371498 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad8c9a19-7274-3076-b8d6-d43f2d6865f6 | -10.6494 | -44.487499 | 2024-12-03 00:37:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0475ff18-bc43-3912-8045-4d4f85f505d6 | -3.1165 | -45.9814 | 2024-12-03 00:37:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 344fc3cf-e345-34fb-b9f3-e714a9442db8 | -6.1081 | -43.949402 | 2024-12-03 00:37:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98ce5a9c-fad5-3980-b40b-64e5ec7fd813 | -3.0308 | -54.053398 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3db601ee-d50b-3db8-aeb5-b29d56aa0ff7 | -4.1842 | -50.665298 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4c4ca49-bb38-3773-a602-eed6dc74250e | -1.7448 | -52.639599 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85dc5026-bc4b-31a9-939d-d59b5d26355a | -2.3339 | -53.7924 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5920f930-8d7b-3686-b9dd-630fc924801f | -4.0489 | -50.569 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0f08828-8a89-355a-9070-6a193e0302d9 | -2.6782 | -46.616402 | 2024-12-03 00:37:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1aec90ae-7f27-31ec-8840-99cbd196c61a | -3.2627 | -53.617599 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57ace815-70af-3ddd-a7ff-466db7243b0c | -4.7401 | -45.1059 | 2024-12-03 00:37:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3968d2cd-57ec-33ae-888c-d7b6b0887492 | -2.3756 | -53.657101 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c97d85a-3b3f-3be0-839f-7f5560c4b63b | -3.7032 | -51.819099 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e105066-40d4-3ae3-aed4-5a55f03a765a | -3.2708 | -50.319599 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d536fb5-604f-3670-a38e-960f782ed647 | -1.6203 | -52.6814 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4c4419e-3a83-3a30-b3a0-c56512ca3142 | -4.4012 | -49.7621 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eaa5caf-7aeb-3e47-b601-d77135d09015 | -2.7987 | -54.028198 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8bd64e7-7f31-3864-b300-ccb1c402c39a | -4.047 | -54.226299 | 2024-12-03 00:37:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4df0a423-ed4b-3518-bdf0-52d000af8c27 | -3.055 | -53.4263 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fec08b8-a929-3b3c-a17d-778daa435aaf | -3.3387 | -50.165501 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9175d6b2-62ea-31ac-a2e9-ff6d2aba19f2 | -1.9496 | -53.319801 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97384e5f-dbce-3aa9-a1c9-8f12ef9d7f71 | -2.7171 | -45.193401 | 2024-12-03 00:37:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb0d9f2c-774d-3643-83a7-f645ac48e894 | -12.4908 | -46.341999 | 2024-12-03 00:37:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b25ce794-e8d8-3ae6-aad1-60693fbfd50d | -0.3526 | -51.585602 | 2024-12-03 00:37:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9239b065-b250-3c98-b0b4-3c17c527eb79 | -4.1496 | -48.574799 | 2024-12-03 00:37:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 952fc096-b369-3d31-bca0-f33b93444a5d | -3.3164 | -50.022099 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 983125a2-278a-31b9-8ba6-bba871982402 | -2.4456 | -54.014999 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bee46c8-1fac-3600-8b45-dbfc8f9a3f97 | -4.3127 | -48.209599 | 2024-12-03 00:37:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2387e14-d6e8-3f73-902b-cfa1ebfe8bb6 | -3.256 | -53.633999 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a65c2d5-eca3-36be-b34f-9e223e50a9c9 | -4.0493 | -46.8074 | 2024-12-03 00:37:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 985d4d24-6713-3a5f-87f5-cb662299aecb | -3.0226 | -54.017101 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e854657-5c84-32e6-94d4-fc96bc767704 | -3.112 | -53.266998 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b2c595b-738c-3a22-a5ec-e69c8cfa2c1f | -3.6022 | -45.5979 | 2024-12-03 00:37:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 170312a3-7941-37a7-90a3-d3bdaaff3def | -1.0718 | -53.448502 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e759152-f00c-35b5-af67-3d20513eb3f9 | -3.0705 | -50.981098 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b6f8689-7bf4-3c36-8252-74d576143ff8 | -3.5925 | -45.600101 | 2024-12-03 00:37:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36ff44a7-3bb2-3e48-bcb1-aa505108f94a | -2.6705 | -52.448898 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 346b8b89-f2e7-3ba6-b309-0c8e2a4eee52 | -2.5526 | -53.3904 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7fb947a-56b9-3ee0-82a8-00bcaee62647 | -3.394 | -49.774799 | 2024-12-03 00:37:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbacf5a5-44f1-35fb-aa4d-1e389351f5dc | -2.7766 | -55.357399 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0abfb429-b7f4-33cd-b163-01629e0cb4e3 | -3.5368 | -50.175201 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d2d503d-d4ea-3318-bd9b-06162fb567cf | -2.5459 | -53.406502 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b497792-4178-3ce8-a8bd-39c1b078d771 | -2.2284 | -53.689602 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9464e21c-bb94-3f94-838a-98eb2c9bf7ee | -1.1782 | -53.417702 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d60ab92-7d0a-3298-988e-be957399e253 | -4.9016 | -49.921799 | 2024-12-03 00:37:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91709ff9-b267-3546-a366-1386a7446fb7 | -2.3355 | -53.7995 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5695a3c-e659-3531-89e2-a6570c83b1dd | -1.2548 | -54.536201 | 2024-12-03 00:37:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bad0778-4b31-3916-9788-19dba6ad21e2 | -3.0932 | -54.286499 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d706def-1430-3d24-b5ea-e4e64a16b3c5 | -4.7358 | -45.6973 | 2024-12-03 00:37:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92e9e394-c973-312b-aea6-f72d436ad3d0 | -2.1858 | -54.004398 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de696044-b75e-3821-b885-b1795931bbb7 | -2.148 | -50.685299 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e639af5-47cd-3315-87ea-4f972ca51310 | -3.1886 | -45.279202 | 2024-12-03 00:37:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8e6ce0d-7ec0-3cc1-997d-1345a0c5510c | -6.1043 | -43.9338 | 2024-12-03 00:37:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa00456c-6253-3c0b-96cd-8241c5799000 | -2.8029 | -53.037102 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47d71fe4-14b5-33bb-84de-6f153b6a18d7 | -2.9788 | -53.8675 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2eee0e-fab1-347e-abf9-c89a7309e088 | -3.1011 | -54.045601 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0df0ade5-f0de-3426-920a-47e425df470d | -1.7334 | -52.634899 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6115bf2-18e2-3212-88e3-fb414f93a360 | -4.265 | -50.839298 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81a633e8-1e34-315a-9d15-f7c9596581c7 | -1.7574 | -52.7869 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c3ddc92-afc4-3157-9007-471d4f5fe605 | -3.1026 | -53.225201 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 849f52df-739b-3134-835e-71df62171916 | -4.4609 | -45.709 | 2024-12-03 00:37:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1a80450-3eef-32b5-9202-85ceb14fd552 | -6.1118 | -43.964901 | 2024-12-03 00:37:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e478de56-a422-3a7b-aff6-7a1ea2bb02f8 | -3.2548 | -50.5667 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eacc341-e5f2-36c1-9e30-39c68ca34b57 | -2.8019 | -54.042702 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c0e0e3c-4128-3bbb-91ad-76bbdab29cc3 | -3.5564 | -50.170799 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be1659e6-1e2f-3ead-beb8-b3ab07003d71 | -3.3331 | -51.2304 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24bcef4c-bdf4-3762-b672-497136759eff | -4.5347 | -42.915001 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82941678-a5bc-3739-987e-caa60584e430 | -3.0185 | -51.525501 | 2024-12-03 00:37:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba497e61-4e85-39c7-9847-c9b31ef45456 | -1.7873 | -52.280102 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b32bb732-0a13-3b16-a3e9-b6aa0521bb60 | -5.109 | -43.213902 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efe2dfb6-1447-3acd-a2c3-0f414cb1a1b9 | -1.4179 | -54.803501 | 2024-12-03 00:37:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 997f85b4-badc-323a-9f34-ccca9fbc515d | -3.2724 | -50.3269 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f99164d-f8c7-3e74-8bcb-b48bd6c3102d | -1.712 | -52.768299 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df67d18d-0814-3a94-b7ca-16112de5283d | -3.4462 | -42.003799 | 2024-12-03 00:37:00 | METOP-B | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 382b15c4-4c65-3d79-97ca-106d7d5bbb6d | -2.0454 | -51.187401 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69c929e7-64d7-369c-92ab-ee090447972c | -3.2725 | -53.615501 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe5f446b-ab50-384b-ad3e-fd5acc58a417 | -2.4374 | -54.024399 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e814de5-3fd8-3821-aa67-85b698ec0873 | -3.2484 | -54.198002 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72c603af-cde7-3112-bbe1-ca1dc90c2819 | -4.1613 | -48.178799 | 2024-12-03 00:37:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4a07d68-e92a-368a-9060-4f4ba4ca5cbd | -3.4874 | -53.7934 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9383b386-db1d-39c1-b848-3de7a222a0aa | -3.0312 | -53.870998 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90d2381b-5111-3d2d-a57b-09947bc1bb94 | -3.3465 | -51.198299 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79c3913c-79b0-3e64-af35-3b84f8bdc743 | -1.0687 | -53.4347 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2930b3b-667e-3c9c-b843-30d8ee76b036 | -4.7533 | -45.640598 | 2024-12-03 00:37:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c614bdd9-0935-32c8-a961-4eea783f2c4e | -3.2627 | -46.919998 | 2024-12-03 00:37:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47a5bbd9-3dc7-3a26-b2d8-ac95f6381c23 | -2.3692 | -53.903999 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4dd2c93-b996-3af4-96b4-0bd0f7018a80 | -3.3741 | -51.001801 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f08ee34-4d85-3bfe-bc5c-2f12740c8e32 | -4.2911 | -48.2052 | 2024-12-03 00:37:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 546dfbfa-ae9a-309e-b2ce-8add72fc97c8 | -3.4964 | -50.314899 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d62f80a-fa2a-3423-aae9-e3b7f5247f33 | -3.4938 | -53.8223 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bef01541-2b38-3b65-9d22-cf78f43f977d | -1.7331 | -52.770802 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 567d7994-c62a-33a4-bcca-f70e29fb72cb | -2.604 | -54.216202 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76a83357-e1b7-3000-8321-a4bd2287d0d5 | -2.2049 | -53.768799 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 608335f9-5c98-3d53-bef5-822bb19a3f40 | -1.2434 | -54.530998 | 2024-12-03 00:37:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97d92dc8-5318-3242-b47f-1ae400a9d964 | -1.3469 | -51.3797 | 2024-12-03 00:37:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 721347e1-5c72-3b92-a634-8c8615280466 | -3.0229 | -52.549702 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 409ce5fd-dcdf-3894-b992-d2b89faa91e2 | -3.4506 | -50.294601 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| becfc121-cf29-3a08-936c-95dabd6379aa | -2.3437 | -53.790199 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a0ac341-8550-320d-ae43-11768b6e36f1 | -3.6903 | -51.077801 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
