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
| dbda6f98-5ae4-36a2-b8d9-a50f07119702 | -21.08 | -49.14 | 2024-09-27 00:03:23 | MSG-03 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47827181-8e4a-30df-8467-c2220b018c4b | -21.12 | -49.16 | 2024-09-27 00:03:23 | MSG-03 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b3f7d319-e166-32f5-80ec-ec022c238971 | -12.19 | -50.81 | 2024-09-27 00:04:15 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 188cce39-3674-312b-aa61-13702ac2cbf7 | -12.18 | -50.75 | 2024-09-27 00:04:15 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7725fe4-fb62-3b7c-8fd4-42529f14637a | -10.93 | -54.28 | 2024-09-27 00:04:23 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba09536a-fdb6-312d-8855-14d77dddf084 | -10.04 | -53.48 | 2024-09-27 00:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1980ecf-64fd-333d-939e-f470dcb2d392 | -1.7494 | -55.2495 | 2024-09-27 00:05:16 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 92823c94-0682-3c9e-83b9-09d23db8d5f4 | -1.7494 | -55.2297 | 2024-09-27 00:05:16 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| d4c875b0-6762-3fb4-8f89-a3b9e715d2ea | -2.6783 | -57.5893 | 2024-09-27 00:05:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| a5d271ff-7918-3bff-9580-6f1d202626ef | -2.8611 | -51.6699 | 2024-09-27 00:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| b239510b-bf27-3139-b2bc-f72945f20fc8 | -2.8795 | -51.6695 | 2024-09-27 00:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| cbd075a7-01a7-3a33-8ed0-edc0b624b620 | -3.1134 | -59.1445 | 2024-09-27 00:05:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 417b2aff-fa5c-31fe-9cdc-59446691f9d1 | -3.1135 | -59.1253 | 2024-09-27 00:05:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c25a1b56-0493-3764-897a-1013188231ae | -3.1317 | -59.1441 | 2024-09-27 00:05:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 8dfaf401-3582-364d-9913-aa3083c86e1f | -3.1318 | -59.125 | 2024-09-27 00:05:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 670e2b17-590c-326a-a7a3-481af0b5b0b8 | -3.6437 | -54.051 | 2024-09-27 00:05:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 1723d0b2-726b-3e5d-abdd-9392c5e0b03e | -3.6438 | -54.0309 | 2024-09-27 00:05:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c8407b9a-2366-3b1d-8da1-33b84bcc015c | -3.7548 | -53.8665 | 2024-09-27 00:05:28 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bdff2d9d-2915-3669-a648-243e59a5da2f | -4.5616 | -47.9925 | 2024-09-27 00:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6fd1feb8-9e64-3bed-8eed-e0aead675999 | -5.0199 | -43.7839 | 2024-09-27 00:05:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c087bd7e-5c27-3fdc-8169-80a31f210f2d | -5.231 | -45.436 | 2024-09-27 00:05:36 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3abb1d3a-a2d9-3529-a9de-8899aa6869dd | -5.2497 | -45.4348 | 2024-09-27 00:05:36 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 240fe392-675d-3480-8809-51a04d511c0c | -5.397 | -43.4332 | 2024-09-27 00:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 3500002b-7777-391f-aa5a-b2f0ede271f5 | -5.7548 | -63.1572 | 2024-09-27 00:05:39 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0e8825a6-7a25-301d-9a94-01081637caff | -5.7549 | -63.1384 | 2024-09-27 00:05:39 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| dc116236-7e85-3fda-b0f9-f7aa375c153b | -6.0659 | -44.0316 | 2024-09-27 00:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 97ad21d0-6022-3dcb-9b8f-be513e201928 | -5.969 | -64.8314 | 2024-09-27 00:05:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| f02cde4d-507d-3ead-a6d6-fb8c5f3cd4ab | -5.969 | -64.8128 | 2024-09-27 00:05:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| d1b201d6-efdf-3bae-974b-4a71d83f3d43 | -5.9873 | -64.831 | 2024-09-27 00:05:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 00600390-fb68-367f-8759-6f5451c9fdf6 | -5.9874 | -64.8124 | 2024-09-27 00:05:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 2e556d42-1a14-3622-84c3-a384d80be40a | -6.5708 | -44.1747 | 2024-09-27 00:05:43 | GOES-16 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| f1a7287b-1c3c-3c55-961c-d9635ee16802 | -6.8199 | -63.1651 | 2024-09-27 00:05:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 4a39ab1b-177e-3cff-bf79-e6204bcf36c2 | -6.82 | -63.1463 | 2024-09-27 00:05:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 61d29164-c8ca-387d-9323-48d9e88f4e28 | -6.8383 | -63.1645 | 2024-09-27 00:05:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 97f4ce2c-187c-347b-a08b-8b7524f826cc | -6.8384 | -63.1457 | 2024-09-27 00:05:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 1861b636-7683-3c88-b372-13ac2d405feb | -7.272 | -61.1067 | 2024-09-27 00:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 731e8225-1049-3368-bc72-91e1dd233104 | -7.2905 | -61.106 | 2024-09-27 00:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 54556f18-aad9-39bd-983f-9e943c1b647a | -7.2906 | -61.0869 | 2024-09-27 00:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 5081bd7e-6789-3e17-9a93-b41a783307bf | -7.3089 | -61.1053 | 2024-09-27 00:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 181bc743-4b9a-3547-9bb9-356cd4f6b800 | -7.309 | -61.0862 | 2024-09-27 00:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 27cabd12-1745-3db6-b7f4-7103ca701715 | -7.4605 | -60.4114 | 2024-09-27 00:05:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ee770fc5-9f3a-305c-a777-e5110786ab28 | -7.4606 | -60.3923 | 2024-09-27 00:05:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 254a3af8-8a7e-3f16-9665-fd7acde38cb1 | -7.4791 | -63.9891 | 2024-09-27 00:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 77dcd42f-2701-351f-9514-b17cad6b1fc9 | -7.5289 | -61.3825 | 2024-09-27 00:05:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 1649e0b8-97cb-3057-a742-9343bb2303e0 | -7.529 | -61.3635 | 2024-09-27 00:05:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 84439221-7497-37b5-a433-c89fcedb63fb | -7.5703 | -60.5984 | 2024-09-27 00:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 9a33c69b-e9cd-341a-b511-9bb0e699cac6 | -7.5887 | -60.5976 | 2024-09-27 00:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 71633300-6b01-3596-ba74-58a2168237c3 | -7.5888 | -60.5785 | 2024-09-27 00:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f8527215-a4f9-3b2c-9a9a-eb1cc6c4febc | -7.77 | -61.2015 | 2024-09-27 00:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 213.7 |
| b62a2d2a-3e85-369f-8da7-8f1a31a4edcc | -7.7701 | -61.1825 | 2024-09-27 00:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 223.8 |
| de2bd3b1-3d3a-3b66-a3d4-f4fb7e5636fe | -7.8156 | -54.7252 | 2024-09-27 00:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| c2fb4c9f-5e4d-3222-96d6-fc19958a6229 | -7.7885 | -61.2008 | 2024-09-27 00:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 795eafd5-6040-3e38-8602-f9822294b8e6 | -7.7886 | -61.1817 | 2024-09-27 00:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 027ff6c5-159e-3bfd-9080-88a11f7d5334 | -7.8043 | -61.6761 | 2024-09-27 00:05:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 17964148-43b6-3664-8e40-dfa8865669ef | -7.8044 | -61.6571 | 2024-09-27 00:05:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d039bf53-e047-3a92-bd26-7e7e9ceab16d | -7.8228 | -61.6754 | 2024-09-27 00:05:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| ed439e1a-ec21-3d51-b59f-d5cc566a9da1 | -7.8229 | -61.6564 | 2024-09-27 00:05:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 5231e902-2d5d-37d5-a49f-7644a923db83 | -7.9081 | -62.9976 | 2024-09-27 00:05:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6c1672d6-95f8-3276-84fb-c9cf93d27b8d | -7.9082 | -62.9787 | 2024-09-27 00:05:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 795a7b4e-eb27-35eb-9726-d0254a5916e9 | -8.3004 | -41.4477 | 2024-09-27 00:05:53 | GOES-16 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| cdd8b4b9-741c-33ff-9234-a4942dbb2400 | -8.3008 | -41.4234 | 2024-09-27 00:05:53 | GOES-16 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 51.6 |
| 0b0f9293-5f4e-3b6a-a200-e052f003fc04 | -8.3153 | -55.0157 | 2024-09-27 00:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d3f59b3c-4f17-3f13-8bb2-9ecf460140d5 | -8.3155 | -54.9956 | 2024-09-27 00:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 97918b89-34ea-3dfb-b5a3-f68eb433cb4e | -8.556 | -49.6112 | 2024-09-27 00:05:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 8818145d-2c78-324a-a18f-63fa84e5d492 | -8.5562 | -49.5897 | 2024-09-27 00:05:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 5b1db20d-f3c0-3353-8810-35c60a094fc3 | -8.5748 | -49.6095 | 2024-09-27 00:05:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 3f0c5437-aaf3-3684-9e9b-613916ad6418 | -8.61 | -63.1415 | 2024-09-27 00:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| cb7ae369-07e5-3de7-8f5f-ad2ab79812aa | -8.6101 | -63.1226 | 2024-09-27 00:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 4dd94cf0-815d-3e23-9fa0-145abfae0afc | -8.6285 | -63.1408 | 2024-09-27 00:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c0618726-0f97-3b2a-9443-4ac9b47b3928 | -8.6286 | -63.1219 | 2024-09-27 00:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| eefb6b32-4837-38c3-b685-ff7693c17114 | -9.047 | -61.3943 | 2024-09-27 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| eb80a2dc-4169-3ab4-acfb-4f704c7e77df | -9.0472 | -61.3752 | 2024-09-27 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| d74e6018-bba2-37ad-b1c0-ffa4a4b88dae | -9.0656 | -61.3934 | 2024-09-27 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| fb10e7fd-8433-3b53-b245-d4064ecc7be8 | -9.0657 | -61.3743 | 2024-09-27 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 073f9126-0dc3-3e8d-b1f4-87bba2c8a7db | -9.086 | -61.1245 | 2024-09-27 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 6b5abeb9-fb0c-3161-93be-37c8068a323c | -9.1029 | -61.3726 | 2024-09-27 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 7c2fcbff-da62-357e-84cb-6a2873e00573 | -9.103 | -61.3534 | 2024-09-27 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 240.9 |
| df10ac57-e9ab-34ba-9dce-bf0c0035b86a | -9.1032 | -61.3343 | 2024-09-27 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 319e6e1c-5ead-3b31-bb72-da45cfa721a0 | -9.1215 | -61.3717 | 2024-09-27 00:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 243.4 |
| a108a909-7a5c-3f66-b73f-f2489f65d462 | -9.1216 | -61.3526 | 2024-09-27 00:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 252.6 |
| fb7f5fec-c015-34a6-93b1-73e719b244a5 | -9.1217 | -61.3334 | 2024-09-27 00:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 1d611941-ce2f-31c1-9acf-ad9394cb6d07 | -9.107 | -67.8881 | 2024-09-27 00:05:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 97c2e32a-7953-344c-9129-01b24207b65e | -9.1255 | -67.8877 | 2024-09-27 00:05:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 19e31f3e-a19a-356d-b217-c263b8eefd42 | -9.1472 | -67.016 | 2024-09-27 00:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f3ab021d-ce69-34f2-888e-4e2219186d3b | -9.3028 | -65.3528 | 2024-09-27 00:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| cffebd1b-4470-36aa-876b-2ec021026e90 | -9.3029 | -65.3341 | 2024-09-27 00:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2485e37d-a9eb-39a5-9134-82ad756e205b | -9.3578 | -65.5006 | 2024-09-27 00:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| efceecb5-72be-3efb-9962-116e08a92678 | -9.3762 | -65.5187 | 2024-09-27 00:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 39e628cf-29d2-30b3-b9f1-53375de366b5 | -9.3763 | -65.5 | 2024-09-27 00:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 94cc9ba2-0bd9-38ea-bcc5-5223276348b8 | -10.3672 | -53.7858 | 2024-09-27 00:06:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 186.0 |
| e2f38ac8-565a-3542-97ff-1a086230dfe1 | -10.6434 | -45.9772 | 2024-09-27 00:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| f9ae0fe2-c174-37e3-a463-a00ae4d1ad49 | -10.6438 | -45.9544 | 2024-09-27 00:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| ecdf1163-82de-3b40-8fa2-449f13b359bd | -10.6629 | -45.952 | 2024-09-27 00:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| aa702b67-8e28-343c-84b8-c9d8aa233260 | -10.461 | -50.7529 | 2024-09-27 00:06:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0a0420aa-95af-3caf-b159-069c8b8ed2fb | -10.6869 | -64.1524 | 2024-09-27 00:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| d0de14eb-b5c4-32d2-a93f-bf422d3027f7 | -10.6871 | -64.1335 | 2024-09-27 00:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 8f3dddeb-56d5-385f-aa71-7a80ca5d1f2f | -10.7056 | -64.1516 | 2024-09-27 00:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0d9da786-a53e-3383-8a0f-22eaa45cec32 | -10.7057 | -64.1327 | 2024-09-27 00:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b9dbc8e4-d58b-3f0c-8f9e-ba2b2a42a66a | -10.8541 | -57.435 | 2024-09-27 00:06:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 178.9 |
| 437d51e4-48c1-382c-bf2c-41b347f21464 | -10.8543 | -57.4151 | 2024-09-27 00:06:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |


[Clique aqui para ver as próximas entradas](README2.md)
