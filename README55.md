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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ab4ccd1-5b91-30f8-9199-40c2a1cfcaaf | -6.85454 | -59.01986 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b48e792e-d4ba-3415-822e-4d1ef4d607c1 | -8.56861 | -54.66448 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c875d784-30a9-37d6-87d6-27f1076dcb00 | -11.18276 | -54.02606 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ad3b96e6-42fa-391a-b1a0-7e5c7aeb8a89 | -9.30789 | -56.81005 | 2026-08-20 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff6611e9-1b77-3954-b895-92695f5e7b83 | -8.49237 | -54.86968 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fbe034d-a324-3efe-9782-cdd107624df1 | -8.55614 | -54.65504 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c6621ea-fd94-3d01-b35e-63177541a7f9 | -11.21558 | -55.05283 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3216da3-4f45-327c-9e08-66649328cd6a | -11.4308 | -54.33551 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f549cca-8334-3bdb-ab3c-f7bb337c84de | -8.5025 | -54.87123 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 729eb881-2393-334a-add1-d120a20d6849 | -10.44766 | -51.80167 | 2026-08-20 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f5115d5-bb17-3ac0-bfd1-3baae2cd02b5 | -8.50022 | -54.86351 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 527d373b-7581-3786-bd00-85f18d5a511f | -9.46031 | -50.31289 | 2026-08-20 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73da8955-d333-321e-9e59-0f2ba75cc931 | -8.58688 | -54.75758 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12cd1564-cf69-3bb1-a04d-ab50a1cea59e | -8.21723 | -55.02359 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26aa3728-7fd3-3a33-8286-a76749dbcc7f | -12.25483 | -43.16083 | 2026-08-20 05:06:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7787855e-7fce-3650-9602-541a144aa043 | -11.19642 | -54.00705 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81203098-5cc6-3e5b-b4e2-951758946eb2 | -8.58752 | -54.77638 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46a1c26b-18b6-3c29-b731-8880c1207ad4 | -7.81446 | -62.32341 | 2026-08-20 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3e88cff-833d-35f3-a590-ef288a4a2deb | -12.47097 | -54.73609 | 2026-08-20 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58391d06-a855-3722-83f6-1c196bb09401 | -15.85572 | -56.08888 | 2026-08-20 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 82a5a0a2-c1f4-3f2c-adcd-43568091d414 | -21.61784 | -49.01919 | 2026-08-20 05:08:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07c0f860-b08d-3c27-a0f0-69a62ffa1329 | -19.39282 | -46.41165 | 2026-08-20 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 932ea89b-4ab2-3a67-a8f5-926a1367c8b1 | -18.79031 | -48.55167 | 2026-08-20 05:08:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5302384f-7ec5-39f6-b2e1-d6ebdb005292 | -18.04 | -44.62461 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 5a8ee9c7-fe61-3e05-8bf6-668043aaf11d | -19.6579 | -45.90959 | 2026-08-20 05:08:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9a5d9ba-7748-3dba-995a-ac59d7589064 | -18.00072 | -49.39841 | 2026-08-20 05:08:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d344ee6f-708e-364d-a119-126b2e408461 | -18.03299 | -44.62389 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| dbe98a2c-95df-3455-af5f-e85ff9be706c | -17.93864 | -44.40923 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 70f0df7d-a29c-397b-81ba-6798b45124a1 | -13.43297 | -57.06397 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e07f077-c5b1-3737-89c5-4c5b64e55b11 | -14.20278 | -52.88999 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 666c04e4-1fea-36af-8606-3d0d1d552cdf | -20.26614 | -46.74174 | 2026-08-20 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1afa62cf-264d-36da-8f46-a3bb70a98436 | -13.43905 | -57.06858 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| debdd2e9-74e7-3955-a01c-3da8274f9f5b | -14.0743 | -58.8206 | 2026-08-20 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4faa24e0-1990-3e6f-b37e-5fe2827eea0c | -14.25451 | -51.81608 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed816573-2c56-347f-bd93-406db237ca6f | -14.3392 | -51.9258 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ea1cacb-c031-3f7a-8d90-1f38a38bcd70 | -21.87237 | -46.56929 | 2026-08-20 05:08:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cc9ef48c-1cd6-3f33-83d5-4bed7d522aeb | -21.87223 | -46.56823 | 2026-08-20 05:08:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4ae0ad93-ba1b-398e-a2f6-953a38e12c51 | -20.30323 | -46.67966 | 2026-08-20 05:08:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3289a65d-9b83-3907-bde7-3116f9c99d55 | -17.94573 | -44.4099 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f3efd64a-9395-3b84-9626-b0270c2123ab | -15.36752 | -52.77829 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edf3dc25-7db9-36f0-9915-a0feeb0f8437 | -14.34657 | -51.90227 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c04b4a2d-a09c-3eb3-aaf6-612ac7f48d91 | -20.26546 | -46.75012 | 2026-08-20 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f0753cc-8493-38a2-82d0-ca68cdc243d1 | -18.55509 | -48.2958 | 2026-08-20 05:08:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e10cf87b-3e7b-30d8-aabf-4c10c8a39774 | -20.27299 | -46.73611 | 2026-08-20 05:08:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1356019-7db0-38cf-bd74-5fb955570ca8 | -14.01818 | -53.67387 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbc5ed9d-642f-3f99-b6ec-c0b50cf71d4c | -20.32421 | -47.74144 | 2026-08-20 05:08:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c066bf7-7eae-31b1-905f-0bb84a4ced73 | -15.89202 | -55.57409 | 2026-08-20 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95974b06-4cc3-314d-ab63-b44456d5e3fb | -20.27995 | -46.72907 | 2026-08-20 05:08:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 370cbdf6-cf97-34ab-8158-2666d0f69845 | -15.71272 | -47.80377 | 2026-08-20 05:08:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2850198b-fe30-3a2b-9747-0a6b45bfa12a | -14.55056 | -53.03969 | 2026-08-20 05:08:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96708ab8-8f3a-3d47-8bc1-8afd0232d8b6 | -13.87771 | -57.65884 | 2026-08-20 05:08:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efe2c8e5-5bd8-3c91-94d7-d1119e9a5075 | -15.36302 | -52.78128 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 485e1b6c-0e24-352d-a9eb-9d986135cba4 | -14.02146 | -53.65054 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94286d03-4005-3e69-9235-e38279c5fcad | -20.26276 | -46.74731 | 2026-08-20 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37b9f9ff-3289-3bef-8342-f0b567ec3a36 | -15.36797 | -52.77478 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a8c81f6-c184-37ec-bbd1-dee0ce3f252a | -20.27926 | -46.73742 | 2026-08-20 05:08:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1d6a16c6-8dab-3ae4-970e-40207aa9e79a | -15.35827 | -52.77831 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8476edb9-5f14-35fd-8ac2-747e98b8df03 | -14.02782 | -53.6326 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec01f6be-eb10-3821-a6c9-7b1301c57778 | -14.21464 | -52.89146 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d160735-e711-3336-b265-f52b2c203102 | -15.48441 | -53.05066 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 369203bf-a4f6-3bd4-b566-42293c845780 | -13.44528 | -57.07293 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e30fb53-bf35-3a5a-97e1-a02097395d30 | -14.07765 | -58.82116 | 2026-08-20 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7c2cd5d6-1d73-3f87-a891-2d228626c8ba | -14.50965 | -52.98673 | 2026-08-20 05:08:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3197295-8449-3b59-8443-a577e373dca9 | -15.58666 | -43.74137 | 2026-08-20 05:08:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 62e5bc7d-d46e-3e59-96d5-57170c72a15e | -18.55553 | -48.29153 | 2026-08-20 05:08:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0acf11f-d656-3b16-85e6-eb85eb057a13 | -15.36209 | -52.75015 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9b9a147-f9c7-3ce3-ac1d-f637e8b4ee2f | -15.26745 | -56.4848 | 2026-08-20 05:08:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 374f53c7-122e-3b0a-b119-01dc33cfed13 | -18.04057 | -44.61736 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 77129207-2bdf-3b89-a591-5503aa488a84 | -14.15429 | -52.9537 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67ac0823-1ad9-3cb8-a3eb-b1d310bdf3a4 | -15.38211 | -52.72918 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b146b8a9-b4ec-3487-87ae-8644945f106a | -20.27697 | -46.73103 | 2026-08-20 05:08:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9da0080d-5d95-3c51-bd2c-51ecb2977496 | -13.43242 | -57.06751 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82360711-6513-3e5d-97cb-f28064571ef5 | -14.35131 | -51.89882 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5aca5bd8-e1be-3205-99a1-8799e34badf9 | -14.19953 | -52.88423 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b85096a1-beb4-3521-80d1-2debcb0c7759 | -18.03357 | -44.61657 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 42.7 |
| a48bb2aa-ff55-361f-90fb-434f1c45521e | -20.26241 | -46.7512 | 2026-08-20 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bea0e7f3-2b8f-3649-84d4-175aedadcbf5 | -14.57056 | -53.15859 | 2026-08-20 05:08:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7841ddca-fbeb-3b16-a253-cc50b67a10c0 | -20.25943 | -46.74568 | 2026-08-20 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d23f486d-b57c-3d38-9716-d471f15f2942 | -15.54319 | -50.27114 | 2026-08-20 05:08:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| accc3b30-356e-31a5-bed5-73959998b459 | -14.21069 | -52.89095 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 079208a1-22a8-396a-98b9-4e3989baf47f | -14.51289 | -52.99245 | 2026-08-20 05:08:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3499a49-8f77-3600-91df-1e59b49d6d65 | -15.01605 | -52.73308 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bd18e18-8e85-3315-a4bb-79872caaf5f7 | -14.20746 | -52.88512 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1e9cbff-ce02-312a-bc7e-0a2c490546d8 | -14.0877 | -58.82284 | 2026-08-20 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61c8d587-06a0-3977-8afb-b3c6d95b7248 | -13.4486 | -57.07346 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acea3695-e4a5-3e70-8a8b-c1d5a2aa0cb8 | -14.01882 | -53.66933 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33dc0af2-b7e1-3dd6-be96-0f7f04cdfe36 | -15.36305 | -52.74919 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8299382f-65ce-3642-b7b8-7d05b0665191 | -15.36706 | -52.78181 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daac15b2-114d-304c-83a7-e5b615833a8e | -15.72173 | -53.78174 | 2026-08-20 05:08:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7375b2de-2ac5-3ec7-ab4a-a3d45418f892 | -21.87182 | -46.57378 | 2026-08-20 05:08:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2cf898ff-267d-31b2-9374-df3c5df1f46e | -15.36843 | -52.77126 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2767015-5844-3032-9164-532ef390ad8f | -15.71411 | -53.78059 | 2026-08-20 05:08:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71e36d84-833f-3390-910c-58eff86422a6 | -15.3592 | -52.77147 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78372bb7-0786-3c83-9271-724d659b178c | -15.71792 | -53.78116 | 2026-08-20 05:08:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fdea8cf-3371-303d-a5e2-24d847c42fbc | -13.43628 | -57.0645 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 045439ab-42a9-3dbc-a9f5-584bdc2ed216 | -14.15344 | -53.04864 | 2026-08-20 05:08:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02c57dcf-20ab-36e1-a23e-44679e3b971d | -14.02717 | -53.63722 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19f2a5cd-7901-3848-95cd-84b7b5155478 | -19.65838 | -45.90376 | 2026-08-20 05:08:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7cbe7138-b2ba-35ef-9b33-0d203669d067 | -14.081 | -58.82172 | 2026-08-20 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0314caf2-01eb-3acb-a232-5b342b1c4353 | -14.15498 | -52.94877 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README56.md)
