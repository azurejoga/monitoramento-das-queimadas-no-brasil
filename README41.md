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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7c9d733-8c5d-3d6f-9a4a-85ff900e9342 | -5.97537 | -53.58088 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6caac9d2-3042-324f-bdec-a1ecf6a9cbd1 | -5.2469 | -55.90383 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a30cb1d4-344d-328d-9c9d-78d69877d96d | -10.87014 | -45.31553 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d81e626-b982-30f0-9b18-2392496f62f9 | -6.68746 | -59.94908 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| af1c7fb4-8475-383f-9bf0-0b834222ce9c | -10.18222 | -50.26669 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 017ff3b6-7e75-3195-a8e0-163a0c2b76b6 | -6.38673 | -55.22845 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39099ef1-ca2d-32b3-b2bc-fec7d8e80571 | -8.0884 | -50.95964 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b27dff3-21ec-3b72-accd-f351150477b4 | -4.96939 | -55.85865 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 102ebf33-12d1-3929-9144-4d9c2d9d920e | -7.05185 | -59.2131 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 124ae59c-6c33-381d-8069-dabeaf9e4dca | -6.19094 | -55.40978 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 863f6ecc-162a-3c04-97e4-f241a18e88cf | -8.43765 | -54.69084 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f01045aa-7904-35f9-a77e-8c9535a1a1a3 | -6.63689 | -59.44899 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f73f6eb6-e7b6-3291-93f7-299dea27b31e | -9.69996 | -57.88667 | 2026-09-03 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 109d9142-d9f1-3716-a057-320d6830ab36 | -6.65587 | -46.13632 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cc5b4da-9e07-39ca-bddd-ae5e3c7a765d | -11.32671 | -50.53051 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 8daf3616-a15f-344d-8c68-50ffc4880b49 | -10.56538 | -47.71199 | 2026-09-03 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a94a77a8-4b76-373d-bc35-edc3b202df5f | -14.04864 | -48.40487 | 2026-09-03 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53052a2d-f422-3191-b5c4-da16c1787c17 | -16.07673 | -46.07456 | 2026-09-03 04:59:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f79121b-78c2-3c43-87f9-c3fe2d9339f2 | -14.14625 | -58.86667 | 2026-09-03 04:59:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c6a195b-21a1-3747-ae59-b35c3217ec38 | -18.13584 | -51.81904 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 128799e6-01a1-3b53-a443-0d683a0f297b | -18.53052 | -46.82225 | 2026-09-03 04:59:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c63a90dd-6bda-3fec-b0f8-76ae1324c322 | -17.08318 | -56.84185 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 03444f88-92ba-31df-a8b7-37c760f98a6f | -14.68841 | -59.60972 | 2026-09-03 04:59:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a7b3641-ed00-30af-91bf-5a0db06cbc2c | -15.02252 | -46.85333 | 2026-09-03 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 001d89ce-3ae2-3f1b-a9a6-975d24df4db3 | -13.38226 | -51.37915 | 2026-09-03 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bd0480a-c48f-3b18-aff8-018de80e417f | -13.58629 | -47.87932 | 2026-09-03 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55a125b4-0ba5-389f-8757-55edad6f5b87 | -17.18595 | -54.30422 | 2026-09-03 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 412e5a61-2839-3b37-ad21-e0dca6520ca5 | -18.64978 | -47.287 | 2026-09-03 04:59:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 01c06198-8653-3ece-939e-ec5e1b66f47e | -17.48735 | -47.84735 | 2026-09-03 04:59:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddef847c-7d5e-3a74-982c-af5cf4fc9e3a | -17.15437 | -50.28365 | 2026-09-03 04:59:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2fc93a14-935d-3aec-aa6b-a91336efdf04 | -17.09144 | -56.85495 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a107d717-109f-3a63-9f2d-e6d06de72283 | -18.16923 | -51.79604 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4629da61-6a14-3965-8b42-853aadcd59d9 | -14.13993 | -58.88028 | 2026-09-03 04:59:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 569d56f3-9fb4-303f-b409-620358b844b8 | -17.15122 | -50.29227 | 2026-09-03 04:59:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f8196d5-2fe5-393c-b38b-61da6a6829d0 | -16.06607 | -53.54936 | 2026-09-03 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42f8d461-6bb0-32ed-9b94-4bcfd9282057 | -18.16552 | -51.79548 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2ef703fe-8178-361b-a53d-cbdcd5746ba8 | -17.08468 | -56.85374 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2f6500f5-7677-38ab-9578-5f36f8f72144 | -13.37218 | -51.34766 | 2026-09-03 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 314460f4-1479-30fa-9465-bd9845b278d3 | -13.58534 | -47.87782 | 2026-09-03 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3389414-50fc-3863-9030-77a3ecacbe4f | -17.09207 | -56.85119 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2c0cecee-c039-3ac6-8c4a-fed1f4711002 | -13.58427 | -47.88621 | 2026-09-03 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bf89edf-d7bd-3514-a262-631551258d1f | -18.16488 | -51.80015 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cd1950eb-039c-3773-aa72-1ee1c2f20577 | -17.08681 | -56.86187 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6d19d1ef-143f-35ac-96c9-131043670c0a | -18.14017 | -51.81501 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bf46d75d-0b98-3927-9e3a-a12ce495ab44 | -17.57645 | -44.96971 | 2026-09-03 04:59:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6cbc29a-930c-34d9-b7d4-3eb145f73c19 | -16.93818 | -49.38276 | 2026-09-03 04:59:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b6a7401-c571-35ba-8d03-7d9588ecf4ba | -14.60936 | -48.87304 | 2026-09-03 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd6fc8bf-f04b-3665-94ac-8f753154c0ea | -16.07636 | -46.07778 | 2026-09-03 04:59:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 472b4ee9-c808-3f55-a56a-931da8277070 | -17.48673 | -47.8526 | 2026-09-03 04:59:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f197143e-d0b7-3e3b-aba7-a1bf7a553573 | -17.0798 | -56.84124 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| af1e8993-e65b-3390-9385-c21ba124f403 | -12.42927 | -54.50469 | 2026-09-03 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58ec8285-e4b6-3434-8f13-88cd97e6fdfc | -13.58571 | -47.88357 | 2026-09-03 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd91f54e-9546-3258-82ba-5e264f7f953f | -13.5848 | -47.88209 | 2026-09-03 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 456ba284-1944-3e72-b1aa-dad11c5e4279 | -18.16361 | -51.80943 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c8b8f72c-1b06-3031-a4c9-0ad710fa8d2d | -15.16005 | -49.57908 | 2026-09-03 04:59:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5aa6b9e-5b22-3fbd-80c6-7a4367200499 | -13.57723 | -47.87926 | 2026-09-03 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 473a64b6-fd62-3352-af29-bf360224289b | -17.08744 | -56.8581 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f8343cec-a07d-3656-a122-d76d6c334269 | -17.18987 | -54.30105 | 2026-09-03 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95e7f132-c2b7-3466-8912-5fbc92a43164 | -18.8486 | -47.14398 | 2026-09-03 04:59:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb641c36-c236-3864-92ae-c81c1e909de0 | -18.83377 | -46.44536 | 2026-09-03 04:59:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f087140b-b405-34d4-9102-15a0e0fdd786 | -13.58176 | -47.87932 | 2026-09-03 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3ec6f76-884f-36a2-9c62-0c3ef5b7a4bb | -14.45286 | -60.10828 | 2026-09-03 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcb702e0-dbd6-37ce-94e1-f6be47a46187 | -13.38891 | -51.35876 | 2026-09-03 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a4e26e2b-5f65-381d-8633-f0d9c3ce7f0f | -17.08593 | -56.84621 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ffd88436-ccf1-3df1-9e6a-2e269f5d5d69 | -15.36188 | -47.68497 | 2026-09-03 04:59:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26320ea7-4d36-3a4a-88a8-4c3a2f11afbd | -18.1371 | -51.80982 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f16877c3-c90d-3a1f-8456-22350f6eedda | -15.33347 | -47.04131 | 2026-09-03 04:59:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c490372-d9f6-3e39-8e42-195346eb3d16 | -15.02061 | -46.85524 | 2026-09-03 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 92e79a63-eddc-3159-9fa5-68317bf3176d | -18.16054 | -51.80422 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 044e9b64-1600-3084-b1b4-694779dd5882 | -15.36248 | -47.68018 | 2026-09-03 04:59:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 438f4731-6bf6-36ab-9a6a-85220840a77f | -17.13386 | -55.92986 | 2026-09-03 04:59:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 550ed1f6-6303-3b4c-8d00-1eb3b72a1d1b | -15.89272 | -47.68268 | 2026-09-03 04:59:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a7e2e934-2a95-3aed-bde3-22d7e5f97ec5 | -18.14387 | -51.81557 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a86b5f12-7212-3192-bfeb-fe94adb02be3 | -18.51609 | -48.23254 | 2026-09-03 04:59:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dd67685-1a4d-387e-9ac0-78c63c4b803a | -17.08193 | -56.84937 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c5826dc7-f613-318c-b534-5021f394dc16 | -17.15296 | -50.29452 | 2026-09-03 04:59:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3915eaf3-6744-33f4-b7ca-c53f12a4c041 | -17.18652 | -54.30053 | 2026-09-03 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 215036e5-d4bf-3deb-8474-e5b2f0fee193 | -17.08566 | -53.4654 | 2026-09-03 04:59:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c84c6af-3799-332c-9373-dfbe97cbe33a | -18.1408 | -51.81039 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3a1c2498-68cf-3f1c-b6fe-2f41e6634d64 | -15.33285 | -47.04637 | 2026-09-03 04:59:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f568a887-bf65-3494-bf42-0b680ec5327c | -13.38584 | -51.3797 | 2026-09-03 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1b711c23-f1b5-3c64-80b5-74554d4953ad | -15.0255 | -46.85568 | 2026-09-03 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7f66a90-f19c-329e-8b75-f8db6a3010fd | -16.93835 | -49.38149 | 2026-09-03 04:59:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca9cda00-6f52-39dc-92e6-61c50df8b757 | -17.14697 | -55.95453 | 2026-09-03 04:59:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 23503f08-0fbd-35c8-9123-01b4af986eee | -18.82684 | -47.60484 | 2026-09-03 04:59:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 094ca2a3-fbec-37af-aee9-7de36529f384 | -17.57415 | -44.96994 | 2026-09-03 04:59:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69f478ff-d537-3ef1-b2f6-2a471a8cd1b6 | -18.16424 | -51.80481 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95419a90-c036-337d-8e5c-def5884838c4 | -13.36798 | -51.35131 | 2026-09-03 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e51973d2-ea5f-377b-873c-0022efa83904 | -16.32672 | -49.45595 | 2026-09-03 04:59:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73c6fff8-d356-331d-a373-9f45081e3ddc | -15.25616 | -53.83649 | 2026-09-03 04:59:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4a018b4-8c10-3eb8-b843-493ba5662566 | -15.36648 | -47.68583 | 2026-09-03 04:59:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bde90df4-70f5-39eb-aa66-687e841f10e2 | -17.08255 | -56.8456 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3cd3b7ab-68aa-3b6a-8cd2-338e55987758 | -18.533 | -46.82453 | 2026-09-03 04:59:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a61d2637-a3ab-36b9-be69-f2cbddc67cd2 | -13.20633 | -56.80952 | 2026-09-03 04:59:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0308204f-a9e0-3543-96d3-8a0398c025b3 | -15.79096 | -57.42704 | 2026-09-03 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91b72cd2-b2c9-3a9d-8d0c-7be782bc1433 | -14.49276 | -59.84166 | 2026-09-03 04:59:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92bed49a-7a17-3d43-862a-fb48aaf911b1 | -18.16118 | -51.79958 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a14f545e-e1d7-3050-8a1e-35681f3bd926 | -13.38164 | -51.38334 | 2026-09-03 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8200711c-4c56-3298-a9ea-399496f102ee | -14.14077 | -58.87549 | 2026-09-03 04:59:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5554eaa-c990-3ff6-8f02-db8c97dc3cfd | -17.08218 | -56.8688 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |


[Clique aqui para ver as próximas entradas](README42.md)
