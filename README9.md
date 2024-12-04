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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a50b3fa3-a31f-3933-ad9a-08c0e15def4a | -3.6757 | -47.1395 | 2024-12-04 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 8ca777c3-d22f-3340-a110-06b2882777ba | -9.19148 | -43.16281 | 2024-12-04 00:52:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| fd5fc209-99a5-3868-ba0b-7427e4c4fcef | -9.19084 | -43.15725 | 2024-12-04 00:52:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a07f42a8-7b04-3458-9c1d-4886e45931f5 | -12.48299 | -46.3468 | 2024-12-04 00:52:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 286fb8f2-f377-326e-94be-79bbc454f7ba | -11.07863 | -44.30061 | 2024-12-04 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0fcbefdb-3ce7-3da8-ad9c-3c041addd529 | -12.78228 | -45.54873 | 2024-12-04 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 619b47d0-8dfd-3640-b6d9-7228663dcd46 | -11.08036 | -44.31221 | 2024-12-04 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 57a2c866-08fe-3ef8-aaa1-9248df29baa4 | -10.98042 | -44.46272 | 2024-12-04 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8840df1a-fafc-361b-b0b8-4fbbee8c1ff0 | -4.5842 | -50.45709 | 2024-12-04 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3365ab33-0b7b-39ca-92b3-d8f2b43602f6 | -2.88894 | -51.79263 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 97128c91-482d-34fb-ac1c-0e1a4dc6ca74 | -3.24974 | -50.65783 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 49deb28a-520a-392f-8f3c-45672094e2bb | -3.0128 | -53.22821 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 252ebe6e-d666-3591-902d-301db644d46d | -5.57541 | -45.14397 | 2024-12-04 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3af3d875-3177-3811-b800-09f06b49bb5b | -4.92322 | -47.85944 | 2024-12-04 00:54:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d435f39e-30eb-3759-896f-a14c22005ec2 | -3.12135 | -54.61282 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 937.4 |
| 3391b454-aa72-3b0a-a5cd-30d256a173c8 | -3.24366 | -50.41638 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ad4c82c3-b2d8-31c7-bd89-924b3007d49b | -4.05247 | -46.98674 | 2024-12-04 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 78a196dd-5e4b-3030-9f3d-530e82eba7cf | -3.06163 | -52.75866 | 2024-12-04 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 181510ce-c8ea-388d-8f98-4afa5544a5c5 | -3.13549 | -54.62776 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| defbef7f-67b1-395d-a02d-9dcaee1ff70c | -3.79073 | -45.67532 | 2024-12-04 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aaa4847f-4bbd-3441-8df1-13742f2cb106 | -3.21453 | -53.1227 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 37787bc2-6843-37c4-9b33-d4d85bfc87ae | -2.93377 | -51.44627 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46437a44-c843-3ae7-9e50-b4f4db3ed962 | -3.74605 | -49.92007 | 2024-12-04 00:54:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0c8e23d-35d5-30fa-b50d-3d44ec6e39b7 | -3.34201 | -51.20696 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3c69069a-4200-3569-81f7-2bc6d123f399 | -4.07841 | -46.697 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3d9f584b-b283-3f45-8a5d-8b1a6e9634bd | -2.8048 | -45.49061 | 2024-12-04 00:54:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| cd3a8d35-6595-3e9b-8167-fd3d84aab160 | -4.33153 | -48.10652 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d5472312-3b69-3102-b0de-7332ae4837cc | -3.03553 | -49.50887 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7d6652d6-3bbd-34f3-8ffb-c15a2211b2a0 | -2.04582 | -51.20104 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 04842fc8-513c-368f-93c4-29839ab4fad6 | -4.09707 | -46.31533 | 2024-12-04 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cb3ae489-3904-3d92-a1e6-a033e3cbac5d | -3.2774 | -50.32751 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 29db98eb-334e-3476-9376-227c304ea140 | -2.68524 | -46.60633 | 2024-12-04 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 052e826d-8b5d-3140-afdd-bb4de6c6cd0d | -3.74074 | -47.57182 | 2024-12-04 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3fa14b3b-bf47-3eba-a679-88fe23070a1c | -2.93639 | -46.77731 | 2024-12-04 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5bbefb5-79a8-370e-b7d0-d161df9c61e1 | -3.33665 | -51.21349 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 82e9c6af-634b-3986-85df-26638f2b0eea | -3.18678 | -54.33494 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b4ea7b44-ca7f-31ec-bdbc-b0ddc45f545c | -3.57806 | -50.30424 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 01de7fec-06c6-3bdf-9ed5-2b2d8e4f6c28 | -3.73785 | -50.19508 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f935c880-a528-3233-943c-0829d32bc720 | -3.79364 | -46.70414 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 77915351-9433-366b-bf64-e8e9b04e7561 | -3.1085 | -49.50174 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 71efe710-204c-340a-95cc-7d91317da5a4 | -1.48648 | -52.52883 | 2024-12-04 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 99f8dc17-63e1-3f4f-9a6a-4ddd96337017 | -2.05231 | -51.19417 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b89a468a-be5e-3160-b8c7-ad2643cc6703 | -6.75523 | -46.29738 | 2024-12-04 00:54:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f2ec9fc9-e429-323a-a561-1f9240bdf597 | -3.54157 | -51.5009 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5eed09f-3b66-3057-8db7-a946e0b48dc1 | -3.55262 | -52.90976 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a7632a3a-4e2c-3e72-8156-2bbb2854031e | -4.11568 | -48.53845 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f3c45937-1de3-32ba-b098-183ce7181d92 | -6.09297 | -48.05827 | 2024-12-04 00:54:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 22e2d7a3-174e-3f7b-9903-7ae0d4b3301e | -3.47707 | -50.24074 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| ac295f41-d1ea-3f1d-9427-af0cbcfbdea1 | -3.33292 | -50.0634 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 90ced957-763f-3eb6-b5b0-425e88dbbd9d | -4.04476 | -46.86652 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 18bd387f-50f4-30a0-a693-2099df8492c3 | -2.07436 | -45.48405 | 2024-12-04 00:54:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 0b13c547-ea20-358f-b34b-627ec4f4ce67 | -4.07933 | -49.33995 | 2024-12-04 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7268f76a-dec9-314d-a1ff-5d060ed53c9e | -3.81933 | -51.65617 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d7c00acd-06e4-30f2-a6d5-cb6801da0a26 | -3.19296 | -45.28711 | 2024-12-04 00:54:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 16329c2c-420f-39cc-8858-af1d73c233d5 | -2.81251 | -45.49595 | 2024-12-04 00:54:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d52bb13b-ac96-38c2-b4ff-8a87c7f445e4 | -2.61035 | -45.41521 | 2024-12-04 00:54:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 791bade1-c8ac-332d-baf7-4a414693fcb1 | -3.33418 | -50.07243 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3b0de474-57f4-3037-a9c2-6b7d092ac096 | -3.57934 | -50.31344 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 5d1e91f6-29c7-39c4-aea1-682003c69d32 | -3.68235 | -50.25874 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| a222530c-59ac-3c50-8b6f-611c59ff6b3d | -3.97237 | -46.66613 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab373d03-9a89-3875-8282-6f499153b147 | -3.30598 | -53.35725 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| aea869a7-e4af-353f-b822-e0696f346e7a | -3.20162 | -50.64555 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 8ef1c9aa-9cf9-31da-aa2b-076246a180c6 | -3.44982 | -54.08496 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ee3d0558-be75-3a94-872d-22426eecfea5 | -3.18266 | -49.2421 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2b22d3d-c1b4-3149-88b3-3a66f38ad86a | -2.97733 | -46.92881 | 2024-12-04 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| aa4641a4-8077-3909-bbc5-52c61815f580 | -4.19721 | -45.37797 | 2024-12-04 00:54:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 86865851-d449-34b7-b08e-c265ac1ff894 | -3.26996 | -50.2078 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b87f0fd2-45ed-39f8-9f42-150f5639972c | -2.9471 | -51.40359 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 2bbb8130-5a8d-362a-9800-8b3e19927492 | -1.25289 | -46.59274 | 2024-12-04 00:54:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 79539478-2aa7-3eb3-a44e-df26de192c47 | -3.09758 | -49.50012 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b975062-cf4c-3c58-b05c-60feab5adf34 | -3.15061 | -50.34178 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7b23e73e-6b44-35e1-aaca-db57308b57e3 | -3.8097 | -51.6575 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ec7e7e7e-309b-3cee-9efd-a7a3c04f5c6f | -4.19075 | -50.68151 | 2024-12-04 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6bea0e61-e8e1-331d-90b5-23ca4492f2b4 | -2.81616 | -45.5208 | 2024-12-04 00:54:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3f3b5588-89c5-342b-8012-dc9501c4bd51 | -3.1948 | -45.29986 | 2024-12-04 00:54:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c1841758-8aca-3ab8-aa2d-b372de87befc | -2.8836 | -51.82536 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 44de54e8-f0e1-3247-81b7-c05c0b495f61 | -2.61446 | -49.26004 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 43abe021-62db-3e10-a8dd-7ad256788938 | -3.13319 | -54.61105 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 214.8 |
| e57cab08-2b8b-3eb0-8ab8-91b70fab8e82 | -2.96823 | -49.36277 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 13a18fc9-17c4-3f2f-a891-ef3ad3359c86 | -3.74219 | -52.4354 | 2024-12-04 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bb23250e-85c0-3258-811a-f4f8a5dc0702 | -1.74528 | -52.62299 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| c313c69c-f14c-3d7e-9f24-7ffb6d42bd6c | -3.12363 | -54.62947 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 382.9 |
| 1198c36e-1f0c-3807-b2fb-7037db8540b1 | -1.66161 | -52.75652 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 158bbf26-937e-3e30-8ed7-137d028fdd37 | -2.28623 | -47.9059 | 2024-12-04 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 24488845-5fa1-3e77-b3a1-28f7cdf28cb8 | -3.0808 | -53.37327 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a9fa74d9-a39d-302f-be9d-2d543bb02654 | -4.12216 | -43.93118 | 2024-12-04 00:54:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| baf4e1bc-0dd0-37bb-ac70-af872a1652c2 | -4.59253 | -45.49163 | 2024-12-04 00:54:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fb83be57-136a-3d2d-b4d0-4ef0f27e49ae | -3.28542 | -53.71578 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 45fdb6df-19d5-3507-9493-d2eec6e9657a | -3.75228 | -45.61482 | 2024-12-04 00:54:00 | TERRA_M-M | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9a6e9386-f9b4-3449-8596-c0353941f667 | -2.75317 | -45.27729 | 2024-12-04 00:54:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 167.3 |
| c4060da2-ad6f-38fc-8242-c5cd14b3e4b0 | -2.47202 | -46.53976 | 2024-12-04 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5536add3-7e54-3047-898c-e32bc88fc8eb | -2.82561 | -53.04588 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a689bc9f-7bc7-3ae6-80fb-3ed7893f12ba | -3.3791 | -51.0619 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2677a28e-7204-3aee-8566-2ae76632204f | -3.75229 | -52.43391 | 2024-12-04 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2bb66043-a048-3163-acfe-a7ba55f27c6b | -3.55505 | -50.20497 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1972beac-e739-3b3e-9de5-edf001509fb8 | -4.44046 | -48.69069 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9ee0d592-b0d4-33d0-83b5-efc9848f5cda | -4.59082 | -45.47987 | 2024-12-04 00:54:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| bfeb1cac-4488-39cb-83f6-4ca0c895de1d | -5.97144 | -46.30681 | 2024-12-04 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7a800f96-a84e-3ae5-8f13-ebc2fcc58522 | -3.00137 | -53.81773 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 71f28791-289c-3c31-b582-8cda923dc8db | -4.19437 | -48.84315 | 2024-12-04 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |


[Clique aqui para ver as próximas entradas](README10.md)
