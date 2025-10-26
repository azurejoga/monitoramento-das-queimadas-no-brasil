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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d644898e-6015-347b-8779-e7637fd29d7a | -13.89136 | -48.4163 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f572917c-dec9-3d66-b96c-a0f15bc8aa75 | -13.92185 | -48.38007 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fcf6c89-2f89-3052-9117-65b2ed4baa93 | -11.51417 | -48.24001 | 2025-10-26 04:51:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3981a8f1-cd8c-3eda-bdf0-44d19578b231 | -12.90858 | -48.51179 | 2025-10-26 04:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 947bff61-c2b6-3290-af8b-928dffa88149 | -11.29122 | -47.79693 | 2025-10-26 04:51:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e378dfe2-da23-329b-aa3b-77aaf647f4f1 | -13.91616 | -48.42336 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa34f8f0-c24e-3be6-a178-8fbd363eae38 | -9.89942 | -52.1949 | 2025-10-26 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4905aad-d943-31c4-ad31-f475f9ca4a08 | -10.91495 | -48.02915 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03071fe2-ee9a-3e7f-b019-9c551221a74e | -11.45389 | -49.74885 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 736a655a-1ad8-3103-bb3b-874ff6804669 | -10.82285 | -47.0696 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98b9dd33-6ba5-35d5-ae3c-405483c110f7 | -9.2905 | -57.55115 | 2025-10-26 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58ba9eb2-94df-36cb-9848-cce6692925ea | -11.51531 | -48.76785 | 2025-10-26 04:51:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| badfa7a8-4760-398c-b5a9-6d5b41b8a99f | -6.54203 | -54.96736 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 240aeec0-77ba-3702-8b62-8409bae834de | -9.15764 | -51.30536 | 2025-10-26 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d97527c7-cbd2-3f37-ad01-b37d6cc63ee5 | -12.31667 | -47.4797 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4da8262d-4838-3e85-bcde-d2428ab9e388 | -12.17575 | -47.01819 | 2025-10-26 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6377e868-2688-3d95-a41c-ff55d7c6610c | -13.88452 | -48.4691 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54d16cd5-e4f0-32a1-b2f9-9287534db541 | -10.99421 | -47.88401 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ee61f85-b0cb-3cec-a147-8281c07b9659 | -7.41852 | -48.7752 | 2025-10-26 04:51:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb0bcb6f-cc8d-362d-a4ca-73cdbfa270a5 | -7.8537 | -46.41628 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2464b90-bdc2-367e-a203-13942c46c5be | -10.87421 | -48.03045 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73a191b4-9305-3a71-8714-06a39d767e57 | -12.13915 | -47.01689 | 2025-10-26 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5526152-495a-31c2-92e6-2cc05b2aadb6 | -11.09798 | -45.73919 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5652c16d-c8d3-36d5-a706-68141235b873 | -10.61596 | -46.60722 | 2025-10-26 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1fe13c5-2a7e-315e-badf-a624528e4a8a | -14.16291 | -44.68298 | 2025-10-26 04:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe371544-9cad-3f91-99c1-fbc7cc566053 | -10.83549 | -47.62732 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d056b5df-f0c1-3b50-80fd-2237a6ffee25 | -8.0361 | -45.1521 | 2025-10-26 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 524f8a9d-0931-38f0-bbd4-32f1945f97e3 | -8.66613 | -47.07855 | 2025-10-26 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46b61225-072b-3ae9-b9ed-290015221a81 | -10.17382 | -54.35746 | 2025-10-26 04:51:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 963a9196-be69-3c58-8e6d-767494182979 | -13.64327 | -47.62587 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed38da5d-7c21-3078-bd69-dfce88dec247 | -11.62345 | -54.99586 | 2025-10-26 04:51:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| affada2f-fb6e-32b4-872a-eb1c615db71c | -7.4479 | -44.74294 | 2025-10-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5fff416-e538-35f9-b94f-4918e1c5bb57 | -8.7002 | -50.82652 | 2025-10-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55ead285-aadd-308d-9a49-8c083c3f1815 | -10.84796 | -50.59908 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 176efd6f-8599-3013-a4e1-78e23ed79e84 | -9.20843 | -50.59627 | 2025-10-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f07cf19-7bab-3749-981a-ccadb50ae5ab | -8.11858 | -55.08242 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80095cf9-83a8-384c-9c32-2072b069d257 | -7.50627 | -47.00336 | 2025-10-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef67ea92-e4b4-373e-9f9f-5f367b8c923a | -11.6948 | -55.46189 | 2025-10-26 04:51:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb63bb11-301e-37e3-ad9e-b5e7887b8e68 | -13.40502 | -43.55656 | 2025-10-26 04:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcf0ba08-4218-3446-a23e-9ef58c5ef597 | -7.80181 | -45.39211 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d4e94523-2c3f-3470-a301-95ec05a311a8 | -11.77391 | -48.18608 | 2025-10-26 04:51:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ff586ca-91b2-3953-b05a-59aa783b866b | -8.12595 | -44.80586 | 2025-10-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a1bddca-1114-3f49-aea1-25fda37700d3 | -7.96054 | -44.81358 | 2025-10-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e2ffafc-ac76-3395-96b7-088b2cc0acce | -8.53638 | -47.2046 | 2025-10-26 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e55f805-4c11-3ecf-a0cd-7cba03f9ac6d | -8.31903 | -46.81665 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e6ac1ba8-61ff-306d-92e9-5556d9de9b1c | -10.40824 | -54.48714 | 2025-10-26 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b2b35c5-622c-3445-9f28-ea6e47087621 | -13.87885 | -48.44677 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e40f300-b9d2-3dcb-bf9d-2f210c145b8d | -8.14445 | -47.0422 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee2aaf20-5932-3271-82f6-8923e1198619 | -8.53616 | -47.20716 | 2025-10-26 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c99f7742-46c8-32e6-98c6-018f0d39c539 | -13.87644 | -48.39508 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b99e11e9-0f88-3351-b5a2-ed20faf3124a | -12.89494 | -54.73264 | 2025-10-26 04:51:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f33adcb9-89ac-3f2e-94be-0800b8212ad4 | -9.1582 | -51.30165 | 2025-10-26 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c22ffe37-3c76-3e0a-b5c5-73f4762d430e | -11.43807 | -54.09075 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58b2e233-91d8-3fc9-89d8-3515967138d0 | -13.17849 | -49.65617 | 2025-10-26 04:51:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aab75503-315c-3332-942c-6702a0101a6e | -11.17111 | -47.79248 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61fd23d4-e21c-31df-b1b4-e4d70c02cae7 | -7.79708 | -45.3914 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 315fdb6c-7094-351e-a8a9-c236198f6ed7 | -11.99985 | -48.93674 | 2025-10-26 04:51:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9deaea1-ced3-3124-a257-df3537bc5246 | -8.12103 | -44.8049 | 2025-10-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc41e61e-2e59-3d5c-931d-1f4a5d86e195 | -12.76095 | -48.62523 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c583958f-9404-312e-a4c6-cddcb984911a | -14.16915 | -44.33234 | 2025-10-26 04:51:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81574b60-3822-3a42-94f0-f9506c4d8f3b | -11.56065 | -54.51902 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4056887e-74db-3af5-a8b6-e38e40946c9b | -9.63622 | -57.0134 | 2025-10-26 04:51:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60a387d2-d775-37e0-a097-e49215f2bc53 | -9.44141 | -56.64491 | 2025-10-26 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a36cb32e-31c2-32dc-8ccb-15d3530f7ba8 | -14.22262 | -49.51175 | 2025-10-26 04:51:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93248ef1-5ed8-3cb5-8189-78a826a8ab5f | -7.84927 | -45.37366 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a546c255-5a9f-3185-bb70-e6e0c952c39b | -9.18272 | -57.69365 | 2025-10-26 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e929667-a1bb-3fc8-85e6-61e8a6e859a9 | -11.05444 | -48.3166 | 2025-10-26 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dd2e965-88ec-3737-a479-f46b7bc10d1a | -6.5414 | -54.97122 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 270a797b-5065-349f-87fa-84b009ef7d2a | -8.6962 | -50.82962 | 2025-10-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da340029-4619-3bbd-b307-e0927b61b60a | -8.48902 | -44.72584 | 2025-10-26 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ac567f6-2ddb-3a13-b8f6-4de26f81f9e4 | -10.88706 | -48.02915 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17c95da0-4fac-3c15-b14e-57973e6a5ff3 | -10.23504 | -52.15559 | 2025-10-26 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dd47b9d-573c-3cb8-bf8b-dbaf051802fc | -10.88605 | -48.03631 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f289f91-d15f-32ea-92e1-d1a9b65d5b0f | -11.05848 | -48.31746 | 2025-10-26 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae51d3fb-0d06-3141-9d41-5fceabc87b14 | -12.86516 | -48.65045 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d42b4cad-2af2-36e2-948e-f0afab372e12 | -13.5303 | -49.54166 | 2025-10-26 04:51:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6401a413-f244-3755-9b3e-5869d841413c | -7.41921 | -48.7706 | 2025-10-26 04:51:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2aff76e9-5db5-3628-ac9e-2b44a60559ee | -7.03141 | -49.30861 | 2025-10-26 04:51:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f842d89-bc8a-36f5-be5c-b9fd19498989 | -13.53819 | -43.01002 | 2025-10-26 04:51:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 6fac23f8-8c5a-39c6-87ce-5094c3b84146 | -10.21139 | -52.66434 | 2025-10-26 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e4c55251-9b62-3eb6-a792-32ab2c3e3612 | -7.9399 | -55.0149 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c5a3c3f0-6e18-3891-9e7a-63b5b80a2c2c | -10.41265 | -45.31804 | 2025-10-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 74895b44-6285-3daa-aea7-35654c494e99 | -12.1763 | -47.01406 | 2025-10-26 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05744c34-2d97-3381-a8de-f51c1b4244d2 | -10.83072 | -47.63045 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8113b1b3-4fe1-32da-ae07-bf9c5d57379a | -8.54038 | -47.2078 | 2025-10-26 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c3e74b8-6f70-3360-bca2-6808380ec584 | -12.89769 | -54.73674 | 2025-10-26 04:51:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 166551e3-9f4e-320e-9041-7777a0ac5b4c | -10.35332 | -47.11926 | 2025-10-26 04:51:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9049dd58-afb3-3b08-a576-d0e2424fe8d4 | -11.06803 | -48.33798 | 2025-10-26 04:51:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 465446d1-2bc7-32f3-a561-a9a72e689e1e | -10.21891 | -50.44875 | 2025-10-26 04:51:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d7850b3-9618-3047-ad67-6811c5fbd13e | -10.8778 | -48.03497 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0930a550-0903-3128-8e9d-80b827042b06 | -8.04093 | -45.1528 | 2025-10-26 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcfcd70a-e6f7-3e77-9570-8a79cddcff41 | -10.33392 | -48.12019 | 2025-10-26 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d10689c7-111d-3b8b-b04c-c26f9a9e0d83 | -13.87513 | -48.47564 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 215bc495-9187-32b4-8874-4f2f8506d39a | -11.21564 | -54.84363 | 2025-10-26 04:51:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0cd886d-e216-395f-8573-abad6d6005e7 | -13.89189 | -48.41224 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3049547-f23a-3c1f-acdb-bf519f405b7a | -7.44068 | -48.05652 | 2025-10-26 04:51:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c391e055-e579-39f3-b00d-0b6afacbb175 | -6.31244 | -52.0143 | 2025-10-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7777b879-49b8-3e35-a5be-f5461ce4902d | -8.3019 | -42.31215 | 2025-10-26 04:51:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ecc6e6b9-2b64-3d7b-8cc7-db77edf08c20 | -13.53282 | -49.5523 | 2025-10-26 04:51:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f3e2369-29b7-36a2-a174-e5ef3c5b8587 | -8.13229 | -47.03606 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README44.md)
