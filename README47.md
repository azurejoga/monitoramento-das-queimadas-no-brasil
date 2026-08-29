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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c768d53-d2a1-316a-86f9-ee2829f4574a | -6.40877 | -51.6725 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a61eba7-a95d-3b77-a3e8-171a264a10d1 | -11.02984 | -57.21722 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed2490e3-26ad-3f39-9649-0d61ab69227e | -6.95216 | -58.95601 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3cf76acc-856a-3f5d-8e6b-362b27032e0c | -7.12006 | -43.16532 | 2026-08-29 04:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9b757dba-f342-382a-a2b5-0f55ff67b3d4 | -6.7581 | -55.65391 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ca8098a8-8d4f-3ec3-b738-cc19d0edb787 | -11.62876 | -54.58703 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 407594ad-1030-3790-92ba-7174c02630e0 | -6.15728 | -57.79234 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 785daea0-e176-3229-bcc9-8d4f5631e975 | -11.62187 | -54.58584 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c37d0637-15a3-396e-94e4-daa2b70ff976 | -6.50741 | -53.60286 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e36c8798-b6bd-3273-b8c4-05da7b026be6 | -11.76695 | -54.5158 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df688332-84c6-385e-a981-2b7221ebcba6 | -8.01441 | -48.0123 | 2026-08-29 04:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a43909fa-da08-32bd-af03-79887097d9aa | -5.98361 | -57.67592 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf187869-c66e-34d5-a86d-11e0e419ad40 | -6.42419 | -55.52486 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40a39c66-cf8a-3f91-b43c-72469ad0e235 | -9.66236 | -55.08723 | 2026-08-29 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0e15534-9c5b-3bd8-9109-6c1b6439f72a | -7.2833 | -45.85659 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fb30f445-05e7-30e3-b90c-7178da29cc3f | -18.02589 | -49.20165 | 2026-08-29 04:53:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a813b46-887b-3b12-8fdd-134ee6b27411 | -6.581 | -55.43823 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 591ab81a-44c8-3cfa-bbfc-c8a28ab3c970 | -9.47065 | -48.20846 | 2026-08-29 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 60721428-d9b5-39cf-bc3e-8067428c66cd | -11.01151 | -49.67648 | 2026-08-29 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5c86e0a-cec1-3fe1-ba02-5f6c4d3e5435 | -9.40328 | -51.6172 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7689754b-6c84-3063-a84b-05133fc3014a | -10.56666 | -59.6154 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5480701-b1e2-3091-a38e-c2d62d9d4094 | -7.50937 | -55.29334 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 997054ff-f053-3813-ac1f-00eb7ea407b6 | -6.16469 | -57.8027 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 289a1cd5-f0a8-35c1-a190-3830e5de43e1 | -9.22006 | -59.7627 | 2026-08-29 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebf91fdb-e8f9-31da-9f72-c8e40106f6f8 | -11.26549 | -54.02485 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb036933-2936-3900-9d9d-ea8fcc2c3d0d | -13.31898 | -48.19271 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62009fad-75f8-32a5-8431-f9a6da6c0f34 | -13.66803 | -47.75177 | 2026-08-29 04:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4a5a239-2c7b-3a17-9f27-5c3e0130c688 | -6.48903 | -49.90861 | 2026-08-29 04:53:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c978def-dd55-337e-96e9-af354c8e3238 | -9.26241 | -45.64138 | 2026-08-29 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fab01b65-aead-39b1-866b-280392d70235 | -10.74984 | -54.00082 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f85a742e-b183-3985-821e-4e017b36f9e9 | -7.29824 | -49.97019 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80fa4c10-92ab-3d6f-94c6-e0d00b07e9d3 | -11.72067 | -54.53915 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d6d578b-e43c-32b2-b60c-69e6ca73a435 | -7.53206 | -44.45535 | 2026-08-29 04:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 830217f5-16de-3efd-847d-d5fe19824e49 | -10.80368 | -54.01367 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f513d7e-7d87-3b13-a045-ac33d4587eea | -8.53052 | -55.26257 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fd79cb7-3422-33a8-933b-1010d42b1266 | -11.37055 | -45.13721 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b983be9a-02b7-393b-a257-ef6120405642 | -11.02909 | -49.6792 | 2026-08-29 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c3f7a1e-5dec-3914-b643-8a6bee6d3cb6 | -11.03963 | -57.20826 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59258a16-69b1-339a-ab6e-4f48b7631636 | -11.02642 | -57.22566 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d890fd8c-5ed7-303d-91ad-b6221d0631c3 | -8.09528 | -47.60163 | 2026-08-29 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7477f83-c530-38d9-93e1-564fdc486e83 | -20.23022 | -47.39889 | 2026-08-29 04:53:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b1fb416-f2e1-32f3-be8c-4414590bf390 | -13.32727 | -48.19048 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 876bb36d-ad78-3464-a0d4-64978a4c973e | -7.56737 | -61.38497 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7f4bf2e4-6ef4-36b3-b1a9-5bd9865b0037 | -11.24458 | -53.99865 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdf19516-c4ab-3422-b02d-22291a8511ae | -11.22582 | -54.00681 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df31f1b0-27d4-3b12-b8a8-7ba2ec78c426 | -7.28387 | -45.85275 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 17499c27-0f1d-3104-b075-ad9bea928650 | -11.37585 | -45.13293 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94fbdd67-fb19-3601-bbe5-4ca60325cc41 | -8.59364 | -54.72066 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea7ee0b0-b7ce-34e4-8db2-d5ade6af10c4 | -8.01508 | -48.00788 | 2026-08-29 04:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9b36c56a-efc6-3ad8-87cc-34cade8d62ef | -6.32183 | -54.74891 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eea39405-13d8-3410-a748-27dcf6ec68e5 | -5.76765 | -57.56513 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e09ea99-1336-3b7f-b951-5e1ac43d8ece | -6.93307 | -58.95251 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c92053d7-bc23-3288-9075-38c23a9054d3 | -14.07408 | -44.0633 | 2026-08-29 04:53:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54a708e6-0796-32cd-a130-23fdff42677e | -6.77193 | -55.6659 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 046f8620-5a78-3b9d-b8e3-9f15e17546e4 | -8.81783 | -49.6305 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bdb63e5-38fb-3761-b192-8baf53ba6939 | -17.27583 | -46.0184 | 2026-08-29 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9a95eb0-d723-304c-867e-add55a5de74b | -6.4258 | -55.52779 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5f0aa11-df1c-3e37-8a98-557408d36dc7 | -9.86899 | -60.30534 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91642f1c-2613-3ddb-86d1-e6869e57a013 | -9.22816 | -51.56459 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eeaab0a-e4b3-3af7-a64b-42f6e83d7c47 | -12.78574 | -46.4578 | 2026-08-29 04:53:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6acae615-23af-3da5-ae95-bf15282a7f2c | -7.50115 | -55.29659 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e3112ce5-40df-3f5a-97c1-717af38e4ee7 | -6.54294 | -55.24874 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ea5d5eb-8a1c-3eec-9560-2b6787e2dbac | -11.01092 | -49.68046 | 2026-08-29 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed8dad66-c8b1-30ce-98a4-f6b495938e4b | -20.22626 | -47.39345 | 2026-08-29 04:53:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b20fca9-9f5d-325b-97cb-6cb46562bb78 | -9.42369 | -51.59539 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a335abdb-d43a-3984-9ebf-bc9ffa8521ff | -7.95273 | -52.44995 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cc6a3b8-54a3-3174-9d16-91a756342749 | -6.95226 | -59.47468 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| beee34fd-a01f-362b-b3d9-a569fcdab8f2 | -16.47993 | -49.42862 | 2026-08-29 04:53:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b04eaff-72ee-347b-8086-07b480da5b33 | -8.53203 | -55.26993 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a429270c-9326-3a91-b6e1-02e2b91e4248 | -11.02522 | -57.23267 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4ec76f4-d289-3799-9c1a-24a3e46cbb72 | -6.93836 | -58.95104 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f917e084-9085-3ac3-9392-4c0b122d963a | -5.89282 | -57.76227 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 88ffed22-e0d4-3cbf-869b-ade97029ea48 | -11.23561 | -53.9895 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd7b14a9-f7c9-3e94-ae61-e888f329c54f | -11.60254 | -46.73122 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a90b854-811f-3cac-9715-ee02d10184e2 | -9.92238 | -60.43493 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cdc7bff-0668-3e7f-94cd-17bf6bda5b55 | -11.26149 | -54.028 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae09d1d5-9f1b-31f6-af68-3bb91618d77c | -17.61632 | -51.61134 | 2026-08-29 04:53:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a00dbb1f-b740-3346-8db1-d13eb2f502a0 | -8.94245 | -63.27588 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f70e5f30-4d6a-3ead-a0f8-e4ea8ebe5661 | -11.26732 | -54.01376 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bec1a84c-a7c0-34f7-b8e5-8554f7937683 | -6.64576 | -53.17962 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| feabaa52-4d0e-30df-955d-fa64894b6992 | -11.29482 | -54.0374 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c93cee53-c757-35c3-91d7-28b8fdd7c965 | -9.25948 | -57.08019 | 2026-08-29 04:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f43d33e-691d-32f6-a992-13cbd6d06976 | -14.07885 | -44.06195 | 2026-08-29 04:53:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 78eb022f-c9d4-362d-adb2-0a870b7a1d53 | -8.95201 | -50.81192 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edcf7ce4-6914-3e79-a9fe-cba9022df669 | -11.26393 | -54.0132 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 616d27e4-963d-32d3-b6b8-6060f59dce10 | -6.75024 | -58.72774 | 2026-08-29 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70ea6f56-fe92-3b7a-af2b-a8b83f3b238e | -11.62658 | -54.57878 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 601132d7-9f5a-332a-bc43-715c1fe6511c | -9.43747 | -51.57257 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38830d92-33e9-351d-9c54-7785136e31ac | -10.3403 | -49.97673 | 2026-08-29 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0b3e934-0d28-3706-8b59-78c2c45715d7 | -11.22183 | -54.00993 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adc158e7-d118-33ab-a72f-c0e986ae657d | -9.40181 | -55.97528 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16035a90-4c61-3fe4-bfea-70f7b6c56de3 | -6.15125 | -57.8005 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2d10267-da34-36cd-864f-0c34413a471d | -7.36042 | -55.16861 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0873a242-5efc-3aaf-ac2f-de17a1c23d5d | -19.28093 | -49.51748 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e99d8f39-e002-3333-af79-0926910876d8 | -6.16546 | -57.79827 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44fad8c5-e54a-3778-a044-c4e511b1e7b5 | -10.53669 | -50.4789 | 2026-08-29 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d708f88-5e78-355f-9ea9-cbb6f2265830 | -7.4952 | -55.28628 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 466c92d2-4041-3760-aff7-85a90db20537 | -7.591 | -61.34343 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 760092d8-41da-3e67-8fdc-fe41fef8a3bd | -11.24022 | -47.0487 | 2026-08-29 04:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fe1173c-ae6a-3c2e-8343-7c4251f72521 | -6.4266 | -55.52303 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README48.md)
