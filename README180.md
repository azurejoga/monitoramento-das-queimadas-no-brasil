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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb3c36eb-e4c7-350b-ba53-bd3a60758f1a | -7.5139 | -55.2851 | 2026-08-28 20:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 50d16286-090f-3aae-8913-fc5b260a116c | -6.7653 | -63.0352 | 2026-08-28 20:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 5e1f7911-e443-36ce-8070-ca9a9578c105 | -8.0301 | -48.0145 | 2026-08-28 20:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| bf97fafa-79d4-362e-8d9c-9c2f2c53899c | -12.3611 | -50.5846 | 2026-08-28 20:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ec72672e-7f1a-3dbb-bfdf-f428fa6a404f | -21.5147 | -55.42 | 2026-08-28 20:20:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 07faa001-d1ef-3249-83b3-892a7120458e | -8.5969 | -54.7755 | 2026-08-28 20:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| ab74c0f8-5886-3d0a-839b-32a88f23bd3e | -11.0445 | -57.2023 | 2026-08-28 20:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 266.4 |
| ba1d6a8d-cdde-3e0f-b52d-8b5bc992ecb6 | -14.4057 | -50.0537 | 2026-08-28 20:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 1f0f65a8-9e87-3455-a0f1-313a7a751cbd | -14.9386 | -56.3216 | 2026-08-28 20:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| f5880426-de9d-3963-9172-0b1371a33a71 | -6.7248 | -59.9998 | 2026-08-28 20:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 364b6eb2-eb97-3115-8fe7-6da830d2f108 | -9.1425 | -61.0069 | 2026-08-28 20:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 214.6 |
| c03b90ba-8913-3e1e-abbb-13f54373b8b2 | -14.1788 | -48.7481 | 2026-08-28 20:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 123.9 |
| ecbfe4fa-6687-375e-9649-363c3e1389d7 | -17.9681 | -50.1762 | 2026-08-28 20:20:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 265.8 |
| 00baed0f-7b96-31d2-baf1-ce4e58ce1668 | -5.9079 | -57.7506 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 54ac3513-d8e3-37a0-8439-157abeeee133 | -11.0244 | -49.6872 | 2026-08-28 20:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 506ea818-4161-392a-be1d-cbf1a59ac138 | -13.471 | -57.0373 | 2026-08-28 20:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6289fd13-edd1-3711-900e-a798717d0469 | -11.6215 | -54.5742 | 2026-08-28 20:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 10956266-039d-38d9-9dcc-b1a23ef69292 | -6.3277 | -44.1028 | 2026-08-28 20:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 03ae2a64-0312-3c30-b401-ab5ecfa9f9f2 | -2.5515 | -45.3387 | 2026-08-28 20:20:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ec9ba85d-29a1-3460-80f0-9da419c134c8 | -9.0012 | -57.5585 | 2026-08-28 20:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| c396d584-9c41-3a9e-80b4-c338ce741d22 | -17.988 | -50.1725 | 2026-08-28 20:20:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 195.8 |
| 46897252-79a5-34fd-bdc9-a560f709ba14 | -5.8894 | -57.7708 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 261.3 |
| 7215d522-06f0-3a68-bd44-da7cc83480f4 | -5.8895 | -57.7513 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 285.2 |
| c4212d01-adf8-3555-8864-f9d8a372c7cc | -6.8756 | -59.4171 | 2026-08-28 20:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| df40e832-0c3a-3256-9636-1189647dc771 | -14.622 | -50.9117 | 2026-08-28 20:20:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 3fc9d487-3f8a-3135-822b-4eb1d6859afc | -12.3799 | -50.6038 | 2026-08-28 20:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| da4b242e-065b-3de4-bc4b-194db535f294 | -9.1424 | -61.026 | 2026-08-28 20:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 8107918c-2333-397d-86b9-03d398936179 | -10.5523 | -59.6161 | 2026-08-28 20:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 63588465-8bf8-3376-a8c6-ee5061ee6074 | -5.2634 | -43.7444 | 2026-08-28 20:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b380d4f2-b55d-34c6-ae13-17f948210619 | -6.1472 | -57.7995 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| d6334916-6e88-3ee8-a3b0-a5c512bacf56 | -4.1934 | -54.5755 | 2026-08-28 20:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| fd178035-8a09-31c4-90cd-2927b4fca260 | -17.9875 | -50.1948 | 2026-08-28 20:20:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 785b32dc-1750-3399-a570-51c2bd2cfcdb | -14.1597 | -53.1219 | 2026-08-28 20:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 6bd76ae0-8920-3b93-9c11-b673504be0aa | -6.9193 | -44.9467 | 2026-08-28 20:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a38c110e-ba40-3d20-aefb-8c92694f925c | -8.5366 | -55.2625 | 2026-08-28 20:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| f2b7b2d6-583f-3853-9c5e-cd11fa15837e | -8.0113 | -48.0161 | 2026-08-28 20:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 4d167779-bb0b-35bc-9973-7669989ff0f5 | -4.5695 | -44.0427 | 2026-08-28 20:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 072c9a0a-af83-3809-a5e3-188406511da5 | -4.9778 | -49.623 | 2026-08-28 20:20:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 154.6 |
| 0f6abbbb-1b65-3099-8fc8-30d5233221b8 | -5.1412 | -44.9897 | 2026-08-28 20:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 65166245-25a2-3bbb-a3d6-52dcbac930ca | -8.0115 | -47.9943 | 2026-08-28 20:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 0e5cf266-db98-3a10-ab68-c2af474288da | -8.1432 | -64.0053 | 2026-08-28 20:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| b0b064b3-0a87-372b-a976-853ad31195cf | -5.5387 | -44.37 | 2026-08-28 20:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 9716adc2-fc06-33f8-8cb7-14602b85f14c | -14.1784 | -48.7703 | 2026-08-28 20:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 34cf1d42-e181-3848-b7bf-ee91e3183edd | -5.2896 | -45.116 | 2026-08-28 20:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 05d6319b-2bb0-3b20-8845-09117f5cb48e | -6.3467 | -44.0782 | 2026-08-28 20:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 5d024547-6416-3545-96ad-cc682abb6e9c | -8.6156 | -54.7743 | 2026-08-28 20:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 904bccb2-0dcf-36cb-87a5-adf032019842 | -14.3376 | -51.702 | 2026-08-28 20:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 0343d4d7-2ed0-3016-a0d5-dec03d2b9c7b | -7.3087 | -72.8449 | 2026-08-28 20:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 0bc1da48-3236-32ae-8fd2-c85e8a5c5840 | -12.7608 | -44.2373 | 2026-08-28 20:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| bca026cf-bab4-3703-a784-171e129534dc | -14.9015 | -52.6055 | 2026-08-28 20:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ffeabca9-32ff-3973-9bb8-80dbe47d6463 | -3.1998 | -61.161 | 2026-08-28 20:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ed27e7ff-6263-3b9e-847a-ff8d395596e6 | -9.8552 | -60.2966 | 2026-08-28 20:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 0fc05da6-dead-34f9-83ab-0a62acd3cb6b | -11.0256 | -57.2038 | 2026-08-28 20:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 64ed8ada-c829-3ce6-8f35-1d78c713ef0d | -11.4972 | -45.084 | 2026-08-28 20:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| cc23ec68-9b77-3aef-9cf7-47864d0bb389 | -17.9676 | -50.1985 | 2026-08-28 20:20:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 345.6 |
| 23ddebcf-1a26-36ae-98c9-6e302247bdf4 | 0.1367 | -60.393 | 2026-08-28 20:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 44f92ad4-8970-37b8-b1a4-9bd28bb10579 | -14.3569 | -51.6995 | 2026-08-28 20:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 85691f4f-bb04-358a-a335-2ebd184b2777 | -6.0004 | -57.6884 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| e3619226-9feb-3345-bfce-378a5a497740 | -9.7264 | -47.7827 | 2026-08-28 20:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2a7f1d94-39d1-3a89-b0c4-c6d115d41817 | -6.3465 | -44.1013 | 2026-08-28 20:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 215.3 |
| 684acd2a-121c-3ee8-b0b3-8a91fb607462 | -8.1617 | -64.0047 | 2026-08-28 20:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| b0760d8c-d7a3-3e36-b22a-39c1253abd71 | -6.3279 | -44.0797 | 2026-08-28 20:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 94cc4cd8-f743-3d7e-a2c6-ee01b8bda1d4 | -12.3608 | -50.6061 | 2026-08-28 20:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 72b903c0-34e0-31c9-940d-734a357d2e45 | -11.0254 | -57.2237 | 2026-08-28 20:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 218.3 |
| b6b42fc9-00bc-30df-8f06-51430ef3ebe1 | -3.6216 | -60.547 | 2026-08-28 20:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 201.8 |
| 89720af9-4142-3f8c-9e9e-ecc08b0ba85c | -5.2696 | -45.2756 | 2026-08-28 20:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| b6a1bfb1-9ea4-337e-b840-08652163baf2 | -21.5152 | -55.3985 | 2026-08-28 20:20:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 40445e52-bc33-327f-bee7-02652f1b1631 | -8.3785 | -70.8456 | 2026-08-28 20:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 99994b0a-0b12-3786-a98a-62c3d2e66959 | -14.3762 | -51.6969 | 2026-08-28 20:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2f6f530f-8f21-39fb-b031-c5df531ad54a | -2.7304 | -47.0424 | 2026-08-28 20:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| a3e345a7-50cf-3fca-a294-c3333a83bb71 | -9.1525 | -49.9639 | 2026-08-28 20:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| ac54ae0d-c4db-3a2d-9ea6-3901ee155faf | -4.9593 | -49.6239 | 2026-08-28 20:20:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 3f3c8a04-2558-3f02-9206-882fa87f0f5a | -9.1523 | -49.9853 | 2026-08-28 20:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| bf44dfb8-eb66-3d06-a611-5ca3be0aac3b | -5.2446 | -43.7457 | 2026-08-28 20:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f65ba197-600b-311f-9002-4816c26ff0a1 | -7.4953 | -55.2862 | 2026-08-28 20:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 9e6a4841-343e-3f09-bf5d-d7032ae05c82 | -3.6216 | -60.528 | 2026-08-28 20:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 90e1ee0e-c652-3666-b878-df8bb822b32b | -14.5831 | -53.1533 | 2026-08-28 20:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 62b4d7c5-fbee-3c83-9feb-6c2ade55ffbd | -5.9819 | -57.6892 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7343d6c4-78dc-38bb-bb93-285ce9eabd5b | -14.4061 | -50.0319 | 2026-08-28 20:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f522d6d2-ec05-31af-a916-c634e96e8e32 | -6.857 | -59.4371 | 2026-08-28 20:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| cb252b90-c475-3d8a-9e0f-fffeec41667d | -9.4728 | -45.6206 | 2026-08-28 20:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 6b5275c4-50b6-3bbc-8914-007a704491e4 | -6.425 | -43.7478 | 2026-08-28 20:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 98e53d98-28db-3a01-8c81-2d99dd6bfbd1 | -10.5149 | -59.6184 | 2026-08-28 20:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| b1f17466-1ddc-38a7-8b57-f9454f389b71 | -8.5783 | -54.7768 | 2026-08-28 20:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 6a81d67a-dd02-3979-b3a3-76984f3423e7 | -7.0474 | -55.69 | 2026-08-28 20:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 42fb155a-7bb3-3814-b332-c7a382e9018f | -15.577 | -56.2916 | 2026-08-28 20:20:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 701b8291-b252-33e7-8c61-8efe8a79ef1c | -11.2317 | -53.9958 | 2026-08-28 20:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| f356d984-dc83-3a01-abb9-0ce9370b83b2 | -7.5516 | -69.9963 | 2026-08-28 20:20:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 94390edd-58db-344b-b49d-26c9e2c596ae | -4.5507 | -44.0668 | 2026-08-28 20:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 56af508c-3250-3a64-90a1-bed8ed0cf446 | -5.871 | -57.7715 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4419bbcd-c944-3cea-8a7e-eb75accb95cb | -4.5508 | -44.0438 | 2026-08-28 20:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a21b5284-d220-35ee-a8e8-2492f9bde578 | -4.5694 | -44.0657 | 2026-08-28 20:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 6c383466-01d7-3eae-b94b-afab5e10dc09 | -6.9336 | -58.9514 | 2026-08-28 20:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 67d6349d-ccc7-3b22-be2d-8fd6e9fec3b1 | -10.4499 | -46.2052 | 2026-08-28 20:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 1f0b310a-6857-30b7-96c2-98b27dfe64e0 | -9.1239 | -61.0078 | 2026-08-28 20:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 25e777a5-df59-31ce-8f3c-20d4e3c8f20e | 1.2055 | -51.0389 | 2026-08-28 20:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 133.8 |
| bc18a30c-3ff2-3ee4-973e-cdb97b5a1783 | -11.7167 | -54.5244 | 2026-08-28 20:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 186.0 |
| ea41cac7-0d14-3fa9-8d9e-3d1574af6449 | -6.8569 | -59.4564 | 2026-08-28 20:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| cb1a3d1b-8622-3ac0-84ad-907fece133a8 | -5.2709 | -45.1173 | 2026-08-28 20:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 239.4 |
| d849b5e4-7d0e-3c57-927c-8ca08895155e | -5.5221 | -44.1185 | 2026-08-28 20:20:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |


[Clique aqui para ver as próximas entradas](README181.md)
