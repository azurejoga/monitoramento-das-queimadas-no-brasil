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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd599ebf-911e-30c3-9e42-2cb8b848dff5 | -11.0126 | -46.6971 | 2025-10-04 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 221cb3cb-b0f1-309f-a0e4-71a2da422fc2 | -15.5408 | -46.8344 | 2025-10-04 12:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 88.2 |
| b920cf45-c01f-3e39-b0d2-606c6fa60a96 | -11.1268 | -47.9077 | 2025-10-04 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 0adf4a51-ab32-3af6-ac9b-c27f5854748d | -14.2126 | -46.0827 | 2025-10-04 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| bd5a009f-bc64-338a-a5e1-66e5e161cbf7 | -12.535 | -45.9864 | 2025-10-04 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 282.2 |
| 974da246-58b4-3d67-a13b-f6eb85d34a68 | -11.9339 | -46.3699 | 2025-10-04 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 08d49fc4-f5e7-3dec-bcc6-fe5302183f23 | -14.2131 | -46.0596 | 2025-10-04 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 99f9097f-6483-3b1c-8160-296f7d9a7212 | -11.9147 | -46.3726 | 2025-10-04 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| aee749ab-3a57-3c60-9e03-115fc60c7b15 | -11.1271 | -47.8856 | 2025-10-04 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0345227b-5ff8-342e-a995-102433bca553 | -14.3171 | -52.9131 | 2025-10-04 12:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f941bc2f-ba5d-3db2-8d06-fa4cc7efd477 | -11.9143 | -46.3953 | 2025-10-04 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e940213f-e2b5-3649-a658-86f7707dce45 | -13.1962 | -50.9739 | 2025-10-04 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 4f86a5fc-0fc0-3434-a187-7435dbbeafa7 | -11.1462 | -47.8832 | 2025-10-04 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 8d8de3b2-956d-3747-98c1-9c311830c184 | -13.114 | -47.9518 | 2025-10-04 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b5a0896d-0385-37dc-bebd-f1804583ed74 | -8.2314 | -46.8289 | 2025-10-04 12:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 41d5ac12-6055-3ba7-9ad0-3fb73bdd62a8 | -14.672 | -48.2933 | 2025-10-04 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| fc9f3250-65b3-31c1-b60f-cfb51a75f47c | -12.7194 | -48.5611 | 2025-10-04 12:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| bc7e6bd7-cc92-3a5f-b101-374d15140bf2 | -10.5648 | -48.6981 | 2025-10-04 12:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| f8a62e98-a8f4-300a-bffb-d1cefe800b1c | -12.031 | -45.2132 | 2025-10-04 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 80a84549-135b-3262-bdf0-1b76d2658811 | -10.5835 | -48.7178 | 2025-10-04 12:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ac01e5e5-e255-3c67-aa5e-9a29dd236859 | -8.2128 | -46.8084 | 2025-10-04 12:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 9855e85a-e5d2-3f9a-9993-6e852b077c4b | -10.195 | -45.4882 | 2025-10-04 12:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 4c547138-cec0-30f5-babe-57f78d413acf | -8.2316 | -46.8066 | 2025-10-04 12:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 341c3459-217f-340e-8db8-2321f07caac9 | -11.5069 | -46.7671 | 2025-10-04 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| b133bb88-9715-3bcf-9144-f220154a1c9c | -12.7194 | -48.5611 | 2025-10-04 12:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 49081c34-8247-3ef2-aec4-063b15c0fa20 | -11.1268 | -47.9077 | 2025-10-04 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6818f459-27ad-3610-83f2-fcad0dbfd91c | -8.8534 | -46.7451 | 2025-10-04 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 49682511-0c07-3698-8938-df5fd2b91f31 | -11.5492 | -47.6773 | 2025-10-04 12:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| d7cc9e87-6053-37b7-ad0a-028ac2a8a426 | -11.863 | -44.9612 | 2025-10-04 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 470644e4-7de9-3c2d-a24e-38d557e3fa2f | -11.5069 | -46.7671 | 2025-10-04 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 680c5824-1fc6-31be-ba50-494795475803 | -13.3081 | -47.8565 | 2025-10-04 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| d7c2263d-fb55-331a-959f-619bddee909f | -13.114 | -47.9518 | 2025-10-04 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| bac9c808-e7a4-377a-859c-97cb8e22047a | -10.3346 | -50.3188 | 2025-10-04 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ae0b45ae-b3ef-39b0-b49e-48ee5815063e | -8.2316 | -46.8066 | 2025-10-04 12:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 32edd3c8-20f4-331f-b8a3-9b0bb375aae7 | -7.8593 | -48.2037 | 2025-10-04 12:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 135b6c08-0e92-3bc0-81b6-29eb3d763e1b | -14.2131 | -46.0596 | 2025-10-04 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 220.4 |
| 1e8a1438-f1ce-369a-b593-a28fbb3a04c9 | -11.5683 | -47.6749 | 2025-10-04 12:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 01d65e52-4231-382e-a82a-ae8235ca61b7 | -13.1962 | -50.9739 | 2025-10-04 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 346.4 |
| 73709a55-cbb6-3115-89f2-315793f2b065 | -10.3343 | -50.3402 | 2025-10-04 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 6a0767fe-eaeb-3209-92fe-3453a202807e | -15.5408 | -46.8344 | 2025-10-04 12:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 123.0 |
| db0e7294-f241-3915-9f10-ba2dddb39d47 | -14.3171 | -52.9131 | 2025-10-04 12:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 01f8ed00-0f0f-3b4e-8ba5-d32085d8477e | -11.1462 | -47.8832 | 2025-10-04 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 1813360f-0c38-340f-99aa-94a1a2c2de39 | -14.2321 | -46.0794 | 2025-10-04 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 87659297-0823-348d-86d2-296a9cd34636 | -11.1271 | -47.8856 | 2025-10-04 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 4b8e1721-70eb-3d64-abef-2874b418f765 | -13.3225 | -48.1216 | 2025-10-04 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| fb5510c2-3d02-3004-b992-197499da13f2 | -8.2128 | -46.8084 | 2025-10-04 12:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 0ee3a3ec-de8b-3e7d-9a29-81b6e84ee130 | -12.8761 | -47.2937 | 2025-10-04 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a0ab80bb-a10b-323d-abc2-1f84e1fd7e9e | -13.1774 | -50.9549 | 2025-10-04 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 49210c3c-fced-3bfd-b315-859e0b6cd739 | -12.031 | -45.2132 | 2025-10-04 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 81a3eb14-bf8a-3fd8-a395-d870759e2547 | -12.9471 | -50.9838 | 2025-10-04 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 846a3ddd-1b14-31d4-8231-75c7c9c1c87c | -10.195 | -45.4882 | 2025-10-04 12:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 302c98b9-7815-3979-be58-f305e0b4d36b | -14.2126 | -46.0827 | 2025-10-04 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 136.1 |
| c33732ec-3e88-3d98-90f7-286bc022455b | -15.9574 | -43.3423 | 2025-10-04 12:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 194.2 |
| cf7c19e4-67b2-3f58-9fbf-4a918d8deb60 | -12.0314 | -45.1901 | 2025-10-04 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 5ae1774b-f121-337f-975f-eb0501359815 | -10.5835 | -48.7178 | 2025-10-04 12:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a0e234d1-2148-3c87-92bb-a9d9d123382c | -14.2325 | -46.0563 | 2025-10-04 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| b79225ef-fe5f-3a45-b36c-f8435d9e92bb | -12.535 | -45.9864 | 2025-10-04 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 48c5dbda-cb3b-3e71-85dc-7a2e5f86ece9 | -15.958 | -43.318 | 2025-10-04 12:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 271.4 |
| 8bf60db9-9ce2-39fb-94b8-a189b95d5afc | -11.1458 | -47.9054 | 2025-10-04 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 02b20516-efb2-3d30-beb2-c9d827353681 | -8.2314 | -46.8289 | 2025-10-04 12:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6e2ded7a-b42b-3335-abd1-a8b64b27a4d2 | 0.41129 | -50.98455 | 2025-10-04 12:14:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 5f41447b-c1a7-300b-9b11-8fef9ed0bed8 | -6.80839 | -43.77677 | 2025-10-04 12:17:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8c393797-db91-3bdd-8142-6aeb651d7fb3 | -8.2201 | -46.82905 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 392035c5-3271-3ef2-8169-8b1f09ffee82 | -7.64704 | -45.47459 | 2025-10-04 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c3f6023e-ae9e-3155-acd4-559234e30801 | -6.84969 | -44.83567 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 771046ac-f645-3d97-b36e-19a416e5ac52 | -9.1152 | -44.39235 | 2025-10-04 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4b91dbde-f6a9-3dd0-92f1-a3e41ed55c8b | -6.46406 | -44.57467 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c2627dbf-b925-3144-b919-edf98edd0914 | -7.77149 | -46.22879 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 5858cb87-9a0c-341c-8293-86043df92d7b | -8.62824 | -44.89743 | 2025-10-04 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 2a5aa706-1e33-35a6-a7f8-efad364144a4 | -8.13674 | -44.07695 | 2025-10-04 12:17:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0efac77f-e5e1-3f1a-8395-4934ba8a0441 | -5.8605 | -44.13641 | 2025-10-04 12:17:00 | TERRA_M-T | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| dd040bba-efa8-3277-a1c1-9ea62b17ce1c | -8.86724 | -46.75265 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 6d49c16e-b23c-33d9-ac85-373eadde7f6d | -7.01271 | -42.30212 | 2025-10-04 12:17:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| b3606440-fac1-3f6a-8963-d007c4cb25da | -3.44514 | -43.33328 | 2025-10-04 12:17:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 7aedfcae-904c-359c-aeca-1589df913ca6 | -9.1052 | -44.39112 | 2025-10-04 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e744199c-f65c-3f69-befd-56381019c3d6 | -4.77034 | -42.09051 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 46.4 |
| e9177c54-8972-327c-8087-27e2daaa4939 | -7.53873 | -42.40093 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 44.8 |
| 444491a4-b992-3af0-a8da-2b6df6c62268 | -7.43534 | -46.96873 | 2025-10-04 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c4d99255-e830-3bb7-8fe3-5f1046bcb21d | -6.16086 | -44.63005 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1bcb3459-22e1-3847-8b3b-e01df93e67cf | -4.97141 | -42.79745 | 2025-10-04 12:17:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 573f2967-a9fe-32a5-bf15-7ccf85abc436 | -8.8519 | -46.79663 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 3dcaa396-2d7d-3d04-b084-49df3d959ad5 | -8.58756 | -46.25721 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 276.4 |
| aec807fa-1528-331a-b20c-9b213df193f7 | -8.85062 | -46.80565 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 058fb3ee-63a5-36e2-8b53-e1297a4972e0 | -7.77147 | -46.29402 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 11b8a245-729e-3b60-954f-8ce01ae784af | -6.71712 | -42.79712 | 2025-10-04 12:17:00 | TERRA_M-T | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 8110f186-5cd0-3fb0-aae0-7626601d2516 | -8.54716 | -47.26067 | 2025-10-04 12:17:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 76abc7cd-057a-3410-83c1-03731cb47fa6 | -7.43026 | -47.00417 | 2025-10-04 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 01e555f3-a049-3e47-93a3-c0f246ae99fc | -4.77227 | -42.07619 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 096a547d-0d8e-3373-93a1-b951b87f3d5e | -8.17111 | -43.35247 | 2025-10-04 12:17:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 1c850740-ed99-31b7-b1e7-a6d48dd2b1ee | -6.80811 | -43.78212 | 2025-10-04 12:17:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| af9988f8-02b3-3d6f-a241-5f81c6190a8d | -8.58628 | -46.2664 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 290.1 |
| 8e2739d0-7948-3db9-a0c5-ba09af42237b | -7.76252 | -46.22755 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f91730d1-b345-3a1c-92b4-f639be430767 | -7.11614 | -46.95073 | 2025-10-04 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8f2070b2-57b5-3fe8-a57f-8ea2993eb577 | -8.46891 | -47.41513 | 2025-10-04 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e2e4098f-f642-34ee-8b2b-6af7acc3d96b | -5.99546 | -44.35171 | 2025-10-04 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 395f3d70-1b48-3005-9ce1-b0b929c13832 | -8.11978 | -47.27757 | 2025-10-04 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 32164a3f-35f1-3d93-99e9-22709de369a6 | -7.74971 | -46.31902 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 24376f46-81a7-355d-b780-27ed5c7b8f91 | -8.23221 | -46.81901 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 5919fec7-f920-36f9-9136-861185a19ed6 | -5.9969 | -44.34114 | 2025-10-04 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 81edf750-8f7b-37ac-9fef-af6b2eb3cb80 | -7.04219 | -42.78062 | 2025-10-04 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |


[Clique aqui para ver as próximas entradas](README137.md)
