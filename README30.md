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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8377076f-cd2b-3bd7-ae8d-7239a7538181 | -3.17768 | -50.29535 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1d6708a-f946-3459-a954-6812acd1686d | -3.07228 | -50.36403 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc346f8e-d11f-3a0c-86cd-75a732a90594 | -3.06984 | -50.49875 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12a22953-e51b-3f43-9b46-6390902b16e1 | -3.06929 | -50.50231 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63bf52d7-5a95-377b-95c3-d732541668e4 | -4.90729 | -50.3969 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fac631c-d4a3-378f-a9d8-7f1805f48a0f | -4.59742 | -49.51666 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ebcb191-931a-34da-b7cf-0cef0757f261 | -4.55108 | -49.65331 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c39ac639-05a4-3547-a756-ab2729892560 | -4.44902 | -50.1539 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b22d352-bb86-3807-a96e-71f7b497a9a0 | -4.41161 | -50.53083 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba004e76-adc3-3ac2-8147-12636c01c369 | -4.41105 | -50.53445 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5db1a9e-dd81-3cfb-afbb-1763880e2f04 | -4.40285 | -49.74989 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b72369ae-cb70-3422-8562-5971d21d1d25 | -4.39936 | -49.74935 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10c5e9de-de37-3918-a4c3-94b7f3291859 | -4.33574 | -50.68502 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bdaf66c0-8103-3838-8198-cce5f7898d14 | -4.32651 | -50.81167 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17d0a8f8-06ac-318b-b406-48e0959a4feb | -4.3237 | -50.80758 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d22f8652-88b8-3ac2-8e66-6905e1da4dc6 | -4.32314 | -50.81115 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f766d4cf-898a-39d9-8b32-47f9cfb28ad6 | -4.2638 | -50.29283 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 217f17ce-3da2-327b-9bff-049794ecfaba | -4.25867 | -50.3033 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 265d2dde-990e-3a02-91c9-4893615c8b99 | -4.12973 | -50.75272 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01d9fd5b-cf28-3fdf-9d2f-33cfc8ccf2f6 | -4.09585 | -50.76171 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fea61167-3906-3cf3-9501-eb6133f04dce | -4.09448 | -49.34386 | 2024-10-19 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36fbe965-0243-3d8d-b3e1-d77d51e47ab2 | -4.04302 | -50.43388 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47434988-243f-3948-8a55-63e4ecee4ee5 | -4.04275 | -50.43427 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57b81338-c98b-3bd7-93fa-47360b37ae7a | -4.04247 | -50.4375 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7307d54d-bd41-376c-a9f2-3082a5aed91e | -3.97182 | -50.71 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49ab6603-9a4e-3b21-bddb-97f791d44eda | -3.8744 | -50.25976 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 575df1ba-7581-3905-977d-2218c5c48cfa | -3.87384 | -50.26341 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 782dcad3-d879-31ac-9f73-44fca732808b | -3.87133 | -50.54825 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98f8bc21-216f-39a2-8864-36e16a75794e | -3.85435 | -50.07679 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d1899f2-972c-3e4e-ada6-c5c48cbc4e53 | -3.85092 | -50.07626 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80b3f0ce-9d5f-38eb-b90b-8c9c36ebefe9 | -3.84958 | -50.68762 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b3be99b-c3cd-315a-a079-d523bb3b6fe4 | -3.76733 | -49.98439 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88d63249-fc7f-3d59-a558-151b4a566060 | -3.60428 | -50.58467 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ece7e5d1-6103-3a9d-a6ed-8837ad2df2ad | -3.59665 | -50.16182 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b26d15c4-aeb1-3276-9655-40797256c8ba | -3.58983 | -50.16078 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54e78fbf-7770-3db7-91ef-8aa4f1b544f4 | -4.25924 | -50.29963 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73d6d3de-7364-33cd-9cb1-8f1b030ea3f9 | -4.24063 | -50.71093 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 957a0d3f-5956-3257-ac03-334d2cdbd10b | -4.13028 | -50.74916 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e54bcdb-9e31-3101-a6d0-ab7e945eed10 | -4.09641 | -50.75814 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff0a5ba2-e91b-3e47-b6b6-fe4eb4514e61 | -4.04218 | -50.43788 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41c015b2-aac6-3145-b352-9f1f8e3aae40 | -3.95958 | -49.89016 | 2024-10-19 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c2f0bfd-d1e2-302f-a37c-6885d6b92ddb | -3.93658 | -49.83268 | 2024-10-19 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 639a88ea-8e55-3caa-9be8-6b3fbd603b56 | -3.93255 | -49.8359 | 2024-10-19 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 763d9991-2ee8-3dd5-9771-2abec6238d89 | -3.87077 | -50.55185 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7537951-5836-3f69-9e43-7b4426acd8ab | -3.86449 | -50.48094 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12dbb40b-70b7-3cc2-8acc-3ce55d7f9c9d | -3.86393 | -50.48455 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81b3c314-3592-39d5-a895-58c3621527d9 | -3.76675 | -49.98811 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edb5efcd-ce15-312c-ac1b-23441e710d11 | -4.95289 | -50.8708 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86872311-bbe4-3baa-bba5-a61a999b0c39 | -4.88137 | -49.75329 | 2024-10-19 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 980d6a28-6375-39a6-a296-445dd9c75ccc | -4.55458 | -49.65382 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69a5aa20-9d5f-3e51-9d51-9a105f37d615 | -4.55398 | -49.65773 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8151dab4-2c97-3800-b80b-841fdd13e39a | -4.55048 | -49.65721 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a19aaa24-b8b5-3b34-867a-08d60ab51085 | -4.5136 | -50.45682 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b0c6380-ed08-3d22-b49c-62e2effabdc2 | -4.49655 | -50.14223 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a18b4a1c-d441-3aca-95f4-224030468ab2 | -4.46718 | -50.35304 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c361550d-fb62-3893-b388-b1916c69951f | -4.40822 | -50.5303 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4091238-7520-3999-9dc8-e13518eb7b4c | -4.40766 | -50.53393 | 2024-10-19 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccd64b7f-7121-37cc-ae3d-64a80e5cf386 | -3.6009 | -50.58416 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab039e4c-3a2c-35c8-ab96-6fce43a539ae | -3.5882 | -50.571 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db982acc-cac8-3b66-8dd1-bfcb88559367 | -5.02769 | -50.45201 | 2024-10-19 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4310f4ee-e0af-3826-832c-5b501678b9a6 | -5.58148 | -51.04756 | 2024-10-19 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37276370-6dc1-3beb-88e9-8fdbd17012d3 | -5.50973 | -50.58448 | 2024-10-19 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28c416a3-d6b9-3732-a479-a318f92b6e3b | -5.50916 | -50.58815 | 2024-10-19 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c45cee1b-55c0-346c-966f-e7759c19de4e | -5.50632 | -50.58395 | 2024-10-19 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0879f446-4c8c-3d15-9535-97e3c1ae007c | -5.50575 | -50.58762 | 2024-10-19 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97c6ea4b-884c-382f-a170-88dbb2293cd0 | -5.50518 | -50.59129 | 2024-10-19 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2d249c7-81e5-361b-99a9-2e500dcdc35e | -5.03111 | -50.45255 | 2024-10-19 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| faddb05d-9032-321a-841d-4ba1c9ceef32 | -5.03054 | -50.45622 | 2024-10-19 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfaa411b-165b-311f-a014-0b0037b9732b | -5.90365 | -51.08248 | 2024-10-19 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2567a18d-e385-3ff7-9896-6e617b7572db | -1.58937 | -51.70068 | 2024-10-19 04:49:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47060e9a-ff2c-3cc6-add4-154fb3f550ff | -1.33739 | -50.57099 | 2024-10-19 04:49:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d0733dc-bf21-39cb-bb26-5646aee1e1bb | -0.92805 | -51.3885 | 2024-10-19 04:49:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 367d0f81-c39c-33f3-9bab-5fad2d32bd1d | -2.17074 | -50.52383 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48f43736-ddae-3e31-b5b3-44682d4fe10a | -2.1626 | -50.69912 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b501919-7daf-3e47-af5b-7367596850c2 | -2.14803 | -50.83622 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09bfe451-42bb-32f4-b857-756f1bdfaec7 | -2.09789 | -51.43784 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 182ad4ca-1105-3f41-88ec-2c5e5dfab67a | -2.17019 | -50.52735 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21a00566-8313-31c9-9381-7903657682c6 | -2.13616 | -50.83025 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2666f4a0-f189-3da4-890f-caf4d1d974c1 | -2.13561 | -50.83373 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 896273cc-b44e-39a2-99d8-49863b9bf8a9 | -2.13366 | -50.69411 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c50b7f2-90ac-34fe-9ded-3c70bbdb4459 | -2.13227 | -50.83321 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c67e35b-2542-3928-9a68-13f76325c6ac | -1.86325 | -51.35847 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c65ad80b-992e-3c1c-86fa-ba5bd3706685 | -2.09843 | -51.4344 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07a63491-3ecf-3205-b4c3-0a9826699da7 | -2.65666 | -51.84274 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b315402-149f-35e2-b83b-0e3896268de8 | -2.62587 | -51.7602 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb756512-d9b4-38eb-84ad-6d0f443f9572 | -2.62532 | -51.76365 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65129f3a-a2a2-3c10-833d-9e486ae025a0 | -2.62478 | -51.7671 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8004957-f4e1-3e55-bc0e-dfbbdcb665a5 | -2.58319 | -51.92319 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d8e2b6f-4bc9-3bb7-a133-6442b5170129 | -2.55436 | -51.24695 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7f23b1c-873a-3a34-b427-f355a5872e2f | -2.55213 | -51.23952 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f6026dd-277a-3b5c-b65f-f2d93c475259 | -2.51518 | -51.8203 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c434286-06c0-3b86-b893-0d99c5a90797 | -2.5124 | -51.81633 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51aec7d9-2fee-3d86-b907-050b21b71abf | -2.50854 | -51.81926 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a93e5027-6a9d-3787-bd3e-e8b8e1179c32 | -2.30181 | -50.82777 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb70ea79-46c5-323d-836c-7506700df30a | -2.28323 | -51.14133 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95692cde-d0d8-343d-bb70-588ac7225814 | -2.27769 | -50.55528 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf335618-c36c-3a4b-bf58-6194654a700b | -2.27024 | -51.2455 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37a2dddf-315c-3c77-9c2f-98a085fcc166 | -2.26305 | -51.24792 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a594b222-4868-3d89-a542-e1b1f0de829a | -3.28262 | -50.9402 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 524b64ad-c54d-3be3-9cc5-0cef0297d1e0 | -3.27983 | -50.93618 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README31.md)
