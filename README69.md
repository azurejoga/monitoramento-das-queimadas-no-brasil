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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6898b196-048c-3f6c-88a2-193866a92efd | -8.74804 | -62.39213 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 973a8306-6923-38a7-89d4-87c6cc376a35 | -13.47684 | -46.96879 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa3df883-7254-368e-9a21-1c8142aba4c7 | -10.47243 | -51.63683 | 2025-08-31 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dd20b7b0-6489-3db2-ba9e-670309d3044d | -9.57484 | -54.49315 | 2025-08-31 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5d22199-5e6d-333c-8bab-5f4317b32d67 | -11.0761 | -52.04071 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f65882dc-131b-39b1-90d1-8508dd5f1d3b | -14.34142 | -51.87772 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bb80b9d-19a0-3f9d-a9d6-884043c24701 | -11.80768 | -46.44913 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 858f69d5-fb82-30fc-b3a0-2b6563f8f84c | -14.04148 | -44.54773 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a1557c0-c631-3240-9bc2-258a1a7bf4fc | -13.35507 | -46.95077 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bd500cce-6803-366b-a8a1-d7fe0ba1695a | -8.6771 | -62.42024 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a101068-3f30-329a-99ed-211034064f13 | -9.43769 | -60.58076 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8fb4a69-a942-3525-b914-07d0a6befb58 | -13.01959 | -56.90875 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c5fa7c0-f1c8-3d14-9a94-84b7302aaf88 | -11.21568 | -45.02761 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fd8d5b8-c027-3c25-b493-3bfcf88071ee | -11.55948 | -47.61706 | 2025-08-31 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8012fbdf-110b-348a-9217-878041080dbc | -11.07655 | -44.61808 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e52e217f-3ec7-3141-b100-79c626c1b1e2 | -7.91453 | -63.0188 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 57eacefb-9e2a-36ef-9f16-ab1b2c9b514b | -10.60104 | -54.91456 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 741ee432-a096-3e57-b5ef-7a52ea660748 | -9.68656 | -62.24876 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 76129753-5598-3d5d-926d-1bcfc6eeee5c | -8.70606 | -50.35495 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 597e9db3-0f22-376a-af5d-e9c116ec7103 | -13.38838 | -47.00748 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b01505d-93ba-38b4-9f83-96e7e1b55635 | -9.43873 | -62.33257 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bd158e1-5b22-3e49-b68b-e8fbeec64d7d | -8.55671 | -51.30144 | 2025-08-31 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0210637-f67f-3b96-8228-6597f80a0121 | -13.02311 | -56.90939 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39e0e29e-ce83-39ac-b9d1-f2320494d30f | -14.15679 | -52.6992 | 2025-08-31 04:51:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea30e66d-d4ce-3a56-970d-103274e4c1b2 | -8.88268 | -62.38783 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5f15507-ce3f-3f85-a18b-34e04a60993e | -11.81644 | -46.86811 | 2025-08-31 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3b41d86-a550-3dd7-951d-57dc77821d90 | -7.74415 | -50.26443 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00a62cc1-a2c3-38ea-9e29-66befef7ea02 | -13.69589 | -46.91398 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 450a4031-3add-3aa4-9f0a-49e02abf2f28 | -8.34406 | -62.9348 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83c62de4-95c6-3f54-ae3b-c772ba427ecc | -9.69505 | -48.29078 | 2025-08-31 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8985216d-7686-3559-a141-37b663ee2d47 | -8.73624 | -62.39682 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d4d19b2-5b4d-34fa-a185-a13beaec23ca | -8.90334 | -62.10067 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80e536be-6992-3650-9642-d81dc53018ee | -8.66932 | -62.43269 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1893fbaa-a44c-3c16-a632-3ee285ef1a71 | -12.97846 | -54.75522 | 2025-08-31 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01e8058e-f4db-3c30-be77-13214ac2d924 | -11.80909 | -46.4386 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07177adc-0e2f-3fc2-bac4-fb1d00ac698e | -14.50173 | -52.98895 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06b49371-3788-3088-a3ef-eb2e3883878c | -11.31727 | -43.68739 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f3bfe93-4415-359d-a1f7-681068d06023 | -14.53545 | -51.98296 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac5c3704-ca63-3c0b-95ab-899e1cb6fa01 | -11.89468 | -46.3848 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b660de07-7b8c-3ee3-a48d-5b640696ead3 | -8.90275 | -62.10384 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deafdb50-da9d-35a7-ab49-706f51988ebe | -11.80977 | -46.43354 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79a1b366-ef0e-3962-bf5b-f36b10bff9a2 | -16.22635 | -52.68132 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc6b6e85-f3e9-369d-8012-ef30a169e51f | -16.22462 | -52.69299 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 411a967f-25cf-3ef2-b7c4-b5da3ac5a8e6 | -15.77147 | -55.934 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7901ce96-4316-3ebc-bc54-fa9869901f98 | -16.33219 | -51.59992 | 2025-08-31 04:53:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f94b1c09-586b-3644-a33d-05860da97762 | -14.58065 | -54.52491 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72e240b8-7da7-38ef-8941-82cf0f86cebc | -15.71253 | -48.94027 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31b59375-92f9-35e6-a43a-a82cda214e27 | -16.97555 | -49.31491 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43044825-9589-34fa-a283-6ee285a7a7b9 | -14.5306 | -57.2192 | 2025-08-31 04:53:00 | NOAA-20 | SANTO AFONSO | MATO GROSSO | Brasil | 5107263 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f41ae107-eb71-396d-bfed-d3d2672b2fc7 | -18.65912 | -49.09549 | 2025-08-31 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2f35d92d-20e4-3673-ba6c-0a2c33d1ea11 | -15.30007 | -52.79592 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df04bd49-c9cb-3b71-bea5-cd1a0ac70f36 | -18.66292 | -49.09378 | 2025-08-31 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7464d123-282e-3de0-8bcd-1a0ef109d844 | -16.40838 | -45.65098 | 2025-08-31 04:53:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8cf2aa69-a900-3760-b9c3-0f4e93992d7b | -16.21891 | -52.65981 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dca2b534-1a48-3e6f-992d-0340e8851e76 | -14.79982 | -59.72247 | 2025-08-31 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76bea1cf-fb19-3886-8aca-37fb2c9d3b17 | -15.68852 | -52.74778 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be6cb8f9-0244-3bef-8ffe-8e3b3c1c2085 | -16.22058 | -52.69635 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| ed6a24b7-ced2-3de4-8ebd-0f77ab5c225b | -14.59344 | -54.4869 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba7d9422-ccd8-3f5d-baef-00684c8e9d3d | -17.60874 | -52.68464 | 2025-08-31 04:53:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 558084fb-c23b-3863-b989-9a888372e225 | -18.65356 | -48.22449 | 2025-08-31 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7933383e-75ea-3766-9234-fe06719f5749 | -14.60991 | -54.53342 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e629401-9325-339f-8e83-3a2383842afc | -14.60268 | -54.55775 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8869e034-96d4-3c01-be75-2c8cebad11a6 | -14.60211 | -54.5613 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd4f9648-d1fd-348f-8580-dd37091161f1 | -16.2195 | -52.65585 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f4145fe-2620-3edb-b90c-7f834f3d7734 | -15.2961 | -52.79911 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6849ffa-bf95-308a-b104-98454d4bdc74 | -14.5988 | -54.56075 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9ec4df0-7d8a-3bbb-a631-9968a9a54d61 | -14.6066 | -54.53287 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b307083d-5336-3ce2-bccc-b22c1fdb8e54 | -15.68794 | -52.75163 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9537f7f-694b-3507-99f7-89e9939eb5f2 | -17.61976 | -44.25857 | 2025-08-31 04:53:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9865c6c-79f5-3b7c-9d7d-162a0178977f | -16.22355 | -52.65243 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1c37d81-f9f1-347b-8950-0a590be55456 | -17.61432 | -44.25359 | 2025-08-31 04:53:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06f546df-b60f-3aca-a648-847aef4d339d | -16.58696 | -56.20568 | 2025-08-31 04:53:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 38eaf79f-c80f-3ae3-9f45-b265e69ca996 | -15.71104 | -48.95184 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1345e1d-3b4c-358b-acb8-6b1c1edf7239 | -18.65962 | -49.09132 | 2025-08-31 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e91af186-f49f-3157-b939-08d95ad01eda | -14.60613 | -54.49266 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c63f245-840c-39ce-b79e-f13d62b129f2 | -15.79237 | -55.91131 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4c3993e7-c97e-3841-a7f4-a88ee73fc725 | -15.71576 | -48.94852 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c564f8d-08a8-335a-994f-b7efa39b2cd3 | -15.16805 | -52.3435 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19c6b21d-a22b-3519-bf56-a9b6fbb852a4 | -17.1424 | -46.07177 | 2025-08-31 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b23d475d-d1f8-3f32-bf27-4bcb851cca46 | -14.60608 | -54.51454 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1004b040-356e-3300-9c2b-191fa9edea01 | -16.22002 | -52.67624 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d752a561-4e13-3d9c-88c1-0915d4ad8bc2 | -15.21367 | -56.0616 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6211fa74-8dd2-349a-a010-f1b458e87515 | -15.6811 | -52.72679 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfac2745-079f-3d2c-b44d-e8369e0fa81e | -16.22231 | -52.68467 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 506aebc1-06ad-3446-a4a8-200d0fcbabe9 | -14.8012 | -59.71484 | 2025-08-31 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb44e7d0-7e8b-359e-9b20-414133722e26 | -14.59661 | -54.55309 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c9bd989-1947-38ab-a8f0-edb89d94cf52 | -17.20089 | -46.99172 | 2025-08-31 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e04377c-5ec9-3736-9f25-d2b907f9dd99 | -14.61154 | -54.54463 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e3432e4-2ddb-3c73-81f1-698015419865 | -15.17152 | -52.34405 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93f1e49a-4b99-37cf-b97e-8d7d28f27d2f | -16.25246 | -48.98811 | 2025-08-31 04:53:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a29f128-17ec-3742-a715-de52007abeab | -17.15151 | -46.0849 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1beaa02-4ac8-3852-a3f4-960c53ccdece | -20.26191 | -46.01664 | 2025-08-31 04:53:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6a14a44e-003e-3318-a66a-da8991103fd9 | -16.99076 | -49.32929 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37df52a6-8ca7-3359-aa8f-6764d29d8fbd | -15.1611 | -52.34243 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16088705-ed36-3f06-a5e0-d4fe651cb9eb | -14.95899 | -54.79539 | 2025-08-31 04:53:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0e66bac-e4a5-35e3-a918-a9d7417f05c1 | -14.6016 | -54.54298 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c96aca4b-2c79-358a-b913-7bb9b95a2a9c | -18.06565 | -45.95281 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c118c891-048a-3d5a-af19-f48c0581c6f8 | -18.06074 | -45.94851 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04380668-1ed1-365f-b5dc-eeb9df7ed0be | -16.99913 | -49.33058 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdf940db-f7c0-36e4-b844-ae8e55e23334 | -20.26154 | -46.02024 | 2025-08-31 04:53:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README70.md)
