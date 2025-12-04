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
| 5f3b2e51-e1db-3177-a044-f56590006ae6 | -4.06472 | -46.56302 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bdbd6404-924c-39ff-bd0a-cc5a973761fd | -4.47694 | -42.39607 | 2025-12-04 04:21:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a0a84fc4-493c-3868-baaf-f2be8d387217 | -4.20373 | -44.25558 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87fd0917-6296-3dd6-a568-f7c10b846817 | -3.84729 | -47.8339 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c6b424f-0074-35f0-9c5b-a7416cc8bf95 | -4.50732 | -40.50557 | 2025-12-04 04:21:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 899687b7-566b-333d-b3f1-98b7e3fa3df3 | -3.40794 | -44.98831 | 2025-12-04 04:21:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| bac02b10-3182-3873-823f-646f3b6647eb | -3.32648 | -44.3819 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f9302e3-e581-3a76-90e4-3cf7f0ea9d8e | -3.32594 | -44.38535 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a8e84c0-771a-3b36-8298-d74c87f718a2 | -5.33213 | -43.56083 | 2025-12-04 04:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6565fcf3-f22c-3732-a834-8b7180d323e5 | -2.57428 | -48.22009 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7b09f4f-bfbf-32c4-a80d-02db0e554358 | -4.85692 | -44.88182 | 2025-12-04 04:21:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29f7b844-f44f-3439-aaee-d0d2fce2be47 | -2.13885 | -47.87846 | 2025-12-04 04:21:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a88ca57e-9c0e-3fd7-a327-36dd0a996978 | -3.1414 | -49.41353 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3003420-087d-36b8-bdd9-0482ca7ff140 | -2.41137 | -48.08906 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8deed4c5-ebfa-3776-907d-bb8a1c9ff99a | -4.10791 | -46.3165 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee07c7b6-64e1-304f-add0-9eeff707934d | -4.77422 | -46.12658 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 312a8d9a-c167-3c9d-be51-f4f90e2bc040 | -3.36802 | -44.09592 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37720121-88a8-3fb0-a62d-b37e1187978b | -5.99131 | -40.36923 | 2025-12-04 04:21:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1b49bacd-d373-3340-85f6-ba48d8c79d5c | -6.00934 | -42.3243 | 2025-12-04 04:21:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c217cf8d-c1d8-3f2e-a10e-0885e38af5c7 | -9.28684 | -43.15368 | 2025-12-04 04:21:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 829d6f5c-433b-33a4-be40-946c242aae1d | -4.73244 | -45.70763 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80c8d2b5-592f-390b-91af-aea677d17056 | -4.05322 | -46.61225 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e8aa581-9f7d-36df-9651-378a6e094f4e | -4.38851 | -43.13385 | 2025-12-04 04:21:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 69d9731a-e0a2-350e-a3bb-81a8bf91d823 | -2.89396 | -45.2261 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19fb68d0-2822-3c92-94c1-d9e21d9a8086 | -4.7875 | -45.62137 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2a4e83e-161a-3f17-bf99-a41d9973fab0 | -4.58409 | -45.10189 | 2025-12-04 04:21:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e1c0ad8-5a99-3bcd-9652-b06e9679b579 | -3.12635 | -40.23417 | 2025-12-04 04:21:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 129a466d-2b4d-3ae8-a2a6-fe2ca28d724b | -6.33141 | -39.82522 | 2025-12-04 04:21:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c0f11fdc-4f7b-3fe5-b563-c9fb53d71b8d | -2.48262 | -49.41106 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b863acb-42bc-3696-af0b-db0d94875b6e | -5.57137 | -45.42017 | 2025-12-04 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e84218b-4c58-3f07-9b81-57f88e67f9d7 | -4.20757 | -44.25265 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24c601c0-0673-37cf-897d-46ce71298799 | -4.21679 | -46.35995 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4cc059d-6d7c-3cb4-9cc3-00eb3d68fcd5 | -2.57846 | -49.09383 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22f54462-c212-34b3-9f92-ee38fb0ecc25 | -2.79226 | -48.90388 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e821bdf-1a65-3105-bdb4-fe2ab96c8ea9 | -2.26394 | -47.84818 | 2025-12-04 04:21:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1833e169-a282-3a4e-b329-187561d92f31 | -9.30643 | -35.63954 | 2025-12-04 04:21:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 89a451fa-367a-371f-a10c-b4f7b64f1605 | -2.63062 | -47.31084 | 2025-12-04 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45a9ccf4-d4be-3804-8f4c-90faa306b2e0 | -2.70632 | -49.31441 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 105e29ee-b7f6-340e-b9e6-a93495047d82 | -5.95676 | -39.70539 | 2025-12-04 04:21:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7120d0c4-9654-3236-ad43-6ec7a116cb73 | -2.38288 | -49.38399 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e3dffeb-0405-3b10-b4b0-8efbd91ee16f | -2.53544 | -47.31958 | 2025-12-04 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c47f9ba7-f995-3526-af02-7f572237e199 | -4.25733 | -44.15116 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d16b6f45-654d-36cb-bf40-f0e959cea59f | -4.67993 | -46.38531 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf47b6df-9e8f-3aad-be15-76c9bcf9da23 | -5.18321 | -40.15726 | 2025-12-04 04:21:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1b28fb1d-1086-3a79-b5e4-4a4239d64295 | -2.8341 | -48.02315 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1789caa7-906b-37f0-82f4-e302963f5a01 | -3.85494 | -47.05182 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c2a302c-a362-3e76-8024-232e79df53ef | -4.69339 | -46.43378 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8f521e5-0c89-3746-b9db-525a33041ae7 | -5.98708 | -41.89089 | 2025-12-04 04:21:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dffb122d-d69c-3a5f-b74d-26962ff5bae0 | -3.23412 | -43.34103 | 2025-12-04 04:21:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 779bfca9-d2ed-3494-9b4e-ba25a3175c5c | -2.26445 | -45.05481 | 2025-12-04 04:21:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17d42820-7013-320d-810b-baf8ffb12efb | -1.98548 | -46.13213 | 2025-12-04 04:21:00 | NOAA-21 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bd87d16-70d2-3ae6-ab55-49f94d59e6ff | -4.66784 | -46.30674 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 599d56a5-f221-3ff0-a365-08133330f710 | -2.92397 | -48.23122 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19876dbc-d1e8-358a-8f4b-d3de80b573e2 | -6.43626 | -44.7891 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a185233a-575b-37db-8d30-cbf8d94b9ea5 | -5.34055 | -42.11673 | 2025-12-04 04:21:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3fbd53f8-ed61-38a4-a6fe-f4fef0d1fbb0 | -6.91606 | -39.61232 | 2025-12-04 04:21:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eb18847f-cf45-3b9e-ad97-e15be322a6f9 | -5.85442 | -39.93192 | 2025-12-04 04:21:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d668e25e-3971-3bdc-bf77-321c4bcbf9d2 | -9.33037 | -36.95515 | 2025-12-04 04:21:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 78f9502b-e5e6-3390-b785-a55913dd84fa | -2.53201 | -49.45849 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cdb26e7a-b2a9-386d-bd2f-cd0cc4ee6647 | -2.57607 | -47.1597 | 2025-12-04 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80887cf9-1213-3f76-9444-dd481c4afa46 | -3.66368 | -47.2766 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d3bb7f6-4d87-3862-b91f-d220f3e82233 | -6.4953 | -43.79965 | 2025-12-04 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f69bb5b2-7383-35c8-a247-3df6e6fabf88 | -5.00667 | -42.94146 | 2025-12-04 04:21:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dab93328-bd3a-3875-99df-9a73851d368f | -4.78382 | -46.13197 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8055446f-51e0-3dd2-9fc0-abb69b4d7408 | -4.52612 | -44.10552 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbb705c0-6f40-37c5-83bc-eb6756c15159 | -3.71658 | -44.62724 | 2025-12-04 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8485d417-c8ba-3b32-ab62-211474d2e144 | -6.47772 | -43.53643 | 2025-12-04 04:21:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1edeaa7-185f-3e89-a914-a5606b8ab121 | -4.0044 | -46.5493 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07dbaf6a-c18a-3a68-80aa-54548b567205 | -5.4264 | -46.091 | 2025-12-04 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0f6c279-7892-3947-92bd-ec1c1baa57c1 | -6.05836 | -43.74533 | 2025-12-04 04:21:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9b846c82-a882-3472-a875-a56c291f2500 | -4.33553 | -43.99765 | 2025-12-04 04:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 839c4d9f-58a9-3467-afb4-482f83fde186 | -2.36358 | -47.68781 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cf6d0ab-558c-3a6f-b630-257c3936bce3 | -5.0262 | -43.97569 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2fc575c-e466-3f13-b968-0ebfc58ddb75 | -3.8556 | -47.04776 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1821be67-4744-3155-b9fc-4fe7e0b2ff80 | -2.57675 | -47.15547 | 2025-12-04 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 701ce0d5-88a0-32b3-a9b4-61d7d1c3cf73 | -4.02887 | -47.34266 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8f0d26b-46f2-36cb-b665-22cd0409f7bd | -3.32372 | -44.37794 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41aebd51-16f3-3ccd-9c35-ba2909d28ba9 | -3.15194 | -45.42014 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cf8c1e2-17f6-3872-955f-c9c34305e825 | -2.53621 | -49.45913 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42411854-a8b2-3d81-afe7-76655366c90d | -3.92794 | -43.12428 | 2025-12-04 04:21:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5ab2ae1-e251-3416-ae30-0a2c7f19c936 | -3.71989 | -44.62775 | 2025-12-04 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1905bb6-52c9-3bd0-ae2b-c3d9a2909cce | -4.84077 | -43.1999 | 2025-12-04 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e55b3fe-fbe1-3490-9167-888c1527b2c0 | -3.67213 | -45.96653 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0c82ea2-24b7-3764-9cc6-0a530abddc94 | -5.73416 | -42.75429 | 2025-12-04 04:21:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e27eee5-2bd6-39d3-8ad8-52c60fbfda0a | -3.41127 | -44.98883 | 2025-12-04 04:21:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 96d99be4-38e5-383c-943e-6ca22a14f417 | -2.38647 | -49.38843 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e026d360-c814-3237-b434-6963465299e5 | -3.68494 | -41.68948 | 2025-12-04 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d541291a-ada3-393f-a518-395ace78e6f7 | -4.67648 | -46.3848 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8828e797-c013-3b98-8725-4df74222839c | -4.06409 | -46.56694 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| ad96fafa-7063-30eb-a640-a938aa5c7972 | -3.29876 | -50.18756 | 2025-12-04 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bd941da-9f3d-3eae-965d-80b737fbb6db | -3.07487 | -46.64841 | 2025-12-04 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fed25278-a223-31e5-a84b-14ae945b940a | -3.78032 | -44.32986 | 2025-12-04 04:21:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ec9c1e1-55b0-36a9-bc64-bdbe4c7c6a26 | -2.95466 | -48.58549 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd18d1bc-5b14-3670-9981-475b993056f8 | -5.01858 | -41.00733 | 2025-12-04 04:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8a5608af-3ec3-3468-83da-766962656c54 | -6.48169 | -43.55526 | 2025-12-04 04:21:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f62a930-335b-3e3d-a243-aa02a1b7d2b7 | -5.40086 | -47.2533 | 2025-12-04 04:21:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57ff19a8-0d4b-328d-9d71-6e3fb258097a | -2.43317 | -50.29219 | 2025-12-04 04:21:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e787144-5123-3ca7-868b-68de825f1a8f | -5.22538 | -43.37177 | 2025-12-04 04:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c94fb8d5-00b9-37c6-a66b-0913f485092a | -2.08044 | -48.36954 | 2025-12-04 04:21:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aabdf22c-7c3a-3ad7-8fc8-ea418d43b0b5 | -3.82189 | -46.55381 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README10.md)
