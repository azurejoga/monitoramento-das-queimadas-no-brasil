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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9415a993-3609-390e-86da-a6eb948dc9fb | -9.75686 | -51.06236 | 2025-09-10 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0624cfd2-f36a-3a0b-8ca9-4fcabac108b8 | -10.71909 | -48.2823 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 66d020e3-c07d-3ad6-9407-a1805ed53fd2 | -21.3966 | -43.87534 | 2025-09-10 04:17:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 442e23ea-f1d6-380d-9939-7c91d2e24a9b | -14.33941 | -47.3007 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3a2b6ba-9409-3499-9f8e-2f0b43338d01 | -20.38755 | -46.63326 | 2025-09-10 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 88c9689c-27c8-3e28-bb6f-2c5cfd93f379 | -13.01496 | -48.04029 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11652f31-251c-3dea-9b7c-314dd66e7b8b | -13.96516 | -48.22181 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dac49fec-d845-37ed-a2f5-1c9279eaef29 | -11.49599 | -50.41519 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b418a89-96cd-3b5a-99e8-9a9a1b2d17bb | -11.41981 | -43.57139 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9c429f2-9db1-304f-8e99-55f13290a345 | -13.33918 | -51.69376 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7746e3e7-2d42-38ed-b619-4ab2bc3130b3 | -11.12411 | -45.11383 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ff93ea66-72e2-329e-add9-7f04ad0f5e8e | -21.02536 | -48.42117 | 2025-09-10 04:17:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 446ada2b-a544-35a0-bf5f-72663fc24aa6 | -14.92661 | -50.10355 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0441bf15-bbfb-378a-8840-25c7d5c0c89f | -14.3914 | -47.32439 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e74348da-bb47-3985-84fe-a14bd9fedb40 | -13.18507 | -47.25962 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a570e026-e287-3b80-8b9c-da3898945896 | -11.11625 | -44.8632 | 2025-09-10 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a706d11b-3f1a-351e-b131-6a58b9b78853 | -14.57581 | -51.4045 | 2025-09-10 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0a3472d-9c9e-321c-838b-48388b30bdc5 | -13.00459 | -45.20908 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db698744-98dd-37df-83c9-39c76d051d90 | -20.93844 | -45.79422 | 2025-09-10 04:17:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea28f0cc-7ef5-3fb6-a525-a083d02ade28 | -15.84002 | -42.60862 | 2025-09-10 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 83004130-c0b2-37b7-aa4d-1c19f882e2cb | -23.35552 | -47.2073 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0d108baa-9394-33ce-bb30-b05ddb2e600c | -15.18034 | -47.951 | 2025-09-10 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9643b1a5-0e0d-3ea7-90eb-0e908be4c235 | -11.10549 | -48.45722 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 707ff0ad-f695-3624-867f-9fb2d5edcf02 | -12.93705 | -54.80843 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cfa4082-bffd-3f9c-97ad-51c4e2471908 | -13.9435 | -48.26245 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f28dec44-dc5d-306d-8fa6-4b58ef96ff38 | -11.2956 | -53.95385 | 2025-09-10 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0e53d4d-528f-3f08-90bc-851e122b4c19 | -13.18414 | -47.24378 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3032a8b-b994-33ca-9f99-469a3873313c | -10.65736 | -48.61847 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16a52ac6-cef9-3d02-80a4-31dba0f5bb05 | -14.65591 | -44.05335 | 2025-09-10 04:17:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cdc03e60-ffee-35b6-bf3e-ef8cf1b835a8 | -16.56705 | -41.64564 | 2025-09-10 04:17:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5aeedefe-31b6-3062-b9dc-e637ae6f7894 | -15.80832 | -52.25048 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e3a8874-edbd-39d9-9a1b-9245cca75ca0 | -11.3068 | -46.48073 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7ad111b-9f53-3a1b-8887-506f21a6af68 | -11.53638 | -47.31894 | 2025-09-10 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 01e5830a-f0a2-360d-b402-387ffc3e00ce | -23.37029 | -46.69388 | 2025-09-10 04:17:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2fbd387b-2ac3-3904-9a43-ca2c0791b206 | -11.4967 | -50.41113 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c329f9b2-95d3-3f9d-b8a0-f328003bcf20 | -12.44142 | -44.74485 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e834eed0-9ae8-3285-b939-c003db4b1f3b | -14.75383 | -45.33527 | 2025-09-10 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53d7b0e4-526a-32e7-b5b4-53fc24a079bb | -13.18092 | -47.26303 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ed14366-c277-3c9b-ba3e-d5732b98e071 | -14.44143 | -52.95333 | 2025-09-10 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a80373e-f390-3c36-893f-19e6006ab129 | -11.9529 | -46.65373 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55865df6-2b6b-360e-902c-69393dcc52df | -13.93347 | -48.25584 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f94122a-ab48-34b8-9f6c-ec18b1e93d30 | -10.19462 | -46.82537 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ad9a032-d509-32f5-888e-58a5106c3a19 | -11.83184 | -46.74805 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcdb592a-4513-332e-93ee-2da332c81219 | -11.10979 | -48.36238 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 611ca505-be9f-3085-b66b-536c77fc371b | -13.18573 | -47.25571 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92dfbec4-d033-3e23-a837-628a1b4aa815 | -10.17332 | -46.21013 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70749e36-09ba-3d90-8c2d-b0b4353c3e71 | -15.95522 | -50.22453 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3b56a01-0ec0-3859-881b-c46066497142 | -11.99391 | -47.19086 | 2025-09-10 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c9a0df7-fc33-3894-964d-46bb6e512358 | -15.10983 | -50.09398 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dcbbd105-6870-340b-8ce5-061504eea424 | -10.30764 | -48.82002 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fc16b1ea-33c3-37a6-89fb-7f3171ae4ce6 | -16.97629 | -45.85025 | 2025-09-10 04:17:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f32f2bc7-25b3-30be-ab6d-db339a076a8c | -11.11555 | -48.44416 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b750555b-b0a6-3e51-8f84-cc434e908fec | -13.98317 | -46.6629 | 2025-09-10 04:17:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7114a48d-f577-3f43-a65d-583e9e39662c | -12.99407 | -48.03194 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dbb63a8-7cb8-3014-b4ec-214606369d81 | -16.28189 | -45.67841 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5211cffd-d92c-3ae4-ac7d-dda02340328b | -20.98638 | -48.00707 | 2025-09-10 04:17:00 | NOAA-21 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| efc764dc-a201-349e-b54c-97881350fd99 | -14.60486 | -52.10138 | 2025-09-10 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da3adcca-8bd1-32e0-b8d9-6996e31133d0 | -10.60417 | -43.30508 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0924ac76-bb59-3467-b22a-ed8699b7a840 | -12.02648 | -45.85673 | 2025-09-10 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02b01f22-eda8-3337-a267-461ec756c99f | -12.01908 | -50.99495 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 765285eb-2a7d-3cef-b733-e0af2dff1540 | -11.91989 | -50.79132 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 347120d5-2626-3ed9-b992-fe0caffcad4d | -12.00751 | -50.98385 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 31da6e0d-3c0b-34a5-9972-bd82124e79b6 | -10.74767 | -48.18283 | 2025-09-10 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72f785ad-ce4e-3e77-a2ad-11750ef47ba9 | -12.18124 | -50.62329 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f11f8d0-0e6a-3c33-9ac0-58e53621d0ae | -13.9718 | -46.66864 | 2025-09-10 04:17:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d2a0aef-5f13-31fb-b385-e1b70d79a88f | -11.61512 | -46.63755 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdc08fdb-72bc-38e5-b3c1-f99bc1f1fbaa | -11.75895 | -46.46585 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84a4c8f8-9252-3479-b173-b70476112000 | -11.54346 | -47.32019 | 2025-09-10 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fff51089-878c-3acf-a873-b6a54dfb027a | -13.75927 | -47.17065 | 2025-09-10 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eba4e263-b649-3127-9a26-5bc29b50d968 | -21.92584 | -45.63832 | 2025-09-10 04:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 89f85749-5491-3697-97af-08e611de22e0 | -11.12095 | -48.43542 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56d5f50e-8cf7-3560-ae00-16988ba83a7a | -15.16493 | -47.95678 | 2025-09-10 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82e0e22b-5647-31dd-a8b5-44cff4afeb3e | -22.22174 | -48.69842 | 2025-09-10 04:17:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dcfc7ec8-6de6-3945-bfd8-7476c0b8f9d4 | -14.32725 | -47.31002 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b02a8c4-c550-34c6-975c-bdbc442befda | -13.76088 | -43.61473 | 2025-09-10 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2856e36-f16e-315b-8a2d-a9ff53cb7e6b | -23.03223 | -50.10348 | 2025-09-10 04:17:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f7fce89f-8318-35b4-90cd-483cd81fbcc5 | -16.28077 | -45.68556 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca21d402-6971-39e4-9f43-cc7e8ddc0466 | -10.29767 | -48.80776 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de7414ba-74d5-36e5-8757-3d4c5042dba1 | -11.43541 | -43.62461 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d3f52d7e-4064-3629-9c74-41fc86814094 | -11.94175 | -50.76917 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e8e4178-edab-3c78-bf59-6d39f3b3d528 | -11.12355 | -45.11735 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 650981f1-a8d8-3474-bb58-dbfe35e7d342 | -21.39717 | -43.87114 | 2025-09-10 04:17:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 34147993-e942-38db-ab2e-ac525718b124 | -14.46297 | -53.27188 | 2025-09-10 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb04bac6-4d67-3f5d-aaf5-3ba341c89fd9 | -12.0111 | -50.98899 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1fe3ebe9-2471-35d5-8226-dde8f031240f | -11.33668 | -46.53217 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 27b4f5f0-0525-317a-a533-0c0ee50d8821 | -20.89717 | -55.18517 | 2025-09-10 04:17:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b17d0bfd-40c7-3c41-8e80-32d3547948c2 | -12.17272 | -50.62172 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0738990b-0dc0-36e4-88c4-b7147e5ae300 | -16.61656 | -49.7734 | 2025-09-10 04:17:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13c0bac1-1a0f-3e84-b225-0b7809c3900c | -10.54929 | -51.51134 | 2025-09-10 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7d745bb-02d8-3c36-8b9b-fabe9335d651 | -11.42536 | -43.57952 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee092b48-4158-303d-b7e1-15ed6b304361 | -14.25492 | -47.10846 | 2025-09-10 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdc7feb0-bf19-30f3-81e3-07f728671003 | -12.44087 | -44.74836 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9021e687-5487-3843-a836-0cdc5c370f81 | -23.40839 | -46.42155 | 2025-09-10 04:17:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e4e37c02-0953-3ab9-8766-e620c4f9c045 | -21.59914 | -43.97758 | 2025-09-10 04:17:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9fc6809-b930-395d-87b1-2204e1121868 | -11.44655 | -43.61888 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9833f7df-b6e6-3414-8c69-2ab310b025b8 | -21.22147 | -44.1446 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 381cdf9b-c6f3-30f9-9cbd-cf724d8131b3 | -11.3445 | -46.54906 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55bcc1db-5167-3745-b08a-2f92451f0ffc | -13.29209 | -51.7226 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 203548bc-c6a3-315f-b321-b30f2f098be5 | -12.01032 | -50.99334 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35ae7b79-3055-364f-8ba9-dd96799bbd8d | -17.55775 | -44.54129 | 2025-09-10 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README44.md)
