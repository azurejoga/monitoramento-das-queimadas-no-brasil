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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05e015e3-4a7e-327f-a3c9-9efeb0a07843 | -6.5435 | -60.00191 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb5af56d-8dd0-3673-b114-5833cb849ed1 | -6.54297 | -60.0057 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 318ac354-65f4-3ca9-9a8e-fa064d37f6a4 | -6.54244 | -60.00943 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dec3302-22b0-39c9-aaf1-bf574e602601 | -6.5419 | -60.01319 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 636a6006-1e6b-311a-b880-6874330ac5b1 | -6.54058 | -60.00211 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a646962e-21fe-3502-a429-0ec86d486ed3 | -6.54007 | -60.00587 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca17fc9f-1a03-321f-9661-73678231afcf | -6.53957 | -60.00965 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8bd47c3-a71f-3bd2-bebd-157d75954d43 | -6.53906 | -60.01344 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c9168c8-9810-3dc0-8660-3e37f94f06e9 | -6.53679 | -60.00854 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be2e6f43-2fa2-33f4-b66d-bfb644752603 | -6.53289 | -60.05936 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05de720b-86d3-3423-b828-5856e5d2df84 | -6.53239 | -60.06308 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 857e0643-5b1f-3b86-8229-58ecf370521d | -6.52976 | -60.05826 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8f5a75c-f364-3b20-9181-bce5429bb612 | -6.52924 | -60.06192 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ace08ba4-b33e-3f42-b225-54b5fa8a6ca3 | -6.52725 | -60.05863 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8630a5c1-c157-3f34-b72b-fc83c28ac635 | -6.52676 | -60.06224 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5e08ddd-d381-3821-a300-62812a861334 | -6.52414 | -60.05732 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d435b6c2-2b21-3788-8894-03516781c8f6 | -6.52363 | -60.06092 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e276247f-40a5-3c01-b2c1-d15ca07886fd | -6.52312 | -60.06455 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1587806b-8eab-36cb-8394-b5f4aba82aed | -6.52212 | -60.05399 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab447123-5642-370c-965d-a01f34a08ead | -6.52164 | -60.05761 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d254155b-7361-38e2-9f97-090c4ce22fec | -6.52116 | -60.06119 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b6392d16-eea9-3519-a332-e19d63ad26d0 | -6.51905 | -60.05268 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5201d345-cb4d-37e1-b2c8-3cce7604fb25 | -6.51853 | -60.05637 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9115062a-337d-304b-be24-61116429b62f | -6.51802 | -60.06 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| abadca07-20db-327d-83e7-7513de7f5824 | -6.5175 | -60.06367 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bf908e7-267b-3323-8eec-8571e4c81b23 | -6.51239 | -60.05912 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d2f109e-ab41-3bf3-91d9-7eb92e1cdc91 | -6.51186 | -60.06288 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65bdd972-1f3d-354a-bd1e-1272db8715fa | -7.05103 | -59.4143 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f9563d2-3a9d-3401-a757-b1e7232c66b6 | -7.05043 | -59.41858 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c24c943-eb3a-3ff1-af8c-f3f0c7216ba8 | -7.04984 | -59.42284 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 970c9295-f33f-3ab8-b5ed-5d0954404749 | -7.04915 | -59.41149 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43093506-ce17-33d7-bee4-ebcdc3a5f537 | -7.04859 | -59.41577 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3549a0c0-058e-3f08-8bdb-b4926b3bed17 | -7.04803 | -59.42005 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 243cd79b-3b26-3277-aa93-906a5039df69 | -7.04747 | -59.42429 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f36af72b-9601-348e-ae58-6aef79c4189b | -7.04688 | -59.40069 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f838f3e4-3b59-3cb0-bb56-57c3b81723ad | -7.0451 | -59.4135 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b8bace39-1e3b-3533-a267-6cdb1b6a8cd8 | -7.04451 | -59.41778 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8d5c87c9-4e7b-331e-bf96-e31ea0f988a0 | -7.04435 | -59.40211 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13b60fae-0faf-3991-b8b4-c4956348bb6d | -7.04392 | -59.42204 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83968ead-9da8-3751-9794-00eff7ca46c3 | -7.04333 | -59.42627 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7739d7e2-cb6e-344c-9f98-b254b8f68bdd | -7.04267 | -59.41492 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dfd1aefa-b09b-3808-a8d3-dc139c91357b | -7.04216 | -59.43473 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6c356bd-ea21-36e6-80b4-abd2fc635205 | -7.04211 | -59.41922 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc780e6d-724b-33f5-bcad-b1e52538f7de | -7.04155 | -59.42349 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c1e8a78-5a7c-3c38-b3c0-927005b408b1 | -7.04096 | -59.39982 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f193f408-0560-3fa5-8cf5-bbba1e839d17 | -7.04043 | -59.43196 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d029e82e-fd8a-3f64-8dd5-b870860dbac0 | -7.04036 | -59.40414 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d2096a3-3cff-36a7-91eb-53cbb830710d | -7.03988 | -59.43618 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 984601d0-aad4-32fd-b5c0-5e41f03e135f | -7.03919 | -59.41262 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d30684f6-b26a-3a84-9f52-7b921cbc5a8b | -7.03859 | -59.41693 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08cbd2b3-a6ab-3e49-b433-e90738f6a598 | -7.03843 | -59.40123 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0502f319-0f33-39e8-88e4-d35dea1b8201 | -7.03741 | -59.42549 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f47231c2-fc5a-35c7-89e7-2ed33555bbba | -7.03682 | -59.42972 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d2dd1c1-faf1-34ac-b920-17739806508d | -7.03676 | -59.41404 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65256fbd-d1cb-3e53-a019-4127e8c96b2d | -7.03624 | -59.43391 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb8888c9-03aa-3c6c-8994-6acae15541fc | -7.03619 | -59.41835 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 265c33ad-8c61-343a-912a-0d3889d46632 | -7.03563 | -59.42263 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5399a853-cc68-3365-9f18-2ddb23691cd3 | -7.03508 | -59.42688 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31bc7229-0e14-3a10-8adf-19e879659105 | -7.03452 | -59.43111 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e9ad7ec-2465-31d0-975e-37b21dedb5f1 | -7.03308 | -59.39602 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc32a728-3dbd-32f6-b19f-7cbff4704dca | -7.03268 | -59.41607 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fba7c12-6d6f-34a6-93f5-870d525ddf6f | -7.03209 | -59.42034 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b60ab93a-1311-3733-8330-ea87e3a3bcab | -7.03151 | -59.42456 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f5ba9db-e718-3913-bca9-2322d6ad27ed | -7.03092 | -59.42881 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 620ae52f-ce12-35bd-8ea1-c0251dd33d20 | -7.03033 | -59.43307 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dece7ddb-bdf1-393d-81e6-2bba35b795c7 | -7.03028 | -59.41745 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bedb7d15-a9c1-3879-aecc-6653a35e9d72 | -7.02973 | -59.4217 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 066cb66b-a2da-3ffa-9cda-96c6766fa9e5 | -7.02971 | -59.39384 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8df34b81-5e55-3832-a761-8d0ab156fa47 | -7.02917 | -59.42596 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac0e8956-ab2e-35a7-be20-f86b69160c11 | -7.02912 | -59.39811 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c530bc3c-19a3-3a7b-9d78-756e75538be0 | -7.02861 | -59.43023 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a762daa9-b2e1-39a0-9abf-676d27c0fe7d | -7.02618 | -59.41946 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66ee735b-22d9-3866-9035-2af4ba3382f1 | -7.02559 | -59.42374 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7328ea00-c689-3f81-9bdb-f378b5c08154 | -7.025 | -59.42803 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d262d004-a53c-3327-b155-c885693b34c7 | -6.97026 | -59.47677 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff4341d6-cf45-3753-bdfa-f531fdf6385f | -6.96438 | -59.47585 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2834277-4d0d-38d3-88f8-f6ebb6610196 | -6.91601 | -59.79174 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cbe5322-0e5e-3c63-889e-088351119db6 | -6.80905 | -59.14559 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fefc1a44-03d7-3fed-b2e2-b9e58113a121 | -6.80245 | -59.14922 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e1502de-b03b-3f84-a77d-923b1fb3aae8 | -6.7865 | -59.3125 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55dcba9f-7153-34dc-9f94-c4ffaf4572ac | -6.78591 | -59.31686 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4ba9506-48a1-374a-804e-4480fd514125 | -6.78531 | -59.32124 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ea9e0fd-3bf0-3cdb-9070-22b219c3d547 | -6.78113 | -59.30745 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72702e10-f2c3-391e-99e8-189b3d88706d | -6.78055 | -59.31175 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8c5cf409-1fd8-350c-a017-b19349b6d715 | -6.77995 | -59.31615 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 85915a40-93e0-3fc3-8a89-110b6e783745 | -6.77936 | -59.32058 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 19f49da8-6a7d-3ad8-8294-c3e557f5ba97 | -6.77877 | -59.32489 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8afeefee-81b3-3ed7-b3a6-a3b54d445876 | -6.7746 | -59.311 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6bd4c420-560c-3f66-8682-8a9e4d521e60 | -6.77401 | -59.31538 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 384556ce-1f53-3338-9099-03763aed984a | -6.77341 | -59.31979 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9324dfc5-fa7a-35ec-8bbd-0a5b4dd77eae | -6.77283 | -59.32409 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 474419f3-2c50-36f8-a438-0288a76f8513 | -6.76806 | -59.31461 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b5a17ca9-7b44-3fd9-ae95-f7d2edc80f49 | -6.76748 | -59.31896 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 526c1f99-73a0-392e-b361-1700338fa98b | -6.7669 | -59.32325 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d40edbdd-d732-3f4d-99ad-12400bf0b70e | -6.76634 | -59.32745 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3bddaeba-a0a4-3d7a-8608-4031ece5b7c3 | -6.76154 | -59.31815 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| daad04fa-f683-38bf-8a92-4f74e174dcf0 | -6.76097 | -59.32239 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c8f5df62-9cfd-3c2c-8161-3ea2d8f149cc | -6.76042 | -59.32655 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6d7aaf75-ed5e-31e1-a267-6eb737c8b0cd | -6.75839 | -59.32032 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d56eb66c-41cf-3c8a-8600-40932824ef2f | -6.7578 | -59.32449 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README143.md)
