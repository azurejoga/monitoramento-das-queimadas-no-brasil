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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d01081ad-ef15-325a-9937-2343c89b538b | -21.97492 | -47.66 | 2026-07-24 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc1b90f2-e0c4-34a4-b364-2153cb0bb273 | -28.48345 | -48.96926 | 2026-07-24 04:32:00 | NOAA-20 | TUBARÃO | SANTA CATARINA | Brasil | 4218707 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 53476d0d-b191-30e6-900e-7a796b7e7e5d | 1.13372 | -59.38363 | 2026-07-24 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98bf7d6f-5f37-3028-9efa-8f196fb00727 | -6.15435 | -55.81299 | 2026-07-24 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3b001b5-7cc9-3d88-987e-e21cabaafc5d | -7.30444 | -47.01691 | 2026-07-24 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2911417-e5f8-3ac0-be03-d5f0002c5386 | -4.37239 | -47.7666 | 2026-07-24 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 01a70307-b353-329b-abb7-a1127d865de8 | -6.57265 | -55.14512 | 2026-07-24 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 117f745a-add3-3029-9e54-d100c587443a | -1.5911 | -50.43602 | 2026-07-24 05:10:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c60fc4ab-5d93-39d2-ac8e-44a5a097ed02 | -7.14569 | -48.67735 | 2026-07-24 05:10:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dadb073-a3a6-3322-8b1a-5b48a0913086 | -7.14526 | -48.68048 | 2026-07-24 05:10:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0516129-076d-3a97-8b14-ffe09886b511 | -6.15717 | -55.8171 | 2026-07-24 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e8cfe95-443b-3524-b8ef-d77b7ded3a78 | -2.39162 | -59.99473 | 2026-07-24 05:10:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2f02331-608d-3821-9953-37b4c4970290 | -6.64657 | -56.4099 | 2026-07-24 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87dc4cc1-76d5-34f7-a975-e5c8020157ed | -5.62388 | -45.97534 | 2026-07-24 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6561395a-ad2c-3d9c-a76c-a9472b5854e6 | -6.48779 | -43.78775 | 2026-07-24 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f14e5aa1-c6c9-3522-986e-e2ab78498fb1 | -4.88263 | -50.905 | 2026-07-24 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 915ba812-ab08-32c1-9a61-e6362df6634d | -6.56978 | -55.14078 | 2026-07-24 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b69510a3-b36f-35d6-bb87-2250d34b8503 | -6.48604 | -43.78472 | 2026-07-24 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 311e0d68-35db-3e03-9e35-901d4afca681 | -2.9056 | -54.56094 | 2026-07-24 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92fc1568-efe7-32a0-893e-b301ba02a55c | -6.64711 | -56.40635 | 2026-07-24 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdb47392-0d5e-3928-9264-e8c8d7272718 | -5.9685 | -51.40191 | 2026-07-24 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66acfd98-a1f5-3ed8-992a-08dc74b00ab8 | -6.57149 | -55.15272 | 2026-07-24 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a090102-2970-31de-81c6-c75f2b2eede0 | -6.56919 | -55.1446 | 2026-07-24 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aa3d812-1126-3937-a71d-bfad20e2702f | -1.78452 | -55.52515 | 2026-07-24 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa3ae3f3-b6a7-35ab-bae0-f2544d9be18b | -4.01473 | -43.27927 | 2026-07-24 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d1f7d5b3-322a-330f-b7bf-70918289891a | -4.37191 | -47.76988 | 2026-07-24 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9eb60a67-96ee-3177-ae04-90c07cf2aaa5 | -6.55363 | -55.15384 | 2026-07-24 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c37d5a6f-f95a-37f6-a5bc-2197fdf2dcac | -3.99972 | -43.28399 | 2026-07-24 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28711e94-a9da-39a5-a9fb-06ffa01baeab | -4.01631 | -43.28212 | 2026-07-24 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdf7d313-340a-3619-8b6a-04a7bb020d5d | -4.01381 | -43.28595 | 2026-07-24 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b6dc37f3-ffa7-3029-8189-30347ee3b930 | -2.81994 | -52.28869 | 2026-07-24 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e240f8d5-0afb-3b9c-bb40-303c9e2fd337 | -6.57207 | -55.14893 | 2026-07-24 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 344fd9d9-9a79-3759-8c05-26dc1d105d0b | -6.56861 | -55.1484 | 2026-07-24 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a3f7028-486b-32ac-8ac8-c103e9f56e25 | -3.15063 | -48.15079 | 2026-07-24 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 221cfeb6-5aad-34b0-add1-234d7a57b6d1 | -7.30975 | -47.0217 | 2026-07-24 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b69dc319-a2f0-3c59-9ca6-3f350aa572f0 | -1.78398 | -55.52861 | 2026-07-24 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cfdcc10-7267-3861-8fcc-9fbac89956ab | -3.2749 | -48.8298 | 2026-07-24 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c574eb0a-7fd3-376a-ab1c-7bc96d3475eb | -3.15108 | -48.14778 | 2026-07-24 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 083c8ec1-2bc9-32d9-a9ec-f4f11aad4a4b | -4.01729 | -43.27541 | 2026-07-24 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71dee10f-7eff-3d2a-aee9-036f3b2ef2b3 | -7.30382 | -47.01768 | 2026-07-24 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba220533-17c1-31d9-afa8-2a3659bb7672 | -5.32209 | -43.56005 | 2026-07-24 05:10:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3879d264-4c38-3457-944f-a69b88a02c39 | -4.01534 | -43.28882 | 2026-07-24 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc5ed509-0ea3-3de1-9fd3-d28e28871394 | 0.89176 | -59.69303 | 2026-07-24 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2750d9d-0f7b-3314-aae8-c0fd8f873014 | -3.99879 | -43.29074 | 2026-07-24 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e57ae60b-2613-36bf-ad26-dc348883942a | -2.71687 | -59.76819 | 2026-07-24 05:10:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22a0a9f2-0bf0-3529-a369-6499383fc07e | -7.43521 | -46.88456 | 2026-07-24 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37ec9c42-f8dc-3d83-8013-b7da51893740 | -6.4852 | -43.79131 | 2026-07-24 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca73b57b-3345-3c57-9d9d-83c8c9f192e1 | -9.17123 | -58.3087 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efcbb54c-d555-3c62-a7f6-53a7a8295503 | -9.16519 | -58.32558 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebdeb26b-b9c6-3cff-9699-0615ae2cf9a0 | -9.17399 | -58.31271 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa182ef5-97ea-3234-adf1-cf6de72f69a2 | -9.17675 | -58.31671 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 383171fc-9f93-3a70-851d-4b7a88f33c73 | -11.36052 | -55.43856 | 2026-07-24 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25ee5bad-1253-3491-9595-19c7fb58fafe | -13.45127 | -51.52352 | 2026-07-24 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c8d019d7-9f45-3d5b-b493-1510cbdd91a9 | -8.52007 | -54.76057 | 2026-07-24 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e590d94-1041-3995-8db6-00b16c3588a5 | -11.8524 | -50.33105 | 2026-07-24 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b92bcea0-921f-3e7e-9acf-2148e7f9739c | -11.5987 | -58.50948 | 2026-07-24 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0de34ca4-fd68-35da-b1f6-3d43315fac1f | -9.15803 | -58.32801 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29897329-10e0-3a10-b112-d642fe47748a | -9.22078 | -51.54391 | 2026-07-24 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c11fc42e-8f68-3f5c-bf50-db676304d568 | -9.1729 | -58.31966 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 814088f6-b26c-3537-b7e6-df5416fae676 | -13.43519 | -51.53692 | 2026-07-24 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7b906431-0c7e-392d-aecf-eb3f3e1f381f | -13.43048 | -51.53629 | 2026-07-24 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6c19871-84bb-3dde-b861-e72caec9b823 | -13.44656 | -51.52288 | 2026-07-24 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d3df5b34-d19d-37ee-882c-17fa0df05db9 | -12.16366 | -59.76033 | 2026-07-24 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15eac02a-b5dc-3d41-9fa0-03aa1a6fe47e | -9.1685 | -58.32609 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6a4d6b6-fdee-355b-8e4d-2b8786f5195b | -12.66102 | -48.20413 | 2026-07-24 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcc359d2-3d84-38ce-a3a8-203f45dff7ac | -10.23803 | -58.5122 | 2026-07-24 05:12:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd831599-57f0-384b-adc2-8bc5dc891585 | -11.61965 | -50.15264 | 2026-07-24 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd9174e3-4dd1-3455-abff-d37932f86c7f | -7.62782 | -56.72747 | 2026-07-24 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dc21982-18c9-3961-a5e9-06ad1100561e | -12.46766 | -49.45805 | 2026-07-24 05:12:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fabdda8-027c-3777-b507-a33fef0b72fd | -11.3641 | -55.43908 | 2026-07-24 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 230c2833-42c7-3182-afa2-9533dc70a08d | -13.44054 | -51.53246 | 2026-07-24 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e619f0a4-60ae-342c-83b4-dba2c21bf5f1 | -11.36112 | -55.43442 | 2026-07-24 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3505676d-bf3b-3356-a4dd-e9fcf8df0547 | -11.82179 | -56.59183 | 2026-07-24 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 701f0fff-dada-345f-b4c1-6f2ddc23ec1e | -9.16738 | -58.31165 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dba7a52-09f2-3b53-b062-0c3c8e43bd13 | -9.13753 | -61.06148 | 2026-07-24 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c21e395-7483-3020-a1a0-49b1349ac58e | -9.16462 | -58.30766 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0581a846-60a7-3af6-a569-74aff483f310 | -10.26168 | -59.03 | 2026-07-24 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 536c6131-c92b-38a9-9670-bd56b6089220 | -9.13636 | -61.0601 | 2026-07-24 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6e594bb-e29e-387a-8fc8-bbc0fa1e4de5 | -11.7884 | -50.39725 | 2026-07-24 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48176b6d-76e3-3098-ac5b-c3b3dee3cf1d | -9.13395 | -61.0609 | 2026-07-24 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1ab05fb-ef96-32fe-b4a7-b68e8a72fe80 | -9.16189 | -58.32505 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e369118e-2a84-33c0-bff7-9497f8f495db | -11.59594 | -58.50545 | 2026-07-24 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1df4c4f0-3a55-36c9-bf71-57eaf3732cf2 | -8.8253 | -63.90339 | 2026-07-24 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5238e872-90dc-313d-9245-739b9eb074d8 | -12.45228 | -49.58686 | 2026-07-24 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b450f89-37a4-33e8-9a1b-1bece0bb1532 | -9.16793 | -58.30818 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 909c0fd3-a26b-3e7b-884c-d890f31d3a3d | -9.16905 | -58.32262 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c790084-acc0-3fc1-b434-8fc799d0b3cf | -13.44119 | -51.52735 | 2026-07-24 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a3fbca8c-3f9c-331a-babd-41b8d89f0938 | -9.1762 | -58.32019 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47ee824b-1b9e-3c30-b147-b28c835fa3dc | -13.44185 | -51.52224 | 2026-07-24 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 027352c8-7e44-3e33-bc9f-7a56f64085b3 | -7.61226 | -55.26831 | 2026-07-24 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d775ffcc-b418-3c7d-a32f-731333b482ae | -11.5954 | -58.50895 | 2026-07-24 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c3229d6-2969-3a62-924f-b0b1ac6850b5 | -9.13327 | -61.06506 | 2026-07-24 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f247aa7-3603-319a-be41-30e7de592ed3 | -9.009 | -64.14993 | 2026-07-24 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95a43a88-8904-38c7-b2e5-1d1c5a6b5e54 | -11.62002 | -50.14967 | 2026-07-24 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7c93b92-61a8-3521-8903-59fabb4a22c9 | -6.88041 | -56.50379 | 2026-07-24 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e0f094d-044f-3279-97da-b0555d30ee7e | -9.13462 | -61.05676 | 2026-07-24 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e61b552f-1a1f-3e45-b530-a7cf8509f6b2 | -10.47257 | -62.44924 | 2026-07-24 05:12:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71bd5051-dd26-3e4a-ad51-be2d6a63a750 | -9.47792 | -57.31824 | 2026-07-24 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ed8987a-7239-3857-b0a9-252bb94bb2c0 | -9.17344 | -58.31618 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75d5191d-f035-331f-8b3e-63128e54254c | -10.64956 | -50.35922 | 2026-07-24 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
