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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99f26dcc-b879-38c3-b0df-f528bf71b49a | -13.18322 | -47.29778 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d981eedc-9bd3-3fd3-aaa4-5d1516f495d5 | -8.92752 | -45.50719 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6bd62c7-b98d-3189-b0a1-0313b0b54c66 | -9.73289 | -46.04208 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24b472ac-d90b-3a90-97d3-be1eab0dbe40 | -10.16789 | -46.14187 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b847850-826f-33fa-9c79-1033298585c9 | -12.61473 | -47.94207 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f24a0235-d1c0-36a4-9a0f-615c39ca7128 | -10.07059 | -48.17543 | 2025-09-16 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 51079ddc-095d-3947-b255-4edc183913a6 | -12.80076 | -47.25616 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19034c68-b3bb-3bcc-be79-4d1588a47673 | -9.06991 | -50.30574 | 2025-09-16 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f15788d-01e0-34dc-9714-39c6d8d78861 | -11.3352 | -43.4841 | 2025-09-16 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c562ee52-23fd-301a-b65d-6128414b8f4d | -9.06789 | -47.02716 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7e5c8049-7881-3dd3-99a3-f32ed5b54a0a | -13.1962 | -47.30442 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7ec45fa-0514-3040-92cd-7c81f49a2fa4 | -8.39267 | -47.25908 | 2025-09-16 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 407ed9e0-86a7-3bf5-a221-a5df6d92650c | -7.50277 | -55.00518 | 2025-09-16 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae9c3415-7398-3614-88a6-828616136b02 | -11.12133 | -45.30945 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7c9828f-5bbb-3320-bdc9-c530b4327993 | -11.27891 | -50.79764 | 2025-09-16 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e4bdaf8-0b86-3df9-9655-226532830cd8 | -13.21018 | -47.30324 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6b99b11d-bfbc-374a-b420-2fe5c429004f | -9.16177 | -61.17002 | 2025-09-16 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fffedb8-12f6-3f81-9a1c-8105590963d4 | -11.23836 | -49.9437 | 2025-09-16 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b45c6c8-10e6-3b62-a7c7-7752c292697b | -8.64123 | -62.66858 | 2025-09-16 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72f9901c-cebe-314c-aa27-8ef7a56fc68a | -12.66871 | -48.01622 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c499d59-9daa-39b5-8870-acc23c6db75e | -8.95564 | -45.87804 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60c3fc9c-3717-3910-9e69-546cfe60c0c0 | -8.6679 | -46.38338 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83cb1e38-e2b3-35ae-bcc2-959bdacf0d23 | -10.73328 | -44.75891 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee2c0ee6-4094-341c-ad5a-bcf01977a91c | -8.43975 | -55.63221 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7dd8af7-3f34-33bb-aa09-64195fe709bf | -8.64233 | -62.66828 | 2025-09-16 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bc76461-65a2-3c43-bc06-807dc47c60fd | -14.56181 | -54.51027 | 2025-09-16 04:51:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ac092c7-3668-326f-855f-0d24e970728f | -12.97696 | -47.95753 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3944e59d-9abb-3e9b-89cc-66f8ba4a0b1c | -9.06931 | -50.30981 | 2025-09-16 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2355092-53ba-3187-93de-564727a9188c | -12.62789 | -45.75361 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2412d269-fa7d-31c0-8b67-d73e2eecf76f | -8.97645 | -45.75868 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d23edc92-384d-30fd-8abd-7a6ce588219d | -11.08167 | -49.74409 | 2025-09-16 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23d1702d-236d-30ae-9211-c0377b93e6cd | -9.73369 | -48.1214 | 2025-09-16 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9603ca5e-28bc-35e2-b37d-36998d964551 | -12.68531 | -48.02263 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32e1181e-27bd-33c1-bad2-d55cbb9d74ca | -10.36298 | -61.25586 | 2025-09-16 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6567258-fc13-34df-9934-3c62a5e897bb | -12.7598 | -47.9742 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d7f7767a-86c1-3b66-a881-a3880c5f4e99 | -13.01202 | -47.95856 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21ff42da-40e4-39a9-aedc-978aac815590 | -9.07169 | -47.03164 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f1988db-4b5d-3bb4-a401-ff39e3b0bea6 | -8.59789 | -46.41253 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 076a08a2-4e2a-38ae-816a-6368fc4c509c | -8.92938 | -54.44736 | 2025-09-16 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94e0a3ef-a60d-36eb-b190-3948ae8f079d | -14.81711 | -48.12465 | 2025-09-16 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a01790e0-c465-3600-bb29-1402bb681ca2 | -10.54906 | -51.96575 | 2025-09-16 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f53d8269-c668-3ce7-91a5-0a15458eb142 | -14.85931 | -51.65981 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba13a753-bb2d-35f1-bdcc-26f72474de0b | -14.47759 | -46.35812 | 2025-09-16 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f47a760f-df87-34df-981f-a86d532c1ae6 | -12.96333 | -47.97921 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 013a12cb-7b72-3dac-bebc-b93db931af1d | -15.61944 | -47.37268 | 2025-09-16 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 08511b95-54f7-307b-a12f-b398e6911cdf | -14.80426 | -51.66962 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 6f6bd2c0-35a2-3e82-955a-f242a5bea527 | -11.46188 | -46.92877 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9bc85962-c758-3472-bb97-05e557f05835 | -8.58292 | -46.35447 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5010c870-8d80-3a2d-9b4f-af0eebdeef61 | -12.65918 | -47.71257 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0f0b966-1e1b-3200-906c-4dab13d1c901 | -8.97719 | -46.23821 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22994a10-be58-39f1-bca2-f3edff791523 | -13.02378 | -47.96931 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f05dbe3c-80a2-3c4b-b2e3-31814df383b7 | -11.08033 | -49.75327 | 2025-09-16 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d0e2565-32aa-3333-8003-8a9523b1add2 | -8.08797 | -50.16124 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae4df186-52a6-36eb-a892-44dced93e578 | -12.81736 | -47.2351 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63f584f3-a4af-382f-abaf-b58af8e7d11d | -12.78856 | -44.74601 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce8a3210-8014-3fbf-a784-033d760ddeee | -8.65263 | -46.35073 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea8df45f-1e5e-3082-943d-8c72ad017dcb | -12.05702 | -46.56637 | 2025-09-16 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8e09799-723f-30d5-8d79-f7304a2389a8 | -12.63135 | -47.5185 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ded8c963-cfe2-38c9-8e3d-fd675311d8e4 | -12.11199 | -44.8275 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1500a46e-e1bd-3f67-9cee-3e5e28162b5b | -14.61143 | -46.38411 | 2025-09-16 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d64f37a-3758-3d3b-9442-89c9ebe307f0 | -14.45745 | -47.28361 | 2025-09-16 04:51:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e40d5b5c-bce8-3354-b8ac-1b91e7c4a9ed | -9.54009 | -62.3811 | 2025-09-16 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 596ae558-ec58-31cb-9f8a-2a1e361e7966 | -9.06674 | -47.03536 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| eee0d561-724f-3a51-98eb-e78ce49cb8ae | -8.22591 | -49.49054 | 2025-09-16 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55eff791-c36c-30e7-94ee-228791ac310e | -12.83282 | -47.22287 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad1501ad-7fb2-369b-86fe-9ad3cf28ea43 | -8.08738 | -50.16513 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 430fdad4-bde7-3f2a-80cf-4bbd4e0c8356 | -12.68103 | -48.02202 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8f6cbba-bfa7-3412-a7d3-78db79be7a8e | -11.1376 | -45.34171 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eda26f6c-7b3f-3e84-bfd7-a02c164fd24f | -8.98592 | -45.76005 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f56e7ce8-e609-3e8b-bc9e-ed2c78a20cc3 | -12.85196 | -47.90946 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 904bb52c-7f64-3b6d-a708-d9d504bb79e4 | -12.62787 | -45.75259 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1aeeaca6-3c36-3c16-af22-0b95cb5f81af | -10.71583 | -44.76212 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c6bdb83-6ae4-38ce-9480-c1f1d08814ea | -12.61939 | -45.73975 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b28825d4-430e-311c-aa5e-82899c9f505c | -12.95152 | -47.96916 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0eb7b5a8-7ebe-3ce5-a61e-ce512a131906 | -12.22135 | -53.86945 | 2025-09-16 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bcab6b6-cc33-335f-9d65-e060ced48567 | -14.82142 | -48.12584 | 2025-09-16 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7f0b671-c065-3f71-8b88-090fc33e3dfb | -11.05209 | -48.27544 | 2025-09-16 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf3601de-b755-33a5-8532-5d3f70efdb7d | -11.27688 | -50.79445 | 2025-09-16 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5eb5e2f9-2030-312a-96e2-128ad7ff93fe | -11.11749 | -45.33892 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aa5b475-bb19-38c1-9b9d-7fef52344fda | -10.71328 | -46.48822 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b8bab6e2-7155-3acc-a1cb-018189dfa0e7 | -9.45463 | -48.59961 | 2025-09-16 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d1c3178-224e-3887-aa6e-23eacf69bd44 | -9.09845 | -44.84731 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6256f05-bac7-369f-b313-b7de0b72e14b | -9.05979 | -47.02172 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7a05f20-5069-3b29-91d8-46d69acad72e | -12.60819 | -47.95798 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d1b5969-1e06-3b54-a5e7-985cfa91d6e2 | -9.47752 | -54.44017 | 2025-09-16 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd7f48f2-d293-3475-9435-965d2b9e54c6 | -11.48473 | -43.60094 | 2025-09-16 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f496e2b-0bb1-3b1f-bbef-d6347d74f023 | -11.23558 | -49.40364 | 2025-09-16 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82efbf86-777f-3a2a-9051-af14be3e37d6 | -11.91114 | -46.74799 | 2025-09-16 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bbefe28-1226-3144-adcf-052f1430c406 | -8.41595 | -47.21778 | 2025-09-16 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6b8a084-b338-334f-84bf-4795e71ee297 | -11.30023 | -50.85106 | 2025-09-16 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 030daac9-0a57-3243-af83-993f0bcb9ae8 | -15.09688 | -52.47839 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea155fd3-028c-3d7e-b7cc-aca5074b8bc4 | -10.72777 | -44.76061 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fcef0dc0-c850-3954-82e1-7966a0e9f7db | -11.7209 | -47.46239 | 2025-09-16 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7f4121c-1774-3c07-89cb-f089ef426154 | -12.54117 | -45.87585 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 22b2256f-a56f-341f-a485-fda788d45f67 | -12.97155 | -47.96532 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b62cb3e-22c0-3657-9fb2-f97592d6cf2a | -9.07288 | -50.31034 | 2025-09-16 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2a65380-48e7-3d09-be60-4b9c245652de | -12.756 | -47.96978 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f7df6a51-092c-32b6-910a-e740a0e1261f | -11.43268 | -46.94004 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9db43fa4-ee52-3167-8af9-9b466edca54d | -13.28384 | -54.23796 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cfc83fb8-c001-34f6-bf4c-8a17cf676570 | -11.27535 | -50.79709 | 2025-09-16 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README74.md)
