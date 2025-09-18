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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86d7aaa9-42a8-3031-bdd0-5a27e7850e45 | -7.4109 | -50.0019 | 2025-09-18 00:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0ba99980-723b-3b23-ac4c-f8e8db996706 | -6.1253 | -47.8137 | 2025-09-18 00:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| cf5bfc19-3951-34e7-9461-8323ca0cdec6 | -6.558 | -43.597 | 2025-09-18 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| e2e08abd-8261-3962-80d4-aa74be0ceff3 | -5.0756 | -43.8265 | 2025-09-18 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 1b195a3b-fc58-39c3-8101-d438c009339c | -5.0942 | -43.8483 | 2025-09-18 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 3b652fb8-ed68-3dee-82d1-54c6870924ee | -5.8245 | -45.9129 | 2025-09-18 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 7329ccb8-6fed-3daa-bc42-3a6ab862f7e0 | -7.8199 | -48.3809 | 2025-09-18 00:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 8875d90b-08ff-38cf-8c69-60605e90c0aa | -9.4159 | -57.039 | 2025-09-18 00:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f399f14c-147e-3b33-bcae-5e3a9e54b95b | -6.6806 | -46.3184 | 2025-09-18 00:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 244483a8-43bf-342f-a97f-6910f086b712 | -7.2765 | -44.8921 | 2025-09-18 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 086e5b7b-69e2-302b-ba29-fd0c12d17d7c | -5.1131 | -43.824 | 2025-09-18 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 61971fb7-5342-3bcf-9eb4-90f67b02626c | -4.6973 | -41.951 | 2025-09-18 00:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| d926e70b-29ed-3336-9f00-0af13bd38fad | -22.3457 | -46.7406 | 2025-09-18 00:00:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| bff703dd-e15f-30a4-a693-cc87b5f14dda | -5.56 | -46.2879 | 2025-09-18 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 39c408cc-b260-3824-87a3-e8d918a2f47e | -19.5869 | -57.7765 | 2025-09-18 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 1b43cfa7-b628-368e-93fa-ab5319f6b760 | -5.0944 | -43.8252 | 2025-09-18 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 468.6 |
| 995f8025-cdf5-3b27-8247-1e578b661781 | -6.6808 | -46.2961 | 2025-09-18 00:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| c495bac9-3e73-3dd4-bc4e-4b5f4abceed9 | -12.9068 | -44.658 | 2025-09-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 9b047972-5ea2-3902-9be1-f85e92eb7621 | -7.2763 | -44.9149 | 2025-09-18 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 825072b4-e652-3c7f-b3cb-f0dae0022c51 | -6.144 | -47.8124 | 2025-09-18 00:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c7a1e08c-e14a-3c1f-9119-931b9473bb42 | -7.801 | -48.4042 | 2025-09-18 00:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 3dc40ae1-9f8c-3aba-bddc-0fa5d326f77a | -7.8012 | -48.3825 | 2025-09-18 00:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| a960caf1-0ca3-3237-bfb5-35e7be937f67 | -11.3871 | -50.8465 | 2025-09-18 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| d2149fa6-d72c-3ff7-b78e-5e422023d008 | -4.6971 | -41.9748 | 2025-09-18 00:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 139.7 |
| 16b92814-001e-33d5-828c-34669743a29d | -6.6993 | -46.3169 | 2025-09-18 00:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 249edf02-4cee-3e64-92f7-f69d2c0ae3f3 | -19.5865 | -57.7973 | 2025-09-18 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 78deddc9-8d49-3482-ae9d-e03f39bf320b | -5.8058 | -45.9142 | 2025-09-18 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7620225a-9d87-3968-becc-0d4d4596fb02 | -6.6995 | -46.2946 | 2025-09-18 00:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 704b9116-1633-34a0-953f-7475fe243a96 | -3.5161 | -49.4528 | 2025-09-18 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a101493d-097a-342e-9531-27aec1f99a73 | -7.1617 | -50.738 | 2025-09-18 00:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 862c9242-f69d-3bc5-b798-f3bc86bae6c5 | -5.0944 | -43.8252 | 2025-09-18 00:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 425.8 |
| 58e6c585-6d83-338c-b11a-ac17aef507a6 | -3.5161 | -49.4528 | 2025-09-18 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| d64935bc-95e8-3dbd-9422-6a67b4b4092d | -15.0511 | -55.2624 | 2025-09-18 00:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ef01888c-ca5a-38e6-9929-8e51489ff0d4 | -7.4109 | -50.0019 | 2025-09-18 00:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9423b6e3-fb87-3df7-b83b-ced61e048dff | -6.6806 | -46.3184 | 2025-09-18 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 98543558-8ba1-3183-ba70-9662b11a720d | -8.9725 | -46.2854 | 2025-09-18 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| cc991862-dc19-3214-8d14-fb95f9ddecd5 | -5.0942 | -43.8483 | 2025-09-18 00:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 90959623-93a7-3ab6-8583-0923801ba88b | -6.6993 | -46.3169 | 2025-09-18 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| ea83c2d9-fd98-30e6-b5f7-00d2c4d42244 | -7.8012 | -48.3825 | 2025-09-18 00:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 3e78d969-5600-3317-8b03-02b38802e884 | -9.0292 | -46.2794 | 2025-09-18 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b5dfe486-95d5-3000-a8b2-7bac2ccb52c4 | -12.4056 | -51.4113 | 2025-09-18 00:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| ef6451af-0198-3ba0-ae3b-373aec5cdadf | -11.3871 | -50.8465 | 2025-09-18 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 9bcf7458-bf06-33be-abdf-db8eaf56d4b9 | -19.5869 | -57.7765 | 2025-09-18 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 6cbf77b0-41f4-3597-8f39-49fe76afad74 | -6.6995 | -46.2946 | 2025-09-18 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| b54311e9-4e8e-3445-aa78-a788b25698ef | -5.1131 | -43.824 | 2025-09-18 00:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 949ea837-dce2-3d9f-9fbd-04dc1e66cc67 | -5.8058 | -45.9142 | 2025-09-18 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 0784f10f-bfe0-3467-b5da-202a71dd32dd | -6.4964 | -46.0201 | 2025-09-18 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 5a10347a-a9e0-3c9d-aeab-82daf990beca | -9.01 | -46.3039 | 2025-09-18 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| eb67d5c5-6fa7-3bf3-8cb6-685f9974cbfe | -19.5865 | -57.7973 | 2025-09-18 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.8 |
| b67030ee-a700-3c3e-bb7a-b9088e8e6c37 | -6.144 | -47.8124 | 2025-09-18 00:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 44d8b327-c8d7-3c33-98bc-e57b02067a83 | -5.8245 | -45.9129 | 2025-09-18 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| adbe68b9-198d-3e41-a1fb-7d023952a035 | -6.4966 | -45.9977 | 2025-09-18 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 38002a8c-41b4-3b54-b229-bce8ff530297 | -6.6808 | -46.2961 | 2025-09-18 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 1844885e-fe95-3e81-9a6b-8851b27824b5 | -15.0318 | -55.2646 | 2025-09-18 00:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ab8fc216-a37d-39c1-8ed1-65407841ec92 | -19.5668 | -57.7792 | 2025-09-18 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| 5f380c15-f08e-350a-9c78-23644e546cad | -6.558 | -43.597 | 2025-09-18 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| e1326d2f-b9d0-32e0-ab09-dbbfbb3ff8ab | -5.0945 | -43.8021 | 2025-09-18 00:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| bdbabb37-33d1-3955-a372-9b86bdb45417 | -7.2763 | -44.9149 | 2025-09-18 00:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c0d8c8ab-f8a0-3741-8a2a-19c7d8f798f8 | -5.0756 | -43.8265 | 2025-09-18 00:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a1376f08-98b0-3bdb-9258-eb86b2157c7f | -7.8199 | -48.3809 | 2025-09-18 00:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 92f13215-1b55-37e4-8dcf-ea983fd56467 | -22.3457 | -46.7406 | 2025-09-18 00:10:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| 37ad0292-c461-3d49-bf53-1eefaf7bb52d | -19.054 | -48.25 | 2025-09-18 00:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 167.3 |
| fc1c8c52-8584-38b9-8dde-f37bb4b8a33c | -6.1253 | -47.8137 | 2025-09-18 00:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 6dc587fe-c2f3-3324-a269-27e0b5a96fe3 | -19.0534 | -48.273 | 2025-09-18 00:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b09be6e5-f593-382b-b7eb-c5bc966607dd | -4.6971 | -41.9748 | 2025-09-18 00:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 124.2 |
| db3c89e5-c812-3612-be53-7cf0591f8655 | -9.0289 | -46.3019 | 2025-09-18 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| fb3f6595-95ae-3d68-9089-63eb61ae362f | -6.558 | -43.597 | 2025-09-18 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4f8a26de-1f69-32a2-b90f-c5b95a8b928e | -19.5869 | -57.7765 | 2025-09-18 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 4d57d1dc-534a-3b31-a98b-1722cb0940d5 | -7.8012 | -48.3825 | 2025-09-18 00:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c95b38ff-92b5-3f18-ad7b-12f72a8ffb35 | -6.6806 | -46.3184 | 2025-09-18 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ea1aa0cc-2be5-3e03-a729-7972140594dd | -19.5668 | -57.7792 | 2025-09-18 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.4 |
| a9e54e35-36ea-337e-8305-d7c89668e61e | -5.0944 | -43.8252 | 2025-09-18 00:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 175.5 |
| a1df8bb3-715e-3f45-bd4d-0288f276a883 | -4.6971 | -41.9748 | 2025-09-18 00:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| bf02c12a-9028-397d-a2c5-014302ba44f3 | -5.0942 | -43.8483 | 2025-09-18 00:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 0d144747-6253-36bb-b74b-b3c6ec4df421 | -6.6808 | -46.2961 | 2025-09-18 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3a5bfde7-3aac-391b-85ed-becd3bd2d9a1 | -6.6995 | -46.2946 | 2025-09-18 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 614a01e0-3e23-3dd7-a582-97337a56f4a9 | -9.0826 | -59.0212 | 2025-09-18 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 0fef0600-f748-3155-96d7-914693c1f3cf | -13.0747 | -42.1261 | 2025-09-18 00:20:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 809f9e28-694f-3928-b48a-3e6d0849b6bf | -6.1253 | -47.8137 | 2025-09-18 00:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2febfb64-43eb-36cd-920b-63a89da00a1d | -6.6993 | -46.3169 | 2025-09-18 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 98f4eb02-80c1-36eb-adb4-1c67f0703a19 | -12.9068 | -44.658 | 2025-09-18 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| f44763a3-594f-30ee-ab8d-86173ab18f90 | -19.5664 | -57.8 | 2025-09-18 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.1 |
| baed5561-7151-3644-9ab1-eafd793be07b | -7.2765 | -44.8921 | 2025-09-18 00:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e7c72784-e1a0-3fe9-9f1f-34862591b47e | -18.9873 | -46.9702 | 2025-09-18 00:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6290a892-9ae4-343a-8703-166eb9f432bb | -5.8058 | -45.9142 | 2025-09-18 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 58712713-a708-30e0-a905-c7d53560e5fc | -13.0942 | -42.1225 | 2025-09-18 00:20:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 61.0 |
| c5efdb18-1dbb-3c84-aeec-f96d2824d9ea | -5.8245 | -45.9129 | 2025-09-18 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 26997642-731e-340d-b28a-97d7b02f91cc | -6.144 | -47.8124 | 2025-09-18 00:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d133dbd6-d315-3090-88c2-f74c167e2d56 | -19.054 | -48.25 | 2025-09-18 00:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 21492e5a-47e9-3937-a7c7-116f3bcf4ba3 | -19.5865 | -57.7973 | 2025-09-18 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 7bee6ba3-a827-3ac2-8927-f7ac8b3e2558 | -22.3457 | -46.7406 | 2025-09-18 00:20:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.6 |
| f25c4d1e-bc0c-37c2-b7f5-981fb1aabffc | -6.6806 | -46.3184 | 2025-09-18 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ba21895e-0514-308c-bb39-f165defa8155 | -6.6993 | -46.3169 | 2025-09-18 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d2a7e877-d935-3163-bf28-25080d82c36a | -19.5668 | -57.7792 | 2025-09-18 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.1 |
| 37fbc1a9-7933-3cd9-94ca-998dc91c599a | -6.6808 | -46.2961 | 2025-09-18 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 37f8d0fe-329e-3a6a-b239-05117f79e7e1 | -19.5869 | -57.7765 | 2025-09-18 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.3 |
| e82c4196-33b0-33e7-97a4-e20f446c51a1 | -6.6995 | -46.2946 | 2025-09-18 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| e2f1a2da-bacc-31b0-9ed6-d41fa9f9ce43 | -6.1253 | -47.8137 | 2025-09-18 00:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b9fb0e70-c4da-3e2e-bcce-138844103da0 | -19.5664 | -57.8 | 2025-09-18 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.1 |
| 64336fae-9940-30c6-8022-245ec619a454 | -5.8058 | -45.9142 | 2025-09-18 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |


[Clique aqui para ver as próximas entradas](README2.md)
