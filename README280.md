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

## Dados Diários - Página 280

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63255b8c-3be8-3059-a23d-e8fc4cc728ef | -5.97144 | -43.87448 | 2026-10-08 16:20:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf24588d-54e0-3dc0-9103-182f5d354db6 | -6.32513 | -35.13836 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| eced4b7f-b2f8-3350-a61f-f61906d46cfd | -8.3724 | -47.65974 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 56a6269d-59f2-39fc-8527-a2cb38d6dbb9 | -7.16824 | -46.51184 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 447d8a97-ad37-35ab-8ec3-9b81d64798ed | -5.75308 | -41.72435 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 2b794380-e6a1-3f86-a1e2-99da609029c2 | -8.22007 | -46.37971 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| acff6da2-6c18-3476-b8a7-7fcdd758f79d | -3.40591 | -42.80613 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 7715b671-d62e-3206-8a02-5cb1c2951b31 | -7.18272 | -52.61555 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| ff854271-80f1-3b41-9769-33045690894a | -7.63906 | -44.37415 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a5a82240-211f-3851-91af-e6f972e977d7 | -6.7496 | -46.89664 | 2026-10-08 16:20:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a8a0a456-fde0-3aae-b4a7-e6b61506a230 | -5.74119 | -53.46263 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c221f281-6048-3ba9-b23b-53d4cbc7e6a1 | -8.32726 | -51.31076 | 2026-10-08 16:20:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 747fd6b4-e537-376b-b1d2-6feb5d733a59 | -8.07222 | -45.60929 | 2026-10-08 16:20:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| ec7f4028-45c0-3556-bc62-7c5be3219e60 | -7.88221 | -44.97091 | 2026-10-08 16:20:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| aeb56ae0-3d36-35f6-9dd8-80e42ffdbcaf | -3.19546 | -42.96458 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 64b71f2c-f02d-36f1-9989-709ce526c53d | -1.40678 | -47.23236 | 2026-10-08 16:20:00 | NPP-375 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6d27e08e-9854-3aba-9fc8-925075213438 | -6.19573 | -51.43288 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f6248c42-a83d-3412-96bd-c91b3085aeda | -2.99009 | -54.08264 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f38cbf36-faa0-3c67-a088-57ee326da8c0 | -4.08947 | -44.12854 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d40e862f-547f-3613-bb09-9250763df570 | -6.27732 | -52.27443 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e1542f38-0521-3331-b59f-f485b474a52a | -3.85766 | -44.12471 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 8f18bf8d-5a80-3847-903d-6d6728817ebd | -6.55504 | -45.36472 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| f24a136a-2c38-3573-9815-bb4ffef07f6c | -6.29724 | -43.869 | 2026-10-08 16:20:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ec1a49d6-b74c-3471-a5b7-a65cffd54ec6 | -3.21275 | -42.95785 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| e2a5c201-ebf1-38b2-84bb-37a10c97d213 | -6.84748 | -41.74611 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| c121d36f-136b-361a-a038-26d5f6677d40 | -7.07111 | -45.37543 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2cb0852-256c-35b2-8176-c1f5901fd367 | -7.20108 | -44.29196 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ef40a81b-07a1-3097-aeb2-eb512446700f | -8.32026 | -50.37965 | 2026-10-08 16:20:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 54cc78ae-d438-3b0f-99f3-7160ee21a575 | -6.46734 | -46.53962 | 2026-10-08 16:20:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e6b0f36d-2e18-35b5-b7a8-421f19f6d640 | -6.21236 | -45.18749 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ee78bf3-af44-32a9-9752-80d36b4d5656 | -6.12902 | -47.93772 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 52b112ec-985a-390e-abcc-c0712d99e2b4 | -5.62236 | -43.06109 | 2026-10-08 16:20:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 37b478fb-fed8-3a64-b087-1f55552d41da | -1.22989 | -49.33906 | 2026-10-08 16:20:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bed445d6-5a66-35bd-8f8e-e151db335b4d | -2.51152 | -46.04928 | 2026-10-08 16:20:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4263588d-c31a-32cd-a0a6-ecade502c5c3 | -4.34984 | -47.76554 | 2026-10-08 16:20:00 | NPP-375 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dbdfd470-bbbe-30f7-9017-9073ce7d3d29 | -6.88367 | -43.70177 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 80caf47e-e2f0-3810-b303-828c774c8b26 | -6.9825 | -45.13355 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3e9fd3c7-419a-3e91-baf0-ab89d80fbbfc | -3.05574 | -53.9257 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cf1b8d4e-9efe-37cf-a153-9e000789205d | -5.70731 | -53.48015 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 42c23c51-39b8-34e6-89fe-70dfcdfc0e9e | -2.83932 | -54.13234 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a9b68c17-6802-388f-8bc5-d4b8d6dd4a05 | -3.007 | -54.0588 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e2379b61-7684-3839-874e-93e1515d2cd5 | -7.39175 | -45.64802 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5487d82-cf03-3468-9af9-ddbc5dc91e5c | -5.88144 | -45.94275 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6f1d81fa-9fa9-3ae1-95e2-85448e67b76f | -5.73506 | -41.77012 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| eb80aaad-8f3d-354f-82ac-1b83e0a33b9b | -2.50724 | -46.04988 | 2026-10-08 16:20:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0523ed06-105a-39a5-ad96-5c8dbf5a6f81 | -6.37048 | -45.80303 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 6551eb72-3224-33ae-9aa2-f95473533e3d | -6.72806 | -41.44757 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6f052fa9-2f64-3d54-b714-a0f9ec9ca639 | -6.97364 | -43.29582 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| aa572537-1d1b-319f-8ac4-0af0d38bbc20 | -5.74792 | -41.64326 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 099245cd-8524-3251-89dc-91b05b74c862 | -6.43425 | -44.84792 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 60156b55-7ab7-36aa-9118-ead2158cd6f6 | -2.05448 | -54.30575 | 2026-10-08 16:20:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 7f728b58-0c17-3768-8a73-eda484899144 | -3.30977 | -53.71083 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 571b1778-56ab-3703-986e-3f340db133ba | -5.09181 | -46.19897 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 66e2e462-0b8c-3b12-8ac9-3cdf8a5d43ec | -1.19933 | -48.92822 | 2026-10-08 16:20:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 809b0979-0617-339e-a6e0-0d113b470142 | -2.08623 | -46.58506 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0cc7c028-3444-3acb-bb5e-f88b044388fb | -6.05836 | -44.03312 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 350eebe4-79a0-3320-a99f-6713dbfb3639 | -6.54173 | -45.3962 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c5fb87a1-ddae-3ea7-8e08-e5a1ae4411c3 | -3.5919 | -38.946 | 2026-10-08 16:20:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cdc24a89-0cfa-362c-9ead-5c3ac83d8785 | -6.80042 | -45.05847 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f83153e1-c5fc-3166-a379-f1e0654c2c68 | -6.96073 | -47.66156 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 062d3f14-da2a-30ea-91fd-38fd84694ec0 | -7.47098 | -42.81984 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 74f9ca5d-689f-38ba-b4ab-5bfe7eb9982d | -3.182 | -50.59748 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| e4035f76-0da4-3495-83e9-3f93e0f6b37f | -3.30424 | -43.06601 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f14ec6b3-0420-38c3-947b-626c58fe1857 | -6.76369 | -43.70149 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e1543e9a-1d16-34bf-bf20-f0aed9b1a042 | -6.06923 | -44.64882 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7e4162d5-f34a-3bec-aa57-2d0b028fee10 | -5.77758 | -42.05423 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| dd9e55dc-38f7-3618-a66b-d8b2d80091f0 | -6.93423 | -45.26013 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e4bc7d81-3d62-383f-bff4-de392b99d1a8 | -6.17128 | -46.0191 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 6f7dd4bd-23cd-3a60-921c-17192f24dc86 | -6.35948 | -42.91222 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9e177274-0dfe-32e2-9216-82222d52bd8a | -7.25344 | -39.40849 | 2026-10-08 16:20:00 | NPP-375 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 96bde44b-fdff-312d-a693-900cca2bd4a4 | -3.09505 | -53.94232 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| b62d4fa6-77d6-3caf-a9d6-1c78c6c0f67c | -6.1517 | -47.94976 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c891fbe3-4a19-380f-a4d1-f58bc0515138 | -5.87503 | -45.96199 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 03f54204-62b3-3ec1-a81b-281a0f6bc301 | -5.28259 | -47.91562 | 2026-10-08 16:20:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a32eaac1-e2f9-3707-b8c7-74053cb82dcf | -7.47111 | -42.84731 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 5dbe5a51-9ddc-3089-ad96-985f18bf44cf | -3.25681 | -45.09462 | 2026-10-08 16:20:00 | NPP-375 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ce8db683-ef99-3f57-9f12-acf68d730ec7 | -3.09221 | -53.96328 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 603288b9-d519-35a9-9414-761a4a99447d | -6.22559 | -44.85831 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 23a9040f-18f8-3d9b-aa58-acb6f6dca5f7 | -3.25523 | -43.87569 | 2026-10-08 16:20:00 | NPP-375 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 60956cf4-05d9-351a-ac27-f4fb86269457 | -1.40061 | -48.94696 | 2026-10-08 16:20:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11381d70-cc4e-35a0-90e3-4d3a5dcee96b | -7.57822 | -46.70139 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 21fd897f-447f-3ae3-b1d1-e66917cc37e6 | -3.89328 | -38.66225 | 2026-10-08 16:20:00 | NPP-375 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ed9e50f8-ab20-3102-b5e4-86b904e1f30a | -5.37259 | -44.19773 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 17d2210f-27a8-36c7-8949-f62af62911fb | -5.50205 | -42.85212 | 2026-10-08 16:20:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| ef32fd76-9a18-3ce9-a557-19d18aae78ba | -4.08737 | -44.11417 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| fe962abd-4a92-38d1-b1f7-d87fc3f32bdd | -6.32805 | -43.35399 | 2026-10-08 16:20:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c8ab87cc-cea2-3e07-9df5-b5309dc60098 | -8.19002 | -46.37331 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 6a04456a-11dc-3a31-b8ae-f554e90638f8 | -5.16744 | -45.33382 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfc45e40-f6c0-36d7-9ae2-2d93e2cd7a84 | -6.85098 | -41.74567 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 07e7a295-f923-31a6-b934-0c54a2fc9032 | -5.93954 | -44.32458 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9ba54373-b4a1-326f-b1d8-ac62ed46d0e6 | -3.15001 | -43.03714 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f7b8c935-1618-348b-ab8d-8bd3039c9d03 | -4.79597 | -43.33319 | 2026-10-08 16:20:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d25f9b76-dc0b-36ae-bc4f-b30e372fd705 | -5.7076 | -53.48721 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 019b7e2f-e95b-3108-a2bc-7bab0b6b040c | -6.17891 | -44.95361 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b0e30b54-54b6-39d9-b53f-35b064c04965 | -5.45506 | -45.59103 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bc5b8765-3408-382c-a3e3-9f114fcf4aea | -7.24959 | -39.40552 | 2026-10-08 16:20:00 | NPP-375 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 1e1e036e-3fac-305c-be58-7dd7178d74c3 | -6.19571 | -37.86048 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 4805eacb-fd06-31b7-a891-369fa40512ca | -6.31592 | -35.1544 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 5c99aaf7-7c86-32d5-b181-cef60a6f90bb | -7.85737 | -45.15123 | 2026-10-08 16:20:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| fea074d3-21df-3095-aec1-48b0c8ef37d4 | -5.7467 | -41.72921 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 431.5 |


[Clique aqui para ver as próximas entradas](README281.md)
