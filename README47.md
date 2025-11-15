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
| 49c195f4-686d-3f46-a526-389ff0e3491c | -11.66555 | -48.46516 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8593a92-330e-3e66-a370-d5a2baf37437 | -11.96629 | -44.32127 | 2025-11-15 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d6774cc-4f05-3440-b64a-850424561f19 | -11.92057 | -46.20955 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 24934b41-9b17-358a-a76e-b9f03939e39e | -11.75396 | -45.33808 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dedfb637-e813-3d0a-816c-c8b67929ef2d | -12.67627 | -46.77364 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| a2624ee2-b2cb-3a42-85bd-cafedabb52e1 | -11.84377 | -49.2101 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| d1ce339f-4f6d-32b7-b2cd-d221b1b0585e | -12.67127 | -46.76182 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 012dc707-cec9-303a-9d07-decc8465aca2 | -14.27746 | -46.2647 | 2025-11-15 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b7a2c1f-3108-3762-a8ef-5c335bd5c288 | -10.70513 | -44.518 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41a3d45e-6dec-358f-8516-7402c5aed92c | -12.54741 | -47.81516 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 799f915a-5d91-3f42-96e7-a2c2ca1cdf9f | -9.69899 | -48.86975 | 2025-11-15 04:27:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15bcc945-a623-35cb-a22e-8aaa0189b5a1 | -12.84805 | -46.43138 | 2025-11-15 04:27:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c5463fe5-9f62-358a-bf94-63dc57ee0ca6 | -10.53051 | -47.93264 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52515601-59db-3ba8-b923-3a995fcf7583 | -10.4265 | -44.95425 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdb32512-9db4-34a4-9789-4f3ca4456eda | -16.87842 | -42.1342 | 2025-11-15 04:27:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c0a90c1-8dd4-32bc-bd48-cca027c5a401 | -12.90513 | -45.10128 | 2025-11-15 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b84a315-25aa-323b-9bfd-e93c85485ce3 | -12.489 | -47.30081 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b64d0363-64af-3ada-a31d-36c66d021e0b | -13.48382 | -47.41026 | 2025-11-15 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71b1e0fe-90e8-3f9d-ab9a-f7f929abc0ae | -16.33286 | -43.94903 | 2025-11-15 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cba882ff-aee5-3625-a8bf-de1b19d61eff | -12.68805 | -49.11574 | 2025-11-15 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d499a19f-970f-3619-85a3-a319201aa0f9 | -12.48955 | -47.29728 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 389a218c-f24f-319c-afb4-ecf9fae152ad | -12.67738 | -46.76648 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dea8b4e0-77c3-3943-bc2a-8efc507af9dc | -17.29248 | -46.82917 | 2025-11-15 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9847ec07-1c1c-30eb-847e-46b78ed00193 | -14.6869 | -46.61797 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81db39df-bdab-3f5d-a93a-f1368661f938 | -12.69759 | -44.47864 | 2025-11-15 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f61536db-b054-32d9-a65a-93c7463a3ef8 | -10.44931 | -45.08315 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe107fb8-c3c4-3abe-8d35-80654e1e4f71 | -10.66665 | -49.3672 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09fd2372-4158-3b72-8bee-bf6764d7940e | -10.04561 | -47.73481 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d35df56-38e2-3a02-a331-b31bb975596e | -11.17267 | -48.14675 | 2025-11-15 04:27:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75fa5eca-0f33-35d9-92ce-8eeaac0b25cf | -14.65559 | -46.56488 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 999951bb-9209-3e10-b5d9-220092622551 | -9.81229 | -48.84264 | 2025-11-15 04:27:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b0d1729-7da8-3f1d-aba2-56a3145a1ae9 | -10.36567 | -49.88709 | 2025-11-15 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e1363b8-ed37-3a43-a3c7-d33f24375bd4 | -17.58325 | -46.68535 | 2025-11-15 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4916da26-46e4-30da-89a9-f112ad6af27a | -12.41746 | -48.1187 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eea0e44f-5f12-34f5-ba02-3652c6f6dbc2 | -11.17449 | -47.45133 | 2025-11-15 04:27:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3f30bac-1617-3bb4-84c2-5f3055af4880 | -13.17891 | -43.05544 | 2025-11-15 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 12cbe51e-a0d8-37e7-8001-be0f9e5def89 | -15.46341 | -43.1491 | 2025-11-15 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1ce95f6d-e5e8-3ffa-8945-7b8d8b22f32d | -12.76013 | -43.65136 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ef7f9d2-cb25-324f-b9f0-2875ab1d0563 | -12.47752 | -43.73592 | 2025-11-15 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ab7bcb83-1dce-34cf-83e5-12b16857832e | -11.3933 | -49.19693 | 2025-11-15 04:27:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0329fea-d5c3-3665-ad3d-ca06b77db289 | -16.44851 | -45.01247 | 2025-11-15 04:27:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40b454eb-3159-3c2d-b058-932263c1cab4 | -14.66123 | -46.57338 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6041a10f-05ab-38b0-9229-07b873981fbe | -10.38508 | -47.28738 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9435cb0-04d1-36fb-8aca-89560ef3c95c | -9.826 | -49.77247 | 2025-11-15 04:27:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5213fcf-1eb2-3db4-bf98-550f55824fe6 | -12.3849 | -48.10974 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fba70da7-eb32-3318-a72d-344c1f1ff869 | -12.90454 | -45.1053 | 2025-11-15 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86950241-ab35-3bb0-88a4-5c14c14b3ac0 | -10.62773 | -45.01158 | 2025-11-15 04:27:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a6037ce-6450-3b14-a26a-909bcc152e36 | -11.7985 | -48.07903 | 2025-11-15 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c7625030-2d55-3f74-a211-053011104ffd | -11.7402 | -45.33574 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ece344e-0476-3458-9cf7-90cbd6658eef | -12.60047 | -48.33432 | 2025-11-15 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a7b3fcb-151f-3a51-ad69-15f97eaf38cf | -15.45544 | -39.24073 | 2025-11-15 04:27:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 15ad1ebf-1b24-3fcb-b1a1-099e4ac93478 | -10.10387 | -47.51788 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f923387-5bfe-39b4-b1b1-760efe28ce04 | -11.75053 | -45.33748 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 59c4b2d5-79df-3ccb-9fc4-93fd290a8d9d | -10.77319 | -43.98232 | 2025-11-15 04:27:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f001cea5-13e3-3675-a91c-6a1658c7cae6 | -16.53099 | -43.56863 | 2025-11-15 04:27:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3c071fd-aabd-3faf-b674-7a5ef1206a1e | -11.00879 | -44.63772 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c9a41437-e558-3441-b443-9359c924c963 | -16.56499 | -47.61328 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4afcb5f6-a42e-30cb-892e-0b68f7257f4e | -14.04417 | -44.06879 | 2025-11-15 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4895b392-5739-340a-85af-7f629feb034e | -11.85274 | -49.21923 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e4fc3fc-d01b-395a-9c2a-546e3aa0b4ed | -13.89291 | -42.89695 | 2025-11-15 04:27:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6066ff2d-da08-3f75-a062-665215ed95f7 | -16.45218 | -45.01304 | 2025-11-15 04:27:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3acc4bee-b56d-3277-8a3b-9ece72781a60 | -10.35697 | -48.73156 | 2025-11-15 04:27:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 12c89c32-9945-3c63-874f-5f433c268a65 | -11.71349 | -48.8756 | 2025-11-15 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70feb5d4-175b-310d-aded-50a3ba7070d9 | -12.43725 | -48.14376 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2ef1df7-fa27-3d94-9d2e-edfaa29072b7 | -11.79235 | -47.41151 | 2025-11-15 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3860a947-63db-3ae3-b1e8-68be2604b97a | -10.6975 | -44.49636 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 426297fc-4950-3428-9416-076c6ef43599 | -12.40478 | -48.11296 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1407172-5b9f-3f74-bdf5-7c56dd2c7834 | -13.54876 | -43.72449 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 665e3532-c9ab-338e-910c-d9eda192e66c | -11.80569 | -48.07658 | 2025-11-15 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19f413bc-99c4-3de9-9495-7a14540e4ef9 | -11.71744 | -48.87257 | 2025-11-15 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a67ab2c-c2e5-3c26-b041-9c6cb3ffbd55 | -10.53107 | -47.92911 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b2aa5b4-13dd-3bfd-a48b-ea87b5b2b7ab | -15.34245 | -47.8586 | 2025-11-15 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc3b6e41-015a-3fd3-93df-cec2047a7296 | -11.41215 | -48.49659 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85550606-d5c2-357b-8bcf-b7b7812a5ba8 | -12.83743 | -46.43334 | 2025-11-15 04:27:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c0e7ca5-39f9-3ecb-8d61-9a147dfe2df6 | -11.62985 | -47.68687 | 2025-11-15 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a6210f8-35b2-3b67-b90d-36c379bf4803 | -10.33783 | -49.6393 | 2025-11-15 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 071acd7f-494c-3212-863d-37e435d7ff6e | -12.66884 | -49.1275 | 2025-11-15 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3649e668-763e-33ec-a8d1-9f07f12d393c | -14.71923 | -44.23783 | 2025-11-15 04:27:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 344b095e-cc68-3d5f-ade1-619db100ac90 | -14.98504 | -42.41269 | 2025-11-15 04:27:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ee5e5a0e-67fe-3b43-83be-35b19d9e0cde | -11.92815 | -44.62684 | 2025-11-15 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e451ff2a-b0c2-3d96-993a-54c3c65bbc93 | -12.80946 | -46.45872 | 2025-11-15 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d134e25b-ec05-343b-9fc9-857b1eb59563 | -10.94318 | -47.62523 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70b7d6c5-8eeb-39b1-a1e2-c32b250921fe | -12.75947 | -43.65607 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eda34313-ded9-3c30-bb2a-767fe7a92778 | -12.3921 | -48.10726 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91d21be5-41fe-31d4-974c-582fb10d2b3e | -12.9223 | -43.09156 | 2025-11-15 04:27:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8b0cbba7-f8f9-377c-ad47-92b72918f854 | -9.7192 | -48.89607 | 2025-11-15 04:27:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0778ba9b-fd94-37a4-aa74-4f42547f64a7 | -10.6257 | -44.58847 | 2025-11-15 04:27:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c2bec3a-8e93-377c-a147-3d3ade274481 | -12.43782 | -48.14019 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f26f2c06-719b-3f03-9d89-0b9bb37da346 | -12.45984 | -43.75217 | 2025-11-15 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61da718d-13d7-331f-827c-c041356f0689 | -10.77537 | -45.00951 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 951b3287-f648-3ef6-842c-7f4d02d1e531 | -14.69027 | -46.61856 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dc1715b-e06d-3810-a94d-c9ed5959674f | -15.09371 | -43.24861 | 2025-11-15 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3bcbd404-19cb-3ce9-a87e-625427b29bb0 | -11.81208 | -45.28032 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f005f8dc-28cb-34b5-a170-23f4c17fdd0a | -10.21303 | -47.89948 | 2025-11-15 04:27:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1b3a69e-86ca-38cc-b6cc-08998e45e01f | -12.84134 | -46.43026 | 2025-11-15 04:27:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b39793d7-7404-395b-892c-aa57f4e6b061 | -11.16935 | -48.1462 | 2025-11-15 04:27:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 000a414b-caff-359f-b22b-9bf764df1387 | -13.89241 | -42.90053 | 2025-11-15 04:27:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 49f1f894-4463-3c27-b690-75bd438dd1a9 | -9.82248 | -49.77186 | 2025-11-15 04:27:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68f72edd-6983-37b0-a3be-d61810b70f23 | -10.36919 | -49.88768 | 2025-11-15 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97c65aff-2d00-330d-b54d-4278608bae63 | -12.41802 | -48.11517 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README48.md)
