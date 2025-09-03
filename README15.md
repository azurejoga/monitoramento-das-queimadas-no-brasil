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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6f0f60c-108a-358c-a520-7cddf1971c3c | -4.99019 | -56.25105 | 2025-09-03 00:52:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3d3e6d32-a652-3779-92ff-032a2f00fd57 | -4.02626 | -49.76714 | 2025-09-03 00:52:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 5884809f-82f4-3266-80fc-4e43b92b2534 | -5.86726 | -57.75451 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4a812f6d-c9a5-3c91-90af-9afda61c76e4 | -5.91067 | -57.72879 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 5e61a16b-23f1-3727-bbcb-19001a47320b | -5.70275 | -45.95135 | 2025-09-03 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 84a957a9-b639-3ec0-bbe9-74a56f974d9d | -6.33985 | -53.4416 | 2025-09-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1970da46-0786-314d-b3d3-39a80266d5d0 | -7.96959 | -55.28973 | 2025-09-03 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 6c0d9ad2-f643-3842-ba84-70df9aff355c | -6.77609 | -52.80966 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 0376470e-b309-36e5-8247-40227b5ca9aa | -6.79002 | -52.82837 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec84fe2e-3330-3991-b131-07dac19ad463 | -3.37661 | -47.15938 | 2025-09-03 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 199f63f3-913c-39ce-a587-dd01ed70b499 | -5.86533 | -48.16778 | 2025-09-03 00:52:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a076f7f3-7f49-3b95-82b7-c906c97be346 | -6.43281 | -58.12906 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 76affc4f-61ff-37ac-8f29-68bc71b04a13 | -6.83531 | -52.83091 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| d5d4102c-8c6b-392d-a118-566789284460 | -7.33394 | -59.64371 | 2025-09-03 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 4a7c7e53-5f21-3a1a-a3f1-5ed4bc8e9481 | -6.82405 | -52.81451 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6b975d66-86d6-36d1-84ae-0a06ef98a019 | -6.80006 | -52.83594 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f4f57ebd-ef58-3b37-9057-61bec1bda1ba | -5.90146 | -57.74437 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 300.3 |
| 93842cb0-b1d1-33d6-b47a-ba56a2594f17 | -5.86001 | -57.7845 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bf2c2a55-52f7-30fa-af71-06b8bf1f58af | -5.90329 | -57.75853 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| af2b3320-5c1f-3c35-9199-11188a05fd75 | -6.34951 | -45.65833 | 2025-09-03 00:52:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b3ce50fa-dac3-37d7-85f2-dc993fc7f457 | -7.38264 | -49.41344 | 2025-09-03 00:52:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0461c26f-4b36-322f-82d3-354ebef3b354 | -5.90353 | -46.16156 | 2025-09-03 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1bfb599a-706d-3741-8416-10a4c772ae84 | -3.44519 | -54.63868 | 2025-09-03 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4235f956-bafd-346f-b312-3d6162714efa | -4.14977 | -46.7981 | 2025-09-03 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| f3aa3636-b313-3c86-aafb-9977d9fbebcb | -6.41481 | -43.7751 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 9c50033f-79b0-3fe8-b0ef-20d0101b5862 | -5.26349 | -50.76559 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 47720bef-d714-3a10-883e-a0821a69dd9d | -2.93749 | -49.46098 | 2025-09-03 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| c2bb7a1b-7465-3f7e-88b5-e1223097983b | -3.23001 | -47.14655 | 2025-09-03 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e4e4b986-94bb-3396-acb0-f65a81bfe4dd | -6.77486 | -52.80083 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4f68e6e6-dada-3f0a-a98a-ba879364339a | -6.4443 | -58.12755 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0290376d-cea0-34d8-a502-7e813b8c4c93 | -6.85685 | -52.79184 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 354d6918-630a-302d-b6c3-dd2e9a42c4c6 | -3.21629 | -47.13424 | 2025-09-03 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| db59914a-683d-32aa-bb37-fbd017741ee3 | -6.82772 | -52.84099 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f93a7b40-9735-3c38-b340-129cd882fad3 | -5.61155 | -45.03083 | 2025-09-03 00:52:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 8205d671-d6c7-3ac7-a5a1-52adacd1131f | -4.53133 | -54.97085 | 2025-09-03 00:52:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0376d550-a9cb-3db4-a5c4-cb7e8c7bcef1 | -5.89022 | -46.16444 | 2025-09-03 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 2f439b0c-8934-35a8-9a18-2287a1c824b9 | -6.81523 | -52.81577 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| dd5b54d3-edb1-376a-9370-c61d86c568fb | -7.38091 | -49.40154 | 2025-09-03 00:52:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 37af2a6a-b138-3c8c-99ee-79ec0e80a2a3 | -6.27675 | -44.49762 | 2025-09-03 00:52:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 06d8a9af-50c8-3ddc-970f-11ccc7ae3ff5 | -6.45743 | -49.52922 | 2025-09-03 00:52:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 235.7 |
| de3ea35b-f0b9-3c79-95d4-0acb8f1ce10b | -5.10813 | -56.97472 | 2025-09-03 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1a090c8e-c68e-366d-9d21-74170a78e3ed | -7.25169 | -57.54732 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ab343d0a-2d4c-3da4-b837-8a355517d650 | -5.69905 | -45.96991 | 2025-09-03 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 77513b4d-e971-3a6f-827c-c0b473f73c29 | -6.79515 | -52.80063 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1ea5d3c3-d982-3485-a3a8-6f139f545444 | -4.1599 | -46.77522 | 2025-09-03 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 9a15bfb2-45ef-3dde-9ce4-20516538fb8d | -2.91289 | -52.72829 | 2025-09-03 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 93269b5f-3bf0-3fe9-8c6e-14b88addbb4a | -5.68905 | -45.95351 | 2025-09-03 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 05786f40-9fd0-3625-9d4c-a8965bcf5167 | -5.10646 | -56.96235 | 2025-09-03 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fe32808d-841d-39a3-850e-86bd9bc9295f | -3.22698 | -47.12625 | 2025-09-03 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 339.2 |
| 8dea26f1-c683-3027-8bd1-ef8187021cf4 | -6.79638 | -52.80946 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 97224fed-d02e-3ae7-80d7-194280bacb04 | -5.90883 | -57.71471 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 20c92dcb-d741-382f-84b3-dc106239e4fe | -6.65612 | -53.19242 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 1034e373-759f-33a4-92ae-f76b2f9871b0 | -8.14406 | -54.92841 | 2025-09-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4057e526-1593-35dc-917e-f7162576099a | -6.84413 | -52.82965 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0fa7a53c-3bbc-3572-82bd-47da292c54bc | -2.13662 | -47.99816 | 2025-09-03 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| aa33799e-1c34-3eda-9733-0e79ef4711fc | -6.28141 | -44.5277 | 2025-09-03 00:52:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 05634800-ff42-3f85-b193-c1bd25010f45 | -5.91252 | -57.74303 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 6a240909-adc3-393c-8e09-819b2c6ec29b | -6.52803 | -56.2112 | 2025-09-03 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 92ac9f9c-9c2a-36a0-acba-7e7f77b0134f | -6.80642 | -52.81703 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c3c61ae4-ec04-3db0-920c-6f6c0f65e372 | -5.92357 | -57.74157 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 0471e94c-0579-3be2-9124-52eabadd2248 | -6.78756 | -52.81072 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| af943794-ace6-3d9e-a11e-c7344f6786c3 | -6.43104 | -55.62404 | 2025-09-03 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d21920d3-f60a-37e4-b322-6f4525f88be1 | -3.37486 | -47.15308 | 2025-09-03 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| da0bf358-1563-3a4b-966b-9685e248b8b6 | -3.19815 | -49.11885 | 2025-09-03 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d4a7e031-b799-324f-86d9-1bb525608f27 | -7.97097 | -55.3002 | 2025-09-03 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 41d38b6c-8295-348f-842e-c4f107b515bd | -5.89963 | -57.73026 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 8cfa30cf-e203-3966-bd7b-bbd3691adeee | -6.57558 | -47.38918 | 2025-09-03 00:52:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| bd6206aa-e822-3e08-8025-d046cf6eb3c4 | -6.45568 | -49.51722 | 2025-09-03 00:52:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 1c34c9ae-d09f-3553-9815-6afdfeae2837 | -2.1341 | -48.00413 | 2025-09-03 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| f3baf504-e20b-31a0-87c3-8fac69b1d273 | -6.80396 | -52.79938 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1774abaf-3b2d-3884-a781-2a4309a70a00 | -6.27892 | -44.52125 | 2025-09-03 00:52:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| eeacf15c-c447-3c6b-bc7d-d5f044f874af | -6.85342 | -45.54028 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f3d2f1c4-6f81-3328-8b2b-e1a97a528665 | -6.46762 | -49.5278 | 2025-09-03 00:52:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 44dadf7f-fc10-3088-b82d-d64f8318dcdb | -5.91983 | -57.7131 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 241.3 |
| 1f2d87c2-9bb7-359b-96eb-10ab0b53d4af | -6.80519 | -52.80821 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6ae3dd69-becc-3312-b5ef-252a9d25a4a2 | -5.90155 | -46.17895 | 2025-09-03 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 34e1c06c-0959-3957-88eb-569f16a3e588 | -6.84804 | -52.79309 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8b10b6eb-d5db-3146-ba5b-a8a3e5d2e4c1 | -5.92169 | -57.72725 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 355.1 |
| 278cf578-0e73-3f2f-8b1a-887090bdc78a | -7.33316 | -59.659 | 2025-09-03 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 810d52ca-ebaf-3d02-bbd6-d65a3db04e4c | -5.89805 | -46.15674 | 2025-09-03 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| c9d27551-236e-30a9-97f1-107720b7ba54 | -6.79883 | -52.82711 | 2025-09-03 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 83ea3d36-e587-3c71-9617-38d3e62f159c | -5.85807 | -57.76991 | 2025-09-03 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| e329d573-7686-33a3-b93b-97bc67a70d38 | -4.14626 | -46.79272 | 2025-09-03 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9784c77d-8779-3e4f-ae24-1409b1dac04c | -2.13666 | -48.02236 | 2025-09-03 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| ec0a7945-749d-3e58-be1a-6372b9ad39df | -2.13931 | -48.01628 | 2025-09-03 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 6b79cde3-fabb-3b98-b781-8f2180270a1b | -3.52985 | -52.92484 | 2025-09-03 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| af03dcfc-ffff-35b4-a7d6-b67a9dc8a6cf | -4.15943 | -46.79082 | 2025-09-03 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 191.7 |
| 8df57d0b-aa79-3424-bac8-d3e94efb179b | -7.5476 | -61.3437 | 2025-09-03 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0a4d5467-a0ab-3663-ab43-24154ec4972b | -7.7224 | -48.7572 | 2025-09-03 01:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d8c4f18e-a181-3f20-a6b4-37f812889277 | -11.0181 | -51.5001 | 2025-09-03 01:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5a5e2024-0989-3249-a57f-70534b01ef5f | -5.6079 | -45.0265 | 2025-09-03 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a6e5ab63-ae9a-34e3-b5d8-1f62b20e7c6a | -12.6341 | -56.9926 | 2025-09-03 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 5dd50b67-8749-364c-9ae0-f762e0e39048 | -10.4853 | -50.346 | 2025-09-03 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 5077f011-2f66-31b1-828e-d6c1f6a8abca | -7.5302 | -47.4443 | 2025-09-03 01:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| a504b70b-7311-31eb-8ed1-6adc2ccc160c | -18.1514 | -51.75 | 2025-09-03 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| e98f33ff-7ba8-3210-8cc4-02d378c33a83 | -11.6647 | -57.3533 | 2025-09-03 01:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| b773fa69-cac7-36a7-a58d-3d6f36744861 | -10.0932 | -54.7667 | 2025-09-03 01:00:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 501420dd-a0d2-37ac-bb28-fb0f51b1897d | -15.5652 | -48.4143 | 2025-09-03 01:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| e0e4df24-0380-3dbe-b558-2ada6ce1fc2d | -6.4646 | -49.5364 | 2025-09-03 01:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 84ee156e-1a1c-3ba4-89e4-a2869e5f594a | -12.8436 | -48.035 | 2025-09-03 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |


[Clique aqui para ver as próximas entradas](README16.md)
