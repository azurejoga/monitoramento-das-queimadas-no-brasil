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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b216357-46bc-335e-b71f-4c2ef0b5adf7 | -12.25206 | -47.93338 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e76f2338-98eb-3eaf-ad45-2558894548f4 | -13.02996 | -48.81175 | 2025-10-30 00:33:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 81025380-6c6a-3c05-ad27-56e3a22e4b22 | -14.97894 | -43.38544 | 2025-10-30 00:33:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 33.7 |
| e9395bbf-881f-3e58-9638-496c94f7fe5d | -12.73946 | -43.43279 | 2025-10-30 00:33:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d0f8106f-3488-3bfb-8a8e-f1064617c51a | -12.197 | -46.7172 | 2025-10-30 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9a51d2ef-72b7-398f-a44a-05f92bb50c6d | -11.06172 | -47.53142 | 2025-10-30 00:33:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 432217bc-b447-3d12-850c-0713f29f333d | -11.07212 | -47.53949 | 2025-10-30 00:33:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2f3cd1c9-4c28-3259-a941-bd51d9cc930b | -13.15098 | -44.00504 | 2025-10-30 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 497daef7-7db2-3b08-b94e-1667b391a239 | -13.5759 | -49.58656 | 2025-10-30 00:33:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ec83b3e9-be02-3c6a-8abd-f8142bcf3823 | -10.35279 | -44.07667 | 2025-10-30 00:33:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1b5a656d-0dfe-3887-9e0f-b97232036b6f | -13.34908 | -47.66979 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ed683fd5-9349-3ca6-bd2a-d7097b772a2c | -12.36404 | -50.15232 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8bc44169-8c4d-31f9-a1de-636ad7daf3e7 | -13.1804 | -48.43679 | 2025-10-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ab9511dc-865e-32b8-9daa-b69b7ed43160 | -15.15881 | -47.24277 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8fabb4cd-a894-3c1d-a396-ffa98bb13f81 | -11.06306 | -47.54084 | 2025-10-30 00:33:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fc72d40a-75c5-3b56-a842-1b4dff6c84b9 | -12.74197 | -43.44859 | 2025-10-30 00:33:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 8ef370d6-38f5-3105-8d42-523295a548fa | -13.02827 | -47.03945 | 2025-10-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8282689a-063a-3cce-9476-63126b6e5800 | -10.27853 | -44.57096 | 2025-10-30 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d89f0c33-ef2d-3df7-ac3c-38908b02ecf3 | -14.22998 | -44.31908 | 2025-10-30 00:33:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 23586ec4-7a9d-32f0-a0e4-d495a77138ce | -13.27639 | -47.74337 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 23044f43-3d87-350e-bd60-83f8d6d5d716 | -13.52727 | -44.33878 | 2025-10-30 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 596bd208-b60e-34d1-9d96-a19626779e2d | -13.22439 | -48.55915 | 2025-10-30 00:33:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2c621216-8927-3497-b8b7-50ef717fefa0 | -12.8746 | -54.74253 | 2025-10-30 00:33:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| ba3d2bc5-6529-3693-9d54-677fb4755338 | -13.07599 | -48.21847 | 2025-10-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3eb6f0b3-f8f3-3993-876a-06922b93b2d6 | -10.49008 | -45.04181 | 2025-10-30 00:33:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| ec5977e4-3e7e-3830-b2f8-534cc3c7e4a3 | -12.33025 | -50.17649 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 13dd2834-ba53-3c5a-aa97-5689cc726c81 | -10.86254 | -47.62177 | 2025-10-30 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 19d62e56-4eb9-3d59-b419-c79718610c74 | -12.22843 | -46.47504 | 2025-10-30 00:33:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b209b198-f444-358f-bbd2-6984d7a3252d | -11.96843 | -43.29625 | 2025-10-30 00:33:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 30bb3a28-c75f-38ca-a3f9-21074cd6e4df | -12.14367 | -48.01116 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ce84082e-d6df-37da-834a-86babb5ca01c | -10.28065 | -44.585 | 2025-10-30 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7325da78-21cb-32ac-bb42-2d9a5e4c5602 | -12.32067 | -50.31459 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f887864c-b894-3d8f-85b1-2a5e6c72d97a | -11.84713 | -47.93394 | 2025-10-30 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 5bd2732c-6eaa-3a32-a921-b0622dbda795 | -14.77593 | -44.98837 | 2025-10-30 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| cfea2de0-7692-3c76-a0d0-1bac35a05677 | -14.30103 | -48.01448 | 2025-10-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 024bca92-a9ad-3429-848f-964db7e1586b | -13.35326 | -43.08789 | 2025-10-30 00:33:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 22.6 |
| ab14c65c-2a18-3f54-b41e-c0ec6a2ce5ca | -13.22279 | -47.04591 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64d401aa-2b7d-3363-9347-cc888acbba03 | -9.81354 | -47.57417 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e3f7b0e3-4f8a-3cc4-965d-e695795b5aae | -6.64681 | -47.29061 | 2025-10-30 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| db522e64-f171-3aa7-a68d-61b16753c7f3 | -3.67305 | -47.61989 | 2025-10-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37eb9060-a2e9-38fe-8f9f-2dcf04c1792c | -5.04 | -43.61077 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 7789fedc-e431-3630-a1f0-56d5c01b1eeb | -6.52885 | -43.56538 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| bfdbf435-1c34-33c1-995c-c32b1f1d6312 | -2.94756 | -51.52153 | 2025-10-30 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 83bbadff-cefe-3eae-8157-aa99296f883f | -9.8945 | -49.12439 | 2025-10-30 00:35:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 50b4dd46-57d3-3daf-aa27-d7386c9b4556 | -6.02446 | -44.33295 | 2025-10-30 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 72b56d03-32ba-3d75-8bed-c863926bae45 | -3.39003 | -45.90545 | 2025-10-30 00:35:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9044821a-6cd2-3bcd-87c8-5a54896998b0 | -2.76139 | -45.3856 | 2025-10-30 00:35:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 799e5b12-95a1-33a0-857f-eed981506052 | -9.18817 | -48.28974 | 2025-10-30 00:35:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f65d16a7-a7c3-3df8-984c-408504587bfc | -3.01225 | -51.38779 | 2025-10-30 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2b071633-c4f6-3795-abcb-b59f4b8b9795 | -3.97261 | -51.06878 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc7629d9-ce92-32c1-bb6b-1c99e7fbe60e | -7.80295 | -46.44888 | 2025-10-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| df510d83-dabe-306c-b269-570bb8efaf38 | -3.73341 | -52.14914 | 2025-10-30 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bf9c6a48-8651-34b0-a7d3-f40de7587327 | -4.46161 | -45.76316 | 2025-10-30 00:35:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1b6cdd40-57a4-317a-a16b-af55542c0425 | -5.41994 | -44.84548 | 2025-10-30 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 94ec376f-cd2a-3744-bb95-95b53a86c146 | -9.2984 | -48.41704 | 2025-10-30 00:35:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c3aeb66b-1a59-397e-af5f-1b05a3a75377 | -3.82701 | -51.21909 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6b16338b-37b4-3432-b4b8-528743213b7b | -7.29964 | -45.66556 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 4445eb15-db2c-3068-8a06-da0aabdc8913 | -6.13786 | -41.70208 | 2025-10-30 00:35:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| e843f5f6-a28e-3db5-b206-fb0f9ff1f778 | -4.46588 | -43.4538 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 3edb7dd2-f6f4-35bb-a029-98d23b5d2ae1 | -10.00873 | -48.22696 | 2025-10-30 00:35:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af9d3806-0742-396c-880c-b1240e317af7 | -5.43434 | -45.33538 | 2025-10-30 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| cd2dbcfd-8bd1-345a-bb4d-99ec68628af3 | -6.15915 | -45.72065 | 2025-10-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| af172b9e-4ca7-31c1-b2e7-b82e4b185fe2 | -7.96506 | -46.71646 | 2025-10-30 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3ce9c44c-7774-31a2-bd2f-282c56518f46 | -3.79623 | -43.88496 | 2025-10-30 00:35:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 7fdf25bb-c2b7-35e9-b14d-51adf1b4ad88 | -9.04745 | -47.82153 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 52fa4817-1b98-3dcc-ae82-26b3a3f405c6 | -3.36194 | -52.80569 | 2025-10-30 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5b1e9e30-2db4-3a5a-b47f-85ba1ffcaf77 | -9.29076 | -48.42746 | 2025-10-30 00:35:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 31cd8ff2-2b1f-3934-a07a-5a7e43a89868 | -6.25609 | -44.11834 | 2025-10-30 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| aa7b0177-b3a3-30e5-957b-ebf434b980c8 | -2.79568 | -50.29271 | 2025-10-30 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| e69b946f-0747-3fe4-a2fd-adf287626617 | -7.70799 | -46.98314 | 2025-10-30 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ede4c76-906c-35d5-9f1d-a9f659056690 | -4.36451 | -48.72468 | 2025-10-30 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 06d7b7fa-f437-3d4e-adfc-ab9f045dcbab | -4.74568 | -46.46236 | 2025-10-30 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5f2bc039-281e-3dac-b7c0-cfa236690621 | -7.38028 | -46.21864 | 2025-10-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| add2f97f-b2cd-31bc-9def-b7fdab621aed | -4.47922 | -43.45173 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ff836310-d292-3fed-b092-f1f58d9b3e31 | -6.01516 | -41.98251 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| c489323f-7c16-375b-860b-0058f1580870 | -4.33781 | -47.89389 | 2025-10-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 16ed3279-9cb7-3264-9039-fac5eeafa9a2 | -4.30036 | -48.07377 | 2025-10-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 848998d4-1594-3767-9387-f4197d2ded7e | -9.88598 | -47.43902 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b2cbd12a-e405-3264-a67d-23791609b37a | -2.903 | -49.80288 | 2025-10-30 00:35:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d97f9b37-6cc5-3784-ae99-f9d614f84566 | -6.91365 | -42.25597 | 2025-10-30 00:35:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 023423b4-c489-30c4-bf5a-9ffe76de5019 | -4.84279 | -45.85595 | 2025-10-30 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7e862a54-ddb0-37b2-8749-fdb4becdbe8d | -4.23554 | -55.66822 | 2025-10-30 00:35:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5e3dafff-2873-376e-a7f9-b05291f09f0b | -9.49683 | -46.97248 | 2025-10-30 00:35:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 9ee357d1-cd90-3055-9c7c-c13f95858f67 | -3.38146 | -48.94157 | 2025-10-30 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 725ac9cf-ebd2-3fa3-af72-4d17b4f26585 | -7.51046 | -46.75848 | 2025-10-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ceb2776f-f04a-31c2-8039-807776b024d0 | -9.94237 | -47.19359 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f3bd9846-6dbb-3b81-8d9b-3436890b60de | -3.39006 | -45.89967 | 2025-10-30 00:35:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 92ffcb7e-d675-361c-b45d-7c0d13ff0630 | -6.8499 | -46.29976 | 2025-10-30 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f861a554-e02c-3929-ad65-82019685b711 | -2.77556 | -45.40022 | 2025-10-30 00:35:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 935b7a57-dc10-3c1e-944f-3b7bd776ee9b | -5.41889 | -46.02287 | 2025-10-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8e5fa5ec-e404-3c48-a880-a19673492b33 | -7.86679 | -44.2315 | 2025-10-30 00:35:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 0cdb8b29-3770-3dc4-aae5-1cdaf7069386 | -5.45055 | -50.9007 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3136ef66-a323-3913-b0f3-7b2a37149541 | -3.22161 | -46.89158 | 2025-10-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d5fc65c0-fe4b-3790-b019-9f6a208f6a4f | -4.03006 | -47.76995 | 2025-10-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4c05430f-9b62-3943-ae37-6490c072c269 | -3.44467 | -54.64005 | 2025-10-30 00:35:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 94841f51-1c91-3481-aeca-460e82141d6a | -7.62273 | -43.59754 | 2025-10-30 00:35:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 86ab6f35-3266-3fc4-b0c9-16cc336f378e | -3.01102 | -51.37888 | 2025-10-30 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9a1629c3-81a2-3471-aeb3-ce58ed65e23f | -4.48938 | -43.42804 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 6c986d68-4000-3d1c-ba2d-f474cfbdef9c | -3.79927 | -43.90554 | 2025-10-30 00:35:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e096cd42-39da-33f6-a7b7-999fa7fa803f | -7.62559 | -43.61628 | 2025-10-30 00:35:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |


[Clique aqui para ver as próximas entradas](README5.md)
