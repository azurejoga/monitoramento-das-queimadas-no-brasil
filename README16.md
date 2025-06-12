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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aec407c7-bfd4-396b-85c8-b5bb52d87622 | -8.65848 | -47.12948 | 2025-06-12 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3714fb7-1c5a-3b5e-ad06-ef8b16030755 | -5.8581 | -43.82574 | 2025-06-12 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aef4adc9-8067-3eac-8268-b9c0a1e776cf | -2.90207 | -54.4891 | 2025-06-12 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c80a78e0-0d0b-3122-8857-356a90a08dd8 | -9.41018 | -48.42886 | 2025-06-12 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd745827-6701-30d0-b797-367fc4816aaa | -9.00504 | -48.73753 | 2025-06-12 04:49:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6952bb1b-24c9-31fb-90fa-18989f422f9e | -9.4062 | -48.4283 | 2025-06-12 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6d1f738-1590-39a7-a50b-630169ea3b39 | -5.12186 | -56.11731 | 2025-06-12 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d26bfc5-017a-3d08-8a87-d4932818c824 | -9.85437 | -47.87682 | 2025-06-12 04:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fce473d9-8c0a-3af7-af90-03775f2bd32a | -8.04687 | -49.64647 | 2025-06-12 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54b18bad-d176-332a-bf96-70974ae9d780 | -9.85382 | -47.88067 | 2025-06-12 04:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 216c479b-5ecd-3a1b-831e-c5b29ac5ad7d | -10.17657 | -49.35621 | 2025-06-12 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e94d01d0-6499-3b6f-99cd-1ba81069b419 | -7.23507 | -43.10658 | 2025-06-12 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbc026e8-9d34-3816-8137-7acb25754562 | -8.66277 | -47.13009 | 2025-06-12 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bda4e3c-d615-3175-bb54-ef5909ee099b | -8.75216 | -51.14368 | 2025-06-12 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c82df7a-a736-3043-9991-d4bbd9444777 | -8.04259 | -49.65021 | 2025-06-12 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 640fb963-0a91-3a88-b2be-a5841727ff41 | -8.7519 | -51.14307 | 2025-06-12 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f01a0149-e250-39c3-ad85-93145cab3a16 | -5.77491 | -43.61649 | 2025-06-12 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c4e02e8-47ff-3653-8a1c-1f59cb86b3ec | -9.41417 | -48.42942 | 2025-06-12 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3f3b4c7-ed88-3ff5-a2c4-74c748ee7417 | -6.96106 | -42.80595 | 2025-06-12 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 863c96ca-1beb-3084-bfdb-98945500c3e2 | -7.22951 | -44.79084 | 2025-06-12 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 517d618a-4653-3bc1-8a1a-47624dcdc562 | -9.60213 | -49.02308 | 2025-06-12 04:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cedcf51d-4b74-36bd-b1fd-f2ef22c9e8aa | -9.38632 | -48.42531 | 2025-06-12 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8780f60-bcc4-3552-8448-0d6edf83769e | -8.58954 | -47.09035 | 2025-06-12 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ec353e5-ee8e-3a37-b95b-4a8146cbd124 | -9.40223 | -48.42771 | 2025-06-12 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5946ec5-1c9f-3e97-b455-f21ed60fdb0c | -8.58615 | -47.09494 | 2025-06-12 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bf15ca1-3495-3678-a50e-5594dfe78d6e | -6.60472 | -44.25698 | 2025-06-12 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2efd4efe-f72f-3a77-9c06-e6084d63c259 | -6.60431 | -44.2598 | 2025-06-12 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f68500d6-e29c-327d-9939-8e551e225e42 | -9.0067 | -48.73444 | 2025-06-12 04:49:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71385de2-c1be-32ab-a4c9-8a75943816ec | -10.03584 | -48.78195 | 2025-06-12 04:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 814aac7b-488c-34ae-aa2a-dcb366ee303a | -10.13664 | -47.43837 | 2025-06-12 04:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79cfc7de-17c4-363d-9eb7-ce7cb0ff0a06 | -8.59046 | -47.09547 | 2025-06-12 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5bdc94e-b323-37c3-9c33-d31b2d91ea21 | -7.86406 | -47.88704 | 2025-06-12 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bb1e504-48a7-34ab-a44d-29cfc8df43ec | -8.58896 | -47.09453 | 2025-06-12 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e413640c-c552-34df-b0ce-7444772e6f8d | -9.39825 | -48.4271 | 2025-06-12 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c6036fa-8dec-365f-91e3-ccdb089b65f1 | -9.9896 | -47.84478 | 2025-06-12 04:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f73abc64-58f2-31a6-bde3-681fe04836d1 | -7.23028 | -44.78531 | 2025-06-12 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7478e41b-4071-33e5-b8cc-ad562014fca2 | -9.60633 | -48.53959 | 2025-06-12 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9ec253d-3990-3934-86f4-dd7515fc75e3 | -2.90177 | -54.48964 | 2025-06-12 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad6e3196-d7c1-333a-acde-37263383546f | -5.85766 | -43.82885 | 2025-06-12 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caf81696-2f56-37ad-b559-4058d9540027 | -6.94939 | -44.56316 | 2025-06-12 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 291f8d2b-07a5-3365-b7b3-cba9737dc494 | -8.74874 | -51.14314 | 2025-06-12 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb674254-f647-32b1-868b-ff9401a6bac6 | -7.24061 | -43.10727 | 2025-06-12 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd509c3e-d16c-3404-b60e-bd54353db4fb | -6.94441 | -44.56239 | 2025-06-12 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c3a9138-9a56-3d34-a3c1-5f768e6b5acb | -9.60349 | -49.02557 | 2025-06-12 04:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce3894a5-afe1-312c-b4b0-33c7b2cf9412 | -4.71301 | -48.43109 | 2025-06-12 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8517869c-3502-3f68-9b90-9325f8201ba5 | -8.31203 | -47.91914 | 2025-06-12 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e12a2a4-5fbc-3e82-bd3b-6568d4e2987a | -8.7202 | -47.85184 | 2025-06-12 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deed1963-f004-3cc4-a3e2-035c37a79934 | -13.8864 | -54.6519 | 2025-06-12 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| f57e21a9-e9d2-306e-980f-e9e299ff64f2 | -10.80899 | -55.87188 | 2025-06-12 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 724d8cdc-7627-314c-855b-f077c5e99256 | -12.47302 | -58.47126 | 2025-06-12 04:51:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c6719f5-9f59-378e-893f-19528e83b7ef | -11.37379 | -55.11579 | 2025-06-12 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22bb0261-cec0-3ff3-80ec-d38cfd77eaf1 | -11.77116 | -54.37378 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5506c50c-b0b9-36ed-b753-ef25073dc6f5 | -10.65382 | -49.41899 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b77d1602-0851-3c0d-b3f4-146ba79c0068 | -11.74659 | -54.71909 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 775bbb0d-df42-3fd9-99a1-52709b3903d8 | -11.83419 | -60.92307 | 2025-06-12 04:51:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44cc05b1-beee-36bb-a55a-0312b935019e | -12.13715 | -54.65547 | 2025-06-12 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a23fcc0-ba93-3fb6-a811-50986c7a8e16 | -12.13658 | -54.65902 | 2025-06-12 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2923119b-0b83-3eb8-b81f-3ddc935103ab | -9.65761 | -56.10703 | 2025-06-12 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef205e86-90c7-338e-b3ea-f3a7bf4dfc79 | -11.13664 | -53.94196 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac3fb692-1b71-31a3-8688-e1c61b3529c4 | -10.87815 | -54.75244 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 413f70ff-8e6e-36af-93b0-9d8ab05c47dc | -10.36684 | -57.23103 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 668f13d8-3d09-3e68-b66f-fac2e24de618 | -13.89789 | -54.65157 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 48a83838-2f73-3eef-9a06-58c5c405b3ab | -11.00573 | -50.75428 | 2025-06-12 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c8c3f5a-f5bb-3da3-8585-12fd6742ab13 | -13.47064 | -56.8589 | 2025-06-12 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e8b8f31-6fff-3cc4-9056-a4ce5ff523ed | -9.28791 | -56.23623 | 2025-06-12 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45735352-2d16-33ee-8a94-514577afbb19 | -11.37681 | -56.56036 | 2025-06-12 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d483abfa-5c37-354d-bfcd-fe93f42260f4 | -13.89183 | -54.64693 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bf7feecd-9216-3000-b159-5a9b960eb1f7 | -10.99385 | -50.76086 | 2025-06-12 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fd5e9fb-f321-35dd-a1cc-b4b34650fb9f | -10.33911 | -57.49022 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eafb43ef-dee6-32e3-82e6-5828b8a302bd | -10.70551 | -49.51765 | 2025-06-12 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdd2ce68-36a1-3f7d-aaf1-a2ebd15659bd | -10.87539 | -54.74829 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dc1fd8a-fbf8-3ace-86d0-80a8734cf942 | -13.97465 | -54.42435 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbd0bf97-9cca-33fd-8437-e35ed58933ca | -13.79723 | -54.30056 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b9e6565-c934-37c5-8861-3c85017f0096 | -12.6292 | -54.06242 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc35c825-dffb-37af-878b-2fc673f09cbd | -13.88795 | -54.64993 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f15661b-e7ec-3e60-9ae3-cf7c84ff8b45 | -10.69862 | -49.51185 | 2025-06-12 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8d8c5af-5bdb-3f21-bc23-43ed567d3dd2 | -10.36534 | -57.24002 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c5934ce-7e8c-32c0-9f54-2f12e28cd1b4 | -13.89627 | -54.64038 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f77d5341-441b-3248-b0ab-d005dadcfde8 | -12.79476 | -48.73167 | 2025-06-12 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ede58219-c5d8-30b3-a22f-b8417e5dc26c | -12.62809 | -54.06947 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0fc95ce6-06c0-357c-9ac7-e66a28c3efda | -13.88852 | -54.64638 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 55e37d49-d5c4-3523-bcb9-7669e24c45e7 | -10.64732 | -49.43743 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7640e270-243e-331f-bdc4-6038d677220b | -10.94481 | -55.31983 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 674c78f9-639a-3f16-9343-529fa4cbea58 | -10.66255 | -49.35745 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a0771b48-0603-3023-99ed-1ec95b71350a | -9.25036 | -57.53934 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1c0c3206-4a5a-33bd-bfe3-11629dfbd872 | -11.76728 | -54.37676 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b2b4edd-cd98-3026-9178-72bb2a158c87 | -15.3727 | -47.8759 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| aa224f69-a44e-30ed-a32d-e98cecc0261c | -10.86509 | -54.323 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1aebfeef-ce91-3c80-9ad0-2ef0a4273c2d | -11.58846 | -51.33226 | 2025-06-12 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7f96cb4-be4f-3fc4-8039-2e8141f40923 | -12.05539 | -48.07795 | 2025-06-12 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45fc47eb-a935-3856-aa2b-aad2c4c194ec | -12.21083 | -49.62997 | 2025-06-12 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c27a1a33-60e0-3a70-940e-5a1d9108b197 | -10.87789 | -54.30699 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ee4962c-d78d-351c-80d0-518dec4a9504 | -11.77173 | -54.37025 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a1143d6-7752-3b9e-8dd3-4268ef7d07c6 | -12.52001 | -57.22791 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58aeb164-fa9a-36af-b239-42793fabd570 | -10.94881 | -55.31672 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c8b0031-a9b3-3fbe-a614-6470d7de99ca | -12.52362 | -57.22855 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49a9eb69-ce6d-34e0-b30a-4d75fb90e186 | -11.43244 | -54.9987 | 2025-06-12 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7daccf3d-71c0-3978-a0fd-d18b74470968 | -10.9516 | -55.32097 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89853ae7-107e-3543-aea0-96b55a4493ec | -10.36313 | -57.23039 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57747f16-5f9b-32c3-8806-f0d2ca97e5d7 | -11.13553 | -53.94897 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README17.md)
