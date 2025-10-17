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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7daad49f-d07f-39c1-9038-c8fbaf396582 | -8.41418 | -46.28286 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abb51292-de02-3794-bd18-fb2ea963555f | -12.39984 | -57.79579 | 2025-10-17 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afb3464e-0010-362e-91f0-6ae62a7f1f18 | -9.01206 | -62.00913 | 2025-10-17 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1ef6e0f-7e1f-39a0-845f-429b88350651 | -8.16136 | -46.0673 | 2025-10-17 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d49325b6-9096-32ce-8de6-f1925fdcba2b | -10.53052 | -49.55364 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4bd0d209-09f1-33a1-8a03-6b82eb7cd5f8 | -10.54291 | -48.55402 | 2025-10-17 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8fac44e-9f62-34bf-b88e-a4df63fff2a6 | -7.90311 | -44.98376 | 2025-10-17 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4352cf5-43f6-344a-a258-2f7f858c90f1 | -9.44415 | -56.65323 | 2025-10-17 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f40fcfe6-c428-315b-ae6f-709a0e66a14d | -10.26367 | -44.04701 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c966adcd-8f2c-3470-bc9d-de4cc0ff7aa7 | -9.96158 | -47.02998 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ea79bd6-2946-3999-af0c-f3cc650fda12 | -7.95272 | -44.1556 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7398471-819d-3c73-b042-d91493fbe776 | -10.28136 | -44.04502 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60560281-6d93-3efe-82ee-01db654dd8a1 | -11.95324 | -45.36217 | 2025-10-17 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3de971f2-dcf7-3d64-8799-d05c9fc0a356 | -12.42803 | -51.30951 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cdc719c4-09f0-3f88-8015-5a21137e1d61 | -6.53317 | -55.04972 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb060fe6-5aca-3d4e-b77b-22523dea6cb2 | -10.13471 | -44.54768 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e31f8dd-a24a-3535-888e-455a1a3d486b | -12.42738 | -51.31447 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 127bd85f-f55b-3722-ad58-d27abd8637ea | -10.91934 | -47.8752 | 2025-10-17 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2631b449-6546-35d1-876c-88a7258e664d | -11.00094 | -55.4195 | 2025-10-17 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9804be2f-a7f5-33ae-8d27-b47e6a63d4f8 | -9.09874 | -46.68581 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0de76fbe-2a92-3b0a-9bd7-3c7cb536b794 | -10.94187 | -49.47926 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8e710ff-d6e8-34fa-980a-2d7e91eddb78 | -12.41872 | -51.30825 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1cc79647-8b07-3e76-af7b-0d477fc31a6c | -9.08396 | -48.03088 | 2025-10-17 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6dbc19d2-bec0-3dc2-8c17-322a543aa08f | -10.64329 | -45.30148 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2c4a7a8e-1c38-345b-a18f-5a0102cc2f13 | -8.45044 | -46.2438 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1975a50-fdb4-33ec-b781-c44e1b53b3dd | -7.05414 | -46.68725 | 2025-10-17 05:10:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2225000e-5faf-3cab-a11b-60e81db936bd | -10.26288 | -44.05363 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85c93d07-3723-3ed2-b78d-eb3b04cc21f4 | -8.45463 | -44.18221 | 2025-10-17 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dd641b0b-bc9b-38dd-ae08-ab9795c432c8 | -10.11027 | -44.56413 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a9f9453-7e0c-3f72-b4d9-c254843e35cf | -7.20177 | -45.49384 | 2025-10-17 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4de7a99-52eb-351d-b9d5-4a7412bc0251 | -9.30049 | -46.93198 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bc5ae5a-54c3-3e7d-888d-31a06412a0f0 | -9.07839 | -48.03035 | 2025-10-17 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a4a6076a-f0e1-39c1-8e31-b7420eac4f5e | -7.00049 | -46.99461 | 2025-10-17 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dd5971a-4d18-363e-a6e3-b71dcbe7c844 | -10.123 | -52.34822 | 2025-10-17 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2759f39-94fb-3e18-8ca8-b91ab204b676 | -10.11145 | -44.56435 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9f8e553-6e97-31ad-aeb9-2bdbabdef63b | -8.50056 | -48.49402 | 2025-10-17 05:10:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c332571-8d34-310d-99f1-38b0bf7572b2 | -7.98053 | -44.15936 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4bb0a303-39ad-31aa-8c11-38b5dd5a191f | -9.28763 | -46.91389 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c429197-109a-3130-9f7d-d50a81a22970 | -14.9238 | -46.7206 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18b2ba04-5a74-386c-b82c-99d8f6d989f2 | -14.23427 | -54.89769 | 2025-10-17 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5eef57f9-1724-3335-838f-589d10406f9c | -14.3032 | -58.15144 | 2025-10-17 05:12:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7f01dad-d34a-395d-821c-5aff7078bbd9 | -17.56801 | -45.60723 | 2025-10-17 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adddbb5e-9575-347b-a1a0-8c6343961d98 | -14.93747 | -46.71552 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d65f134-7345-3029-9003-0077a6f407e3 | -17.57069 | -45.61523 | 2025-10-17 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 479c5fc8-e4eb-3434-be25-d4c44648823b | -14.29987 | -58.1509 | 2025-10-17 05:12:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98bc92d6-4a78-3edc-96b7-f4add96512a8 | -17.81605 | -57.62492 | 2025-10-17 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1a8a4328-fb40-3b07-9c23-2b9d247ae923 | -15.02785 | -48.76419 | 2025-10-17 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7daa0cc7-a4ba-3057-82a4-3a9d2b54e945 | -18.56372 | -54.54124 | 2025-10-17 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a67e245d-df44-3bbc-91f8-a6d208b6499a | -16.81539 | -53.92072 | 2025-10-17 05:12:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 953f1e6e-73e0-3f96-8d9f-540200e7997c | -14.86624 | -52.44076 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfc7d786-913b-31dc-b8de-2d7791f6b40d | -18.3331 | -51.69528 | 2025-10-17 05:12:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 823db2d5-727a-36ea-a7dc-6ae3149918a8 | -12.13415 | -64.29506 | 2025-10-17 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c8d6b35-5944-3ac8-8c9e-6af3834cb00b | -14.89033 | -52.43018 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae68a6bf-e85c-3004-ad51-c3f6c89b4664 | -17.56742 | -45.61422 | 2025-10-17 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acc4731e-f242-3bd7-92cb-8d7d7a9308c6 | -14.23662 | -60.19561 | 2025-10-17 05:12:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02734099-ea6e-3465-a0dd-f7d716bae4d8 | -18.3804 | -55.4598 | 2025-10-17 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a5f4d60d-e5ef-3bad-b019-5d84ac6d7a67 | -14.89538 | -52.42628 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f04d7cc3-e41e-3701-9104-ea1484c4700a | -14.91637 | -46.73012 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32bea045-650d-36f8-becb-39badfa98032 | -15.03177 | -48.76371 | 2025-10-17 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c816aaf6-387f-3d17-abc1-d867ee080db4 | -14.87633 | -52.43298 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c22fd60-91fe-3b9b-a379-5068621819f4 | -19.44078 | -55.91956 | 2025-10-17 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 68057069-e57f-3f01-b58e-60826480d773 | -18.33734 | -51.70198 | 2025-10-17 05:12:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 443297ab-3ed7-3271-8ca8-731424ddfeda | -14.8948 | -52.43079 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6213d85f-b914-3d8c-9956-c7d28413fb4e | -15.0455 | -47.31221 | 2025-10-17 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc941df4-062d-3687-8fa3-365574081eed | -19.44459 | -55.92014 | 2025-10-17 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 86c77fb4-ac82-327e-947b-6736706d3be4 | -14.6815 | -60.26292 | 2025-10-17 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b533c19-6d75-32d7-9012-8bee27d94459 | -14.87575 | -52.43747 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edc6428e-8e8c-3679-9917-f6dab59cefd9 | -18.2747 | -51.30422 | 2025-10-17 05:12:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8dfb559-f518-3200-9d11-7c902c0b42d6 | -14.2398 | -54.91299 | 2025-10-17 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f8d0872-82ff-36c1-b8f4-a55f021e28bb | -15.02615 | -48.76221 | 2025-10-17 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12495b03-3357-3b48-95bb-0f1366c34c6c | -14.23292 | -54.90716 | 2025-10-17 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4ea7740-abf6-37ab-8c5e-c57eb5a538c6 | -14.23327 | -60.19503 | 2025-10-17 05:12:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9c0ca7c-ca58-3837-b9f6-16e109e00858 | -17.56417 | -45.60813 | 2025-10-17 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 219ef15a-18a0-37a6-8345-b4b91526c805 | -19.45602 | -55.92183 | 2025-10-17 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0feb6575-096c-362f-a10b-d09ae8389baa | -14.86681 | -52.43632 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 047f06be-d91a-3c75-9122-5ce7bf440cf6 | -14.23669 | -54.90774 | 2025-10-17 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9f66250-ef50-371c-a801-5fd57bd2ddb0 | -15.03315 | -48.76873 | 2025-10-17 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74bed56e-7247-3452-8895-cea7acaa690a | -12.43024 | -64.14338 | 2025-10-17 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fcf549b-e812-37dd-b413-5f496c7647bc | -14.87127 | -52.43696 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d8e36d3-79d6-3c87-b193-6ab13613496f | -14.87247 | -52.42772 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a725c337-ecad-3f58-bb3b-d5eae3b3ee00 | -14.89093 | -52.42559 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9924a9f8-66dc-3b59-b5dd-da2e4e29f85a | -16.68511 | -52.13032 | 2025-10-17 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c6bd2e5-5a6b-310a-b186-d767f3d56985 | -14.23359 | -54.90243 | 2025-10-17 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a861d2ed-6633-33f6-a977-d1478d6b77ed | -14.92278 | -46.73017 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a25a8ead-e544-3348-8688-433048c93d88 | -14.89598 | -52.42175 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2f129bf-e556-342f-84c5-45cb1432812f | -14.91577 | -46.73442 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf1b1bcf-8fd6-31b1-8764-eb3d1c7aa521 | -14.23737 | -54.90301 | 2025-10-17 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7503aeda-1e95-364f-8c1d-85bf098acd18 | -14.23805 | -54.89826 | 2025-10-17 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e3140331-16fb-34f5-92a1-c3a20a50da13 | -16.54996 | -52.44216 | 2025-10-17 05:12:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0fa30a2-0caa-3957-a0af-672ea1b4ceec | -14.9233 | -46.72633 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af37bb15-c693-38b3-b6d6-bd333703e4cc | -14.8707 | -52.44137 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8fa02fb-fb4c-3dc3-8777-c994eb8c39da | -12.13486 | -64.29108 | 2025-10-17 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 079e7008-0d3a-3829-93eb-839979dbc7d7 | -14.93086 | -46.71643 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2eb605b5-cdea-320a-8385-f16b1d48cfa4 | -14.9374 | -46.71665 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54671dc3-68a7-32a6-8540-f2fc5bde198b | -19.06198 | -57.49352 | 2025-10-17 05:12:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8d3ccd6d-e4bb-3d9d-859f-10c3b90f1e32 | -14.86741 | -52.43171 | 2025-10-17 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37754a91-a82f-3adf-be17-32d189dc1818 | -19.05847 | -57.49295 | 2025-10-17 05:12:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1d3f9e4b-0947-3d97-9c5a-78fb5c7dcefb | -14.92378 | -46.72156 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 405a4d60-b5d0-3537-b17f-8ae32a37d039 | -16.80654 | -53.92368 | 2025-10-17 05:12:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ed69161-b9d3-3d47-8448-07b3080de152 | -18.38492 | -55.45535 | 2025-10-17 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README113.md)
