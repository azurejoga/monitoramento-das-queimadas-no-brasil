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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22c1a8b9-a6e2-3a33-9178-04df3905ad9e | -14.4217 | -52.59054 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c083fac-4630-3bf6-b1ce-b5b4f8dd2ef6 | -10.88945 | -50.52081 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80b7d109-bf1c-3056-b144-1a7408fb2053 | -11.56555 | -45.49765 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfe605a8-c40c-3abc-8a79-ae2ae81e8944 | -7.37482 | -55.15144 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 407b295f-48ae-3890-82c3-b69023638709 | -10.80309 | -54.01646 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec761ce7-3a76-3550-a6b5-194422229bd9 | -10.50151 | -64.50163 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9f9e7c52-9c49-3169-add6-b8ac2907df5a | -8.72364 | -48.2281 | 2026-08-28 04:51:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b1de6b5-dac2-3252-8e69-36af45f06e19 | -9.23672 | -51.54567 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f77c1500-5c00-3602-8292-ef19dc2afb6b | -9.22587 | -51.56991 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bff945c0-9f5d-334c-9166-ab8c9f4543eb | -14.32461 | -51.70467 | 2026-08-28 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1f95a501-bd66-35e2-82d8-7a53e2b1e709 | -13.40991 | -51.41402 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 58ab91a1-d969-37e4-8816-863ea20dc0fb | -11.29411 | -54.03327 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2bdabb1b-7d19-360f-b46b-1bd766bfd9dc | -8.59563 | -54.78546 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d0acddc5-1c81-3690-bd96-9d0d6514d326 | -9.33914 | -48.16611 | 2026-08-28 04:51:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9c377fea-112b-3d8e-8e8f-b526eea13c25 | -9.98883 | -48.59726 | 2026-08-28 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a2e63ba5-eee9-3829-8f94-713a74b1b648 | -12.50577 | -43.81656 | 2026-08-28 04:51:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 661f334c-9dde-3324-90c3-1f78c10e2a70 | -8.77779 | -49.94451 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f58306f2-4217-379f-b1c6-4edefc57acb0 | -12.26056 | -50.57614 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 6c2829c5-5af7-373e-b2d7-1dfb9f450b53 | -11.61863 | -54.58513 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46a54302-c98a-3e23-bd9e-4bf1925f23ba | -13.40602 | -51.41702 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86072c36-b6da-3648-8ef6-2910e0eae9b9 | -14.86013 | -52.62359 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c12b2533-65dd-342a-a43a-24c037fa5cfa | -9.43419 | -51.68877 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71918b18-4fd1-3726-a89f-e151cddff299 | -8.23427 | -54.96949 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1b345ea-ca0f-3163-b01c-8cb41f4245ed | -14.93723 | -52.60258 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff50ce98-f4c8-3469-a39f-13ee71d42262 | -10.96614 | -49.57242 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27694311-3ca6-37fc-bfec-6b6838102a2f | -10.92336 | -50.5369 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c7173d6f-3a4d-3b08-8e52-9975aee0af7f | -12.77058 | -46.4589 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51952005-5c22-3abb-bc7a-160be1158f34 | -8.15805 | -54.95338 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42a5d51f-1e09-3ad3-96ed-4676e6fa4326 | -9.43314 | -51.69291 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f7db875e-232b-3d52-a6a6-0742ddfd3de1 | -11.5661 | -45.49851 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b41c02b-0b83-39c3-b5a4-712b20dad620 | -13.4121 | -51.42167 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66518b3f-731d-3f6c-ba3d-993326af6ea6 | -11.20562 | -51.23312 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 478c57a6-816d-3626-b321-a8bb69d679ed | -11.64025 | -46.72953 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98f8dc60-c7d6-3100-9257-9ed5a4502715 | -11.01403 | -45.06944 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d87b605-7cab-3e5f-a26f-5b857d54668c | -8.94579 | -62.40112 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99885214-8375-381b-aa43-8a98c9a22505 | -11.71499 | -54.544 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68411e79-06ee-3e8e-bd5c-3dc7b3571de1 | -14.96253 | -52.59562 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71c7ed2a-4d5b-3796-8cc3-c141b004d412 | -9.163 | -49.9705 | 2026-08-28 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf2ba2a2-39c2-3168-ad01-7d4b76cfa40d | -8.58947 | -54.78254 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ed91aa96-3347-34f0-a734-96e835685492 | -8.82181 | -49.62203 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfa3ce6e-ca3c-376e-b0e1-2050ffe30cab | -9.43817 | -51.68567 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30b5e7b9-5c2b-33cc-addc-b26a3030bfff | -11.82703 | -47.21677 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaeff618-462e-39d5-9ed1-3c93fade1239 | -9.2153 | -51.54945 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15c17e65-3056-3b67-8de1-91ee1811e676 | -11.71205 | -54.53881 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab2677be-3d76-3bdb-9cb8-2fb28acbb41a | -9.34065 | -48.16723 | 2026-08-28 04:51:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e12c44ec-0f20-3138-8fce-06f7c72a3733 | -10.50088 | -64.51787 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 3bc72b0e-ecb8-348c-90d5-58430de91769 | -11.82334 | -47.21618 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a47b18a5-5866-3780-bb52-3667f79b993b | -8.77895 | -50.06627 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 433956ed-7a2e-3bee-a310-a75ae7c196ca | -8.75823 | -44.25005 | 2026-08-28 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3579ffc3-05a2-363d-8a07-ef60afbebf8b | -9.01485 | -40.99196 | 2026-08-28 04:51:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0c8fa608-9b01-3a24-9326-4954c8824f83 | -12.02245 | -47.17337 | 2026-08-28 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7a9f9d1-471f-3254-b778-a8ddc3862158 | -8.94791 | -62.39032 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd088454-da68-3568-8b9b-190fa389e8f9 | -9.43383 | -51.58105 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c61b685-19fa-3d45-8b02-4234a0a41491 | -8.60443 | -54.71741 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3570941d-a5bf-3abf-b91f-3002a2155a83 | -9.22719 | -51.54023 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85771d91-60f4-36dc-a9f3-3f94d234f984 | -11.75393 | -54.51839 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3e67de4-ac5c-3c05-acf6-39359c73e6f5 | -11.21134 | -53.99423 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b06d309-fff0-3e77-ad8b-91239e72cb73 | -10.75494 | -54.04161 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| eea22070-1899-35c6-a09c-30acfdfac26b | -14.86492 | -52.59425 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b78fa9f-d55e-395f-ab6c-2172017fc53d | -11.8227 | -47.22053 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2f0198ea-1672-34c1-baa7-b9cfcf162553 | -10.83074 | -50.5257 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cba9dee-4fbd-3d10-a6f9-40a10fba43f0 | -14.92443 | -52.59648 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e81f53d9-03ea-3868-baf3-b36fa0877ce2 | -8.59033 | -54.77742 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50abdc6e-60cd-3ecc-a31e-8cddbe3bbc7a | -10.78691 | -54.02266 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60467487-0ce9-36c1-8ea0-3631a32dc626 | -12.24726 | -50.57397 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 58f3417b-2344-3df2-a11d-b92202b303f5 | -14.86565 | -52.63211 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c0dc51c-2aec-3c24-8798-094a261b585c | -14.87044 | -52.60274 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29307baa-175c-3d6d-852d-010c18c36861 | -10.79851 | -50.64288 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a80b41e-ed96-3aa7-afbb-6967c365a9ac | -8.55632 | -54.71398 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86b97bb4-052d-30c1-9bc9-81dadbc3e811 | -9.96812 | -53.93973 | 2026-08-28 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a55652eb-94fc-3052-b86a-41858255d573 | -12.28828 | -50.59516 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87b22fec-6648-3598-a203-169fcdddef22 | -11.24227 | -47.06306 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 072194f9-b8ad-326d-b597-e85f15002420 | -14.42417 | -53.3783 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0857a54c-497b-3e47-8645-cfd59e964637 | -8.60051 | -54.78963 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ec6fe8c-e13e-30ff-8a86-fd81a5eee39c | -13.59602 | -45.77437 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a70ce265-47b8-34be-8a3d-d3c44836ac08 | -8.56073 | -54.90515 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6098fe75-da70-3311-94db-0220042bf7b0 | -14.18688 | -52.82734 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30c0095e-51cb-3bc3-ad65-65bba2058646 | -11.29046 | -54.03261 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 819c7659-9417-3079-82f6-1ffd0d825ac6 | -14.98818 | -52.60756 | 2026-08-28 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7cd9348-95e8-3875-9c89-a646cffb9a33 | -11.47045 | -46.94356 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26109ea6-a947-35b7-a84d-9786ebd8f41b | -9.43325 | -51.58466 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d166204-7f60-3f72-96e1-8b36dddd15b7 | -10.32354 | -49.96929 | 2026-08-28 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cf201d7-f69f-3eda-826c-ac436995f483 | -14.93327 | -52.60566 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42ad48fa-d40e-388c-b1ba-57e281d40dfe | -8.60221 | -54.77944 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6012724-e7d1-31b2-ac82-6eb77fc30e9c | -11.20839 | -51.23721 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| cafed4c4-face-31e6-af1a-336e3e57b00a | -14.8744 | -52.59965 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4537f64-291f-3356-a366-2415cb04c7c8 | -8.59768 | -54.75782 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62904088-62de-3d2d-9fed-70a981ca2a17 | -13.47047 | -57.04374 | 2026-08-28 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12ad2d14-26c5-39b2-b462-a94ecc67f492 | -7.70865 | -55.37189 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1331f9c9-846c-3758-abea-02d2ef80f5ce | -9.61211 | -55.12042 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3197e4bd-5c16-3239-9170-3ed7e0bc3db1 | -11.19563 | -51.23147 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 46c323e8-3144-3b1d-9d88-af34e48beb9b | -10.5374 | -50.77668 | 2026-08-28 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa76c3f3-0858-3253-bd87-d6d268b04d1b | -12.26389 | -50.57668 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 8ba3f2b8-9fb0-3ae9-a344-47b296a36c24 | -10.76598 | -54.04351 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8c9289e4-7022-3695-8008-0effd6bf267d | -7.51302 | -61.39033 | 2026-08-28 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f57323e5-b7a0-382e-ab32-af1b0ca8caa8 | -11.15905 | -51.20367 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a661d895-8766-31e0-b705-d45535f82192 | -8.94898 | -62.38489 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39485c91-58c6-3b62-9b7e-3a5638607a20 | -9.44811 | -51.70985 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7d9cbbb-4683-3df2-81c8-43cbc0c2a3e7 | -9.46404 | -51.69751 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a55d022f-fd5f-3fce-8b4c-1d5fcb661e79 | -10.94806 | -49.58827 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README35.md)
