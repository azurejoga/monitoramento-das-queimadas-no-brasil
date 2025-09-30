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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79eb5dd9-af43-3dd8-8fc7-f776e01d1393 | -13.73131 | -48.64771 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6787633-134b-3849-b713-9a78719d2f18 | -13.61819 | -48.0267 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5a7e0bf0-dc7e-393f-859e-e86c55db8987 | -10.20001 | -44.88256 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c619e61e-6b65-35b1-95a2-5b9e15a7ede2 | -9.4242 | -54.72305 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 665c8f3c-7691-3044-8321-77b9622ff8c1 | -10.1917 | -44.89623 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 433.1 |
| b946cbef-a7f6-389c-9c22-f5b6ccb0fc0f | -11.74807 | -44.75086 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f83b01cd-f199-3b0c-a990-14d4f9305930 | -12.02349 | -49.71749 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5cec4683-3898-3640-9c25-5e2f8e092fc1 | -11.06598 | -47.82394 | 2025-09-30 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| f5f13d2f-b763-3002-a752-dca0294a4a10 | -7.75946 | -45.77377 | 2025-09-30 00:33:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b85680c4-82f1-333f-bfc7-fb83b348969c | -15.06837 | -45.0699 | 2025-09-30 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4da308fa-91ab-3a99-9543-215bf800d99b | -12.84193 | -47.00772 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 3a9f2ca8-1374-3579-a1d2-743c158e0618 | -11.8926 | -49.90738 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5498a13c-1d5c-33a8-81f1-f7ecde67788a | -14.08691 | -44.08526 | 2025-09-30 00:33:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e610d380-2fd9-3db8-8217-12cd70ffb725 | -14.7062 | -48.23207 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 92220a06-5a1f-3d0a-a5af-fe17951146a0 | -14.72371 | -45.23386 | 2025-09-30 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 3c964533-3871-3f84-8435-3b647454f042 | -13.45544 | -51.69404 | 2025-09-30 00:33:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 3a09bbb3-7229-3150-a7b7-636f0f6f7e26 | -11.89724 | -48.03062 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cf922466-5ad2-36e5-8647-538ca8e389f0 | -11.37468 | -45.05867 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 811a766c-f53d-3aec-816c-d51a2c4ed6a7 | -15.48731 | -48.56725 | 2025-09-30 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f4c39a70-0bfd-38d9-ad2b-68db01836839 | -13.6194 | -48.03564 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4ada09e1-1884-30ac-9d1b-813b27e54069 | -14.01001 | -49.63562 | 2025-09-30 00:33:00 | TERRA_M-M | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3388a6d6-124b-36bf-aee2-98a7c1be7258 | -8.71891 | -47.98734 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 391c9cb8-58d7-3edf-a945-12897183d3cb | -14.24954 | -54.76592 | 2025-09-30 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 0dfd250d-93bb-3936-8289-931d0be64033 | -16.06583 | -51.04338 | 2025-09-30 00:33:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8e11cc72-838b-36cd-ac7f-fa5f29f30b1f | -11.16431 | -54.12696 | 2025-09-30 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 165.7 |
| 14ec7b0f-0455-3b87-963c-ab04e4e9428f | -14.56236 | -48.46372 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 1a4f2047-8ad7-3790-9d9a-7149993e845d | -13.63249 | -42.53741 | 2025-09-30 00:33:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 52ff54fe-963a-3ec6-93ff-64646a048756 | -10.70324 | -46.75954 | 2025-09-30 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b8aae308-826c-3c29-bf13-79a36f40274b | -14.51901 | -48.00983 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7570bf7a-0118-3b42-af7c-dd8aa89326ba | -14.6417 | -46.96329 | 2025-09-30 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5d6cb086-55f7-3dea-8f33-3a1c71870c52 | -10.53289 | -43.6417 | 2025-09-30 00:33:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f14c4894-10a0-3c74-bdae-7514071e4d91 | -11.75629 | -44.73756 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 198.2 |
| 4ad8d232-6eba-3a14-a7c3-576007b36f7e | -12.3789 | -43.89796 | 2025-09-30 00:33:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| dd340d3f-0dbf-3ef6-b82f-ee6b3da6c0a9 | -8.90145 | -50.58751 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1f6e2c1a-baf5-3fae-add8-e9ddba615983 | -11.72144 | -44.44445 | 2025-09-30 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 2bfdf2a4-09a7-329e-b088-628dc09f49e0 | -10.6296 | -53.69391 | 2025-09-30 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| a338d4e8-37c3-31a1-b3d3-5cd81d0b9e2d | -11.64699 | -47.494 | 2025-09-30 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 561fac7e-3cbd-3154-9310-a5d6fe60efb0 | -13.37867 | -48.08337 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6502fd61-92c0-3607-830a-6da85942e902 | -9.37897 | -48.95304 | 2025-09-30 00:33:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cab84629-f2a3-34d3-b1be-e55c14a83cfd | -13.99937 | -49.62681 | 2025-09-30 00:33:00 | TERRA_M-M | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f87b5402-f163-306d-add8-175ee45158b0 | -11.75803 | -44.74929 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 3ffcfb54-2f93-3916-966d-9c79b056e051 | -13.58534 | -48.04992 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ee0b034e-e56d-3ec1-bb62-82e8c034004b | -15.62024 | -47.8488 | 2025-09-30 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 72c6374e-7a9b-3a1a-b6c3-f283b01d5d2b | -13.36453 | -47.31538 | 2025-09-30 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 35f41516-55b2-3e40-bffb-51b06fb5ef2f | -15.04855 | -46.96426 | 2025-09-30 00:33:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f2a13194-e775-302a-826f-2b03fd1896b2 | -13.8218 | -47.49918 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5f338bc7-4202-3402-b1ca-67b925809871 | -13.57777 | -48.06033 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 270374ff-327c-3ef1-82ec-364c9da1b560 | -8.54605 | -44.65819 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0d48cff4-32a3-3a1e-8c6e-38a5c78e92c8 | -14.25957 | -52.96445 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| aaf1806e-a457-3154-ba24-5e0a2c0700db | -12.85168 | -46.88503 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d36651a5-88d6-356e-b9dc-10f43ca75ca0 | -14.5368 | -48.47694 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 2d1a3187-7965-3a0a-baa6-947342b43916 | -13.66434 | -44.40289 | 2025-09-30 00:33:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 2f2a2f5c-5dbd-3cbc-b5eb-3ca28c8d362d | -14.57424 | -48.28255 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 65216ae2-f78b-3037-91a0-3e7ea10cac2a | -14.23973 | -49.79398 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2c695dd3-f2f4-3ce5-89dc-5ada2e876b8c | -10.63063 | -48.54276 | 2025-09-30 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2195ebd5-39e5-333a-abb7-3949a45c01f3 | -8.24569 | -45.52311 | 2025-09-30 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| bc7f2fa1-a435-3162-989d-c5cb195f4d4e | -15.2534 | -48.74551 | 2025-09-30 00:33:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| bd1f3b51-e178-35f4-b802-07b9a74d4244 | -8.98656 | -47.52619 | 2025-09-30 00:33:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 40a622a7-9301-3c4a-81e1-0a55f784b624 | -10.32012 | -50.53915 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a45aae43-edbf-3754-a5ff-7a87e3ee2a99 | -12.88811 | -46.757 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d4714a08-135c-3e6e-a22a-ae2bd3e8b935 | -12.75836 | -46.87665 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f25bf5c5-dd9d-34e4-a082-ca95a200fde2 | -15.46867 | -47.94305 | 2025-09-30 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 77ee03db-5cc2-3871-ab7d-798ac5a95126 | -15.03103 | -46.98204 | 2025-09-30 00:33:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b492fd9c-f5cc-3347-a878-f130011114b2 | -13.84328 | -47.50849 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8e86743e-6473-383f-87ff-47b54e24f664 | -7.85171 | -47.26273 | 2025-09-30 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6da3a87c-3872-3010-979b-9e06f5a61e97 | -9.42054 | -54.7095 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 4df6861c-2c31-32bc-ac4f-ce00d114dbe0 | -10.27091 | -46.57197 | 2025-09-30 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c35f6e13-0e66-33b8-9b21-de661cd0314c | -15.49505 | -48.55636 | 2025-09-30 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bf9e21e6-cfed-3170-a90c-b5303e630677 | -10.88622 | -53.74517 | 2025-09-30 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d9a555a5-f3c1-3713-b23f-e65cbb020b8e | -13.00852 | -49.44278 | 2025-09-30 00:33:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 003190d5-118b-3df8-95cb-0c3a4b0bd094 | -11.24935 | -47.22598 | 2025-09-30 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2f4779db-9716-363f-9e03-2fc7464b1e04 | -8.53749 | -44.67279 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 5d9600c6-0f0a-3b7b-9050-310ae5af5851 | -11.05222 | -47.66119 | 2025-09-30 00:33:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1ea45783-9782-3f4e-8f71-6c56c30c8fe7 | -14.54573 | -48.47557 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| de452331-22b3-32b7-8978-030352aa5ca0 | -14.68989 | -48.17835 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| addc140a-72c7-3f19-a819-a50caa34abfd | -14.70637 | -48.16633 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 197eca0a-6b5c-32b9-b345-a285039babfd | -11.20342 | -47.74583 | 2025-09-30 00:33:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6da5bcc5-e498-3bad-b471-dc4651ba8f31 | -14.52415 | -48.45038 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.8 |
| c1de90d6-a37e-3c10-9d1c-50cca6400fdb | -13.37337 | -47.31412 | 2025-09-30 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8d66cc8b-e205-3fdc-b23f-6dcc66da0e27 | -14.54004 | -48.23101 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 001f8556-2d90-3ce0-9152-9dcf0f20a855 | -14.44583 | -46.36067 | 2025-09-30 00:33:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 62d1fbd2-db90-3782-91ba-999e449e5f05 | -12.75703 | -46.86738 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 913c206e-e3c6-349b-b4f4-e6649ee8ee68 | -14.64686 | -42.38682 | 2025-09-30 00:33:00 | TERRA_M-M | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 34.7 |
| c1e97d7b-b7ca-3ef0-b3f5-45651d36adf5 | -13.21714 | -47.32204 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 9fb885cc-c5f2-39e1-9b60-b696342d71b0 | -14.04243 | -42.15316 | 2025-09-30 00:33:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 42.3 |
| ec89c5cb-24c0-3795-a9a3-c37e485d368c | -11.88967 | -48.04087 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 8538f3f0-5208-3f45-a5c5-2ea779e26a82 | -13.23609 | -43.37133 | 2025-09-30 00:33:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 38.5 |
| a3af2b1f-73da-3951-b13a-f95f66694621 | -12.87648 | -45.16051 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1ae5b3df-6380-3f61-b964-7075f3cb2a55 | -14.58367 | -48.27479 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 86d2599c-1b4f-347c-9b89-71fd33499820 | -13.24289 | -48.43936 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ee5b945c-8a64-30a4-8d14-a27bfeeb7a90 | -8.09695 | -48.01337 | 2025-09-30 00:33:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d19c49da-032f-3b7b-b0d3-d24f7fadf17b | -14.54377 | -48.25859 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 05588454-70aa-3763-8e9c-940caed04b01 | -14.5903 | -48.18934 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2b2ab397-ea42-3461-aee3-1a5445410e53 | -14.63306 | -42.37333 | 2025-09-30 00:33:00 | TERRA_M-M | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 75f97f65-0da4-389d-8d53-dcc0f394a4cc | -13.73937 | -47.89518 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| af332635-cbbb-3936-bb38-adb4e4809052 | -10.38483 | -48.1635 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4920fe9a-1bb8-3183-82aa-eddd76ddfd3b | -12.85038 | -46.87587 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b6ae0e94-ef93-3b92-bcc6-baa6d97e3f3b | -14.04385 | -42.14271 | 2025-09-30 00:33:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 47dee750-7888-391c-93d8-2dbcb43843ce | -11.96863 | -46.57912 | 2025-09-30 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a4ee1612-51c2-3309-a520-263f3f841b36 | -14.70866 | -48.25037 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README6.md)
