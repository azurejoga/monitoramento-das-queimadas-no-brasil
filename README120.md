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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20930306-a769-30ab-8f53-2120a6a4cf12 | -6.16367 | -52.19394 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cec294a-0b5f-3c0f-8792-4b1c35984f27 | -6.16331 | -55.47129 | 2024-10-09 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a7cea6a-5c4a-3899-baa3-969bdd0355b0 | -6.15936 | -44.00713 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c29d567d-f080-3d8c-92ff-a25e2506eded | -6.15527 | -44.00645 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43b8cdf5-2909-3a48-9e1e-f58cf665c414 | -6.13669 | -44.01857 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ba0e3e6-5a92-3f18-94bd-2b12beebd75b | -6.13458 | -44.6995 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0ab6cb1-8c1a-34a0-85b2-d34463d9cb51 | -6.13258 | -44.01802 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d299d861-9c59-3a9d-961d-387504e4159a | -6.13065 | -44.69896 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b25f3c4-5be5-3cfb-9ad2-1a602154f233 | -6.12661 | -50.9497 | 2024-10-09 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5368fdab-edd0-34ad-adfd-a23cd80acd46 | -6.12436 | -51.13873 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2918d44-257f-3e0b-8fb5-2e4a276825ba | -6.12091 | -51.1383 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2561a05c-d269-389d-907e-730bc66070f3 | -6.10932 | -47.03268 | 2024-10-09 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89b760c8-3e0e-38b9-aa7b-392adcf866e5 | -6.09438 | -52.83088 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab5664d9-3c78-32b4-9769-bd747d79342b | -6.09135 | -52.8261 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51708d34-35f7-3817-b428-92f69f844418 | -6.09066 | -52.83036 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cef411db-03b0-3e20-8b87-dc1d0c994ff7 | -6.08517 | -46.48301 | 2024-10-09 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cbba1a3-9a1f-3312-9897-f0aefa42e0cf | -6.082 | -52.46693 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53ef580c-5e3c-3ff8-b884-5da24841255a | -6.07836 | -52.46633 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dbafe54-6e07-387e-9636-dcfcd9721f1b | -6.06161 | -44.02301 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae70f8f4-e90a-3db8-9473-78796f32d1e4 | -6.06107 | -44.02665 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 701cf7bb-6ec6-3b76-a9ce-6b62de27f27b | -6.05754 | -44.02229 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14d55c5e-d2e9-37ba-9b24-beac02a7ea6c | -6.057 | -44.02586 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e3ee751-a4fb-377d-8e05-705a833aa6f1 | -6.01333 | -44.5206 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 380676a0-3a12-36b4-b6ca-d6f0ca8e2855 | -6.0126 | -44.52555 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0fe108b-ea9c-3bd1-a4c3-242dfe87b055 | -6.00575 | -44.62733 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8270c95f-fd9b-3d96-a7e3-38cb68a5533b | -6.00181 | -44.62675 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c9b00d71-f66c-3a33-93e8-452b69d45e6b | -5.99787 | -44.62619 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e801d7a8-5377-30f2-b57e-0ecb54d9951a | -5.99714 | -44.63117 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f6607b21-d3e6-3184-9b3f-4df3ef46fde5 | -5.9944 | -51.05378 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f83f8acc-65c8-33ab-8162-274187d84d4a | -5.99393 | -44.62564 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1b66cdf5-6a81-3147-aaae-a952e22b9c41 | -5.99379 | -51.05754 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b72cb688-ac61-355e-8568-0f72ba8db6c7 | -5.9932 | -44.63061 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c81c664-c59c-3424-99c8-c98b292e104b | -5.97285 | -49.76971 | 2024-10-09 04:38:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4ac247d-0cdf-3960-81f2-511f1b2289fc | -5.96014 | -44.58703 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 457a75c6-a86b-3565-8238-7c7448219751 | -5.95696 | -44.58136 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 307066f0-ed31-321d-acae-44e7c4dff459 | -5.9562 | -44.58642 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef8447fc-6595-334c-9330-62e277101a08 | -5.95302 | -44.58076 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a024438-8617-3876-a9f6-5873bb4eb798 | -5.95226 | -44.5858 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f72375f6-dd1c-3cec-bc5c-80f07b4bc971 | -5.93869 | -45.3919 | 2024-10-09 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de182435-36d2-3ca8-9d4b-6d5f8bfd326a | -5.93494 | -45.39132 | 2024-10-09 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c433dd76-ec5a-3aa9-b9c6-10bdb6277abd | -5.91426 | -51.43916 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d99401fe-3733-3421-abec-73d1ca733e38 | -5.91402 | -44.62638 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56343294-0983-3a8e-8986-536f24315f27 | -5.91255 | -44.63628 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b6d4fb9-1d5c-3224-89c6-f6049831d7ea | -5.90649 | -52.53757 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2822dbf-1d2b-3878-84cf-66ba30f35e25 | -5.90357 | -44.83035 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d621723-141b-3976-a7c3-678ddc0db9d6 | -5.86385 | -53.56694 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c43fedbb-104d-3de3-ad4a-9b43a276f18a | -5.86364 | -53.56476 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03eba35e-84a6-382f-ae4b-aeedfbe247ca | -5.85976 | -53.56406 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b5a227b-a4eb-39c3-a099-3d7cb469754d | -5.85898 | -53.56892 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcd10812-1815-3322-a6f3-ad12d234f307 | -5.85452 | -49.94144 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1ea36f6-7bcf-3491-b81d-926e8afb4ef7 | -5.85406 | -48.16021 | 2024-10-09 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a26f58f5-f3b6-38e5-8465-2ae94f388c63 | -5.8535 | -48.16375 | 2024-10-09 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da77473d-3bbd-3984-bfbb-4de2e00868ef | -5.8507 | -48.15969 | 2024-10-09 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 05b6e9e8-606c-3e85-9939-b76620a6e061 | -5.85015 | -48.16322 | 2024-10-09 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e007d512-77c1-3350-9a43-b4a5540f7519 | -5.84839 | -49.82933 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 377f16f3-f737-3a69-861e-b67d60bd50f7 | -5.84784 | -49.83282 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a4704f5-23dc-33ec-8c07-4bb6f63ee298 | -5.84683 | -46.23577 | 2024-10-09 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 471cc098-c948-342e-b400-36f0856025dc | -5.84472 | -46.23407 | 2024-10-09 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58e51ea0-d040-3186-95c4-e5e11ac7d7b9 | -5.84324 | -46.23523 | 2024-10-09 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9a1e8f9-d680-3123-98cb-fb1c08bacfbf | -5.83937 | -50.1447 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5949aa0-dfaa-3d0d-b531-3d54eeb5485f | -5.83106 | -51.64 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da42c762-b4b6-352c-8978-a22c7a4d024f | -5.8308 | -44.46339 | 2024-10-09 04:38:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cb8943a-4339-3049-8dfa-c5f37a8105ba | -5.81489 | -44.12122 | 2024-10-09 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02247560-cd6e-3201-ac1c-f24ea2c1a5dc | -5.81435 | -44.12481 | 2024-10-09 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a7aed0ad-880e-3990-a5e0-1dd9ed523301 | -5.81247 | -50.20573 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 771eb38a-5fcf-3cc8-b354-7176a7920d7c | -5.81084 | -44.12057 | 2024-10-09 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ca1e7c0-948f-354e-912d-99d02b29004d | -5.8103 | -44.12415 | 2024-10-09 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1ef42899-f361-386b-a2c5-b9482376d801 | -5.80695 | -50.15404 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 757769bb-fe82-39e3-a523-1b0daaebec5e | -5.79623 | -51.61045 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96a6897c-9808-350d-abba-e1ed151573af | -5.79413 | -53.36105 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5b54012-681c-31f5-b36e-24b5e7c68ecd | -5.793 | -53.35888 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 419a1cf5-dfe1-3aaf-83ac-36c9499c0f28 | -5.79028 | -53.36044 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54a20c93-d128-3aa0-853c-25d324319692 | -5.79012 | -53.38486 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffecc407-dbed-3843-ae69-63a5c5145dd9 | -5.78948 | -53.36519 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f790ff7b-1ba8-38b1-a5ab-3bfc7dd6f2fa | -5.78915 | -53.38275 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f8337e7-2273-31e4-a169-3e9e802de6d3 | -5.78838 | -53.36307 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d80b7cc6-bc9a-3280-b782-16aed461f26d | -5.7817 | -50.20447 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88298900-7f2a-3b9d-a9b2-71525041e550 | -5.78113 | -50.20801 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 525d3966-9a1b-3d2f-9c4e-df1c2f09d341 | -5.77943 | -50.21865 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05550e6b-30e5-3326-a220-95aa7287e454 | -5.77886 | -50.2222 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29c277e7-f35c-3912-8f34-45741ac3feb7 | -5.77834 | -50.20394 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f73abf5-b7e6-38a5-9f48-24e3c2def71d | -5.76765 | -51.44802 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8bc0b34-e11a-3dc8-a7ba-2f1c212d594e | -5.7613 | -51.44307 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca5ab48b-a35d-30b9-a074-77ae7996f89a | -5.76112 | -46.57893 | 2024-10-09 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 990cdb6b-55c0-38ef-8b1c-79f531e42256 | -5.76068 | -51.44689 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b82e5b0c-cc94-345f-987d-9d07c7807a10 | -5.76007 | -51.45071 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00acb7c3-0c2f-393a-9b9a-91c8c5fb37dd | -5.7572 | -51.44633 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dae82004-a92e-3eac-93e7-8b3f86016793 | -5.75046 | -49.25138 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17b4cc27-9c76-32de-9892-1fc3ca3f03dc | -5.74714 | -49.25085 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ee7677d-1216-37da-8554-b9a9b04872cd | -5.73196 | -51.10482 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb09267f-8be0-33fa-a002-c5bff6f0b871 | -5.73083 | -51.10381 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5979f83b-3b8e-30a6-801e-a7f563868b1c | -5.72862 | -44.0361 | 2024-10-09 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43d10e56-4ebb-30b9-8b3d-0aade62793ce | -5.72459 | -50.05438 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 017c9301-f6a1-3f9b-8301-c0c8a9de1ba4 | -5.72403 | -50.05791 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c07db2f4-0c56-32b1-8c3b-68b10506c8c4 | -5.72268 | -48.9767 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3959e0c-d416-39fe-9aad-68ad13624f17 | -5.71795 | -49.98838 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b5733ee-84b9-361c-a084-d9ecf8b5b5ba | -5.71739 | -49.9919 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b7336b9-74ec-35d9-acf9-89be115812e1 | -5.71461 | -49.98785 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94fb6eba-4411-3c23-a860-96941dc0abe3 | -5.7135 | -49.31301 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff310845-47c1-3ae4-8fa7-218e14bf4f27 | -5.71232 | -49.27734 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README121.md)
