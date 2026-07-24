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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c03fdc8e-abdf-30f7-b570-284c06d831ae | -2.90385 | -40.39377 | 2026-07-24 04:23:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 52760029-71be-3e44-be9a-2d7691c09e32 | -3.52975 | -42.69891 | 2026-07-24 04:23:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3abfe81d-4d8d-3ebc-be02-66c49dead8ac | -3.99475 | -43.28279 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fae39ec4-f545-3192-b573-0653c2324fbb | -3.523 | -42.69786 | 2026-07-24 04:23:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c8dc6e0a-3b73-3736-a095-faa3b4f99349 | -4.77247 | -41.79754 | 2026-07-24 04:23:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ffa14c1b-f784-360e-b956-708a2f9e529b | -5.48818 | -45.12029 | 2026-07-24 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f52f58b6-bded-32cd-82a6-10aca6817954 | -6.4863 | -43.78895 | 2026-07-24 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3916a6d5-037d-3ab4-9e54-c3c18fc8aa8f | -2.80647 | -48.24118 | 2026-07-24 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36d250f6-4ba5-32f3-82e6-0137826ef560 | -4.77321 | -41.79123 | 2026-07-24 04:23:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4ed62db2-4821-3c3b-84a6-9ca26cbf5e0d | -4.16115 | -43.08413 | 2026-07-24 04:23:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26ba4970-e94b-3367-92fe-80d2e31bf6dc | -2.8196 | -52.28952 | 2026-07-24 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76e3db6e-1937-3246-a6c9-37813d59ae75 | -4.0126 | -43.27446 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fc75298-78bb-3a8e-bfe9-f65bbc89cffc | -3.52638 | -42.69839 | 2026-07-24 04:23:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1efbde7-7c81-3095-a4d0-f3d6224d1567 | -4.77307 | -41.79359 | 2026-07-24 04:23:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f5f639ed-1a5f-3d15-9b8f-afa44eaa57eb | -2.90687 | -40.39872 | 2026-07-24 04:23:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| faf69f7d-18fa-3c07-b095-cb346f737851 | -5.61713 | -45.9753 | 2026-07-24 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edb85fed-c2c1-3b23-bf2c-aa5376a6edb4 | -2.76783 | -48.57697 | 2026-07-24 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39740ef3-8df6-36e9-a4f3-19e90a00a6bd | -4.3712 | -47.76466 | 2026-07-24 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 29284937-f0ed-34dc-878b-8e3f8356452d | -2.90755 | -40.39435 | 2026-07-24 04:23:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3f7cc979-2d0a-333e-86c3-2c12927c6ca5 | -5.80686 | -43.636 | 2026-07-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 161a0cca-e60b-3e7e-9a1f-67856868559a | -5.62105 | -45.97229 | 2026-07-24 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e658e3fc-95ca-36d7-8066-a43e2f97f754 | -5.63242 | -47.10408 | 2026-07-24 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3860892a-9f98-3029-a1c6-5af7210c8554 | -6.48685 | -43.78542 | 2026-07-24 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b86716fd-cad5-381f-9393-6f1242380d4c | -5.79417 | -48.02443 | 2026-07-24 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 077db8c2-f206-350a-a7dc-8c5aa541c565 | -6.13873 | -44.94067 | 2026-07-24 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9baa4ee-d554-3bf5-a954-d5146cf0b54f | -4.01429 | -43.2855 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1a6484e-30d8-35d6-8a1b-f9345fb61857 | -5.62048 | -45.97585 | 2026-07-24 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dee03bb-e4a9-3ba2-b302-1ded0f54217b | -4.0376 | -43.26756 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f08842ee-3988-33f0-8368-3fd1181abb39 | -6.26854 | -46.3583 | 2026-07-24 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a9cf17a-548c-3e09-82e7-dcab3c730c9f | -6.26795 | -46.36192 | 2026-07-24 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dc9e4da-960b-35a8-b50f-c5bba884395a | -6.13543 | -44.94014 | 2026-07-24 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba3d24b6-5efe-3f3a-97fa-9ab5cb06e20b | -4.01539 | -43.27848 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfbde3f4-527b-3c9b-a2d1-615ef1147f81 | -4.91705 | -43.4657 | 2026-07-24 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28241ed6-8527-30a0-961d-f3937443c93e | -2.8146 | -52.28855 | 2026-07-24 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b4735d-0370-3371-8b33-f4db32e8e857 | -4.93956 | -45.27831 | 2026-07-24 04:23:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cb2d92b2-72fb-376f-a9bb-9463176596ed | -5.31985 | -43.56058 | 2026-07-24 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed59b45a-dda9-3389-8551-fa339dba52db | -4.01205 | -43.27797 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fc19d25-a0ab-3877-8aa1-f2a4ddb578f5 | -4.43361 | -40.92423 | 2026-07-24 04:23:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 683e9e76-cb38-3019-9106-309ba9d06bbc | -4.01594 | -43.27497 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7534ab5e-db6b-39d5-acab-faa215f37729 | -5.59681 | -44.90733 | 2026-07-24 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e01f6316-cf7c-3f6e-9d84-16d3ce917f50 | -3.41865 | -43.16465 | 2026-07-24 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc382ef2-86aa-3175-afdc-93b5ef74e6a9 | -3.41484 | -49.11595 | 2026-07-24 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56f427de-1c48-320e-8187-6a83937bb839 | -3.52581 | -42.70197 | 2026-07-24 04:23:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22346e04-ca49-3c41-a102-d535e99242cc | -5.80631 | -43.63954 | 2026-07-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29b2e272-4d93-32c5-93e1-ef6e46cbeb1d | -5.44116 | -46.28702 | 2026-07-24 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ddf70ee-972c-38ef-a180-3be49806c6c6 | -4.01151 | -43.28148 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7317a876-4db0-309b-820d-e53961066d9e | -9.90165 | -47.87614 | 2026-07-24 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1d3e6e5-1127-3141-85a1-90c4281de201 | -7.01218 | -45.43102 | 2026-07-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a905fdd3-9767-37ff-97f9-cee08762baa0 | -7.83173 | -47.10537 | 2026-07-24 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14732a16-566a-39b0-b28b-150854ad4e3b | -7.14492 | -48.68023 | 2026-07-24 04:25:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7127021-f83a-386f-ac8a-0cfdc2f0ab5b | -7.14565 | -48.67578 | 2026-07-24 04:25:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1b7cc77-13e7-3d9c-9d30-0dddbd7ea6ea | -10.55824 | -48.02562 | 2026-07-24 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4d2fa3e-c4fc-312b-b48a-c6ee85c38fa0 | -6.56477 | -55.15088 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6ea54ea6-c728-3ca4-ae48-5f7fc3d7545f | -9.16698 | -58.30944 | 2026-07-24 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b50db4f1-fa85-3a43-adf3-32fb4ce676c7 | -12.66779 | -48.19872 | 2026-07-24 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8558169e-9574-3867-83da-3107d8aeae7b | -9.16232 | -58.33328 | 2026-07-24 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c73895c-cffc-3946-b0a7-94c651a778db | -11.59372 | -48.0284 | 2026-07-24 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d36fbb85-2f55-3aa5-b1d3-e6ca37fee0d1 | -7.01439 | -45.43849 | 2026-07-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b55acb83-0840-3939-8d8c-f805c26e7e82 | -6.57048 | -55.15189 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a24e349-7185-3130-9420-95f59be30603 | -7.00556 | -45.42996 | 2026-07-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c4e05b7-3fce-39b5-a6f8-5b04b09258be | -8.83348 | -47.076 | 2026-07-24 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 038e756d-2a70-30a8-94e6-9560da59080f | -12.9813 | -44.93242 | 2026-07-24 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07144131-8819-3f80-88ed-81182c31d5f2 | -12.46424 | -49.45777 | 2026-07-24 04:25:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4262b526-604b-3af5-9d52-6bdee6cad145 | -11.37858 | -47.46132 | 2026-07-24 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9069edb3-fbf4-3da1-a659-df67d94ce73a | -6.57279 | -55.14809 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 316a276e-7c65-3730-9365-53b6e59fc689 | -9.15569 | -58.33193 | 2026-07-24 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 320c7602-20c4-3493-9210-0908d2ff637c | -8.83288 | -47.07967 | 2026-07-24 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c5c4662-d27e-3b89-9ec5-ab00b80ce994 | -11.36345 | -46.9299 | 2026-07-24 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90c0e495-10ac-3fd4-95ca-fd12459a1759 | -11.373 | -47.46478 | 2026-07-24 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db374d6e-0f9d-3ed5-943a-b2c89ab4bedc | -9.17248 | -58.31657 | 2026-07-24 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9800b1d2-d188-3f31-bc04-134a1db3445d | -8.70974 | -54.54529 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 182a300b-d630-321d-8920-9b812221e67d | -9.1635 | -58.32727 | 2026-07-24 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c3d89d8-b7b7-34af-a5b1-1116120d7bbf | -11.37696 | -47.46168 | 2026-07-24 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 937bb84b-da5d-3eb7-9a8b-9644606a0529 | -10.55217 | -48.04078 | 2026-07-24 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80138b92-91e1-3ffc-8dd6-f4543916570a | -11.59574 | -58.51445 | 2026-07-24 04:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20bb5d20-510f-3090-b24a-697e0e6bb895 | -12.18713 | -40.40749 | 2026-07-24 04:25:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9feda08c-a954-335a-a7d9-fdb69fb92424 | -8.71033 | -54.542 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ed4336e-cad5-37bf-8b44-5b77317fa45b | -12.49898 | -48.26357 | 2026-07-24 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af4bfb3e-71aa-3e29-ad78-c4f13a0c5dc1 | -14.23418 | -42.7687 | 2026-07-24 04:25:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1074315c-cb8e-3497-8457-89b5482b2e80 | -10.6954 | -50.37162 | 2026-07-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b6007db-6e55-323b-bbf1-be91f9312f0f | -11.62006 | -50.15168 | 2026-07-24 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b054e33-b13d-3014-a3fd-3cfb327fde97 | -7.01163 | -45.4345 | 2026-07-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 623b8335-991d-3d11-a59d-6a8730acf4cf | -7.30223 | -47.01669 | 2026-07-24 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2afcd1b-ca79-327c-9df8-82ce7cdaa76e | -10.69925 | -49.61066 | 2026-07-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14a96bd7-11b5-3b16-bc0d-22a2dda1736c | -12.04069 | -47.32903 | 2026-07-24 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e541df7-9193-3d2c-8cbc-277943ccac77 | -10.83409 | -49.39528 | 2026-07-24 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b2246e4-1e0b-3fd5-98b4-8347ab272c2f | -11.36288 | -46.93344 | 2026-07-24 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b17c2a22-4cf6-33b0-83dc-c121cec8e4d1 | -8.71563 | -54.54298 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eccc03f8-1ba5-3ccd-b13b-42c889e58365 | -6.57119 | -55.14784 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1cea43e-e3eb-3b27-8a0d-dc4a1dd026e6 | -10.55283 | -48.0368 | 2026-07-24 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 651259f3-2833-3a39-a0f4-705c96971a14 | -11.59687 | -58.50892 | 2026-07-24 04:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fdd26db-bb7a-3985-832a-e777360630fa | -6.288 | -47.70874 | 2026-07-24 04:25:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b278b6f5-9402-3bbb-b35c-dc6457ee828b | -7.01108 | -45.43797 | 2026-07-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 81ed5cc0-dfd7-3d5f-ba20-ddeece0ebf19 | -6.56634 | -55.15109 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0cf6624a-35cd-3f77-aa95-432a31a52950 | -11.54385 | -48.26736 | 2026-07-24 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ca2b71b-1bb2-3843-a3da-e0a223e205dd | -12.66313 | -48.20578 | 2026-07-24 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d34ba834-931d-3679-b921-59e6e9085526 | -7.00887 | -45.4305 | 2026-07-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 54087a4a-c570-33f8-8871-8a5f932ce7a8 | -6.57206 | -55.15211 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad255f83-dd27-33ff-8cf0-ccd347e4a08d | -6.56709 | -55.14705 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0defea20-6f56-3cc4-a449-3885352b368b | -7.81429 | -42.57836 | 2026-07-24 04:25:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README5.md)
