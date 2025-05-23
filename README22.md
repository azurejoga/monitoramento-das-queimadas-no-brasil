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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e70a069e-2c6c-344c-987b-c5e6172294d7 | -8.77844 | -47.9489 | 2025-05-23 12:42:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7b7aaac9-170d-3f76-aa2e-5e87ef83c7ca | -10.89542 | -47.22094 | 2025-05-23 12:42:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 69d85544-78cf-3aec-b50b-91fb42adfde5 | -12.38149 | -49.99433 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d0c41758-53cb-383c-91a7-d26c7c8351e7 | -11.45413 | -47.86377 | 2025-05-23 12:42:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5b40320a-6c2d-3615-b71c-9ec5943241f7 | -7.65935 | -46.09693 | 2025-05-23 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b65b06c0-8824-3ab8-b20d-9f1295498646 | -12.35294 | -49.93196 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 287.2 |
| 237ed2e1-3b95-33ff-9d10-ee40398dce18 | -12.39058 | -49.99562 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 869103a5-ebae-3ee6-93a7-e5eedde5dfc5 | -7.80561 | -46.21173 | 2025-05-23 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8e7e3ac3-f00a-3190-ac96-5322b1353309 | -10.32805 | -46.64335 | 2025-05-23 12:42:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| b47dc0a9-962f-39f4-9f11-b25ab64b9234 | -13.78883 | -54.31046 | 2025-05-23 12:42:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 365a7534-5e15-377e-8ce6-96f0c0816de8 | -10.50742 | -42.41558 | 2025-05-23 12:42:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 116.1 |
| 232481a4-ed82-3f28-b6e0-4662d55d8da9 | -12.96839 | -57.80586 | 2025-05-23 12:42:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ec99e322-41f4-3ba6-b480-40669286e319 | -11.90016 | -46.79314 | 2025-05-23 12:42:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 7e73a0f1-3f85-33c2-839a-ef8720d769b7 | -13.47421 | -52.2818 | 2025-05-23 12:42:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 7efa855f-911c-3711-ac5c-8e38942be347 | -10.23577 | -47.43341 | 2025-05-23 12:42:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e5fdec2b-ddf1-3ed7-8506-340662853dc7 | -12.41145 | -49.97908 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 0bcf9d45-2ea4-35c9-a478-8a3195ee4a64 | -12.39323 | -49.97658 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| c3c14032-bea2-3d48-bec6-10122e29d4a6 | -10.23739 | -47.42119 | 2025-05-23 12:42:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 83303ff0-c20c-3a72-905c-98973a82cc05 | -7.80384 | -46.22518 | 2025-05-23 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 53e6bc51-e9d1-3922-a14c-52cd8a16e101 | -13.47554 | -52.27266 | 2025-05-23 12:42:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| d4c44a59-6d24-3419-8912-319e098df735 | -12.35163 | -49.94154 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f2297852-cd8a-327d-89ba-661ebd3e0d61 | -12.35426 | -49.92234 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 9c3d6a5a-9df3-377f-b578-014444eda8d2 | -12.30032 | -52.49113 | 2025-05-23 12:42:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6e31f66e-7e05-3ace-9b04-5609c87c0a70 | -9.03329 | -46.80883 | 2025-05-23 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bda7affd-3d71-389d-a52e-c2ba3c2321e9 | -12.36338 | -49.92361 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| f16534c6-c0c7-37c3-bf18-18032da54aa3 | -14.0289 | -55.14266 | 2025-05-23 12:42:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| df25d2e5-2205-31ad-9763-c211497fa7e2 | -14.23668 | -54.27241 | 2025-05-23 12:42:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 939938fa-b840-3ddf-983c-02523808f1c6 | -12.29895 | -52.5004 | 2025-05-23 12:42:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0555d78a-d5b3-370d-9330-063897410634 | -9.57261 | -50.50717 | 2025-05-23 12:42:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 08fa8831-1cc5-3380-93c2-459c450c927f | -12.3919 | -49.98612 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 9a96c266-f23d-33b4-80c3-4a2e9c62aecf | -13.98465 | -56.00576 | 2025-05-23 12:42:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 36.4 |
| e502917e-576c-3dd3-a6ca-e793dc25860d | -8.75214 | -44.93098 | 2025-05-23 12:42:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| e216c965-e4fe-321c-955c-aaf63659d96b | -12.42056 | -49.98035 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d155202e-2b74-3e5c-a412-d2062a5e90b4 | -12.37082 | -47.32422 | 2025-05-23 12:42:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 31270bac-ea95-30f8-b0d0-04fae04bc79d | -7.75761 | -47.04207 | 2025-05-23 12:42:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e2b5c864-9083-30ba-aa1a-e4076b5d850e | -12.29135 | -52.48979 | 2025-05-23 12:42:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 23c5cb29-7510-3359-b43a-bcf4dada74b7 | -11.79719 | -44.27734 | 2025-05-23 12:42:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 365ce3d1-ea9d-334e-bb73-8dd24086ed52 | -14.69874 | -45.3721 | 2025-05-23 12:42:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1809e7d4-d74a-30dc-9109-26595d22fd76 | -12.36207 | -49.93322 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c71209de-cd5d-33fa-8f15-120afa4f5cbd | -11.91856 | -54.40602 | 2025-05-23 12:42:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2580d40d-3976-337b-8b0e-e860c9c5a8a9 | -14.23831 | -54.2619 | 2025-05-23 12:42:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f5a9b93b-77c1-3ccf-9c24-af3b71235c21 | -12.07122 | -47.3475 | 2025-05-23 12:42:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| eaad8fc9-8c5c-30a3-8294-e5bd34ad4afd | -9.56246 | -50.51485 | 2025-05-23 12:42:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 135663d3-d517-3668-b191-0fcfbf35cc0c | -9.29034 | -48.31405 | 2025-05-23 12:42:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 27d7ac4f-de6d-327d-b5cd-035614431713 | -9.56374 | -50.50592 | 2025-05-23 12:42:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c3b36f1b-04d5-3792-8d86-872aa20268e9 | -12.28998 | -52.49906 | 2025-05-23 12:42:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 66967386-148c-338d-bfe8-d8624440d711 | -12.38413 | -49.97529 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 54b496ba-b537-3277-afda-0931f53d8a4e | -9.03498 | -46.79602 | 2025-05-23 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 46cea93f-3395-3046-a7fd-6835d9f5a2e7 | -11.79204 | -44.28343 | 2025-05-23 12:42:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 8b5798d2-1464-3adc-804a-9c6ec508a6c9 | -8.74978 | -49.75066 | 2025-05-23 12:42:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 022e562d-e819-3af0-8289-d75ecfe22036 | -14.0547 | -45.53496 | 2025-05-23 12:42:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b20d5312-ff36-3057-b02b-a3c79ec322a2 | -14.88402 | -45.10785 | 2025-05-23 12:42:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 09c6b1c7-e98a-3a4a-b7fa-297986bec026 | -12.41012 | -49.98864 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| b16a46bb-bdbc-3cf6-863c-654d1e657e52 | -11.80584 | -57.34694 | 2025-05-23 12:42:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| a6e374f9-277b-3f1d-9587-0d0e3648f458 | -12.37574 | -52.48051 | 2025-05-23 12:42:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3468d720-233f-333f-bb6b-18bfd257e436 | -13.18138 | -53.57589 | 2025-05-23 12:42:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 873d2372-bc9f-3f26-8985-e2ea8c78e557 | -14.0418 | -53.37435 | 2025-05-23 12:42:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 55a6361e-a561-32bc-9264-44126d525166 | -7.80208 | -46.23863 | 2025-05-23 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a475e1ae-c2f8-3847-9fe7-cb16f8260a94 | -17.28186 | -47.00937 | 2025-05-23 12:44:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| be88267d-cf45-3ebb-8767-b70a7a9f219a | -20.85766 | -53.7483 | 2025-05-23 12:44:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a97451e8-6d0a-3546-8f6a-556289860bf1 | -19.96193 | -45.84007 | 2025-05-23 12:44:00 | TERRA_M-T | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 930a04be-8509-3b31-b699-f05a8642393f | -18.42736 | -54.69482 | 2025-05-23 12:44:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7ff8bc96-1dc0-30ef-9e76-8878bc13eeda | -19.95909 | -45.82283 | 2025-05-23 12:44:00 | TERRA_M-T | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 45b07d50-c4c3-3e98-9fc3-fbbbca17e055 | -21.42255 | -46.63119 | 2025-05-23 12:44:00 | TERRA_M-T | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 3d7c15a6-b395-39c6-bb04-16b60184d292 | -18.3392 | -45.59777 | 2025-05-23 12:44:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1a0b2d79-c87f-3bd6-9afd-2566bb08c91c | -18.35489 | -55.1622 | 2025-05-23 12:44:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a424ab52-138e-3f9e-a575-9ac09842b262 | -21.4236 | -46.62562 | 2025-05-23 12:44:00 | TERRA_M-T | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 207821f5-9a30-3e64-a43e-a87dc015b14a | -17.26814 | -48.6208 | 2025-05-23 12:44:00 | TERRA_M-T | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d6156276-a854-3200-8729-527bd0bef5f1 | -19.96436 | -45.81688 | 2025-05-23 12:44:00 | TERRA_M-T | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| fd7612ab-ada5-3e12-a9c4-6900b259c486 | -18.34283 | -49.86956 | 2025-05-23 12:44:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 127d31db-dddb-3006-b9d6-5c105426fb57 | -15.26871 | -51.4753 | 2025-05-23 12:44:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8d4e1307-63c5-38d1-b9f7-7245ed5219b1 | -18.34427 | -49.85822 | 2025-05-23 12:44:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1613a88d-f16c-3bff-bd6b-1c828558e0ce | -12.4086 | -49.9978 | 2025-05-23 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 20319138-9906-35d1-9bde-fc8d1da2cd40 | -12.3898 | -49.9786 | 2025-05-23 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 433.6 |
| aeb3e797-bfbd-3fe0-a6e0-41eb51eb14a6 | -6.2224 | -43.3693 | 2025-05-23 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| c5f654bb-a648-3881-acdb-63e79d9b7f51 | -10.4922 | -42.409 | 2025-05-23 12:50:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 119.9 |
| 810d00b9-60e7-37f3-a255-0e447c26fbf7 | -6.9427 | -42.789 | 2025-05-23 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| a8f1e015-5555-3406-91a6-c2c6829fe490 | -6.2409 | -43.3911 | 2025-05-23 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| aed34186-cb92-37ce-a25b-eedbeedc9cb2 | -6.2411 | -43.3677 | 2025-05-23 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 355d015e-2508-38a8-91d4-85701b695d2d | -12.4089 | -49.9762 | 2025-05-23 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 298.2 |
| 7d80922b-e2dd-315f-8b66-d72db8a35f01 | -12.3522 | -49.94 | 2025-05-23 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 69b5fb9d-f346-3e04-b937-dd4c130ed248 | -11.8156 | -57.3612 | 2025-05-23 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 50d46ab3-ca78-32ef-b38e-6156e53803c8 | -6.2411 | -43.3677 | 2025-05-23 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 1a6564fb-280d-33e6-b983-0417f91f54f3 | -12.4089 | -49.9762 | 2025-05-23 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 396.3 |
| dcd856eb-66af-3955-b5f8-80831835b9d1 | -12.3898 | -49.9786 | 2025-05-23 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 741.9 |
| 35a8da51-2d9e-3915-bbd5-630097a12b44 | -10.4922 | -42.409 | 2025-05-23 13:00:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 90.7 |
| f8e06cb4-c682-3960-960a-e45a7bae3fe6 | -6.9427 | -42.789 | 2025-05-23 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 1d4e39ff-157c-3197-8396-d299506d91ff | -7.8063 | -46.222 | 2025-05-23 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 7751a1d0-ae84-3649-ab83-2e6ecf2d3c1e | -12.3522 | -49.94 | 2025-05-23 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 1a67572a-c2d5-3fc7-a393-942b4e7de65b | -10.4922 | -42.409 | 2025-05-23 13:10:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 0cfecc7a-0ad8-3ee8-8eb5-304d266b0782 | -6.9427 | -42.789 | 2025-05-23 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| d0481e9d-8b57-3124-8c1a-44b02a25a552 | -7.8063 | -46.222 | 2025-05-23 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3e4f7d3a-7391-3b98-942d-a0f8a3505c9f | -6.9424 | -42.8126 | 2025-05-23 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 6255eb88-63d8-311e-b898-17473c748959 | -12.4089 | -49.9762 | 2025-05-23 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 326.1 |
| 65f00504-237e-39dd-a5aa-0dc083b69d3a | -6.2409 | -43.3911 | 2025-05-23 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| eb05f674-fc54-3e5f-9cab-98d1759488e6 | -12.3522 | -49.94 | 2025-05-23 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 279.0 |
| 0cd8f844-5636-3d00-b706-3e3e438139ba | -6.2224 | -43.3693 | 2025-05-23 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 189.5 |
| fd92d738-a7f3-301f-ae0f-7720bcbb67f1 | -7.8063 | -46.222 | 2025-05-23 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 6ddabd86-e94d-32ea-8176-674eee4b75e4 | -12.3522 | -49.94 | 2025-05-23 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 306.4 |
| 7a5220be-463f-345b-bb03-687b66670488 | -6.2226 | -43.3459 | 2025-05-23 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |


[Clique aqui para ver as próximas entradas](README23.md)
