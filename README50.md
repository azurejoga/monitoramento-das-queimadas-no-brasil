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
| 190ff036-a0af-393f-a6b6-bd7fe962ba5c | -10.06228 | -46.94566 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fefc8d3d-f054-3cb0-a8a5-0f1bcee5697d | -6.2301 | -53.47882 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f173e689-6b74-36c5-98ca-7a1ad25d69a5 | -6.98169 | -55.64454 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d506b9e-fe67-38f1-8ba3-1d71810f8df1 | -6.15327 | -57.79461 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00fdc8b0-50ae-3825-95ef-e1291dc581aa | -6.25237 | -55.42244 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97d3894f-12bb-36ff-94d2-4477af8af557 | -6.22846 | -55.93987 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfdda953-a69d-31a9-ad65-6e337c9de5b0 | -6.24624 | -55.39657 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b4c6542-86e4-312b-b518-9071716c1f0b | -6.17467 | -55.46357 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b439e40d-4c0e-301c-8d9e-661ddccab0e0 | -6.53709 | -55.25309 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97bbecce-6651-3856-b88a-9bf3d11990b5 | -6.2508 | -53.36607 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 995e4ac2-0e4c-301a-955a-e5ff28084396 | -6.07922 | -56.47311 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8bd3c00-e494-3786-b951-855a0d833bd2 | -6.83317 | -55.61728 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1174ff7f-9002-3c5e-a435-1ede722d80b8 | -9.21412 | -51.54848 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f1126ec-f879-3607-aeb5-2dadae145d54 | -6.21712 | -53.58769 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a46fb8d3-9e92-3469-abb3-ce711261292e | -6.15609 | -57.79885 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6888430-ca1c-3117-a94d-11d5e7595157 | -8.60089 | -54.77684 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5c35ce4-4701-3672-bc26-5e03599c623b | -6.90046 | -56.62968 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4dc6cc1-245a-3811-9ee0-cb97edd6ab38 | -8.53165 | -55.34753 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e99c59e-20cf-37cf-921c-124401cbaf18 | -4.95931 | -56.27331 | 2026-08-28 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63f4a6a2-76fc-334f-a59a-3bcc0794e011 | -7.26938 | -49.85487 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f10bb9ce-b3ec-3867-a036-41a18124a859 | -6.00356 | -57.83166 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df93dbf0-3003-3b4c-9cbc-37feccb50a61 | -5.28776 | -50.93588 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 979ba271-8e94-3c40-b010-4b34fe04041e | -8.59635 | -54.78367 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acee4463-59ad-35b2-b634-3e856c3790e2 | -6.53431 | -55.24908 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e2114c85-b408-36eb-90d5-7cda5643542d | -6.22154 | -55.42474 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 252ff898-3383-3602-92b3-93648b44cc37 | -6.76188 | -46.13667 | 2026-08-28 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff2bc532-ae05-3d9b-81cc-31ecf897cbd3 | -7.26561 | -45.86747 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe05675e-74d0-3ed1-9164-345bcc0eec85 | -7.69751 | -55.36656 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c3cf80c-0676-3991-8120-49b6787b5b70 | -7.78723 | -61.57907 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a821deee-177f-30dc-b72d-ba30d3522eb7 | -5.25531 | -50.96238 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f615529-8764-3a93-8577-ff9b2ea23a5b | -8.602 | -54.79211 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc61908d-1d15-3d48-b5f1-09149f384cb2 | -9.98602 | -48.59832 | 2026-08-28 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4b0489c-8103-3b44-ad07-95d3a5745e73 | -7.26567 | -49.84957 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e71b2c3f-c081-33b8-89b4-0125bd7be5e9 | -6.22823 | -55.48978 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dda2ffc7-e55d-328f-a41e-d71e1ea2ba77 | -7.37398 | -55.1529 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9aedbd9-a29a-3265-92df-64aa88a4d927 | -4.92777 | -55.76556 | 2026-08-28 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd950095-1cfd-3b0c-8d21-a63bdd3a485d | -7.26919 | -45.34841 | 2026-08-28 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5925315d-497e-331b-bd8d-c8be2464f14c | -4.45457 | -55.49303 | 2026-08-28 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2710aa4e-f210-3270-ae22-5c29f9dba29c | -6.15728 | -57.79147 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 692e177b-2b23-3fda-b7a8-7221c1f9ef66 | -6.12667 | -53.53886 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6a05c16-ee8c-3878-b680-a695fc8ebd75 | -6.23481 | -55.46947 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af4b7087-7b8a-336d-8f2d-cf43fee42701 | -6.53098 | -55.24856 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cf5197d2-3407-397f-a98a-6dbff0431799 | -8.2233 | -54.95541 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 84669e77-a340-3838-8c13-c647860ccd73 | -9.44798 | -51.71096 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74a0abee-36b2-3871-a26f-40f3a1657d13 | -6.25787 | -55.40905 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fda86c1-e127-37c4-b0f7-73e46a5f4609 | -6.16634 | -57.8005 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 911ebd4e-d3df-3128-897e-09bf3cf130d3 | -6.84167 | -45.02974 | 2026-08-28 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8b623d1-f6d9-3202-8262-d7dbb4805e86 | -6.97837 | -55.64402 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db69188b-06a6-3c92-aae8-1c2a22694c37 | -10.53631 | -50.77881 | 2026-08-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6ab595a-d267-3efc-b2a6-92cc8bcc73d3 | -8.16739 | -46.16269 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58325fbe-6646-3f96-927b-18e3a194f593 | -9.20941 | -51.54807 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74804e00-7885-3751-818b-42e602cfa50f | -5.1498 | -56.27188 | 2026-08-28 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 367c4cd4-72a6-3242-9014-88657fe0201e | -6.26119 | -55.40958 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e16f16f-3da7-30eb-b202-d20d7f0a9ffd | -9.61622 | -55.119 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 021efaf3-d749-338c-b1dd-a1a5593445ea | -6.17153 | -57.78999 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 280acb39-b215-3cbc-a260-b0ff77b61ec3 | -8.589 | -54.7637 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a3e46f6-1c2a-3f69-9426-b09dd82ae377 | -7.37064 | -55.15238 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de72d8cf-c562-3f93-b07e-d687900ad2c1 | -6.32194 | -54.74272 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4ebc39a-bb7c-37ba-bb1f-d6049552f11a | -11.24437 | -45.04522 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b4c9fed-03e6-3d9f-9f83-ac194e1fede6 | -4.85404 | -45.40519 | 2026-08-28 05:10:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0c30f9-363f-3b0f-ab3d-9213b956dcb2 | -7.49257 | -55.28739 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dccd6e2-4f9a-330c-bc06-9532efa5edb6 | -6.15847 | -57.78408 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b68f0493-a9d8-357c-95a4-e39711048165 | -9.46266 | -51.57961 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 184b7f75-5423-3612-83fd-eee67e841164 | -4.49839 | -55.51703 | 2026-08-28 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56dbcf47-5684-3e44-82ae-3a05fefcb46d | -7.57783 | -61.31427 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7c259d1-f96f-318d-8efc-e0104af4de4a | -6.75803 | -46.14064 | 2026-08-28 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d78f293-99c8-3890-95f7-29c4b4c7b9a9 | -5.89397 | -52.10991 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 11d96500-d5c3-326d-a994-d978cc29976a | -5.93514 | -52.36341 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23db2044-31ac-38b2-bd87-b41e3f04a34d | -5.99953 | -57.83485 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a605075-1b7d-395a-b768-fb9959e1842e | -6.42663 | -54.93703 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a847e46-088a-3dca-a6f3-f15d3afe5b36 | -5.92778 | -52.36227 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3e3745c-3cc2-345b-a6c6-1d41edd3d94f | -11.01493 | -45.07153 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9f7c0671-4400-3acc-aca3-4af891bb7cb4 | -6.26134 | -53.36767 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d007c3ff-707b-33bb-9653-fb00e5cc311c | -6.75489 | -55.68319 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d2e8c5e-6e9e-36b1-8590-15eda431b9b4 | -6.84031 | -56.45275 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3763ae23-a69b-3157-89c8-f8ac4de94f22 | -10.06032 | -46.94852 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b786611-a333-3963-b332-9e4e1395ff2c | -6.9712 | -55.64646 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2aad9794-c0f5-303f-92a9-f62eeddd5271 | -9.2232 | -51.54258 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfa01e23-9d15-3591-9dcb-73bc83266623 | -5.76014 | -50.22398 | 2026-08-28 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a81576e-5fa4-3c71-af16-e19b5cc25242 | -6.23149 | -55.46895 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ecd99d7-6ea6-3960-ae85-903dcbfc7ae6 | -8.02822 | -48.02396 | 2026-08-28 05:10:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dec3524-a4ce-34de-8d54-e67952d7a14b | -6.49824 | -53.25986 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8a7b92a-1df9-35f6-8100-9dec8f350af0 | -8.05875 | -45.86366 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc061d21-5b05-3724-b82f-065df7b00348 | -9.21315 | -51.55531 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0efe0378-2359-35a0-9aae-44c5425d097e | -6.41375 | -51.68217 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0b2bfc8-1009-36d7-8780-c7757f2b51f8 | -6.41445 | -51.67742 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba917b62-8cf0-3b60-9ff6-f40ccb16d4ec | -11.38334 | -45.14624 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d1f69cc-fcef-3b47-bce9-e225e5edc117 | -7.49312 | -55.28387 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbab49da-6a4c-30a6-a3c1-cfb2b4da1774 | -3.45812 | -59.51809 | 2026-08-28 05:10:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24aa9732-5f68-39dc-9123-fba59e069095 | -5.99268 | -52.20025 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8bebfcfa-8547-30f6-99d7-1839a91b8746 | -6.26559 | -53.12423 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee810ac5-37d1-391f-89e1-57356cdcad44 | -7.37119 | -55.1488 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5c63986-fcad-33f1-84eb-f67b2df24de4 | -6.82046 | -55.6117 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94314849-6924-3ee1-a46e-a2394c2acd74 | -2.50049 | -56.07367 | 2026-08-28 05:10:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36020147-4628-3e47-95ca-50b71e8816c5 | -6.84078 | -59.94171 | 2026-08-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bef4f402-3525-38ed-a772-6f6b8c12df84 | -5.9241 | -52.36174 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f1d614a-d08a-3f0d-99ed-6ee8ad953517 | -10.01571 | -46.40889 | 2026-08-28 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc62ca9b-fbd0-34a2-9b02-9a9cad2d7e58 | -9.98178 | -48.59199 | 2026-08-28 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf596601-0195-3abd-9301-43e6ffd17374 | -7.57905 | -61.3072 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce9d16a3-3688-3276-a825-5c6e29a6a1fb | -8.16098 | -54.9565 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README51.md)
