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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fe846c6-d2cb-3077-8fef-285855026d73 | -8.96109 | -60.50857 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 073c9a5c-cc1a-3fac-b0da-8c995026bd05 | -9.49077 | -51.61261 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2997a9f7-9e65-3907-997b-8217aa34eaca | -8.95502 | -60.51111 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58276c3d-aca4-3846-82f7-eb6bf01d9829 | -11.40719 | -46.33342 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8d1288a7-2821-3fed-897c-87b4b6017f08 | -8.61506 | -54.6728 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be936f3e-2736-3a96-992c-5f9fc8182263 | -12.0154 | -46.42475 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b843a5f5-2a68-3b81-b943-db45ecbb8642 | -10.48939 | -50.16032 | 2026-08-15 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d081f6d1-63ee-3ba6-8fee-497ee7726520 | -11.34509 | -46.22678 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25c274a4-0476-371a-9738-94d989eabfde | -9.97684 | -53.95086 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 121618b5-fbb6-3c22-895e-a42cc4ab7d41 | -12.01574 | -46.42202 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8bccca63-20f4-3f13-9f6e-64b86c00cde6 | -8.96819 | -60.50943 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5995e628-5f5a-3be8-b627-c99c120f533e | -9.35276 | -62.34433 | 2026-08-15 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81d26bb6-7038-37ba-af2f-c87745ac4a67 | -10.48987 | -50.15676 | 2026-08-15 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ebcb2cce-b786-31d6-9294-b182a0977fa5 | -8.60809 | -54.67116 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0124c29d-deaa-3000-a511-4d40ed2128a2 | -8.95854 | -60.51568 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41a7e37d-4a22-38e0-86be-5cd02f17b5f7 | -10.72327 | -50.55691 | 2026-08-15 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0c457745-df35-358f-ae51-15b1751cb030 | -9.49428 | -51.63918 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85c35102-e3ab-3f46-ba0c-a2b5f80d7fcb | -8.96042 | -60.51239 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 77070a93-d46e-3628-a449-1f6d7597fd6b | -11.42125 | -46.34401 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1a717808-6493-3a21-bff4-2b1fefeab842 | -8.65533 | -54.69688 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1ba8b14-1555-324e-82a2-702a86e91b45 | -8.89908 | -60.56147 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e539e152-7a88-3c13-ac3f-e1639c8125ef | -10.42032 | -47.97765 | 2026-08-15 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a3b7383c-29f2-30ed-ab11-ca0a21ad5919 | -9.98743 | -53.94884 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c890211-9660-3144-ae64-b1cd8b265b5f | -8.95975 | -60.51623 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d3831fa2-17a4-35e2-9171-dcaa28af2dbc | -11.42612 | -46.34811 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 41bbadc3-028a-3908-bd2d-77b7ab7aab71 | -8.96459 | -60.51311 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8065513c-4bf6-39f8-a39f-86c067c90780 | -11.40757 | -46.33047 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f588b2f3-1f3b-32bc-899d-6a9ff74dcc36 | -12.01608 | -46.41926 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c6342f8d-8c09-3471-ad4b-ad32839b37ac | -7.59142 | -60.87713 | 2026-08-15 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e74e32d3-ea19-30b2-941f-e76d96373d77 | -11.4201 | -46.35352 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 227cb841-4fc4-3c7e-8631-d750e37f7621 | -11.67626 | -46.75336 | 2026-08-15 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb92b2b9-33ed-3a82-8043-78b72bcf66df | -8.97309 | -60.53835 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ebf1074-99ca-32d2-8a72-ab4f324f6f1d | -9.98128 | -53.94421 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1d0248d7-eebf-35a9-b349-9987a784c1e9 | -10.16256 | -48.25813 | 2026-08-15 04:59:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12b8bd12-ddd8-3bba-8d33-ab31a539950b | -8.65094 | -54.7033 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2857df74-31f9-357a-b8a8-f8101fcb9349 | -11.35036 | -46.22787 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4b5e57e-3d80-3996-b00a-7cd145a050c2 | -10.41499 | -47.982 | 2026-08-15 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 663a1eae-7d86-3cd2-a44a-ab74d7b63352 | -11.41682 | -46.34214 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ca2e05c1-15d1-386e-9d9b-047fb46656d6 | -8.60754 | -54.67463 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5d55333-1aaa-38e3-a2d3-8c681f1169a5 | -8.89136 | -60.55616 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63334134-56cd-3d34-a3a8-7031e52e7998 | -8.60538 | -54.68852 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0d9c4ce-9627-3221-8f54-36774eef6b35 | -9.48224 | -51.61993 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b07d2b11-da62-3b99-ba94-0c144588ef79 | -8.97862 | -60.53132 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad97337b-972a-3d67-9c23-ca51742ec02a | -11.41121 | -46.34399 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9a25af89-50c7-3ae2-a9a0-dcb81de8de8b | -8.6504 | -54.70678 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03b9f35c-1bb3-39ff-a6a1-2b51b7dc8b29 | -8.607 | -54.6781 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0043f7bd-8454-3160-9106-c7ac096bd109 | -8.96272 | -60.5164 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 486db75a-e523-33f3-ba6b-1e6fd668cd49 | -7.59519 | -60.87817 | 2026-08-15 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b2a99f5-64f0-3599-9f55-a6bd4d1f9428 | -9.98183 | -53.94062 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad7e2dfe-6901-392f-b229-0a4aed0e47d1 | -11.43059 | -46.35549 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ab4de42-10eb-3f44-995a-ec9778dc4280 | -8.97376 | -60.53448 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55a015ef-e05f-32f8-a687-0c3b45dd4892 | -11.43077 | -43.92144 | 2026-08-15 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d9a236c-6263-3f81-a62b-b7e0d7f096c3 | -10.81127 | -50.32534 | 2026-08-15 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a363a6d-9603-3026-a1c6-ed3161fde650 | -11.42086 | -46.34723 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 76c12b6f-c15b-37a0-97bd-d7341d7bd570 | -11.41491 | -46.35202 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 5c08db28-8cba-3009-b2d6-c352a0aac008 | -8.25818 | -57.34498 | 2026-08-15 04:59:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c502afb-e59e-3c9d-978b-114b4ccb198b | -10.72254 | -50.562 | 2026-08-15 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 35dff61d-9673-327b-96ef-5829d900c412 | -8.96754 | -60.51327 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8eba9d3c-f149-3386-b6ca-72e4e1859f0e | -11.41527 | -46.34901 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| a2bcf6ac-810b-3777-995e-5ddff750a065 | -7.5958 | -60.87787 | 2026-08-15 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cc9ef6b-5960-3c79-8e06-e8cf49f5abfc | -8.26586 | -57.34212 | 2026-08-15 04:59:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f40f0801-6c50-37bd-8b81-dd31a86e9201 | -8.60869 | -54.68904 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74e876de-5d11-3f0f-9303-a3d172f5a28d | -9.98408 | -53.94832 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5fefbc28-e993-32e7-8207-f2eab921cce9 | -10.52961 | -44.85146 | 2026-08-15 04:59:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2afedf9a-9187-3453-827a-e6498c7d08e3 | -10.22192 | -48.47926 | 2026-08-15 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55f42266-c191-3431-a53d-30d057eaea0a | -11.42165 | -46.34074 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecce7bcd-e812-3806-b392-64a12c800584 | -10.61161 | -46.57033 | 2026-08-15 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fde33859-ce6b-3547-90a2-a4b19474ed0e | -11.40706 | -46.32807 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8456fdf2-2788-3fa4-b257-a8255130ff46 | -8.71509 | -54.59598 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0c15fa5-2f2a-3042-8181-0f57ef9dd6e0 | -8.95437 | -60.51497 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c960ab2e-708b-381f-9c4f-e3e5b5287b25 | -8.60863 | -54.66768 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 512d7a0f-105f-36e4-ab2b-8b8a8adc1c60 | -11.41044 | -46.34462 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b022441d-b7f0-353f-bc19-49c0c1a6fe7f | -12.02328 | -46.40482 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4457efff-0720-3633-b320-6752b9d53181 | -8.96594 | -60.50545 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34eedd6b-5e29-33f1-a697-a125981e54b5 | -8.96401 | -60.50873 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6f9b289c-5077-3a47-83a8-6d1173ec5f0c | -8.64541 | -54.69532 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2b2dcb3-a4a7-302f-a63b-368074dfe584 | -8.89555 | -60.55688 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 721a4e14-26be-326d-9123-6c159c02dec0 | -8.26458 | -57.35009 | 2026-08-15 04:59:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fbc3f80-83cb-3509-ac35-6973706d7c5f | -11.33456 | -46.22443 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 848a96db-eabd-3b60-bd8c-b50bef2c83ce | -10.40568 | -47.98067 | 2026-08-15 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 26abece3-a112-387b-ba74-0425968ee81b | -11.41562 | -46.35139 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 30cc77c5-d364-38b2-9059-2cce1859ad11 | -8.60478 | -54.67064 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a74d94b-2589-3633-8a32-7b63c2f142ff | -8.96527 | -60.50928 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2fc3a46c-8c4e-3a19-bddd-3ccc4228f6de | -8.61452 | -54.67627 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92e25be3-7f3e-3b55-8152-ff4ad71777aa | -12.02059 | -46.42626 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dbe32dc-05dd-38c5-82fa-9e5d8a514faa | -9.48286 | -51.61575 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60a68c29-241d-361e-afc5-4caf936b14cc | -9.98019 | -53.95137 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26c6f42c-00bc-3d9a-8e56-9a85a3bbe986 | -8.95176 | -60.53044 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b81dc2a-f91e-35d4-98a9-f88e6b8bea15 | -10.4939 | -50.15735 | 2026-08-15 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| da9d5b4a-6dd7-3e83-906e-ec0bf9fe9006 | -9.4786 | -51.61935 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa163494-8ff8-304f-9182-9a1ad2685f78 | -8.26522 | -57.3461 | 2026-08-15 04:59:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bc5b263-d419-37b9-8fc4-6ac09c31bcb9 | -9.97739 | -53.94727 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2e24b290-82fd-307b-a22f-dd99036b5523 | -8.96336 | -60.51257 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 288daecb-91c9-3106-9222-76eb50ec3e8c | -10.52913 | -44.85548 | 2026-08-15 04:59:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3e36d97-daf8-32ec-8692-060f47bec780 | -11.39711 | -46.32819 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a392bdf7-50cf-3ae6-a52b-ba4d959543f2 | -11.41679 | -46.33648 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 222b2d6e-c35b-35a6-a0fc-0d7411759e22 | -8.65263 | -54.71424 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d0a6e6-2367-33d5-a019-48732c88412a | -11.41006 | -46.34769 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 7d642172-3c5b-3810-8ce2-c89440722cbb | -12.01093 | -46.41738 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2cde194-8080-3dcf-bb3c-ffcf8ebfd4de | -12.02578 | -46.42784 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README29.md)
