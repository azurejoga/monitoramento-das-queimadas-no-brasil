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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0c2c9bd-3506-3ee8-b3bf-ab94a6ea61ac | -10.22795 | -52.66161 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ec7fe01-861e-386b-8dcd-3637b2b20f03 | -8.35499 | -48.13661 | 2026-05-21 04:23:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7835940e-b5a0-3104-8bf0-9f56b892ba88 | -12.0004 | -45.136 | 2026-05-21 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29bb3289-7715-3df3-9b2b-4869c4869bcb | -15.09024 | -41.15399 | 2026-05-21 04:23:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 22ce958a-dfc7-3bfe-91a0-d89b02a34ebb | -8.66846 | -49.43207 | 2026-05-21 04:23:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 355a6d2d-78c8-38a2-a10a-baa4e0562265 | -11.30006 | -54.7124 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a16127ec-648b-3dca-bd45-e5478581ed7d | -8.56757 | -46.4347 | 2026-05-21 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddbb8f39-4ba6-3134-859f-60e4a19e10e8 | -11.33977 | -48.00103 | 2026-05-21 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0670bc3b-a191-3133-bf95-9f05288e94c8 | -13.28461 | -50.28361 | 2026-05-21 04:23:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b967494-b649-3004-82bf-4e19af97608a | -9.29751 | -45.48223 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a66259c5-c218-3af9-a4c3-f32ca514ab1d | -12.22901 | -44.26278 | 2026-05-21 04:23:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b77bc6af-0cf1-35bb-af44-716233bdaa45 | -9.95896 | -52.45204 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0eb3571b-6565-3d3b-9efe-223f26c6fb01 | -11.03427 | -48.91162 | 2026-05-21 04:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f974866-432d-346f-b11b-b207dabc9858 | -11.6816 | -44.86991 | 2026-05-21 04:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f788b18-4b70-3795-9b5f-1ce2850d214f | -11.54555 | -54.5349 | 2026-05-21 04:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ad0fbae-8ed6-368d-8faa-ec5a2c0435d7 | -11.07518 | -48.26277 | 2026-05-21 04:23:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bea7f6ce-69a1-3cb9-abbf-d78e908cd309 | -11.187 | -55.91237 | 2026-05-21 04:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82421a4b-1f19-3416-84b7-de9e306f7980 | -9.66691 | -46.92563 | 2026-05-21 04:23:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbe4c138-c899-37dd-955d-662fa4a9d358 | -11.54103 | -54.53087 | 2026-05-21 04:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f22e2972-e4f8-3bd5-84e5-c1082794be1e | -8.6235 | -45.97979 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6931b3ca-c424-3564-9dc2-19e6d8e665b3 | -10.65305 | -42.29805 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d3e90df8-cec6-3b7c-8f45-89834604a332 | -11.18064 | -55.91506 | 2026-05-21 04:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64b1de10-a595-3abf-8c76-bd28ced438e2 | -12.05433 | -45.28995 | 2026-05-21 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c03b922-b6da-3c4f-bd66-1aaae198751d | -8.71244 | -47.86266 | 2026-05-21 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03c719fd-795a-3791-912c-38b5ae674e68 | -11.30525 | -54.71339 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bbc4564-d0d3-3279-b060-4a0483b95d8c | -10.64777 | -42.3036 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f04b404-0acf-33b8-a7fc-f9276666147a | -10.6435 | -42.3073 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 25630cc3-effa-38d2-b49a-77a75c8a1ffb | -9.30026 | -45.48624 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0b933e5d-6394-3f3b-8c25-3a46c2d910f6 | -11.95895 | -43.38538 | 2026-05-21 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95ebde70-3638-32f0-92d7-6e33d503d40f | -12.82187 | -48.57772 | 2026-05-21 04:23:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4429fed-5b3c-3069-9c38-99705d0fe4ed | -11.18138 | -55.91127 | 2026-05-21 04:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b1b5c4a-453a-3216-bfb8-abdf13c6a310 | -11.30984 | -54.71753 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d187f25-fd59-3853-a376-90df4f2defb4 | -10.35573 | -47.81546 | 2026-05-21 04:23:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cae2f9c4-c98f-3209-a4a4-f0c7f01623a9 | -13.67861 | -52.59181 | 2026-05-21 04:23:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a156f8a-096f-314f-aaf4-f534d495558e | -15.06943 | -42.3747 | 2026-05-21 04:23:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dac71ea0-54d4-3724-85fc-33c2e482e15c | -11.33849 | -48.00872 | 2026-05-21 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47976ac9-1278-339f-b13e-ed2078a85cc9 | -10.97639 | -49.42714 | 2026-05-21 04:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 785ede21-abfb-3693-8938-f3e86c79f5eb | -11.29945 | -54.71556 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c717047-12c8-384b-af03-ef7adc776397 | -11.03447 | -49.47746 | 2026-05-21 04:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20d3ef65-5ed2-3a4a-a1b2-a3c507f96bbd | -8.32251 | -48.00966 | 2026-05-21 04:23:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28b10b5d-97e7-347a-b605-b1a753c37e32 | -11.01834 | -42.86251 | 2026-05-21 04:23:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65a66c4c-3961-3b0a-ade2-9a32fc0c4897 | -9.81675 | -48.00227 | 2026-05-21 04:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6406848b-2246-3524-a6cd-a1515cb59043 | -10.10799 | -52.41021 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf7f41b5-db0d-3a7e-b95a-a73971e62dc3 | -11.8127 | -45.53296 | 2026-05-21 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d350d2a6-37d9-38c0-a993-a813e5292e6b | -10.4891 | -49.36604 | 2026-05-21 04:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7522d31-37a2-3a8d-a429-4010369236cb | -11.46892 | -52.91875 | 2026-05-21 04:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd841a37-2e32-33ff-b072-ed1a2e7196a0 | -12.22958 | -46.60912 | 2026-05-21 04:23:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fb4c990-3888-36e7-8663-2d05f5c007a4 | -13.51776 | -47.69312 | 2026-05-21 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61e4be2e-f7cf-3c10-b8ed-e6cc1272df5a | -9.62473 | -48.88246 | 2026-05-21 04:23:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ae1c8c8-e02b-3ea8-b587-5c90833b4444 | -14.22684 | -43.65407 | 2026-05-21 04:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2736e0ac-2805-3385-b18e-e40ff27d3e43 | -11.33546 | -47.42924 | 2026-05-21 04:23:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b153721-68d6-3afb-8332-00423b91a8d6 | -9.94439 | -52.45434 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10b67ff5-d28a-3eca-be51-67723fd40df2 | -10.32249 | -53.57752 | 2026-05-21 04:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28a8696c-00ef-32c2-9b92-ee96d74e30c4 | -13.02952 | -49.94221 | 2026-05-21 04:23:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a52a4529-d35f-3dcb-9b5e-222878165b60 | -11.30066 | -54.70927 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b89e2f8a-bab0-37cb-8902-fa7c760e309e | -9.96101 | -52.46726 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b206250-0423-33a4-a4fb-4dda2b116e09 | -9.30082 | -45.48276 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0e8d4f86-76e6-3627-95ea-485f4c1bf284 | -9.93162 | -48.00842 | 2026-05-21 04:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6bd53a9-00a7-36a6-ad44-725ddaa1f7ce | -14.16377 | -45.32182 | 2026-05-21 04:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c273c0c7-9f80-3091-9260-0dcfafffceef | -10.49061 | -49.35703 | 2026-05-21 04:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3b7159bc-c22a-3efb-90fc-261811546d28 | -10.64942 | -42.2975 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba4ef9e0-5399-3e33-a548-38b1c44400f7 | -10.65139 | -42.30415 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e3e3c01-a60b-346f-96c3-eb5675ec1057 | -10.64578 | -42.29695 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9db65d8-3bc1-39d6-ba7e-131a86101671 | -14.16043 | -45.32128 | 2026-05-21 04:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 590db79b-504b-342e-a887-7b53ed972fbd | -11.4606 | -55.11757 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a8cdc70-94c6-3d71-91b8-94232852dae3 | -11.83521 | -47.09509 | 2026-05-21 04:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d890d8b6-9de8-31b7-94dc-766f60cf86e1 | -9.30633 | -45.49079 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6fd3f832-7581-3ea8-b2c9-7df21a15906e | -11.83127 | -47.09814 | 2026-05-21 04:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6bcdb16-e12d-3b33-8063-172a861c4a30 | -12.07974 | -51.25849 | 2026-05-21 04:23:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b659487-e91f-32a4-b667-0a9583e1379c | -13.51715 | -47.69682 | 2026-05-21 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 187f88ce-2c92-3d22-ae06-bac0176f810e | -12.22913 | -48.10015 | 2026-05-21 04:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84e56f30-c7c8-354b-8513-f64bd9733a7d | -9.30577 | -45.49427 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3238a040-3ad0-34d1-83ed-b1512e3ec113 | -11.55729 | -48.26084 | 2026-05-21 04:23:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 173db8e2-bef6-3573-aeb5-3b79616cb8f9 | -14.15987 | -45.32491 | 2026-05-21 04:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbf6c0c0-f6f1-3938-be1a-c071d0943c82 | -8.73269 | -47.98178 | 2026-05-21 04:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c9d9f9e-4e17-3a06-a4c4-1a9a0b03e309 | -10.64455 | -42.30547 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d21a53c8-5d17-37e5-9843-c33f679e8549 | -11.30585 | -54.71025 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77c9295e-7a1d-3759-a641-38a33a609b98 | -11.07167 | -48.26218 | 2026-05-21 04:23:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfb1901b-a2b2-3240-ac8b-8f5705d40efa | -8.31894 | -48.00905 | 2026-05-21 04:23:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfd1739d-af5c-3576-919d-1b2788fa0342 | -12.06097 | -45.29102 | 2026-05-21 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3108065e-b5da-36bd-acc0-0a1922993c09 | -10.64414 | -42.30305 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 16286280-19d7-3275-b354-151ba5bd4396 | -9.14261 | -51.27933 | 2026-05-21 04:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72a2a7c7-7084-36ba-ac0b-cf5d61bf4a7a | -8.62683 | -45.98033 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9ed09b8-f694-3dbd-b725-b12bc945cbf6 | -11.56517 | -56.94794 | 2026-05-21 04:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0925f52-a9af-3fb2-8da2-3913f95e45d6 | -8.55463 | -45.98648 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0a430b62-7966-393c-98b2-db7cee1bf167 | -8.62627 | -45.98386 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8e04dc0-ed7a-3445-8716-2b82a43c735e | -11.99985 | -45.13955 | 2026-05-21 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ae2f044a-7c55-3651-92f9-28cea1565c91 | -10.64818 | -42.30602 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f6e2a93d-9874-39d5-8db6-b84d060ea424 | -8.5574 | -45.99055 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 078ab3b3-ec9b-39c3-b829-02ad20005a1a | -11.08596 | -46.55518 | 2026-05-21 04:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab79b16f-7fd0-376c-b505-bb69f526f327 | -11.33913 | -48.00487 | 2026-05-21 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ea55965-2ae7-30dd-82a0-2100ca565de0 | -8.55186 | -45.98242 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cae0fd2b-40ae-35af-82aa-579366e03633 | -11.29884 | -54.71875 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14a9d610-bf9d-38e8-805b-736cd2bb1b14 | -8.60748 | -45.9519 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c8d5ae4-debf-3c56-8a77-24a9a55370aa | -16.35579 | -43.87773 | 2026-05-21 04:25:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2095123f-d2e1-3132-b4fc-e02425464691 | -21.12007 | -48.62439 | 2026-05-21 04:25:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9e25a0a0-1bfb-38aa-8848-0d93166d7cc6 | -16.35221 | -43.87717 | 2026-05-21 04:25:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94a41e53-2dfe-3290-8e24-ff8c7ba685eb | -19.76516 | -54.07126 | 2026-05-21 04:25:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 452f9742-fab3-3eb1-90d4-1811432968d3 | -14.90347 | -47.75074 | 2026-05-21 04:25:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7be73425-92d6-3f80-8a11-719b2c4a993b | -20.76526 | -48.56886 | 2026-05-21 04:25:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
