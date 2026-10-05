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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d0fb7f2-1416-3985-a1f6-ddd936610382 | -2.90541 | -54.08283 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7e0ca547-7f01-3b5b-b9e6-da43880792d9 | -3.28355 | -54.17936 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 271f3707-753b-360a-9b4b-d3ef8b993b16 | -3.64173 | -58.62293 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| fa57a435-77bb-347b-a134-b35e676c91fa | -2.93417 | -54.13075 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a6afda7a-ec57-3ae1-9ff7-9e1be5b1d042 | -3.97031 | -59.35408 | 2026-10-05 16:39:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a2a8e212-9926-321a-a20f-75042d39ba2d | -1.80001 | -45.27844 | 2026-10-05 16:39:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 94a3e0c1-1cdb-3d63-96e0-9900dcfcfeb0 | -3.37501 | -54.09768 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a6df8e17-0e1f-313b-978a-cac289413c0a | -3.98559 | -55.82211 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c77e1a32-5d4a-3f91-bfde-9a3873868305 | -1.05389 | -53.58736 | 2026-10-05 16:39:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 34947ec6-1a85-3611-a81f-b9c27f9fcc12 | -3.21011 | -42.87495 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| a67da55f-dbad-3cdf-a052-d986a0489500 | -4.0745 | -55.7672 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| d705d77b-dff9-31ac-8663-2d55d0aae402 | -3.74632 | -39.54265 | 2026-10-05 16:39:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4682917d-069e-37b8-9a8b-5c40e520052a | -7.21876 | -55.20619 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2fc18e26-a1cd-3e07-b3dd-fac95cafb1c0 | -3.79637 | -41.76723 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 04a33eff-d8f0-37dd-9fcf-ccc57f5f3c1d | -7.23674 | -55.19298 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5fc13694-7482-30e1-9220-3a1e2277ac46 | -1.46816 | -54.77509 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 4dd846e7-c93b-30ed-bbe6-e4c35c74f20e | -3.28398 | -53.83225 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 15a50b91-1bd7-36cc-906b-2d0e199e6be5 | -6.20274 | -43.08802 | 2026-10-05 16:39:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eceb516f-0387-39da-9cff-2f1cf09ba2d1 | -1.46469 | -53.61396 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 52db3e52-3bf2-3e9b-9dfe-41e6caa1046e | -5.97331 | -41.32563 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ab9a3c69-35b5-398f-93a5-8681a6c5cf89 | -3.55185 | -43.8992 | 2026-10-05 16:39:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| df2ef210-9ed8-36bb-bed6-62207afe70a8 | -7.22653 | -55.20215 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4f4f51a4-4ddc-313f-98b9-d61ce9cfe3fd | -3.32365 | -59.47566 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9d0f5ac2-4dcd-3c71-b762-0328288803b2 | -6.06697 | -53.83889 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e9892e63-49bf-3854-94be-c386b8e05fc2 | -4.811 | -45.65218 | 2026-10-05 16:39:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f2d6fd4b-8fe6-3f48-b05c-908e3f880abd | -3.63347 | -58.93364 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| abfb856e-c16d-36b7-bed4-4ca78eb904e0 | -3.00401 | -44.01801 | 2026-10-05 16:39:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a3d725b7-ff75-3be3-a1b1-9bfd1c4ab3d5 | -7.23067 | -55.19604 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ae60579a-7388-3687-baa4-a0bab4af93c8 | -3.3762 | -42.51151 | 2026-10-05 16:39:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| dc3c7acc-dd2f-3597-9898-8696c045aa22 | -3.10102 | -53.74302 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 09b0e26b-c84c-390c-baf8-db964847712a | -2.9324 | -54.11893 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4f0fcf8e-3fd7-3cd0-b85e-56f80eb26f50 | -2.448 | -50.25364 | 2026-10-05 16:39:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| dd3aaac9-8212-361d-a7cb-0130d3545ef6 | -2.28521 | -56.78948 | 2026-10-05 16:39:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| daa96761-4479-3709-95ff-c3582a8c2291 | -1.17817 | -49.2515 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 36617a45-4a3a-348d-858b-08be27eb633e | -6.17872 | -55.36211 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ac70a389-6b54-37a7-bc42-f93141342948 | -1.47434 | -54.52461 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c6504337-0265-34bf-a789-8bf87d7b0c6d | -3.53561 | -39.89417 | 2026-10-05 16:39:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 70ef0131-b40b-3ac0-a80f-fb7ed8b1c04d | -3.76907 | -39.84332 | 2026-10-05 16:39:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| b045451e-9b6c-3b3a-bc1a-37113433747c | -3.81455 | -41.68441 | 2026-10-05 16:39:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 7f267412-85ed-3d5e-87ab-cf7cd58b9fed | -5.98812 | -53.63827 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e97c52ca-8f39-32b2-9c90-daf4ca1af79f | -5.83499 | -45.01297 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c82fd390-3bed-3350-aba4-6423aeff3e7b | -5.03639 | -42.73022 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 78e696a6-1e78-3344-9e37-f626468efd17 | -3.37738 | -58.22641 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d8d485d-7f26-33fa-87c5-c379d8b87a4b | -5.33228 | -45.9359 | 2026-10-05 16:39:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c30dd039-2622-339e-ae64-15983af5065c | -3.6287 | -58.6137 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8b14e340-660c-3e1f-a020-80fd06360221 | -5.12238 | -43.99623 | 2026-10-05 16:39:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 00f6bc62-271b-3ab6-823d-e6e22ec2a4b5 | -3.74069 | -39.5405 | 2026-10-05 16:39:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a63f6d34-fcda-312c-be61-dbf33595ac36 | -6.0713 | -53.87662 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 66d25b4b-88e7-37c9-8f90-f1d851b3818e | -2.97056 | -58.45385 | 2026-10-05 16:39:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 05e4d1c1-21f6-3f1e-9f11-d0013ff73989 | -4.43436 | -43.42608 | 2026-10-05 16:39:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| a4357b89-db75-342c-a5cb-858103027836 | -3.68433 | -54.53922 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c7959f75-e756-3157-add9-a822aa9d4621 | -4.84312 | -40.40284 | 2026-10-05 16:39:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| b6609922-defb-3b87-b334-fcd61c56ce88 | -3.138 | -53.71794 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4e5b11c9-cd24-3ace-b834-4ca78e13ab04 | -4.84914 | -42.20091 | 2026-10-05 16:39:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| b9d87b4d-689f-3597-89cc-704a3d23e309 | -3.52182 | -54.62744 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 40e12141-435f-35e6-9347-252e2bc9dcbd | -1.36447 | -47.44169 | 2026-10-05 16:39:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fe91c185-6ffc-34f1-afcb-127b06b3e966 | -4.37319 | -45.02842 | 2026-10-05 16:39:00 | NOAA-21 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 198f37e6-6466-38f6-865d-e2724ddf4975 | -1.1682 | -46.73305 | 2026-10-05 16:39:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b1209e63-70f6-3458-ab67-e4ef803d97ca | -4.1032 | -59.10101 | 2026-10-05 16:39:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| aea2d151-e1b7-3df8-8d55-2ed7a2383054 | -4.56989 | -39.58784 | 2026-10-05 16:39:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 29f13f77-60f0-3eed-b4a0-1fb32ab5f5a8 | -2.01278 | -49.87346 | 2026-10-05 16:39:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3e56dd3b-96bf-38c5-a1b3-7a20faa78cbe | -3.15628 | -50.43961 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 1362379d-155d-3ae5-b0d2-a66c14fd1031 | -5.84785 | -45.02338 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f521f5da-6bd7-38bb-a359-11622f938223 | -2.97614 | -41.80172 | 2026-10-05 16:39:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 279b046b-0f41-30b7-8945-f0373b3a2eef | -5.84722 | -45.01945 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9ab2b87e-ab52-3fc7-8d40-0acde75da894 | -3.69218 | -44.9389 | 2026-10-05 16:39:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b47ae5d8-e381-3fde-a3c2-173f916d069a | -3.30816 | -59.5017 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8a137753-618b-39c0-81bf-9d07840d27ef | -3.313 | -43.93698 | 2026-10-05 16:39:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 938a0a10-ef51-3b43-a7bb-cf02a9ff8c30 | -3.50488 | -59.5602 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fa7377aa-d6d1-3ad4-b1bb-63646dc21bee | -3.62176 | -44.41852 | 2026-10-05 16:39:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d7fa4a81-944f-317c-9654-1b65603af13f | -5.48136 | -39.56237 | 2026-10-05 16:39:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 39.9 |
| dbd4b078-d3c7-31d9-a4c8-2cefe1665f5f | -2.78581 | -54.0922 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 230c589d-1e44-328f-ba00-5a895a626676 | -2.88919 | -43.02707 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6c661356-1ad7-30e1-b489-0ee8d0d1ec0f | -3.53416 | -39.88534 | 2026-10-05 16:39:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 271ffeb0-02c5-3441-b9b5-0476d8722a2c | -5.95344 | -41.34177 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| d35355f8-2e44-36e3-aed7-0099494c2550 | -3.10838 | -53.70775 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 340.0 |
| 0a8908d5-8256-3e73-9e9d-11188367fc07 | -3.21155 | -42.87392 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 0a552c0c-2af5-3955-a68d-24a62e2961d7 | -5.16311 | -42.97607 | 2026-10-05 16:39:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 019906aa-adb0-36c2-8538-f071af52399a | -2.95248 | -59.15863 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c8287cdf-342d-31e6-8d3b-aba7eecbbd84 | -6.4548 | -55.48069 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ab8823f2-f41c-3744-8e08-266f8f3bce45 | -2.92286 | -42.38176 | 2026-10-05 16:39:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2607c919-1e9e-38d9-bc6b-b51bb18f3437 | -3.21527 | -57.88298 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 3edc62d8-5dda-3655-9cc8-451106ba290d | -1.05596 | -53.59162 | 2026-10-05 16:39:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4707d521-b7d3-36d1-a2aa-4819ff170030 | -6.46078 | -55.45192 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 2a065c1d-3be0-3d5e-95d8-ce3c1eb65438 | -3.31653 | -44.22856 | 2026-10-05 16:39:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0c6b817d-8f1a-3567-ab12-287c5ded5e34 | -2.06966 | -56.8558 | 2026-10-05 16:39:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80f079c0-be82-3ea2-a980-547ec233e754 | -0.3376 | -52.02781 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 93f68d16-87dc-3c1f-b43e-0e9cdd22d14f | -4.97052 | -43.07929 | 2026-10-05 16:39:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6de4e63c-93d2-32bb-b8c6-274962a5d449 | -7.21243 | -55.19651 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 09c148fa-93e2-3b46-b191-b17774246d1b | -7.11259 | -55.72552 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 36939018-f860-3472-8dff-97208ee03d3f | -1.48947 | -55.67285 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 941ab2f4-43e3-36c2-a21a-cf0ba067855e | -2.89409 | -42.39462 | 2026-10-05 16:39:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca8a872d-2c1a-304e-a33b-2e4c5bf13616 | -3.91632 | -44.14523 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 08ad0798-0070-392a-b4ab-98cf7836b1a8 | -3.16794 | -58.63327 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 30d442d6-7985-30e5-b7e2-c8adcadf8e27 | -3.27868 | -54.17599 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| d6e23725-c32a-388c-991b-b8b776729ad6 | -3.7691 | -58.92206 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5551193-2c98-3fdb-bf3e-b0f7e9306977 | -3.34897 | -42.90595 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6965db61-fc84-323f-8776-bc9697789e7a | -6.22189 | -60.0368 | 2026-10-05 16:39:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bfabf8d9-2332-31fb-9259-53c254f23e97 | -4.33404 | -43.81453 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9465fc73-7621-33a6-9c68-baf9092e63c8 | -3.31835 | -43.94589 | 2026-10-05 16:39:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README95.md)
