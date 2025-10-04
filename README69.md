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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27a15ed8-457c-3540-88ac-3bccd5e4fe8b | -10.19264 | -45.4806 | 2025-10-04 04:14:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4608ddd-c4b3-309f-bdfe-f3b3abc102d5 | -12.71466 | -48.56832 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae75885c-9cfc-3f02-8a01-adcab3b96a8b | -13.4681 | -47.26418 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 75ed1d2e-e562-3190-8fb6-3497487cede5 | -11.12451 | -55.46824 | 2025-10-04 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6296d3e5-0559-3b4c-ac78-3d1c1e8e1264 | -14.75284 | -48.14322 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2468e33-3fab-3297-860c-687ec02c566b | -11.79621 | -45.01729 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63b522bc-b5ff-32b5-abb8-10b920eee020 | -8.01344 | -55.42183 | 2025-10-04 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e26438d5-b10b-3f58-9ed9-318d519ffbf8 | -12.52847 | -45.96597 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5bd1e4ee-9db1-352d-b862-a4162c03fb7a | -13.67215 | -47.30203 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fefd912-774c-383d-bd58-cdfc34f2f462 | -8.6678 | -47.21897 | 2025-10-04 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d03971cf-2265-3d6e-a2ec-97cd616d5c9b | -11.13168 | -47.17675 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f134ebb-93a7-39d7-803b-8e5107839f0e | -12.90249 | -54.75322 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a23f9953-6224-32fd-a2e0-f41638c2d638 | -13.30171 | -48.1379 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05120641-62c9-37bd-8ae7-59cfe7d8e42e | -8.0186 | -55.4198 | 2025-10-04 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4aab8ce-15d2-3b63-aed7-13711f500530 | -8.61302 | -54.97103 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0dffc922-e316-3cb8-8758-b8474230f760 | -13.1211 | -47.83376 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7f23cc7d-2cfe-3170-a430-62b031b96b88 | -12.53003 | -45.97761 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ade71a11-89db-3d5d-9c2c-220a337e0cbc | -12.698 | -48.55171 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 30a21f27-874a-35f5-a1e7-eca2605ee05b | -13.31153 | -47.57022 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b26cea90-1911-3844-a61f-fef2a525bca5 | -11.48261 | -45.02013 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a687ba8c-45ca-3a6d-bccc-a22619b8a985 | -11.79507 | -45.02444 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea5ec34c-c563-33dc-bb04-b0f16547f633 | -14.83802 | -48.37112 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c54f4bcf-33da-35f8-9d8f-fde42449481d | -11.80342 | -45.03333 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46b3a2e2-6cf2-3f22-ab18-c56fac2a1f2e | -11.91027 | -46.3692 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cf2065d-2fde-32d2-a58a-f018a8ee7663 | -15.35119 | -46.29805 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e6947e80-1489-301d-b2fb-5ea72f2ec17e | -11.10048 | -49.81083 | 2025-10-04 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2048dd89-4f2a-3e44-adb9-71c0bb2a380b | -9.94767 | -43.73679 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7452cacc-b752-33c5-8b78-d4edf58fa9a9 | -11.43229 | -43.49319 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77b3a6a4-3cc2-3d1f-8a44-be1fe72e7eda | -11.91905 | -46.35898 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b35a839-23b9-37be-a3a3-da204150720c | -12.38639 | -54.46316 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03d8eda1-2fdf-3ada-b292-7cf30ca86969 | -13.93115 | -48.16589 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d76aa4b4-2bc3-3a3d-9142-e8bbbb58b524 | -13.11024 | -47.91902 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca079ffe-6864-3647-ad48-33859aa2a29b | -9.33454 | -45.7751 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03c4e7e5-97b9-3ce2-ae7a-33f2ac9442e5 | -13.75521 | -48.05375 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f16ceea1-d7c4-3970-a4c7-7ebbe9711213 | -15.29912 | -46.30003 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0388dea5-1b2d-3999-8de8-574106820901 | -8.84493 | -46.83048 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9deae91-1a83-3616-9107-b3f2243dc023 | -11.79577 | -48.92377 | 2025-10-04 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aab1b02b-db3e-3bdb-9697-e61efa111cc9 | -14.44531 | -46.10277 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 525b0667-8532-3aa9-8971-63b386de0c7e | -8.5667 | -44.64472 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61cabac0-3092-3e0a-8a94-63269f515238 | -9.92481 | -50.20364 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fec7fa51-467e-3eb6-90f2-3afd387146d0 | -8.91753 | -46.06459 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ac6354b-3b3b-355f-822f-d42eae376313 | -12.42612 | -45.15783 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62d4332b-350b-3bd6-8c84-8dba9ccc90db | -9.89956 | -43.74045 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| df84ca7d-1478-3959-a077-e777b5220aa8 | -13.93328 | -48.1753 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62a36787-f33f-3bb5-a811-8556fd72831a | -14.42006 | -46.35149 | 2025-10-04 04:14:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f37109c-a65b-332e-ae71-c2de594b7cdf | -9.94629 | -43.57279 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83a4da70-c714-3d65-89ac-1aa61d3f62a7 | -12.92879 | -45.07309 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba821d72-9c0e-3c02-b743-e2aaed0f2efc | -13.29524 | -47.60144 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2c96f12e-1aee-3933-bada-7eefefbfe676 | -15.78649 | -42.04737 | 2025-10-04 04:14:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 48a5f6eb-4940-3f1e-b675-6a8118050a31 | -14.68056 | -48.06727 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cdcc98b-1300-3fbe-ad0f-260558437cf9 | -8.50721 | -44.6939 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 631c1a09-6c10-341c-9876-0e836f7e6a16 | -14.66347 | -48.29454 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6a0516c7-3c2f-3ac9-b283-3e40797ddeb7 | -8.23181 | -46.79811 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa19baa3-879e-38f8-878f-793a4e62833e | -14.91226 | -48.28822 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c68c0b98-4565-3ab9-aa76-f84c2e7701a6 | -10.57401 | -48.70062 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d40e1dd-72a2-314f-bf0c-05fd235c2465 | -14.65008 | -48.30685 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 346ec93a-a7a3-30ba-95bc-085ef990e90d | -12.8437 | -46.8576 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5601510-078e-3b79-8e60-014352e01383 | -14.59754 | -48.24141 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abf381ef-ee1f-3c30-9e2c-4558e70c0244 | -8.21721 | -46.79567 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 533994e3-98b0-3559-b1dd-f4baa757727f | -12.31148 | -45.38099 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66a4f66f-d5b5-309f-81ef-67f84d4e6e22 | -14.45962 | -46.34309 | 2025-10-04 04:14:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e532817-3288-3c38-ba24-c8887bd4fda5 | -11.50602 | -45.00213 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a7a1c29-15a5-38fc-9cb0-7561ff79f3c5 | -10.0718 | -48.18449 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e2a6023-e127-38b3-9368-33e418614380 | -8.87268 | -47.82198 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07310eb9-70d0-319a-a81e-9d209f7b6843 | -12.91231 | -46.90479 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3658411f-ee6c-3e2d-aa75-8d74861f7651 | -9.34217 | -54.52444 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 92070d75-4074-38c2-85fd-e2338244721b | -13.12193 | -47.85068 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a46cf7ed-8bc8-36c3-8885-796842f94f52 | -13.3268 | -47.62349 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84ebda92-696a-3b8d-a7c2-d6a53e96d245 | -10.27373 | -44.33799 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1620528-7087-3954-ab15-3447e507c49b | -14.21019 | -46.06252 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3da60d15-07fd-3822-80f3-e7574710809e | -9.11724 | -44.38853 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12210f0c-2466-3c41-8935-382ca9a0e037 | -8.50688 | -54.59743 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47662d37-39e1-387a-9876-8bffdb5ad295 | -9.63844 | -54.31791 | 2025-10-04 04:14:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51ea6282-7bdc-3f5c-95b5-238c191f3ede | -14.19333 | -46.68032 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5fd30ac-6e72-3469-bb48-748a6aec99d3 | -11.17273 | -47.75068 | 2025-10-04 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e22894a6-5065-3b65-afa5-b3a4b9f85912 | -12.27354 | -55.12915 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09b87fab-2e13-36a5-b7c9-cdeef465f2e3 | -9.06028 | -46.66524 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fae3b14-7f1e-3a5b-b028-13b89c3f56a8 | -12.93674 | -46.38331 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a03f4607-eca6-353e-a766-8d6dae28b497 | -13.47095 | -47.26874 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f6346caf-ddd7-3656-9c72-5fc4941a3049 | -13.99438 | -48.19021 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 518c24fe-ba8f-377b-b904-b4e420573aa7 | -9.94878 | -43.75127 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f2730778-3e76-3138-a54a-d8331fc48075 | -12.57993 | -48.12718 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e6d90155-95eb-33e6-ad1c-361d96e49245 | -9.91003 | -43.7171 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5a56e8fb-3dc0-34c4-9e9f-da9cee457ab9 | -14.94071 | -46.87199 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36686ab2-b576-3b76-aa59-2fb00eb0b00e | -11.12186 | -55.45269 | 2025-10-04 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65150f1a-bfa0-33b7-ad8c-024de6cfd8d6 | -10.33896 | -43.73214 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaa2e883-ced9-33f8-a19b-a6807fd597cc | -9.25707 | -45.77811 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5a011c05-674b-38ee-9943-8f438dda20e1 | -9.9415 | -50.23496 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd0d6b4a-7a53-37e3-b343-72ef3bb88473 | -8.82492 | -44.81119 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d87f5d74-a0b3-3525-8887-f018d4676473 | -8.70759 | -47.98406 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 181d4a9d-91f4-3f63-a795-a4aafca554c4 | -9.30953 | -54.53538 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ecd016c-b66c-30db-86e9-070d3d09783d | -13.29445 | -47.82582 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 526de0e9-bcee-39eb-aeb3-3a2ddac107da | -8.17618 | -44.13212 | 2025-10-04 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82ed2cd8-0b35-396d-b626-5cd02e4de227 | -11.86257 | -44.96273 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9db3656-001c-3be7-9fd9-65aa5295ea0d | -10.63913 | -49.14151 | 2025-10-04 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92e3c99d-6ad3-34bc-bf17-a02915ab55d9 | -13.31965 | -47.79371 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0510f6d7-661f-326f-851a-24916c95dad9 | -13.33451 | -50.9491 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f42ad60e-ccd2-3f9b-b20d-3d8857efebdd | -13.73321 | -47.92117 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 43de51f8-c6c2-352a-a138-40728ea61a4c | -12.64502 | -46.98071 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f2a79f6-86db-3cb7-b790-c172c8c8df5b | -10.05587 | -45.56835 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README70.md)
