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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 838d0297-584b-368d-84fa-ddec6993f105 | -22.93257 | -49.1663 | 2025-09-09 04:38:00 | NOAA-21 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9312ead6-5696-38c7-99f6-8fd9f6568413 | -22.60575 | -51.96047 | 2025-09-09 04:38:00 | NOAA-21 | ITAGUAJÉ | PARANÁ | Brasil | 4110904 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d93aac53-71da-376a-b666-ab32fca179ee | -21.72647 | -46.23008 | 2025-09-09 04:38:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3da211c2-b36f-37e9-87a1-05419105261c | -23.06431 | -44.96465 | 2025-09-09 04:38:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c6632ce2-a175-3e89-bf4e-aea599743a5c | -21.44445 | -48.83503 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5331f3fd-528e-3af6-8f0e-4feaaf6778a3 | -22.34953 | -50.88853 | 2025-09-09 04:38:00 | NOAA-21 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 081d868e-1385-3d1a-a63e-36e057b265b0 | -21.85973 | -46.08452 | 2025-09-09 04:38:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bc202404-4c41-35ef-9bd6-fe535bc8b1c7 | -22.3423 | -50.89112 | 2025-09-09 04:38:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7494056-6e2d-33d8-82f7-8c5292053544 | -21.64308 | -47.03769 | 2025-09-09 04:38:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| fb61885b-f241-3613-b066-78bf18fcb2c5 | -21.64438 | -47.02739 | 2025-09-09 04:38:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 83744185-7ad4-3f0f-948f-58d2f00ef153 | -23.71678 | -47.46036 | 2025-09-09 04:38:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| dc930b05-3f01-39ac-adda-5c38f9429167 | -21.94242 | -46.71906 | 2025-09-09 04:38:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 62821ecc-3df8-3764-b31c-556ae0713615 | -21.64757 | -47.03315 | 2025-09-09 04:38:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 581efa0d-532f-31c1-bbeb-61b519e9d4c6 | -22.35618 | -50.8897 | 2025-09-09 04:38:00 | NOAA-21 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d49b5f94-ce67-35e1-902e-9ad70423714d | -21.09677 | -45.92915 | 2025-09-09 04:38:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3115bfa9-ba40-3774-b0c1-ec2c5659951b | -23.56249 | -47.16776 | 2025-09-09 04:38:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0cbe5e27-9f44-3fcc-9474-695ce9055acc | -23.1462 | -48.25961 | 2025-09-09 04:38:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3370fc7c-1386-31f5-8d0b-8e4a03ac15a5 | -22.09789 | -51.37811 | 2025-09-09 04:38:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2560d6d3-f37f-3e7a-9871-5fef1412560d | -22.34563 | -50.8917 | 2025-09-09 04:38:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9cc3673-0f1b-3d3b-ad16-8efab5d063d8 | -21.44678 | -48.84398 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 6fd6029c-aaf8-392f-b95f-c2682b8f2a1a | -21.43968 | -45.34264 | 2025-09-09 04:38:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 69834e08-ecde-345d-973c-e8c5b6e6a12e | -22.36121 | -50.87902 | 2025-09-09 04:38:00 | NOAA-21 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8307394f-b549-3d41-90ef-1dd4a044b559 | -21.9337 | -49.96252 | 2025-09-09 04:38:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9f391f14-8fe3-3126-9401-b63ec25c523d | -21.45087 | -48.84036 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d7dd235f-6213-323c-a51d-bd04a1a34fa4 | -22.35058 | -50.90413 | 2025-09-09 04:38:00 | NOAA-21 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0518201-61f5-3ef9-9dd8-1f7ccf554f24 | -23.71897 | -47.45671 | 2025-09-09 04:38:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 6a8e2989-eb1d-374d-a675-178763a98803 | -21.72168 | -46.22949 | 2025-09-09 04:38:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| de167f56-a7ed-3047-bb4e-d89795d5ce4f | -21.43335 | -48.83749 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45ed1ade-2200-379b-a62a-05421c9d549f | -22.32785 | -48.81697 | 2025-09-09 04:38:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 07d2d80f-3160-3c85-9709-99b3f66c1267 | -21.58506 | -50.35041 | 2025-09-09 04:38:00 | NOAA-21 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d5646b0e-ddef-3639-83bc-99f695f34239 | -23.32829 | -50.88322 | 2025-09-09 04:38:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 83d0112f-72c1-372e-88a4-5bc188e4af0e | -22.09459 | -51.37752 | 2025-09-09 04:38:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 68db8d8c-2ae6-3281-ae46-6e33f8d75ea9 | -21.23141 | -49.87728 | 2025-09-09 04:38:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| be07065b-1121-398e-b6e6-28a8c3518be4 | -21.23537 | -49.88165 | 2025-09-09 04:38:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 22aaf71f-9717-3b04-bd5b-9320682feec7 | -21.02202 | -48.41908 | 2025-09-09 04:38:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9431adff-cb8c-3bc7-94e6-4d2848800338 | -21.44386 | -48.83923 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8b0aea47-b38f-3b03-b567-95d043fa75f8 | -21.58114 | -50.35365 | 2025-09-09 04:38:00 | NOAA-21 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 016c923c-db5b-3e2f-afb5-7342c4bd1688 | -23.71833 | -47.46198 | 2025-09-09 04:38:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| e30411bc-03ba-3682-84f0-ae31a8fbbdc5 | -21.64053 | -47.02681 | 2025-09-09 04:38:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f5d57471-f3b7-3241-a708-69af05e7957a | -22.38426 | -45.41642 | 2025-09-09 04:38:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dde3b5d0-e1d4-3d63-8a49-141d957c0588 | -22.92906 | -49.16574 | 2025-09-09 04:38:00 | NOAA-21 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9dd9a70d-6020-36a3-9fad-638a5b7e309c | -22.59531 | -47.42871 | 2025-09-09 04:38:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69b89083-44f7-3aa9-bbc9-52e270e4417b | -22.22735 | -49.72379 | 2025-09-09 04:38:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b182d824-d248-3db3-b593-baadfef5b37a | -23.72061 | -47.46108 | 2025-09-09 04:38:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| aeafc467-eab7-3938-a6fb-eed5721fd950 | -22.32864 | -50.98134 | 2025-09-09 04:38:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d179399-719a-3053-916e-b127c666c6a9 | -23.14502 | -48.2685 | 2025-09-09 04:38:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c178718e-2a37-3741-8868-1afebe19c659 | -23.35905 | -46.34338 | 2025-09-09 04:38:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 65bde74b-315d-38c3-97ad-266e429df78a | -22.22794 | -49.71978 | 2025-09-09 04:38:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a6a44525-3789-3272-b209-61820bc4c468 | -21.72244 | -46.22934 | 2025-09-09 04:38:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 75c85261-7e4e-3501-958a-19c4c36469c2 | -22.32845 | -48.81268 | 2025-09-09 04:38:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 95e666c3-262d-340f-9f38-21f1d14b61ad | -21.44328 | -48.84341 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 835bb7b1-da4a-363a-ade2-1b98698c55df | -21.23593 | -49.8778 | 2025-09-09 04:38:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7d084760-1bc9-3fd1-80cf-62f05159bec1 | -22.33199 | -48.81326 | 2025-09-09 04:38:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2a90e8c9-0b2d-35f4-a9b3-e33a8bec61cc | -10.0111 | -64.9151 | 2025-09-09 05:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |
| b8d6f793-85f8-3d84-a05a-3a3769f699d6 | 4.41097 | -60.39741 | 2025-09-09 05:21:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6155dc69-2116-3660-ae94-d7125884cdc4 | -2.42788 | -49.31034 | 2025-09-09 05:21:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5828c90-b7c4-313f-acbf-d510704e4ce8 | -2.62832 | -46.84015 | 2025-09-09 05:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2ca6181e-456f-3c71-b72f-1ae7ff143ee3 | -2.43367 | -49.31123 | 2025-09-09 05:21:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d99e85a-cc1e-3249-a7e1-edb4dbe4c397 | -2.62687 | -46.83524 | 2025-09-09 05:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 47773e45-ee31-328c-9a46-a45830bb94c6 | -2.62599 | -46.84105 | 2025-09-09 05:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 41ce7f17-4b4a-399c-b18f-bf6b39454667 | 4.40753 | -60.39808 | 2025-09-09 05:21:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 662f9659-e74e-3aa1-bceb-4f6ba6c9668e | -9.24655 | -57.0645 | 2025-09-09 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc4d802c-23d4-3a74-85c5-a3628bf79bc1 | -13.95609 | -54.01503 | 2025-09-09 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc45e14a-e15c-3851-a927-e73f059d6690 | -7.58524 | -61.68424 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7db5ff9-f1d5-389c-bd54-46cda48958bb | -15.78799 | -53.5389 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db614b5b-beb6-3c48-b438-e2b1263ff152 | -7.56306 | -61.31087 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18de328d-326d-3de2-9097-cd6a78038bca | -7.40051 | -61.62916 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57e1abf1-a86b-31bb-9179-81e0abf096bd | -6.86255 | -47.9078 | 2025-09-09 05:23:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26a1cc48-5824-34dd-91c3-c020e26894b0 | -14.54367 | -48.75591 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 036c0bff-9bea-31c3-b3c9-ededa4bafbc3 | -9.25347 | -57.07042 | 2025-09-09 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8367df6b-985e-3f7b-a7c0-d1870db64d04 | -14.59209 | -52.11602 | 2025-09-09 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee25f19d-1db6-38de-8726-f715be752a14 | -2.19076 | -54.46999 | 2025-09-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67b8697f-8602-3f85-844d-bdeff5e6fe4c | -8.09182 | -54.75517 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36c13216-dae8-35e2-a5f5-5dd78c96e8bd | -16.07567 | -50.48537 | 2025-09-09 05:23:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b4caee9-c5a0-3175-8033-42e16f6244da | -13.90126 | -53.96452 | 2025-09-09 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77bcc2c1-0f69-3ab3-a89d-7f66aa0f6f15 | -7.82364 | -63.57267 | 2025-09-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36e56553-71ba-3da3-8f3e-845d9ae4fda2 | -15.73397 | -53.58974 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 851ab46f-9548-3166-acdb-6f0c04ef92f0 | -3.32589 | -54.90919 | 2025-09-09 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50d72b74-3434-31f3-a54f-28b7048c32b6 | -4.70067 | -55.67254 | 2025-09-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c77f357-4e63-3ca0-b525-553ff75f0f1d | -15.82123 | -48.94668 | 2025-09-09 05:23:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 856fd5a3-f760-3f1d-b0b4-678c6b4531c9 | -9.27835 | -56.8988 | 2025-09-09 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15cbe7fe-c3c5-3b32-8536-26c64c578784 | -13.03644 | -48.0287 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b9bc1780-b620-39db-8f6a-737749cecade | -9.85351 | -47.79147 | 2025-09-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e87059a-6ca6-3bba-8ccc-00040a592587 | -7.39995 | -61.63267 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c390945-fbaf-3154-9088-cd2b82cfe37f | -15.25257 | -53.79357 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4447c5f-5bba-3e50-a84a-a20473d23b26 | -14.72122 | -60.25024 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f9aa833-ed6c-3d1e-ab0d-10f4118bd663 | -14.71893 | -60.2417 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ef5096f-4128-3d9f-a31a-05c695df3343 | -14.87583 | -55.80186 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69a9d8f6-9ff2-3a36-a73c-294a536784fe | -12.82704 | -52.9438 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffa0095a-7a7b-3071-b931-e1980dc9214c | -15.53176 | -48.39483 | 2025-09-09 05:23:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d85d3aee-bece-373a-981c-c2a0ea57c385 | -14.52198 | -48.74546 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb61f766-9a73-3311-a136-e825c42de60a | -15.24917 | -48.81375 | 2025-09-09 05:23:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e9e3e1a-d031-3b98-9efa-6cb995dd86f2 | -13.03955 | -48.02985 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 231ed063-c8c5-329c-bb7c-a805c282dee2 | -5.4192 | -51.53817 | 2025-09-09 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e6bc6e9-2b70-37d1-8b4e-00f7790ca247 | -14.375 | -60.29789 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c612698-aacf-3f04-9a11-f7b8ff8655f3 | -12.83314 | -52.93778 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b669342-cc23-32f4-b4bd-2a31d348a8b7 | -12.93254 | -54.7661 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59544f0e-a3d3-3205-9de4-8de83592fa8d | -15.24233 | -53.77588 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62cece68-d7b6-364a-9b18-2e202f6bdbe4 | -12.19763 | -53.90078 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 182c56f7-9a08-3e4e-80c9-b6d6690a5479 | -14.62241 | -52.15459 | 2025-09-09 05:23:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README57.md)
