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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84604bf1-d576-3467-b983-8f07f2db24f8 | -8.4314 | -45.8467 | 2026-09-20 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 3d61552a-d643-3f23-903f-c51efebf69de | -13.241 | -51.7571 | 2026-09-20 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| e5370fa1-8424-3104-a673-e8ddba8f8db8 | -7.5337 | -45.4141 | 2026-09-20 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| eb166348-121c-34a7-95b3-88a4ecb264f9 | -14.1253 | -45.6136 | 2026-09-20 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f10f01bb-5596-3368-b0a4-85b1320e5000 | -8.9752 | -44.6722 | 2026-09-20 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 19161403-8d0a-33fb-846b-fad712e5812d | -14.6856 | -46.6886 | 2026-09-20 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 84e5dada-b357-38ed-8b67-dafeeb590e5b | -15.4174 | -53.0236 | 2026-09-20 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b6f99c24-79be-3501-ad2b-4d3217304ba9 | -12.1328 | -47.041 | 2026-09-20 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f0d78f24-1dc1-3ada-9c44-9fe1cd04ae0f | -10.7899 | -46.3429 | 2026-09-20 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 51b03d50-c669-30b1-8d5f-29a7e9e0290a | -8.8636 | -45.9596 | 2026-09-20 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| dd92278d-d3e1-38bd-af9d-960371719feb | -10.8757 | -57.1554 | 2026-09-20 13:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| afe7a526-c22e-3696-a8a9-3fb5d9332b66 | -12.5227 | -50.0267 | 2026-09-20 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| db53a7a0-f259-331f-977a-fbff76a5bb9c | -12.5224 | -50.0484 | 2026-09-20 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| bd5c0916-f061-3975-9b50-55bc79bc5e4a | -14.7051 | -46.6852 | 2026-09-20 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 393.9 |
| 799b10e2-f201-3e67-9725-618bcccdc9b4 | -9.3609 | -48.3251 | 2026-09-20 13:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| cf632de8-8cea-3c6e-a7dd-c50aa7f6df8c | -13.2602 | -51.7548 | 2026-09-20 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 87978877-d2da-3d10-89e7-8c67ed04c1a0 | -9.84 | -46.4136 | 2026-09-20 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 7827299f-c83e-35c3-9efa-d9b97faf3de1 | -11.118 | -54.0268 | 2026-09-20 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 161.9 |
| bdd126a9-df83-3696-bcf3-84c5ebde0f33 | -7.2519 | -55.5994 | 2026-09-20 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8c9b1809-0105-3231-b324-f86aa6ef5583 | -9.3485 | -46.4018 | 2026-09-20 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b4620d0b-0afd-30b6-9910-3fe0bd42e74d | -10.8364 | -50.9479 | 2026-09-20 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 173.3 |
| a46d3603-4c8c-3691-81a8-c54bbb2a7d65 | -6.2949 | -41.7785 | 2026-09-20 13:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 6d5061bd-d1e0-3146-a55d-b327a5e20520 | -14.1458 | -45.5638 | 2026-09-20 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 8c8f2109-10e4-3c41-b08a-7d334bbf42c0 | -9.5536 | -46.6031 | 2026-09-20 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 6674f295-646b-3d31-ab85-0ff33b274e0f | -7.211 | -44.0252 | 2026-09-20 13:10:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 734b4b22-2633-3d52-8f91-a03d811eaa35 | -10.3917 | -48.8915 | 2026-09-20 13:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c53f5177-52e0-34cc-83ae-7ad6f34a6a73 | -9.8313 | -48.4073 | 2026-09-20 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 8eeb940a-45da-3cf7-adac-0219b3306fbd | -13.5911 | -51.458 | 2026-09-20 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| cf899667-c952-3bfb-8d5d-c9a6ff3aa567 | -6.9414 | -42.907 | 2026-09-20 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.9 |
| e61b5148-eae7-3bda-b480-666351f49d65 | -11.0991 | -54.0285 | 2026-09-20 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.9 |
| 72a2e9ee-e8f8-3fe8-b912-7d2789ece013 | -3.6946 | -60.5835 | 2026-09-20 13:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 6de916e5-cd10-339d-8c4b-3cabeac68bd4 | -7.5522 | -45.435 | 2026-09-20 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 61b67206-698f-32c7-9a2f-73cf8dcdff1b | -12.1711 | -47.0356 | 2026-09-20 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d9c57286-97cf-34c5-8947-b98a4d289fa7 | -10.7902 | -46.3203 | 2026-09-20 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 11c02f8f-0c1e-3dba-8e33-951e84c65593 | -8.8827 | -45.935 | 2026-09-20 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9fef50dc-79d0-3db1-a961-d4ffbfd23e06 | -7.4288 | -44.718 | 2026-09-20 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 8b1f5de3-90dc-37ac-a8fd-eadf0e155653 | -3.7129 | -60.5832 | 2026-09-20 13:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f7329aa7-f35b-3d0a-a4cd-3fd47aab4292 | -6.4485 | -59.9909 | 2026-09-20 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| bff490e6-7f46-3431-8014-9ddc0a60e799 | -3.3367 | -57.8673 | 2026-09-20 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| ba069abb-3d35-3b63-bace-cb0f1d1041b2 | -11.0256 | -48.3164 | 2026-09-20 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| bc52bc68-f36a-3b5f-b902-5bc615517d7f | -11.379 | -51.42 | 2026-09-20 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 224.1 |
| 4718c63f-99c2-3688-8d8e-79969baf76de | -10.8553 | -50.9459 | 2026-09-20 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.7 |
| a9d24c84-342c-3897-aa1d-18d3b8bb2c9d | -9.0541 | -48.7686 | 2026-09-20 13:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9eddbe58-ef08-3cf2-bbe4-f0b6d612f6ff | -6.8945 | -43.7531 | 2026-09-20 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ef19753c-c6bf-3b06-acd3-3a448a516a02 | -9.2676 | -48.2472 | 2026-09-20 13:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 75b65c38-4d49-32c7-a646-34b9a5a3a6ad | -9.2603 | -45.939 | 2026-09-20 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 7480baa8-bb03-322b-85a4-ecb995494ffb | -8.8825 | -45.9576 | 2026-09-20 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| afe1377c-6dad-3799-8d42-141824874786 | -5.8408 | -53.5408 | 2026-09-20 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6f4d3c97-9aa9-333b-97a9-0d8aa10781dc | -10.8367 | -50.9266 | 2026-09-20 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 4f2c0136-b58b-311f-9e12-573386586ab0 | -5.8411 | -53.5002 | 2026-09-20 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4257305d-67c3-38fd-8011-17bb80b74709 | -14.6861 | -46.6657 | 2026-09-20 13:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 2bc8de12-5e91-379c-a8be-69615a5f0caf | -9.5539 | -46.5807 | 2026-09-20 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 4967f463-9dda-3869-bb31-f8cc9959e07c | -8.9269 | -49.9843 | 2026-09-20 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ff91ffa1-8f55-39d1-8973-0173f66a8b1b | -7.5334 | -45.4367 | 2026-09-20 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 9ebecbb3-0cd0-3863-a485-4b8195949aa4 | -3.6947 | -60.5645 | 2026-09-20 13:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| ece70519-0bec-3f46-86bc-9747a0a83ef6 | -9.3488 | -46.3793 | 2026-09-20 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 659b1440-04a0-3280-b431-052857720d37 | -6.4486 | -59.9717 | 2026-09-20 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 62afad29-1494-39d8-86c6-84798a0fd3f0 | -6.4671 | -59.9711 | 2026-09-20 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| dbda7a44-bd4c-3c39-baa7-58e7f01af02d | -7.3259 | -55.6153 | 2026-09-20 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| a835885b-7410-339b-a47d-c886406ab623 | -5.841 | -53.5205 | 2026-09-20 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| d49ee3da-6994-3ee9-8ed0-382263a0ded4 | -11.0802 | -54.0302 | 2026-09-20 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 6366ed1b-24b2-3f9f-bafe-d2f3309dc371 | -14.6661 | -46.6919 | 2026-09-20 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f5517f53-3b12-3057-b341-8b677167a123 | -6.9228 | -42.8852 | 2026-09-20 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 3ec581c5-580c-3ab4-92cc-310a6fb8b1d4 | -11.6609 | -43.4239 | 2026-09-20 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 1c8e86a2-8fe9-302f-b5ff-1cb323d1b18f | -8.8639 | -45.937 | 2026-09-20 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 14a3846f-dd41-350b-aee4-93f5c821a2d9 | -11.3793 | -51.3989 | 2026-09-20 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 511aa84f-5383-32e7-9d26-1729d5d26f8d | -10.2787 | -50.2605 | 2026-09-20 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 13867948-9eff-3b69-8200-ef6a753ebd49 | -6.9225 | -42.9088 | 2026-09-20 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.1 |
| 03406e74-3685-384e-8525-2766a6e02fc9 | -12.152 | -47.0383 | 2026-09-20 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 40fd7568-c378-39ca-99b2-d1643d3d7c64 | -9.8397 | -46.4361 | 2026-09-20 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 160.3 |
| f0dcd51d-b784-3897-a077-adde39052896 | -10.7708 | -46.3453 | 2026-09-20 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 1b80c9f5-ca57-3a71-8fba-d883b663faf6 | -3.3675 | -59.8666 | 2026-09-20 13:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 75b86175-aae6-3be5-a86a-1d8e32dc3b6f | -7.5711 | -45.4333 | 2026-09-20 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f194911b-fa27-3677-8bda-1960b0675499 | -12.7616 | -46.2029 | 2026-09-20 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 83d429c6-754a-3d9c-8966-e9b97e2ae729 | -11.8744 | -50.0199 | 2026-09-20 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 464accf5-807f-322e-be9c-6f84b92eaba3 | -12.7653 | -52.8661 | 2026-09-20 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b0876cb2-e9c4-388f-a9eb-9b0829846291 | -8.1376 | -46.8155 | 2026-09-20 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| be3e968f-4df4-32a6-bff9-86edb7be4175 | -7.5605 | -46.3785 | 2026-09-20 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| a63b07df-0d76-3c21-b0ec-be420e4aecf4 | -12.7621 | -46.18 | 2026-09-20 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 85271c6d-e105-3c40-b131-1b69d79b5c2f | -11.4537 | -45.3892 | 2026-09-20 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 94d463de-04f0-363a-9b57-4dfde72c8761 | -11.3787 | -51.4412 | 2026-09-20 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| b12be288-72c4-3141-bd46-80a683b21ef9 | -14.1263 | -45.5671 | 2026-09-20 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 13ee3892-c6ff-3ab9-9468-5a342268cfc4 | -11.8747 | -49.9983 | 2026-09-20 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| acac182a-5947-33c9-bdf2-7bd338b5a0f6 | -9.2865 | -48.2453 | 2026-09-20 13:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| ed18c121-c663-3af8-b506-c90a3e3d5656 | -9.8502 | -48.4053 | 2026-09-20 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 65b1d589-7633-3663-9794-f7dd83622838 | -11.04 | -54.96 | 2026-09-20 13:15:00 | MSG-03 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8942a4b4-5ec7-3c44-b4be-c458c5446870 | -12.77 | -46.24 | 2026-09-20 13:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 962df3c6-7d4a-3e24-a988-af30bb0f3d16 | -12.8 | -46.25 | 2026-09-20 13:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 758577f5-f6b4-3140-b2a2-04bfad0ec544 | -12.77 | -46.19 | 2026-09-20 13:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb20da45-4d6a-3b9e-8b80-2ae45d9b9105 | -6.93 | -43.74 | 2026-09-20 13:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 740caacc-8d69-30d0-80e4-4f9b9cbe8d0d | -11.04 | -54.9 | 2026-09-20 13:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3082b1f3-48b4-3594-9f0f-8086f10e0b86 | -6.93 | -43.7 | 2026-09-20 13:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 62f2d06c-e37a-30e8-b577-2bf5910b3433 | -9.2606 | -45.9164 | 2026-09-20 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 235.2 |
| a497fb7f-80ba-32d5-a2ca-4e44c1bbbf9b | -11.8744 | -50.0199 | 2026-09-20 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| dfdf42e2-e27e-3690-9a5d-2121e7668c3a | -13.2219 | -51.7595 | 2026-09-20 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 853c640b-e7e3-3798-88e1-3d0ccd4cb23f | -9.2603 | -45.939 | 2026-09-20 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 565.4 |
| 4f7deed3-d6c6-3147-9920-51c7bf79bd3d | -8.6357 | -47.608 | 2026-09-20 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 20c14251-a072-3345-a626-f9344fe94b94 | -11.1183 | -54.0062 | 2026-09-20 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| fdcb4c95-0a9c-3aa5-ae2c-e580a9dc8421 | -12.7616 | -46.2029 | 2026-09-20 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 07c769d2-3e8a-390a-a5a0-ce2b5f11fc73 | -11.4537 | -45.3892 | 2026-09-20 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |


[Clique aqui para ver as próximas entradas](README117.md)
