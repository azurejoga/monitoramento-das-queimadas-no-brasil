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
| 8982f6b4-f6a0-3c54-902b-24e08fcc0ec7 | -5.87351 | -43.847 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b1079ad-d720-3c72-9d98-cad5261afea9 | -6.39942 | -42.55982 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b54ab691-1167-3df5-8c64-7b568f9d90f9 | -6.36876 | -41.48595 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f612a97f-98c8-38fd-b943-e15ab67660a7 | -6.02871 | -44.31777 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01ebafd7-8555-3683-b3b5-00625a0e3279 | -5.86935 | -43.84658 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 764b488d-5a69-3f21-983b-cb9eaafb70a3 | -8.06667 | -45.41999 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3f8bd46c-9300-3ac6-89a4-15c03228b607 | -6.06402 | -44.3119 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f44c278-00ac-332d-abfd-5efd006b1bc2 | -5.45753 | -41.02176 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 133a64ca-c53e-3dfd-bcc9-0f5b0fa9d4e7 | -3.38952 | -50.26647 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a4b498d-c331-361a-9617-3b8a9752395b | -6.17701 | -44.30663 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d97343d2-dd19-39dc-be2d-c31689806343 | -7.18704 | -42.36465 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| aa3f7143-6785-3d42-bf6b-eff2b85ce363 | -8.25633 | -44.08999 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40198580-9066-3b03-a007-c10743f36540 | -4.66986 | -44.09468 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 4d0fb8a2-4fd2-3b0c-a554-a13d37abe70a | -4.71915 | -46.16187 | 2025-10-16 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acef8f5c-da5c-3b6d-881b-c7a090f4a1b4 | -7.50225 | -44.6629 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61173d2e-36a7-3c17-803e-7f6211d1c072 | -5.47608 | -42.9346 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8012a467-27fd-3a1b-90af-0f3772d05b4f | -7.9606 | -44.13657 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 001014af-49f8-35ed-88cf-1e0c2105a690 | -5.08755 | -45.45388 | 2025-10-16 04:38:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df64d6d0-2200-3683-a8bf-834ae669ad36 | -2.87077 | -50.72976 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afd2faa4-a5d4-3355-890f-17997157183e | -4.36479 | -43.39978 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8df3a206-3381-3f1c-867f-7083ed6827de | -3.07799 | -51.17023 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cef477a-440d-3f0d-a7e7-66d2b4a6c64b | -3.27789 | -50.04356 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9974de7-8e82-3c7e-ab5f-a20a993bb813 | -3.35201 | -49.25062 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffe69e54-1430-3435-ab84-125e2c6cf494 | -5.69251 | -42.68367 | 2025-10-16 04:38:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 75b6c707-9033-3742-bdc5-d194cfdec19c | -6.51536 | -52.38865 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4818594-7d55-32dc-a856-479c53a950ae | -3.01973 | -45.3809 | 2025-10-16 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| c216bcb5-2021-323e-b129-b729ab98f148 | -7.07953 | -44.94635 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5faba920-e6fa-3696-a33d-76d77aaf7898 | -4.40454 | -43.39027 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77030b8e-7d07-3616-9a84-de2517b00731 | -4.66292 | -44.08654 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b58bf1c-526f-3720-8238-7f7cbf3b55b2 | -6.19364 | -44.10542 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b97cd3df-3ef0-323c-92b2-f9fbbb7688ae | -6.21569 | -44.15276 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cd871a4-07be-30c0-86cb-4e7b69909adf | -5.86746 | -41.23185 | 2025-10-16 04:38:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dbd17fdc-d6c4-342d-8422-8730712aa403 | -4.84309 | -42.799 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 555896a5-c37a-384c-9fed-4262a70bf170 | -2.9278 | -48.30495 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55d7455c-49f5-365b-a5f3-ead6731f7503 | -4.80874 | -43.20517 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17d1aa8b-d38f-3238-8c70-8953a1f02c20 | -7.39383 | -44.74739 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c7b1c9c4-917c-3379-8d74-2062f75ab05e | -7.25853 | -47.36295 | 2025-10-16 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 130ecdcf-1fba-3bbf-9593-35b0676fe144 | -6.06822 | -41.90204 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e57d660-075d-3974-8f87-8f6f5b159aa4 | -8.29273 | -43.40223 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| baa80ce8-ad00-3136-80e5-7150e365058d | -7.16478 | -42.52007 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b203b1f-d1ab-394c-9f7c-20bd4147c182 | -7.09751 | -44.27067 | 2025-10-16 04:38:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d684ab21-574f-383b-9f99-0b6057c29b88 | -8.28951 | -43.39293 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 729322e7-d966-3ccb-9ee9-9f7b0b8b70d4 | -5.54511 | -46.35192 | 2025-10-16 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 943b60fa-a064-3b01-bea6-e55981da894b | -5.42518 | -44.23878 | 2025-10-16 04:38:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc98df49-404f-3ed1-ba90-f42e98b1e850 | -4.3945 | -43.40052 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2fbde2af-0bd5-3282-b350-0fae8c9a6322 | -5.7329 | -41.31338 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 65fa4c79-f048-3587-85fa-61201d8e0a79 | -6.16465 | -40.90953 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 57380919-da01-312c-b471-99fa3301a2fe | -2.72954 | -48.30933 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 381501ff-97ee-3c96-9fa2-457d55b2281d | -4.67836 | -44.10609 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1558d46-d7d3-3598-9038-1817e48a51e5 | -5.3059 | -49.57369 | 2025-10-16 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fad06282-673c-379d-906a-7c47db4b5302 | -4.3998 | -43.39351 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| d075f4bb-6140-3863-8046-f258a2ecc7e9 | -5.87623 | -43.88575 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e0b8579-7aaa-31e6-bb3a-ac460ab6f8ec | -3.84641 | -48.15622 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af6cd643-10ce-3971-ae24-e3c889029256 | -5.17739 | -43.13565 | 2025-10-16 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34e79525-81ef-3ceb-ba1d-f532036d198a | -3.4286 | -50.25024 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43fe5d3a-7741-3787-a99c-47d5d090248c | -7.07639 | -45.44648 | 2025-10-16 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 652c59b2-1e9e-399c-a2c8-673bfa98c3cd | -6.02183 | -43.396 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66cd4e52-3f12-3e1b-9f38-cff66bc8f6aa | -6.16588 | -40.90072 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 11c0841e-f8e5-3d9a-88f4-0d62589cb9f9 | -4.59369 | -43.57478 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec7d4633-4a1a-3c53-8d67-bbd1d6900242 | -8.27162 | -43.35912 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 25a180d1-2e45-3ce6-b4c6-774a165dfa6c | -4.01847 | -44.17811 | 2025-10-16 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4300210-a4e6-3f88-a191-3edc85d3b742 | -6.05183 | -44.24546 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eec21716-445a-34bb-a168-09136b602eea | -8.25437 | -44.10891 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 167b7c58-c48a-3771-a613-d63a9509a44b | -5.24743 | -43.22463 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16784355-b84e-39e8-81e4-3b185e217e21 | -4.67984 | -44.09588 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76634d3f-df29-3d42-9229-67c8e2287c36 | -5.43821 | -44.23357 | 2025-10-16 04:38:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 376d5c39-a9ef-3a63-8297-3e6c5ca592c7 | -4.9235 | -41.5542 | 2025-10-16 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c57ee91a-4c0f-3431-9927-1832506fd043 | -4.37478 | -43.38971 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 6d1143a6-1adb-325c-8c5c-6e346e99d179 | -7.2061 | -45.48701 | 2025-10-16 04:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f637e718-92c6-387e-8be2-8bab7316b3d2 | -6.11247 | -47.29028 | 2025-10-16 04:38:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47a8b76c-3021-31f1-9511-d3d71b16e5a0 | -4.86936 | -48.64574 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10e146fd-d449-36f6-a19c-c6aab890065f | -3.81436 | -48.96786 | 2025-10-16 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d045fbc8-4a47-3dec-b5c4-be3b5b51587e | -4.28672 | -48.58233 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31a77e56-52b8-3bcb-962a-a6ba994785ff | -3.43384 | -39.65174 | 2025-10-16 04:38:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 996310c1-7b61-3fe7-bdd0-d11646eb017a | -5.61636 | -42.68377 | 2025-10-16 04:38:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4f3e4749-b115-3440-b812-238b54b92161 | -8.25128 | -43.34253 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c47de29a-3d35-3771-bfbb-196e99d1a89d | -4.66032 | -44.10376 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b5b8ea0c-d0b5-3f01-8167-cd3acc5d6ca9 | -3.09069 | -51.24789 | 2025-10-16 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 368c9baf-9ca0-3728-b329-eaa4310c09b2 | -6.12598 | -44.28192 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 704bbde7-ecd2-3fc3-8a9d-2409a7e93509 | -3.88199 | -52.07204 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9163de31-e044-302e-869d-fff5709176ae | -7.37068 | -44.68285 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69c2f1ac-b13d-3305-b2d7-131d89b2d8cf | -5.3307 | -43.9422 | 2025-10-16 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d758b4e7-dcf7-37e9-b40b-72b11943bfb2 | -5.51355 | -47.30782 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 727188dd-0510-3930-b914-12e738b9ffb5 | -8.25613 | -44.06496 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 599ceaf8-a3ac-324e-b589-65a138fbdd62 | -2.79782 | -48.94107 | 2025-10-16 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a1e769fc-7011-39fe-be8d-1e842eec40c2 | -6.53878 | -44.69485 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e661b249-f152-38c1-a045-a799f5588ca8 | -3.13546 | -50.21189 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c5c5a17-18c1-3348-af61-12706e62c783 | -5.92379 | -44.72726 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7392afeb-82b2-3f67-8383-0b2484965cf5 | -2.8742 | -50.73029 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| abe3e6bf-ae06-3a10-9ce1-77c7767f0794 | -7.34657 | -43.8642 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 69a14620-d682-3fc0-813d-13f250fb6875 | -5.56754 | -45.38782 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85780a29-b0b7-3a42-88f6-3be38098551f | -4.40037 | -43.38966 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9f8c75e-7d4c-3ea4-a23d-3cfffc73e178 | -5.4377 | -44.23707 | 2025-10-16 04:38:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e120ec1-d608-3423-a2c5-a989ebda642e | -2.5756 | -54.66241 | 2025-10-16 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 941c758f-a238-33a6-8e83-58777eeeea7c | -6.38867 | -46.81055 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be6a9fa8-e651-3336-a396-3e9dcaad9f48 | -6.33577 | -44.01201 | 2025-10-16 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed8024f2-4249-3d13-8b51-921635b8a78b | -4.84936 | -42.78687 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75ebd6cd-a0e7-3869-b6de-87e538dba827 | -4.36644 | -43.38839 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 53701bd1-a1b2-35eb-b15d-c0f9faae5622 | -7.47621 | -47.01863 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a4b7b06-ed48-31db-9f1d-37e3d2127a7d | -5.41999 | -47.11552 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README49.md)
