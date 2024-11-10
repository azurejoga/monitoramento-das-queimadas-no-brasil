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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0d1f6c4-584f-3157-8518-ce7c41eddff6 | -8.41034 | -44.13782 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bb73322-ceb8-33a0-822f-ba87fe6ead62 | -3.02739 | -48.09186 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aebd6a8e-8705-3811-a53a-83f5a17ab2c2 | -3.86379 | -46.4486 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c8b33e2-34b1-354c-b0b8-a9ce39779e84 | -3.15252 | -54.48016 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e9960bb-323a-31f5-a9e2-3ec961da3d85 | -3.03711 | -50.35253 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3615bc11-c273-37fe-a1df-ae562a4f16e2 | -3.2528 | -48.7453 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3758503a-bdfd-32fc-bdba-eb2c9ee84709 | -4.88943 | -48.60233 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d347922-df70-3c03-80bb-c8456779153e | -8.39576 | -44.11965 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ceef28c2-cb45-3d8f-95c8-506fcf1a5b08 | -2.31877 | -53.87819 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3c5f39c3-14a9-316a-8197-80d584c0ad53 | -2.66467 | -49.90078 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d6f6e3c-e058-34ec-8383-bfa1b4a04141 | -5.53245 | -41.69531 | 2024-11-10 04:38:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4c24171-23b2-30be-a184-e1f49a00efae | -4.01453 | -48.29159 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad685d7c-3bf0-3ab4-833e-48649c944f53 | -8.3966 | -44.14365 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e7ff2ca-a036-3fee-b249-02069941f259 | -2.71757 | -51.99778 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a5cd29d6-d101-3114-a384-52f282b4b301 | -3.25989 | -46.28109 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb243690-b999-3c30-932f-1f9d64f7cc2c | -3.59238 | -42.85178 | 2024-11-10 04:38:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44d01df3-f36e-320b-9bca-b2cd577fa4db | -3.62098 | -48.91977 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a22a0ad-0373-3336-8e04-2e259f554d4d | -4.77239 | -48.91705 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cd79554-1ce7-3c49-87b4-38d0f2cf61ea | -3.79209 | -47.46638 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e506076-a043-3ad4-b5ab-62a892644e13 | -4.16321 | -48.24704 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 962bbfe9-9ae0-334b-ac57-5ae0d7f205ef | -2.94797 | -49.34756 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 484fc59a-05e3-3b50-a11c-4fc0a69c31a1 | -3.6138 | -48.92218 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c853120-a52b-3097-8693-074d7000ac49 | -4.21202 | -47.86806 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b831da15-94c0-3e17-9c73-18dd8d7f759a | -2.71388 | -51.99718 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c7b2609c-b45c-3447-918b-47eda4f0ff75 | -2.19084 | -50.82633 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fbf1e9bb-c972-3c1a-bd5b-29894fc09b20 | -2.1561 | -50.51593 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba8471a0-1111-380b-97e2-032714d07020 | -6.47999 | -47.50526 | 2024-11-10 04:38:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0c206a8-f7ca-3867-9fbc-157cf6075bc5 | -5.56865 | -47.78178 | 2024-11-10 04:38:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41ebb906-70c0-3c98-9625-6b1fa371fc89 | -2.95699 | -49.56441 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b90c022e-907b-31a6-a932-959fae754145 | -4.49205 | -45.69636 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a5cf943-c267-35ae-8498-030c77914de9 | -3.44318 | -50.434 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbd567a3-f8c4-3fc7-b557-606de87577e1 | -8.42104 | -44.12347 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dc204e7-92f9-3971-92ec-bb658f26a881 | -2.21515 | -50.44749 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b625cd4-4533-3bce-9a7e-74b7fa61d30e | -3.86658 | -51.97663 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7944323f-c8c9-3ac2-a0a3-0c945e2b078e | -3.34757 | -50.13585 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7cd583b4-1569-37e5-a034-2caba0540ddb | -3.62358 | -50.61718 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 877d0840-306c-3c2e-a1fa-ca20907bd2cd | -3.97206 | -48.1712 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82a0634b-6d66-369f-8bca-8b23551b310e | -2.67682 | -48.66243 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| adf566b2-ecb8-37c2-8f44-a5cd9492a0f6 | -2.88403 | -48.29198 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1237af6-1484-3661-b264-966d39aa054a | -3.10931 | -50.20686 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67508325-ad4e-3ddc-8b00-5b7f19503c64 | -3.41521 | -50.30211 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37ab0ca4-7071-3d9b-88dd-50a6caa36390 | -2.98547 | -49.53643 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63a06261-4e5d-35d9-9bd5-769f0e0482a3 | -2.8712 | -49.44309 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e0c35274-51c3-3667-8084-844d5bbdd053 | -2.32869 | -50.47977 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 874db60c-2223-34ae-842d-28db70bfa0b9 | -7.43202 | -39.7624 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a03cb3e2-0b0d-3c50-9169-f5a6f8e3b9f2 | -5.36799 | -48.245 | 2024-11-10 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 691f9f7b-44cf-345b-8fda-c77ee54be97f | -5.2895 | -46.22821 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3318405b-327b-390b-afd0-fb6df9aa305f | -3.98137 | -48.13349 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c80200ce-d1d0-3f45-ad90-88b9f9deb392 | -3.24398 | -51.23525 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccc4df45-2093-3711-9dea-bb9b1317eddc | -2.93693 | -51.05738 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b4a3a9f-0ec8-3d38-a75b-d4f23beba2a1 | -3.35641 | -49.50455 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34a7de23-e261-371b-91b1-73518cbd9515 | -3.95473 | -48.12929 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2df86486-1185-3c96-a0b8-9b9b98f879cd | -1.87378 | -54.17974 | 2024-11-10 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 45dfb628-395a-3dcc-b033-aed8725db165 | -3.81318 | -50.78753 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de2ac70b-e244-348d-af30-1981792701ad | -2.68106 | -51.94326 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9cc93798-2e1d-365a-90f2-c65785d44c0f | -4.7033 | -43.87052 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ff91c68-0c09-3e57-b873-98d424a2ddb1 | -2.8671 | -47.90678 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e775665c-f8fe-3735-a5e5-da999b03978f | -2.63365 | -49.19463 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f89ec0bf-0b72-3705-90a9-47ed761951de | -2.89013 | -49.38865 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a6a2339-28df-359d-98c0-730b4596eb90 | -2.4255 | -51.9615 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 08090b78-d13b-3d3a-97f0-ca0797d1a964 | -4.77957 | -48.91463 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84caed9c-d5a9-3718-8efc-3b2b02c6b58e | -3.38462 | -51.46516 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0107d571-06c4-3969-af2d-297486324c2c | -3.28386 | -50.22977 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea3f3243-1d7c-3564-8e3b-fedbbe841e3e | -2.84311 | -49.4353 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ce89ff3-f794-3ae2-a182-a8c122975117 | -2.65569 | -49.4021 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1fb71efa-bcb4-3fba-a9d8-4a8c28f89e0c | -3.24375 | -49.57701 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15407eac-7ba4-3a86-b068-ef6031761d67 | -4.38015 | -48.17786 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d461310d-330c-356b-80c1-17bed7c7fb46 | -3.08112 | -50.42762 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d151476-686a-341a-a655-df6d298d185f | -3.10421 | -53.32935 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9ab018cb-6588-3742-9447-1503cabace94 | -4.05767 | -49.28619 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff5705c4-cae0-34af-bde2-c4461fc16375 | -2.64689 | -51.88244 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df745d67-e076-3e9d-b93f-a376fb8a41a3 | -3.15322 | -45.94292 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e69822e-7810-3520-a5a3-c5415bc14bdf | -2.92573 | -49.3584 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc881084-ec8d-38e6-949a-de705f2c07d6 | -2.20864 | -50.78156 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ce15c423-3292-3e14-a2a1-a4b7a86af97e | -4.2161 | -45.45425 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10e6c8df-440c-33d0-99f7-f139f6ef6c69 | -2.57163 | -48.45198 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3472206-0bd3-3e96-9ba3-52d845df72c6 | -4.21649 | -45.93938 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 800055e9-b83d-35c7-a413-e88107c446ef | -5.31095 | -46.23128 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29f4f707-8fc6-3492-88ca-b509d672147d | -2.91787 | -51.68045 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 444f4bba-9079-31d9-9081-cadf45f86327 | -2.96019 | -48.02406 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cded15ff-6e5a-355b-8271-c2de699f920a | -2.66185 | -49.89666 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78e285ae-9d98-324c-95c1-5dc0ba73980d | -2.4282 | -50.49117 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f69bfbd3-0140-3442-bbfe-0b224c500add | -4.29695 | -48.64446 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b65ce9b0-b4d0-3cbf-a2b1-2791468f8de3 | -3.44244 | -50.30637 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82bc0b91-9231-3573-b89c-680739349982 | -3.44924 | -50.30745 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43c9b869-f64f-3818-90fc-10dbff4ea3d6 | -2.15536 | -50.5113 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51f5cfeb-be5f-3509-8484-5dc6a929fbda | -4.92907 | -48.52327 | 2024-11-10 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29188b84-d354-3eb4-a657-0ed41ca61f0a | -2.80463 | -52.54177 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dab78b9e-39a6-3d50-8d74-4cd16e34e99f | -8.40053 | -44.11639 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8db53c08-c579-31cc-b7d7-aec04be23685 | -2.63538 | -49.88882 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| faf903b7-4762-3ad2-b566-9eeb9e5f0fed | -7.44171 | -46.63234 | 2024-11-10 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e067dfcf-a449-3547-987a-8813698cc1aa | -2.87056 | -50.32332 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec5f83e3-34bb-3f43-b592-a85677b204bb | -2.39414 | -49.84783 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1da2bc55-c18b-30ad-bfea-72e99e5ebd22 | -3.86953 | -51.98141 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc102a2b-c4b2-3e00-a49d-ed77f902555f | -3.95321 | -49.00405 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2819764f-de10-3c6a-bd91-bfae9a2f84b2 | -2.45452 | -50.39199 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 279fd5d8-d493-311f-a8cd-5f252a772146 | -4.02227 | -48.28569 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6af6ba9-317a-37c1-91a1-0b1f09e25c54 | -3.6188 | -48.93357 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89cf8852-849e-35f3-9178-634022894454 | -2.60181 | -48.19538 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 005a5048-5258-3730-ac4c-3e198ea7853d | -2.03287 | -52.05255 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README96.md)
