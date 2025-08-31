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
| 8bce1564-8903-3349-a997-0a4ca54dd2fb | -11.81712 | -46.44267 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8724fb44-a25c-3b20-b811-4a6d1dffcafc | -13.33197 | -46.8609 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eccab0a6-7cb7-3743-aa4f-ebd7f7b3cbdf | -14.80618 | -46.72852 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 49222c96-f643-336a-aca9-b03375cc7025 | -11.81903 | -46.43179 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d8b19f2-4e68-34e3-8d91-45155c045f39 | -11.80348 | -46.47317 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df3487b6-ed83-3e38-9ec9-9aa3e6994ce3 | -13.30942 | -46.88844 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de1a6d33-e2f0-32ed-8e86-e4f158ee540a | -17.15932 | -46.08003 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 410390e3-1073-3a1b-8989-08297ce696a8 | -13.3443 | -46.97756 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49ce920e-2f70-3195-96b2-8da4a1f169a7 | -11.83652 | -46.78368 | 2025-08-31 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ab695d7-5006-3f2c-92c3-5dcb9733cd85 | -11.83236 | -46.42647 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5bb51f9f-440c-324f-be0e-ab416a20ddf4 | -11.89982 | -46.38137 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fb32e54-7a69-3cb6-bbd9-b96c5217d99b | -13.51181 | -46.97666 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77dc1ecc-4a55-38fe-9e15-4e4b03192593 | -14.81062 | -46.74883 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fc704e15-c03d-34ee-88cd-63fd923bcb31 | -12.83489 | -48.08417 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b70a4c56-2e97-301a-a8ce-56e44400b1eb | -13.36932 | -46.95442 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd7efd35-c3d1-39f5-abc8-d5e969be39a5 | -13.31493 | -46.90453 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc81af7c-48a1-3a61-b0e5-c1e6e9b13857 | -12.83048 | -48.08345 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cfe5aa1a-7161-3bf2-ae1e-644a91eefc4f | -13.52516 | -46.97575 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eafafb74-46ce-360d-8b02-1636c7d4b8f7 | -11.91195 | -46.40595 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 869c4540-e3e9-336d-8502-a501fa67421f | -17.96616 | -42.9817 | 2025-08-31 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 158d26b7-b28e-3263-bdf1-7412753ae96a | -18.06817 | -45.94608 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9708377d-b888-34e7-981a-79bfd620fc18 | -15.23242 | -56.07564 | 2025-08-31 04:04:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c26e142-b5bf-319b-8610-423196c909ef | -11.8165 | -46.44625 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cc4de22c-ee0e-37ab-a502-529d6e891ac8 | -10.95297 | -50.84736 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4cb9d1b3-7f90-3b6c-a93a-924951e047cb | -11.82834 | -46.42584 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3efc2975-123d-3a84-8ec1-f71fd4293722 | -14.81738 | -46.75612 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fb3b8c1-183e-373d-b51a-ca0cbe869379 | -13.49562 | -46.83315 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2735b15e-ef7f-36b3-b4e8-417da52096e3 | -11.81989 | -46.45053 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5829db1a-965e-39c0-b1dd-034d1e98b2db | -13.34408 | -46.8628 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f90a3033-fa1f-33c6-a58c-a38715dbf550 | -13.35293 | -46.95269 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 916e276c-6921-3614-8bcd-7c78a94d820b | -11.82593 | -46.51094 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aba25119-fa87-3c39-bdc3-5608344696b0 | -18.56714 | -45.37089 | 2025-08-31 04:04:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b2113d7-38ab-3d73-9ac4-377373200f12 | -14.8135 | -46.75528 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cba09f0-4409-343a-b0c0-87be5e23386e | -10.95841 | -50.8484 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8a56592b-ace0-3c3f-b31f-a8027a23f35b | -11.81588 | -46.44975 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e2e6ec9e-910d-39b8-864b-d871abde1aae | -16.22274 | -52.68927 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| bfb498c6-4fda-3ffb-8046-10ab55a7f1c5 | -18.11774 | -45.01213 | 2025-08-31 04:04:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03c92c55-4541-30f3-8f71-ff4acce1b82d | -11.90948 | -46.70474 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aca4fb5d-6216-35bb-a3ca-5a30dacfba70 | -12.41097 | -46.46737 | 2025-08-31 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b93d6e64-618c-3995-b850-228dc2b48c76 | -16.97809 | -49.31438 | 2025-08-31 04:04:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b84ae5de-5e8a-37f1-98a0-d212561833ef | -11.86061 | -46.45437 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5eeeb96-bf04-3888-8fc7-bc7c9f2e67eb | -13.39945 | -46.94916 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cd744de-015e-38f1-853e-a7a941ea7a41 | -13.39777 | -46.84068 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61838644-39cc-32dc-b16b-6bf6395f4942 | -13.6886 | -46.88099 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e4711a9-ec19-369e-a495-954328038e1f | -14.55472 | -51.98059 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5cc2551-357b-3499-a901-eb6ba0e3214e | -11.82303 | -46.43256 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89ff2fcd-0573-3a3e-b9b4-72057ceb658a | -13.48822 | -46.96863 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e58d2569-6558-38cb-893f-68028943ca6a | -15.67416 | -43.22913 | 2025-08-31 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2af40043-6dd1-3df5-8c86-73550d329d38 | -11.89614 | -46.42529 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b25d2f78-02fa-32fa-9370-96068cd5313a | -11.82934 | -46.51527 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3d1be293-1d12-3c88-b24b-87be6758aa95 | -13.49294 | -46.9655 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56670137-4e0f-3050-8f5b-a38227ae18e3 | -19.21634 | -43.74319 | 2025-08-31 04:04:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9be3064-0a07-3f74-b441-0f93104e775f | -12.31712 | -45.71883 | 2025-08-31 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d26e748-badd-37ab-b7bb-bd467495bdfe | -13.35605 | -46.86551 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ca80f58-da9c-3dfe-8543-15792e9ee839 | -13.9907 | -46.31847 | 2025-08-31 04:04:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 853e8bc5-39bf-3d83-a85b-790510009da3 | -15.0002 | -46.70178 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53db73e6-e9a0-3d26-a3ee-164f4b28b570 | -12.82607 | -48.08277 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1b177e5-73c2-3ba5-bc25-55b93b64efe9 | -12.10567 | -47.22537 | 2025-08-31 04:04:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02c6e83e-0d71-3a9b-8721-556fca2592b9 | -11.83146 | -46.52696 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09b85d81-726a-3fa6-9620-19769e3887f8 | -11.8914 | -46.37104 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0398e703-5930-39b0-9f8f-af3308e71b18 | -12.0939 | -44.72622 | 2025-08-31 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4dc4b01c-bb9f-3f15-85ca-44937652fe21 | -11.91148 | -46.69329 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00882a7c-ce4d-32fc-b99c-e29359e8949f | -11.82679 | -46.52991 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfde075f-de48-3ef4-b46e-9b50f6c46ea0 | -17.73776 | -39.52881 | 2025-08-31 04:04:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5e6f3302-f937-3bf9-9764-8e58f3ebb083 | -11.86547 | -46.50449 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 399d0559-774c-37ec-b9a8-2b904c09fa65 | -14.03438 | -44.57618 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e62d996e-0b7a-3be5-b85a-e0d54464db3f | -13.67574 | -46.92963 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80008118-eb20-35f5-8886-c389bad0cf6a | -16.24024 | -52.65381 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9168dfd9-742f-3b0f-b1d6-2d9d1c73d139 | -14.00077 | -42.15405 | 2025-08-31 04:04:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ddcb1017-2d48-30ce-87fb-2dc2af14b727 | -13.39598 | -47.04047 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be5a5732-2750-33b1-a938-702470b310e1 | -16.40949 | -45.65551 | 2025-08-31 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 818aeb9a-bee9-3371-a7a6-99364a250587 | -11.89725 | -46.46572 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 550a75e1-21dd-318f-9408-01055f53370f | -13.33937 | -46.86589 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfcb9676-54bc-371f-8cab-93eaa8cb1939 | -11.88652 | -46.35151 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00e53950-2b7c-3791-862a-431d249a320d | -13.37333 | -46.95535 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 976395fd-6612-3678-8ceb-eeaa85cb4070 | -14.53711 | -51.98298 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 54da6dc9-578b-3873-b730-b1f2c4ee7370 | -13.50779 | -46.97583 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03fdec22-03dc-37b3-9d12-3e8f95616988 | -14.33626 | -51.87221 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4495a8d9-ab56-38a0-92e5-c730534d3751 | -18.05783 | -45.95003 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b83a1f27-8d2f-31b2-8651-71120b2ae83d | -13.46984 | -46.97818 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9e37901a-4c25-30f3-bdeb-8f8dbd9f2ecf | -13.58869 | -46.89984 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33afded0-167a-33ae-a186-c11832e3ef09 | -11.90195 | -46.39259 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4cacbe7-7f8f-3534-8fe3-133eac40b1fb | -14.27559 | -51.89056 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0322d3c2-3237-3adb-a18f-585d68707fbf | -10.95858 | -50.85231 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 268e04c2-cedc-3739-91d2-8242e98bb97f | -11.94528 | -46.69203 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c673e26-2a96-3b89-b51d-510dcb93fc45 | -13.68514 | -46.87725 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b69337c6-3722-32fb-a001-ac29ca73cdc5 | -14.55321 | -51.98801 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a0848d5-bb2b-3e8f-9901-363034f5651c | -13.97044 | -46.3206 | 2025-08-31 04:04:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5762bc6e-3ea5-300b-acba-c25ff1baf7a4 | -11.90405 | -46.68772 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a42ed181-51ac-3dd1-9b5a-eaa9d0870247 | -13.4816 | -46.95898 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b87e3e62-b613-3ba8-882a-b0713caa0b6c | -11.82657 | -46.50729 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e953b2e9-834e-358e-9c02-7d2ab896d214 | -12.30895 | -45.6977 | 2025-08-31 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de14281f-3daf-3afd-85f6-e684baedc5cb | -11.56494 | -47.61136 | 2025-08-31 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f57ecb9-e908-329f-9f4e-d661b7f2ce9b | -11.89709 | -46.37355 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dfc7e76-8b59-3a1d-9967-9316c7919aba | -16.22517 | -52.67743 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9806a61b-e93e-3957-af21-57603af0a3e9 | -17.71552 | -43.50807 | 2025-08-31 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9982365c-7047-3862-bea5-a6b48510af13 | -13.49101 | -46.95284 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43f2149d-63db-3454-b8f2-f6020dc50874 | -13.36524 | -46.95388 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 54a54e2b-0e7c-349b-b945-4774940f19bb | -12.87481 | -48.08913 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c0fa53b8-2e96-3417-b37d-c18aa84caa51 | -17.61388 | -52.68755 | 2025-08-31 04:04:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
