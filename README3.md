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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6706f66d-db58-33e5-9f95-4d0f72e86669 | -10.47212 | -49.54685 | 2026-09-23 00:01:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4c61507a-8232-3310-b050-b785c16cebea | -7.12663 | -43.0808 | 2026-09-23 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 32282d4c-83f2-3838-bf05-ce4418e34c96 | -7.55982 | -55.0151 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ed533b74-da7d-302e-bbca-649732985583 | -8.32934 | -50.72992 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ee53e606-5c68-3d71-abf0-42d356654b62 | -9.57994 | -46.53648 | 2026-09-23 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3895103a-814a-3b35-9abb-7cebf17807bb | -7.81013 | -46.61641 | 2026-09-23 00:01:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 90e4b6c0-f446-347b-926f-dea1960c833a | -6.52467 | -43.53877 | 2026-09-23 00:01:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 568c8f1b-c818-3239-856b-758027176b07 | -7.17585 | -48.62498 | 2026-09-23 00:01:00 | TERRA_M-M | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 18.4 |
| d11a758b-da01-3e3a-a9d8-4d3cbb16a0b5 | -10.36321 | -50.45451 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3858c33a-3f7d-33e3-8998-d00178edbbca | -8.36833 | -45.60622 | 2026-09-23 00:01:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bfdc980b-daec-3c81-a08c-e57a43b20964 | -8.45921 | -51.48813 | 2026-09-23 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e9191b0b-f685-3ef5-90cf-4e95703f10c2 | -8.2562 | -50.87079 | 2026-09-23 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f99e3061-b89f-3260-99dd-b56aaf2b89a7 | -6.57648 | -44.14135 | 2026-09-23 00:01:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1a40a7a1-03ce-38ad-91dc-04ba910d3017 | -7.41249 | -44.73791 | 2026-09-23 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5c09fb8f-8d29-3e33-9e04-5727a17a46d6 | -10.44148 | -50.3502 | 2026-09-23 00:01:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 48b45571-e435-3dc8-92e8-687be2359d63 | -8.20727 | -54.72975 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 18704695-0dc5-331b-8f82-95826d6a3328 | -7.42687 | -49.83951 | 2026-09-23 00:01:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 86419b99-e9ef-39ec-abed-1829ddd17cf2 | -9.53231 | -45.37345 | 2026-09-23 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 657045ee-d6b6-3197-b9a3-c54405bf10ab | -8.91437 | -50.90468 | 2026-09-23 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 39d7364b-27db-3a83-be11-8eb6cb8ddfc1 | -8.46694 | -48.69201 | 2026-09-23 00:01:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b8812f4a-79a3-3483-80cd-4d3719f62d77 | -8.44798 | -48.70093 | 2026-09-23 00:01:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 209adf9f-a913-3759-9f91-2fcee7ecdc1a | -6.62356 | -43.75766 | 2026-09-23 00:01:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 64090559-2c09-34d0-a1d0-c1b20b851f8d | -8.27915 | -54.76595 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 3cc2b8f5-8f20-3a2a-b682-1d6f4d676929 | -6.92868 | -46.55412 | 2026-09-23 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 824736ad-9d41-3ab1-9713-939f99b9623b | -7.0302 | -44.64177 | 2026-09-23 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 48cb942c-8608-3680-b60b-74f7c01bbe6b | -6.78221 | -46.45708 | 2026-09-23 00:01:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d2f2bac7-2e4c-33f1-93b0-5a264f8d91aa | -10.8539 | -56.21812 | 2026-09-23 00:01:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 42086c6c-9ba1-386e-9105-81f31912e81e | -8.20515 | -54.71296 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| b64303fa-57ad-3cf5-a4b4-515d00b4e5f7 | -9.9069 | -48.44104 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a74ea3fe-d56f-39af-bc43-51f1892b9926 | -10.11802 | -46.09423 | 2026-09-23 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 89c54944-0761-39a8-9f5e-b196ac9e5187 | -7.82289 | -46.63638 | 2026-09-23 00:01:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b869b313-942a-3a0f-9b96-cbd61e1323c8 | -6.78401 | -48.66592 | 2026-09-23 00:01:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 675fa5bf-bb7e-33d3-8337-55cc3d911001 | -8.45558 | -48.69075 | 2026-09-23 00:01:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 69.2 |
| df5b49a7-9e20-3600-98a0-1aec9a02759c | -8.15185 | -49.5532 | 2026-09-23 00:01:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8f84f5e7-cb49-3a7d-90c2-44b1909a3596 | -9.51898 | -46.55145 | 2026-09-23 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f08c741b-ab36-347f-959f-1868c6fc3534 | -6.03344 | -44.03513 | 2026-09-23 00:01:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b931aa30-1c0c-325e-82fc-e621c7b620fb | -9.03867 | -45.00355 | 2026-09-23 00:01:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 15c13bad-a85a-3061-be09-2ea4d9a06a5a | -8.0832 | -48.8591 | 2026-09-23 00:01:00 | TERRA_M-M | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 22ed7989-2a7b-341b-89dd-7e9973ed7c00 | -6.78776 | -48.69297 | 2026-09-23 00:01:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8597fccc-98b9-304d-9360-f714d92b1403 | -8.28125 | -54.7829 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cbb30afe-3aab-3f65-90f8-0674d1f12489 | -8.59408 | -44.54519 | 2026-09-23 00:01:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 30110f39-01fb-312c-9c4b-d9e992de736e | -7.98203 | -44.09057 | 2026-09-23 00:01:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| c9217aa5-4731-3d98-8120-81bdcb2220b0 | -7.50127 | -44.32978 | 2026-09-23 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f7382e13-cea3-31fc-8337-eebc796b95b6 | -6.78651 | -48.68395 | 2026-09-23 00:01:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 124.3 |
| a6f8fb3f-c631-3e90-b69f-717506f53536 | -6.78526 | -48.67493 | 2026-09-23 00:01:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fd65a96c-813f-35ce-9285-ccbb8533447e | -10.25269 | -49.96869 | 2026-09-23 00:01:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cd7240b6-10f9-39f0-9693-131e5e5c8eab | -10.04533 | -53.77856 | 2026-09-23 00:01:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 7b371449-4800-3b0d-88a5-703a460c0627 | -10.31653 | -50.51634 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 00e11cf2-846b-3c46-ad61-cff40564173f | -10.03395 | -52.10884 | 2026-09-23 00:01:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8b247d56-a565-3ba9-9b15-a42be85c959d | -6.1042 | -44.14027 | 2026-09-23 00:01:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ac0f8310-8f45-3412-8dfc-c3222d169dde | -9.94717 | -48.47161 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 2e8a3d3b-2c0c-371c-b40d-f78cea999203 | -7.55511 | -55.02761 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 76aec437-0968-38ba-9e20-42a93d007d7f | -9.56228 | -47.95756 | 2026-09-23 00:01:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5e9a072e-c730-384a-b7da-2db54a4f02e8 | -7.45535 | -44.56061 | 2026-09-23 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0959eae0-7e3d-3dbc-b9a2-21b0e1db643a | -6.00636 | -44.26311 | 2026-09-23 00:01:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5d04bf10-7742-3516-9636-83b490e257c3 | -7.42929 | -49.85731 | 2026-09-23 00:01:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7168217e-9f1d-3fdb-9b8b-12fcef151a25 | -6.61139 | -43.75955 | 2026-09-23 00:01:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 135.2 |
| f74a1724-a0cf-370d-bbd4-9ff8055fde8a | -5.99461 | -44.26531 | 2026-09-23 00:01:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b277dbc9-8737-3fab-935d-ee2c9c22f2a6 | -8.47055 | -50.20863 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ff9eb873-7b4d-3179-b2f1-e099ac0068b3 | -10.45184 | -50.35847 | 2026-09-23 00:01:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 02b0c551-3075-354a-bead-d8a875e05b80 | -9.93834 | -48.4729 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dc48e6e8-e6c7-3267-9a7c-6faa933bbe20 | -8.25493 | -50.86131 | 2026-09-23 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b47281e6-4cd0-3d8b-8e03-e5ec7bca4cf8 | -9.56358 | -47.96673 | 2026-09-23 00:01:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1bb26b1c-d638-3a9d-b798-98427cbb3f94 | -9.6089 | -43.95473 | 2026-09-23 00:01:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 2bfa8509-a499-3753-a5b0-999a3f4aa327 | -8.45805 | -48.70856 | 2026-09-23 00:01:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 027477ef-90fc-33a9-80e9-8d4ffcf4bc05 | -10.37646 | -54.41279 | 2026-09-23 00:01:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 001e2bef-4d9b-326a-99e9-0252d7898b88 | -6.03839 | -44.02891 | 2026-09-23 00:01:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8516fd3b-24e3-3079-8d84-f16bce80ff56 | -9.39427 | -47.75063 | 2026-09-23 00:01:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2d9a33bc-11b4-31b6-917d-e6d699b16c5e | -9.54927 | -47.93747 | 2026-09-23 00:01:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1675c59a-5209-3545-8b17-9a942ff5c505 | -10.04642 | -53.78475 | 2026-09-23 00:01:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| a6e3b07a-8c2f-3aae-a42d-183316eb462b | -8.48577 | -57.60914 | 2026-09-23 00:01:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 8596377f-4d6a-33be-aa03-02436ef99a87 | -10.61905 | -53.98683 | 2026-09-23 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 3f0b3b72-37f2-3430-b0fa-f39541cfc0ec | -8.1821 | -54.81884 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ed79752f-7406-3538-b5f7-85819b26a21d | -9.62991 | -43.94479 | 2026-09-23 00:01:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 29.6 |
| 589b08f5-cfb8-3cf9-bdfa-e9f18648025d | -7.521 | -45.40627 | 2026-09-23 00:01:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1ac05d86-d2fc-3b43-a372-5ad4c23a2172 | -9.01759 | -49.82178 | 2026-09-23 00:01:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8c97c6be-67eb-3ddc-b9d7-9fa211dc7318 | -8.37484 | -50.72692 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 794ee469-40c7-33c8-80dd-b9de2f5f928b | -8.73741 | -47.60357 | 2026-09-23 00:01:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| dee11b3d-0b7f-3d62-86c9-8ed0ef068d84 | -9.96999 | -50.26298 | 2026-09-23 00:01:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0b51393a-eff0-3215-8c47-90dfa61ec436 | -8.79007 | -45.62225 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| daba3c70-137a-3e5a-9bef-d0e281504000 | -6.88133 | -46.57198 | 2026-09-23 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 82818fd1-564e-367d-8f90-2d0f9eac8ae6 | -6.90091 | -46.56932 | 2026-09-23 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9c0c6643-1f0a-3d79-a073-95da7fc1a275 | -8.45163 | -55.02022 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 83cb6ec7-302f-35bd-87ae-cd920c512088 | -6.52948 | -43.55116 | 2026-09-23 00:01:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| cc060e48-21bd-3b7b-8d40-dd6d304270d7 | -9.94841 | -48.48054 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 1eb4b2f4-1984-36df-9bf7-9a5be438288f | -6.92205 | -46.57747 | 2026-09-23 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b0173d8d-0b7c-32ec-84b5-5cb9ed9187a9 | -10.48972 | -50.29507 | 2026-09-23 00:01:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fd81f424-959a-313c-9f82-8830149cb30e | -8.19331 | -54.71452 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 2d6373dd-11dc-3207-aedb-24ab35757354 | -10.47089 | -49.5378 | 2026-09-23 00:01:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8bceffe9-de78-3625-ae4b-8baf6d61017e | -8.34594 | -47.24364 | 2026-09-23 00:01:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c020bb18-eff6-3b2a-9eb9-cc8a2f17f34f | -7.64022 | -49.52684 | 2026-09-23 00:01:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f41615c-a871-3ef6-9183-0e64760bffa6 | -7.17712 | -48.634 | 2026-09-23 00:01:00 | TERRA_M-M | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c5ab5ab4-a621-351a-a05e-241cdc1dab5b | -9.86284 | -48.39888 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bcc57d6d-6030-3ca4-a3c1-1cd637a127cd | -9.04539 | -45.00931 | 2026-09-23 00:01:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| def6235a-dc1a-3902-8978-9a42b3beb659 | -8.78174 | -45.63586 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6b42f9e1-fabf-333f-9e5b-8404b8e0360f | -9.59524 | -43.9411 | 2026-09-23 00:01:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 7a45f796-9dc9-3195-94bd-997d780f1a1f | -8.86459 | -50.18808 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bf9ccb72-56ea-350d-80b1-28fe240cbcfc | -7.42808 | -49.84838 | 2026-09-23 00:01:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| aaad399e-029d-3c5e-8383-44942b5710f0 | -9.56098 | -47.94841 | 2026-09-23 00:01:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0d0aab17-54b2-3b01-a3b2-14861cecbe5b | -9.17461 | -51.47758 | 2026-09-23 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README4.md)
