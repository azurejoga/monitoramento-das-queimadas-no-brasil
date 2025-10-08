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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99033c69-5903-353c-8cdc-56573b55df6c | -14.7471 | -47.85758 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c28b61e9-539f-304a-97f6-5deb678801d7 | -8.19394 | -44.11305 | 2025-10-08 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bf24ab6-31c4-32ec-8aac-e1d0a3121c82 | -8.22669 | -44.19514 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e94d87f5-6742-3613-ac29-a58e6159bdce | -8.47505 | -46.287 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b594ffc-a4e4-354a-98a0-22f7176f49ad | -12.32264 | -50.26888 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f583de06-2cce-3b25-bb24-c3b71eb32aca | -8.62102 | -45.10512 | 2025-10-08 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fa70e19-cd6f-36b5-bf2a-9364f36d24bc | -13.4636 | -50.406 | 2025-10-08 03:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5391331-a6bb-3133-afdb-ba88d585faaf | -11.0515 | -44.78343 | 2025-10-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 336626dd-57cd-33fd-8cbd-86c282782a30 | -12.93942 | -46.85737 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2c5fbaca-a09f-3970-93cc-a574321a275d | -11.73112 | -50.95472 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0ab5ffa7-abfb-3b0e-beea-b242bbac7b31 | -14.71158 | -46.08302 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd44146c-c9d7-3e75-836d-a8d1206d87b2 | -11.77156 | -45.14479 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9e9c2387-f1f9-3d56-beaa-6bc869587406 | -13.29936 | -48.02935 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2ca5977-f5a0-356b-9426-a5b81ec1de67 | -11.15695 | -47.74335 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b57c5083-6dfd-3665-bc24-ec073f0dca84 | -13.237 | -47.18853 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5e28040-035e-3836-a54f-a4b9b9e7c660 | -12.53233 | -42.34482 | 2025-10-08 03:49:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b0aaf18f-f8f1-3a55-99e7-85c79a9da5a5 | -15.65207 | -43.6741 | 2025-10-08 03:49:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcd8cd17-f3f6-35f5-979a-50168e63dbac | -12.95887 | -46.83693 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e3e477d-f80a-3afe-b98a-6a1853593958 | -11.99677 | -47.19464 | 2025-10-08 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 186172e7-fe19-3f7b-a208-85d409fc0916 | -13.06528 | -43.59097 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f8faf26-0156-3e33-ad40-6e456588951b | -10.7345 | -47.65666 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cf794270-6d26-32a5-85ac-b975cff5ccdb | -12.64024 | -50.56483 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7388267f-e619-3e21-8ab9-2cc341b8b788 | -15.24285 | -46.35862 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 175ca0f1-64d6-3aca-8e36-d73c265d735f | -8.11274 | -44.77331 | 2025-10-08 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 07ceae3a-4ae9-3692-8690-cae031618bf3 | -13.33791 | -47.55966 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3b74265-00cd-3003-9a2b-f0598fa1f26d | -13.27389 | -48.04464 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2862310-f1d4-343e-8a7b-e3a4605fdd9f | -8.60782 | -44.90379 | 2025-10-08 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45dc579b-7455-33c4-bbc7-735ce035cfaa | -13.73134 | -45.70299 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f804e69e-9631-38ad-9ec5-e791e033f0dc | -15.07513 | -46.62054 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 479f3391-feda-3d1b-87e3-06070c4c23be | -8.22835 | -44.18843 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 720107bd-3a38-3851-990f-11684bd8e995 | -3.56874 | -44.46194 | 2025-10-08 03:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f369d7d0-9e64-39b0-a28d-7de3ff194a8a | -12.93886 | -46.86035 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1d573b25-22a7-372e-9186-cce407449d3d | -11.78766 | -45.05789 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39227097-03e9-3d63-b3c5-88df1dfc69cc | -8.65712 | -44.90568 | 2025-10-08 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7eef1ca-acaa-38f3-ab99-deb4798e7050 | -10.36581 | -50.2829 | 2025-10-08 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1dacc37f-033e-3baa-ac9a-f8cd27d6399d | -12.3665 | -46.49226 | 2025-10-08 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7df6cf2-5265-3df0-96d5-99a8a9d1ea7d | -9.77493 | -48.29422 | 2025-10-08 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f69992c9-9edc-3064-b97c-1f809d9d6cc1 | -12.79242 | -48.81668 | 2025-10-08 03:49:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fffd53d1-720e-3f32-a97c-1eeec89a5e8f | -13.23183 | -47.79454 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e57319a9-3983-36e0-af26-c57633426987 | -14.6963 | -46.01194 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b357a1ea-e7c4-300a-a43f-ec372c099d0f | -11.76794 | -45.13884 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 612a2ada-6f2f-3b01-a555-8523f6c55738 | -13.22711 | -47.18486 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2368bc9e-3b3b-35eb-bd59-3dfb536ddb78 | -11.72333 | -50.95922 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 39599c29-022d-362f-90f6-f0253a3e1b14 | -3.34907 | -42.33156 | 2025-10-08 03:49:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b81c2f73-e047-3dee-8705-b7d3aa7055ea | -14.39061 | -46.02716 | 2025-10-08 03:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c2c43b81-6073-3a5e-a2b4-a39ffbea2cd3 | -11.45068 | -50.21337 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 00d837c2-e247-395e-b6ae-972da9ab9145 | -11.73231 | -50.94884 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8f7cca10-48b0-30e1-8765-6cd239eddab2 | -14.36318 | -47.73528 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4e5d7e4-49b8-3365-828b-b45b2f3adb25 | -7.79775 | -46.02253 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4375f14e-a6e0-3b43-9c2c-c4e38932613f | -11.79166 | -45.13842 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9f25df7e-d03d-38a7-b0c0-29d386bdc5e0 | -15.26382 | -46.33911 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d701de11-0331-3f22-9ca5-ec332a5bca12 | -11.73891 | -50.95023 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5643e256-1472-3515-bbb5-5974ef07fa00 | -14.70637 | -46.00914 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| db306917-c9df-3e20-ac2f-4707bdff35f4 | -11.45703 | -50.21466 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 635ebede-cddd-3d48-b60b-8ec7e1a5d154 | -14.92125 | -46.79932 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5544a52e-b29e-3ffb-81c0-f4b230d69837 | -12.94553 | -46.85256 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7452d176-acba-3a8f-9528-ba2db14f81ad | -11.03116 | -50.88346 | 2025-10-08 03:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7067976c-8c05-3e82-abe6-87ab2ca56fc5 | -15.25724 | -46.34815 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94ee2ea5-01f5-3fa4-bbda-ebc70fa2e69c | -3.45296 | -45.59313 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9048fd8-bebc-3386-abe0-02ec7657813f | -12.9418 | -46.8562 | 2025-10-08 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 5c6fa3b2-f560-3a84-a419-c1fd77c6a819 | -11.7462 | -50.9555 | 2025-10-08 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 1b55776d-f737-3b6b-9277-e4a57a8e1a99 | -11.7275 | -50.9363 | 2025-10-08 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 296.7 |
| 72e4c656-ba0f-3d3e-b0f0-8828daa1556c | -11.7085 | -50.9385 | 2025-10-08 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| fed23abe-f02b-33ff-85ea-1ef77a6c142b | -11.7082 | -50.9598 | 2025-10-08 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 8b24d237-b604-3f4a-80d2-3b5f6abec8ee | -5.1414 | -44.967 | 2025-10-08 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| abb6098a-befe-37f6-9ef0-3334c922a412 | -11.7466 | -50.9342 | 2025-10-08 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 23cd8f59-5d13-3f18-a989-ed105a20586f | -11.7272 | -50.9577 | 2025-10-08 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 266.7 |
| 5a2f1204-3132-316f-bd8b-7c01a05efbb8 | -5.7325 | -43.6177 | 2025-10-08 03:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| aa683a54-382b-3448-a41c-025156ec14ce | -10.3924 | -50.2275 | 2025-10-08 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| a3eb3995-a7d6-3178-afd3-94888c32a962 | -18.07307 | -44.46234 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ae4c23e-6d14-3835-8cf3-dc58356f180d | -15.37544 | -47.30314 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b3c4883-8be3-3b2d-8ce5-1b9b908a3c82 | -17.99533 | -44.98133 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75747e94-4ec3-3532-90f0-5f64343ac501 | -22.38332 | -49.96507 | 2025-10-08 03:51:00 | NOAA-21 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c9d94539-c996-3168-ac6a-b259595a8616 | -19.81989 | -43.08505 | 2025-10-08 03:51:00 | NOAA-21 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c603b61c-f4d5-30c3-9d67-7f8617e99129 | -19.29473 | -44.45868 | 2025-10-08 03:51:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcec5705-f572-3be1-8709-50930248e6cc | -19.30401 | -43.16777 | 2025-10-08 03:51:00 | NOAA-21 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| be073cb5-6ab4-330a-92a8-c7f9b7c06f92 | -18.07589 | -44.46929 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2728f88-c975-3b40-9bad-41a383679b0e | -17.29398 | -42.64997 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 700916d8-d481-382c-b3f1-db9e6919bc1c | -18.0271 | -44.94541 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1543706f-8f69-31eb-ab45-7e719f65b2c0 | -16.3322 | -47.0597 | 2025-10-08 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31f4fad7-eeac-3019-930b-8b82bd9103e9 | -15.76906 | -46.25234 | 2025-10-08 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f41655c3-312b-3491-ac71-398892fb5331 | -18.02308 | -44.31296 | 2025-10-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fbb637b-f66b-30dd-84b5-8dbc3a6097d8 | -21.39361 | -45.54987 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 04464ea8-6714-3c22-9d4c-eac80e05654a | -21.53267 | -45.43257 | 2025-10-08 03:51:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 011228d8-716c-3608-b3eb-88cde43cd97b | -15.06713 | -49.48273 | 2025-10-08 03:51:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff84417b-a0f4-3c51-9be5-7bff6260add2 | -19.94497 | -42.10988 | 2025-10-08 03:51:00 | NOAA-21 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fcc5b04f-0bd7-31a2-a128-14b79fee9d60 | -16.2926 | -47.08734 | 2025-10-08 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43143fb4-b371-325a-935f-54f5d78e7f24 | -22.38622 | -49.97635 | 2025-10-08 03:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bc5e0391-d168-3e66-a911-20d3907cf2e1 | -17.45021 | -42.09968 | 2025-10-08 03:51:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c65492fa-1c9a-3780-b432-0282513fd0d5 | -16.58811 | -46.55468 | 2025-10-08 03:51:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95c5c9e1-d300-3f7b-ac20-5f6bb8b663bb | -17.97907 | -44.97816 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 92189dda-de46-3e89-8094-e0a8b4c274f7 | -18.05067 | -44.45125 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6fcd105-8601-3e21-9cdb-72a1e0e99343 | -20.39377 | -43.07162 | 2025-10-08 03:51:00 | NOAA-21 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e6a54dc9-11ea-3585-a28a-d250f1779560 | -19.46936 | -45.95828 | 2025-10-08 03:51:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5ed360a-9196-39ad-857c-9e8bd30e553c | -18.41709 | -43.03193 | 2025-10-08 03:51:00 | NOAA-21 | MATERLÂNDIA | MINAS GERAIS | Brasil | 3140605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2620f4d4-64dd-3cbd-b64e-7d8b178e7454 | -19.39711 | -44.38631 | 2025-10-08 03:51:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3168198-a0fb-3363-becf-9e637cc229d7 | -15.8032 | -46.24609 | 2025-10-08 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8c0fa9f-4f11-319d-980d-77637c9c828f | -21.85023 | -45.37864 | 2025-10-08 03:51:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 930de71e-2d9c-338f-85d3-ab8d38543c6a | -19.1009 | -43.7287 | 2025-10-08 03:51:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6506b8e8-14e6-3d8d-a135-04d57031b03c | -16.76179 | -43.97803 | 2025-10-08 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
