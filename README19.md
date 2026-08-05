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
| 1c99f69b-b5a2-3761-afbb-5cc57ba8c049 | -21.26348 | -48.73839 | 2026-08-05 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7263edf7-9c69-3aa4-9d26-b36023339439 | -18.38516 | -51.45338 | 2026-08-05 04:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c60a18b0-0547-33d7-92c3-0c36b3421f61 | -19.38954 | -44.32684 | 2026-08-05 04:51:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eb60ad9-8aa1-31a3-a920-8e2ed529431d | -21.03787 | -48.46325 | 2026-08-05 04:51:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5acacc3-5aea-30cd-b722-918e54050fb7 | -20.04053 | -47.16372 | 2026-08-05 04:51:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 046fa814-584a-3334-ad32-8c8e4810c63a | -20.90576 | -44.08409 | 2026-08-05 04:51:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 31f38184-4a2e-3acd-a98e-ac6ca729653a | -18.84748 | -47.9191 | 2026-08-05 04:51:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 53c39271-64c3-3c72-9029-0f28684c3cb7 | -19.16164 | -47.31824 | 2026-08-05 04:51:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb5e5594-aea9-36d4-a8fb-21cee718c97c | -23.14301 | -48.67181 | 2026-08-05 04:51:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0da18821-4737-3b0e-af17-c8e462add7e3 | -23.19444 | -49.15343 | 2026-08-05 04:51:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c1456f1-f9d4-3eb7-9aa6-4a6e77a4effb | -17.7069 | -53.27158 | 2026-08-05 04:51:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9b6cc7b6-a8d3-30f6-aa00-5b7b3f75dda5 | -21.70527 | -47.16872 | 2026-08-05 04:51:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ba21d7a5-3ee8-3930-89b1-5106a41cbe3f | -21.67546 | -47.82802 | 2026-08-05 04:51:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e891ec0-982e-3b8c-a7e5-37e5d6492789 | -21.67663 | -47.82674 | 2026-08-05 04:51:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a50791f5-2042-3f50-a278-eaa9aef7691d | -18.56568 | -46.2501 | 2026-08-05 04:51:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b2eb901-3989-3428-bab9-f396ff210cba | -19.7932 | -46.04288 | 2026-08-05 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fa4667d-4890-323d-b213-414052933862 | -21.29743 | -49.04725 | 2026-08-05 04:51:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 27e4154a-c2f0-3b76-becd-b888ff7bb24d | -11.1828 | -54.9194 | 2026-08-05 05:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| fea5462f-bacf-3e96-be77-f36e64168dcd | -12.5947 | -46.9301 | 2026-08-05 05:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 5676aa18-40d7-310f-a8f3-430c334b97b1 | -11.1642 | -54.9007 | 2026-08-05 05:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2886fd95-491d-3365-a411-5958b2a4812f | -11.183 | -54.8991 | 2026-08-05 05:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| d22786e2-387f-3a88-b9d5-e8f0c5268490 | -11.2019 | -54.8974 | 2026-08-05 05:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 5f952857-b984-3061-aee0-9ea6587bdff7 | -11.2019 | -54.8974 | 2026-08-05 05:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 8b524173-8184-3ec1-a9d7-fa1ce249690c | -11.1828 | -54.9194 | 2026-08-05 05:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 47fbd524-3f3a-3afa-b06a-210510df7329 | -11.1642 | -54.9007 | 2026-08-05 05:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e55e484a-e3ba-3c07-b129-3a0430ccd93a | -12.5942 | -46.9527 | 2026-08-05 05:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 871d79cd-1e38-3ae1-bc19-d379fa625223 | -11.183 | -54.8991 | 2026-08-05 05:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 606f33fd-7f5a-3d2e-b4ee-dbbbc7e160e0 | -11.183 | -54.8991 | 2026-08-05 05:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 6d080058-af36-38a1-b9fe-c97dfe6ad3cd | -11.1828 | -54.9194 | 2026-08-05 05:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| bbb1bcfb-dc98-36d0-b23e-1367202b6542 | -11.2019 | -54.8974 | 2026-08-05 05:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| bc30a4a3-05cd-3cc5-96b2-882cf82fbdcd | -11.1642 | -54.9007 | 2026-08-05 05:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0d35f790-2022-3584-86aa-918341a47fa3 | -2.95433 | -50.31881 | 2026-08-05 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8ffeae8-68b9-3c54-a608-f6432a373492 | -1.80523 | -54.47776 | 2026-08-05 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0defdc36-7704-348d-b9a3-8373c69ee58a | -3.03149 | -48.41433 | 2026-08-05 05:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db3bd7a8-04b2-3921-a372-f34ef725ac4c | -2.86905 | -50.47121 | 2026-08-05 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 975917fe-0ea3-340a-a655-cf5c730922a1 | -2.46439 | -54.67594 | 2026-08-05 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2412667c-f7c3-38cc-98aa-67cabbb5f706 | -3.16977 | -48.13687 | 2026-08-05 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dbb4e6e-7f77-395b-9352-fcc88d0dfa2d | -3.65568 | -49.18961 | 2026-08-05 05:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f5a8771-4a31-3390-b4c2-3cad77b1a2b9 | -3.69215 | -47.64197 | 2026-08-05 05:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7ea8506-0ddc-3491-ab65-e89f8d69d2dd | -2.89231 | -48.02241 | 2026-08-05 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 89b1d729-5827-3fe9-a537-a53b53b7b129 | -4.36546 | -47.76479 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb7d7adc-7c12-31de-be0f-9cebee1d2e6a | -4.46429 | -47.9194 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef9e21fd-9552-3ff4-bef2-dae5b07ceafa | -3.91529 | -49.40659 | 2026-08-05 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7d36ca4-09f2-3f53-9226-81b39f5913c7 | -2.94476 | -50.32187 | 2026-08-05 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36f605ba-180e-36ed-803d-297405476149 | -2.81731 | -52.29184 | 2026-08-05 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 136dd8e6-3724-3c0a-9a0d-2bd47d5d65e6 | -4.36973 | -47.76662 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2372e2bf-4654-3944-975f-5eb63a34303f | -3.67336 | -49.46553 | 2026-08-05 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4549fba-822b-31e5-b60b-2da55dd2de1d | -3.24403 | -47.92756 | 2026-08-05 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5374dade-92a4-3acd-a0fb-63079e265dda | -2.51981 | -57.73814 | 2026-08-05 05:21:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af1db948-0506-3c69-a690-b9b3a4ce43d3 | -3.18652 | -52.88574 | 2026-08-05 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03e3aa72-e2b9-3637-a682-41c7d1a71829 | -4.29172 | -48.35517 | 2026-08-05 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b24279b4-607a-3246-8511-916c1b2bf95a | -3.19099 | -52.88177 | 2026-08-05 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 457affab-aebe-3248-ac20-17c1abff1595 | -2.96304 | -50.35141 | 2026-08-05 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 609a3038-7dbb-333c-9f1d-616dc94aad88 | -4.29235 | -48.35163 | 2026-08-05 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f324764a-6cd5-3603-9831-f4209e014dfb | -2.96682 | -50.35646 | 2026-08-05 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c812389-0ea6-3f4c-81a8-a5d9af11a5c4 | -2.31317 | -48.5802 | 2026-08-05 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 013bb59f-8c0d-32bf-827c-bbc8a0e92f24 | -2.31241 | -48.58525 | 2026-08-05 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11c603e1-e7d1-34b7-a6cc-07a09578c582 | -4.46161 | -47.91763 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f78501a-f1d8-3352-80ac-8f312e14ffd5 | -3.6678 | -49.46995 | 2026-08-05 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8adfaf42-95c8-3ff6-89b1-780c59ea8597 | -4.46113 | -47.92101 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 740ecec1-28cd-332f-a7de-3e6a9855e270 | -3.66702 | -49.47507 | 2026-08-05 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3319026c-2606-3452-89ad-8bf2eee15ef3 | -3.16931 | -48.13992 | 2026-08-05 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f26fa238-e996-317c-b217-0a7a21b430b7 | -2.91487 | -54.16542 | 2026-08-05 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff56ad71-8b93-3e7a-a303-33b2f8637a32 | -4.45942 | -47.91523 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 441a9e67-d74a-3310-a65f-435b23efbec4 | -3.58419 | -50.26507 | 2026-08-05 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2621740-202f-3620-95ca-98ec21d88c5e | -3.24977 | -47.92532 | 2026-08-05 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03b4f3c3-e76a-3e94-9406-a273b8e7207a | -1.94514 | -54.07057 | 2026-08-05 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5f8c76b-f589-3c36-b35a-606a0777155f | -2.31328 | -48.5797 | 2026-08-05 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc284d32-6e21-3abd-9cf7-0bf675331f3a | -3.18721 | -52.8812 | 2026-08-05 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 456fa23d-0c62-33f9-8fe2-8316fbf7be23 | -3.66858 | -49.46482 | 2026-08-05 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 725baad6-74f8-3b92-a68c-cbfc3432c1af | -3.03194 | -48.41133 | 2026-08-05 05:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51353769-ae9a-3704-816a-988338736273 | -2.94921 | -50.32253 | 2026-08-05 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 105d716b-8382-3bd1-a354-25989d26b348 | -2.89279 | -48.01926 | 2026-08-05 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5752a13c-973f-3dd5-917a-f78540aade00 | -4.36431 | -47.76574 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7592f284-cfe7-3f17-a49c-90e5c51b9d09 | -4.28665 | -48.35424 | 2026-08-05 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a9baf9d-f68e-3b6c-ba7e-9221c3ba27d8 | -4.28648 | -48.35456 | 2026-08-05 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f9536a7-0455-3e32-8d96-be93cce20e6e | -3.24926 | -47.92863 | 2026-08-05 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43f1a745-1e90-3cac-9297-88a56f7fe356 | -3.1903 | -52.88631 | 2026-08-05 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 537a9e37-fcc1-39cb-afc3-65f8f1f6ed3c | -3.69264 | -47.63865 | 2026-08-05 05:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef964bf9-746b-37d3-a585-4ae1f590108b | -3.91688 | -49.40566 | 2026-08-05 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30860750-3112-33b2-b858-c8345148afc1 | -4.29221 | -48.35195 | 2026-08-05 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3596a98a-c81e-3026-b5c8-b442eb2ea11c | -4.36922 | -47.76999 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 819b9c87-957c-3244-b634-2aba85629fab | -3.99733 | -48.396 | 2026-08-05 05:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d06b99-7ad7-3367-9771-5d9d8d451d8d | -4.28022 | -48.03603 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0c07c49-4a4f-3b5e-b5ac-d249a8696ee6 | -2.95367 | -50.32319 | 2026-08-05 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f468de0-21e7-3ec3-9032-653bbd424824 | -3.33012 | -54.67473 | 2026-08-05 05:21:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4793748f-4cee-3b8d-be5e-ecfbb92ff64f | -4.36498 | -47.76818 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66e99747-310f-3110-96ab-59bfaa2da70e | -2.31235 | -48.58577 | 2026-08-05 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7919800-23a9-3be4-b5b2-253a29e3b17c | -4.36871 | -47.77343 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 124a4b9b-3bc1-3da6-b3c9-29f2204b8ba3 | -2.87346 | -50.47184 | 2026-08-05 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0d8e960-3d81-3d3d-8479-9abbd14e506a | -4.36991 | -47.77248 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd09a229-ed2f-36a4-b468-a40669956387 | -4.45891 | -47.9186 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c0663f4-3a69-3480-9fc8-6e7d1c21ce7f | -2.87282 | -50.47598 | 2026-08-05 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e71af5ae-1f52-33e9-bdb9-e33f023b70f8 | -4.3704 | -47.76906 | 2026-08-05 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 400b38ea-03b1-3364-a6c0-bbc7bcd0d823 | -6.54907 | -55.16144 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11372d11-fa5e-331b-87d2-633466ebb1ce | -6.5287 | -55.15422 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7926c94b-35f7-3e53-970e-f4a895b44972 | -6.53628 | -55.15145 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b21e40b-3b58-3059-83ea-c5cfa4611db9 | -11.199 | -54.90908 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a207bf0-2ea1-3499-8ef2-3711b18080a6 | -11.17671 | -54.87836 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e92a5089-7d2d-357e-a99e-e3f2ec6db8f6 | -14.16985 | -54.40481 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README20.md)
