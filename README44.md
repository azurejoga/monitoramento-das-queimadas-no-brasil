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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7900b8d-57c7-3c2d-b2a3-6b687867be68 | -16.6127 | -57.217 | 2024-10-02 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 8338a279-a4c8-359f-802f-3d6e9454de54 | -16.6124 | -57.2375 | 2024-10-02 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| ed3012f8-c7e0-3a29-9548-e2f9bb78a1ec | -16.4536 | -57.4188 | 2024-10-02 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 4426ad56-e703-3a1b-b722-71ac8f46db7a | -16.7063 | -57.4718 | 2024-10-02 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 07758b18-ac05-3066-a7b7-b4e890ae6783 | -16.6916 | -57.167 | 2024-10-02 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| f2a98eb5-9b6e-348f-af43-5bef20b6689f | -16.6912 | -57.1875 | 2024-10-02 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.9 |
| 2fcc869d-7c86-39cd-aa8b-356e10ca61ad | -16.6887 | -57.3513 | 2024-10-02 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 196e0727-349c-3259-9266-410c144eb3d2 | -16.6884 | -57.3718 | 2024-10-02 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 73ee9368-168f-378a-ac26-8f033da4fc57 | -16.6717 | -57.1897 | 2024-10-02 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| fbf6b2f3-8544-3b1a-a6c1-0b1290e21ec9 | -16.6518 | -57.2125 | 2024-10-02 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 92949c77-3fe4-39a4-be63-8962b4bf2149 | -16.6322 | -57.2147 | 2024-10-02 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| e5a19e48-f0e7-3d41-9b35-fc8966a2a7a2 | -16.6319 | -57.2352 | 2024-10-02 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| ef1b4f07-1bb1-3bea-b1e8-05e29af68446 | -16.7461 | -57.4265 | 2024-10-02 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 32a810fc-2cdb-3a87-b31f-606c3ba88865 | -16.7452 | -57.4878 | 2024-10-02 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 5ca31243-dd0c-34f5-a23f-166d725d62ac | -16.7269 | -57.4083 | 2024-10-02 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.8 |
| 2e9ba859-15a5-303f-9aed-4e8b3038b502 | -16.7265 | -57.4287 | 2024-10-02 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| e79a242b-2206-37a4-a068-a2b410b8d5b8 | -16.7108 | -57.1852 | 2024-10-02 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.6 |
| 17fe8645-e82f-3013-b975-5030450d7bb4 | -16.7082 | -57.3491 | 2024-10-02 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 17a1dfae-8ae5-3013-bc69-96a653900783 | -16.8698 | -55.8272 | 2024-10-02 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 8e15434b-a9b1-3814-8b4f-aa662c194112 | -16.8695 | -55.848 | 2024-10-02 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 5dfcd49e-6483-3659-bdbd-a5f0caf1ea6c | -16.8491 | -55.892 | 2024-10-02 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 48fdd54b-416a-3004-80f2-f55137c5171d | -16.8299 | -55.8737 | 2024-10-02 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| f0b07967-2fdc-3380-a75a-742e6b0fc5a3 | -16.8295 | -55.8945 | 2024-10-02 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 129.6 |
| 76e285c9-2996-3476-9a89-a744bfacb720 | -16.8292 | -55.9152 | 2024-10-02 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 124.4 |
| 5fa133c4-30e3-3a34-b132-6d2ba6b9b35d | -17.1581 | -56.1637 | 2024-10-02 02:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| c94f9c03-470e-346a-a452-5bee68a13a99 | -17.1577 | -56.1844 | 2024-10-02 02:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 350ca40a-4444-3cdc-8548-8ff1e06522eb | -17.0895 | -56.7503 | 2024-10-02 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 4adeabf8-366a-3cff-bb4f-19e9dd52720e | -17.0892 | -56.7709 | 2024-10-02 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 3cbaa7e3-28dc-3ac9-aeb3-26f9eb58b622 | -17.0695 | -56.7733 | 2024-10-02 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| fb794e77-3721-312d-8c8b-e83ee9443a63 | -19.2519 | -46.8641 | 2024-10-02 02:16:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 023fd68b-af29-3a28-bb91-055cf8fa9615 | -20.0424 | -55.9738 | 2024-10-02 02:16:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 5c593308-df7c-349b-a65f-5d720757a33a | -21.3451 | -55.7056 | 2024-10-02 02:17:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 663fa854-8257-359e-9ac0-1a88e06a2ab2 | -21.3456 | -55.6841 | 2024-10-02 02:17:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 152.8 |
| ea85da65-1f4c-3f28-8106-7c26493b33db | -21.3656 | -55.7022 | 2024-10-02 02:17:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 06445120-f0b1-3fbc-84e5-7f00dadf0624 | -21.3661 | -55.6807 | 2024-10-02 02:17:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 136.9 |
| a1c40015-c6bd-399a-8bac-3fa68d04862c | -22.3713 | -49.3011 | 2024-10-02 02:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 254.9 |
| 7da6b588-4a0a-3876-b412-c46ff4024236 | -22.3707 | -49.3244 | 2024-10-02 02:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| 0ce28847-8416-358b-9dfd-0e2dddaed89f | -22.372 | -49.2777 | 2024-10-02 02:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 201.2 |
| f6b425ad-0001-3706-bd41-cf960449fcf4 | -22.3916 | -49.3194 | 2024-10-02 02:17:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| 2052cc3e-0387-34f6-874c-2e1801e0adfd | -22.3922 | -49.2961 | 2024-10-02 02:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 230.5 |
| 7cc1e954-e5a0-34db-9645-4eac81868aa6 | -22.3929 | -49.2727 | 2024-10-02 02:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.4 |
| e5dae8c6-0189-385a-a21b-adfb0baebc29 | -22.9277 | -43.7243 | 2024-10-02 02:17:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| 44cfc24c-321f-314d-86a7-2a4a11b80fe7 | -3.1465 | -49.4229 | 2024-10-02 02:25:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 188f3cb3-fde9-32ee-b8c1-668eb4700e1d | -5.9786 | -45.3847 | 2024-10-02 02:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 4309de28-dac7-3196-8fa1-fc08fded036f | -5.9788 | -45.3621 | 2024-10-02 02:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| d99ff927-a4e6-3e64-b4ff-e6979e412ca6 | -6.1114 | -47.2677 | 2024-10-02 02:25:40 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| eafb8be5-a35e-360f-887a-0a0d271f2754 | -6.1301 | -47.2664 | 2024-10-02 02:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2c118679-ab96-3eb8-8275-0b092cd77776 | -7.1796 | -46.9444 | 2024-10-02 02:25:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| ac09ad6a-abe8-3d13-9830-88f42bc978ce | -8.4643 | -62.7124 | 2024-10-02 02:25:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d8902045-a0ca-3229-b703-5d66466b70d2 | -9.9367 | -64.9179 | 2024-10-02 02:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 2e345ebd-3b44-3d16-819b-c3a303357f87 | -9.9368 | -64.8991 | 2024-10-02 02:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| be096d09-998c-3a3d-8119-7e225a14e261 | -9.9553 | -64.9172 | 2024-10-02 02:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| adbf1a6e-fe18-3f96-9ea3-dd6cea414f19 | -9.9554 | -64.8984 | 2024-10-02 02:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| aec558ee-dac2-3d48-badb-3e78d172cc01 | -11.6554 | -65.018 | 2024-10-02 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 6518c863-a95b-346d-8c55-2dc87c6839d1 | -11.6555 | -64.9991 | 2024-10-02 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8aee10f5-a3c2-332f-8828-bf5742cb2c57 | -11.6556 | -64.9802 | 2024-10-02 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 844875c8-3570-3409-815e-cfc27808b29e | -11.6742 | -65.0172 | 2024-10-02 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 6768b1f7-c7bb-38db-9c13-e7fd18191712 | -11.6743 | -64.9983 | 2024-10-02 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 112.7 |
| f25f53cb-ec2d-3e8d-b407-4c62fc3fc25d | -12.2946 | -47.6446 | 2024-10-02 02:26:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 88e3d613-0c8c-3a2e-98b5-9b832d9f8544 | -12.6484 | -63.1214 | 2024-10-02 02:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 9872d5e5-c4ae-39a7-a3cf-0043c57d5aa6 | -12.6486 | -63.1022 | 2024-10-02 02:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 6753a1b9-1a6a-390e-841b-a9f09c82ed15 | -12.7054 | -63.0798 | 2024-10-02 02:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 71c888ec-4ab9-3ef7-885e-e7303c07835b | -12.8593 | -62.7826 | 2024-10-02 02:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 3a63df73-aed9-3116-816e-b768f9f3ba1a | -13.055 | -51.4186 | 2024-10-02 02:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c26e68ff-7c24-3587-9c99-37bd97745438 | -12.9357 | -62.701 | 2024-10-02 02:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 163e46cf-941f-3c04-b337-4672cb85a0b8 | -13.0742 | -51.4163 | 2024-10-02 02:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| dfb38404-9dea-3a87-be0a-ac243da764ed | -12.9546 | -62.6999 | 2024-10-02 02:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| fe4dd995-d53f-34fb-8b3f-ec8979910671 | -12.9548 | -62.6806 | 2024-10-02 02:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| b4008f05-2d87-3806-8db4-ecb2569b2053 | -13.093 | -51.4352 | 2024-10-02 02:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| aa27301a-80c2-3e7c-bcbd-ec6cd4b8f87a | -13.1118 | -51.4542 | 2024-10-02 02:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b29aebd1-7d9b-3b3a-b30f-f8094e4a2b51 | -13.1122 | -51.4329 | 2024-10-02 02:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 16f9fd55-db1f-3749-88ef-9f0024e61a81 | -13.5965 | -51.1367 | 2024-10-02 02:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| f9fb0157-8698-3fee-b4fe-2a75a5369a92 | -16.6868 | -57.4741 | 2024-10-02 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.8 |
| a7c68c16-3ab1-3ce4-980b-f1fd6b915ee3 | -16.6884 | -57.3718 | 2024-10-02 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 06458e83-624f-32e0-898d-84d609163279 | -16.6887 | -57.3513 | 2024-10-02 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.1 |
| 6779ba3b-d3a3-3c41-8b64-b6fec4074db1 | -16.7063 | -57.4718 | 2024-10-02 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| f26e578b-522f-36db-83fc-053feef124af | -16.7265 | -57.4287 | 2024-10-02 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.5 |
| b7883698-b34d-3cdd-8c4f-e67f4aff7247 | -16.7269 | -57.4083 | 2024-10-02 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| b2b722e5-d655-3b9f-b97c-98614fb1cf7e | -16.7452 | -57.4878 | 2024-10-02 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| a2c272ea-a3f9-37da-a5d0-0de11adc4c8e | -16.7461 | -57.4265 | 2024-10-02 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| efa73e09-25b4-3e9f-800f-713923b867d5 | -16.7862 | -57.3606 | 2024-10-02 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.5 |
| 434e5e60-0fb1-3e83-ab20-ce10180e2017 | -16.8292 | -55.9152 | 2024-10-02 02:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 114.0 |
| a4affd98-14a2-33c0-b711-734f842485a7 | -16.8295 | -55.8945 | 2024-10-02 02:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 119.5 |
| 17f81732-573c-305e-b1c6-3ffc2b81f194 | -16.8491 | -55.892 | 2024-10-02 02:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 5d9d9075-8c27-3e8a-b829-b1f44386566f | -16.8695 | -55.848 | 2024-10-02 02:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 2508ac17-1400-3269-88c8-ef71b17843ee | -17.0895 | -56.7503 | 2024-10-02 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| eb5c2195-2d50-35b6-9272-395b3e592438 | -17.1091 | -56.7479 | 2024-10-02 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 43f13562-e027-3344-9ae5-fa6073f11941 | -17.1577 | -56.1844 | 2024-10-02 02:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 13d284a0-677c-3227-82e0-c4301988ac7f | -17.1581 | -56.1637 | 2024-10-02 02:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 6a9f2ceb-3938-3d52-975a-a56bbaceadca | -17.0892 | -56.7709 | 2024-10-02 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| c2fffd99-966a-30de-b890-4891bde28519 | -20.0424 | -55.9738 | 2024-10-02 02:26:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| dbf7bfde-449e-3989-a64b-e4cb4c26a07a | -21.3451 | -55.7056 | 2024-10-02 02:27:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 19c6f5fa-b347-3acc-a938-9a58c867f500 | -21.3456 | -55.6841 | 2024-10-02 02:27:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 263a179b-2241-3d7e-98f5-035631e0408c | -21.3661 | -55.6807 | 2024-10-02 02:27:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 18579f78-dad2-3264-893c-817d7c332868 | -22.677 | -43.7014 | 2024-10-02 02:27:09 | GOES-16 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 103.5 |
| 4441cf56-8f5b-3494-8c99-fa7c66d615a2 | -22.9006 | -45.1029 | 2024-10-02 02:27:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| 9d07a621-7242-3ae2-a47c-35158aa69eab | -3.128 | -49.4235 | 2024-10-02 02:35:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| fedd98ec-98f8-3f61-985e-d71ed45f505a | -3.1465 | -49.4229 | 2024-10-02 02:35:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| aded0ca8-da67-3519-8fff-108a4d772165 | -5.9786 | -45.3847 | 2024-10-02 02:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 87acdee8-3f95-3321-9190-a14ac87672d3 | -5.9788 | -45.3621 | 2024-10-02 02:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |


[Clique aqui para ver as próximas entradas](README45.md)
