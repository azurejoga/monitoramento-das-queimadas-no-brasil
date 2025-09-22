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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59330fdb-6cf5-349a-9bdb-d5b52f1fc411 | -8.46144 | -44.78112 | 2025-09-22 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 164.9 |
| aeba1751-f95e-34d7-8536-0996baf95c46 | -12.07957 | -44.80538 | 2025-09-22 12:36:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 19602479-61fb-3822-ae60-b61e5bda2f79 | -12.4438 | -45.08482 | 2025-09-22 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 294f4370-e1f8-3b76-9e5a-8006aceb3e65 | -8.27967 | -44.38052 | 2025-09-22 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| cea29e3d-1f7c-372b-b766-67a1ecb39486 | -11.464 | -51.48247 | 2025-09-22 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 56a53749-1d47-3b10-b800-0a6b89e47a26 | -12.08474 | -44.78514 | 2025-09-22 12:36:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 65757ae6-6e16-31ae-9ab1-b6345a7ba0cf | -8.53359 | -44.9354 | 2025-09-22 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 4cd28d1a-7daf-34eb-b31a-1c8f6c83cd49 | -9.31283 | -43.36639 | 2025-09-22 12:36:00 | TERRA_M-T | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 5f91ef36-5f7e-3829-b625-0d575dc7bbdb | -11.39702 | -53.93084 | 2025-09-22 12:36:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 442c4d24-897d-3ba6-86fe-638909ddb21f | -11.11617 | -49.67716 | 2025-09-22 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ef42c15c-4237-3ec4-9821-f60b22ea514a | -8.4544 | -44.77512 | 2025-09-22 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 286.5 |
| 1622be63-7ce4-3965-a99c-6d530c2d850b | -11.07845 | -50.7384 | 2025-09-22 12:36:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 2bb4e138-de5f-386b-bc21-55d097b62e23 | -6.54794 | -55.03828 | 2025-09-22 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f0cb258b-8f12-3ec9-bb95-27583f821fd4 | -7.82276 | -46.1992 | 2025-09-22 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 949c5a00-8ea1-343c-a26c-d0aa03cc2040 | -10.03804 | -49.34604 | 2025-09-22 12:36:00 | TERRA_M-T | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 0cfc5074-e002-3fc5-b953-460ff640fc84 | -12.42085 | -45.03168 | 2025-09-22 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| b731c082-4a83-33e6-bf9a-de6415c7846f | -11.6378 | -52.85404 | 2025-09-22 12:36:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 24d376ce-2f2b-3758-9727-baea6eb7fcf7 | -6.46806 | -45.68327 | 2025-09-22 12:36:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 81fe86af-79a2-3f80-9e44-bf69590bc928 | -10.41375 | -53.46955 | 2025-09-22 12:36:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4dda718a-a795-3bd2-bca4-35b1cf4483d8 | -12.41732 | -45.02596 | 2025-09-22 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| aa0ff1c0-98ac-3b31-b4d7-8f8e757e6481 | -11.13882 | -53.93093 | 2025-09-22 12:36:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 26960086-5913-3e55-863d-ae7800b94d3f | -11.23156 | -49.59166 | 2025-09-22 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 77ad2f2f-3765-388d-bda5-232cdf3af025 | -11.20957 | -49.59365 | 2025-09-22 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 34261c45-b22a-344b-9f1a-54de02a62bbd | -8.44763 | -44.7804 | 2025-09-22 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 3289ae05-a935-31e5-8353-6d672eab3c32 | -8.53962 | -44.92936 | 2025-09-22 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 3b178d8d-381b-33a5-ad84-52360797a725 | -11.65031 | -44.33553 | 2025-09-22 12:36:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 6ce657ee-daa6-368d-bf42-1d932af1eb58 | -8.50318 | -44.66882 | 2025-09-22 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 2d5691c4-cc28-3bd7-87d8-0d9a02fb6f92 | -11.08768 | -50.73967 | 2025-09-22 12:36:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 951b83cf-a2c1-31db-be71-56f585be9184 | -11.08634 | -50.74945 | 2025-09-22 12:36:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| f1619d6c-0453-3e34-ba37-46cca2393ebd | -10.99315 | -54.16537 | 2025-09-22 12:36:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e054948f-9d46-3f8b-bb27-898e06044216 | -8.45735 | -44.75224 | 2025-09-22 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 6f73b428-1a34-302a-9aaa-a146512a6a86 | -12.98639 | -46.36814 | 2025-09-22 12:38:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| e9c36e65-88aa-3d76-945a-6df136bb4b22 | -14.98176 | -44.38726 | 2025-09-22 12:38:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d586f53f-673d-3c85-982a-fd0952d1eb52 | -13.92931 | -44.07148 | 2025-09-22 12:38:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| e89f1a35-02db-3495-88f2-04ffbbb5a006 | -13.44452 | -45.88578 | 2025-09-22 12:38:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| dcba8714-a28c-336d-8eb6-21648d1613af | -12.98389 | -46.38887 | 2025-09-22 12:38:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 2d057d06-1f68-39fc-a212-b2071fe6f6db | -15.84137 | -59.51008 | 2025-09-22 12:38:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 59993eb3-7b4e-3620-b895-b56cde593102 | -13.30821 | -51.06362 | 2025-09-22 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 68495ba3-18d5-3af6-b13b-cf25ec9639e4 | -12.98521 | -46.37345 | 2025-09-22 12:38:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e45daf2b-c108-3780-9d35-c38bbae94d61 | -11.78271 | -54.25206 | 2025-09-22 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| aa13634e-5050-38cb-b6ec-b50d04613c5a | -14.61159 | -43.52112 | 2025-09-22 12:38:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 3af7c6a8-ebb9-3593-924b-773971754bd3 | -15.03487 | -55.26374 | 2025-09-22 12:38:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 4d1f03eb-239a-38a6-8b4b-3b62bc2a5971 | -14.61755 | -43.52703 | 2025-09-22 12:38:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4c90aa86-7645-399e-b37f-c5b244ec2adb | -19.13799 | -45.47371 | 2025-09-22 12:38:00 | TERRA_M-T | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 8f79d6d0-2746-3071-8d20-2297631522a4 | -14.8527 | -45.47277 | 2025-09-22 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 9f1d49a2-d73b-3b0a-b204-e860f46ad9fe | -14.97851 | -44.41879 | 2025-09-22 12:38:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 31d0d092-03e4-37d6-96d5-8625b8f3b6e0 | -14.46636 | -44.84168 | 2025-09-22 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 085fc271-220d-3704-93e9-a08bcc5bb8f5 | -12.98284 | -46.39445 | 2025-09-22 12:38:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 974f7654-3c2c-37db-8ed2-2a467d77a8c9 | -15.03181 | -55.28368 | 2025-09-22 12:38:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 13dbea1c-83db-3a75-868b-4b98128e5f3c | -14.84942 | -45.4657 | 2025-09-22 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| cc3316df-1416-3295-b68b-77cab7b83a91 | -14.46561 | -44.84725 | 2025-09-22 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 0b124aff-63d0-353a-9da4-13ab7f21a466 | -15.02567 | -55.2622 | 2025-09-22 12:38:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 166e59b9-6fc5-370e-b48c-0db6dc41dc58 | -17.56497 | -44.92278 | 2025-09-22 12:38:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 75fe18d4-57df-3cbb-9dba-b79181156133 | -16.4701 | -55.11507 | 2025-09-22 12:38:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 8703e9be-7864-3d6e-a23e-ef9f18554520 | -11.78414 | -54.24253 | 2025-09-22 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c814b06a-e82b-3e9f-bf98-de36e04b6909 | -12.4353 | -45.1515 | 2025-09-22 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| daaaf064-eaac-37f7-a146-219013a6a48b | -14.9895 | -44.4022 | 2025-09-22 12:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b0b196e4-1e50-3d59-a6a8-9ce86b24fab9 | -12.4357 | -45.1284 | 2025-09-22 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| af911fb0-1360-3c32-92ee-53c7ddbe2eb8 | -12.4361 | -45.1052 | 2025-09-22 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 93b71017-ff20-3d7d-affb-49203bdfe921 | -12.4554 | -45.1022 | 2025-09-22 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.2 |
| fb1c1eda-f1d8-3870-8cae-11bd386d0a11 | -11.8814 | -64.9323 | 2025-09-22 12:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 42da0e23-9633-3ed9-bbc3-469320ebb64e | -11.6442 | -44.3434 | 2025-09-22 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 78138ce3-be1a-3eaf-b477-1c486887f843 | -8.2803 | -44.3801 | 2025-09-22 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| b8e6e57e-1c57-380f-a6dc-4ca6fa3f511a | -11.6446 | -44.32 | 2025-09-22 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| aa259c7c-331b-36b9-b929-69e881451f97 | -12.455 | -45.1254 | 2025-09-22 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d74d1402-bfcd-392e-a31f-52f0a8a77d79 | -12.4545 | -45.1486 | 2025-09-22 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ae11624b-e0ab-33a8-a339-cece779633cf | -8.5185 | -44.9291 | 2025-09-22 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| bfcb8c53-5ae2-384a-9d33-f42063852ae1 | -20.94784 | -51.82293 | 2025-09-22 12:40:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8d6fe140-201a-35ac-909f-c7596a88a675 | -19.88557 | -50.85517 | 2025-09-22 12:40:00 | TERRA_M-T | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| fe420fdd-8ace-3649-b05d-7c87a98aa1f0 | -19.89252 | -52.96017 | 2025-09-22 12:40:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 367143c7-90d1-36b7-9a3d-f4ee52f8e5be | -19.8834 | -52.95886 | 2025-09-22 12:40:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e445d383-c5b1-3dad-9e70-704afef184e6 | -20.94641 | -51.83439 | 2025-09-22 12:40:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f695be0c-55a8-348f-8ce1-6a1046755e01 | -19.89119 | -52.97009 | 2025-09-22 12:40:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d1a4e0a7-0b49-368a-8f08-153b7b5e7764 | -19.88207 | -52.9688 | 2025-09-22 12:40:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 27bc12c3-40b0-356c-be9d-4c20392e2ede | -30.39955 | -56.23478 | 2025-09-22 12:44:00 | TERRA_M-T | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 6.7 |
| 1f4a6a24-7311-3750-b559-548b4bb462ae | -5.5773 | -42.1255 | 2025-09-22 12:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 84028756-d45a-3042-9a89-de890983fec3 | -12.4357 | -45.1284 | 2025-09-22 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| dbd8d2ed-7184-3c4a-9e45-eb5339f7a9de | -12.455 | -45.1254 | 2025-09-22 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| cb87a7c2-67f4-372e-95b9-02a73cb62f9b | -11.6446 | -44.32 | 2025-09-22 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 41291c1f-b84a-3144-b23c-a39043eecc9b | -8.5185 | -44.9291 | 2025-09-22 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8aff5cef-b37b-319b-8b8c-698d577291b1 | -12.4353 | -45.1515 | 2025-09-22 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 8179b494-f903-39b6-8e99-ad2223e95e7a | -12.7153 | -47.6972 | 2025-09-22 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 3513d854-f8a7-3d38-8ea7-3a2a6300ee7a | -11.6442 | -44.3434 | 2025-09-22 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| a154fd06-f3d0-354e-a589-f2c9f983b640 | -15.9594 | -59.3687 | 2025-09-22 12:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 12a93093-02d1-33be-99d5-76316a093371 | -8.2803 | -44.3801 | 2025-09-22 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 0bdf936a-6c97-386e-878e-31f84bcd4aaa | -11.2115 | -46.1748 | 2025-09-22 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b1a49fb9-afb0-3c60-816a-9eab7d6c0593 | -11.8814 | -64.9323 | 2025-09-22 12:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0a06a54e-9aa7-3167-b29d-5bdd21fc2227 | -12.4554 | -45.1022 | 2025-09-22 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 99c7fc46-8aea-3f67-8927-ad41a93845e5 | -14.9895 | -44.4022 | 2025-09-22 12:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 6b4a81ec-b0b8-3041-9571-dcb39fb52ae1 | -12.4357 | -45.1284 | 2025-09-22 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 04c6331d-8018-3d2b-95b0-9539f0214a60 | -11.6442 | -44.3434 | 2025-09-22 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| c1650410-45d4-3c04-abac-7684554175b6 | -14.4526 | -44.8568 | 2025-09-22 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c7c7e5f1-e38c-3cf7-b8ce-db59950812b1 | -12.4361 | -45.1052 | 2025-09-22 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| d49656b5-8819-3da4-9d8b-7b84c0be04e7 | -12.7153 | -47.6972 | 2025-09-22 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 0794e2b8-eee5-3816-8839-b62e2a1f8e38 | -15.9594 | -59.3687 | 2025-09-22 13:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 160.7 |
| ec398066-2885-31e0-898f-98cfa42ce8d9 | -14.4917 | -44.8496 | 2025-09-22 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| bd441b51-270e-3287-9594-a743b25ace46 | -11.467 | -43.5485 | 2025-09-22 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 885ce4ad-b116-3522-8c5d-488892c83f60 | -5.5773 | -42.1255 | 2025-09-22 13:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 0de21109-cd12-3619-8931-22ed7be9a17a | -11.2153 | -49.6008 | 2025-09-22 13:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 9102a956-91f7-36b8-b7a2-912af2bcecdd | -12.455 | -45.1254 | 2025-09-22 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |


[Clique aqui para ver as próximas entradas](README45.md)
