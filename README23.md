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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6654d123-611c-39be-b2a7-d419c033994b | -9.0888 | -61.157001 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a9ca457-067f-3731-9ebd-0addb10dbe78 | -9.0904 | -61.164001 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4caf185b-5ebf-323a-98d5-62159188cc67 | -9.0919 | -61.171101 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a140861d-a99b-31d1-bd2a-ae06983a1a5e | -9.0935 | -61.178101 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 271eaaf7-9052-3764-a097-6aed8491e19c | -9.0759 | -61.1451 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 431b3203-7f9d-3379-8889-e2617943f652 | -9.219 | -62.171101 | 2024-10-14 01:23:26 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a34ff74-90cb-3125-b939-f726617f1221 | -9.1779 | -63.4035 | 2024-10-14 01:23:31 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf9594fa-a91e-3e4e-8fdb-35b877c12782 | -8.8989 | -62.351898 | 2024-10-14 01:23:32 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 943ca18a-e21e-3595-8301-d3b80a1a094f | -8.7413 | -63.4711 | 2024-10-14 01:23:39 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0047bf32-2a2b-3ab7-9c71-588747f95977 | -8.0605 | -61.252701 | 2024-10-14 01:23:42 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a300ffd-3370-37aa-9408-2ffb7a7e70e5 | -8.0507 | -61.254902 | 2024-10-14 01:23:42 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df06e6df-35cf-350b-af4d-28123562b1f6 | -8.6535 | -64.1119 | 2024-10-14 01:23:42 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33ecd6ec-cb05-3ebd-8c6c-f9901a178c1e | -8.5907 | -64.201698 | 2024-10-14 01:23:44 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4c1ea95-bbd0-3e94-bd45-408007e58efc | -8.5926 | -64.2108 | 2024-10-14 01:23:44 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d17f4156-3d04-3174-97be-e5852cbe3aa3 | -7.588 | -61.2113 | 2024-10-14 01:23:49 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c16b5583-1718-3797-b75b-393965475416 | -7.5896 | -61.2183 | 2024-10-14 01:23:49 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9cefa934-157e-3bdf-89c6-10b33c2a8d02 | -7.9499 | -63.606602 | 2024-10-14 01:23:52 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4586b4e2-a179-3fe0-ba40-58582310372b | -7.9518 | -63.615002 | 2024-10-14 01:23:52 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0de84b6-333d-342a-9896-9f43b61f5b8e | -7.9536 | -63.623402 | 2024-10-14 01:23:52 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb031417-5114-3723-8a4b-daca86cf6c12 | -7.9401 | -63.6087 | 2024-10-14 01:23:52 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5adaa40-8dcf-33f7-9800-7187edeec65a | -7.942 | -63.6171 | 2024-10-14 01:23:52 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5d6cc6f-79f3-3904-859b-b7a7e8ef3291 | -6.3767 | -59.991901 | 2024-10-14 01:23:56 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb6e5136-effd-380f-9ecf-66161ac31ad3 | -6.385 | -59.9828 | 2024-10-14 01:23:56 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f59a1f14-4465-3963-a43d-b898324f258d | -6.3865 | -59.9897 | 2024-10-14 01:23:56 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94430112-5882-3288-bd23-8ee9962e4bce | -6.3752 | -59.985001 | 2024-10-14 01:23:56 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fdce422-6f6f-3fbc-a6f6-3a56ebac42c7 | -4.3284 | -50.476002 | 2024-10-14 01:24:01 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b41ebc9-e196-3120-bbdf-bd0d4271721b | -4.3347 | -50.501598 | 2024-10-14 01:24:01 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1415c73-ee51-3727-865f-c9767b56ae39 | -4.3429 | -55.115002 | 2024-10-14 01:24:11 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ae41d40-25d9-39ce-8963-9eacb3f3dd5b | -4.3458 | -55.127201 | 2024-10-14 01:24:11 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cf4b4b3-fe4c-392c-9c7e-354af41ef44e | -3.4151 | -52.753201 | 2024-10-14 01:24:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87b609c1-9599-3b38-9b85-2e2a66b7bfd6 | -3.4195 | -52.771599 | 2024-10-14 01:24:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0284d619-3424-3cf5-bd33-620dc91b8271 | -3.0897 | -53.021301 | 2024-10-14 01:24:23 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8489444d-03e4-3d1b-a07a-5565e3e78241 | -3.0939 | -53.039101 | 2024-10-14 01:24:23 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6784d08-f5ae-3864-9dd8-0cbfd75b71a6 | -3.8253 | -55.980099 | 2024-10-14 01:24:23 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ec27770-b179-301f-8b4f-beba7fd8b539 | -3.0842 | -53.041302 | 2024-10-14 01:24:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea65b65b-e099-3d81-a31a-01fe04f3d47b | -3.08 | -53.023499 | 2024-10-14 01:24:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23657c5a-c518-3569-872e-9a79aa4aff1b | -4.2635 | -59.990299 | 2024-10-14 01:24:31 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f63b8533-dec8-3f15-9ef0-c1330f32b485 | -4.2619 | -59.983299 | 2024-10-14 01:24:31 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9c7482a-905f-3a85-96eb-0e0294fcba1a | -2.948 | -54.642399 | 2024-10-14 01:24:32 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1cce076-abe5-3f38-a9f2-37ac7172fe33 | -2.9577 | -54.640202 | 2024-10-14 01:24:32 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9ce7c89-66dc-3eb6-93cb-23fbb80e1731 | -2.3179 | -54.580002 | 2024-10-14 01:24:42 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4ee82f6-a0ba-3cb6-aa00-4d72c4f97ed3 | -2.3276 | -54.577801 | 2024-10-14 01:24:42 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 494461d3-e259-3171-b293-40ad2df40485 | -2.6059 | -57.560699 | 2024-10-14 01:24:48 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b07dfcb-96b5-3d51-b376-f700fbd5c5d3 | -1.4139 | -53.4664 | 2024-10-14 01:24:52 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f944d74-5f3e-39b5-96e9-4438b28abb3e | -1.6357 | -55.0881 | 2024-10-14 01:24:55 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9737bd2e-bf80-35b8-b02c-00002389716d | -1.6455 | -55.085899 | 2024-10-14 01:24:55 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caa962f5-07d7-32a6-ac74-032e36f19080 | -1.6423 | -55.072399 | 2024-10-14 01:24:55 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5184bc1e-da7c-3440-82a5-de31fb2e46a0 | -2.4529 | -46.919 | 2024-10-14 01:25:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 60a5f82c-fe01-3eb9-a530-81379f8af2cd | -2.6117 | -49.1198 | 2024-10-14 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 273d05a8-4143-3922-85c6-b4ebd4b460ed | -2.6118 | -49.0985 | 2024-10-14 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 89433005-2cf9-3caf-98e8-0b637a781410 | -2.6119 | -49.0772 | 2024-10-14 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| b1321de8-0b20-3d38-9a18-377748a90e72 | -3.0656 | -51.1883 | 2024-10-14 01:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 5707214d-5ff6-3063-8baf-7deb27e577e9 | -3.0657 | -51.1675 | 2024-10-14 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 987e298a-2547-3f90-a2c8-aea57fb52484 | -3.084 | -51.1878 | 2024-10-14 01:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 5acfc08c-f442-3a97-b7a3-3f07e6f8df23 | -3.0841 | -51.167 | 2024-10-14 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 553619d1-5d60-3bd9-a1fe-c11ccbaabb9a | -3.2889 | -42.8561 | 2024-10-14 01:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 9b85537e-f950-36d3-a048-0480d1d22db7 | -3.289 | -42.8327 | 2024-10-14 01:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 253b4a5a-3173-3675-bbaf-6632ff1ecbc2 | -3.3076 | -42.8553 | 2024-10-14 01:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 37c822c9-a950-37cb-85b6-a72ab6bf5bf4 | -3.3077 | -42.8318 | 2024-10-14 01:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 194.3 |
| f6e8b71e-5fd2-30ba-a0bc-2e3ce5e62445 | -3.3264 | -42.831 | 2024-10-14 01:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 9c1d8c5c-65f7-302f-b2df-526b44b06e38 | -3.1982 | -50.3077 | 2024-10-14 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 1110ca44-28a8-369b-83d4-eb9c46979ea5 | -4.3428 | -50.5172 | 2024-10-14 01:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 8f910392-9c9d-35d9-8e23-a009b89a8b4a | -4.3613 | -50.5164 | 2024-10-14 01:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e13f640b-c185-34f4-81cd-9f265782c75d | -4.3565 | -55.1291 | 2024-10-14 01:25:31 | GOES-16 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 49a28a20-9965-3560-af30-43525b324673 | -7.8701 | -44.0068 | 2024-10-14 01:25:51 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 3bb548ae-3084-3d17-bbcf-b36f284cb37c | -7.9625 | -49.0607 | 2024-10-14 01:25:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 806f65f7-c0f9-3ea8-81f8-f18b83cb90b5 | -7.9418 | -63.6365 | 2024-10-14 01:25:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 00d87507-1c3f-3314-8e12-56f18caac805 | -7.9419 | -63.6177 | 2024-10-14 01:25:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| f48069bf-0dde-3036-8990-c1eab68b8069 | -7.9603 | -63.6359 | 2024-10-14 01:25:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ec61e81b-d915-3b3e-b1e1-4adecb9470e7 | -7.9604 | -63.6171 | 2024-10-14 01:25:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 746d3504-66ab-3a43-b792-817dd8e7cf6a | -8.6044 | -64.2148 | 2024-10-14 01:25:56 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e2896ced-276b-38db-8f3b-c1f8cffe9c3d | -9.2701 | -45.2342 | 2024-10-14 01:25:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b6900b81-06df-33c8-8e63-7f700ac5e459 | -9.1043 | -61.162 | 2024-10-14 01:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 1896a61c-0bd0-30ad-b3e1-6e19a9cda01b | -10.0622 | -44.2391 | 2024-10-14 01:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 92ffebd3-e9f8-34b8-aed1-cc5bfba0143c | -10.0626 | -44.2158 | 2024-10-14 01:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 34b8bbc5-82f2-3870-884f-19cba10267f3 | -10.0813 | -44.2366 | 2024-10-14 01:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 174.8 |
| f295e94b-2698-3b45-9bed-0f4e1e660da3 | -10.0816 | -44.2133 | 2024-10-14 01:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 42839eb0-39aa-3117-ac56-db32920c97a4 | -10.0163 | -47.3308 | 2024-10-14 01:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 178.8 |
| ca034449-7651-3215-abd6-546d5500927d | -10.0166 | -47.3085 | 2024-10-14 01:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 4f5f3380-ba5e-338e-b1f7-6b89d99d51fd | -10.0352 | -47.3286 | 2024-10-14 01:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| cd354517-93a2-3413-9651-079036cef7dd | -9.9973 | -47.3329 | 2024-10-14 01:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 40faf2d7-abfb-3523-8547-47e47fa30063 | -10.4918 | -42.433 | 2024-10-14 01:26:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 6cfffb72-cf9d-3f25-bf6f-84712932809f | -10.5307 | -49.7843 | 2024-10-14 01:26:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 995f65fe-dc59-3941-8544-74179ce2f144 | -11.17 | -39.9192 | 2024-10-14 01:26:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 127.7 |
| 1d5a1e3b-adcf-3010-8933-444d8be7a6e8 | -11.1705 | -39.894 | 2024-10-14 01:26:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 193.6 |
| b6c6c7fe-0c1f-383c-bde6-650e51aeb8d8 | -11.1893 | -39.9159 | 2024-10-14 01:26:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 1c382848-2810-3c36-89eb-507a5636d5bc | -11.1898 | -39.8906 | 2024-10-14 01:26:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 129.5 |
| 50efc10e-df62-3c16-8341-be33067ebce3 | -12.3807 | -53.1167 | 2024-10-14 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 2f03c63e-0cd6-389e-830d-ab9ddf1ce592 | -12.3994 | -53.1355 | 2024-10-14 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| aeda2aea-d4c5-394b-87cc-962a2a547ed6 | -12.3997 | -53.1147 | 2024-10-14 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| ff4d8344-7f9e-3ab1-b200-8e941c18a41d | -12.4981 | -63.0148 | 2024-10-14 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 6a45bec3-92da-3361-a5d2-5bd90e106c88 | -12.4983 | -62.9956 | 2024-10-14 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c46a8c94-7120-34f8-a5dc-86c6c6afba50 | -12.517 | -63.0137 | 2024-10-14 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 12c75941-dd24-3dcb-9517-d5c840b64178 | -13.1475 | -62.3215 | 2024-10-14 01:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7348259b-caf8-3000-b606-ac6106625532 | -17.0823 | -56.0076 | 2024-10-14 01:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| cc6ad5ad-ecb7-3d40-b4c8-71f8779659da | -17.6471 | -56.3084 | 2024-10-14 01:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 95204924-2456-39e7-8367-c7ece602a143 | -17.6474 | -56.2876 | 2024-10-14 01:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.3 |
| cceaca81-e9dd-3f0f-b60f-ea44a36f6b6c | -17.6876 | -56.2409 | 2024-10-14 01:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| c44f9107-da25-37fa-a982-7534f0c40b25 | -17.7264 | -56.2774 | 2024-10-14 01:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 9147c202-f1ab-37f7-a8f3-11938cb56e1e | -18.236 | -56.5014 | 2024-10-14 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |


[Clique aqui para ver as próximas entradas](README24.md)
