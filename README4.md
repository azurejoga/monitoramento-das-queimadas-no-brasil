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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35955b54-7b67-37a7-85cd-9b30ffd36a55 | -16.70254 | -41.51598 | 2025-11-03 04:01:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1560db1e-20d2-384a-a19c-27931f636697 | -12.24558 | -43.07884 | 2025-11-03 04:01:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 24d06fc7-76c7-3fea-b52b-090cb105749a | -8.72812 | -44.46997 | 2025-11-03 04:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8f6a72e-b2ee-3f5d-8de4-4ee8a468ca2b | -12.84927 | -43.76662 | 2025-11-03 04:01:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 666da6b2-69e9-38dc-a138-9439aa355f1a | -14.40423 | -44.37682 | 2025-11-03 04:01:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df3f9257-a536-3ba6-89a3-0b3ddb281788 | -12.39338 | -46.64594 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1beceef1-cf71-3713-a9c6-cfbf75c36f3f | -9.9373 | -44.83935 | 2025-11-03 04:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c513a7f3-a625-3c86-b0d1-7d1d859882b1 | -9.9481 | -44.91523 | 2025-11-03 04:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f08ee99-c999-3045-8716-87d4994a881c | -11.11955 | -41.09314 | 2025-11-03 04:01:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 922a29a4-1e68-305b-85ac-8d20f5401d3b | -12.40013 | -46.63153 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9b9e603-6248-3006-8e39-d680eb0c4087 | -9.86173 | -44.15236 | 2025-11-03 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8a4e9459-0353-36ad-8886-e7f35f009cf5 | -12.40107 | -46.64303 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f58b6942-d966-368a-8e91-93a29ac948b8 | -10.40672 | -44.35493 | 2025-11-03 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 73e65748-adfa-38a3-b3e8-df4b61925a89 | -10.03756 | -42.28408 | 2025-11-03 04:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 628816ab-ad45-3487-b58e-ff2d3cc576c6 | -12.85276 | -43.76722 | 2025-11-03 04:01:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14b6e99f-767d-3370-b28e-48eedcb6698b | -9.85806 | -44.15172 | 2025-11-03 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40fcbb27-ebb6-3851-a5f9-b4a721408c6b | -9.8588 | -44.14728 | 2025-11-03 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b5e56cf-2eee-311d-9a91-3ef639d2bd92 | -11.05535 | -45.33157 | 2025-11-03 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 45ed858a-ac02-3a8a-ac26-416f4ac9c846 | -9.18366 | -43.02165 | 2025-11-03 04:01:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cfe0a0b6-ee55-3df2-90ac-88f63d5a6d4a | -11.82954 | -40.49025 | 2025-11-03 04:01:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c53fe930-54c2-3a35-a7c7-54c325f4b6c7 | -15.87028 | -43.65965 | 2025-11-03 04:01:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3919a5d1-7734-3bba-80d5-a8eb744c022c | -10.72336 | -46.23671 | 2025-11-03 04:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b6b6124-4ed0-35fb-a857-2c479c1f7cc9 | -9.94031 | -44.84478 | 2025-11-03 04:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45fdaf30-1d27-303c-93a0-46a8ccabe2b3 | -9.94796 | -44.846 | 2025-11-03 04:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17bbb3a3-ca70-3de1-9da4-21aa4156ec24 | -12.33756 | -43.65335 | 2025-11-03 04:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fc93ff8-f846-3e47-83f6-852a0e9a1be3 | -13.3055 | -41.92384 | 2025-11-03 04:01:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d9c2ac2e-5a2c-3f4b-96dd-23cb200598ec | -14.97624 | -39.40479 | 2025-11-03 04:01:00 | NOAA-21 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 71eb7d3c-4723-39b4-8803-3397f4796b6e | -12.24962 | -43.0756 | 2025-11-03 04:01:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 773c7d03-c698-35cc-81eb-72ddcdaae1f4 | -12.39404 | -46.64215 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1490491c-f7a9-3a00-a6bc-8dffc6c02416 | -13.29056 | -41.93246 | 2025-11-03 04:01:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 751c91af-2192-3977-a7bd-13ed057c5edc | -10.82848 | -42.69538 | 2025-11-03 04:01:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b58c7718-6816-37cf-b515-5906c23702ef | -10.58183 | -44.56652 | 2025-11-03 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26573799-6420-3864-a402-7d1b9e05156f | -9.86247 | -44.14793 | 2025-11-03 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b58a624-63f8-328a-885e-d3ddebd44dd2 | -13.73486 | -44.23032 | 2025-11-03 04:01:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc8d73ed-e54a-3b8d-ad44-ccd644990b19 | -8.59379 | -44.15895 | 2025-11-03 04:01:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a49f495a-09ec-3d55-9768-fc7fcf6a610c | -12.24978 | -43.07518 | 2025-11-03 04:01:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f39f4315-5be0-321d-8333-2e25db4e3cb0 | -10.14586 | -36.2439 | 2025-11-03 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 13315111-ef36-34de-9bf0-a739d85ea3bc | -9.09461 | -44.32114 | 2025-11-03 04:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84b87598-a75a-3ee3-8a1d-9be328c6c113 | -9.1441 | -50.01538 | 2025-11-03 04:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fe7903d-ff71-396f-89cb-9b719c6516e8 | -12.40176 | -46.63922 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 695bdcfc-f2a7-3b42-99f7-17062feb25e6 | -9.8485 | -44.14101 | 2025-11-03 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e61c656f-84d9-3d2b-b491-8a14015a572c | -10.62347 | -44.67026 | 2025-11-03 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6536489-e7dc-3d26-9a64-bfaa32c74839 | -15.84863 | -43.63704 | 2025-11-03 04:01:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8596a360-5c0e-3e23-8d95-86c2bf517bcd | -10.62268 | -44.67495 | 2025-11-03 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ad3cf4e-4076-305a-99f4-20409a2e4840 | -12.24915 | -43.07894 | 2025-11-03 04:01:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 49b98184-031e-3bd5-9482-da135b0ef2f5 | -11.66873 | -41.68748 | 2025-11-03 04:01:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7a170869-6965-3d2e-acd3-e67a01af2c71 | -12.40313 | -46.63166 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27db8fc0-2fc1-3f21-a4ba-42ddcc395e9a | -12.48092 | -43.90675 | 2025-11-03 04:01:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3340424b-9c86-333f-bbfb-fed25ba82455 | -12.40245 | -46.63543 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2495eaac-133d-3341-8d5d-cd2ba87c88ac | -12.30246 | -42.70551 | 2025-11-03 04:01:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec3eb8a7-f9be-3826-a08c-6947a2a9e3c1 | -10.14027 | -36.24044 | 2025-11-03 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0d602f19-5adf-3527-8350-2f063b242ff3 | -10.1441 | -36.24115 | 2025-11-03 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 2af94169-91cd-326a-b407-e7a65d1b5a30 | -12.4049 | -46.6285 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 843883cc-e72f-3bb6-bff9-0a9177160ed6 | -8.50992 | -44.17062 | 2025-11-03 04:01:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fef577f1-b8c0-372c-afd1-ef40258467fe | -9.09385 | -44.32576 | 2025-11-03 04:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce9a8634-5982-3139-92ec-e9c850cb8f76 | -14.87699 | -43.55995 | 2025-11-03 04:01:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e4aecc61-46e2-33b0-a85b-e8dd54a681e8 | -14.87358 | -43.55935 | 2025-11-03 04:01:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27a1ef08-ae59-394b-97f8-f0daea14f720 | -12.39749 | -46.64671 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad88dc84-2d5a-3615-a313-7f50283d186f | -9.09592 | -44.31924 | 2025-11-03 04:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04a1d645-b5a5-34d1-94f9-025e5f24a612 | -9.92365 | -44.82722 | 2025-11-03 04:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d61279d-180e-3dc0-9842-e057f3074541 | -13.30276 | -41.91971 | 2025-11-03 04:01:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4c5d2cc7-58b7-3f35-bcf3-ea4a5f359cf2 | -13.29387 | -41.93302 | 2025-11-03 04:01:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d6df5a43-f105-359d-bd53-0d10520d92a7 | -15.78593 | -41.46504 | 2025-11-03 04:01:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7abb9e05-34c3-3abc-b38d-e31e4c550499 | -9.67895 | -37.08725 | 2025-11-03 04:01:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ef7165e5-5a24-3309-b15f-f466ca40205f | -12.64302 | -41.01012 | 2025-11-03 04:01:00 | NOAA-21 | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1955671e-cc20-35a7-bd63-176a4ffcf843 | -12.69133 | -41.56899 | 2025-11-03 04:01:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 53e45a70-4989-3720-9530-481ec86dd655 | -12.33407 | -43.65276 | 2025-11-03 04:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33c6e964-35c3-3564-8aba-8c7e97b2a5b8 | -9.85512 | -44.14664 | 2025-11-03 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88efa0d1-2120-3a5a-8ab9-9701e1d69e7e | -13.30219 | -41.92332 | 2025-11-03 04:01:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f65e8851-4da4-30f7-b970-d7227c87fca1 | -10.40598 | -44.35938 | 2025-11-03 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ff267225-eeee-3963-ae57-03d27f4e9a69 | -12.40381 | -46.62789 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6be43fe2-8107-30cd-bed8-53ea93e56744 | -12.39815 | -46.64291 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5df08350-e661-38c7-ba22-a2f307db6993 | -14.50235 | -43.85067 | 2025-11-03 04:01:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7bcd2cc5-98ff-3bbb-9d49-6ce234d6d0db | -9.91983 | -44.82657 | 2025-11-03 04:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae6679ce-525f-3f58-bbf3-98c382f14f23 | -14.5058 | -43.85126 | 2025-11-03 04:01:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae22f6e1-7bab-3a8e-b7d2-154ecab1a33f | -15.87091 | -43.65588 | 2025-11-03 04:01:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eff58a75-a900-3d95-ba71-2955005ef963 | -9.09513 | -44.32384 | 2025-11-03 04:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03aa52e6-7906-3499-a077-46f5b229f3a6 | -12.40358 | -46.63605 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 20832c51-276d-3068-801a-aa7df20f4626 | -9.85732 | -44.15616 | 2025-11-03 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4072d39a-7103-38e3-8fcc-ec89117e5ccf | -8.51367 | -44.17126 | 2025-11-03 04:01:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28d6a44e-5c5a-39c8-8765-fee4004bdef2 | -8.59753 | -44.15955 | 2025-11-03 04:01:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e55a3e75-8112-3dee-a717-cae7eac0441f | -10.42517 | -44.35165 | 2025-11-03 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9505e2d-7995-316e-9c1c-bc0012dfc888 | -11.1201 | -41.08965 | 2025-11-03 04:01:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 56106246-6656-38f5-bdfd-6d488e0c3534 | -12.05274 | -43.54996 | 2025-11-03 04:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd785e1a-bd34-3b40-9f4e-73294ce286d7 | -10.14202 | -36.24324 | 2025-11-03 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f8877d43-1806-3a82-b4e7-e0d6d077467f | -10.1427 | -36.23836 | 2025-11-03 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a82048bd-b27a-3e02-b51c-2b7818aff396 | -12.68803 | -41.56845 | 2025-11-03 04:01:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f7e63f92-2ebb-3e77-8aac-20483e25f176 | -9.93687 | -44.17353 | 2025-11-03 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96abbaf5-9183-3787-a24a-abb67332d383 | -13.6824 | -40.68822 | 2025-11-03 04:01:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 96787642-0ceb-358b-8a32-e5196ccb75f9 | -11.05921 | -45.33229 | 2025-11-03 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4c4f4ac-8916-3df8-b58e-eac6ffc081f8 | -11.06005 | -45.32737 | 2025-11-03 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8f20b5f-53a1-3ecd-8e1a-e9462c67e4c7 | -15.55834 | -40.84141 | 2025-11-03 04:01:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0f9a0374-dbfb-38e7-abcf-fd0baacbb783 | -11.01169 | -42.73648 | 2025-11-03 04:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 78f7e767-832e-3296-a3f9-6d477c031d2a | -11.11625 | -41.09261 | 2025-11-03 04:01:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 972ec974-2304-30aa-a8aa-271b0909fac4 | -13.38891 | -41.32988 | 2025-11-03 04:01:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 642beb76-4195-3807-a9f6-e83e820be39b | -11.17849 | -40.95922 | 2025-11-03 04:01:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 224d6168-c71b-3305-859c-4a679f3ad323 | -9.94333 | -44.85013 | 2025-11-03 04:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b513b58d-1b6a-3d34-bbe7-b8c4545548f7 | -12.37472 | -43.69624 | 2025-11-03 04:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d52b616-9bcc-3309-8141-3524c1f6c18c | -13.00038 | -43.64215 | 2025-11-03 04:01:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00164f0d-f8bc-32d3-baeb-4917d17eb21d | -10.42807 | -44.35687 | 2025-11-03 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README5.md)
