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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3384bfa2-8357-3039-92c0-c82c8b39a340 | -10.94471 | -49.58773 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73873f9f-4134-3dc8-ab8a-3e53841841db | -13.74971 | -52.01628 | 2026-08-28 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42103f13-9425-3c5e-a982-a90a38b8aec0 | -12.37515 | -43.44439 | 2026-08-28 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46fd8375-e500-3368-8810-44dc8c621c49 | -14.15517 | -52.82954 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 738cc25e-d857-393f-b1f4-128fa7a39589 | -12.7624 | -44.26199 | 2026-08-28 04:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b24bf83f-4037-30e6-8539-5e3b9eb80d60 | -11.20725 | -51.24428 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d71ff231-7b8d-3eb8-87fb-ec091200e2b0 | -11.72696 | -54.54148 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6095bf00-2016-39bd-af4d-d2e4003467cd | -9.98655 | -48.58931 | 2026-08-28 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9a06eaee-98ee-3c40-9938-041cff5f06d7 | -13.41267 | -51.41812 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76dcce0b-1264-35d0-a3c2-f2a7303075e9 | -7.37895 | -55.15217 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| badb591b-3979-3abb-978d-e99056d3bec7 | -11.37565 | -45.15037 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05078921-4850-3b96-aef7-a6e211e75500 | -8.76774 | -50.4944 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 277ccca5-efc0-3eb6-9629-b64ba579a868 | -9.0612 | -45.78104 | 2026-08-28 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fce22a93-8080-3ed1-a0c9-c0c2eb163dbe | -8.78836 | -50.07135 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d94f7538-a794-3f9e-b047-23dd6c77fe27 | -11.81289 | -47.21005 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20306d2b-e7c3-367d-b34e-4a5fc6a7c8f1 | -12.26445 | -50.57315 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 9a357799-87d1-3451-851c-105d60fa9c05 | -8.62001 | -50.01946 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f96e66b-14be-3234-8e64-8bc0f110a54e | -10.06055 | -46.93643 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a9b1b00-7433-3668-b98e-4e68d3d6026b | -8.78112 | -49.94505 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32a6dc16-0040-3a2f-8c06-6f28ba52b380 | -10.96496 | -50.29496 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3f4a477-e8e9-331f-937a-213a5ce47119 | -11.49709 | -45.11329 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf1015a8-142c-311a-8626-4e9b828a3d15 | -10.06297 | -46.94572 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 511b0e79-85fa-3e20-8cad-62afc33674f3 | -13.41153 | -51.42522 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 154277a9-7458-365b-a4cc-cabb11f880d5 | -8.93963 | -50.77353 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53d13a60-7435-3b46-a3ea-4917d4943876 | -11.28828 | -54.02327 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 459ba4c3-a752-3f02-8e80-cdb12f7f614b | -11.22921 | -53.99522 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b68bb3cf-31bc-3c4e-a707-4c72cc5e89e8 | -13.45669 | -54.01843 | 2026-08-28 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cef0a0e0-0ee1-3ffe-bf4d-451fed6eee25 | -9.21353 | -51.56047 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3afc1a1-7b53-3e12-91d5-a85d53213090 | -14.61038 | -47.98211 | 2026-08-28 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9a0daca-3b30-33fb-bdfd-19bbe5861a1f | -8.11634 | -51.66906 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1f28502-94a2-3a09-909b-00a7a777004e | -9.43359 | -51.69242 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 104cc38f-dbc1-3b21-a134-fa2c8c09a762 | -10.7623 | -54.04286 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 141ff28e-cc20-3cd8-9d6d-f6abd01a0920 | -8.77669 | -49.95149 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00f8db6b-1f67-3c55-867a-a3140cbc7465 | -10.75784 | -53.9794 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4f89972-7327-37c2-b02b-45cc28f3ac44 | -10.76078 | -53.98435 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25ebc7a5-679e-379f-8cf0-fb989bd392fc | -11.01874 | -49.65416 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7d8a4c7-04b3-3653-bebf-a93f43dee3cd | -14.87836 | -52.59656 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b738a0a-a8e9-3125-9eb2-88109e387b95 | -14.92142 | -52.61475 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 615074b6-f8bf-3349-b338-fe44344c769e | -10.26548 | -64.50448 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6072f6ba-167e-337d-a869-f9c5f0241c26 | -10.96829 | -50.2955 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b153fdf-468e-3678-b881-a588afec5807 | -11.72463 | -54.55505 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a1a9bb9-4ef0-3be8-80d4-66cbb9e31341 | -12.91389 | -59.89288 | 2026-08-28 04:51:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5df7e1f1-00ba-366f-a8a6-609983161ea7 | -10.76296 | -53.97137 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e50a56f-128d-3185-ad6a-3e6709336bcc | -8.94404 | -62.4106 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 552f9ed9-3a3c-311a-907d-4489a900b625 | -9.86465 | -60.26636 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b68152ef-ff8f-341b-bf95-d94f721e8bcb | -11.24486 | -45.04554 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9cb18d2d-7f66-3fc2-8d66-151d584140c7 | -14.87895 | -52.59288 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f3e7a48-5a7d-36b8-848e-1624e50b93f4 | -9.98541 | -48.59673 | 2026-08-28 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9a82cfd3-dce3-3936-9257-8966c85b30de | -8.80212 | -50.49277 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec362fd8-3dd3-326a-886e-011d9c64b568 | -10.75568 | -54.03723 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 858bfd1e-01e8-3cf7-8159-712ec2548ea0 | -13.42753 | -54.01753 | 2026-08-28 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10d55f95-ed50-3d2f-a04b-34bb84fd24f3 | -9.46741 | -51.69812 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8efa918-cca1-3d8b-a4da-78d02843058b | -10.78408 | -53.99528 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dc7e517-cd61-3c39-a48a-dbe92ba54c20 | -12.91328 | -59.89603 | 2026-08-28 04:51:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6e046ac-9199-30a5-8a34-1b920fd55ed9 | -9.98598 | -48.59302 | 2026-08-28 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1cc0e3b5-5cc9-3433-96a3-42e928b0e00b | -11.28681 | -54.03195 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6ac2c528-d7fe-30fe-a0b6-b107e84d4a36 | -14.11836 | -44.38457 | 2026-08-28 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99398d70-e833-3341-acff-11314d229a7f | -11.23211 | -54.00019 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d68c777-c324-303f-92a6-ec3ff1368af2 | -12.26888 | -50.58838 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5254cad-c2c6-3e8f-ba28-15fb3c51839d | -12.78761 | -46.45142 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34ae9bca-ecf2-334f-bf64-4c747551b49e | -10.78992 | -54.00518 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ee6100c-f7fe-370a-a2a0-802098065bc5 | -11.72773 | -54.53696 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 833c48cd-16e9-3fb7-94fa-1f01d3d72501 | -9.40418 | -51.63571 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36eca5ba-70a4-3bf9-b459-41a53bff16aa | -7.63784 | -55.07577 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b49bdbd-e761-323f-94d3-36a5f19e3752 | -8.95024 | -50.17996 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a815ac5-27d3-3f22-ac4b-63891cdcc565 | -10.39107 | -61.23491 | 2026-08-28 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b398aefb-f1ab-366d-a090-dce4b142d416 | -12.01631 | -47.1633 | 2026-08-28 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8233bfe-d44b-376f-8097-66b50e9f30ed | -14.42387 | -52.59843 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d65b9f70-481a-3427-bc1f-0d64825a8d90 | -9.97551 | -53.94104 | 2026-08-28 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4de3b3b6-2525-3806-85e3-169099ac1252 | -11.72555 | -54.52727 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04bf6285-6e99-3251-864f-827428949985 | -9.22249 | -51.56939 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9baaaa0a-a9aa-33e0-9493-3e639762e08e | -12.23007 | -50.5748 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42e1bab2-9275-3cdd-ae78-b67044f8d135 | -9.15912 | -49.97347 | 2026-08-28 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc23db37-c2bc-354d-9ed7-e23a8f433668 | -8.99518 | -52.38974 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82165fd3-0e6b-313e-a312-25543e7cdab5 | -11.51545 | -58.50879 | 2026-08-28 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fdfd27b-b1b9-3b74-be7a-52fec6780898 | -8.11574 | -51.67276 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 975f05bf-b27f-3b03-8451-bbd056ca6b9d | -11.76585 | -54.51595 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a8a96c9-0a21-3164-9b5d-7cc160087b34 | -8.59871 | -54.79117 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a05482f3-7a20-3cf6-b104-cb6b55d74682 | -8.60793 | -54.71477 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e6cb275-81ec-32a1-812a-a33070bd2beb | -6.84114 | -55.61079 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16943bee-f81d-3783-be72-3670dc919a44 | -8.24158 | -54.97509 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86372694-92e0-3fa9-889b-a8e0683532c8 | -10.92448 | -50.52988 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21f8fe39-edf4-38b5-a2ca-04d2a619a54f | -8.95357 | -50.1805 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 137f3b4d-d02d-3f3a-837a-42778e083fac | -12.07276 | -47.16714 | 2026-08-28 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e5522e9-f04e-3b6c-b48d-e931e3e71dd2 | -10.79141 | -53.99653 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cbd3830-5101-3c9d-b5ae-3beb4d92440c | -9.8791 | -60.26939 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63f8dc8c-f05e-3ad3-960e-e13b53f5dcfa | -11.17124 | -51.21292 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35baf47d-0b58-3cf1-8251-0078afd6afd8 | -10.76081 | -54.02917 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f871ecf-d2b1-35c0-9e97-fd15a5d82c9b | -11.27294 | -54.02508 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a8b3199-53df-37db-96cf-2339e1523436 | -9.46046 | -51.71944 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 598d01a8-a29f-3337-8b44-569e9fc7d68a | -14.45329 | -53.35189 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27cc0a81-240d-326e-a7c2-90042b517075 | -10.78766 | -54.01828 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b407f27-3906-3aaf-a419-7813cf9fc684 | -12.27774 | -50.59707 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dcc75df-4f16-3040-86a8-3e40386fea30 | -6.8342 | -55.61536 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3bf232a-ad43-31ff-93bd-1930c9218d8a | -9.07656 | -53.03973 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1b3119e-6b92-302f-a0d1-4a093f50e257 | -8.02827 | -51.82153 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c6ecbac-7952-3c3a-99c5-017f5fbf11e8 | -10.9433 | -50.54013 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c5354371-31eb-3435-bc6b-efd049f2b6b8 | -15.53106 | -41.92528 | 2026-08-28 04:51:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 41a77e82-ead4-34b1-b832-e6a1b2bb8aa2 | -11.79769 | -47.66869 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ca5f8e5-8e42-31c4-85c1-3cfa007d88df | -12.77585 | -46.44986 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README39.md)
