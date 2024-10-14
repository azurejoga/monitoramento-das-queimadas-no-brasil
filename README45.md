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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03905502-c822-348d-97a4-8ebb29d290ea | -6.94116 | -45.54303 | 2024-10-14 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d34647f-8284-3505-a328-c87c0e7bfaff | -6.82405 | -46.49525 | 2024-10-14 04:19:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f55a6183-586a-3459-936f-470a10680671 | -6.79813 | -46.37535 | 2024-10-14 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0b1f461-51cc-33ac-b1a8-41df56b4a2ac | -6.74907 | -46.46453 | 2024-10-14 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 908cf831-5fa2-39ef-8971-8a2e25fade53 | -6.67787 | -45.95836 | 2024-10-14 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eab194a7-a884-32c6-ab97-dfba75dccaae | -7.70795 | -46.59945 | 2024-10-14 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37a704ad-6a4b-39c6-bb4b-8ac9b9391f2d | -2.08438 | -46.84782 | 2024-10-14 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 662fa93e-e71f-317a-bb9b-fe4caa52e310 | -1.98417 | -46.60685 | 2024-10-14 04:19:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc56048b-8ed1-38ac-bcbb-8c59f1b49ee3 | -1.82225 | -47.0847 | 2024-10-14 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f655d0be-439d-3fa5-b39a-c134cf06ce01 | -1.28906 | -46.32352 | 2024-10-14 04:19:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83bb5a19-cf67-3658-aaf4-49118927996d | -3.55998 | -46.14683 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25eb65aa-d6a4-33ee-9fc5-5a9f11bf6ab1 | -3.53405 | -46.30901 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16464921-59d8-3836-b621-dca20fec2f36 | -3.28161 | -46.34787 | 2024-10-14 04:19:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87535559-0a1e-3687-acef-383bebbfa60f | -3.27752 | -46.35117 | 2024-10-14 04:19:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 696bfc55-c32f-309d-a67c-041d01602c76 | -3.06832 | -45.94807 | 2024-10-14 04:19:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b75f821e-6899-392f-9368-13c5329cf0b0 | -2.75533 | -45.97246 | 2024-10-14 04:19:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bb8634a-1a0c-34ea-95a4-a02b2674d422 | -2.74937 | -46.74618 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 742b0ada-45f6-3e15-8003-39ed630acd19 | -2.74873 | -46.75021 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3aa9b274-a615-3e58-851f-d6ea63f55352 | -2.7481 | -46.75424 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca14b696-8dca-3453-acd2-95c73d088135 | -2.74454 | -46.75368 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce5b5b49-9af9-3418-ab0b-91af8836829b | -2.71896 | -46.70846 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5737f84-76ce-3860-9089-f1b3ed0addaf | -2.25142 | -46.74973 | 2024-10-14 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb61a870-322e-3cda-8931-e76e0387a78b | -2.25077 | -46.75381 | 2024-10-14 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88e56b6d-56c8-3b24-81da-aedf4cefe5c6 | -2.24981 | -46.73697 | 2024-10-14 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfb1c626-5695-3a8e-b6d8-98032191fd0d | -2.24785 | -46.74918 | 2024-10-14 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20d845f1-6a06-3376-8dba-07b568ef9545 | -2.24589 | -46.76138 | 2024-10-14 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51d88485-a0df-3a94-89be-030e9467ec73 | -2.24558 | -46.74047 | 2024-10-14 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1f886e4-cf1b-3149-91b8-117af2ce2263 | -2.23676 | -46.77252 | 2024-10-14 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c143170b-0c73-3c7e-80eb-7980152b1e6b | -2.22401 | -46.76754 | 2024-10-14 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80896e77-8c3e-33b8-93c3-499df32ec280 | -2.20055 | -46.45523 | 2024-10-14 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f631c66f-08c6-3d73-b658-70bb3df6d230 | -2.19702 | -46.45469 | 2024-10-14 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43251f7a-d4b5-3d78-801b-9214b99649b9 | -2.18631 | -46.56712 | 2024-10-14 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab9281a9-91a9-3032-8354-afb82dbf0708 | -2.45253 | -46.01886 | 2024-10-14 04:19:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2204aed-96f5-35df-86a9-f53349f0c055 | -2.45192 | -46.02264 | 2024-10-14 04:19:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ddcf17a-6b06-3f38-9bbf-075af2cd10e3 | -2.44878 | -46.92199 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 08e77f05-d6f8-3099-a8c8-f09bde802577 | -2.44812 | -46.92612 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 31f352c1-0fe1-3aed-bff6-432c2baa7adb | -2.44585 | -46.91727 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5073ee06-f809-341e-8e17-8eec0a4426ef | -2.44518 | -46.92145 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 39ece771-0342-305b-8f42-4e3d51a60134 | -2.44452 | -46.92558 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 531e2fa1-1ca5-3707-a76c-885171aa1cb6 | -2.44226 | -46.91672 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d1ae44de-960a-33cb-9a44-e77bdc3e7243 | -2.44159 | -46.92089 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 828edd12-da6b-3122-96b8-fb0da3cf3ae8 | -2.44092 | -46.92502 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b215b417-65ce-33b6-ab62-02a704290829 | -2.43866 | -46.91617 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da68450d-0119-3488-8aad-f4c0aec62761 | -2.43799 | -46.92032 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 687709ed-6b0d-3c43-b0eb-47726412fe29 | -2.42506 | -46.15457 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02128df1-6559-3372-906e-7536cd2953e9 | -2.42158 | -46.15403 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21af03b7-09fd-3607-9509-4a286216eaa1 | -2.42098 | -46.15788 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fb92bec-8487-301c-8f34-f60dac48e65c | -2.41811 | -46.1535 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2537ae9e-d9d4-371d-bfc8-86a246ab3ded | -2.41751 | -46.15734 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e00da64-a8b3-34d4-9381-f94af9db1d6d | -2.37041 | -46.48075 | 2024-10-14 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c47a37ae-c586-3d87-bf62-958e8188b91a | -4.52804 | -46.55546 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c874720e-8f78-3f49-87bb-7d7a1392a8bd | -4.28553 | -47.305 | 2024-10-14 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f10022d6-6571-3044-9a56-b1eef8fee6bd | -4.28489 | -47.30904 | 2024-10-14 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8028b731-4a34-3036-860a-10fe5f946a21 | -4.2012 | -46.90232 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55f0482b-4fd5-3101-bd5f-0f256be1243b | -4.19119 | -46.6652 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2146065b-fd79-3152-aaea-7d7da6170331 | -4.18015 | -46.73504 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb4d2efb-0864-31f8-a46f-db30a8cb70a3 | -4.17953 | -46.73896 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85e5d812-d3b5-3297-b81a-caa253a4d2e8 | -4.14915 | -46.86265 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f925f97-aae2-316c-bf23-393500c545ba | -4.14854 | -46.86653 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e42c6939-d24b-3bfb-a395-1caa2129c62b | -4.14564 | -46.86205 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 384bccdc-8389-3d5b-9b31-a04307d94687 | -4.14375 | -46.69346 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a361c16-6151-3299-b2e6-9aeb471fc23d | -4.06062 | -46.2243 | 2024-10-14 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 615590a5-44f4-3d06-99c5-65f98895ceba | -3.94558 | -46.43765 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b3aa09c8-56f1-3cc5-91c1-9c413617cae4 | -3.94497 | -46.44146 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| efc2cd54-916c-382f-9d8d-664f546193d2 | -3.9358 | -46.43222 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9f484e6-755a-3634-a672-d500932ab68f | -3.93295 | -46.42791 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c95c3ebf-0260-389c-a154-b34a55a8b24e | -3.93234 | -46.43171 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fbc5ac6f-a11f-3256-a982-92e5677fcba2 | -3.9313 | -46.41607 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da4cfd68-2ae0-353b-a29e-f5eb92153fef | -3.92845 | -46.41177 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5959f5e2-1ceb-3da3-8c45-2d634226d2e3 | -3.92784 | -46.41553 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8920c8f6-992d-3a78-81b3-aae636e9e60e | -3.90222 | -46.42771 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f900637-0083-34e4-a82c-42616089e03e | -3.89864 | -46.45041 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f03354f3-16c7-36ea-802e-a532720d1370 | -3.89744 | -46.45799 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5ea4959-b2ee-35a1-80a9-094d578b5653 | -3.89051 | -46.45688 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| deac5fd9-ade8-33f7-9f95-f12d84cd725c | -3.87766 | -46.47066 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb04c02c-1bb1-3520-9ae1-43a33891ade2 | -3.87481 | -46.46621 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c603370-2637-3ef7-ac58-12608ad22053 | -3.87135 | -46.46566 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a900a0e-3269-3a10-be28-efb71b697d68 | -3.85716 | -46.91969 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2def2281-d76a-3133-ad08-9dd5481dab5e | -3.85624 | -46.4712 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a69b0f37-e04b-3df5-bd15-52ddcef9104c | -3.85429 | -46.91502 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4401caf-5e39-3b8f-ba98-faa54acdc84f | -3.85363 | -46.91907 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b6d558c-a613-33e8-b21e-8098cbc0b27c | -3.85298 | -46.92312 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8dc73b7f-8b3b-357d-9b2a-a03720ddc8b0 | -3.85215 | -46.47453 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b39acbe1-6199-3e2f-80c0-053d4408d0bf | -3.85141 | -46.91043 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d0d6d2b-64c0-34dc-9ddb-fe1007174798 | -3.8501 | -46.91848 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a65a1b27-a1a8-3c8a-8c79-3d1f5dca3f22 | -3.84944 | -46.92253 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99e2afd0-cce9-37ce-8dba-869e2ada1261 | -3.84657 | -46.9179 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e519b97-41b0-3d8d-941b-ee4568549282 | -3.84591 | -46.92194 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1053355-d2e0-3b9b-ba72-be5811cff51a | -3.84562 | -46.90138 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 284032cd-2f0e-39a4-9da4-2b1003c02f9e | -3.84497 | -46.90534 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 843609bd-0a97-345b-b939-eca8b2055ae3 | -3.84433 | -46.90932 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a3c793e-2047-3ad1-b8ee-f15fd54e0663 | -3.84398 | -46.48114 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94e2fe64-6187-3541-a418-8b92f78cf537 | -3.84303 | -46.91733 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c9ec9e4-3485-3d0d-9565-4bb8c595308e | -3.84175 | -46.47285 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d22f7706-01f4-3a98-a472-cece1c831e2f | -3.84112 | -46.47675 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25b0bd2b-600a-38d4-8e52-9060522eb8eb | -3.84079 | -46.90879 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbc62b64-8f43-3e8c-988e-e6da8fc49428 | -3.83764 | -46.47624 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 548be86f-b3db-331b-9e47-e683f70ab02c | -3.83724 | -46.90826 | 2024-10-14 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86c09f4e-595b-3b92-a7b1-21d19412fb9d | -3.83702 | -46.48011 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 74b76c16-ffb7-3ac0-8237-86c39ac6e2a5 | -3.8313 | -47.49444 | 2024-10-14 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README46.md)
