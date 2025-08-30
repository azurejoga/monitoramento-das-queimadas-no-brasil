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
| bf3d63bb-5923-3fc3-8411-085ca377938c | -9.24577 | -59.78049 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26b9979d-22ed-3aae-8b4c-b667f35ef60b | -10.6659 | -48.72947 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d7169d14-eb00-308e-945a-1093a61559e1 | -9.44108 | -60.55297 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d56a3f4a-e01b-3400-a931-d918c75541cf | -11.30359 | -43.62061 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57792471-ac99-3e2e-b4c9-c91ab28ff81b | -7.63068 | -42.66327 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0c469088-2004-3658-b966-e7bcfc7246f9 | -6.68622 | -49.77522 | 2025-08-30 04:49:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4b18946-f602-3718-bdcb-9cfbde55bf73 | -6.80339 | -59.97005 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8603743e-421d-376d-864b-8b3736493d68 | -11.84556 | -46.38414 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa6a5ad2-5928-399f-bcf9-fdd509de42c5 | -11.35466 | -43.54748 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64c80cf4-2c73-3a36-a820-d53b8d9f5930 | -7.23647 | -45.42595 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 716eb580-4a53-3efc-ad3f-e699ef2009ff | -7.79119 | -50.96736 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5438ddce-ca55-3724-b286-f6740dc8062a | -11.86749 | -46.44564 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b4c4b35-c72c-3093-8161-7281315e87d2 | -8.29473 | -61.42278 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 020520fc-3df3-3bfc-8a9e-9b006c9b84ce | -9.44328 | -60.57008 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 69343a42-e2c4-3315-a907-33c1b45b0e1e | -11.92897 | -46.69024 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b09455e-17db-303f-b005-c518a0a4388d | -8.8022 | -52.08451 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69630bc4-b929-31cc-b53b-1f8c16cc0793 | -8.55992 | -63.01649 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1089e025-65f2-3e83-bf60-66cfc98776dd | -11.83472 | -46.4651 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06092edc-0d17-3e86-b6cb-adedae4ed871 | -11.29959 | -43.57127 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7502ea2c-a52d-375b-b6d8-942d73b23693 | -11.82627 | -46.4685 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b9119c76-f224-3ee7-9245-17716e68b73a | -7.24515 | -45.45478 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d14fdba-0835-3d7f-a62b-016cab1e6e37 | -7.15163 | -44.90556 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 88b654d7-c78d-3ee2-ad03-854db21bd2be | -11.5677 | -46.3506 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 34fa8fd9-45d4-3424-aeea-40692a408a8f | -12.69753 | -46.80829 | 2025-08-30 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 101750ca-949f-360a-8a13-88c876daee50 | -9.22116 | -46.76438 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99c65ad8-3f8c-3f2e-a0d7-ef467315926b | -11.93417 | -46.68324 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd08e0e4-0d17-3987-8bfe-e8e581bf2d4d | -9.44414 | -60.53681 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ef7e267-69dd-3782-8844-a6b6a3093711 | -10.9629 | -49.57141 | 2025-08-30 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddb797b7-fc86-3fea-b5de-45e0a44db618 | -10.84262 | -53.77155 | 2025-08-30 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7753e000-23b2-39ae-b9ad-74c1bec8a3da | -7.72161 | -50.30636 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac2e54ef-6bc6-3d70-8ad0-4c2bd2205bdc | -11.06497 | -52.04243 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63a93f38-5183-3ed2-826f-897378219647 | -11.35631 | -43.55093 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc44749a-d0f2-3339-bb28-22ea80622619 | -7.95434 | -46.39171 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83a7f3e2-0b86-3d67-b5c6-8593b80f112d | -9.65523 | -54.43631 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a11fde7-e325-334c-b5b0-1985185b70a4 | -11.31647 | -43.64085 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fa72444-92d1-3363-a621-10e00e9c2826 | -8.55938 | -51.30709 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1bed46e2-7a51-3810-afaa-869236be659c | -9.43524 | -60.55526 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3b22967-66fd-37b6-921e-1b767074657b | -9.43763 | -60.54252 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 61eb17c7-e125-39ed-8b2f-74f5be2629f2 | -11.3071 | -43.63342 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b941d2f3-b52e-38ad-b12f-bead03028e4e | -9.45628 | -48.25714 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f612ed0b-06a3-3d5a-9e48-348872efe357 | -11.77752 | -47.55815 | 2025-08-30 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e120c632-9a77-35b6-829d-2c63bcd9f300 | -11.1459 | -47.15516 | 2025-08-30 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 445c2d09-6fe6-3941-a02c-250c2846b671 | -6.95003 | -44.06394 | 2025-08-30 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cfd2b7f-d575-3937-8323-cfe4b3809065 | -11.83693 | -46.45397 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5115523a-334f-32da-a7ed-99e9d440081f | -11.83855 | -46.4425 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6ce733cc-2df3-357b-b344-205b7f429b6d | -9.18015 | -59.5814 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4401cfb3-73d6-34cc-84d0-1d711175cc5a | -9.69131 | -48.30344 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edcfdb28-36db-3eb0-ba5f-ae36d5809cd0 | -8.71609 | -50.36903 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15e5b780-eb17-3153-8ca3-b74b0924d5c4 | -11.3498 | -43.5843 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c0bd474-5f68-3ba0-932b-3cb9c5f2cc19 | -9.45272 | -62.34134 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 769e7c11-976d-3c8e-9a05-d25dd5654380 | -9.44127 | -60.55278 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9511cde5-416a-3c30-ba85-ffe19d2046c1 | -7.39885 | -45.92366 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a2dbb19c-96e7-3517-bcd9-8d94029d6bde | -7.2445 | -45.45443 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16cdafc9-606f-3d2f-9a6c-4f8460cf9458 | -11.83529 | -46.46563 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 9d0ad5ea-5f16-384f-be46-e2a007bc2f8e | -9.11142 | -46.04599 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f26ae98b-4a01-370f-905c-30d1250ddee6 | -7.20035 | -43.70429 | 2025-08-30 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ef6ae21-b5b0-3b07-a4fd-e1285f021052 | -7.33384 | -59.64011 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bb87d78-2402-3bd7-8e3f-a1088506ba6a | -11.36205 | -43.57024 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43ffa1a8-3eed-355a-84fe-f510d4b5a809 | -11.8659 | -46.39364 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6bd7e71e-87b6-3409-90e1-6f903fd1eb5b | -7.61086 | -44.72571 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cbfc721-3bc1-3914-9ece-f6cf9256230d | -11.14989 | -47.15579 | 2025-08-30 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 83c80ae2-0961-379b-a505-038c8feee169 | -11.32077 | -43.6475 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b84331e6-6011-370e-ae32-4351afd57a76 | -8.87112 | -60.73538 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6363c03d-57e8-381c-895b-2afa153ab042 | -11.88924 | -46.72074 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e941e84-804c-3f72-b8c1-ff32d53f4e2f | -11.30127 | -43.63848 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 677be2a7-7196-3125-ad01-0b5d354e8576 | -7.6024 | -42.71541 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 946855e9-d910-3599-b84e-541ceae79ecd | -11.87542 | -46.45069 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 336e1c45-b9d9-36da-b0c6-9ce24541ba12 | -9.17033 | -59.57949 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25574584-a87f-3810-a6fa-155ceb6e7a29 | -9.70788 | -49.46839 | 2025-08-30 04:49:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cca8cefc-4162-32d4-a2b8-331afb27b099 | -7.62163 | -42.72736 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2753886d-620a-3aae-b30b-3da7c78f25d1 | -8.69035 | -50.3797 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da9a8439-f62a-3bcb-b283-7dd5618c427a | -9.7073 | -49.47225 | 2025-08-30 04:49:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 5dd50bbc-f8db-3162-b9ff-32ac9dd7d0d2 | -9.44227 | -60.5466 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5190a5f2-5f67-3708-9c08-0aec996bbfe3 | -7.43052 | -44.80338 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e3278641-558d-3017-a3cc-11f57dcef53c | -7.63729 | -42.6627 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d6eaff3e-d1ac-3027-ad5e-54284e946c02 | -9.44708 | -60.5505 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 40ba930c-0bd3-32cc-8686-f7d76ee762fc | -11.84669 | -46.38481 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a315ca8-c1b0-390b-8b97-468665de765c | -11.86687 | -46.3865 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77b738a6-d6b3-3d51-9ee0-55f92056a439 | -7.59174 | -42.71682 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6bfb3503-99d4-3ac0-8181-5d4f0d56b13a | -10.37973 | -57.82153 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c0b561-0ec1-3b2c-af8b-5e7d70e0dcd0 | -9.4644 | -62.34383 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ef64815e-e0ec-37e8-a4ed-20637ce19569 | -10.02343 | -48.09145 | 2025-08-30 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f333e60f-d151-3420-99b5-89bb39f7b7a5 | -7.74162 | -50.26581 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| accc432d-ad55-3927-860e-808f1be64f78 | -7.37788 | -48.19296 | 2025-08-30 04:49:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d994f38-664d-3991-900a-13f56c0fd873 | -11.31531 | -43.64968 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fb20322-1f62-3022-9e03-af377f2fc748 | -8.51715 | -54.71671 | 2025-08-30 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 852b5aa8-828c-3ee3-982a-5e546184033e | -8.34878 | -62.93431 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c86df81f-f532-3a58-a6c1-d1a0f45eaf0d | -9.50766 | -49.10143 | 2025-08-30 04:49:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58b1e5b0-8e4d-393b-9f91-7c32aaff3510 | -12.40356 | -46.4794 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa144a8f-d766-3708-a4fa-072f3d8143fc | -11.91496 | -46.6997 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52b4bbdf-62dc-3a48-b763-e2b7ff5b2f80 | -11.37549 | -54.34013 | 2025-08-30 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 58b33068-1c23-3526-9de9-d33620f8a579 | -11.77682 | -47.56319 | 2025-08-30 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b7b8940-e89b-3bae-ab27-18227de59fba | -11.41108 | -44.6865 | 2025-08-30 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9c86e2f-9fdb-3bb2-a84f-2dae575b2b99 | -7.22202 | -45.43605 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3271a82-6ab7-30de-87b2-df3288ae5fb8 | -7.39403 | -60.59143 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90f2361a-8f3c-3f53-952c-68f148c7abe2 | -7.956 | -46.38048 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46b96aeb-622c-3769-a3ee-13cf53151756 | -10.46114 | -57.94478 | 2025-08-30 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6951cfb7-ad8a-3267-8c7a-3d979e2ff4e9 | -11.32432 | -43.62031 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5a2007f-8fe9-3247-8410-44dbe101f1bd | -7.40141 | -45.92305 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9fdf87e-354c-33d9-8d6e-ff3f3f1600d9 | -11.87496 | -46.39064 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README48.md)
