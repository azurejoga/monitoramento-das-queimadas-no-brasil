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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6478dd57-4dcf-3205-a614-af8c1c3015e4 | -13.1746 | -54.9337 | 2025-08-18 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 270647a5-b0d2-3676-af54-608e37cc17a6 | -12.9968 | -56.8597 | 2025-08-18 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 690534c2-b57d-3dae-89bf-a3c2b937ec2c | -28.8503 | -54.0861 | 2025-08-18 00:00:00 | GOES-19 | JÓIA | RIO GRANDE DO SUL | Brasil | 4311155 | 43 | 33 | nan | nan | nan | Pampa | 71.1 |
| 545b047e-9f17-33aa-9f21-8267526bfcf9 | -13.2378 | -50.7756 | 2025-08-18 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| e525f2ed-2c20-3770-bba2-9ec7cad86f88 | -13.2375 | -50.7972 | 2025-08-18 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 3f11482b-06a9-3368-b956-ad5c2737e631 | -13.0162 | -56.8378 | 2025-08-18 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| fc967904-3368-35e2-a1c0-936d80edb11a | -13.2186 | -50.7781 | 2025-08-18 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 7d606b72-6de0-39ee-9979-1e8491150479 | -11.3114 | -55.2128 | 2025-08-18 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d8c25695-a1d6-3df9-acb3-d03f6f996f48 | -13.1749 | -54.9132 | 2025-08-18 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| bbb5b7d0-c54f-3933-a634-026102e9c5c8 | -3.982 | -42.516 | 2025-08-18 00:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 131.8 |
| b6f0d331-05ee-3f54-9703-f5ac88be7d73 | -6.5678 | -44.4738 | 2025-08-18 00:00:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b2b53409-17c2-3c1d-8188-39e398304b1a | -3.9819 | -42.5396 | 2025-08-18 00:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| c52de979-efaf-3d23-beea-7d6d84bf00ba | -6.4335 | -44.7822 | 2025-08-18 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 6d0202a7-69d2-309d-a579-81445aaf2ce1 | -12.9971 | -56.8395 | 2025-08-18 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 015b9d3d-89f4-39d4-8918-488684812003 | -19.1467 | -47.0279 | 2025-08-18 00:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| a14199b1-f2e5-334e-ade5-98623a508fd1 | -18.61606 | -42.44798 | 2025-08-18 00:07:00 | TERRA_M-M | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 81d3570b-a1c7-32e0-810c-0d824a9ba2f8 | -22.14679 | -44.83036 | 2025-08-18 00:07:00 | TERRA_M-M | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 448adc8b-4ec4-3fb6-b4c7-4339c52911f3 | -18.05026 | -43.82269 | 2025-08-18 00:07:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2d79e8fe-4bd0-3571-9b6d-a53b270a7c0f | -15.96373 | -43.89948 | 2025-08-18 00:07:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c039febf-48f6-3b80-a65d-08faaa3eebc8 | -17.84811 | -42.52171 | 2025-08-18 00:07:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| a0f56c09-29c2-343f-80b0-af10b6dcee91 | -20.21752 | -47.02872 | 2025-08-18 00:07:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 2cbfb251-ec2b-3e94-aabe-072a498f1bc0 | -18.61469 | -42.43703 | 2025-08-18 00:07:00 | TERRA_M-M | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| fcd2dc1a-4fb8-3d8b-a3e4-78ddf1b8fe9c | -20.21056 | -47.03554 | 2025-08-18 00:07:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| c339376c-c5d2-360f-921b-c9916d325387 | -17.16003 | -46.21328 | 2025-08-18 00:07:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 680405ea-406f-31b9-aac9-58c3c9a9e898 | -19.14298 | -47.02594 | 2025-08-18 00:07:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f96ad92d-2e3e-31b2-9e8a-5ff7617e88f8 | -18.95385 | -39.91299 | 2025-08-18 00:07:00 | TERRA_M-M | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| b22df3f2-1146-3add-aa37-9f58b953d397 | -17.1621 | -46.2319 | 2025-08-18 00:07:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 49.4 |
| ac7c778b-ac66-3b39-b7d7-cedd1b779d76 | -19.14538 | -47.04979 | 2025-08-18 00:07:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 768ca7a3-c287-39d1-a693-c846e79b41b1 | -13.239 | -50.79143 | 2025-08-18 00:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 58f637b2-b993-3764-befe-3b6c565be7c3 | -13.22244 | -50.79317 | 2025-08-18 00:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.8 |
| e40712c4-84e5-311e-b761-62c36bd2f6a3 | -6.42682 | -44.78101 | 2025-08-18 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 5c3a690c-ef3a-3357-9a67-c673acc85291 | -6.15372 | -42.70657 | 2025-08-18 00:09:00 | TERRA_M-M | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| fabba7ff-fa65-3c67-8140-bb8972f8ad13 | -8.50242 | -44.73574 | 2025-08-18 00:09:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5f1e73e9-9863-3016-b43f-4bf71ab758d1 | -5.55325 | -43.90026 | 2025-08-18 00:09:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 01375d21-96d4-388c-a517-954b549953fe | -4.9114 | -43.24654 | 2025-08-18 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 5630f312-2129-36e2-83cd-116e510cbcbf | -14.16866 | -41.59361 | 2025-08-18 00:09:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 634a4d20-edef-32a2-a066-469c436e11c8 | -7.55546 | -45.4388 | 2025-08-18 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 21cd1f08-7a83-3200-b5f1-5a3acfea5fdf | -5.79021 | -43.88325 | 2025-08-18 00:09:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 93167d7d-5ccf-3e78-b1b2-5a8e083a9d1d | -5.98814 | -44.11879 | 2025-08-18 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f2dca602-ca43-31ee-b437-554749000cbe | -6.67702 | -41.76745 | 2025-08-18 00:09:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3bb70e5d-3385-33b2-8ce8-0142d7984f9f | -13.56281 | -47.79084 | 2025-08-18 00:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d8c9a81b-ef32-3606-9f9d-a905990be6cf | -13.22821 | -50.78697 | 2025-08-18 00:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 6bf7aeab-2d73-3840-866b-c033205314bf | -11.33196 | -48.39579 | 2025-08-18 00:09:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1f96ab79-1b41-3bad-9d5f-710f17d440ee | -11.80497 | -44.93363 | 2025-08-18 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 12f206a6-f684-3c2d-935f-1ee5e03b7407 | -3.79917 | -38.9455 | 2025-08-18 00:09:00 | TERRA_M-M | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| e6e46357-9360-3201-848d-751ca6b9d8ea | -12.63623 | -46.90378 | 2025-08-18 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| bd680ba3-cb5c-3b35-af0f-2089089e8fa8 | -13.25555 | -50.78967 | 2025-08-18 00:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 84c5ab0a-c023-33d3-8bd1-66a637601890 | -5.9931 | -44.29266 | 2025-08-18 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5226f027-66f0-3a81-86b1-9a7c64329496 | -6.88324 | -41.13626 | 2025-08-18 00:09:00 | TERRA_M-M | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e1763221-6ed6-3c98-89c8-238215f6d94a | -4.91903 | -43.23644 | 2025-08-18 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1c375899-d54f-3e2f-84d0-ae98afa234e5 | -10.49322 | -47.0687 | 2025-08-18 00:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 36f5290d-4067-3bbd-abac-d21c35da5d85 | -6.1149 | -46.67337 | 2025-08-18 00:09:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7ac1d52c-fb35-3222-97d9-ec3a98baec16 | -14.16741 | -41.58437 | 2025-08-18 00:09:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 22ed6dde-3424-384c-b66f-180e2e30a498 | -6.7542 | -41.5303 | 2025-08-18 00:09:00 | TERRA_M-M | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9ee027b1-2d20-35ea-bb79-fb5724f5dc8f | -4.78226 | -45.33238 | 2025-08-18 00:09:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 625a0f51-1aae-3c48-943f-0be0ce203db4 | -6.5509 | -44.47593 | 2025-08-18 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 77cd508f-c038-39ac-83c8-a1336dc3c27c | -6.63845 | -43.89059 | 2025-08-18 00:09:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 479f8f33-6a50-38eb-8382-a2c6ebeff6cc | -8.10522 | -42.35855 | 2025-08-18 00:09:00 | TERRA_M-M | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8bea6b34-20b5-31b4-8178-2a5a561534ae | -10.95814 | -45.17692 | 2025-08-18 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 10bc1e04-f072-3894-9e86-5a1ee147feb7 | -6.56022 | -44.47471 | 2025-08-18 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 98333bb3-9d7f-32a7-989d-41f93ad4ac5f | -11.3276 | -48.39098 | 2025-08-18 00:09:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| b5fba438-be54-33c2-aeda-f655ccec05bf | -11.00631 | -45.65253 | 2025-08-18 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 3de65f60-5cda-3bb0-b760-1901d5aecc4c | -10.94942 | -45.17126 | 2025-08-18 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 12a04886-0bbb-35bf-8414-6de314ef0a1a | -5.14503 | -48.10763 | 2025-08-18 00:09:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 9cc8c576-6104-3bb7-b990-5988aa9ae190 | -5.66808 | -43.39106 | 2025-08-18 00:09:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fd795474-c3d2-35fb-9860-d01482f18085 | -11.80654 | -44.94592 | 2025-08-18 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0ca6b9a1-ecd8-37b3-9a3c-6efc45453305 | -13.24475 | -50.78515 | 2025-08-18 00:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c0637179-96a2-3c3c-9404-f9d6ed6ac819 | -7.6035 | -40.49669 | 2025-08-18 00:09:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 19.5 |
| ddd4f44b-4b00-3646-a4ee-91d89703b08c | -11.00221 | -45.65874 | 2025-08-18 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 782f9f2a-fc2a-3050-b00c-86857d6e67e4 | -6.02852 | -44.34661 | 2025-08-18 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 15c5b319-e6e8-3150-a84c-d69792c6cf13 | -12.62882 | -46.89911 | 2025-08-18 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 625634bc-3180-3f5c-8b19-8f9cd641b2e6 | -6.56954 | -44.47356 | 2025-08-18 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0af4ea06-8e74-3aaa-8dac-06d647d82c3b | -10.95661 | -45.16462 | 2025-08-18 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ce7817c1-0d53-3fc6-b698-876f93b874b1 | -13.56589 | -47.79719 | 2025-08-18 00:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 6263655b-953a-3eee-ae7e-7aee484b1f99 | -5.98943 | -44.12826 | 2025-08-18 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6f3afea6-5571-30ee-9b84-02dcb644fe1c | -5.65919 | -43.39232 | 2025-08-18 00:09:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7aff01a0-a61b-38ca-9f4f-a27415b88171 | -8.09638 | -42.3598 | 2025-08-18 00:09:00 | TERRA_M-M | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| db9fb7ea-9a90-3652-8210-88585d7c5487 | -6.43764 | -44.78996 | 2025-08-18 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 50d28d43-f065-3188-a2af-fabaf9aab48f | -6.43626 | -44.77968 | 2025-08-18 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| dc38701f-6f9c-3017-9fae-78ce427da2dd | -14.19286 | -42.81148 | 2025-08-18 00:09:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 548111d6-c027-30db-ac65-4913bb163984 | -13.73498 | -42.68204 | 2025-08-18 00:09:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| bacfc416-fe62-3775-ab35-5246f5ae33f2 | -8.04561 | -47.68823 | 2025-08-18 00:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| eb0badcc-ad8d-3c36-80dc-304dcf70cadd | -6.56822 | -44.46367 | 2025-08-18 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| ebb269ca-bb95-33e1-af7e-2bfcec1d0958 | -8.03147 | -47.6728 | 2025-08-18 00:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 40403156-5c92-31d9-a98a-f7bc450c53bc | -6.42818 | -44.79119 | 2025-08-18 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c65898a9-eb0f-3ac9-8dfe-07c7985110a8 | -11.00049 | -45.6454 | 2025-08-18 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 29a8300e-732a-3dcd-9248-b31034a60efe | -6.09797 | -44.59963 | 2025-08-18 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f1356e4-a2b6-3d48-b4ac-d3f9b4747179 | -5.366 | -41.22623 | 2025-08-18 00:09:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 81649c05-1d57-35c1-8853-ee312e50c866 | -4.91018 | -43.23767 | 2025-08-18 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7bd77f91-bbf4-359a-9e94-07d56c62732f | -4.7713 | -45.32331 | 2025-08-18 00:09:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d8fb6ac9-0dbb-3d86-9830-b1fadfb93587 | -4.92147 | -43.25415 | 2025-08-18 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a0b8140b-235b-3315-bcb3-ad0742edb164 | -5.66685 | -43.3821 | 2025-08-18 00:09:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| f76ab465-92c0-33f3-8401-d52627986b32 | -6.43488 | -44.7694 | 2025-08-18 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 24e04a3d-4249-3dd2-a06e-7d01dd568724 | -6.98053 | -41.62637 | 2025-08-18 00:09:00 | TERRA_M-M | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2d945baf-6bf9-3c4e-9436-6e3f12f3c014 | -6.67284 | -43.67117 | 2025-08-18 00:09:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 758162e0-5c3c-3ee1-8191-e7c1ec19fb8e | -8.0434 | -47.6712 | 2025-08-18 00:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 00befb1f-7d66-363c-a8f3-5cdb6d69d20a | -6.08303 | -44.60749 | 2025-08-18 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f25f3f81-4f0b-3d75-86db-51ebfb7b696c | -4.92025 | -43.2453 | 2025-08-18 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 9733d179-178f-3bd1-a068-3ef479af33be | -6.66815 | -41.76871 | 2025-08-18 00:09:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| df13d3b1-98c7-3cd8-a421-00f6d1cf74b7 | -4.78085 | -45.32203 | 2025-08-18 00:09:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |


[Clique aqui para ver as próximas entradas](README2.md)
