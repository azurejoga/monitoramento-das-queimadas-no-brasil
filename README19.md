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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a7da27e-6ea5-3495-af9c-dde8d9877af7 | -7.13369 | -42.20094 | 2025-09-27 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 62b05a5b-6d91-308f-8430-ecc10ce7b1b9 | -11.97735 | -46.61533 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95998034-71d9-38ba-9d20-a666718f79f4 | -10.6001 | -46.28279 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7d50aa2-6322-3642-a9bf-6e03d338ede2 | -11.38356 | -45.03193 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3a26832-7d0d-3a05-8e76-a9c092d1ed2c | -11.44845 | -48.52824 | 2025-09-27 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b927828b-7372-3b6b-8b30-5728eced53f7 | -10.57187 | -44.06916 | 2025-09-27 03:55:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 032b7654-ef13-36d4-9716-661c4dc50aba | -12.30425 | -47.21817 | 2025-09-27 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31a605c3-bbca-3630-9709-e1b7e271d257 | -6.99401 | -42.38934 | 2025-09-27 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9635d9e5-3d2d-340b-a8fe-261626e159ae | -8.51533 | -44.61515 | 2025-09-27 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 940990a0-d4cf-3f7b-98c2-3fdc93c5c637 | -6.99475 | -42.38483 | 2025-09-27 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 08552f2b-8d50-3e63-9320-c0a5492b2269 | -12.55643 | -45.84418 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4c465509-ce50-34fe-901c-9ec1723c8495 | -10.11077 | -45.34934 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec23126c-417d-35ca-9270-7b6ee6a847fb | -10.4713 | -46.53208 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f694568b-4f40-3326-86e1-6f8e2d3f83d6 | -10.45485 | -48.21324 | 2025-09-27 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1de9f460-9171-3002-8d72-0de31caa7cbf | -9.99779 | -44.17414 | 2025-09-27 03:55:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e212c334-7a04-3df2-a1a0-9c3452ef1a8e | -12.26332 | -44.06411 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36009c45-00d3-3f6e-9982-f78b443634df | -11.29284 | -47.81213 | 2025-09-27 03:55:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12cd0bfe-0104-3290-be24-bfc913d3d369 | -13.16206 | -44.65491 | 2025-09-27 03:55:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5e0ffbe-3bb4-3493-a1d3-5160fb3354b3 | -9.87342 | -45.90621 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43821606-34fe-3527-a666-86f82e599efe | -11.3842 | -45.02819 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7f4fbed-112d-3653-96ca-e79871e289d4 | -11.3786 | -44.96265 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d4ca0ec-d338-30be-8017-6deef920b52c | -11.34859 | -45.01412 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc892662-0e0a-31f4-a840-053c75830ac7 | -10.11362 | -45.3328 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fd8dea6-5d41-3062-b77a-dd49d20f0106 | -9.05142 | -45.5061 | 2025-09-27 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a1a90c3-d86b-38ba-afd6-79e38ccc8651 | -6.70143 | -44.58864 | 2025-09-27 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73ea57b4-93b1-39ff-8adc-a1830381a1af | -8.83053 | -46.22145 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce196885-d217-33aa-8e77-82d47e83099c | -6.2188 | -47.33169 | 2025-09-27 03:55:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfc03115-d869-399c-ac50-c4937dc67c31 | -11.40814 | -43.50979 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3690878-b0ae-3f48-a25a-1bfc91453bb5 | -7.7134 | -47.30214 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8f3f607-1f09-3985-ba16-e1dcdb0a4a8b | -10.13947 | -46.48024 | 2025-09-27 03:55:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73f0cf8b-0f00-376d-9434-b09030648149 | -11.79149 | -41.20058 | 2025-09-27 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e61a7121-3ee2-3fed-9fc3-32b3d8f6e928 | -10.17001 | -49.37454 | 2025-09-27 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45bb3d27-41b9-3a8e-a3cb-bf82586a1979 | -6.79206 | -41.76262 | 2025-09-27 03:55:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ef07de65-96ee-32e3-9bc8-4a4fd9743b54 | -11.35269 | -45.01483 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b84fbab-8cd8-3e5b-b67c-a3394572669d | -12.0311 | -46.50814 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97715785-8f79-3373-aadf-cf1036a354e7 | -11.43262 | -44.98698 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6bacc4ec-b1d4-356f-834a-dc5d2a92b389 | -12.25562 | -47.16751 | 2025-09-27 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0814fb9b-0297-3184-a4e2-38b3591b0693 | -6.70779 | -42.75862 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bd1c5197-6512-34f9-b560-94372835e4d6 | -6.21938 | -47.32843 | 2025-09-27 03:55:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a1ca01a-36e4-3a7b-95ba-22bab6335713 | -10.5665 | -46.26211 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56b9b93b-aed6-37dc-b63c-c627b1833e31 | -9.05429 | -45.51558 | 2025-09-27 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cfe210e0-c411-3e7b-9528-d1582eb0d7f6 | -7.8113 | -46.96066 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e39fd557-3744-3be7-97ba-5c0723bda839 | -6.45751 | -44.05636 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c852cc1-7036-324b-8f74-1f414c30909d | -11.49465 | -43.52834 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83092e2d-dc9c-3e98-8e76-57d559e458ea | -11.42728 | -44.92195 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ba2c9b8-0ac7-3807-8eb6-9c95043dd3a1 | -12.29471 | -45.653 | 2025-09-27 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb723398-8efd-3a15-8a79-85c0c0571013 | -6.90024 | -44.16132 | 2025-09-27 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c766819-d1da-385e-92af-38d0e1d6e1b2 | -11.61309 | -45.41819 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68318637-2ba9-3356-b96c-06270397b3b7 | -11.35334 | -45.01109 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8c85463-54d4-3caa-83ef-2ea2aed5b5f0 | -11.42072 | -43.51074 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d3c84d2-114c-3a5a-aa87-12d295c0115b | -8.82821 | -46.26171 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75f15420-99be-369c-a88d-49ed71921a57 | -11.69876 | -44.41331 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75c33e5c-287c-3988-9d71-d985d25fc796 | -7.47964 | -42.01485 | 2025-09-27 03:55:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 927073d9-1ecb-3f40-9685-c725723e83b0 | -11.37897 | -44.98494 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21d7c0d7-b09a-3604-adba-aa3692dea49d | -13.37808 | -47.83147 | 2025-09-27 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e8cdfe9-6727-335f-9db4-086cfe7a4807 | -7.77537 | -46.93285 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 014d8fd4-2441-3bfa-b00f-dfdd78e25869 | -7.78765 | -46.94493 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a03dcc1-0a52-3886-861a-48bc0e96d3f1 | -11.40754 | -44.9149 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b72e69c5-54f6-3a99-88dc-6c569fb72e95 | -6.70327 | -42.73848 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 80079cef-f488-32cd-844f-5d78c659db3c | -9.27439 | -46.56057 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ef60413-db8b-32e6-8e00-83f31762959d | -11.97681 | -47.89299 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec36aea5-ff09-38bb-aaef-8cd772189eb7 | -12.28022 | -44.05711 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6a4443b-c4eb-3c70-92a0-ac7d71d4bbcc | -11.35874 | -45.00434 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e26eb3d3-cb26-3c85-ba3c-bbe7c0b3fab2 | -9.71239 | -48.24501 | 2025-09-27 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2107944-b912-3ccc-9762-2d7c68e1a3b5 | -10.11292 | -45.33691 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7888717c-c913-3199-9122-98d43a95c3fb | -8.72732 | -46.69173 | 2025-09-27 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db5f9013-5bd3-3cc4-ba9d-d254bf5b7b03 | -9.9711 | -43.61318 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fb504a7-d875-3b4f-9e05-c4a3074941cc | -12.64652 | -48.15237 | 2025-09-27 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bef2742f-68f8-303c-9e6b-c952c99e1831 | -10.12146 | -45.33849 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d1f88a25-a41e-32b8-a2dc-e798b8757ce3 | -13.37893 | -47.82773 | 2025-09-27 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12b963d1-5fc3-3ab2-9b1e-7321be91d50d | -7.62645 | -43.848 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5b67d7bd-e57f-3a29-b87a-9431bc5700f8 | -7.12257 | -42.17667 | 2025-09-27 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d325d376-53bc-303c-81ee-e2c158250a05 | -9.11317 | -45.877 | 2025-09-27 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9e98110b-9d08-31f7-8cea-c74a30b9a9a1 | -13.43256 | -46.5129 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a68066d3-55bd-3002-a70d-dde9eff5f4d1 | -10.04545 | -50.40105 | 2025-09-27 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99489a13-1c2d-3614-8240-fc82dcd3db3c | -11.96482 | -47.89339 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01257dd8-4723-39b9-a753-42d225a6f010 | -11.7809 | -44.86533 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fd16ab2-5106-321b-bb20-ad355ccce5bf | -11.43734 | -44.98412 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 869faac6-5b5d-3bec-8852-638395ecdc7f | -11.67425 | -44.46181 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cef5d8a9-d8ae-3513-aab3-be8c866ccc39 | -11.68435 | -44.42657 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 159c936c-6770-3c2b-b42c-9ad8a08b97f8 | -11.4335 | -45.00595 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5a98d19-474e-371f-88e2-09e433e11965 | -7.61794 | -43.82465 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57a8c5bc-6a81-3c5a-9b66-04149a59bf5c | -11.78871 | -41.19638 | 2025-09-27 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0b39b48f-1a15-3202-bd9f-c50ddb94d26a | -6.54865 | -43.84278 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33dff140-7c1a-3752-b70f-cbac7f00393c | -7.88055 | -44.02824 | 2025-09-27 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e890d330-e7af-3611-901a-2f34fc094641 | -11.96481 | -47.90264 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84b4c18f-a921-3a9e-b7f1-806febb53744 | -7.87711 | -44.02393 | 2025-09-27 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e08e3ff3-9e9a-3c7f-9f8b-b678011afcc8 | -7.78352 | -46.94434 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 456d7b5f-3e15-3b11-bca8-d7a54bbfe2e6 | -10.47101 | -46.52959 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16c7fe65-2d4b-3651-a257-ddcbd4106e12 | -11.43532 | -44.92394 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54312bb3-0224-31c2-a081-582776eb0594 | -9.04077 | -45.54079 | 2025-09-27 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d0277bb-a2d4-3978-bb3e-9018a7680a34 | -10.44981 | -48.21164 | 2025-09-27 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39f8b565-8142-3cf4-acfd-5f8319a4ae27 | -6.99848 | -42.38542 | 2025-09-27 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6ba7d1e8-26ba-38e5-8547-7c9955c71f89 | -8.66549 | -43.99081 | 2025-09-27 03:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7e9b3a1-8413-3bb7-b809-69f683523dba | -10.5711 | -44.07198 | 2025-09-27 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2a07989-58c2-3890-8032-9dd8f6d4608e | -6.70396 | -42.75801 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a3407a28-c0b1-3374-b891-3e3402ef789b | -9.43381 | -40.74123 | 2025-09-27 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e309569c-03b8-3580-96fb-c300c3648cdf | -7.046 | -43.03233 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1057e20e-32e0-3231-a341-bd7157f5d027 | -6.4926 | -43.27776 | 2025-09-27 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb3cf0e7-6739-3630-b0d4-16f7f8f6aa35 | -12.96985 | -46.91013 | 2025-09-27 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README20.md)
