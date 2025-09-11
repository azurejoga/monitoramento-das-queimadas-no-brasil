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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d9b6e09-905b-3a53-8ef1-6f0eaf9f81e2 | -11.71292 | -46.50366 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6129fa71-b04b-3946-9c2e-eec6cb6a4ade | -11.59982 | -52.21691 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2319692-04a7-3407-810a-6dfb83e79e62 | -11.73716 | -50.62503 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d00b6e65-eb02-3b42-b7c5-a89cb3f82026 | -12.8571 | -52.94219 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0670ee5f-ab85-3683-90ce-41da14c137ea | -9.67911 | -47.52285 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fa064c7-e1b5-3455-aa52-f81556b18333 | -12.41741 | -63.88855 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da2ead6f-778b-354f-9296-84b3c378e739 | -16.28024 | -45.68211 | 2025-09-11 04:46:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5868167-24ce-386a-842b-5888c02c6861 | -13.13393 | -54.91078 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e003e52-b09b-3bf9-a15f-112f5047cf25 | -15.14045 | -48.61329 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 403106b6-5293-3155-acec-330103acc826 | -12.93951 | -54.81445 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f389240c-30db-3abc-9251-29e6457b8ab0 | -12.01773 | -47.58527 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a17d22f9-6e11-3257-a409-37f93557cda8 | -11.78633 | -50.57583 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd25d416-0692-3ecd-99f9-8ec2c23f883e | -9.02848 | -49.77221 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13d1e655-6f38-3aed-ad9a-d682925f008d | -9.76725 | -51.0641 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d273b07-78c4-3345-b0bf-5518228089b1 | -13.50743 | -50.80928 | 2025-09-11 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31a53e9a-19a7-3401-9919-b82eff51ec40 | -9.90173 | -50.17256 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77849d87-3252-3e94-b140-05fec0135372 | -11.60755 | -52.21096 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f010dedf-ab52-3682-8063-a7a9673dd263 | -10.55218 | -49.87574 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f70427a6-57b8-3aba-81d0-e7eadde0c2ba | -9.89987 | -49.90999 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d764a06e-b6ba-3400-8730-bac19fd205e8 | -10.39766 | -50.52131 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a555d27-f487-3e4b-9633-93f337129faa | -11.43292 | -43.5747 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28eaf6d6-681a-3fe2-a41d-eaacf6c3b886 | -9.151 | -60.25716 | 2025-09-11 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16f93c2d-9b1d-324d-9409-7296b3b5fe53 | -11.15064 | -52.02949 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 304760ae-150c-3fe8-ad64-30458ba2fb3a | -11.35887 | -46.54121 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3b33681-88b6-3211-b4ca-42a687945163 | -11.35682 | -46.52502 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 35920061-0608-30a8-8e85-26d4cf259ba7 | -15.12492 | -50.13581 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56fa6d58-27f1-31aa-9c32-a0dca6b0d7ba | -12.87627 | -47.96151 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16a10495-9e7b-3d41-be4f-4d6e2cbbb6d3 | -9.01719 | -49.50157 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92b5ba78-d8b4-3811-982b-5738788cb41b | -15.60447 | -47.10429 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 259a78dd-048c-3f7b-8cf0-60a5ec5c3449 | -11.77071 | -46.49029 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ceb06df3-f733-39ab-81df-342e85e7f9f2 | -8.58688 | -54.67009 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec2b8054-5ccb-3c5a-afe7-5b770377cecb | -13.22521 | -51.76388 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5443fecc-4ec4-3485-aa74-4792538713a1 | -12.39762 | -54.16504 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b2bed84-56c4-3640-b7f7-17a71707339d | -9.71814 | -43.52356 | 2025-09-11 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfc46842-bf8f-36e3-a4aa-02510690cc01 | -10.71306 | -48.30456 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c25f24b7-96c5-32d3-8ea1-ba4a4744aa6b | -10.5683 | -52.03951 | 2025-09-11 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8bc644f-fbad-3389-b0f8-03e54c2121dd | -9.7247 | -48.09381 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bb5c14f-acaf-3911-87ba-1dc81ce9d5ef | -11.95983 | -46.65351 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04a80d97-0422-396e-9812-a7aa51799dc6 | -11.22296 | -54.99415 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da77d209-d772-38b6-912b-29906e32c397 | -12.20512 | -53.86345 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 691137d8-741e-38c4-a3a6-b333f734a1f0 | -12.40775 | -63.81321 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dcb1129-2dc3-3bdb-b566-c4431e52953a | -9.7189 | -43.51773 | 2025-09-11 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f15a7559-e641-3f92-8c6f-0aed549b5323 | -11.47785 | -49.26403 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a661f94-70d3-3ff3-9412-6ee349565ec2 | -16.28498 | -45.68276 | 2025-09-11 04:46:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3769e99-0a8a-3347-b8bc-7dcdb5f3a8fb | -9.45196 | -46.42283 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7ae97470-75ab-32ad-a798-1e87b5786c90 | -10.20387 | -51.67955 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20dbd2ba-2f12-391a-b2c2-b3d2d23a4f3b | -13.15584 | -45.28571 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc1dfef5-107f-35c1-9f72-b30fc66db41e | -14.306 | -45.03977 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a94b30eb-9e21-3f0b-a655-ecbe0ff229d7 | -9.79261 | -61.52057 | 2025-09-11 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e469aaf8-a9b5-3ab3-9542-1b778d50184e | -11.64829 | -46.91002 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5142ea2-e2a5-3b85-9fdb-2fbeb9797bd1 | -12.46883 | -53.8353 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dab17681-5cdb-36e2-833d-e8a683bbf268 | -15.80836 | -52.27997 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8359fc0e-b9de-3cf8-b7fa-893bcb58161d | -10.19451 | -51.69596 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dd7b1ce-dbe2-3806-a1f0-991c6dc70998 | -9.53409 | -48.30252 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edf1649b-ce38-38a7-8adf-f2d404956b76 | -10.26735 | -48.8257 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c822bbf-bc83-3b7e-946f-b4a3089a7fce | -15.67127 | -47.02774 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6d78dde9-b10d-365b-9a14-b5d799932b6c | -14.88754 | -55.84695 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f81c0378-6527-392f-af17-313bfc3b1a0d | -11.87602 | -58.81733 | 2025-09-11 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe5c6417-173e-3b16-94e1-436eace1fdba | -12.4087 | -63.80861 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 172112e8-3f57-392d-a077-a364c469cb07 | -8.51876 | -51.38251 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ef678ac-8b8e-3d24-850a-7d5b7c034ce7 | -16.17697 | -48.68185 | 2025-09-11 04:46:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d69bb67-81d4-3f93-b32d-7e063aa3692a | -8.63144 | -53.12255 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 85de74c2-fdb0-32fb-81e7-b52a82b3cbd5 | -11.35984 | -46.56517 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2830a4f3-6c61-3e27-b7b9-764e93e08eba | -9.02221 | -49.76743 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c6c91865-1243-3a06-9444-5f6fd25a6b3b | -12.01847 | -47.58009 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fce13bcf-6ec6-355f-859a-8ab2390d756f | -8.58231 | -51.30322 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2c1ac441-da81-33ca-8dbf-fb5fc71c497e | -9.89211 | -50.1673 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14c5a5bb-4d7c-3a8d-8b9d-0d581cff56b8 | -11.47256 | -49.25066 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a51d28f9-d85c-3385-b17f-4b3687e4121b | -15.80387 | -52.24214 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e823f037-76c4-3958-9299-c0bf80c21134 | -9.29911 | -46.76688 | 2025-09-11 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9810d49e-4509-335c-a38c-8040cc76743b | -13.33628 | -51.6818 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48f8729a-07fa-323a-8352-f544e99eaa14 | -11.16362 | -45.31368 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b7a9206-b8af-3000-9238-c99b1027a1ef | -10.39771 | -48.57111 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a77824e1-cb76-36ce-b484-9c4b3d116d0d | -12.87057 | -62.12576 | 2025-09-11 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50f70fe7-e50f-3570-be28-f331cfe22b73 | -15.54836 | -54.74508 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b0d2f29-6209-3ba0-9034-69ec515ccfa5 | -11.47502 | -43.69093 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b942caa7-7bb8-32f5-b2f9-e6c9df17505e | -11.34531 | -46.484 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4a64d12-5c34-3c47-b6dd-e08337b4e919 | -15.13904 | -52.42 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dfd0c96-240e-3f50-97b3-ad846a445ba2 | -15.69376 | -53.83271 | 2025-09-11 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3b7ae5e-192c-3522-82fa-876e1db7ae95 | -11.15819 | -48.35003 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b9bbd74-78ed-35a5-a438-780e6c88ed5b | -11.41991 | -43.55391 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1f521454-6638-3441-a51d-ba1e9d79fe2a | -9.3765 | -50.38323 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6498edcc-1e76-3849-8e85-94b417254ab2 | -11.78622 | -47.32196 | 2025-09-11 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01db8487-51a8-36bd-9f56-973635dbe9b6 | -11.43673 | -49.29537 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa1feefa-b4ac-333f-805a-c2a2501b7ee9 | -10.65676 | -48.6368 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74f1df60-b5fb-3454-8fe0-02a191123ebe | -14.40258 | -47.31299 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd28e313-d562-3c47-9a7b-547243dac8a6 | -11.34115 | -46.48311 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7ca541f9-28cb-33f0-b289-01dfc14cc0b8 | -13.85219 | -43.81993 | 2025-09-11 04:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12f77873-d81a-36cd-a248-83fae906fab1 | -12.02897 | -47.61449 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0bd25e2-e97a-36e0-b247-b0ff85e4c768 | -9.01711 | -49.77807 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f440a3b-28ca-3948-b18f-ed371327d5a5 | -11.67758 | -46.87998 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2d60dc8b-f587-32dd-a1e7-bd15b99d3bd7 | -9.56151 | -48.29092 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ee0a457-cabe-3431-a144-0a3d405717c5 | -15.28407 | -53.7822 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc164092-9498-3725-9f98-74c97544bb26 | -12.07917 | -50.99264 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5378ee84-583d-30ab-90f0-e75efd94ff11 | -12.60435 | -56.96677 | 2025-09-11 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2da4728d-f1d8-3efa-9583-e418079f7a0d | -11.8255 | -46.74361 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28048694-098f-3c51-91ac-77c7fbc02021 | -12.93538 | -54.7538 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30a7ff91-985d-37f1-a3c9-408c21b816f1 | -8.57016 | -51.29417 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee8c3b44-7ac3-39b3-a9fe-3c3dd8e023b4 | -11.40922 | -43.5353 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8edda4c-ecb6-3569-bfa7-481f3dcfcc37 | -11.36715 | -46.54295 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |


[Clique aqui para ver as próximas entradas](README112.md)
