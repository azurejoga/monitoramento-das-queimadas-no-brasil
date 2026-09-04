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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84c0fa25-1abb-31b8-9d8c-73eb6a38f292 | -8.27141 | -62.75856 | 2026-09-04 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dad0c5b-ae31-3349-9be8-3911c89c77b8 | -3.1925 | -61.19421 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a07bb2cf-5e3f-3a62-948c-94022cd00db2 | -6.68187 | -59.95301 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c837ba2-2e99-3457-969d-16e2e2e9d1bd | -7.09124 | -56.51831 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc284b8d-2d02-3c50-9158-aa76ecb7f713 | -1.81244 | -53.97726 | 2026-09-04 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5622c74-a82a-38d0-8c71-e36b5acb80cd | -7.98117 | -61.15384 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf256d46-1486-3cdd-86d9-91eba95d2791 | -6.68132 | -59.95651 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d698e04e-8072-3c15-bc1c-5b335fa78a1e | -8.11599 | -54.77753 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f4dd12d-baa0-30ce-b6e7-c0da7abe48e3 | -7.58988 | -57.68587 | 2026-09-04 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20f49eb9-c58f-3030-bb9c-568dea267a7d | -7.73347 | -61.64853 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2d10f63-4f3f-38ef-92b5-4ecccde2b619 | -1.74548 | -54.98986 | 2026-09-04 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88ea6a00-93e0-3eac-af71-bf1dcbda189c | -7.27831 | -60.64539 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3c1fbc0-cc7f-3f2a-97dd-923f072d965d | -6.64134 | -59.44417 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 933f3a7b-5948-37e0-9893-4febecee905d | -8.69378 | -62.92749 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd6787aa-2552-37a0-9994-b67b77e241a4 | -8.11045 | -54.78541 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c687844a-500a-320d-a256-afbbda0a3c75 | -6.6947 | -59.98005 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 06e97ead-dce4-3a92-85a5-5485a90c3889 | -9.16249 | -58.31339 | 2026-09-04 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5306e262-cfdf-3d0b-8d71-66d7f7ddcf5d | -8.50185 | -54.64998 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fe9603d0-84ff-31f7-8acc-10efd7d5912b | -7.56086 | -61.33948 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 330f2b5d-993d-361e-acfa-d923584f9202 | -6.67692 | -59.963 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4d6f55d2-5a24-3e2e-8a06-415854fa2b4b | -8.68478 | -62.9185 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ece2e93b-c39a-3a8f-8b9e-622d71f4b09b | -8.49114 | -54.66192 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04c87654-1777-31c6-b333-34ef6b0edd58 | -3.29711 | -57.88261 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35f79f6f-fb90-393c-a644-4154131e672e | -3.32378 | -59.4626 | 2026-09-04 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eac46b24-985e-3643-9a24-bdf6b291ac58 | -6.68689 | -59.96453 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 567e9220-1650-3884-b9d9-9ac130f64f22 | -6.74989 | -59.44593 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c60006e-7475-3702-8f19-5a1020991820 | -6.79045 | -58.95396 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f51aac95-1220-353b-aa49-f90c2d53e46b | -3.02048 | -61.48549 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb1fd8bc-9e62-3f29-9af9-2e3b7a3003a5 | -6.98509 | -62.98574 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e41a33a-e9df-37ab-910c-295f72ab96b7 | -6.70567 | -62.86388 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6efb62da-7df2-368e-88b2-23b9ec96c40d | -2.40985 | -57.90279 | 2026-09-04 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a5cd0ce-4844-3919-89e1-67f7e89366c2 | -10.65008 | -50.38438 | 2026-09-04 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59b6f408-6ffd-3046-837c-9a8445a4002b | 2.23123 | -60.70517 | 2026-09-04 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10469af5-00b8-3d86-86a7-4b92832fb7ca | -8.50309 | -54.64104 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38fbbb8d-bd45-3369-9177-eb87c00eae0b | -10.50573 | -51.32911 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| aa423aad-5023-33aa-b1ef-ee02faed19da | -2.70237 | -60.95825 | 2026-09-04 05:23:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7319515-cc89-30c4-8389-dd2972dace0d | -7.79284 | -62.34726 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e6e5589-6362-3ecd-b16d-29f4e566b4fe | -8.78444 | -62.55418 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7987ee92-5eb6-3d81-87d1-3e9e923620c4 | -8.43912 | -54.68314 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f66f5182-5e5a-38ab-a505-ede687f6e29c | -9.47301 | -60.38667 | 2026-09-04 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8c4b1b7-8b29-33be-a870-81f29c7bde2a | -3.16235 | -61.12435 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02023362-1062-3094-b2c6-b038b0b2eef2 | -10.49874 | -51.33827 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1acdd831-e372-3971-ae03-47e367a9b163 | -6.678 | -59.95599 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35c594b6-fed2-3200-aaa6-aa3f3bbf864c | -8.62263 | -54.84725 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a470cd74-f58e-357b-b6b2-b4ff11fd72ae | -8.11424 | -54.79039 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6d46e992-5626-3394-b83d-b8a70a78d2c5 | -6.52405 | -59.93948 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea622e59-0f50-384b-9519-33d7289e76ad | -6.67351 | -59.94099 | 2026-09-04 05:23:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6d20709-6103-3b6e-ba5b-23b138686988 | -3.1467 | -61.17987 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abe7936e-5b0b-3df1-81ab-783a467ce99a | -8.83676 | -62.30582 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e26d4ec8-07be-32db-914f-1787aa1dcbd2 | -7.57283 | -57.70053 | 2026-09-04 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e03c6ee-013d-3919-b530-67433c6a59e5 | -3.8967 | -52.04856 | 2026-09-04 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 059b31b3-ab5d-3388-8d3d-ca2b42a0b89a | -7.32926 | -59.58571 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 417c9c35-3f35-332b-b38e-f17db414c574 | -3.17016 | -61.14003 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f128134-534a-3918-a122-62732b33a9cf | -8.44196 | -54.69094 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b777824-26c7-3c52-8f2d-edec23d87d68 | -6.44386 | -58.15818 | 2026-09-04 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 409f600f-eeda-33cf-b93b-a95f9bd2ce0f | -7.55646 | -61.34586 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| da1605d1-612d-3dac-aad5-111ce0bf107a | -3.3681 | -59.50479 | 2026-09-04 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32f63119-f2e2-368f-ac4c-198226b5a3ec | -6.68975 | -59.99 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 613cfb97-cf44-36eb-85bc-1c085acf69d0 | -6.68642 | -59.9895 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0569548-b8dc-34f4-9157-112e80be7476 | -8.49175 | -54.65747 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9240891b-bb1b-3db2-b876-3ebf21c7c90f | -8.92242 | -62.37057 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 444e8127-7876-34c7-94da-9bd507e14292 | -7.51484 | -60.78517 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a90c853c-4826-3d58-9fb5-3457330344a8 | -6.15308 | -59.94262 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 86f4fd94-ee4b-3f53-925f-c2cd07a88289 | -6.78704 | -58.95345 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54fcaae0-c5c6-35f5-9577-ecbca517e195 | -3.24708 | -47.25034 | 2026-09-04 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eb6de41c-76f8-36b5-929a-ebb9875f36d8 | -6.69069 | -59.94004 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f2db47c-86e7-3f29-983f-f50ca6b8268d | -8.91464 | -62.35473 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f54e3de7-b5c2-337f-98b2-ef9008a6cb1b | -6.68071 | -59.93851 | 2026-09-04 05:23:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6356a08-4660-3b98-b989-5525b8b6e868 | -8.1192 | -54.78351 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5c011712-0ae3-3727-a89c-d30ff8e937a9 | -7.0202 | -62.98295 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeb90a50-9a1f-3a37-95b0-a4a8dbadb747 | -3.36917 | -59.49788 | 2026-09-04 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5423ecb-0cf5-38b8-b4da-d829a17d5d9c | -3.17071 | -61.13651 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e6480ae-bb66-3d19-b2c2-4a9c6a8d312b | 2.23155 | -60.70549 | 2026-09-04 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 189a8e1b-f99d-3b2f-8328-208c3b6dc0b5 | -8.11165 | -54.77379 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f35ca886-18ec-38a7-81d1-b390575cfe65 | -6.64525 | -59.44112 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c82e05c-3b67-30a8-a2fa-4cb497b24a0c | -8.11482 | -54.78286 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7100b920-6923-3b87-8afc-1564ef0cedea | -6.70628 | -62.86012 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5779888-5a0b-31ef-85ae-6a3e52265304 | -10.50041 | -51.32514 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86b3fb34-b1f8-3903-824f-1abf1b177bd2 | -7.34682 | -49.53213 | 2026-09-04 05:23:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 644a5828-8146-3686-8248-99c5be29881e | -7.09194 | -56.51356 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb9042d3-c975-31b4-a638-fa282968ed32 | -6.68581 | -59.97152 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7d07f196-1a51-357d-8fa5-04e5af7c0f31 | -8.41653 | -54.71521 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4d665c9-48bc-3e35-b69d-a985171bf6fa | -6.77626 | -58.95555 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 229b5120-a359-38ab-b672-b3f1ebdd650a | -4.36578 | -47.77514 | 2026-09-04 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e4052614-0ac1-341a-98ff-63c9dd3464f7 | -6.68349 | -59.94252 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee86c807-cf59-3b98-848a-3c9835c7648d | -6.15694 | -59.93964 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c95279bf-57cb-3297-97fe-30296d3c4fd1 | -6.67413 | -59.95899 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d0102d84-4942-3677-9d66-1fe3e17b4451 | -8.11483 | -54.78608 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 60b162be-96ef-32ed-9d2a-a9ba93f34c74 | -7.03176 | -62.97704 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbb19b5f-d676-33f5-81dd-e38857ca542e | -6.99829 | -62.98721 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c47e2df9-c025-366a-b554-1fa5269f0b50 | -3.02386 | -61.48602 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2001a1b-1502-3324-a782-f630f37f6fbf | -7.55197 | -61.30962 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84780522-e06a-3597-b3f3-35bc87d1a0bd | -8.90739 | -62.35722 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d673edcc-18ab-3b97-8ba4-2fcded1ec548 | -10.64399 | -50.38355 | 2026-09-04 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee3f242b-d226-3e97-a6f9-926d85979679 | -6.99484 | -62.98667 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 142bda6a-58ca-3075-bc2d-2bbffcf51db6 | -6.67684 | -59.9415 | 2026-09-04 05:23:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f953d173-25a6-3920-a376-3bdf2e52a48c | -8.11979 | -54.78244 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 251ce362-75e1-3f01-aaea-96c2da247f16 | -3.25941 | -60.65952 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0705cc5a-4667-3b54-a415-be4f6b0574b0 | -8.11044 | -54.78222 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a3129835-4136-387c-a773-ff9af4367469 | -3.17127 | -61.13297 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README26.md)
