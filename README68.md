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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3732a84-8e80-3089-838f-b48af80be85f | -7.11155 | -44.58824 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39bb7709-9377-324a-b0d8-5cc06d4e76ea | -8.72733 | -63.06849 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5a906b0-e015-3610-aae0-8bf297df0193 | -10.38346 | -57.82583 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e4400cd-6e76-337f-919c-226e150dcf3c | -9.99396 | -59.63636 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c34986b6-d1dc-3c14-b7a5-7e4977fae1d0 | -9.17177 | -59.57745 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| add4f837-640e-38de-ad5b-c292f0126216 | -10.99506 | -46.84913 | 2025-08-30 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7069617-2d43-35af-a687-2fa1500398d1 | -9.2505 | -60.92913 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3ab4b29-36e0-3a91-bc8b-a5afa56e2f46 | -9.43934 | -60.57062 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2064128f-41ea-36ae-aec8-2b18d8545987 | -7.08986 | -44.31794 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cc4b5011-d629-3ab5-be26-01b368652fd6 | -9.43713 | -60.56221 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cc65c27e-345b-3690-8f4b-3f35884ee740 | -9.511 | -54.43098 | 2025-08-30 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ce61398-9d71-35d3-a669-de0ee7bca7c7 | -10.44423 | -57.95771 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 155572ac-b8f4-353a-a9dc-415a390df950 | -11.93049 | -46.68514 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9b740a3-6325-3bfb-a6d8-19ea584a7862 | -11.84494 | -46.44872 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80de637f-554f-3309-a601-0962237cc1e3 | -9.46751 | -60.30945 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2f33a61-c8aa-3c27-b5de-93d8a5180494 | -9.44664 | -60.54775 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 85e54639-6978-3f0b-b21e-fd00c6861b3e | -10.36133 | -59.2104 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 283c9327-4e61-3127-b6cd-7def4307bc24 | -8.18756 | -61.37535 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f950513d-d67b-3e79-bc8a-c670a1734c74 | -11.85724 | -46.39282 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 303086ee-f4d2-3778-a335-5e1bd3578bd3 | -8.05122 | -45.41432 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72827339-f087-3a57-8b6b-e9e89a7d928f | -10.36361 | -59.19621 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a46f8df8-0c7e-3174-95e4-e108f354363e | -6.78067 | -43.78814 | 2025-08-30 05:10:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 47c2ef12-b9e8-3eee-97b9-79b922369487 | -6.34133 | -58.17377 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4348d445-9a67-34e3-bc4b-5302618c4b23 | -9.4403 | -60.54271 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| feab9f9d-f89d-3cdd-8f37-b36858ac3a69 | -9.71082 | -49.47048 | 2025-08-30 05:10:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aced2b3a-3657-3436-a479-b420329a4394 | -11.84408 | -46.44897 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 20682520-9a4e-3b6f-8444-8e9117b16451 | -8.88884 | -60.7466 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a4fcd04-42f4-3bc9-8d0e-018abf81a5b4 | -11.82807 | -46.47395 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 0b55af78-a0bf-3cb8-9e17-44b8bd3d34f3 | -8.9215 | -64.23341 | 2025-08-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94a7b3b1-f20c-3e99-a651-5f2d4e39c711 | -8.87317 | -60.73162 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1332398d-25ce-3809-9d43-6a06ac1de555 | -10.45585 | -57.97031 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d49379b-5c0e-380e-b79a-6d4d99b59b13 | -9.44245 | -62.36883 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5fa65df3-f367-30ef-b635-222d6c7c879a | -9.4479 | -60.53997 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 23c50d3d-d2a4-3cbc-8ecb-90211005d86a | -9.2559 | -65.84896 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18c5a517-a99b-3711-ad8d-3e04c2c35564 | -10.6506 | -48.66105 | 2025-08-30 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a381fa3-ae17-38cb-ae8d-0688118def85 | -9.44707 | -62.36471 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb08d218-9303-3378-8d47-6dd0d752f97a | -6.76553 | -43.79321 | 2025-08-30 05:10:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 13aef18a-33b8-3409-89e9-636551f9bd37 | -6.58843 | -43.65117 | 2025-08-30 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e69b7d34-7bf2-332a-ac8f-c8fb3c6bf9e1 | -9.75007 | -63.31702 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d35eb957-5902-36ce-a549-f3ea2f8445a2 | -7.15358 | -44.90196 | 2025-08-30 05:10:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 75ae2d0c-5b08-39d4-af73-ccd4cba4ac6e | -9.48873 | -45.41268 | 2025-08-30 05:10:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a991004-7849-331a-9acf-e31655bd6e94 | -8.54994 | -63.03009 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa7bce47-042b-3469-a023-590d7c3e0c9d | -5.61802 | -45.01197 | 2025-08-30 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 173ee4e7-f1fa-3cbc-9bf3-274d56ed42d8 | -8.59784 | -60.57836 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf6cdc61-97df-3390-809b-0dc6a0a08d44 | -9.63651 | -48.30056 | 2025-08-30 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9cff64d-7b6a-3e68-923a-6ad5c68ae4d3 | -10.46132 | -57.93529 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b0b5dd9-9221-3e1b-876c-478f6acbfc93 | -8.7112 | -50.36129 | 2025-08-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 965423a1-2a4b-3b71-9771-ddfb9b27d520 | -10.03246 | -59.35454 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33db8cd3-2cf5-33cf-a90d-9c291b8c0ed7 | -8.04223 | -70.10412 | 2025-08-30 05:10:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f07d2a97-8ccc-38bd-81c9-b722e62d72ad | -8.28777 | -61.40422 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f78b4a01-103e-3edd-8de4-0e11af753d01 | -11.57727 | -46.3647 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2bd1f59-46c6-3a36-9862-95d3b14ed10a | -9.63236 | -48.3007 | 2025-08-30 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d95b4599-69a3-34a5-b5e7-b8b13d0e923d | -8.51579 | -60.56947 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4ec180c-590f-3f71-93ea-fb110f275fd2 | -9.44867 | -62.35516 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f8f97b09-efa0-3fbe-9c46-9a9bc9f05abb | -8.87604 | -60.73621 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2bd59d58-6022-3f76-acc1-1beb0782ff84 | -8.88377 | -60.73339 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 136913e7-e0ce-3044-92f4-77f7d678d1a0 | -9.11375 | -65.76053 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| effc43c2-a7a7-383a-a8e8-2f7d01a98a7e | -7.09679 | -44.31883 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1f1e2b71-009a-3815-bfe5-0fb78772fc3f | -9.20199 | -59.54882 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 078abae1-8fcc-3837-88d3-ce9816dbee51 | -9.11187 | -65.74364 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13bac296-a83f-36ea-be29-2b461a926ba3 | -9.18249 | -59.46735 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20bba6d1-fc71-3b55-90db-c8b1dc4eddda | -9.45178 | -60.56821 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ed0fba4-179a-3e33-939e-3a49b7457b5f | -9.11284 | -65.74232 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 281cddaf-3b6d-3452-adb5-9b2b5c82661a | -9.16898 | -59.5732 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2237fb97-3986-3c15-8661-174296ae42a8 | -10.46078 | -57.93879 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52666ad6-a450-360a-b421-e174807784fe | -9.16397 | -59.56119 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7ace06a-347d-3322-84a2-24fb584665eb | -10.65097 | -48.66166 | 2025-08-30 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 921c6692-0b92-3b0f-a21a-22d75daab553 | -5.82881 | -46.35591 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1e58e4e-5964-3787-a9c5-ea092ea03eff | -9.43499 | -62.34304 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3815e152-9d38-38d0-b7be-bee8eec8e29a | -11.84549 | -46.44378 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4bff092-0a69-3b65-804d-fe929607d4b4 | -11.15068 | -47.15065 | 2025-08-30 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 61b185c8-291d-3b70-88a3-923071f872cb | -9.45788 | -60.55316 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fbfbb99c-b308-3cdc-ba19-8a5889519185 | -9.1758 | -59.58186 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cb70e8c-a1bf-3c86-bb65-ec2dd11d5002 | -8.5448 | -63.93958 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f08a981-f4df-3a74-b5fe-1b86da2cc6fe | -11.84467 | -46.44401 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b157177f-9fc7-355d-9cbe-e9672253e41a | -5.8253 | -46.36673 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ba4bca8-0848-3d29-8c2a-236bf79e141b | -10.38568 | -57.83337 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3642901e-49c1-3213-bdb7-31bb766997fd | -7.77856 | -45.47642 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 170c9196-f77b-3bb2-9de4-7b4b20661042 | -9.46252 | -62.3429 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 043cd7c4-f31e-3843-a77f-a85c01c55373 | -10.44922 | -57.96926 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4b4d86d-dcb0-35df-a0fa-ddd570964d5a | -8.90747 | -62.1091 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6825ee16-8c1c-3fd8-b131-e3e830d33dec | -9.17859 | -59.58606 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cd941cf-746d-3b40-bdab-ccc0dc570cef | -5.61154 | -45.01516 | 2025-08-30 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 589e05ef-517e-3247-a531-c3c69d7ce6cf | -11.93633 | -46.69075 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 535225ee-3b21-3d7d-a869-3e6382812f8a | -9.17421 | -59.57035 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55d44334-6676-36dc-8250-d8e634949ead | -9.44742 | -60.55138 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b38d5e4-a447-3bc7-97fc-865ad1754f8c | -5.42937 | -45.52511 | 2025-08-30 05:10:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 557f96dd-c846-3941-bc06-4f94e30049a6 | -5.21825 | -60.28682 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd17b7de-67e5-3c6f-993e-827d849d313b | -10.45968 | -57.94582 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61158e24-6c48-368f-9924-76bc5a2e5f4f | -8.69956 | -60.4858 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccd3b58e-2df3-3f33-85e6-ddee570d3ba1 | -4.87876 | -46.85323 | 2025-08-30 05:10:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fe49397-8fda-35f8-855f-b6f75661d96b | -9.54074 | -62.3831 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2973e05f-fcef-3456-bf94-7179efeaaba3 | -9.15134 | -59.59663 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad3bb0e3-729b-3956-b895-a2aa53f0f271 | -10.32205 | -59.18179 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 362db0aa-bc4f-3c5d-bf44-9d3422da52a3 | -10.07258 | -58.35706 | 2025-08-30 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 397e0d88-679a-387c-b93d-4bebc8ad21ab | -11.86384 | -46.39663 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0e580302-a20f-36b5-bbee-0de876c2bb59 | -9.24889 | -56.89421 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1be9130-e5db-35bc-b787-0b38eaae167b | -9.17302 | -59.57764 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7d6b78a-d000-3f7f-acd2-e7fca310d971 | -11.86385 | -46.39252 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c07b0b5-1242-3bea-86db-010051e3e402 | -8.56044 | -63.01725 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README69.md)
