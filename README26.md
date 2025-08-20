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
| 7c810d20-d94d-3298-90c9-0b79cb3f9d62 | -6.01008 | -42.82239 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 67083734-2c47-3032-b24a-b1c5768ceaa0 | -2.90692 | -48.29307 | 2025-08-20 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd2435f3-e4e5-36f1-b57e-83b07e412847 | -7.29549 | -43.68097 | 2025-08-20 04:34:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4a8e41e7-c5c4-3377-b7d8-67981edf6272 | -7.60119 | -44.39626 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41167d8f-a520-3a6f-9518-ac6ce997138a | -6.20046 | -43.55889 | 2025-08-20 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09e315bd-75a2-38f1-8f11-327eeea3181d | -8.3016 | -47.62105 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0f95c18-fe19-3d73-9907-d8207a2cfc7a | -8.8295 | -52.04047 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4ecb54d-484a-3e71-8f18-b7de4a5f630b | -4.90991 | -43.23332 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8d2a63d8-12c5-32a6-845c-37aec373175f | -6.96849 | -42.86798 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 425175ee-9540-358c-9ae9-a0c5b6cee1fc | -6.16299 | -42.71311 | 2025-08-20 04:34:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 81415be7-f530-37dd-89fd-bb6b6e44e751 | -4.91374 | -43.23387 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c4096c6e-f5ae-30df-8349-0889a978e88a | -3.35945 | -43.35987 | 2025-08-20 04:34:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9db5489b-e8be-3968-b056-94834b6288cc | -7.81501 | -46.88665 | 2025-08-20 04:34:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af33ede9-0551-3717-94e5-416a60613346 | -8.07115 | -43.66891 | 2025-08-20 04:34:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4b611ec-32dd-3da1-aae9-2a00181ef9c3 | -2.38498 | -47.65989 | 2025-08-20 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ff6f6429-3061-3483-88bd-043dba3d24c0 | -8.17221 | -47.34869 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5da6fd34-7713-303a-a68a-fafedbf74d42 | -5.88114 | -48.12538 | 2025-08-20 04:34:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5287b190-4dd3-3fb5-b5ea-cfd184bf7c76 | -7.64578 | -45.2738 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57dc27de-0cca-3ad8-be4d-4e13c94b23b6 | -5.65721 | -43.5078 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ecddd7c-1e54-3def-9681-d41868ca95d8 | -3.97397 | -42.50677 | 2025-08-20 04:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 83749e10-a707-326a-a394-b6fd9fd0665c | -6.032 | -44.38736 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0675e95b-d6f2-349a-bbf4-d69935a7ca52 | -6.57748 | -44.47539 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f4f81b7-c859-36d3-a501-5a7409980090 | -8.29936 | -46.35082 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95877924-83f0-3fc9-9271-8b3dc4a3efe0 | -7.30346 | -43.70661 | 2025-08-20 04:34:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0551c657-ee20-3f2a-8b85-e306df4129e7 | -6.00935 | -42.82731 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 225fd09f-7ba8-35cc-8b43-b5834b14e90c | -6.39496 | -44.24848 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa0f5412-96dd-3f1e-bd27-cb688f906c7a | -9.37451 | -48.2853 | 2025-08-20 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37c727da-9e7e-3bab-8e09-cc2287ead189 | -7.63849 | -45.27797 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d792e41-c093-3d36-8c1c-70f2315d265e | -9.26641 | -44.53738 | 2025-08-20 04:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4422854-8c35-39d4-8303-b71f7912b34b | -5.97893 | -44.14352 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b47e7af-300e-3208-8f89-2ea0e69bb5ce | -7.12956 | -44.63972 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7f327c4-b9f0-31b7-95f8-6bae1f19e218 | -6.50854 | -43.44687 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e13f8b72-d329-34db-b4bd-060a023d50e2 | -9.37396 | -48.2888 | 2025-08-20 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0091283-1885-3c9c-978a-2324a48fc08a | -6.06765 | -44.39968 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54d21b1c-0e44-3645-9cb0-70bcede48f74 | -9.37286 | -48.29578 | 2025-08-20 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36d6c25d-9d09-3e7b-b360-b09c15369de9 | -4.91327 | -42.09411 | 2025-08-20 04:34:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c10f0afe-71cf-3f29-8a40-9072401e31c1 | -5.54486 | -45.37432 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 075fa1ce-3884-394a-9e7e-92d16ea13da1 | -7.2274 | -44.70534 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e60fcef-1c08-3b1d-8e22-b41df2785607 | -7.05205 | -59.23044 | 2025-08-20 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bae475cf-9793-3a08-a7f6-498dc58e3097 | -4.91739 | -42.09472 | 2025-08-20 04:34:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf4b9cba-5a3d-39af-a548-fae42281f00c | -3.39669 | -46.90665 | 2025-08-20 04:34:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eb9b1ff-5e47-38d0-9666-d606c39d14c6 | -8.82273 | -52.05818 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85db528c-12df-31fd-8051-d03956e69e68 | -6.39612 | -44.25066 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93b0220d-920b-33ae-8392-a8f7a1e62677 | -7.22868 | -44.69683 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13ac6a6f-01a0-35bc-912a-741cc16f7fd4 | -7.58363 | -45.42373 | 2025-08-20 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40164f8a-762f-3e72-90f7-d6373ceb31b7 | -5.78812 | -43.61463 | 2025-08-20 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e0d3171-538e-3bf9-95c9-ac05ff488056 | -4.29825 | -48.07183 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11c15445-4c00-3844-a19f-bb61b2ec3e3b | -7.52498 | -45.0044 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7eb64e31-7900-3202-9205-39dece0433f4 | -2.38443 | -47.66339 | 2025-08-20 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 994bc32b-3ae4-3979-b9a1-f8dd0bcd7d91 | -7.65231 | -45.2543 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80e544c1-6994-3977-8d99-25cf8bb7cf93 | -8.83251 | -52.04556 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 746de127-eb03-3ba5-9b4e-c7a4dffe37fa | -3.97131 | -42.50462 | 2025-08-20 04:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8cbc9394-fa80-3e63-a493-6e84499da2de | -4.40046 | -42.14507 | 2025-08-20 04:34:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e3589a02-752e-38fc-9b32-c160683a53cc | -8.83389 | -52.03945 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 692d66f3-f9d9-37d7-b4d4-6d6d2201f46f | -6.26326 | -52.82246 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a6d9d8d-cda4-3bd8-807f-ee9243bf0c2e | -2.83701 | -49.14334 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cc79110-6d2e-3031-87c6-66892725bf34 | -8.30278 | -46.35135 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76a028cb-0f58-3a77-956f-d1e718bc1255 | -8.21829 | -47.30952 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5272f736-46d0-3687-b508-0562a89ad6a9 | -8.2144 | -47.3125 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fcb7dc2-badf-3428-83f1-43cd521c2efb | -5.98866 | -42.82949 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f842dede-1c0b-3872-8a89-e59e72ed563d | -8.29882 | -47.61703 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d37d80ec-5d53-3ded-978a-632497f04233 | -6.08393 | -44.58603 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68dbf3f1-90c3-3ad5-9ca7-ff02113760bb | -7.63203 | -45.2728 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d032fbc7-d61b-329b-b233-a9e1cc14159c | -6.45894 | -53.37704 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bff70bf-4794-3e6a-99eb-9b13a7d3fae6 | -5.61478 | -45.1809 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de363c8c-ac3a-35ad-8653-c3fb907a6a26 | -3.23763 | -46.80062 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff21183a-1118-3fc0-a09c-340d5eaf7dc4 | -6.54212 | -43.00499 | 2025-08-20 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 942f9e67-c336-3dbe-b92e-4a08b667069b | -2.90304 | -48.25209 | 2025-08-20 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57572114-d103-3593-8651-d822869357ff | -6.46248 | -53.38161 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b103d68-5832-3f32-85f1-a2218c29883d | -9.81141 | -46.88512 | 2025-08-20 04:34:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95e8b7e9-7e7f-3359-81a5-371dd0b0c3ee | -6.51814 | -45.46366 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6d2afc9-20d8-3d9c-8382-50923bd8e092 | -2.58477 | -51.92367 | 2025-08-20 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 758c09a9-047e-34af-ada5-8629b2f602cc | -8.29718 | -47.62752 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eb6a8c61-fb37-37be-9d8e-c0e608b0cb48 | -7.96898 | -55.29503 | 2025-08-20 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e61de0b8-1247-3fce-ab16-11f71d506e93 | -6.96798 | -42.87152 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 31f79ad4-2ede-3a41-8068-3d08e9308153 | -9.66765 | -40.58905 | 2025-08-20 04:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 382b6f28-aa31-353a-8ec1-6f049ba9f585 | -4.43084 | -47.7533 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fcf9f91f-7652-3472-a53a-ccc0c955726d | -6.05853 | -44.11593 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d35c1f72-5799-3487-bd89-b0d7284634a4 | -5.32071 | -44.48686 | 2025-08-20 04:34:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ad8a939-cad2-3ead-ab4a-d02cc47d849b | -8.07189 | -43.66395 | 2025-08-20 04:34:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4c7632c-b9fe-3033-9d0a-f55cae406676 | -7.64496 | -45.28309 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be226b5b-27a2-30b4-bc04-5d24f10daadf | -6.06828 | -44.12624 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b33d1b8a-8b48-3c2f-8275-034c1a3c4f28 | -7.63213 | -46.2205 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0211495-5d4b-37f0-809c-f12253ef2517 | -7.63682 | -45.26526 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7d94af5-090a-3a5b-82ac-728940ecd531 | -8.15699 | -45.56122 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de677a47-e1bc-3fba-9910-59bb98a755c7 | -3.47199 | -47.69854 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eec9b24c-a6af-3a6b-84cb-06e689873efb | -3.14073 | -49.20935 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb174d0a-7b08-3040-8dbf-019d3e7ba891 | -8.02343 | -47.67381 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b7885111-8a35-3ae6-ae9f-359a57600b78 | -8.02562 | -47.65985 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a2ced44-fbdd-3226-a50f-ba676b467a2d | -6.37082 | -43.26821 | 2025-08-20 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c1649ac-fdfb-3182-8b22-f7ac297551f7 | -7.58837 | -45.41631 | 2025-08-20 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d76fd265-bc64-35fe-a4e1-000f8d7bafa5 | -3.98336 | -43.23982 | 2025-08-20 04:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aaa7ddc4-59b7-3a06-b69d-4d22d4ebd396 | -7.14214 | -44.18811 | 2025-08-20 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec3cb748-824f-39a8-baf9-53f8d1c1fa9a | -9.52678 | -42.93425 | 2025-08-20 04:34:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 37425cfe-64be-3484-9329-35451ed5776b | -6.52163 | -45.46414 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24230ed4-bec7-3a97-84da-3bb79437bbbe | -8.45372 | -43.8629 | 2025-08-20 04:34:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97ab033a-a530-3378-a707-2908abaa7cc1 | -2.58884 | -51.92431 | 2025-08-20 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b742b97b-afeb-30a8-966f-65f27f950a4f | -7.27722 | -50.1864 | 2025-08-20 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88c1a9eb-b3e2-317c-a660-9c5fa6abedfe | -4.91685 | -43.23911 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5f320391-c830-31ba-a315-31f7f217371c | -8.79285 | -45.47824 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README27.md)
