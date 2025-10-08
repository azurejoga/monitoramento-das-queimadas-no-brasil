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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a50f28f0-594e-3da5-8ab1-1785a316240d | -10.97733 | -59.02531 | 2025-10-08 05:29:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ea5aae8-1620-3bac-91f0-3ec23c6610df | -12.39296 | -51.12776 | 2025-10-08 05:29:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45f2464f-22e5-3da4-a799-74bcd6777cc7 | -10.39027 | -50.23042 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4239cfb-cb7f-3e2f-a663-d97f60d4feb2 | -11.14442 | -54.89428 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c69c4cfe-77e8-3222-ace2-72fc5dbf0777 | -10.86986 | -53.73979 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c31e0de-c07e-31d1-9884-bfa2828713f2 | -9.33566 | -59.5979 | 2025-10-08 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17222c5e-d835-30f0-976b-b1e2573d1d83 | -11.11485 | -54.03659 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 963dfedc-61b7-3a6f-91c8-6ec2b4900c53 | -7.59005 | -64.51185 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45debfc7-c1f0-336f-b6d4-2931c0fc7d63 | -7.59751 | -64.50919 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cbc5636-19e2-378a-9636-e7bb8d5768d9 | -6.69855 | -58.81021 | 2025-10-08 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07f5ddde-e6b2-3152-935d-0f609a6b2ab7 | -11.17739 | -54.87377 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c6910006-8920-30a8-a3ac-e3b53b3f1d4d | -11.74633 | -50.95069 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7b2310e2-766c-30f7-a671-fb1ee3e1c2bf | -7.88388 | -61.18952 | 2025-10-08 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 090ae7a8-2b8b-3884-afd7-1419225ba79c | -11.38023 | -54.35339 | 2025-10-08 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a48fbe5-80f5-3d21-84dc-57406f9f6695 | -11.18262 | -54.8759 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb4d8712-b4e5-3440-a910-fd1ff3ff072e | -7.02904 | -62.98399 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01a442e1-9bd6-3ed1-bcb9-db32202cad8a | -11.11973 | -54.04084 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 900e0168-604d-3294-8a6b-74c2e3e4dc8f | -11.17681 | -54.88117 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bad31a5d-ec1d-3611-9512-114bfbf3df34 | -9.38803 | -59.4255 | 2025-10-08 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c74207d-2e5f-3bf7-b6fb-0a05316ae202 | -11.74634 | -50.9489 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 4a1d7673-ed73-3671-ae1c-e4a62b8e5b13 | -11.1817 | -54.88031 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a5ee0a15-8eba-325e-8bcb-3969a31ca31d | -11.73521 | -50.93215 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f0dbb44d-5295-3857-8986-408567b3a17c | -11.74698 | -50.94508 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 88c45e25-e528-3fe8-9903-465bc5399e75 | -11.01402 | -50.88788 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6d2d7e1-0673-3e35-9472-1a9dd6120a04 | -11.1828 | -54.87143 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9da28fef-8b83-3382-a6c0-0cc9818a56ff | -11.70591 | -50.95686 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 2641c64b-83d5-3468-98ab-3ecaccd05453 | -6.6949 | -58.80966 | 2025-10-08 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c226e44b-df4e-3c97-9b6b-17dbc16e8434 | -10.99871 | -50.90561 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 75b2c2eb-e0d5-3e13-ba30-4b0b93ab5840 | -11.74828 | -50.93384 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| eb568ce5-8e45-3ef6-bc45-5a398982b5a2 | -11.1467 | -54.87667 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2756a4d3-14a6-3820-a425-ae44aa53a6de | -11.11316 | -54.05015 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 810eb0a2-2561-3206-bc89-189a4d0d1fb7 | -11.13551 | -54.88409 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0ffc6da-5f5f-3d85-bca6-04130d2d080f | -12.39291 | -51.12959 | 2025-10-08 05:29:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f184a6cc-96ad-36dd-a1da-a0bb5a71257b | -11.74286 | -50.9199 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 632c802b-172a-304b-937d-fdef6d2bdf34 | -11.14709 | -54.87364 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11191160-5555-36f7-89d7-9c5d581a9256 | -11.75089 | -50.91128 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 44848435-627a-3b95-a4c3-2ac6b2dbaeba | -11.14554 | -54.8856 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c35542ca-84c1-38a2-a3cb-73392dbab448 | -8.15944 | -50.17022 | 2025-10-08 05:29:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f083d9ea-5809-3dd7-a830-ed29fd5b7034 | -7.10359 | -59.77552 | 2025-10-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3aa9f1f-87a2-3b85-9a76-e2d0f78c5e1a | -11.73207 | -50.95842 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a2249c19-0a46-351f-aa36-e520eaa6b185 | -9.26233 | -56.28987 | 2025-10-08 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 476b1c2a-42ba-3744-b7bf-909e527bbebc | -11.18528 | -54.89256 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6c38183c-362f-3a59-8f9f-37e26a150dba | -11.74695 | -50.94329 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| c34bc9fe-b538-3d82-b780-f247c2238f8d | -11.67858 | -50.96465 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e592a7d-8110-3c72-afeb-278a2cc524ea | -11.16252 | -54.87304 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d25c36a4-f661-3eed-a3a4-5468797fa5e4 | -11.1193 | -54.04427 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d31f5847-ae1e-30c2-b504-dd72a3e657c3 | -9.33122 | -60.60035 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7297461f-4b77-3024-8c2f-918e8a060c59 | -11.7547 | -50.93289 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f84dc875-e885-3dc9-b272-4ebd946fa5e3 | -11.13976 | -54.89076 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e2947ea-6ce6-3f6e-abc8-7ef25ee78e9a | -11.76265 | -50.92423 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ace563e9-04a4-36cf-9c09-02649f0f900e | -11.17491 | -54.89555 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4b1e2547-e358-3007-bd78-7e03d787e4a0 | -11.16877 | -54.90208 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c735ae3-7fc8-38a1-84ec-4b4b568cf508 | -11.72418 | -50.97058 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7fe0b9b3-33c6-3bc7-ae72-9d13f8bd7fd6 | -11.17813 | -54.8678 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9ba8548-37ef-322f-8314-d8a71e82ce10 | -11.18206 | -54.87737 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d778ccf-b794-3720-a1c7-4c9142f8ae17 | -10.90669 | -51.02066 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d3103c4-7371-3861-9b27-5415b54fb55f | -11.16291 | -54.87007 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 042c9d77-4f92-3bb4-ba88-f533e6c40ccc | -11.17702 | -54.87674 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c0ea5d8c-7d82-3fde-b3b4-06303842e017 | -11.75023 | -50.91693 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| bce1df0d-7c93-3ca5-ae45-e83fbe6447de | -7.59065 | -64.50809 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16a006e7-38ac-306e-b981-3b4c90ef9c2b | -11.75409 | -50.93853 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f0b89804-cb22-3299-8046-3fd720dd4f6a | -11.75124 | -50.90379 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 0a09bd94-ad45-37da-ac07-9b0763b70270 | -11.17178 | -54.8805 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c64d3f86-f2cd-311f-8934-05dd0868b38a | -11.16098 | -54.88488 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d41e71d6-f70d-349c-a622-3f55ea9521b2 | -11.15558 | -54.88706 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e882e62-bf9c-379c-86ef-edf21118cc50 | -7.82677 | -61.69077 | 2025-10-08 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7ac1bb5-d58a-3d8b-b3da-1730e8251db0 | -11.75677 | -50.91776 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8b59a0a9-c3e8-3c22-bba1-c9e6f8190ea9 | -11.73199 | -50.96024 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| acf24a9f-5dd6-3b63-8e4f-af822d4e96b3 | -12.33071 | -50.26408 | 2025-10-08 05:29:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87ecdff4-4c57-3398-a38f-81fd238ad83a | -10.88719 | -56.0659 | 2025-10-08 05:29:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f915da1-3299-39b6-8078-4f4aec7d69a7 | -6.82095 | -63.07261 | 2025-10-08 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 592ea166-a102-33ac-898f-fae9e7f85348 | -9.63901 | -55.1297 | 2025-10-08 05:29:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e6b1d2a-5acb-330b-a85e-30e197cbba66 | -6.62334 | -62.88012 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d8cab09-bf21-338a-8223-3e0ea622abb8 | -11.75873 | -50.90083 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 82d6474d-2617-3378-80ac-abb399e5d54e | -11.72354 | -50.97618 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| aac53776-2280-3715-b5ab-33eada24b7b9 | -11.42355 | -56.28904 | 2025-10-08 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44a23fbf-dbb3-3a57-abc9-39eba3928f11 | -11.17453 | -54.89843 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5b428a8f-8e09-3192-b94c-f2d66d5fce48 | -10.32179 | -58.49775 | 2025-10-08 05:29:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 801c50d8-5685-3356-b95b-d6f17ad5f997 | -11.16984 | -54.89349 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d4c4295e-a316-3d26-92ca-0c04b4bf98c6 | -7.88053 | -61.189 | 2025-10-08 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c698e7da-d0ac-3486-a51c-5aceaf63a098 | -11.76528 | -50.90166 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| af5c0f28-c2f6-35b7-a496-38c453f6f6c8 | -11.18601 | -54.88676 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1b6d337e-14fd-3cf8-b0c1-0d7e3f57c0f5 | -9.32834 | -60.596 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2434cd23-0cf5-3369-a3c5-c7fdb5754497 | -11.1552 | -54.88997 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23ce52a4-88b6-3e51-8aa5-b295dad4ff41 | -6.59693 | -59.12096 | 2025-10-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af0d9bc2-664b-3833-8b33-68cbacf0897c | -11.75743 | -50.91212 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| b4f65b6c-2a26-3709-ac70-2276227bc5ef | -6.93946 | -63.11992 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cc6cd9f-5f03-3eb5-a47c-08dab1cd0285 | -11.76433 | -50.90554 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e275984b-c7b0-3c5d-8639-7eacff793c3c | -11.17956 | -54.89907 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a524d38f-f892-3819-8e50-61b21458565e | -11.17384 | -54.86106 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46e94af0-bdf8-3e91-b837-39d806684a87 | -11.17255 | -54.87459 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b5b82c1-56f1-3729-a5dc-3260dd3edf65 | -11.17719 | -54.87824 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e88f38e-c4e5-3793-923e-6b8d68a7bb14 | -11.76371 | -50.91119 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6d5cada7-fb90-36e5-b163-e05912d43be2 | -11.75717 | -50.91033 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e4ffd604-c3eb-352d-81d0-7fc8622dc680 | -11.75778 | -50.90467 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| c1b2a7a0-9a0e-3a38-a748-7bfa3f9be2fa | -8.48181 | -54.94523 | 2025-10-08 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b06f4ccd-9447-3985-98ea-1fafce08025a | -6.37027 | -58.20424 | 2025-10-08 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19efa0e1-78fb-3639-b505-fe33c237e41c | -11.16989 | -54.89491 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dbf3f37-4f56-3964-ab6e-7a48bcf14c69 | -11.12058 | -54.034 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d632ed9-474e-3505-9d74-243c84220d66 | -9.60586 | -57.1362 | 2025-10-08 05:29:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README91.md)
