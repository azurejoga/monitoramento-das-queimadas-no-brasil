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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c3ca886-7e83-3151-9d39-ffd186f01da6 | -13.41373 | -46.91962 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72a89725-2027-3484-a783-515f90616829 | -9.1988 | -59.50556 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bdc2847-9681-34b3-a3cc-905364de06ea | -8.84629 | -62.44927 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.3 |
| bcc23c46-5abd-3cc1-9faf-de7499560653 | -8.34007 | -62.93185 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7181935-982e-326c-a9e7-27ba4658eede | -11.05032 | -52.0239 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c16dc2e-c093-3731-8d80-ca149a1a18e6 | -13.4465 | -46.99311 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1af0ca68-3f37-3ff4-b770-ae094d53ca5a | -12.94224 | -46.32859 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82cb521f-84cc-36dd-9530-d030fab2fae2 | -12.74597 | -48.16107 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 14254b09-c97e-389f-ba5b-d5a164b954e4 | -10.60884 | -54.8947 | 2025-08-26 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 182cc63b-3d2f-31ff-95cf-f0af3e329d2e | -6.83378 | -59.35803 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 881bea9c-5c12-3f0f-af55-98be8cb8023f | -9.17289 | -59.45688 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e821b3b3-11a6-3682-be12-f2a807b51aa2 | -12.67604 | -47.86773 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 205c340f-e693-3edb-8438-8ee557f19f8e | -11.54924 | -52.11126 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf7ddafa-539b-3538-9076-29257f307f5c | -7.38846 | -64.34858 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d6651b18-c8bf-3ca0-a708-04df23042e2c | -11.54814 | -52.13987 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a830efb-74a6-3f45-9e17-a111ed424a69 | -9.03983 | -65.7318 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28001285-5384-3333-a2e9-8cd209f41c7c | -13.09213 | -57.20343 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4441a7e-4708-3c5a-9dd7-3cdc35560a32 | -13.4632 | -46.87243 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6889ef6-13cc-32da-8048-a03d42f7b458 | -11.39783 | -47.60317 | 2025-08-26 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 420e3050-e579-3675-8e89-cb3268d42122 | -11.55641 | -52.10882 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d257b11d-572d-36a7-858b-4a7aaf61470b | -13.05634 | -46.31161 | 2025-08-26 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1528a102-c971-3313-8151-8e08ac09f7ac | -9.30844 | -48.26729 | 2025-08-26 04:46:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c1c6b3d-b515-3a8c-9a0d-20e07da1bb63 | -9.16188 | -59.52488 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3e1a178-41b0-3d77-8858-45f8d29f97ef | -15.03024 | -48.66992 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ccbac63-53de-3d37-8b5f-fc3b7a0ab279 | -13.36855 | -51.78489 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8744241e-54e1-3944-9d23-8a200fe05027 | -8.8854 | -62.45712 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 945d5311-8ff2-3254-9c29-9784b25f9748 | -13.01036 | -56.89292 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 288813a6-70b6-3dbf-bc8a-a6446bdfcb2f | -9.23341 | -60.91508 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 548b7f25-ee68-3bb6-83e3-847ed5fc11f0 | -9.25477 | -56.9043 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 196cf9da-7e48-3822-a354-bb59b20113a4 | -14.2514 | -48.03587 | 2025-08-26 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c4a2704-0890-3925-9866-e05469e3c7fe | -11.15257 | -44.76718 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3c729eb7-b782-3145-ba12-3432e41ce1f7 | -9.23542 | -60.92673 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ef92d98-ce4f-392b-b985-cf5ce3c2c1d0 | -10.24876 | -59.66434 | 2025-08-26 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7070cf71-ef13-392d-aceb-51c6b5a2cb6c | -11.30216 | -55.10571 | 2025-08-26 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2c70bc21-c1d7-39b2-a59e-13a33eaa7c37 | -13.40956 | -46.91875 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1dc145ec-f591-3c36-bbe6-38f803608f18 | -12.77786 | -48.11295 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 200090b9-3696-3087-8dce-9a01ab1c5794 | -10.6997 | -55.14836 | 2025-08-26 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bca907fb-ec33-3916-a19c-549ff6b8af09 | -7.43491 | -60.62366 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf5dc2fe-c14d-3806-92d0-145b9c56b542 | -13.51263 | -46.88963 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6d5421c-c8aa-36d6-b97d-2dd7ca16c4c3 | -12.41142 | -46.50184 | 2025-08-26 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08d89157-0f73-3c15-9f5f-e0e553c3fea5 | -7.29313 | -59.66939 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b3d24d6-7510-3e3e-862c-c34db247ad68 | -10.75331 | -47.00528 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63f4ce06-be5e-351e-b8a7-77931eccc826 | -14.30872 | -53.06811 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8efc785-6ee2-3d96-9715-9c7350ac2d11 | -14.26077 | -48.02673 | 2025-08-26 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f5858fd-e13f-3c72-9534-3e8fbcf7661e | -11.56524 | -52.09584 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3df57eb1-3243-38d4-89d6-b8b54567cf0c | -14.34685 | -51.95557 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cad61ce-3f47-3616-bc9c-ccba0ba1d629 | -14.28207 | -60.36519 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b689f329-48e6-3cfb-a313-96d380e06023 | -20.05085 | -44.46881 | 2025-08-26 04:49:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7ba5b90a-aa3c-34a8-a34a-f750cf1d9d5d | -16.24377 | -58.72498 | 2025-08-26 04:49:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8efb1fdb-de9b-3bd9-baf0-3a609fe1e72f | -15.65116 | -52.73349 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56e48b93-70e8-38c9-a131-7393ab2e0176 | -15.62873 | -52.72602 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5905973-51f1-3bfb-932b-b452583c1043 | -21.42968 | -45.47829 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 70783959-db99-3666-aa32-e1728ab5a682 | -14.68427 | -59.64211 | 2025-08-26 04:49:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18be28a9-6fe8-3c0c-9168-cd43795fd49f | -17.37309 | -48.08688 | 2025-08-26 04:49:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9ba92a1-aaae-37ae-acef-580ca605535e | -15.64452 | -52.7324 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e99cc0f-70db-3fc1-b0ab-eee71a03d4b9 | -19.12532 | -46.45329 | 2025-08-26 04:49:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d8badce-ce55-354b-b2f7-c13cf3446700 | -14.31044 | -60.36847 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06e62097-2594-3afe-9bd2-6745d1f6a6e0 | -17.20846 | -47.22318 | 2025-08-26 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df0162a5-4647-3e9f-8e88-fc1f7db8f0c6 | -18.13982 | -44.4274 | 2025-08-26 04:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1479413a-e99d-3fed-8a2b-dfa59665a20e | -16.41271 | -49.64529 | 2025-08-26 04:49:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94c2bef7-d9ad-3987-865a-562535ebda80 | -15.61937 | -52.69867 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45f41d67-3257-36fe-8f08-7cebbe05b19f | -19.17963 | -48.73331 | 2025-08-26 04:49:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5eaa5348-ffec-3ace-a4ed-3ddc27149920 | -19.9192 | -44.61956 | 2025-08-26 04:49:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 89559e77-cf33-345b-ae50-7ca20c7a6eb0 | -19.94123 | -47.03724 | 2025-08-26 04:49:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c87532a-3f6b-3db4-9760-8f66f12246ed | -20.20394 | -47.01416 | 2025-08-26 04:49:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 521b9998-aa03-397d-a167-e0c2fef5b9a0 | -16.7399 | -47.60235 | 2025-08-26 04:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5067a740-8c8d-31a7-bb29-89d17a726623 | -18.81144 | -47.59569 | 2025-08-26 04:49:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 370d1488-1a84-353e-a081-7fab37a8cded | -21.12325 | -45.87599 | 2025-08-26 04:49:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 529fce10-75f2-3f1b-a102-b85bc7bfa221 | -20.88254 | -49.03194 | 2025-08-26 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 48aad8cc-1ee8-37b6-9cb6-ce30d969ef00 | -19.92649 | -44.62363 | 2025-08-26 04:49:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ef0af8c3-099f-3379-971a-e9e4e655eb1b | -17.20902 | -47.2187 | 2025-08-26 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17c95df6-bbde-389e-a850-a51b2ff25937 | -17.72384 | -50.73236 | 2025-08-26 04:49:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d713c776-4746-3bb3-a0ed-187f3a0b5dec | -16.23837 | -58.73162 | 2025-08-26 04:49:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 3609cef7-5509-3492-bcb0-f5b1f91dc23b | -18.84263 | -47.00409 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a6c550b-ff84-3baf-abdd-d45e8470d021 | -21.19756 | -48.92404 | 2025-08-26 04:49:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 1637ec39-c177-364e-b9e1-3603be8d0f6e | -20.88662 | -49.03246 | 2025-08-26 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d0fdd6fd-c629-36f0-96c6-67e6d3aed585 | -19.17854 | -44.5142 | 2025-08-26 04:49:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c526d0af-2965-3b15-beb8-e05528d082a5 | -15.62213 | -52.70282 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52247320-8522-3e5c-b060-d20ab198dac7 | -18.23784 | -51.27113 | 2025-08-26 04:49:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c5ef11e-5652-34ef-9050-4cfa8076c0a1 | -15.63813 | -52.73125 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ab2440d-4c43-3fcf-9409-609b59b19139 | -15.90766 | -52.30466 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98bb50f7-1aff-3a4f-a1fc-05b7d4bb030c | -16.6664 | -49.35077 | 2025-08-26 04:49:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 551c75a5-41d1-32cc-8ce9-d05962c9f47e | -21.43115 | -45.47828 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3fdbbb36-2bee-3a73-abea-3ef1f908f320 | -17.78344 | -44.48512 | 2025-08-26 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b76771f5-9f36-3c4b-9f68-f568cb59377c | -14.30569 | -60.36807 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c16d3592-d2ba-3057-b9ed-bb4a551f5ce4 | -14.75632 | -59.72233 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0faf9167-f689-3ec0-9f23-7f2ef6ec7532 | -19.91885 | -44.62307 | 2025-08-26 04:49:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9ddf82bf-bab3-3938-82d5-a72e8d2b6ba9 | -21.60947 | -49.70173 | 2025-08-26 04:49:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5b964d68-c3f1-3cf8-acf5-21f43ee8aa4d | -15.61881 | -52.70227 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e70438ac-e79a-3236-be2e-7a5c33a436b4 | -14.76392 | -59.70594 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e024e812-4c45-39a6-820a-6081e1b3e91c | -18.85221 | -47.00072 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e5dfa8f-de10-3542-9f9c-1176888fafc0 | -19.92455 | -44.6203 | 2025-08-26 04:49:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0418eb20-979c-31b7-a4cf-1c216f565ab3 | -15.63205 | -52.72657 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69a44e02-35e2-3a9f-a4b7-c20a7d18dc72 | -21.38631 | -45.49298 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 58a2b76d-d74e-3bd7-b220-1b5bee255f00 | -19.03411 | -46.91443 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d41782ae-1519-3f72-8026-e36d7609ccc3 | -15.62817 | -52.72961 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 46e5fa2d-b308-38b0-b197-b22dd06e3262 | -19.17818 | -44.51755 | 2025-08-26 04:49:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7c74a2f-8858-3ea4-b56a-b2216719425f | -18.84212 | -47.00847 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e33aaa6f-b495-30eb-969b-8643de2fda2a | -14.29627 | -60.36676 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65e2f7c1-4ddb-373d-a487-cb3ec23d1b1f | -14.30955 | -60.37323 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README73.md)
