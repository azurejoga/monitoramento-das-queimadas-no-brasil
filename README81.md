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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e884f031-808f-3bc9-a022-d07408515822 | -14.16655 | -46.15971 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d548b765-9621-3f3d-9e45-e893e79fd15d | -10.70433 | -50.49539 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e20024b0-e8a0-3d55-88b5-d15a94b44d2e | -12.56562 | -45.67165 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b40ac341-c8aa-3b85-80bf-c042b17a53b7 | -11.19152 | -51.42687 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| fda40025-11d5-32c8-8c91-661b9b3e9795 | -14.3002 | -46.06978 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5c72e0a-a961-3377-b647-574bbf0941c6 | -9.49058 | -55.9664 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33498fc4-5daf-33b2-8cde-3b7f9bddcb25 | -14.21852 | -46.24494 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87004f14-1ad1-3991-bc1d-60e98c99dd51 | -15.16815 | -52.48467 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7af21b76-8d93-3939-a7c2-a51a45728bb1 | -15.21937 | -56.68872 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb7be42e-b706-35ac-a93e-e177a463c602 | -15.21986 | -53.81142 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 048ec490-bde2-3155-85b1-2727d14023ce | -14.45992 | -47.35041 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ce92555-ffe8-3d7b-a8e4-ce4636b8e7c1 | -9.26393 | -59.40932 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 85c080f6-be0b-3eb8-9a6a-a439eb026a01 | -12.91883 | -54.74746 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77a2aa64-ad96-3cfa-b447-c5ba028ce2c9 | -11.10322 | -51.44934 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 659507ab-e29c-34b7-a3fe-9addd570039a | -10.66283 | -48.66784 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd6f0975-577b-3e8f-9672-0c287752e571 | -11.57011 | -50.57589 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5320273e-9e3e-3343-9487-a51a4c335d6f | -12.1318 | -44.84648 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcfbafb1-112d-3289-860c-93ecb05f3499 | -13.00379 | -46.75265 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90b8e054-70f9-3062-9b41-0221925231c2 | -14.28731 | -46.0831 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a7825e83-b572-366e-ad79-04bc2388cb35 | -9.80714 | -61.51974 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2499f7e-cf00-345e-b91b-aab18a418630 | -9.27634 | -59.40638 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ede3eacf-f332-3418-82d3-1db0de60e25e | -9.50388 | -55.96854 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6308b3d1-8ef1-3b02-9dd9-47d270e5634b | -11.65814 | -52.24471 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 411ea26e-fc06-3333-9d70-60039d0c530c | -11.10012 | -51.44416 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| bea966b9-509c-3e7f-a644-b05f95b5d93c | -15.87152 | -49.94793 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 697c582d-a686-3fd6-8b7c-fee0e8da628d | -15.23862 | -51.39941 | 2025-09-13 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d598e675-3e03-3ff7-866d-831691dde2b6 | -14.19208 | -46.27888 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| a64e8d8c-dd9f-331c-b353-705a48f7813a | -12.09431 | -44.87199 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ebff54dc-a608-35b9-ac7e-00134847b6bd | -14.20464 | -46.26674 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00776636-e3c1-34ab-9907-9345c7797128 | -16.43163 | -49.04701 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ef35f15b-98ad-35c2-b478-2011b5f2208c | -15.248 | -51.38995 | 2025-09-13 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 98978522-8dfc-3e72-aa4f-fb94665b97f5 | -10.53886 | -57.10522 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00a9db6b-0b91-3fac-a2ce-72caf202ff6f | -12.89261 | -62.08898 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5928302-f7ce-39d3-a9f3-5feecf26521f | -11.39703 | -50.47192 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6a1052b1-79b9-33a2-a601-74c1b1b3fd84 | -12.2765 | -53.91808 | 2025-09-13 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bc0e244-4f4a-3210-9a08-82753b21d08c | -9.20285 | -60.62642 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c4f4a11-7652-3739-9dba-814d554691eb | -15.66923 | -54.35559 | 2025-09-13 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c7669e0-2b83-3bf9-9c59-07e56b469c9a | -14.18745 | -46.27063 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e56682ee-f09f-3d78-bfc8-d04ebc127920 | -15.10009 | -51.15873 | 2025-09-13 04:59:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8857ec1c-264f-3c9a-a177-9ec40ca71bed | -11.14 | -50.70267 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 6fd01932-59a0-3f2b-9f18-560d45f1a667 | -12.96443 | -54.73988 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30a73550-60c9-3418-b905-684792b24bb0 | -11.85138 | -50.56208 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d4d191f-f0bf-341c-bea9-fffc405cf5db | -13.1151 | -56.80166 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3d5284d-3a39-3745-b874-022bb1c0ffa1 | -14.28817 | -46.07564 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2b29e616-0430-343a-a8ee-e78e0878c871 | -11.4591 | -48.70871 | 2025-09-13 04:59:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0861fe1b-2b5e-3785-8666-35c6b9d4ccf1 | -12.83398 | -47.91788 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 40cfb4c7-5217-3da5-8834-b64d220baf5e | -10.54068 | -57.09409 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9135e013-8ae0-3950-9d46-25451ebe011b | -14.18245 | -46.26541 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 6a33682f-3b6d-3c28-a835-f9b4798f3624 | -14.19565 | -46.2485 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1299875d-094b-3a40-8fe0-5f74926f506a | -12.94061 | -47.99975 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 69b8f821-51a4-3cd0-912d-6ecb5b335d7e | -11.57361 | -50.57998 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60cdcfb2-8aa5-3b49-9bf3-3e7e6aabc285 | -15.82244 | -52.21417 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cb1b121-3f37-3f0b-8058-3e377c5592f5 | -12.85052 | -47.93325 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bcbf3862-91d7-3893-9c1f-aeaa7a61b1d8 | -15.59119 | -54.76875 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c29dea33-b2ce-3c4d-8543-6c4d931c4f05 | -14.73552 | -60.23554 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7a7b5f8-8caf-38d7-8665-37b2f37fb78a | -16.40452 | -49.03302 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c660ac65-a6ba-321e-9710-510724cf291f | -11.18841 | -51.42166 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| af0c13b7-95bd-3d6b-a53a-9445bd520afb | -10.50278 | -51.52773 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8afb2725-158b-3541-948c-5cd8d5d93b7c | -11.18714 | -48.3535 | 2025-09-13 04:59:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c781cef2-9db2-3109-81ab-779c7ee10208 | -14.41391 | -46.39963 | 2025-09-13 04:59:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4357ad19-6705-3b89-90cd-0f81145df2a0 | -12.83247 | -47.91946 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d7ad9254-fc03-3bf0-907a-6cccd1ae5e37 | -10.44565 | -50.62643 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e1f0a58-d7fe-3a26-a61f-133c4cb00568 | -14.21341 | -46.24064 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06df7423-319b-34a1-bbaf-1f4792c73739 | -14.21334 | -46.23869 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09b1a2ef-5265-3d4b-8642-7421869e4c0d | -12.56609 | -45.66772 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f06b2b1-3249-3832-856f-7e1ab08641a1 | -12.92939 | -54.74543 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b006e6a-74a5-3fa4-86da-b93484190320 | -11.57109 | -50.56889 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 94e39b12-0ff1-3159-a287-f090ef8fb2c0 | -15.23209 | -53.75159 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daaf58ce-4f85-3300-bd84-7efc846f600c | -10.33309 | -58.01922 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 096f0a79-a714-38c7-9414-395dd96912d6 | -15.78614 | -52.25904 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9affac4-afea-39eb-a9de-ab60d0c9599e | -11.55066 | -50.56947 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca8d719a-09b8-3ed1-97a8-4f8c1c660567 | -10.77556 | -50.52901 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3bcfdb6f-696a-3b0a-a5f1-fddaba85c462 | -9.49779 | -55.96394 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 816ca861-0977-37c2-95dc-57ef13442ef9 | -10.50383 | -51.54634 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 066d65b4-7738-3e29-b97c-59b6d094ca82 | -9.98186 | -55.05312 | 2025-09-13 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fea44f97-9184-3c12-a861-b57d93b90cfa | -15.25126 | -51.3959 | 2025-09-13 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c41478de-b506-3033-a4a9-5c60e6cce975 | -16.43238 | -49.05295 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 788bdc1e-9b58-3c89-a72f-b61ffb2521a8 | -10.39746 | -60.81185 | 2025-09-13 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5051b802-c6ad-3d96-a138-b4a221589f3f | -14.20178 | -46.24173 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43c411ea-4d15-3cff-b004-cac2f79997d1 | -10.90256 | -47.22421 | 2025-09-13 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b0d9d229-46b7-3431-bf5f-ff8d45004a17 | -10.66409 | -65.19845 | 2025-09-13 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32244517-1a2d-3782-920f-0af78a1e0c99 | -9.26106 | -59.41634 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fcec697-fb24-3435-bf47-390a9fb4088d | -12.76671 | -47.16292 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f556129-cd86-3bc6-98cc-05ece4a5c2ff | -10.51068 | -51.5513 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b9525a08-3bc9-3656-8c1b-9591dd56ca62 | -14.19824 | -46.27398 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bd3c879-b364-370d-a68e-340b9a73eb69 | -16.28429 | -45.68308 | 2025-09-13 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9f37754c-8da2-3609-93ef-226f9067aa82 | -11.23151 | -54.99932 | 2025-09-13 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50d350d2-0e53-3a86-933b-cd93a3819036 | -12.10858 | -44.85251 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 839612e8-9454-3c40-855b-aae0fe1a353c | -13.13822 | -47.13247 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e108df9-f7fa-30a4-9abe-f3b0c42ff448 | -14.41936 | -46.40066 | 2025-09-13 04:59:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcce85c3-d58f-366b-bca7-5113da4816c3 | -10.51266 | -51.53791 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c2bdf6d-6b53-3682-b063-66468c7da191 | -15.16571 | -52.47466 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a8a5fd35-c0f6-3d72-a19c-be25359aa678 | -11.84432 | -50.55381 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe5b1c60-3d59-3702-877a-70d801cc23b3 | -10.78671 | -50.53592 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5acf5de9-0ee3-338f-a249-8fba05e7341b | -11.9325 | -51.1349 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 22d78149-27ad-3577-990d-9b78139465fb | -10.66481 | -65.19471 | 2025-09-13 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d67ff8c1-7841-3b87-80d2-f86ec4edc20d | -10.37145 | -50.49902 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b80b5b05-59d5-381d-889a-7c11868694aa | -14.22831 | -46.30524 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| dca9ea17-4410-357c-a14f-6a5dfe7448f4 | -12.95408 | -48.00195 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d7a98854-a7b7-3acf-8d7c-967a7101ea94 | -9.26779 | -59.40996 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |


[Clique aqui para ver as próximas entradas](README82.md)
