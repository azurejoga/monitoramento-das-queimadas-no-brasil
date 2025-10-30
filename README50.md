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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a52fa70-b84d-3cae-bdf2-bb528df80bbd | -9.40727 | -43.72156 | 2025-10-30 04:25:00 | NOAA-20 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 36f79562-1659-3f32-9a54-f6056a39dac9 | -7.75465 | -47.54876 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad9a769a-f7d1-3441-925f-17c1fa359567 | -5.61088 | -47.12303 | 2025-10-30 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8d78c4f6-0067-3bdc-a516-328bea4adb11 | -7.96128 | -46.72169 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 422d3763-0262-36ba-9393-f34bed113668 | -10.85811 | -47.86659 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dd550b6-739d-3edb-841a-f0344d980c93 | -6.85595 | -42.13979 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 11b6b7f0-74a3-3951-a6e3-0ca5f56810d6 | -5.43456 | -45.33605 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b80eea6-597e-3cde-9d52-41a78f372cfa | -4.90916 | -45.6749 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b044841-a9fe-3638-be1e-d38b2c87105a | -7.39639 | -43.65501 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4d677996-8099-3630-9c38-7c79eaac9782 | -12.03035 | -44.80527 | 2025-10-30 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38c34ba1-2e12-3f22-9991-6aca24c51517 | -4.91917 | -45.71881 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 760f090e-fb02-30e9-abb6-3f5cbbec9298 | -10.13484 | -48.07567 | 2025-10-30 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6ff71394-5644-39b9-9d2c-04eb5f0718c9 | -8.32464 | -47.933 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b2b73186-b1be-31ea-b142-22de1460731e | -5.25344 | -44.27506 | 2025-10-30 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d756923-34e1-310c-8ecb-67e6542a5bf4 | -9.61895 | -47.77397 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95767fda-4022-3141-8e3d-740d14b9140f | -7.38409 | -47.63879 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62b0dba3-92bd-37c9-bceb-ee322f005609 | -10.88408 | -50.09022 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abb0b4e6-9eb2-3ac6-82b9-fc43f162e35c | -4.1803 | -47.65094 | 2025-10-30 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5051072f-b8c5-3029-8644-7cfc1629f2de | -11.25675 | -47.62527 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d721372-e7a3-365d-8ec2-65ba6341a14d | -4.23475 | -48.37241 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25227068-0898-3546-92ac-e1793af8037f | -7.05491 | -46.2654 | 2025-10-30 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be04b267-ea69-3373-be3b-c0b20984361f | -6.95878 | -44.84228 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 603b5ebd-894a-30d0-97c4-d7c96ac6e033 | -10.10999 | -45.15016 | 2025-10-30 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7b83582-5fe4-3dfe-bdfc-ee90488e1c57 | -7.1621 | -44.86557 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 305eb622-c3dd-3c5f-a182-0b653888d42e | -7.2259 | -46.66798 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 703488bf-5954-3f36-96b5-161eb8bb1ccc | -10.90197 | -47.99696 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24a7b8e2-e95a-3b4f-945f-ff47a00eec28 | -7.4543 | -45.47229 | 2025-10-30 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d8c23be-f856-30d8-afdb-4f70dc5bba29 | -5.70366 | -43.16092 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 169bd663-180d-3846-8035-bb6deb8d3afd | -4.46864 | -45.75362 | 2025-10-30 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9703643-b006-35f3-a170-1b1ad77dae94 | -11.91436 | -44.17434 | 2025-10-30 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af9b896f-1a5f-3382-af07-1aade8d623d8 | -8.01312 | -49.71804 | 2025-10-30 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb2ab026-7139-36c5-a394-b5762acbf1af | -7.79944 | -46.4581 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6cc0cace-b757-3700-9367-48045f088893 | -5.79013 | -40.81531 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cefe7d58-3b66-388f-911f-b247ab65664d | -9.82194 | -47.69429 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 128c4c8b-b91d-38f7-aca2-fe2b02aba903 | -6.33329 | -46.23219 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 048ad8f5-6433-3dda-a529-88c4dd3c86d9 | -7.16461 | -44.99496 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 45756baf-6edf-3e79-bef5-cb71013d8a31 | -4.6776 | -45.80739 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40ed12e8-5137-3883-a89e-716c5774caac | -5.61144 | -47.11947 | 2025-10-30 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a5e3460-a36f-3a92-b96c-bfda023e7672 | -7.92552 | -46.79774 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd663923-62fa-389f-a818-5a898a0c0e7c | -11.14832 | -47.77343 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f87f5b60-71fe-30a6-b305-79b48a463049 | -6.14372 | -41.69033 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a4a82536-c94d-3fa9-816f-a627d0c4df5d | -7.30159 | -45.66822 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0da3ca8e-684e-3327-a8b2-0ae1d5bce2df | -7.86869 | -44.2354 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cb24cb5-caf4-3020-a5a1-238c346abefa | -7.88088 | -46.73732 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3198a356-f008-3868-91bf-20b1ece60d99 | -10.43147 | -40.5031 | 2025-10-30 04:25:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7b733c91-4182-30f4-8556-6943e8175de8 | -6.15407 | -41.59665 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 559aca85-1797-39d2-bea5-1cde21544327 | -10.21619 | -45.96463 | 2025-10-30 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91d300cb-5995-32f2-b14d-836ea152e7f3 | -5.22987 | -46.13801 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d185afa0-8f13-3e3f-bf5e-6dc236aefd69 | -11.00526 | -47.77499 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6da689c-16a2-3aa1-9ede-bc1e05a90392 | -10.65078 | -48.79494 | 2025-10-30 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5a155ee-f3d1-339e-8729-24cb16af3fda | -6.15211 | -41.66912 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ff9914e5-dc70-3135-a362-11bc09de6033 | -8.3258 | -47.92582 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6bc1d9f0-50d9-360b-b154-494378179b29 | -6.40402 | -47.06914 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81f2b63c-9a15-313d-98cd-04f7caf711c9 | -5.0403 | -44.88148 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6438302-3c5b-3aa1-b079-093677f41e3b | -7.70913 | -46.9837 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14bf6b9b-1ae2-39c8-9ea6-e9c43e552430 | -10.68027 | -48.04443 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d64479c2-0eed-3029-ae6f-d65ab0b86964 | -10.97816 | -50.11323 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee4f2da1-ebb6-3406-92d5-fe50cf2a3cb6 | -6.39254 | -47.39697 | 2025-10-30 04:25:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c21d14e-e879-3dac-89c1-275c87cb31f6 | -9.89116 | -44.88316 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cff03e56-127d-3435-9579-beeb5f7ae32c | -10.76097 | -47.83601 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 920fab3e-c558-396e-a9ed-e1bdcf7993a9 | -9.84187 | -44.88779 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bfa8a742-87c3-32c9-b4ee-fb32320f08e2 | -5.02525 | -43.59819 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae1385b4-7725-317b-b6ed-a98c032392b7 | -7.45603 | -47.18679 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5534de75-eea0-379f-a818-e5ad6d54a365 | -7.78527 | -46.41645 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1327ea5-1542-32e3-b34b-bff3df647d00 | -5.57424 | -42.17688 | 2025-10-30 04:25:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5e9ed961-1d58-35e4-989b-783df7fbe231 | -10.27922 | -44.58141 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64cee62e-65f8-30cd-8d62-3a0ab02470ed | -5.43015 | -45.34249 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87bd1843-6afc-329c-9e75-d2d0d237f7bd | -9.82138 | -47.6978 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68390f7a-dfce-3d78-b2b2-fdee71b94752 | -5.79069 | -40.8116 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24dd1510-9dc6-39d2-b062-984e1eab35b1 | -11.21883 | -47.79938 | 2025-10-30 04:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8673c533-af31-359c-82aa-d4b9ab45c62d | -5.60389 | -42.79556 | 2025-10-30 04:25:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13633499-4333-3bb8-a45b-81893e14b9e5 | -10.647 | -47.89024 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddecddf2-b36b-3fa2-a318-98a15f5b24f8 | -5.60754 | -47.12249 | 2025-10-30 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2c3257fe-3fcf-32f5-9701-60067d2d6134 | -7.32998 | -42.49223 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9ba4e82f-bc93-31c6-b2d1-9363671d538b | -6.92033 | -42.25442 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7dd2f8fb-ccc4-390b-a454-b8263a218134 | -9.84817 | -44.89259 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fdd06ab-8fc7-39f3-9f08-77dbb9b2f3e5 | -7.48242 | -42.73334 | 2025-10-30 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09c719f6-a5ee-3367-9908-4bbff4a91e1a | -7.02955 | -47.62273 | 2025-10-30 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f3ec6f6-0d46-3b60-91d5-97f4c9fea790 | -6.95187 | -40.91261 | 2025-10-30 04:25:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dfc56282-a674-3a15-a0f3-157aafe7ffe5 | -6.5574 | -42.35243 | 2025-10-30 04:25:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 832e7e91-077b-3faf-9d31-389bb8a0fc02 | -10.85479 | -47.86604 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 196ad711-66a2-3635-b0ef-d1ceb396e1cd | -7.07357 | -44.467 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bf9b810-7279-399f-8292-5b0df7de3784 | -11.03936 | -47.83831 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27d51107-f446-33dc-89a8-e13abd12a115 | -5.39823 | -43.12142 | 2025-10-30 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4e7ddc4-56b4-3408-a0f4-3b0688b00b75 | -5.86166 | -40.78059 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 27c47a5c-68fb-3e07-89a8-6c58dc9476b6 | -4.33468 | -47.8896 | 2025-10-30 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 53be0724-7741-3cb7-81ee-f980fe98e913 | -10.98103 | -50.11793 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50b95c7e-e7c7-3930-be7d-1bb8efc14e7f | -5.06901 | -45.13308 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da46a8c2-6914-3cc2-80a6-ac59708dd297 | -9.81749 | -47.70079 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd8cc803-a0b7-387d-b59a-bcee0d6e7d1e | -7.59772 | -43.56443 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cf8fc58-ae43-3fe0-9fba-4fd5466a28a0 | -9.09356 | -47.78662 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cce2bb53-9ad9-3bb0-88e5-043f4935badc | -5.58506 | -46.47099 | 2025-10-30 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4b6286a-1cf1-3cba-8a45-bb5dd692a4d7 | -7.79079 | -46.42443 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 399f3e35-41c0-3c43-a2cd-3f174657e8d4 | -7.27279 | -46.88526 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f15b51c-ea0e-32c1-899a-c2c9b513a3b6 | -11.55313 | -47.96252 | 2025-10-30 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f47c983-d315-3c4c-9098-0d38cf93c8c8 | -10.99453 | -47.8634 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4eb96a91-d8a8-31ba-bfd6-b2854f15e37d | -3.73756 | -52.14294 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 906c654e-2eec-3ed2-b88e-9fd2a66bea78 | -6.13408 | -41.71125 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8743f56c-246f-3a87-a3d8-16daa30fafd1 | -7.22425 | -44.3293 | 2025-10-30 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6355fbee-ea39-3e91-a4df-0a01f1198300 | -8.15681 | -45.47665 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README51.md)
