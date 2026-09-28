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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa3d928d-5846-31f1-aeb0-cb60df611471 | -8.93387 | -47.42057 | 2026-09-28 17:09:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3de1b127-864a-3b7a-aee8-70ed7feebb2d | -10.82644 | -57.18045 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 88902df0-6aec-37fe-8119-e403926eda22 | -5.22011 | -52.90824 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 24002409-7f93-3edc-951e-3fc4dc58be0b | -6.15217 | -52.88477 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f5ed2cde-c3c1-3916-abc8-69828f7437a2 | -8.66365 | -45.37296 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e62cbe68-84c8-3bb8-8859-4ee4e05f68d3 | -9.5129 | -46.35963 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 04f95337-9d2c-3c64-aaa5-379ce8123d56 | -7.05858 | -42.87874 | 2026-09-28 17:09:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| dff2c7e2-22a3-3aa6-943a-f953331e5273 | -10.00613 | -52.10122 | 2026-09-28 17:09:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 77af6829-e19a-352b-930c-7cc66889eab1 | -8.27878 | -54.78186 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4811ccca-6edd-395c-9fbf-3c32b0e73b09 | -11.12737 | -50.06007 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 5ee33f37-00e8-394c-b3b8-7008cbd2f4b7 | -10.7505 | -57.53053 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 557cbddc-20a9-36b1-9a5a-d6fe462b345d | -11.20087 | -44.80429 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 65237271-004d-35fc-96e5-8d0339c7653d | -10.80605 | -48.72529 | 2026-09-28 17:09:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c4f7abb6-5036-3f84-8fa5-d5ed8b1a070f | -7.45787 | -45.80657 | 2026-09-28 17:09:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 884bea93-3ab6-338a-b842-5a123f5590b0 | -8.32018 | -44.85447 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 09c62457-8b6e-39d9-a7b7-48eab0eecd27 | -11.0748 | -46.08836 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| da12dd92-9ab2-3b84-8c04-b2210343f4c2 | -12.80087 | -54.01317 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 503ba289-b56e-3654-b632-33bf6ee6231d | -10.20468 | -50.00698 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7cdfbf4e-d983-3939-b869-23d70a3de02a | -8.19337 | -54.79861 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4aa6a3b3-8394-32e8-89a1-c99fd9c91832 | -9.1112 | -58.90418 | 2026-09-28 17:09:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1ec25309-7a74-3b96-a94c-331eb7be8fd7 | -9.33326 | -46.42168 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ef75f905-5f18-3e96-aea6-bb0d4eee81c3 | -10.82119 | -57.2212 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 13389e02-324a-3adb-82ea-b7b569bd345d | -12.84707 | -54.02748 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 738c9cc4-09d8-3322-9e91-4e10ab23d57a | -5.11735 | -45.80264 | 2026-09-28 17:09:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| abb99ad2-2438-355c-9c8d-6fb116eab3bd | -7.28894 | -44.31141 | 2026-09-28 17:09:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1ef03a42-dbcb-39ad-bce4-9db6fe60f670 | -6.452 | -55.48278 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7f5d3bf5-ca77-3cda-8da3-f7ad64712be9 | -4.97843 | -49.62179 | 2026-09-28 17:09:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| e2949c17-befc-32f3-8859-9bbed007ef33 | -12.31234 | -50.15364 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 80f3d726-32d1-30b4-917c-77a409580bc3 | -10.24255 | -44.61294 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7f31e180-7cf2-36e5-9624-726b31cc0d3a | -5.73732 | -45.03763 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 00f60e64-0296-368e-bd6e-6c0728354a76 | -8.74439 | -44.90917 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2c365e5d-03a9-3c0d-9ca1-9a6b7980ac5e | -7.3059 | -43.31821 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5c86d994-b3a0-30fa-ae6f-5286b3348a1d | -11.13544 | -50.07077 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| bf60836a-604e-3c85-8949-49882aa451a3 | -12.79649 | -54.00665 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 5107dc2c-498e-3a42-9a0e-abeab602afbf | -8.63526 | -49.47977 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c92c7e0d-b9e5-3746-96db-b2120125aefc | -9.17774 | -51.42994 | 2026-09-28 17:09:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bce0bcfe-cae4-3c92-9aa8-a13046818a61 | -11.17796 | -44.8016 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| bb427148-ca54-307a-8dc0-79cb1b6935fc | -8.23596 | -54.65682 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f7e1a879-260c-37e1-a3f5-516c4f78ac24 | -12.79533 | -54.02126 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ebf92e3e-38dc-36e7-9155-3c7419fa8ed1 | -11.12677 | -51.18094 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ab864a04-855a-3bd0-a0f7-1bbbfd16ab91 | -9.76753 | -44.84543 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8d0c4fd4-6ab8-3054-a00e-9e8ff37723bc | -9.29723 | -46.44947 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3afd7174-69fc-3b5b-b065-582c366b5e5d | -9.51654 | -46.06168 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| cb6b3bea-1a2e-370f-817d-0a9b5c5b481c | -6.15154 | -52.88087 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f242b5e-525f-3c85-829d-b21c449eae9b | -12.79202 | -54.02179 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 3a1ceb25-c897-39c0-9f30-e6de7af85266 | -6.83659 | -52.44215 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3c596b1-17bc-3bc8-99a0-ec9a01e2d2dc | -7.69321 | -54.7755 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5c5e467b-8d79-3053-b181-76ffc0c4995f | -9.92905 | -50.24009 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| d6e5c7c3-7c8a-3a45-bba9-e0914cb9f699 | -4.70928 | -47.93174 | 2026-09-28 17:09:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| d027fd6e-6e9d-3410-9c16-585191939ef8 | -12.15961 | -50.40767 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8db334ac-e904-372e-9299-5f18d7f10029 | -9.77169 | -44.86604 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0367fb50-4be1-3fd1-98cf-649f9f3e6a5d | -9.3277 | -46.56176 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5a26059f-5289-3265-b0f3-9260caa85845 | -9.51391 | -54.65512 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2cc5928b-abc5-310d-8341-fe2f9252c080 | -6.16799 | -52.82545 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4a3cea02-7c9b-345d-baab-b30cca70a8e0 | -11.90693 | -49.98629 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 6383f01d-f6ae-3fdd-9bf3-9a05547a9cd8 | -8.14635 | -46.97139 | 2026-09-28 17:09:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e65a67f4-f17f-306e-9ed6-c949977f747c | -12.14401 | -50.35921 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1bd16838-aa22-356f-9a7e-af8c1b8ca484 | -8.03509 | -54.89867 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| aac8407a-bc7c-370b-b315-86a1875914b7 | -11.61415 | -65.15871 | 2026-09-28 17:09:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 43567776-95a4-31ba-a215-fd938454097e | -6.16157 | -52.83053 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3f399a46-b2a4-304d-acb2-2494b9ebd43e | -11.16082 | -48.31924 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4d5026c6-f69b-3906-a6cc-f36c8a15e55d | -10.91975 | -50.65879 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 48666c52-8170-3dff-a128-d14ad67570fa | -10.69696 | -60.73455 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0b2eca9a-2395-3bec-b40e-c5996a3335d2 | -10.72242 | -49.03127 | 2026-09-28 17:09:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 84d08c70-5b6e-3208-be3d-ebff1e8f2e34 | -10.59721 | -50.5679 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 7760bb6e-c9df-3dd2-a0dc-9c2c391efc56 | -11.84505 | -50.84776 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dd09faf-dbee-3888-88e9-9d48f13630f8 | -6.34162 | -55.31656 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2ee2379b-0ee1-3709-bfe3-72320ef6868a | -11.13279 | -50.06908 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d44955ff-5d76-38ec-ada3-2a88decaa1ed | -9.40092 | -46.39659 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9b94231-8234-3150-a194-ca94559bc79f | -10.8778 | -61.395 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ab80b9bc-adf6-3eb8-94e5-e8f7a2a17b18 | -11.85528 | -47.08328 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 00a9431f-1d82-3dfb-81f6-314f523c03b5 | -11.08301 | -46.07936 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 6b7d2d7f-3826-312f-8e76-a82cb6fecbac | -7.49593 | -54.97421 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04e435a9-a60b-3571-81eb-85102607912f | -12.80257 | -54.00208 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 9ad70c01-9f04-375f-aba3-8619361c0af7 | -11.54347 | -47.37039 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 64d9035b-b411-3c5a-a760-fbb81c1bad39 | -9.76541 | -44.83424 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b18aa4fd-3136-312a-8666-5fbc7d5a23fa | -7.27847 | -46.93141 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de7874ac-97ce-3fc7-8108-e98799a5bff9 | -6.20701 | -52.91253 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 962b0ed9-abe1-3c65-af41-78ecd5b71df2 | -8.97113 | -44.15601 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 553fc80e-5c73-37eb-a0f1-0f1cb84459a5 | -10.88876 | -50.69018 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 39ca4764-b67d-3fd7-ae26-1b256e1b2c47 | -7.70869 | -54.766 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72db7a28-64b6-32d5-bdff-cb37cf676863 | -7.45849 | -45.80999 | 2026-09-28 17:09:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 741316cf-4b0b-3b28-a001-a4742264355f | -9.14012 | -49.9729 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 28cb5f53-a156-384b-ba3d-bbbc88efd6bc | -11.30525 | -58.33858 | 2026-09-28 17:09:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 01020ea8-52cf-32c7-afb8-cb2db0597829 | -6.22201 | -48.12283 | 2026-09-28 17:09:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6d2686f4-d093-3926-8ac3-66773c73a790 | -8.35593 | -64.07826 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d172422d-4c72-3961-bd27-c457a31deb69 | -9.33148 | -45.35849 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 205586f4-2666-3c7a-a582-e2ff7fd0c744 | -12.11526 | -57.16904 | 2026-09-28 17:09:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| fbc42771-5f0a-35c2-8a69-c9bd6afd8285 | -12.16183 | -50.40886 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9a89e123-95cd-3ed0-a285-74a6437bc89f | -11.23474 | -61.16474 | 2026-09-28 17:09:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 30.8 |
| f73b4269-fc07-38ba-82f6-adbd0ee7da99 | -7.53667 | -50.92806 | 2026-09-28 17:09:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c5db102b-6e72-3c2d-82cb-ab1fe25f46e8 | -11.57198 | -47.39885 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 64210bb4-c7ce-374a-b371-226021ddd316 | -8.7316 | -44.90258 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 84dad139-0383-3c40-b2d8-b3d70e568455 | -11.18888 | -50.03659 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 88454fff-0fcd-3c16-95eb-e90641bf097b | -7.3313 | -55.58811 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9a62054-c8d6-38b9-a920-8063bd2b64b1 | -6.31747 | -46.6551 | 2026-09-28 17:09:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5cad095-5125-31b9-b0bd-0766c0f89da5 | -10.21639 | -50.00496 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 979347ba-8306-32b9-baf0-64b21f2c8034 | -11.56745 | -47.39965 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c848ef52-66fc-3895-b131-378d94bff563 | -6.30722 | -56.02957 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 2511228c-7802-3cc6-abce-13dcadcb38e1 | -7.60995 | -55.11881 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README161.md)
