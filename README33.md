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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d6d8896-40fa-3d8f-8157-d06cd4608abb | -5.55295 | -43.4291 | 2026-09-12 05:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8731f7f0-82ea-3a0c-b17a-d0417ccc9c3e | -6.07154 | -53.49165 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7facb39c-3b9c-377b-8a24-b832afb63233 | -10.72865 | -53.99598 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f97dfe2-e1e5-307f-b5a7-e55b81f42e13 | -6.22954 | -51.68434 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f0d1e36f-7d97-3680-b8c3-db5f377b07fa | -11.37924 | -46.83636 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee4d0ec4-4991-34ce-a791-a7c31412635a | -9.70527 | -54.33969 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d152c3b5-b86d-3bbc-8e59-14084154c17c | -10.47766 | -51.363 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cee025d-0d28-33af-beb2-919c847ef00c | -8.11835 | -54.79365 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df719fc0-c119-3ba2-a305-cab8719727d4 | -8.5333 | -54.72085 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ba2ba61-a1cd-3545-a3fd-6939758df69b | -10.53597 | -51.35794 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54090b0f-ac19-3ef9-aece-ad4900e1b13a | -5.76999 | -45.09885 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| d229b5e7-fa02-3515-86f4-0734d489d6ac | -3.74008 | -61.74983 | 2026-09-12 05:10:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72bc1849-50ab-3a89-8767-5f4ba81fa6df | -2.72908 | -57.64828 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73aeba31-ea3c-326a-b775-e3c6ccb6eba1 | -5.47793 | -45.12912 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1afb6ac-70b8-31f0-a0ba-c08c032814a5 | -4.28357 | -46.53119 | 2026-09-12 05:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebda4895-8084-3df4-a249-735b1db70d7b | -9.37028 | -48.41676 | 2026-09-12 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 544d0c73-a3fa-390c-b385-cc92feea1c53 | -5.12574 | -55.97752 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16e81d4a-35ca-3360-bd4e-1546a8331a8d | -10.28909 | -45.2901 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15f9201c-3528-34ee-baee-6f8fd014eda6 | -8.57323 | -54.5697 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6808a168-4b5f-3787-80b4-66eb7198a34c | -9.69823 | -43.39781 | 2026-09-12 05:10:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9ca9159-e55b-30e1-b0cf-c827489287ed | -10.33725 | -48.01421 | 2026-09-12 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea864c6d-032f-3c4e-a62c-b53f539ef6cd | -10.62981 | -46.12601 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c47cd9f-033b-31fa-b093-19aeb8453516 | -10.33658 | -48.01914 | 2026-09-12 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efe87c09-107f-3afd-a64a-532b2f54a26f | -10.55377 | -51.36735 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18a8fa17-048b-3c25-9725-42c2f9c58aa4 | -6.24011 | -51.68593 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee0d458f-02ad-309e-9a6a-44ca8a799ed7 | -9.90921 | -46.23637 | 2026-09-12 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fbbee7e-e87c-394a-85ea-0ddb26d3d9d4 | -6.84358 | -55.8113 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8793653c-4af9-3cba-95b3-4ad33c8665d3 | -5.79894 | -57.72375 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de8467b7-329d-370a-b467-2ef926139140 | -10.54517 | -51.37351 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daefa609-d199-349d-91cb-a621a2f9b6d1 | -8.58763 | -54.56485 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd9d219c-28ef-3db2-a04c-f85b341aaf73 | -11.3745 | -46.83276 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d57f973b-ee91-30e5-aa54-a800c80a0367 | -9.32169 | -45.6381 | 2026-09-12 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75e46e7d-6e17-325b-9c49-dfc203d5775a | -6.82278 | -58.64566 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bc9af16-eaa9-3cfd-b6bc-b5419a8564df | -6.39333 | -55.19631 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fa387e1-f22d-3e7a-aa95-25ba1fc4bd74 | -8.22203 | -55.25155 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4984eee4-e35a-34cc-be3a-8f2600072571 | -6.6178 | -51.14046 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33480b1b-87db-3262-8e3e-391580a778e1 | -5.80195 | -57.72864 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc29baad-91a3-381b-bd84-fc004ddf8d5d | -6.85278 | -55.75658 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52617755-71db-3d41-a952-cf68b8a14fb2 | -9.72842 | -53.96166 | 2026-09-12 05:10:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90d1f70e-c46b-383f-ab7c-c5f4ea1b2fbb | -6.23306 | -51.68488 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7a822b5e-b2b2-3831-81cf-4293cd64eb66 | -6.18875 | -57.72035 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 032518e3-f40f-335c-b66e-583089cdd716 | -11.1003 | -50.82496 | 2026-09-12 05:10:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53de5f31-293f-3a06-8133-7a589e84acbd | -5.77144 | -45.09938 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 8e05f602-97c4-334e-9fd5-214cf31fda43 | -6.11998 | -55.64321 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c50d62a5-3f75-39a6-bee6-ef95c40d4197 | -6.11202 | -55.64937 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58006300-ea98-3b3b-bbf0-847e441d496a | -9.70798 | -43.39472 | 2026-09-12 05:10:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 93197af6-8a39-347b-962d-000fef4c601c | -11.53438 | -44.89486 | 2026-09-12 05:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a305bcb-1b9c-3103-b66d-d9321862a547 | -10.69578 | -54.16447 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 24993155-ec9c-34f7-abdb-7271f1fd17f2 | -6.88725 | -55.65123 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba909b5f-2e9d-31ef-9c6a-1684552fcbee | -6.12218 | -55.65102 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff91b2a7-87cf-3ee2-a7ad-0ca6f3babcbe | -6.79805 | -58.79091 | 2026-09-12 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8b7fcc0-83d6-37da-b2de-f0913784039f | -10.46511 | -48.64306 | 2026-09-12 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 357c6ea7-a369-348d-ad25-c77feb3edb00 | -4.302 | -49.11221 | 2026-09-12 05:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cdf264de-09d3-3e50-af86-98c21ae5c9d8 | -5.77132 | -45.08926 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9ab64124-f82f-373b-9a58-2b4506c5af0f | -5.79823 | -53.80875 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfc72904-f2f3-3f92-b3de-134a918bce9c | -6.20614 | -55.26039 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70cff6df-7cba-34f2-9010-3c5ec3d0eb91 | -6.11879 | -55.65047 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13a0921a-be69-3f11-b16f-da506fd4bbd9 | -10.23599 | -56.26257 | 2026-09-12 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e70e25c-6d15-343b-9001-adf30ef547d1 | -4.53457 | -54.96592 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b569ab3-311a-317b-b3a2-5d0360989d8d | -3.37107 | -57.71245 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dbf61b99-6f48-3eea-a806-89795a90342c | -6.89004 | -55.65538 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99414481-33dc-3003-a952-866edf58a40a | -6.24122 | -51.70213 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1eedf61-a7be-3ec3-8160-d4b1ba78bcf7 | -8.53562 | -54.72103 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b20b7cdf-5b2b-3e55-9e5f-d3ccd2b3ee3d | -10.54223 | -45.21322 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c14f675-4609-3009-b8d3-5ab44363ba40 | -5.74179 | -53.47895 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54aa1bc4-43ae-32fa-bfbf-38ea5f10c58b | -8.95766 | -48.90496 | 2026-09-12 05:10:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbe5c6e1-b3d5-3a23-84e1-d7520dfd0750 | -7.09561 | -55.41745 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fe65509-2e02-343c-a6cc-2fd0ec92c224 | -10.2332 | -56.25843 | 2026-09-12 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ca25ae-9383-3976-8924-fae4dd7beeee | -6.10999 | -57.63374 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2ac0745-19cc-338c-a45c-c302e1623414 | -6.50297 | -47.59385 | 2026-09-12 05:10:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43eae9c9-e479-315f-a3d8-1cdd6a65aa8e | -10.56322 | -51.35492 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8db42502-4347-3d9b-86ae-4302a2018464 | -7.41924 | -46.1506 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4e4cceb-d4e4-358d-a56d-40b86df3d0aa | -6.07822 | -53.49266 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c9460bf-bd2b-38e1-b98b-4b99fca50357 | -10.29515 | -45.2873 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6bedac0-608b-335a-ac35-2fe69acf8ac4 | -9.16067 | -49.98482 | 2026-09-12 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dda1070a-c21b-3bfd-b05d-7c1b0c02aaf0 | -5.78994 | -53.81811 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e60ddafd-27dc-33f2-bcf5-33360f1b69c9 | -5.80876 | -53.80684 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fd98186-9029-38bb-9067-af0ceab14b3c | -6.39781 | -55.18981 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83941c20-74a8-30a5-ae0d-0d3eb412804b | -8.58265 | -54.57479 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c54f501e-b9d5-3285-8481-c43fbec490c2 | -6.32162 | -56.05915 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f6a1054-cecc-3dab-9863-1c722516592d | -8.32218 | -54.76581 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17ee7af6-4bf1-3ae5-a8e5-6b05c0061631 | -6.11321 | -55.64205 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29322c36-fabf-327b-8237-5c02c78b8833 | -2.73061 | -57.63877 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23189378-48c3-3327-897e-1cda7041885d | -6.07378 | -53.49915 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cd0ebb1-05d4-321a-b573-31bf0bfe6225 | -6.10285 | -55.63713 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 515992f8-0b78-338c-8ee1-0183855c4149 | -11.36392 | -46.79391 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecf30bbb-d33b-38e9-8468-4c2de8abacfa | -5.81036 | -47.22078 | 2026-09-12 05:10:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14b2731c-c400-3f80-a506-455021af3a54 | -6.09888 | -55.6402 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de21958c-fe8b-32d9-a3ca-5e1e13dd65b6 | -4.46623 | -55.43466 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1f4bdf0-dc8c-32c4-bca6-7ffda82743bf | -6.12057 | -55.63956 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9d267c2-0f17-3d69-ae9f-12f9b6dfe264 | -8.07726 | -54.86588 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d772b122-7b47-3285-b556-bc2e0a718b91 | -10.55784 | -51.36578 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fa37fcd-c5d2-3bac-abf9-77beec9fef8e | -6.85065 | -55.25134 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a7f7f7d-d7cd-39da-a14e-b8c097ec34ab | -6.2395 | -51.68984 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae7a688c-24b5-3bab-be5d-2b0050db9f0e | -6.61866 | -58.85765 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1033ae30-1668-303f-a85b-1d0f4fc0d3ce | -5.97641 | -57.76548 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc1b7be4-d861-32d1-907e-d127f8e54c80 | -6.88341 | -55.63219 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca900e53-3aac-3c84-adde-dacaa45285d7 | -7.41839 | -46.15654 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 873b0184-d22f-3376-bef7-0265f6fe8aae | -8.31776 | -54.77222 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4645f3f9-b12a-3282-b6a8-a1f2ef7037e0 | -5.77237 | -45.09299 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |


[Clique aqui para ver as próximas entradas](README34.md)
