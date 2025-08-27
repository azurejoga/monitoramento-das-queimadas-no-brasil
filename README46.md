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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f25cf52-1fdc-3526-ab33-01e4d78237e8 | -11.81327 | -46.80378 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc061302-c5b1-3aea-a116-311ce64769ae | -12.89636 | -44.64565 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ed63f6b-eddf-3a3a-880f-843a2899c8ee | -12.73642 | -48.08479 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c8ddc41-7b8a-3c76-9193-2c492287d853 | -12.8765 | -48.10051 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ef6fed66-468c-3b82-897a-6bb2d8bd9621 | -12.74692 | -48.08288 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a0c74f5-3078-30bf-b541-6c19373dabb8 | -19.08034 | -48.14687 | 2025-08-27 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfdb8a60-99b2-327f-a668-4f5f0477ab02 | -13.06974 | -46.32294 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cb0777ca-5f39-3956-922f-e10c78d4d82e | -13.58388 | -48.20222 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16049ce1-2a75-3482-8f97-79717faab68c | -13.60497 | -48.15485 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d84e2f3-3163-3bf4-a235-6ad8d67fa486 | -13.17545 | -45.28568 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb420aea-ebdd-394d-b96c-6cec18e3338c | -15.3579 | -52.7776 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f8bb239-f22c-361f-95cb-d44cbf9b8863 | -18.30311 | -47.67192 | 2025-08-27 04:27:00 | NOAA-20 | TRÊS RANCHOS | GOIÁS | Brasil | 5221304 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1da486b8-7d41-3e52-bfa2-d08994ff41c7 | -14.24253 | -48.03084 | 2025-08-27 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0aacf0a5-c73d-31aa-9a59-96a94ceed92d | -14.24637 | -48.04967 | 2025-08-27 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d93d7c2e-8c14-3d16-9eac-473d4286c952 | -13.62545 | -48.13284 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 903fac9c-3702-3918-91da-9518b4ab7db1 | -13.05397 | -46.30583 | 2025-08-27 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e8de75ba-995a-3e09-8015-8fe7e04c2523 | -12.19227 | -47.18327 | 2025-08-27 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20d64e3c-6f64-3f1d-ab35-7115bbe03ad7 | -14.29687 | -60.35832 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb2edd8b-3f48-3d6e-8be6-55a93125467e | -14.7647 | -47.92696 | 2025-08-27 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb14cfa5-a519-379d-b209-d6d67f6dd3c6 | -12.19282 | -47.17973 | 2025-08-27 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b1f93b6-74a9-31a4-925f-b48ed1256d85 | -15.79293 | -41.4682 | 2025-08-27 04:27:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6ab17e33-0b5b-34a8-8d68-d8f3cce967f1 | -12.75023 | -48.08343 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 349afa8e-5ca7-38f3-8215-340fd2a08f29 | -12.24775 | -45.06239 | 2025-08-27 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 415fdd17-023d-30b1-8d88-21d77f1b8cb7 | -9.41018 | -60.53579 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b311edcd-1f57-3a68-9a8f-5ff66a998043 | -12.79698 | -48.10909 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6b85df3-ef65-3b74-9097-ae8375a5d052 | -11.92562 | -46.71203 | 2025-08-27 04:27:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f9e940d-ac20-3846-8232-2d61756cda23 | -13.59707 | -48.22619 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0962f48f-ae32-3f10-b018-a4e1e00ce7f3 | -19.28282 | -43.73898 | 2025-08-27 04:27:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d589854-9287-3e43-afc6-ed5142eeb6be | -13.42999 | -47.01248 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dae60a0b-3f3d-37c6-b9bf-b14fbc610143 | -15.83068 | -48.14194 | 2025-08-27 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 60a1fde4-35dc-358a-ab40-6383ed4d5e0a | -12.75558 | -48.15673 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c222d87e-1ace-3044-a71a-094a07862c28 | -15.09873 | -48.56618 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dcabd7d-a999-3235-917b-b7c17525f855 | -14.30877 | -60.36414 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74147f8a-a79b-3c59-9536-c1388c945500 | -16.91908 | -49.44199 | 2025-08-27 04:27:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dad55062-989a-303c-8afb-c2c595e9d476 | -12.92989 | -46.31656 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9826e977-a142-3c01-a82a-7a1b07b4d89a | -12.74777 | -48.18453 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3eae9903-c5cb-317f-9a9a-3a3c407fcca3 | -11.82826 | -46.81706 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c2914f1-8dc3-3fe4-ac88-66dbba2092a0 | -19.12288 | -46.44337 | 2025-08-27 04:27:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1945e40f-df69-335d-a8ef-9b55dbf7b5f1 | -15.12688 | -48.66594 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27919b33-9eba-3f7f-945c-bd34aeca6d71 | -11.81605 | -46.80785 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ddb5bdf-7198-33a2-ad53-3cf7ff992b12 | -18.05738 | -45.17747 | 2025-08-27 04:27:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 509b4c48-8a55-3de1-8837-1c9d06df9d71 | -12.69359 | -47.34337 | 2025-08-27 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9c64b46-2eb1-33b0-bab0-c731846d582b | -9.64343 | -59.63265 | 2025-08-27 04:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c6b4c56-a4be-3715-889b-94eee3104502 | -13.83873 | -46.6936 | 2025-08-27 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6f92978-b0f2-311d-a54a-bfd434b62174 | -12.9524 | -46.32775 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 670da1cd-ecb8-3397-981d-76d66b7bd486 | -12.87263 | -48.10348 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a92225be-92e4-31b9-b31e-e9382126c375 | -16.13853 | -49.64061 | 2025-08-27 04:27:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfee1304-2111-394a-9bdc-78bf01d8d1f8 | -13.06357 | -46.33367 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 74806708-5951-3e43-8bd0-33a2ca512458 | -15.60157 | -52.71899 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a89a3f6b-ac68-38ec-bc25-f7981fe70711 | -10.59528 | -54.89779 | 2025-08-27 04:27:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f9d351e-aafa-3fda-acc4-f25758788d25 | -13.23466 | -46.54366 | 2025-08-27 04:27:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa75d31c-34bd-3b90-9466-f9723e20d24b | -11.92638 | -47.60202 | 2025-08-27 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef7553fe-130a-3b3f-833e-29ab3241e640 | -12.40084 | -46.51058 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7e5e2b7-849d-3b56-b660-0389a01ec5d1 | -13.61811 | -48.20058 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0fe14257-6387-37b8-ab2e-1b5bcd9d78da | -18.05675 | -45.18208 | 2025-08-27 04:27:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be9d9615-a955-3f2a-9524-9c2215b4f7a9 | -13.61867 | -48.19704 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41a00b39-88b9-3170-a123-716e455eb175 | -11.82936 | -46.80996 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cf2d736-9e66-3d7a-b6ef-38a719eef02f | -11.05712 | -52.02779 | 2025-08-27 04:27:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6facd1aa-9d25-38b2-8718-fccb35e9528a | -12.42201 | -46.48438 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e71e977a-490e-3c3f-82a5-af7c4bde7f65 | -9.4167 | -60.50314 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c95634c0-d787-3cc0-91bf-423ef5575840 | -18.14055 | -44.44677 | 2025-08-27 04:27:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36af67e4-b4c3-3ee2-b5d3-d4e2413610fa | -14.76419 | -59.738 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fc3f0538-fb82-33a9-bf32-9b2f2c81490b | -14.23856 | -53.31318 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3e199e3-18c6-3e0e-b57f-952ab1900ad5 | -20.06059 | -42.61513 | 2025-08-27 04:27:00 | NOAA-20 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ada82ee6-2a10-309b-a709-16cc1d6dba2a | -12.73945 | -48.19408 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56e71af4-1859-3fd3-9a6a-fe20a257741a | -13.43721 | -46.98773 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cd70f54-1256-35c3-89c9-24840e6f6e50 | -18.28832 | -41.00011 | 2025-08-27 04:27:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bbc4c37f-1ca3-34ff-ba54-63f849255295 | -12.42959 | -45.97121 | 2025-08-27 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e968852-7214-3071-b191-3a50a75f21f7 | -12.76878 | -48.18074 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c1c8076-c580-35db-b059-d0ad197b2a17 | -13.07139 | -46.31196 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee488e76-4685-3c0f-a8ce-2e86e48a1a6b | -13.44831 | -46.98222 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16f358a5-269c-3ae5-abd3-7dc8555859c8 | -19.90509 | -41.58221 | 2025-08-27 04:27:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6df247b4-b5b8-3500-9447-9b70dba8abfb | -13.44705 | -46.85631 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 39f23dbf-7a39-3bf3-9228-efbc90f0324d | -13.38976 | -46.92483 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 351435d8-57c1-398e-b108-adb12fabbe81 | -14.76083 | -47.92997 | 2025-08-27 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c59c1d97-42b9-341f-9a4d-f027bfbadb96 | -12.92935 | -46.32014 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99aaded9-5a8c-3879-9519-52ea9e7efef1 | -12.40194 | -46.50338 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e0b6e63-a6c5-357c-ac3e-3720fdf59ccd | -18.05429 | -45.1723 | 2025-08-27 04:27:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a115fed7-4383-3c02-b4d3-943b3753186b | -13.40923 | -46.93175 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a78586c2-0760-3c8b-a900-64f0b67fc638 | -12.75079 | -48.07992 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae0eaa4b-b2f1-344c-873e-041617a77109 | -13.04718 | -46.30494 | 2025-08-27 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd105bd8-e264-3707-ac7f-3bab760cba46 | -19.2468 | -42.05366 | 2025-08-27 04:27:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8bf44331-eed3-30b4-98a3-89b674c40daa | -12.49689 | -47.2316 | 2025-08-27 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7dfe130-a984-3fb6-884e-56575b0c759d | -12.69414 | -47.33984 | 2025-08-27 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a68a2bf8-03c0-3f66-a509-4deba5c09901 | -18.19712 | -45.56669 | 2025-08-27 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f4ccb4c-d9cd-3711-864f-c1d0380bd6a3 | -13.43312 | -46.85772 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1372c153-574a-3d85-a4d3-bed281f8ad6f | -9.40592 | -60.52127 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b066a118-8332-3e5e-8a3f-465955293caa | -11.81382 | -46.80022 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a2266a5-8524-38a2-b719-b011e7b93d20 | -11.74731 | -49.08389 | 2025-08-27 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2474f893-ff83-3a0d-94f7-01e5ca470660 | -17.36562 | -49.17658 | 2025-08-27 04:27:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22d3c26d-9af1-3b1f-b6c7-149e944191c0 | -13.61974 | -48.21173 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d62ce45-379c-3b2a-9cac-10041ca357a9 | -11.82768 | -46.79877 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c79e7744-3a69-3ef3-91a4-5490835458d5 | -11.31107 | -55.21519 | 2025-08-27 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 187ff0aa-f42b-308f-bc09-2ced0972baad | -12.39547 | -46.42118 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 146ac6bf-5c62-336f-9bd1-8089a6ef7080 | -18.05492 | -45.16771 | 2025-08-27 04:27:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab5ec03f-9ccb-3718-9fb8-b8afe0b37505 | -19.07699 | -48.14631 | 2025-08-27 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 266dce2c-6a8f-37f7-ad93-c5490b94fa61 | -11.51938 | -52.12533 | 2025-08-27 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f45ce983-6a5f-3515-9d64-e87fd7ee736b | -12.78321 | -48.15412 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 349af032-ae34-39b1-a2a5-8fd5d9b1b442 | -13.16784 | -45.28859 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6614b9a4-1277-33d8-8ebe-2340f90850bc | -12.87926 | -48.10456 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README47.md)
