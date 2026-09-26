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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76c92d4f-6928-3e42-8c85-5cf696fec1cf | -9.06193 | -72.21603 | 2026-09-26 06:08:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad6b71a2-d01d-36fe-855e-a730007e7a69 | -8.14487 | -70.94552 | 2026-09-26 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 566bff46-b1b0-33c7-a768-ee30e1d30ac9 | -8.47677 | -72.79079 | 2026-09-26 06:08:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6a6ccde-60c0-33a0-8e37-2c874e9d9fe8 | -8.14156 | -70.94499 | 2026-09-26 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e770ba60-96ad-37c7-8544-b22bf09c656d | -7.67802 | -72.28776 | 2026-09-26 06:08:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be6edd5b-412c-37a1-a5c0-e6ee76ce7991 | -7.19495 | -72.56284 | 2026-09-26 06:08:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba187be0-e6af-31b7-85d8-89cce650c935 | -7.67861 | -72.28408 | 2026-09-26 06:08:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44d88e02-cb1d-3a1c-afcd-81b8e23d1616 | -7.98518 | -71.34914 | 2026-09-26 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8283710-075e-3964-8773-be898ca84001 | -10.68719 | -69.02483 | 2026-09-26 06:10:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92e52702-7f2b-3383-9b7a-7c61ed053fb8 | -12.90282 | -61.72176 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3526bdc-2a7d-3ed1-a116-ee2855acdf75 | -12.89946 | -61.71753 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69e3ff88-922a-3749-8d8e-c9225824a5ff | -12.89852 | -61.72516 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab376a9d-77f9-3e27-a7e2-a898834a08de | -12.9046 | -61.72203 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb23e867-c96e-36ac-b3fc-549324ae0aa5 | -10.59232 | -68.79278 | 2026-09-26 06:10:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ac6d5e0f-3994-3d52-aabb-2a118b784d9b | -12.90413 | -61.72585 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9728bf0d-68af-3f76-a332-7551cfc982b1 | -12.89899 | -61.72135 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 902e0667-fdd5-3d7b-a468-4091226265f9 | -12.90326 | -61.71792 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd8c2c45-5784-3a2a-832a-f8ee96e0ddbd | -12.90238 | -61.72559 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b9c25f5-c204-3bda-a945-237cb01acf54 | -12.89676 | -61.72488 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ea6491-f76e-32fe-91ea-9fdc61265c7f | -12.8972 | -61.72105 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dcc61ba-db86-3106-b0fa-70735d4c2fe9 | -12.89764 | -61.71724 | 2026-09-26 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c576b4a-2c8d-37f6-9e9f-06f6e641edff | -6.97433 | -71.75945 | 2026-09-26 06:52:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0dc97401-5a15-3297-9be8-2a665fecdb48 | -1.13389 | -54.08676 | 2026-09-26 06:54:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 65a186b4-ec58-3f98-b456-1d80d87540bf | -1.14618 | -54.08883 | 2026-09-26 06:54:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 299657ab-92b3-3a8a-819d-c46972bb0056 | -3.26603 | -50.13929 | 2026-09-26 06:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 9990b59e-1c4e-3306-82e6-536df2ec7951 | -5.73368 | -45.05151 | 2026-09-26 06:54:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ca3a571f-dd72-3abe-a761-6c8b2520db10 | -5.77209 | -45.08338 | 2026-09-26 06:54:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 328ad253-78dc-3053-9ded-823966dd1e2d | -4.60428 | -44.64988 | 2026-09-26 06:54:00 | AQUA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| dff85058-27f7-3b9a-87d6-a1ba61be4568 | -1.83904 | -54.7199 | 2026-09-26 06:54:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 477d5515-8220-3166-8c42-f2bcfd407612 | -5.77664 | -45.09079 | 2026-09-26 06:54:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 2fb63f53-b91b-3fca-9286-5ccf09674b69 | -2.15011 | -53.70649 | 2026-09-26 06:54:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 729f66a1-e6ff-3038-b4db-6780b05f5a18 | -3.79529 | -51.02056 | 2026-09-26 06:54:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a52a1f0f-42e7-3117-906a-136d90a18b52 | -5.77485 | -45.10358 | 2026-09-26 06:54:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 4d369d51-a1a9-3dc5-b4b0-ea21742b3191 | -3.87494 | -52.28293 | 2026-09-26 06:54:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 553bb29f-6c1a-3fd8-b321-476463fef6aa | -5.77845 | -45.07784 | 2026-09-26 06:54:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 40038c21-e9a0-39e8-80c7-ac589b99629b | -3.80342 | -49.17392 | 2026-09-26 06:54:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 068d5012-a62a-3ef4-84e7-5d1d18fbd757 | -3.26461 | -50.14864 | 2026-09-26 06:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4a39ab1e-9d11-34d1-b1e0-deaacd69733c | -5.78072 | -45.09778 | 2026-09-26 06:54:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0c2c9899-3ee6-3f23-8593-449a1e66a970 | -3.41724 | -50.42139 | 2026-09-26 06:54:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 317f252b-aab7-33bd-98b2-8b2b3ca18ea1 | -4.45421 | -47.92207 | 2026-09-26 06:54:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 82a0fbcc-95eb-3611-9e6e-7e739a09659f | -5.74239 | -45.06577 | 2026-09-26 06:54:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 852d6818-50c1-37ed-9aa9-48c3ca71738f | -5.77884 | -45.11052 | 2026-09-26 06:54:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9eae2d73-4f3e-37dc-9a11-31b35e2d5ef0 | -4.28584 | -48.61009 | 2026-09-26 06:54:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 416e1b24-b683-38b8-8233-50c162315b0f | -1.83864 | -54.71488 | 2026-09-26 06:54:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 0232c90f-2f8b-3a0a-b96e-0ba1a824075c | -2.99429 | -50.46487 | 2026-09-26 06:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3d286b59-492c-37e9-aee6-bb00e39c0c94 | -2.99281 | -50.47453 | 2026-09-26 06:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 37a51ba5-9908-3d23-945a-5878c5d4d46a | -5.73184 | -45.06437 | 2026-09-26 06:54:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 12bebacb-8f7c-3a09-9050-840e140db83a | -5.74425 | -45.05288 | 2026-09-26 06:54:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b0945f1b-ea19-3a67-ac46-012ce78b6673 | -13.20417 | -48.3222 | 2026-09-26 06:57:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 93a26ce7-29ce-397b-8fa5-43f42e5c5f5b | -10.02739 | -50.14921 | 2026-09-26 06:57:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 41d4d32b-8473-3b03-8366-35a765cb38c0 | -12.15599 | -50.31654 | 2026-09-26 06:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0c27ebf6-f6a8-3ecf-ab7d-aa59a4ca51bf | -10.02605 | -50.15805 | 2026-09-26 06:57:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d675e563-a2c7-3b86-a108-1f3e58266a92 | -12.0134 | -50.64418 | 2026-09-26 06:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4d2bb756-e8fc-39c3-acad-aec50e3f0f52 | -10.30604 | -49.45324 | 2026-09-26 06:57:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 204af089-bd59-377f-bde9-022d1612d37c | -11.95289 | -50.67382 | 2026-09-26 06:57:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3b610c42-7c17-3033-8a04-d521db0325e9 | -12.26844 | -50.35866 | 2026-09-26 06:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c08ec41f-cd2c-3ae5-a019-2f645a8fc122 | -12.27081 | -50.72039 | 2026-09-26 06:57:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 297cb8cc-5ac9-3eb2-adb6-f70948347659 | -12.25933 | -50.73687 | 2026-09-26 06:57:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 17097457-0a35-3eb4-9759-02b51bd8bcdb | -12.24884 | -50.31003 | 2026-09-26 06:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ec41c1b4-6610-311b-84da-fdd0308e9cf7 | -12.14722 | -50.31519 | 2026-09-26 06:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9e78f327-3546-35dd-93f7-720c8d0a1d57 | -12.13979 | -50.30494 | 2026-09-26 06:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4fc4e9d2-a362-394a-85a8-e80f3afd46eb | -12.94119 | -51.05727 | 2026-09-26 06:57:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9cf4b109-8b32-340d-8828-5d149ad89946 | -12.25967 | -50.35732 | 2026-09-26 06:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8470e11d-5d02-39b6-9693-f0dae4adef05 | -12.14856 | -50.30628 | 2026-09-26 06:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1aca3320-6b94-3681-a43d-39e828d51965 | -12.20594 | -50.34241 | 2026-09-26 06:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d32964e0-0013-3ba4-a160-c5917e87eb0b | -11.79074 | -51.00858 | 2026-09-26 06:57:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a466ee8b-f9ba-3503-b2c4-fe4f3720a594 | -11.27751 | -54.43467 | 2026-09-26 06:57:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 83a8d29f-d329-3fb8-be52-bdc55375ec24 | -12.13845 | -50.31385 | 2026-09-26 06:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9ad36087-cf13-3c2d-8bdf-ee15002b0775 | -21.55528 | -48.52415 | 2026-09-26 06:59:00 | AQUA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0149955b-1bfd-3c9c-b1af-1d6c9d48c7e2 | -20.85387 | -49.06278 | 2026-09-26 06:59:00 | AQUA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 660be525-b7b6-3c30-8b0a-3b1866fe6198 | -17.5639 | -46.3458 | 2026-09-26 07:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6663bbe2-9894-3f76-b2c7-900f44dd46a8 | -17.5439 | -46.35 | 2026-09-26 08:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 7e8f6687-c2dd-3a5b-a6fe-e4131f1cba5e | -17.5639 | -46.3458 | 2026-09-26 09:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e1346355-c04a-32e5-812c-5a8e1ed2c7d4 | -17.5639 | -46.3458 | 2026-09-26 10:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 0b0b9e1d-f502-3eaa-a509-3f587bfd4e78 | -12.2123 | -50.3451 | 2026-09-26 10:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| cd5fb3dc-182f-31f7-bf08-9288195efe94 | -17.5639 | -46.3458 | 2026-09-26 10:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 30ecb6fb-6533-3cf1-bdec-40fe00831a61 | -17.5639 | -46.3458 | 2026-09-26 10:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 3d134543-32bb-352a-ab4d-e81d09229eca | -12.1366 | -50.3112 | 2026-09-26 10:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e386238b-4a6e-34b0-a918-916958a99207 | -17.5639 | -46.3458 | 2026-09-26 10:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 166.0 |
| f9bbb900-88ad-3ba9-8e31-057ecede8984 | -17.5639 | -46.3458 | 2026-09-26 10:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 154.5 |
| d164af40-b351-3240-80be-df7e9a515368 | -17.5639 | -46.3458 | 2026-09-26 10:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 4498b9ca-2530-3440-9e70-c417765a550a | -7.77903 | -40.2852 | 2026-09-26 11:04:00 | TERRA_M-M | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 1a8ed523-f3e3-30b6-a138-63ceeb741253 | -7.99632 | -44.15256 | 2026-09-26 11:04:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| b1fb0789-fd26-388d-b93d-bc489f97df5d | -7.77744 | -40.29584 | 2026-09-26 11:04:00 | TERRA_M-M | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 2a56da2d-d274-3f89-9eb0-8ccd5c160dad | -11.9374 | -38.30131 | 2026-09-26 11:04:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 6d1065bb-8751-33c7-bc16-71dcf1b69891 | -11.93867 | -38.29236 | 2026-09-26 11:04:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 833aba90-c988-303f-9aa1-237d3be0addc | -11.13554 | -42.822 | 2026-09-26 11:04:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 43d218c6-7983-31e8-9b00-2d5a796678ab | -7.52919 | -39.10949 | 2026-09-26 11:04:00 | TERRA_M-M | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 36.3 |
| 998161c5-67fa-3a02-b530-fdebd98175a1 | -4.90794 | -38.79711 | 2026-09-26 11:04:00 | TERRA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 77b6ba68-366a-3091-abc0-1665ad2b199e | -4.90932 | -38.78752 | 2026-09-26 11:04:00 | TERRA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 45.9 |
| 39bb608e-1d02-37e5-85fe-1882fdeb9987 | -8.95848 | -37.25898 | 2026-09-26 11:04:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5cc3e52b-223d-3b71-bf78-89a66439d800 | -7.3542 | -42.08589 | 2026-09-26 11:04:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 8ad55794-66cb-3a25-bb44-ef819d36f5ca | -8.26499 | -42.15757 | 2026-09-26 11:04:00 | TERRA_M-M | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 8030c6b2-fc44-31a4-adda-558d19e232a0 | -13.12417 | -42.42351 | 2026-09-26 11:06:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| fd984d06-2256-3245-b375-e22af3f9755b | -14.55826 | -39.63565 | 2026-09-26 11:06:00 | TERRA_M-M | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 3b40541f-225d-33dc-925b-0a542ed68611 | -13.55097 | -40.64538 | 2026-09-26 11:06:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 6075ee24-32fe-374e-829d-ecf471e45ca2 | -17.55865 | -46.3481 | 2026-09-26 11:06:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 47.9 |
| affea7c7-e86e-35f1-a633-b90f6aeb3cd5 | -12.53967 | -42.48453 | 2026-09-26 11:06:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| f27b4fbe-a7b0-3ed2-b1f9-2c3791868dc0 | -16.5706 | -43.98127 | 2026-09-26 11:06:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| d40a23fb-2de9-3167-ac75-cae619c46dde | -16.56828 | -43.99556 | 2026-09-26 11:06:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |


[Clique aqui para ver as próximas entradas](README31.md)
