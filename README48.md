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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e37738c6-ae07-3cb3-954e-d3b87bcb1318 | -3.7901 | -46.70292 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66619144-bf86-39b6-9b7c-81d58be829d6 | -3.63383 | -50.14504 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 144b2fc8-0bad-3215-a542-3029556a4ebf | -6.81785 | -46.77351 | 2024-12-03 04:29:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51d12bc4-3ca0-3f5b-9c1d-ab0b6a2e3982 | -7.56511 | -45.73506 | 2024-12-03 04:29:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d633f19-5a52-3b6e-b380-3f480e54b6ef | -3.94204 | -46.92468 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48af1aaa-d0f2-3a39-90e7-bff83c520952 | -3.07386 | -53.92165 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd6e77b4-abf5-343d-bde5-51b716752273 | -2.68262 | -46.14072 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87e2c645-636f-3dbe-be55-044cf0c778d4 | -2.35842 | -47.14479 | 2024-12-03 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfde1c67-4c03-39c8-a355-b707428c160c | -7.23961 | -46.74404 | 2024-12-03 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a774a8b0-4656-3ead-b652-499e1c6e25fd | -3.12303 | -45.99413 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4cc05439-cae1-3245-b35b-b8fe724469b4 | -4.09336 | -44.85836 | 2024-12-03 04:29:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d8135aa-d7c0-36c7-b616-591be036b1ec | -5.10967 | -43.21377 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 569d1ade-532f-3c35-a55e-3a0565eef244 | -3.79374 | -45.32531 | 2024-12-03 04:29:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4020a30-b655-3700-8bb1-8752e8eab123 | -3.18326 | -46.43515 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a10416-95a7-3b06-b7c7-de1bd2ce87af | -3.08917 | -53.25462 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a848099-8979-33cf-8560-41023c51b9f8 | -5.79682 | -46.48558 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| f7af2188-d82e-3482-869d-8b0cf071d319 | -3.58643 | -53.05087 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdc1977b-cdf0-354f-ad40-8524b53af6ad | -2.52067 | -47.06491 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 220a9c95-f018-3531-a3c8-0aff351080ec | -2.33559 | -53.80926 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c73cf795-21a2-32a3-8ec0-f26b82d08284 | -2.73003 | -46.29371 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85f8ff20-5a23-39a7-9277-dfd62696128e | -3.2143 | -50.07476 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15437bd0-ef4a-349f-8d94-044b2582bf82 | -3.93266 | -46.9197 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d86efed-7563-3ab9-aaec-52a11394e367 | -3.25099 | -51.14035 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53c90ee9-db73-3e9e-b2e9-daabf31e183e | -3.29632 | -53.66203 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 70aeb9d5-0872-3a69-8895-fce96e7147e9 | -4.56286 | -45.47107 | 2024-12-03 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ac5509e6-102a-353a-9dd7-5428026d3248 | -3.18406 | -51.16778 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1654700d-16c8-3abd-86bd-5b20ab282097 | -4.17036 | -48.77187 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69c24295-7cfc-3b95-82b3-68d2da87f3b8 | -2.81852 | -53.05903 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 11f12608-09b6-3ac1-80ef-aab32c159187 | -3.92216 | -52.39225 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 260cff42-f282-3caa-8277-b7ef26c2651d | -3.53852 | -50.17696 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 377d7629-1f71-394b-9d3e-39a49252ff4a | -8.13916 | -44.47545 | 2024-12-03 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66308163-ca8d-36e6-8fc1-60c46edf1076 | -2.55792 | -46.56703 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8494cbe8-9e53-3925-979a-f40457af6b35 | -4.55928 | -45.71768 | 2024-12-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43a9420e-c822-393b-8031-3a7e3fefb951 | -2.60343 | -46.58154 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d37a584e-7fbd-3f9e-af7d-57568833f8b1 | -2.75455 | -46.11623 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb654745-ee91-363f-873e-8e96c54887cf | -5.45311 | -43.57959 | 2024-12-03 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8672d752-72a5-3a3a-bd23-22dd3ae8179b | -2.55174 | -46.34719 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 500d9a8a-8d37-3179-8a4d-ef81d7442871 | -4.32443 | -45.51812 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5d88d05-3437-3503-b8c6-dfb0ee92248e | -8.13545 | -44.47491 | 2024-12-03 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73e960d9-a4cd-3cfe-9cc2-1d250aac04db | -1.93018 | -53.44475 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7fca528-8962-39f1-978e-667e83daa6b7 | -2.84181 | -54.10441 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f14a312c-4a7c-3b13-b3b0-e4f9c30a9610 | -3.30928 | -53.37027 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 632f6ae0-452f-3f90-84fa-9ecc85df7419 | -2.72177 | -46.30307 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b965cfcf-e5d8-3c1b-81b0-4b718fd60d76 | -2.54577 | -46.55809 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efd591eb-a9e3-3afc-bd45-f4032c0bba6f | -4.26269 | -50.85007 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c21b5081-205b-368e-9f45-83a6e30bf94a | -4.11677 | -49.06586 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1764bc3b-2060-38a9-afb5-094cc246859a | -3.17319 | -45.78156 | 2024-12-03 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bc77ffb-302e-3f51-9567-7a9676953766 | -2.56114 | -46.35214 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 827cf959-7d0f-3bcc-89f6-4c6f4da13b73 | -3.7978 | -46.69705 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f166b5be-8516-32fd-96ef-98acc7a98ca4 | -2.43998 | -54.00629 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c50d8940-89c0-3aa4-b68f-847f445a7795 | -2.80387 | -53.03968 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f8c88ce-8a81-3187-91c4-2a243b5cb882 | -2.55407 | -46.56996 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77ebf326-4fb9-38ff-bb16-c0b4409654ce | -3.33478 | -46.05176 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 697ab7e1-759f-36c1-a97c-84d12cb44674 | -2.68342 | -46.61158 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b73a929-97e5-3b2c-a538-fd710b544c7a | -4.93889 | -43.77834 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 032d2d45-c5bb-36f8-8f49-5a9a5dd4fab6 | -3.85472 | -46.52867 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b279e1b7-8788-3339-8cc5-73b00d8bc84e | -6.18591 | -43.41245 | 2024-12-03 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5b0dd667-9cfd-3515-b027-8b2dd6eec2d3 | -2.31302 | -47.28235 | 2024-12-03 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a152cf7d-4cff-3ade-a4ba-c00c28960ac0 | -3.34431 | -51.21033 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5eee3a0-2b59-34b2-add7-4007c0279c88 | -1.75597 | -52.7995 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41dbf5f2-d1e8-3399-9969-7bababcbb68b | -3.0814 | -53.3853 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 6d96780f-d4fb-3780-9ce2-5f73c34dd370 | -3.98073 | -46.52714 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bff5591c-a9d8-3498-96d6-91078d710661 | -3.08622 | -47.9583 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a86744e1-d7e8-33a8-8016-af70b5cb50fe | -3.80849 | -46.58531 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ef4eca3-b9a5-3b8a-84ae-bb2ae30a923b | -5.14277 | -43.2284 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ebd82da-d5b4-37d8-941d-751662159fb0 | -2.64697 | -46.58477 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad383c55-2bcb-312f-97df-dea15eb9d66c | -3.16156 | -46.55212 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0501dc77-7356-3dba-a266-0aca08868d8b | -3.89832 | -46.68472 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d5d8340-795d-311e-b198-778c50049bae | -5.41267 | -42.93011 | 2024-12-03 04:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9ad3b0d4-ff67-36b0-9453-8b412ec441e0 | -3.25043 | -53.93462 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6da95ec2-7ff7-3689-b967-ab34000ad9fb | -3.26315 | -53.62597 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8cb05f21-4a97-39f2-a7f1-737100bca696 | -3.29483 | -53.67085 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4f260f0c-62b1-337e-8e04-ac07b099c0b4 | -2.5728 | -46.19096 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf81e0f3-88d6-3a32-bd0e-f8f2ea8a4e50 | -4.52487 | -45.7383 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d23cb4ed-a758-3a0f-91ce-576655ce69c4 | -2.57061 | -46.57253 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4735444f-a029-3ad2-8997-1b05eb1dad9e | -3.29111 | -53.66561 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 5fdf517e-7984-36dd-881d-8a502f6a1037 | -5.58851 | -44.89632 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36ddf51c-c537-35c9-82ae-87bbbeddcd72 | -3.68915 | -50.75786 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c7ab46c-7fe2-3b8b-9736-1fd92965303e | -1.61733 | -52.68701 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2113288-d31f-397f-b96d-11ecb52d7002 | -3.01799 | -54.03708 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a505f0ed-8aec-369d-9656-304825b9124e | -3.54945 | -51.45775 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0a1edb1-bfaa-3032-99e8-bdde23fe716b | -2.46962 | -53.70763 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9fffc3d-3b23-3996-8064-37d0dc78c6f8 | -2.48353 | -46.56606 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbb3989b-f960-3e21-a7b0-c7f27ac8546d | -2.88424 | -46.80479 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2db3317-168f-39af-8a4a-e76adf7e3033 | -3.37044 | -45.84409 | 2024-12-03 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07ff1302-c90b-3b70-8cbe-21d2fcbfc42a | -2.85051 | -45.39572 | 2024-12-03 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 433a5f0b-fafc-39e8-8a06-32b7319a23e8 | -2.57225 | -53.97484 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cdc333f-75b1-3da7-ac3f-0ad14d963b58 | -3.80442 | -46.69808 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0acda753-1861-3a69-a8b1-c646e9189e03 | -3.84863 | -46.52417 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fc22241-deeb-3253-8844-701e637ff56b | -4.39126 | -46.00855 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4be1c7b-5935-3a6a-a75e-73a09261ad46 | -2.83849 | -46.68486 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66a061bf-2166-3952-9566-5ddd06f330b4 | -4.04563 | -46.87033 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9849747e-352b-3d6e-96f6-943ddf943288 | -2.65311 | -46.61039 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c10f7a4-4570-3bba-a93c-444135a0f08a | -3.25944 | -53.34428 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ff5509e-f1fc-304e-8216-c6d4ccd42a8b | -5.81909 | -46.47458 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd2f566f-14b2-306d-9ff6-342d1f56bfb7 | -1.7553 | -52.80363 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e17b459-a0fb-3328-bac1-7ed63929df85 | -2.71318 | -46.18459 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 306a777d-72bf-32b8-b7a8-413661dd9235 | -3.26014 | -53.34003 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2357ef0a-519d-3748-a088-8360cc7dac1a | -5.00105 | -42.94608 | 2024-12-03 04:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71d108fc-a437-396e-b0ee-52246b90fa4f | -4.61322 | -48.03443 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README49.md)
