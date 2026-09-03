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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11f7eb52-de53-3240-97eb-7b25deb34659 | -11.2292 | -51.2879 | 2026-09-03 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 688fccec-8da1-3a5f-b409-522803d2b0c9 | -10.6473 | -61.7549 | 2026-09-03 15:40:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 5b0cc24c-ace4-36f4-af31-fb7dbb406842 | -7.0242 | -59.2374 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 598bc4bb-6605-3756-8131-587a937ffb16 | -14.4835 | -52.1938 | 2026-09-03 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 32dcb38f-4c97-3dfc-9af5-e4f3319b1421 | -8.4488 | -54.6644 | 2026-09-03 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 7318961c-c677-3b27-aab7-e70deb793bd4 | -6.6697 | -59.9635 | 2026-09-03 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 0909d2bb-0219-3f59-b1f6-925d4af6f1b9 | -17.0878 | -56.8534 | 2026-09-03 15:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 159.3 |
| d36ed70a-f45a-3d32-a9c4-32c17cbea186 | -6.7463 | -59.4416 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 186.4 |
| ac6089c9-64fe-3075-9104-9091c25c10f5 | -6.8203 | -59.4001 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 139fd2fc-f66a-3363-ae32-06c6bfe967cc | -14.2989 | -51.7072 | 2026-09-03 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| b3877053-0207-3286-bd41-3aeb856a27e2 | -7.5325 | -60.7338 | 2026-09-03 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 92953f9a-79e8-33c6-9609-f033fa67c2cb | -10.547 | -49.9758 | 2026-09-03 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 08628544-8fd2-3cde-9694-b0d51bda5bb9 | -7.3302 | -60.589 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 61a38924-f81f-323e-b146-13a501ac48a9 | -10.1134 | -45.8621 | 2026-09-03 15:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| fee7e61f-6124-3113-9f59-2ec4822f053e | -6.6015 | -58.9651 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 8238fb43-489a-3fb1-a8ff-e28acd4f602a | -20.8174 | -57.6709 | 2026-09-03 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 144.7 |
| 5a94c673-3dc7-3739-9031-85ddb4565245 | -15.2866 | -53.8617 | 2026-09-03 15:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d22fc158-6532-3a17-b1fd-f0a36365184c | -14.2537 | -52.0964 | 2026-09-03 15:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a93b5984-6e23-3588-ade8-254258a7cff0 | -10.3577 | -49.9957 | 2026-09-03 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b8b9a538-23a8-3ecc-9ae0-f93eff8a5407 | -4.1515 | -60.7068 | 2026-09-03 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| dc4b27fb-b7b6-393b-a01b-b5c87e98fe56 | -3.1815 | -61.1424 | 2026-09-03 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ceeb208b-3fbc-33d9-8ecb-355405f9f271 | -13.8371 | -54.0989 | 2026-09-03 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 8deb1b95-e6d4-3c7e-b853-9c543954e327 | -13.4516 | -57.0592 | 2026-09-03 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| a89e434e-c81d-353c-a5d1-73d8ae19174c | -7.0427 | -59.2366 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 65d16b2f-b60d-365c-b8ac-4cb0860121f1 | -9.4813 | -60.4516 | 2026-09-03 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 3984885f-0b5b-32cc-8ab2-a740f0e4195b | -8.4677 | -54.6429 | 2026-09-03 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 272.4 |
| 81f1a452-b357-3933-9cf8-407a22b14a0d | -20.8573 | -57.7072 | 2026-09-03 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 067576ac-7d01-38ed-aadb-c055ccd8f00f | -7.3301 | -60.6081 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 81f755e2-c8ea-323c-96b3-0c6400aed0d7 | -13.856 | -54.1175 | 2026-09-03 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| a822717a-7e81-3a46-a102-5c79210220c2 | -8.2226 | -54.9814 | 2026-09-03 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 3ffcb74f-8e72-318e-aa6c-17c4a3f3985e | -3.6216 | -60.547 | 2026-09-03 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| b595f051-41e9-3386-b892-3185df6a6730 | -8.7615 | -62.5679 | 2026-09-03 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 201.1 |
| 6e06fa90-31d8-332f-a68f-569ea702ffdb | -10.7859 | -50.4852 | 2026-09-03 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 20028c5d-1547-3179-b439-56a08bc54356 | -17.0875 | -56.874 | 2026-09-03 15:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 976e1a27-74df-3806-a96a-c4320a07db81 | -3.6232 | -54.5931 | 2026-09-03 15:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| c528941c-920b-3568-821b-0f27c515ad9f | -3.6215 | -60.566 | 2026-09-03 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 181.5 |
| 1d8800c6-20f2-3f63-887b-4812a6c70621 | -13.3998 | -51.4183 | 2026-09-03 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| a05f3882-f55b-30dd-9449-69ba90c898a3 | -3.6215 | -60.585 | 2026-09-03 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 954690a7-7968-347c-8837-0f74c6cd0c49 | -3.9251 | -49.0539 | 2026-09-03 15:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 59ae8ee0-c842-3b12-b6fa-0938032fc398 | -7.3672 | -60.5875 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| d5a2ff45-4546-3ad5-8bab-f40346dc3959 | -13.4325 | -57.061 | 2026-09-03 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| ab645d3c-0d95-30f6-afd9-97943edc81ce | -6.8019 | -59.4008 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 656d3bc8-7507-3b4d-a89e-37e650bf8af9 | -7.3118 | -60.5897 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4257d936-1216-38bd-8e10-0f4280b35b4c | -13.4009 | -51.3542 | 2026-09-03 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| cca3abf8-7366-3c37-9e93-4ad97e555bdf | -11.2295 | -51.2667 | 2026-09-03 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e7f462f5-61b8-36cc-89a7-8b991671cb57 | -14.4201 | -52.5201 | 2026-09-03 15:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| bfb78639-2be8-3d82-b7a8-598018665f97 | -3.1084 | -61.1814 | 2026-09-03 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d7a813a8-54c3-370e-b7ca-25bab073395c | -3.3321 | -59.4469 | 2026-09-03 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d08c27e7-584b-35b2-a2b8-70e76fc099a0 | -3.0164 | -61.4848 | 2026-09-03 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 3b804772-5be6-3ea3-afcf-24ac3449b71f | -15.4601 | -52.806 | 2026-09-03 15:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 089f413d-8f2f-3634-98d4-e495f8eed04c | -8.9111 | -62.353 | 2026-09-03 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 4f25c75b-4569-3e61-b132-58a9e35a0f8c | -10.1324 | -45.8598 | 2026-09-03 15:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f916b725-4973-3e44-a1ed-f99c3fd1d868 | -8.7613 | -62.5869 | 2026-09-03 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 15ac5369-b9c1-3545-b7b2-0d6c4d9df197 | -7.0428 | -59.2173 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 9059bd28-db38-3a9d-94f8-45683b926a90 | -13.6233 | -51.8371 | 2026-09-03 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1b3b5a12-f076-39ff-87a8-957f26f81ff6 | -3.7828 | -61.7545 | 2026-09-03 15:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a4cd9166-ddee-376c-9e04-afea0d48a3e8 | -7.5326 | -60.7147 | 2026-09-03 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 5a9272c8-58ef-3bbd-8268-d6c32f3341af | -6.8387 | -59.4186 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 0de89b76-e620-348a-8b29-d72a058b0981 | -10.2214 | -50.3089 | 2026-09-03 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 2c3064c2-087e-3a24-91ab-157d1a63555f | -8.799 | -62.4905 | 2026-09-03 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| fb110bce-dc39-34f6-a0d9-dd2e048a1a51 | -1.4752 | -54.8157 | 2026-09-03 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 870953fc-3525-3d65-a2cc-6a8079b5f7f1 | -13.3817 | -51.3566 | 2026-09-03 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 8d35079f-9744-3486-9474-162bc52c32fe | -3.2179 | -61.2174 | 2026-09-03 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 8678a43e-0e29-328c-ba28-b67cfb74808b | -8.6853 | -62.9307 | 2026-09-03 15:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| df4bb20f-0ad7-33d7-ae3b-cbea937e9c7b | -7.3117 | -60.6089 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 4f643cb1-34e0-38cc-a7cb-ac2db326acc6 | -13.396 | -51.653 | 2026-09-03 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 52462759-dd54-3386-b098-e18e35f3e565 | -11.2298 | -51.2456 | 2026-09-03 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 563bf2aa-8002-32f7-b084-509b6ecccc7b | -17.1227 | -55.9402 | 2026-09-03 15:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 373f0275-3db0-30a9-9fd1-bd6366604965 | -20.8377 | -57.6681 | 2026-09-03 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 159.0 |
| 2adcba44-2948-35a4-8e65-629dce384d44 | -10.5278 | -49.9993 | 2026-09-03 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 25280109-53d2-377d-96ce-1a8af57ad3e0 | -7.5511 | -60.714 | 2026-09-03 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 94843d32-0bb1-3510-a6bc-445264e4dcb3 | -14.4007 | -52.5226 | 2026-09-03 15:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 2f852746-b9fa-35c7-baef-26208018dff2 | -9.6839 | -48.1386 | 2026-09-03 15:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c3294cac-86c6-3b28-ae97-6c5bf9564f56 | -10.6472 | -61.7741 | 2026-09-03 15:40:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 2c4a4322-c8a7-3c3f-bbeb-c33887200362 | -7.2006 | -60.6706 | 2026-09-03 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 1b95dd1f-8fcc-31ad-99be-7a0ff6312a47 | -8.3718 | -62.697 | 2026-09-03 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 2179bcb4-f6f1-3b72-ad73-e83d9046ebcb | -3.1266 | -61.2 | 2026-09-03 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4e4b4530-3617-327f-a8ea-f6fe8e8ca110 | -10.3583 | -49.9528 | 2026-09-03 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e7e3bb3b-b826-34e2-bde9-4cdd0d93df10 | -3.7533 | -59.3231 | 2026-09-03 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 193750f3-1975-30b0-9402-67c69f4e8015 | -10.5281 | -49.9778 | 2026-09-03 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 87edfd2c-79a6-30fe-a94b-47b499857a91 | -3.3504 | -59.4465 | 2026-09-03 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 8cc40ab0-bd35-3547-a309-a49fe35cc7a8 | -6.8598 | -58.9545 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 46d8daae-a6ea-3b12-a6a2-92909752a274 | -11.4892 | -50.344 | 2026-09-03 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 122d2ab6-0274-30bb-9d3a-dcdf19e08dd5 | -7.5137 | -60.7919 | 2026-09-03 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 152.0 |
| e83eb048-0ecc-33a8-988e-b82585495a75 | -9.6676 | -47.9429 | 2026-09-03 15:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 973b4385-d7c0-34c5-aa3f-398fff60f09d | -3.0347 | -61.4846 | 2026-09-03 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| ddfbae37-a3ee-3a6c-9952-d9cc9afe7d64 | -13.8384 | -54.0158 | 2026-09-03 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8b380f31-da87-3538-964d-b6419362281c | -10.2403 | -50.307 | 2026-09-03 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| f89dcede-acd5-3439-9bb1-3f29c410cf6a | -9.4814 | -60.4324 | 2026-09-03 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| af816a40-eb03-3196-b8d4-f6c633fd8bcd | -6.9872 | -59.2582 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| dfc05fe1-588d-377f-84f7-83834b63ceab | -9.4352 | -45.6022 | 2026-09-03 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 166ecb02-f094-3885-9a62-177ac17e1115 | -3.1267 | -61.1811 | 2026-09-03 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 436d04f6-54a0-3a1c-9320-111fdb43f8fb | -6.8202 | -59.4194 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 11dd31a4-946a-3eef-8260-737ee90e5faa | -17.0881 | -56.8328 | 2026-09-03 15:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 0a41d11c-6542-38c6-9c92-1b2516b231f8 | -10.6473 | -61.7549 | 2026-09-03 15:50:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 20b899cd-2d04-39c1-96d8-c7e308e39e5e | -10.5281 | -49.9778 | 2026-09-03 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 48bbeac3-c4ee-3cfa-b6ea-57d914dcf337 | -10.8046 | -50.5046 | 2026-09-03 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 09c06b3e-9fb0-3714-af41-20b15509da25 | -8.4677 | -54.6429 | 2026-09-03 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 283.5 |
| 34c2a156-4208-32f8-b253-c6cc7dd527cb | -10.5604 | -50.3809 | 2026-09-03 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 3114c506-5677-324d-adc8-8d5fe8f43949 | -15.2866 | -53.8617 | 2026-09-03 15:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |


[Clique aqui para ver as próximas entradas](README68.md)
