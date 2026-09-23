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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a6ce157-b11c-321a-9731-5a8c1b90f589 | -7.15407 | -59.595 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bb5f30e-a0fd-3f41-afd5-8fe0be266cc4 | -6.74927 | -59.47003 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea3957e6-943a-3341-a7b1-30b0a0d0d60d | -6.30952 | -59.94905 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e08f01a7-d03b-3ea2-b744-c9721c7efac8 | -7.78226 | -50.22742 | 2026-09-23 05:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 960ef9d7-ed58-326c-ab63-45f2a676c233 | -8.19566 | -54.71798 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4203a0de-d7ad-3d4f-868f-3e1799ca9551 | -5.91674 | -55.69239 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6395e93-d6df-381c-be00-17758fba12b8 | -5.98234 | -57.7841 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d390623-2fe3-35b9-9368-ca3cc11884bb | -6.34758 | -57.77438 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5743a933-fc2e-3df2-84a2-2663f053e834 | -6.46992 | -59.96416 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6535c81-e1d5-324b-b3c8-2155f229493a | -7.09792 | -52.75571 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19bea92f-4126-32c6-a7e2-759936b7d730 | -6.07149 | -57.73175 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6eca019b-ef13-3a0b-9129-6ba3906eb00a | -6.16591 | -53.31253 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8296181-e4f3-3bd7-85b3-9ab548dc1e9d | -6.64367 | -59.91954 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 255b91c6-2519-3424-b2be-e91964dcc7ab | -6.05032 | -57.8236 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2361dd36-e9bc-3ac4-a703-d988fc3205fc | -6.38261 | -55.28621 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab127d8a-e529-3cde-9926-d070d3f6a349 | -6.60373 | -59.95618 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8bb90d4-3f19-36ed-ba06-150d1ee13659 | -6.92305 | -55.60695 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5a02a3c-b629-3079-9807-28578aacd9dc | -5.93913 | -57.70776 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52156142-6474-3450-b402-a12c1fb7777c | -6.70834 | -58.9986 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85db2be6-f996-3132-9f1c-49ecb1073b46 | -5.415 | -60.2125 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0388a2e9-20f0-394e-81e4-80a58f2b543c | -7.08754 | -61.09094 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2c399ad-3e96-3533-b868-587d9db421a5 | -6.14187 | -59.9327 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23580ef4-3544-3373-b36a-42b08ddfa3de | -6.39277 | -54.88381 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5a7564b-7aaf-3916-b7f7-efd1613ebfc6 | -6.95019 | -59.82968 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15295b7e-7945-364d-9e76-01c98c583481 | -6.74982 | -59.46657 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 438efec5-1776-3020-bbac-2303c0ecb97e | -6.33444 | -59.96015 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ed1628d-1412-3f81-930b-7c4d7efef90f | -6.76054 | -63.13991 | 2026-09-23 05:25:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 151e0e85-b191-317a-9511-5a74b7b14b28 | -6.67625 | -55.05464 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50b154a8-45ad-36fd-b25c-37b322875ad2 | -6.61817 | -59.9298 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 71cbe95f-ae47-3319-8933-c6ae2519e76c | -6.35965 | -58.28051 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a09a608a-ed42-3cc6-8a29-febd4f26ff96 | -5.92304 | -59.91973 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d307fc42-290b-3931-b9e3-8b1ac37fb7b1 | -6.66997 | -58.57328 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5102dab7-742d-3c52-9132-aca9efa9f8e5 | -6.02935 | -55.34544 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbc4cba9-7708-3cd5-b655-2b90a53a178b | -6.91761 | -59.62823 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6e01748-e8dc-3312-8f40-aea3a3cd46ab | -8.2044 | -54.71395 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 49fd6f3a-8d32-35d0-bdaf-3e5dad4fcd5d | -6.04305 | -57.82611 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0f64350-441f-3008-925f-9f26ce3eaa36 | -5.41836 | -60.21304 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2053ec7-642d-39f4-8022-531f2a0d4807 | -6.71381 | -59.45695 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c496830a-9c47-3c32-8a2f-55a8bddcfe0d | -6.07044 | -57.80483 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0ef3967-bd7f-3444-8f6c-28a8ef9e8b4d | -6.30998 | -57.75014 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e390cb8-9a00-33dc-a781-95cc735a5e52 | -6.92632 | -62.90855 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc28ff3b-deb1-396c-a800-8321e104aec7 | -6.20006 | -57.78116 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73c1d238-e9c8-3fac-9d5b-4899cc4d0c9a | -6.69873 | -59.95735 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b463179-520a-3214-945d-32c98ebd8aa1 | -8.32917 | -50.82962 | 2026-09-23 05:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14b878f0-b01e-35b1-839b-767cf8fa0d7e | -6.10232 | -57.6888 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be241333-7c80-3db8-b3a6-f915c16dff15 | -6.00644 | -57.67407 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6ccd546-e880-3f51-9628-1ead99c50425 | -6.69929 | -59.95384 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34bade39-8b98-3f95-9ba3-b2b931b71e37 | -6.74596 | -59.46951 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70b8e6c4-2c56-35dc-9ac5-af6880db5a20 | -6.11308 | -59.88148 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09773ba4-86bc-396e-b0a1-eae1ec7f89c4 | -8.2766 | -54.76344 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bdbbe99b-3f69-388b-8ebf-e546d448a1c4 | -8.2577 | -54.78173 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 114c089e-cdbf-3147-b94f-401545755414 | -8.28057 | -54.76407 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3c4766d7-c83c-3fc5-b8ac-52d5d2fcf370 | -6.4232 | -59.9815 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d23fc7bb-c917-39dc-ba0b-4acfbd8ba5e2 | -8.24977 | -54.78048 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2683f60e-a5b8-38a3-a669-c1735aa9e2dd | -6.30717 | -57.74603 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee673a96-d448-3bad-ae4f-cc62769b7e93 | -7.04561 | -62.93568 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7e73dda-7493-33dc-8f05-4c9126187253 | -6.42486 | -59.99255 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ac11bca-3504-3ed3-bcc2-012e67aa78f6 | -6.36133 | -58.29155 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28e11067-0564-36a9-81fb-1f251517bd97 | -6.6655 | -58.55831 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87293ec1-fc19-3c59-addd-ac7fc527e9dd | -6.12077 | -59.93651 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e331a9fd-f045-3a47-b373-f57be76872bf | -8.25374 | -54.78109 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2181301-66e4-34c8-9b44-a17bd0e84b1b | -6.3111 | -57.74297 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a86769d1-3906-3e1d-9502-9c7c9925101d | -6.2539 | -57.77822 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bc05a21-0fe1-3e13-ad38-6d79e107a5e7 | -6.73198 | -59.42792 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25112c39-5eff-3494-83e0-4e5b30d7f1bb | -7.57196 | -57.65528 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a05980eb-c43a-3bcd-90da-8761c9cd88d0 | -7.43174 | -49.84209 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3719c164-2dac-3958-80a1-4c9a55a9b5b0 | -8.33023 | -50.82857 | 2026-09-23 05:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e2b84df-b9f3-3d80-90fd-b05504817a03 | -6.14295 | -59.94725 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b144985-a80e-3faf-81e1-29f4529fdd75 | -13.85045 | -48.57608 | 2026-09-23 05:25:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5dd7df91-834d-363f-8119-18b44b8442a8 | -6.73639 | -59.42152 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afee5931-750b-35f4-b8bd-cc73f37aeff9 | -6.13642 | -59.88156 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3193136c-6897-384e-bb4f-ef82617f10ee | -6.30044 | -57.74497 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86d79a71-f840-34e9-9c98-0f51ec872ff9 | -6.70779 | -59.00206 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9a7fab2-d773-303a-93eb-fbf8aac05d5d | -5.92637 | -59.92025 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8d91996f-9302-3115-a70c-43a1aa6cedef | -7.4128 | -49.85831 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0aaf268-015f-3a8d-970d-a95de14e3c89 | -6.35109 | -59.96278 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f2c0423-6c9a-316a-bc49-e9109e9ee138 | -7.09539 | -52.7532 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce53181a-bec3-3dc6-9434-747a93d2c272 | -5.59921 | -60.20486 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4438f7a2-5918-372e-99ff-f2844402836d | -13.85516 | -48.59303 | 2026-09-23 05:25:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 596d0678-c27b-3244-a24a-493330a4d325 | -5.98399 | -57.70737 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 127bb3e3-d8b5-3904-bc26-55df90aaba78 | -6.34814 | -57.77081 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5dac92d9-e01e-37f5-ac5a-6dfa595b2901 | -5.42518 | -60.24625 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15bacd7b-557b-3f08-a9f0-c4c52ce161c3 | -5.46788 | -60.21651 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566bb206-ac39-3f79-b2c9-cb7635283547 | -6.12963 | -59.94513 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b95d92a-7464-3bda-89ac-ed6956946316 | -5.9275 | -59.91325 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ec36e83-70ed-37bb-b8a6-3dd8e9af60f5 | -8.73433 | -47.59611 | 2026-09-23 05:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a507ce71-46a1-3b37-bc65-2455737edb9f | -7.58105 | -57.66423 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98dc0638-d686-3bcc-a5b5-5dd34095ac83 | -6.466 | -59.98865 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6e7afc2-1f75-3c66-bac6-a7ac973788b3 | -5.99914 | -57.72073 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b34fb174-964a-3bc0-bceb-c4885e85b8ea | -7.01594 | -62.90811 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79216481-efbb-3d5b-9379-1c6ea42cedad | -7.58502 | -57.66108 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5deb70d-ee73-388d-8a19-1295a0d4e116 | -6.56499 | -55.41089 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c65275a-8058-3878-a90d-ab162fc1953d | -6.34335 | -59.94719 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ba4155e-3e26-349f-840b-45d27b9ed183 | -6.92093 | -59.62877 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6832918e-4fb7-3761-b20b-3771d6b48a23 | -6.6852 | -58.45397 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56bce804-6e0c-338a-a0b3-5469b5000282 | -6.63147 | -59.93193 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 306c2755-14d8-3c7f-958a-27e55d4b2c89 | -6.4455 | -57.87689 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59b8e14f-7042-3cbc-b318-6934dc21bd62 | -7.78493 | -50.22778 | 2026-09-23 05:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00bf00c8-6c94-3634-8e11-14fa957dfb7a | -6.81213 | -59.43743 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e89a4740-3d2e-36cf-8398-9c92af21ea76 | -5.42307 | -60.21665 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README119.md)
