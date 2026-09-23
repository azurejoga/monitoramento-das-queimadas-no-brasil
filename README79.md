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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 126760f7-2579-305c-9fb7-3972e6f08db9 | -4.50571 | -54.9855 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af59adbe-e285-3be4-adb1-18888697aabc | -7.43405 | -49.84314 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 97a17901-9581-36f5-bd49-697e16cf5465 | -6.66939 | -55.05612 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2d9a763-9ac5-36b7-8784-0f480ae6e545 | -5.27601 | -60.20823 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 430ec70e-035c-3878-bc07-41006508a5b4 | -11.67422 | -50.97685 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f1c2beb-324f-30ae-8a47-10df1678630e | -9.17337 | -51.47027 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebc3140d-cc14-3ef7-a36c-a4ca492f7421 | -5.76794 | -52.35799 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97e4b30d-15f0-3590-86c8-11f4876986a7 | -7.32854 | -55.59681 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8a1c7ae-e469-3d57-a5a9-76436f782b03 | -8.45333 | -48.70337 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70546570-093b-368d-9d3f-f2ac20269ee8 | -6.93698 | -42.88196 | 2026-09-23 05:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b1b6019-954f-3910-b396-af69e2b3d175 | -4.41594 | -55.47203 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 558bd7b0-e5c4-3526-8bfd-a77b75be732b | -6.43914 | -48.45913 | 2026-09-23 05:04:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e211305-3203-37a1-b1aa-2fbc38185f16 | -7.40238 | -44.73646 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bcc38ab-068a-3858-bb20-f96c22ac31e4 | -6.67607 | -58.55556 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e9c2815-a4f4-36f2-917a-875ce484e62c | -5.87723 | -52.07287 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aac4b76b-a675-3e38-9abe-2ac4f8446888 | -3.14816 | -60.62867 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da6b2ccd-a2dd-3c47-aa15-485e0e7094c0 | -5.82161 | -57.74156 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d310b4a3-945d-3a02-9383-889f5833de1b | -6.10806 | -57.67387 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1903776e-e26d-396b-ac2b-90b434fbaaba | -10.95784 | -50.6079 | 2026-09-23 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 215465f0-6f94-3d46-83ee-d5b88084a5e6 | -8.73277 | -54.97502 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87644c3b-c8dd-3068-a565-1e7d44b2e99b | -4.56986 | -49.55486 | 2026-09-23 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86ed1a19-d2dc-311b-83c3-6d2d0af5d08f | -4.1539 | -50.45882 | 2026-09-23 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ed0153fc-16d4-3da6-9cc2-11bcf4d40bc6 | -5.60205 | -60.20776 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3830ec76-0fd1-3647-89c8-d4fe34cb9b83 | -6.70254 | -58.92417 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 280b2f94-d5f3-30af-83b0-ca822280393d | -6.52256 | -55.38586 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 357fbf4e-497a-371c-8a0d-e477a645b310 | -3.90481 | -55.83598 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 743f531b-a43f-3b12-9e3f-a07bc6dc11fc | -8.92639 | -61.48023 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8840a6d4-23d8-388c-8547-de5db002b141 | -7.41724 | -49.85702 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b85fc96b-8056-3aa3-af40-030300760f40 | -10.91161 | -53.94469 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d257d02-8bb4-396b-9c56-61c249a8eded | -6.6261 | -59.99688 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4fd7d027-efa6-3773-ae23-ebe664425f88 | -8.25185 | -50.86307 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f232951-199c-3182-9986-962b0fdfee21 | -6.55133 | -56.03173 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf590294-3190-33ab-a074-9d27650e201d | -5.8506 | -52.02951 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 135bd5de-6acd-3e95-bd49-3c4e2b0126d1 | -8.94197 | -50.91413 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4692c4d-3be5-3c10-83ca-affc4a9e3c42 | -7.43767 | -49.84348 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e023e388-0866-36c3-a902-4b51492f0d60 | -7.03882 | -62.93543 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b6d358d-90fd-3632-8fb7-06237ec40d97 | -5.31711 | -49.0544 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bfd93b8-9392-3561-8534-be67477824b2 | -7.41428 | -49.85214 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38e5043b-7c2f-31aa-8767-979fab169693 | -12.12526 | -47.38171 | 2026-09-23 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42ebb4b8-ee21-3725-a8f3-6336ec0fe159 | -7.56129 | -57.67873 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f8dc467-e97e-3763-8dce-7c02cc505546 | -10.85729 | -54.11307 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edc5453e-5bb8-3df4-a26b-df776d977806 | -4.05067 | -56.31579 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e49270a-1f63-3470-b2c2-101f5e3af499 | -6.94206 | -42.88667 | 2026-09-23 05:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f510f73b-f627-37ee-9212-49b351a3cb18 | -6.67577 | -55.06109 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6365e40f-d939-373c-9ffe-ef58e830d166 | -5.28065 | -60.20273 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 034d24b4-ba61-3867-b832-af2d84cd23b0 | -3.90541 | -60.59236 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc034b2c-c0ba-3d72-bbd2-993086940063 | -3.49 | -54.68512 | 2026-09-23 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ced20fc7-efc4-3859-b93d-cd95629d4779 | -3.82639 | -59.33749 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b15203e4-5a59-3e8d-8681-809ae567694a | -3.92176 | -60.55769 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a02fd775-9338-31f4-a0d9-8365c8d7b552 | -3.45146 | -57.49174 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fe9a34b-52f2-3279-9dfe-28a4209fe155 | -6.39521 | -54.8825 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1cae4c3-2b1c-3aaf-808f-22cafb56bae8 | -11.78559 | -50.9755 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c539bc3-cc42-3db7-8766-ba77c8034f38 | -10.29339 | -50.54872 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3aaee13-7778-3e90-b9e3-77e1782d0905 | -7.13485 | -43.07167 | 2026-09-23 05:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d3d09266-ba22-300e-8950-b68d29e8496c | -6.62462 | -59.92573 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8267f33-d45a-3ed8-a8f6-8090f5e40b52 | -5.59762 | -45.37228 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1449a09f-b078-32c5-8a5b-02efc9ce22d3 | -11.63158 | -50.95426 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51be11b4-7b0c-312e-8ec8-54faeaeb1a8f | -7.38571 | -51.77252 | 2026-09-23 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddbe5238-8c71-3205-9e2f-5d3544201981 | -8.92702 | -61.48443 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 648db95a-661d-3fcc-99ef-798d8d07c425 | -11.03581 | -54.1459 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 856f60da-01a8-34c9-b88a-8c8556540a49 | -4.09309 | -62.08962 | 2026-09-23 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e4bb711-3fa3-3225-9b0c-0cccfadf9d54 | -6.94896 | -59.82639 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf28f70f-5c2e-35f2-8693-8265ae7b6bb6 | -6.75091 | -63.14576 | 2026-09-23 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d04b4e3e-d71a-3cc8-b116-afe5d64a5024 | -8.33592 | -50.82512 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bf90d27-ea60-3e40-8dfb-48025435b4d5 | -6.39284 | -60.01649 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac736180-68a3-3df7-9fdb-e429e723f2bd | -10.27977 | -50.51708 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06c4df15-bf50-32c8-9803-57d8330dbd3a | -9.56922 | -46.53683 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b9be2aea-1b2d-3bf3-97fb-2b9850753bf3 | -6.61506 | -43.75151 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 850676da-b4c0-37cf-859e-54f9befb4263 | -8.30839 | -54.76956 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f730040c-2b22-317d-b9d4-c788bac56bb5 | -6.30325 | -57.74839 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb520a07-8320-3dbc-8410-6d96fa073f9c | -11.6605 | -43.48291 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22164ec5-24e1-399f-bf1a-253a405a3fc8 | -5.9092 | -51.95645 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5d720d6-bcea-3ad2-81b6-751072366c4c | -3.78679 | -60.75674 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 218b9378-63a4-39ee-8767-6782e9248068 | -8.08342 | -44.34575 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcf4d239-3750-3255-a14a-384ba7525660 | -6.70097 | -59.96005 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| beceea00-6b22-37f8-9f09-aa0b2314b3ee | -10.90547 | -53.96175 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 939b5f45-f4ea-3e9f-9233-448321a1e637 | -11.64636 | -50.97746 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45d0186f-967e-358a-81bb-9b799311d119 | -8.195 | -54.7135 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d071b373-13d1-3f5b-88b3-c6ee1b0eb0ef | -6.60977 | -43.75075 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 66ba02f6-f132-3c1f-a6e1-8e685d273141 | -6.03177 | -44.03368 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1cbb1eb-05a0-305d-a978-6aecce8e4b12 | -8.92313 | -61.49775 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 925d9803-0d46-35e8-aa73-7dd5f02dafa4 | -8.1944 | -54.71718 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f61a36e9-f5dc-3bc1-bac3-4594c802a7bb | -7.83372 | -63.41289 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4bb6ad76-3d94-3bf4-8cd2-e7c81b7b4120 | -4.53904 | -54.93722 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5b67ee7-46c0-3402-9ba0-212e38e51795 | -8.92303 | -61.47775 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a72139a-a73d-3e94-87bc-f9e28189ab6d | -11.29551 | -51.37172 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfbed19c-c93a-3093-8b08-d78f720f9f19 | -11.65576 | -50.9782 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98f2cfde-9761-3dd4-bcd3-99039015d550 | -8.91593 | -61.48844 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dfd5974-69cd-3812-ad60-fb34ec5b186e | -6.64427 | -59.92412 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5350e13c-2995-3b1b-8460-10988f8ad89c | -5.7779 | -47.15676 | 2026-09-23 05:04:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 01e2d9dd-67d5-3616-a7e2-dd0d9ec12d15 | -3.60344 | -60.57603 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d412d3e-7640-3168-8f95-7493b3107af3 | -6.19787 | -57.78136 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 614fe7f5-22db-387d-9f18-9028d1cc8cf8 | -6.4335 | -48.45586 | 2026-09-23 05:04:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb0b7b43-cad2-3919-a4e4-7444c23f5a34 | -5.87057 | -52.0327 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b12696ca-e04b-3c09-b5b0-2da0afbe6e70 | -10.00452 | -45.18827 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8c0a68aa-b7d2-31ea-8d59-92b6c9b9b665 | -5.76645 | -45.10685 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| dba83b7e-e8e0-3b15-8719-1fd48861a7b6 | -5.80724 | -49.15588 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e54e64f-5595-3b98-929e-7e44cc2f6949 | -11.63147 | -50.97937 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0fc8aca-afc5-3968-b08c-f66a19544c98 | -6.34651 | -49.87162 | 2026-09-23 05:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f46bd349-a3a5-328f-8ded-c756483f1376 | -8.25812 | -54.77646 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README80.md)
