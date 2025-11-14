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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 436d1ba3-1827-3b1a-b312-193dd3a55c25 | -15.556 | -44.488098 | 2025-11-14 00:38:00 | METOP-C | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| c2c945f6-f3aa-395c-9206-c02f3dfd8582 | -4.6986 | -46.4506 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e61f5eb-0692-38af-9949-5755596be5dd | -10.7519 | -44.918098 | 2025-11-14 00:38:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4752281d-8d1d-3bb8-ac2a-f7de51e927fb | -3.3508 | -46.867802 | 2025-11-14 00:38:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 288b9546-2d74-3a3e-b59b-2b57da2f2769 | -3.5131 | -45.564201 | 2025-11-14 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a762aa4-56e6-3b5e-beae-06f3bb1ae8cd | -17.792801 | -44.986198 | 2025-11-14 00:38:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 308bdaa6-c32f-38c6-aa70-4193aa949710 | -11.6661 | -48.461899 | 2025-11-14 00:38:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b6beb37-9d10-39f2-b5d6-5a5b11e14ba6 | -11.9922 | -44.215199 | 2025-11-14 00:38:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| de343e70-9ff8-3da3-9dc8-b1c19e8ad9e3 | -4.9574 | -47.709301 | 2025-11-14 00:38:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa19e6e1-2bf3-3044-ae54-feea9e1e6592 | -7.8391 | -44.2971 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ab032bf-0265-3f01-aad9-3d7e1a8329b4 | -6.2395 | -46.243099 | 2025-11-14 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6cb45276-fa0e-3c27-bcaf-f83882c00db5 | -7.1478 | -46.289299 | 2025-11-14 00:38:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31c79dbc-2481-3307-8d10-9d83a782c171 | -12.6935 | -45.415501 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c0b6f24-4283-33c3-bf0e-9ae01d29a856 | -11.9887 | -44.287998 | 2025-11-14 00:38:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb92ada-a87c-3d93-8b4a-e5a62b2f830c | -2.1178 | -45.372101 | 2025-11-14 00:38:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0065730-8779-3f3a-be47-9da0dfaad43a | -5.588 | -45.172298 | 2025-11-14 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8555514-703a-3367-b456-198c45df28a4 | -14.673 | -46.5648 | 2025-11-14 00:38:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dfd55d8b-a5b3-36a8-b618-5624b91fc5eb | -2.8051 | -45.490898 | 2025-11-14 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52f93fa8-6fd8-35de-b504-331793adebf4 | -6.2899 | -46.953899 | 2025-11-14 00:38:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff798e81-5809-368c-9602-1f51e9a7c93c | -7.4699 | -42.5723 | 2025-11-14 00:38:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2745c28e-f2f9-3073-8822-9bfa2c78dba5 | -7.9346 | -44.351601 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 589b3435-ac5d-3938-b0ba-19220251c370 | -5.3473 | -46.757801 | 2025-11-14 00:38:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7be32205-51d4-31f9-b37b-3fd62fbc250d | -7.1553 | -41.2719 | 2025-11-14 00:38:00 | METOP-C | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e25b9083-142b-3471-82fd-b199d159fae3 | -5.5529 | -47.3377 | 2025-11-14 00:38:00 | METOP-C | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9f477ea-ca6d-3f88-a0ec-cf6bd631cbab | -4.7213 | -42.937599 | 2025-11-14 00:38:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eeca4ab2-9e18-3c65-a15b-e6c0455872ec | -1.8332 | -53.8055 | 2025-11-14 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f9702cc-ba21-3c80-9d8b-a27698f893a9 | -12.1461 | -48.026299 | 2025-11-14 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ff93e7c-e10f-3104-ad03-fa111bb7c2ad | -2.8831 | -45.2939 | 2025-11-14 00:38:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0a77665-523d-3ccd-9b3a-0f2477ac974a | -4.1101 | -50.052799 | 2025-11-14 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8aba71d-3cc1-3bc1-af1b-365459c9c3f5 | -9.1089 | -43.946098 | 2025-11-14 00:38:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a0ccf6e0-1040-396f-83a4-c972e33b441a | -7.3576 | -43.354401 | 2025-11-14 00:38:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2abb5458-d6ba-3389-8e72-8e9fe6cae9a7 | -1.8307 | -53.7948 | 2025-11-14 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3161550-b3ca-3eee-a890-fbcc86028b79 | -12.6869 | -45.431999 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2727857-97b2-3976-8351-1581c444f890 | -6.4841 | -43.761101 | 2025-11-14 00:38:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dbbf4a0-52b4-3873-8196-83164df1df13 | -4.5228 | -45.603699 | 2025-11-14 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4133c62e-7288-308b-8f23-050ab383ddb5 | -1.4923 | -47.8004 | 2025-11-14 00:38:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d9e84e3-32d0-38a3-a604-a6b1717c3b6a | -9.679 | -47.897301 | 2025-11-14 00:38:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15a131ca-1a6b-3a80-850c-46cc901f67bc | -14.308 | -44.5816 | 2025-11-14 00:38:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b9eae1d-df00-3b26-b694-636ae0357f57 | -6.6887 | -47.7952 | 2025-11-14 00:38:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f6832a2-c2ea-3171-8fdd-8c00f7f4bd13 | -0.8632 | -47.306599 | 2025-11-14 00:38:00 | METOP-C | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9725ee0-8532-3722-be76-8a0684154eb2 | -4.71 | -46.455601 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 956a55bd-2982-3771-9d4e-ae428ffd8a55 | -3.6595 | -45.928398 | 2025-11-14 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13bba0e5-6b04-399f-9885-3b322fdc1f43 | -7.8372 | -44.288898 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74561ca3-9a31-3218-b929-7fa4b3eb094b | -2.9612 | -45.763599 | 2025-11-14 00:38:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 539e8ee5-ace3-348a-aa64-ac8d3fa18f16 | -12.4024 | -48.117199 | 2025-11-14 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe5080e1-e48e-3143-8121-3779288f1c07 | -5.4567 | -47.098701 | 2025-11-14 00:38:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afcc39a7-0335-38c8-8be9-12e626c8294f | -3.8018 | -45.0326 | 2025-11-14 00:38:00 | METOP-C | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e0b9509-de78-3270-adde-b93972d9f786 | -17.9834 | -42.9244 | 2025-11-14 00:38:00 | METOP-C | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eb03d6ef-ae9f-36bc-bef5-f641979ff1a1 | -4.1095 | -48.014198 | 2025-11-14 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d574e675-9c46-3ec6-9537-d123eb9c22d5 | -11.8425 | -49.224998 | 2025-11-14 00:38:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ee29bd1-1437-3d29-aef0-63bcb844aada | -12.7065 | -45.427399 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c940850-2a4b-3f68-b31d-86e40d120d6a | -7.9368 | -44.317001 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3e4f7721-d37f-39cd-b704-866d3422b7db | -9.6642 | -43.891998 | 2025-11-14 00:38:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 720233bc-bdb4-3172-84bf-431bad9cb7ec | -3.4625 | -50.103802 | 2025-11-14 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 601a4e9d-37fa-3023-a987-9a4217301677 | -2.7921 | -52.9604 | 2025-11-14 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a72de58-081e-302e-a866-2b301811b0e0 | -12.7131 | -45.4109 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 701082d5-8eb4-318a-83d1-018b78727c5a | -15.3835 | -48.962502 | 2025-11-14 00:38:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c27f3558-ca50-3e43-8d34-360cd7478bda | -9.6414 | -40.3475 | 2025-11-14 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aef8c9cd-5fe8-3b42-a760-12e2784d09b3 | -10.7527 | -45.010502 | 2025-11-14 00:38:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6def2155-34ab-3ef9-ab60-cc51dee532eb | -7.7894 | -49.618999 | 2025-11-14 00:38:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d7ccbd7-6ccc-3dc2-a3c9-39f5df008463 | -7.884 | -44.312199 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18bb57c2-22a4-36e8-b914-1189624a8faf | -11.9869 | -44.280499 | 2025-11-14 00:38:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34b4bb7a-91c0-3353-af6a-b7bc1d3373af | -15.3932 | -48.9604 | 2025-11-14 00:38:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4793adc8-83f3-31ce-99b4-7568a3504150 | -13.3311 | -43.187698 | 2025-11-14 00:38:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c3414dc9-6342-3ce2-ae94-84d7d22e18ff | -3.2882 | -52.1077 | 2025-11-14 00:38:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c5359b8-d6bd-3308-8698-f6fbe9df5df3 | -4.0752 | -44.1301 | 2025-11-14 00:38:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99920607-dcf9-3d20-a636-44b4341769d8 | -6.854 | -46.760502 | 2025-11-14 00:38:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4a7732b-d52e-37d0-841c-58ffa27c7494 | -11.7333 | -48.534302 | 2025-11-14 00:38:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c21eb2ea-b40e-371f-97ea-d223904fa16b | -4.4607 | -45.381302 | 2025-11-14 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1ed709f-dc31-3afa-b1c7-c9312cbcc5c9 | -6.4293 | -47.291599 | 2025-11-14 00:38:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ac1b709-8cdf-35e9-9cf5-a465edcc7c71 | -3.7581 | -47.7411 | 2025-11-14 00:38:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12bb8b6a-b14e-3b0e-8044-038e8645f404 | -11.7317 | -48.526699 | 2025-11-14 00:38:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9dfc005-0ac9-331b-b552-56394f3c77a2 | -12.6983 | -45.436699 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1dd6b7e-baab-32ac-8049-884da0342f45 | -3.4493 | -44.538601 | 2025-11-14 00:38:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11a11f54-9d2c-3717-8e31-f42c56586245 | -6.102 | -41.604 | 2025-11-14 00:38:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 43ad0196-e5d3-360f-95e4-2f93bd437938 | -7.7877 | -49.611301 | 2025-11-14 00:38:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8adb0f21-81c7-377e-8249-a41fab6823d6 | -12.0084 | -46.7589 | 2025-11-14 00:38:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2eb948b3-7d23-377e-802a-58b5eb1c1103 | -1.8283 | -53.7841 | 2025-11-14 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5605445-be9c-388b-9523-7d9b5fa625f2 | -6.4435 | -45.6549 | 2025-11-14 00:38:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db529b8d-7c8e-3327-acf0-9aa388c9f81f | -7.0469 | -45.056 | 2025-11-14 00:38:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c484fa23-a646-3c37-9f78-67c2cdd69d46 | -3.992 | -47.188499 | 2025-11-14 00:38:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44640502-5c82-3c81-b8a6-513185eee576 | -1.4939 | -47.807301 | 2025-11-14 00:38:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dedc90ea-5c86-3654-ba1b-58083634116a | -4.0453 | -46.124298 | 2025-11-14 00:38:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f86019e-10e6-375c-b278-eceb2028f5a4 | -12.1428 | -48.0116 | 2025-11-14 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 683796cd-8521-361a-8825-f4e13dff16c0 | -5.4551 | -47.091801 | 2025-11-14 00:38:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4bb0cfb-ff1c-3a3d-9929-d03aba581f41 | -15.3817 | -48.9538 | 2025-11-14 00:38:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 514e3bb8-62eb-3ade-acde-acf11d587bec | -12.6638 | -46.741901 | 2025-11-14 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9812491-09f6-36e0-bc7e-a16dda58ade1 | -6.455 | -45.66 | 2025-11-14 00:38:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 208eec25-81d9-3879-b6f5-affba76d78e1 | -6.1089 | -41.589401 | 2025-11-14 00:38:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e35d4c2a-44da-35cd-a110-1762c34f3655 | -13.4726 | -46.490101 | 2025-11-14 00:38:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f79cb41-9e90-3b5b-8a3d-143daa277d42 | -15.3038 | -47.381001 | 2025-11-14 00:38:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 921e29a5-75d6-3ead-900e-cd08cf9b0b10 | -2.9431 | -49.361698 | 2025-11-14 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3e510cb-c33d-3f20-a702-f4617aaa083c | -3.7679 | -47.738899 | 2025-11-14 00:38:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ddce201-f9ed-3fdc-861a-2b2771a63ced | -11.8604 | -49.212601 | 2025-11-14 00:38:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4203730-efc4-35ff-8f67-0be242f5184c | -8.9029 | -41.078098 | 2025-11-14 00:38:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7b7c0d95-71b4-37b3-ae12-faa09d2c722d | -3.7596 | -47.748001 | 2025-11-14 00:38:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f66fc76f-8dc4-3ef3-988b-046b07142f46 | -6.4062 | -39.729401 | 2025-11-14 00:38:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7df84d26-06e9-305b-be79-ec075b2dfbca | -14.986 | -42.408401 | 2025-11-14 00:38:00 | METOP-C | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b1d52a7b-f0c0-375b-8124-f6f31048a124 | -7.9289 | -44.327301 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bdf373d2-ac84-32f3-b735-86fa5cf2da90 | -3.4472 | -44.5298 | 2025-11-14 00:38:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
