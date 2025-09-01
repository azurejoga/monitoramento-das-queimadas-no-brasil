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
| 0d527be2-2edc-3a77-b183-e4ff0cd66d13 | -8.86268 | -49.5515 | 2025-09-01 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d13e7e7a-1c24-356e-af5a-488e80bb3d1c | -9.67545 | -47.82418 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddf7cfb9-4ea9-3fa0-9b3b-30ddbdde3b6b | -10.59875 | -44.32887 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| ab402ba5-2059-30af-aaed-d0f1b78d7a60 | -6.15697 | -43.32883 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91ab2f7d-6cd3-3778-b811-e827661ad356 | -7.62419 | -44.03303 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdf1498b-659d-38a1-a80b-1d235f75b806 | -6.92308 | -45.57066 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c77805f7-c4da-321e-842f-c7b28de56ef7 | -10.0368 | -48.07604 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c83d4727-6f94-36ca-a149-1acb48e1d756 | -6.9338 | -42.02254 | 2025-09-01 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f23abf11-a73d-3ee3-86ae-987ca3913d6f | -6.19397 | -53.76278 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bf7798d-5584-33e7-98fc-fc7254339e61 | -7.88034 | -46.99218 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a6f2968-e89e-394c-aaf3-84552245769c | -5.44201 | -42.82847 | 2025-09-01 04:32:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bf4b8e95-d3af-34a4-80c9-dd1cb53a43c5 | -7.10791 | -44.30852 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0924e640-ff0d-3874-b146-ecfea8c93a99 | -9.5017 | -48.84665 | 2025-09-01 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f520433-665d-348f-834c-68fae18e02d2 | -7.0738 | -44.35826 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1fb6c1a-e7a9-3885-a7f5-19880a2323f8 | -6.26718 | -43.55145 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b85a046f-a7cf-3be5-8722-5db7ff6c771e | -7.74113 | -50.2585 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 71eab4fb-0317-33bd-837c-24b883c07d7b | -8.85368 | -52.02726 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a3ff278-047b-354b-bdb5-ff21bd68b50e | -6.51303 | -43.55087 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfe6c478-8074-3dd6-86f0-270847c1d3af | -5.58425 | -46.32527 | 2025-09-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9dd8bd4e-76f3-3a1f-aaa1-0280e72194ba | -6.83727 | -52.82219 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3d40996-5738-34fa-9bfd-1573a215ebca | -9.26975 | -47.11362 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc03c4b2-a93c-3dcf-8c7a-4621d37bfafb | -6.84918 | -52.82418 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12fcea04-0b1b-3f57-b09d-68b143b5b05c | -6.67715 | -44.39147 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba485336-1b38-3f1f-b1d8-7d0d3fa03127 | -7.08896 | -44.3332 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b22e944-e831-3732-8519-5dea322b6c68 | -7.68355 | -61.09998 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c4427aa-ce26-3dd6-9413-dbb86f275f4e | -11.32382 | -43.47313 | 2025-09-01 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 646c8fb7-7b8c-3907-8202-c8384ac3eb33 | -7.71711 | -50.25869 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61bb9703-2566-37bd-b608-e7a3a90167e2 | -10.03957 | -48.08011 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cde6fc27-b22b-36af-b375-4fe49f8db9da | -6.31236 | -43.78791 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72e1473a-b941-39f1-9c60-8d50fd90c40d | -11.08487 | -44.61929 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c47a821-50f2-392c-bdf8-9d2eed7be812 | -7.67496 | -61.08838 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c092ae90-0b3d-3cae-bd25-3dc2a7fcc31d | -7.53617 | -45.03425 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7af39456-51bf-3951-ba50-31b757437e19 | -8.17496 | -45.03593 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecc0dd21-9861-3dae-b829-c2c0d63880a7 | -9.23405 | -48.73551 | 2025-09-01 04:32:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58601791-7dff-3beb-b9b1-92f9962e35f7 | -11.08637 | -44.62202 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 642a9a17-12f5-3f68-9d2d-34c0d8a24c99 | -6.29583 | -43.31013 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96cee60a-5305-3e60-b7fb-668f8b1a7928 | -10.65779 | -47.07956 | 2025-09-01 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f21124c1-ad72-31ca-81c8-1f7804743d93 | -8.87973 | -47.96511 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4c6fb30-89f1-342b-9d83-9f7ca99bf2d3 | -7.76401 | -50.31287 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89c57f09-14cb-3600-b2a9-ac5083dda43c | -6.16061 | -44.12526 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc38edea-c3b0-3c16-88a4-e5b24534dc97 | -4.15178 | -46.78122 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 261b5fec-fff5-37f0-8266-9a0916320e3b | -10.04293 | -48.10238 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8d503d5-fec4-3c8e-9663-0bc2365374a8 | -9.14367 | -45.20269 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 470f7145-9fec-3d10-81ba-dcb7ad0f8c71 | -7.57462 | -45.20688 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 242d0535-d6c1-3674-bf59-ff52dc261ecb | -6.8994 | -51.19385 | 2025-09-01 04:32:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7100c90-5aaf-31a7-8628-e76225487a73 | -11.03577 | -45.14628 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a3402c2c-13dd-337c-9313-bf67ab868ace | -7.4442 | -44.82809 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25b24e57-dda5-3e2f-a415-ebcc4ed2895a | -8.85046 | -45.73427 | 2025-09-01 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 142d8ca1-8fef-3749-9930-74cc8e239f09 | -6.92938 | -44.69791 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d91e09f-83ee-3956-84b3-f15d6602aefa | -6.34142 | -53.43372 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3784e71c-d68a-36ec-9246-f751a3d24c17 | -6.83501 | -52.81129 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 308b053b-c613-3e9b-8b15-c9767bd2d8ba | -9.14306 | -47.95315 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0985f68b-065d-3d7d-82b9-e7422cc87a49 | -6.84037 | -52.82809 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 21adf1de-cb20-337c-88ec-f7be9f33e023 | -6.44394 | -43.96814 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c01a2a76-c23a-3eac-ab7c-726f2afe0467 | -6.54406 | -44.57694 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5e9c2c4-61ce-3018-b6c7-72f24c8459db | -9.15997 | -45.21806 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 24dd7a2b-ff2a-32e3-9784-13c3243de7a7 | -7.97514 | -46.4227 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6abb76c-b708-3d35-84d5-afa7473fd72b | -8.82758 | -47.82038 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83fba6a7-bcb4-3302-b8e0-5950152c7442 | -7.9592 | -46.34416 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 623129ad-6e5a-3913-9b30-640efeac2ab3 | -6.94684 | -42.01032 | 2025-09-01 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b56a023-3bf5-3b59-836d-0badec9b8ece | -7.67019 | -61.09729 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fecb444c-6b7a-3270-8fca-2cc6146a6c4b | -6.49359 | -44.07323 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 361192b4-a97a-3df0-bd8e-981fa0967010 | -6.57326 | -43.70135 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16a3f1f1-09ab-31fb-a0a0-6af50c44f1f1 | -3.59047 | -47.51968 | 2025-09-01 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e028ac9d-c0c3-3f6a-a267-26a66ef74f30 | -7.48391 | -45.99675 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69b76191-93b0-3745-8f73-ac9055be9303 | -7.10417 | -44.30803 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fe577ac-b7e7-30e1-9097-11490d03ceb2 | -5.73427 | -45.53776 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a12885b9-c493-3a23-92ba-12c5414f8c90 | -4.55515 | -46.43666 | 2025-09-01 04:32:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90f35379-420f-33e1-abc6-be0c669e8de7 | -6.33245 | -53.4361 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d949e872-ea65-37cf-8530-e2eb7a47592f | -10.27464 | -49.04992 | 2025-09-01 04:32:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bbd7b5a-f144-33d3-9741-a697a49ba29f | -3.63322 | -49.20253 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8098c50b-89f0-3b17-a6e1-5b3a0166c4ff | -6.57754 | -43.7141 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f72803f-73e0-3787-aa39-e85b87b543d6 | -7.42543 | -47.4285 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef7fe6ff-a0ed-32e1-89f5-115e081561e8 | -7.24852 | -44.0672 | 2025-09-01 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23123f39-e4f4-32dc-8620-76814894d0cc | -9.66655 | -47.81552 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ded18a00-f7e7-3a86-869d-8f8d9fe2750e | -7.55883 | -45.93758 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b3d7207-6fbc-3a99-8be1-f6e3c3c46b2c | -6.74839 | -43.79388 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f69b1c02-8271-3e0f-9926-f155156a9cf7 | -5.73198 | -45.52962 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e208db6e-74d5-3322-b229-a80bb12c9361 | -7.07645 | -44.34056 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35280e8a-356f-3ae4-bc98-65bc28cd3f89 | -8.84518 | -47.50936 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2e1a95a-f858-3841-99e4-676140daed79 | -6.49949 | -45.40968 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daba5609-22f7-30c0-a4a4-f6bb22ed2da5 | -8.824 | -47.49155 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5030961-9bba-3393-830c-6b84d506b2f1 | -9.5797 | -46.00108 | 2025-09-01 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b601b55e-45eb-3562-83ac-7a3136794ecd | -6.24563 | -42.41887 | 2025-09-01 04:32:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a9c5f028-866d-3f96-9c32-f0a1cedb8919 | -6.74287 | -43.77853 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c45f1c47-c8a1-3412-abd6-9fb9dbcf04b2 | -10.02242 | -48.3649 | 2025-09-01 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c351a66-9709-3e87-a05a-da1f6e1834d8 | -8.8447 | -47.79792 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d26266d-3375-3cfc-ae76-21cb3a0ab52a | -7.58471 | -61.63059 | 2025-09-01 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0be1a2c4-c877-365c-98b0-8bdc92b662b3 | -6.85571 | -52.80935 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0cd903e5-65da-34f2-97ea-659bd51f7eaa | -6.28723 | -43.56199 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3bb34a50-b274-33bf-9b68-f69c55c7010c | -6.61546 | -53.12625 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dff740ea-caa7-3415-b17a-0d468dae890f | -7.98084 | -46.43112 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10fd0d81-b3c7-396a-b9ba-51ad8af94bb9 | -7.39028 | -47.43703 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d9ba489-01c7-3969-8f49-cfe7bf4553cf | -6.81337 | -45.69316 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ce681bb-20da-3c8d-a06e-ace831f479fc | -10.04627 | -46.02343 | 2025-09-01 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 191102d7-5f53-3d48-9c91-35f86a7f1122 | -7.07446 | -44.35388 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5f6e762f-e13a-33d9-834d-3c7d6bee9636 | -7.70378 | -50.27573 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec0557e4-0ccd-3627-a46b-f79e8ee17a73 | -8.47535 | -45.17641 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b521f6a5-531e-3ac2-a8a0-ea470afa21da | -8.70453 | -47.86976 | 2025-09-01 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39da9c77-67d8-37ee-b7bd-9e5f853f9065 | -4.90832 | -43.18083 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README51.md)
