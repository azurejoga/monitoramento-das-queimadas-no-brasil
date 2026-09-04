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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 829436af-1bb0-3d7c-8567-e78647eeb80a | -7.56918 | -67.39924 | 2026-09-04 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 802c0fe8-80c6-3308-beec-bbe6fda9cf14 | -8.68817 | -62.91905 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28981958-198a-3279-81a9-63a6a719f608 | -6.67512 | -58.76614 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c02fb35f-f4ba-3532-b2b1-fbd4793d7428 | -7.4406 | -64.61578 | 2026-09-04 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15ba6e72-7a9b-3176-80a5-1705a091978d | -3.16012 | -61.11678 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce69e526-a9fe-3659-a1e4-b7127df28dc6 | -6.81278 | -59.96286 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fab8a4d-2ff3-3c5e-a1c2-5efabc159e43 | -8.11858 | -54.7878 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 918da8e0-d5d8-3a5d-8bea-73198d30837f | -1.47309 | -54.26378 | 2026-09-04 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b71dcec4-cda6-3acc-b20c-b9df289282b9 | -7.24685 | -59.52567 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a300ce47-5321-3545-9d71-07e15c232631 | -10.31737 | -50.34217 | 2026-09-04 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2958f9ec-5028-3886-94a2-ebbd2cabaf92 | -8.50507 | -54.65949 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e1209dee-7e59-3a87-9016-4e8a3e1951b8 | -3.53436 | -58.98199 | 2026-09-04 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfa54004-05a3-3ab9-a151-56d0508637eb | -8.43283 | -54.69562 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28b4374e-e345-3162-9bb1-1d0e9f986074 | -6.8161 | -59.96338 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05afbd85-d019-3cca-a1f6-9a0dd32ced99 | -6.7085 | -62.86819 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0ec37d6-fbc2-354b-9d68-93ee0733fb3c | -6.6972 | -59.98455 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ccd4a5c-e032-339e-8610-bf75ba7cf304 | -8.81005 | -62.34909 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5def5388-e5b2-3f02-afc9-4d5a47b512b8 | -8.43665 | -54.70057 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc45a2e2-6841-363d-9b25-9ab5e47fc6ea | -10.50531 | -51.33238 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 78dda05a-07d3-3c18-bea5-bb2561e211cb | -10.49999 | -51.32846 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83a8f1db-14e6-3718-9638-17f6a194a064 | -7.09053 | -56.52306 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e91319bc-13d0-3ee5-b540-0a99d2b14858 | -3.079 | -61.17972 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2404d40-49ae-384c-849c-d395c24a67d5 | -7.74439 | -67.06731 | 2026-09-04 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4560789-1e85-3254-b37d-ef7de95e3cae | -7.574 | -61.29885 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66ad6e52-4acb-37a6-9be3-2efe665631af | -3.10359 | -57.90729 | 2026-09-04 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d26318b1-16d1-3202-845c-e46ff551c0fe | -6.67738 | -59.938 | 2026-09-04 05:23:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb2b04a5-dc18-38e8-8501-b9271d983f2f | -6.37695 | -58.28449 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1b06df4-4a42-39e9-b403-e5e0ebc1e0bf | -2.76018 | -49.47709 | 2026-09-04 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 964068e5-76ba-3202-9fc2-a8a16f358250 | -8.07887 | -55.33133 | 2026-09-04 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2d256f0-f0ae-37ee-b5a1-5aea4c3166cc | -5.92384 | -60.19434 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 136c334d-6249-326f-a71b-31ee73f3df43 | -6.68519 | -59.95352 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5243d9b-91ea-3895-8693-1b787fa74efe | -3.7746 | -47.55271 | 2026-09-04 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5de18d60-e440-32a6-9aca-748a19e7e69b | -3.01767 | -61.48136 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b53c5cb-48b5-3c1e-8daf-b7cd18446753 | -6.67297 | -59.94449 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ab43c03e-7901-30a6-94ee-3c6fd06b18a8 | -7.01208 | -62.98943 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfe0d1e4-d4d5-3e9b-8be5-ed5a51db9679 | -7.55592 | -61.34933 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| fb2281a8-3783-3e65-95b9-8499aedf210b | -8.92858 | -62.35332 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf6d8140-f866-39ed-b17c-60a7a2d6be84 | -6.56665 | -58.97355 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b425da66-4df9-30dd-a4d1-1800caaafe41 | -6.14976 | -59.9421 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dde9936e-9fa1-3023-b9de-6011e8245798 | -8.6932 | -62.93118 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae545af-31de-3d75-bc52-bc02748053e3 | -6.12158 | -59.94846 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80aa3779-c7c3-3887-81a3-4cd48871155f | -4.12212 | -51.03051 | 2026-09-04 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2a9da73-550f-3b0f-924d-18171657320a | -7.28305 | -61.11757 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02adf244-a705-30bc-8a11-4d5bf8e77035 | -7.55977 | -61.34637 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3ef98d8-819b-3c60-9b5d-934a62b9bb18 | -6.52791 | -59.93649 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56fcd822-3ba3-35c2-809b-d9898e4e4a23 | -8.56005 | -63.19228 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42724dfa-56d1-361d-8201-3e7eb5fd2044 | -3.07845 | -61.18326 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 215a8df6-86cb-3db4-abf9-52fb10e92f32 | -3.29366 | -57.88208 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9973cf96-c6c4-3601-b6c3-446558366238 | -6.56963 | -58.56242 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac6e1c18-a6ca-3093-81ce-0c6497c50898 | -6.6797 | -59.96701 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1ae24641-4865-3639-ac01-76fabfd18e9e | -8.52466 | -67.15865 | 2026-09-04 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd244802-f8a6-3fa5-a51d-c36c6133a4ae | -8.11218 | -54.7727 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2006216-bc54-35db-99bb-0fffdc048f21 | -6.5351 | -59.93404 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d5d32f6-4d74-37ff-b4ef-6485159f07c2 | -1.62191 | -55.16662 | 2026-09-04 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| def06c11-50cb-306b-88e5-44cd60a838cd | -6.91249 | -62.93148 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8e4ba36-1440-3cb3-81d4-cba3c8019e2d | -4.11675 | -51.02985 | 2026-09-04 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0429bdf3-795a-39d4-9142-086ce2623efd | -8.16692 | -62.77515 | 2026-09-04 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c88b7f6f-d92c-3c6f-ba39-310565ef3334 | -7.9834 | -61.16129 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37de09c8-f2b9-3125-b791-1fc83c332392 | -2.94769 | -51.28844 | 2026-09-04 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aec2402-d0f0-3203-bdb3-273bb2e82d9e | -7.03115 | -62.98081 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d72a7c3-39c8-3c94-8d4d-5c2a9463db2c | -3.90249 | -52.04355 | 2026-09-04 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 900dd974-598f-30f5-bbbb-9165208b2341 | -7.08284 | -56.52184 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc1dfce6-ab5b-31b1-bb31-fbd883c92e6d | -3.1228 | -57.69526 | 2026-09-04 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd6dcdf9-f5fb-3e13-b907-a82502635bf3 | -3.02553 | -61.49737 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73e55b15-3a6a-30d6-8643-0465aa98c72a | -7.8636 | -63.75589 | 2026-09-04 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8ee4be8-ccf6-3248-be34-8c68b27e9a1a | -7.53981 | -61.3006 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5ad9485-9787-36aa-967a-433762c264a2 | -6.68253 | -58.76348 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe83e03-3814-3941-9f04-a2de0b14fcf9 | -10.50075 | -51.33488 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4e47b0a2-2b6a-362e-a7c7-7af48c278ee2 | -6.68023 | -58.75547 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cb3f0e0-74f7-338e-8ef0-60c901f6a42e | -2.76088 | -49.47428 | 2026-09-04 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cb76476-35ac-32f6-9b50-ba60ddb9416c | -8.26066 | -62.76059 | 2026-09-04 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36e2d24b-c969-3f46-94a4-5a633db4b8b3 | -3.07784 | -61.07816 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fadb5d42-0545-3b70-8c77-548b993ddf64 | -0.93065 | -47.19574 | 2026-09-04 05:23:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9392d65-14b1-302d-aef7-99eff88e2d0c | -6.11664 | -59.95839 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a1f30ac-43c7-32c2-b305-140b3d995ba0 | -6.68125 | -59.93502 | 2026-09-04 05:23:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dc2f6fa-af3f-3439-886f-3d80bc2829ea | -8.11604 | -54.7744 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b642673-f324-388e-89ed-c2a2e8bd9e34 | -6.68364 | -59.98549 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e480a381-db2f-378c-8bae-712f20253171 | -8.17031 | -62.7757 | 2026-09-04 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7438d4cf-94a0-3cac-bad0-84ed29aa10ba | -3.36863 | -59.50134 | 2026-09-04 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a1cea0d-0e89-3b55-b2cd-421a9c991b94 | -7.55453 | -61.22828 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e02cb9e-8c50-37cc-b7f5-6413aa75ea5e | -6.68078 | -59.96 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3ed0ea69-86ce-32fc-9099-b3f83401ff61 | -6.68418 | -59.982 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 69c4e7e6-c04d-38ba-ac94-625974d39589 | -6.74708 | -59.44183 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68d336d0-2718-34f9-b48b-b5b3e2f594c5 | -8.48792 | -54.65237 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb9e5698-ef71-315f-af45-ab391ce4d034 | -7.61615 | -57.61423 | 2026-09-04 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef3d3568-7167-3beb-b507-85b8d9accb1c | -7.67341 | -62.54335 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c791bf76-107e-395e-8442-ca3295ba155e | -3.4459 | -57.80035 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7456d5a-c09c-3ce0-b8b1-ac64adbafbd4 | -8.20133 | -62.79944 | 2026-09-04 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c05b6eae-98b5-374c-af8e-e60fd8a47308 | -4.11374 | -51.02697 | 2026-09-04 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afa0f47f-1939-3ed0-87bd-313d4da6f9d7 | -7.00925 | -62.98508 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f35b9cf-8400-3b4e-a54a-b7c79cb14561 | -3.098 | -61.18992 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0419fd60-d77b-3e5c-870b-7b67d02bf3aa | -2.95284 | -51.28929 | 2026-09-04 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54138b77-e1f9-3ce4-8c2a-9d9c9700c9d6 | -7.0277 | -62.98027 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7625a73e-20a1-3d28-99f1-b3746155a0b3 | -6.6814 | -59.978 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9320122c-decd-39e7-ad4a-9c91b3c4eefa | -8.68373 | -62.81679 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf91282f-f0b3-3895-9440-7102fa23eebc | -8.43407 | -54.6869 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af3afc9a-7f93-387e-be41-51b88346ea1b | -6.67908 | -59.94901 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b28e114-32d4-31b1-8e29-22bcc3f9f900 | -3.12626 | -57.69579 | 2026-09-04 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6c64cbf-5501-3221-8b1b-38cfcc512f5f | -7.01736 | -62.97861 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e0f335c-0889-3352-a1f8-ddcd2ce38587 | -8.42537 | -54.71648 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
